"""
RefSeq Sequence Fetcher

Fetches DNA and amino acid sequences for RefSeq transcripts using UCSC API.
Returns data compatible with genome_browser_demo.py.

Author: ClinGen Project
"""

import requests
from dataclasses import dataclass, field
from typing import Optional
import time


# Codon table for translation
CODON_TABLE = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
    'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
}


def reverse_complement(seq: str) -> str:
    """Return reverse complement of DNA sequence."""
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'N': 'N'}
    return ''.join(complement.get(base, 'N') for base in reversed(seq.upper()))


def translate(cds_seq: str) -> str:
    """Translate CDS sequence to protein."""
    protein = []
    for i in range(0, len(cds_seq) - 2, 3):
        codon = cds_seq[i:i+3].upper()
        aa = CODON_TABLE.get(codon, 'X')
        protein.append(aa)
    return ''.join(protein)


@dataclass
class Exon:
    """Represents an exon with genomic coordinates"""
    exon_id: str
    start: int
    end: int
    rank: int  # Position in transcript (1-based)
    phase: int  # Reading frame phase at start (0, 1, or 2; -1 if non-coding)
    end_phase: int


@dataclass
class AminoAcidMapping:
    """Maps an amino acid to its genomic coordinates"""
    amino_acid: str
    position: int  # 1-based position in protein
    codon: str
    genomic_start: int
    genomic_end: int
    exon_id: str


@dataclass
class TranscriptInfo:
    """Complete transcript information"""
    transcript_id: str
    gene_name: str
    chromosome: str
    strand: int  # 1 for forward, -1 for reverse
    start: int
    end: int
    cds_start: Optional[int]
    cds_end: Optional[int]
    exons: list[Exon] = field(default_factory=list)
    cds_sequence: str = ""
    protein_sequence: str = ""


@dataclass
class GenomicRegionData:
    """Complete data for a genomic region ready for visualization"""
    chromosome: str
    start: int
    end: int
    dna_sequence: str
    transcripts: list[TranscriptInfo] = field(default_factory=list)
    amino_acid_mappings: dict[str, list[AminoAcidMapping]] = field(default_factory=dict)


class RefSeqFetcher:
    """
    Fetcher for RefSeq transcripts using UCSC API.
    Returns GenomicRegionData compatible with genome_browser_demo.py.
    """

    def __init__(self, assembly: str = "hg38"):
        self.assembly = assembly
        self.ucsc_api = "https://api.genome.ucsc.edu"
        self.session = requests.Session()
        self._last_request_time = 0
        self._rate_limit_delay = 0.1

    def _request(self, endpoint: str, params: dict = None) -> dict:
        """Make rate-limited request to UCSC API."""
        elapsed = time.time() - self._last_request_time
        if elapsed < self._rate_limit_delay:
            time.sleep(self._rate_limit_delay - elapsed)

        url = f"{self.ucsc_api}{endpoint}"
        response = self.session.get(url, params=params)
        self._last_request_time = time.time()

        if response.status_code != 200:
            raise Exception(f"UCSC API error: {response.status_code} - {response.text}")

        return response.json()

    def _get_dna_sequence(self, chrom: str, start: int, end: int) -> str:
        """Fetch DNA sequence from UCSC."""
        data = self._request("/getData/sequence", {
            "genome": self.assembly,
            "chrom": chrom,
            "start": start,
            "end": end
        })
        return data.get("dna", "").upper()

    def _get_refseq_transcripts(self, chrom: str, start: int, end: int,
                                 track: str = "ncbiRefSeq") -> list[dict]:
        """Fetch RefSeq transcripts from UCSC."""
        data = self._request("/getData/track", {
            "genome": self.assembly,
            "track": track,
            "chrom": chrom,
            "start": start,
            "end": end
        })
        return data.get(track, [])

    def fetch_region(self, chromosome: str, start: int, end: int,
                     transcript_ids: list[str] = None,
                     track: str = "ncbiRefSeq") -> GenomicRegionData:
        """
        Fetch RefSeq data for a genomic region.

        Args:
            chromosome: Chromosome (e.g., "chr20" or "20")
            start: Start position (1-based, will be converted to 0-based for UCSC)
            end: End position (1-based, inclusive)
            transcript_ids: Optional list of specific RefSeq IDs (e.g., ["NM_000022.4"])
            track: UCSC track name ("ncbiRefSeq" or "ncbiRefSeqSelect" for MANE)

        Returns:
            GenomicRegionData compatible with genome_browser_demo.py
        """
        # Normalize chromosome
        chrom = chromosome if chromosome.startswith("chr") else f"chr{chromosome}"

        # Convert 1-based to 0-based for UCSC API
        # User input: 1-based [start, end] inclusive
        # UCSC API: 0-based [start, end) half-open
        ucsc_start = start - 1
        ucsc_end = end

        print(f"Fetching RefSeq data for {chrom}:{start}-{end}...")

        # Get DNA sequence using 0-based coordinates
        dna_sequence = self._get_dna_sequence(chrom, ucsc_start, ucsc_end)

        # Get RefSeq transcripts (UCSC uses 0-based)
        transcripts_raw = self._get_refseq_transcripts(chrom, ucsc_start, ucsc_end, track)

        # Filter by transcript IDs if specified
        if transcript_ids:
            transcripts_raw = [t for t in transcripts_raw if t["name"] in transcript_ids]

        # Filter for protein-coding (NM_) transcripts
        transcripts_raw = [t for t in transcripts_raw if t["name"].startswith("NM_")]

        print(f"Found {len(transcripts_raw)} RefSeq transcripts")

        # Initialize result (store 1-based coordinates for consistency with Ensembl)
        region_data = GenomicRegionData(
            chromosome=chrom,
            start=start,
            end=end,
            dna_sequence=dna_sequence
        )

        # Process each transcript (use 0-based internally for UCSC data)
        for t_raw in transcripts_raw:
            transcript, mappings = self._process_transcript(t_raw, ucsc_start, ucsc_end, dna_sequence)
            if transcript:
                region_data.transcripts.append(transcript)
                if mappings:
                    region_data.amino_acid_mappings[transcript.transcript_id] = mappings

        return region_data

    def _process_transcript(self, t_raw: dict, region_start: int, region_end: int,
                            dna_sequence: str) -> tuple[Optional[TranscriptInfo], list[AminoAcidMapping]]:
        """Process a single RefSeq transcript."""
        try:
            # Parse exon coordinates
            exon_starts = [int(x) for x in t_raw["exonStarts"].rstrip(",").split(",")]
            exon_ends = [int(x) for x in t_raw["exonEnds"].rstrip(",").split(",")]

            strand = 1 if t_raw["strand"] == "+" else -1

            # Create TranscriptInfo
            transcript = TranscriptInfo(
                transcript_id=t_raw["name"],
                gene_name=t_raw.get("name2", ""),
                chromosome=t_raw["chrom"],
                strand=strand,
                start=t_raw["txStart"],
                end=t_raw["txEnd"],
                cds_start=t_raw["cdsStart"],
                cds_end=t_raw["cdsEnd"]
            )

            # Add exons
            for i, (es, ee) in enumerate(zip(exon_starts, exon_ends)):
                exon = Exon(
                    exon_id=f"{t_raw['name']}_exon_{i+1}",
                    start=es,
                    end=ee,
                    rank=i + 1,
                    phase=0,
                    end_phase=0
                )
                transcript.exons.append(exon)

            # Calculate amino acid mappings
            mappings = self._calculate_amino_acid_mappings(
                transcript, exon_starts, exon_ends,
                region_start, region_end, dna_sequence
            )

            return transcript, mappings

        except Exception as e:
            print(f"Error processing transcript {t_raw.get('name', '?')}: {e}")
            return None, []

    def _calculate_amino_acid_mappings(self, transcript: TranscriptInfo,
                                        exon_starts: list[int], exon_ends: list[int],
                                        region_start: int, region_end: int,
                                        dna_sequence: str) -> list[AminoAcidMapping]:
        """Calculate amino acid to genomic coordinate mappings."""
        mappings = []

        cds_start = transcript.cds_start
        cds_end = transcript.cds_end
        strand = transcript.strand

        # Build list of coding exon segments
        coding_segments = []  # [(genomic_start, genomic_end), ...]

        for es, ee in zip(exon_starts, exon_ends):
            # Clip to CDS
            seg_start = max(es, cds_start)
            seg_end = min(ee, cds_end)

            if seg_start < seg_end:
                coding_segments.append((seg_start, seg_end))

        if not coding_segments:
            return []

        # Sort by position (reverse for minus strand to get 5'->3' order)
        if strand == -1:
            coding_segments.sort(key=lambda x: x[0], reverse=True)
        else:
            coding_segments.sort(key=lambda x: x[0])

        # Build CDS sequence and position map
        cds_sequence = []
        genomic_positions = []  # genomic position for each CDS base

        for seg_start, seg_end in coding_segments:
            if strand == 1:
                for pos in range(seg_start, seg_end):
                    genomic_positions.append(pos)
                    # Get base from dna_sequence
                    if region_start <= pos < region_end:
                        base = dna_sequence[pos - region_start]
                    else:
                        base = 'N'
                    cds_sequence.append(base)
            else:
                # Minus strand: iterate in reverse
                for pos in range(seg_end - 1, seg_start - 1, -1):
                    genomic_positions.append(pos)
                    if region_start <= pos < region_end:
                        base = dna_sequence[pos - region_start]
                        # Complement for minus strand
                        base = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}.get(base, 'N')
                    else:
                        base = 'N'
                    cds_sequence.append(base)

        cds_seq_str = ''.join(cds_sequence)

        # Translate to get protein sequence
        protein_seq = translate(cds_seq_str)

        # Map each amino acid to genomic coordinates
        for aa_idx, amino_acid in enumerate(protein_seq):
            if amino_acid == '*':  # Stop codon
                continue

            aa_position = aa_idx + 1  # 1-based

            # Get the 3 CDS positions for this codon
            codon_start_idx = aa_idx * 3
            if codon_start_idx + 3 > len(genomic_positions):
                break

            codon_genomic_positions = genomic_positions[codon_start_idx:codon_start_idx + 3]
            codon_seq = cds_seq_str[codon_start_idx:codon_start_idx + 3]

            # Get genomic range
            genomic_start = min(codon_genomic_positions)
            genomic_end = max(codon_genomic_positions)

            # Check if within region of interest
            if genomic_end >= region_start and genomic_start < region_end:
                mapping = AminoAcidMapping(
                    amino_acid=amino_acid,
                    position=aa_position,
                    codon=codon_seq,
                    genomic_start=genomic_start,
                    genomic_end=genomic_end,
                    exon_id=""
                )
                mappings.append(mapping)

        # Sort by genomic position
        mappings.sort(key=lambda m: m.genomic_start)

        return mappings

    def fetch_by_transcript(self, transcript_id: str, padding: int = 50) -> GenomicRegionData:
        """
        Fetch data for a specific RefSeq transcript with padding.

        Args:
            transcript_id: RefSeq ID (e.g., "NM_000022.4")
            padding: Base pairs to add on each side

        Returns:
            GenomicRegionData for the transcript region
        """
        # Search all chromosomes for the transcript
        for chrom_num in list(range(1, 23)) + ['X', 'Y']:
            chrom = f"chr{chrom_num}"
            try:
                # Query a wide region first
                transcripts = self._get_refseq_transcripts(chrom, 0, 300000000)
                for t in transcripts:
                    if t["name"] == transcript_id:
                        start = max(0, t["txStart"] - padding)
                        end = t["txEnd"] + padding
                        return self.fetch_region(chrom, start, end, [transcript_id])
            except:
                continue

        raise ValueError(f"Transcript {transcript_id} not found")


# Example usage
if __name__ == "__main__":
    fetcher = RefSeqFetcher()

    # Fetch ADA gene region with RefSeq transcripts
    region_data = fetcher.fetch_region(
        chromosome="chr20",
        start=44620965,
        end=44621240,
        track="ncbiRefSeq"
    )

    print(f"\nRegion: {region_data.chromosome}:{region_data.start}-{region_data.end}")
    print(f"DNA length: {len(region_data.dna_sequence)} bp")
    print(f"Transcripts: {len(region_data.transcripts)}")

    for t in region_data.transcripts:
        mappings = region_data.amino_acid_mappings.get(t.transcript_id, [])
        print(f"  {t.transcript_id} ({t.gene_name}): {len(mappings)} AAs")
        if mappings:
            print(f"    First: {mappings[0].amino_acid}{mappings[0].position} @ {mappings[0].genomic_start}")
            print(f"    Last: {mappings[-1].amino_acid}{mappings[-1].position} @ {mappings[-1].genomic_end}")
