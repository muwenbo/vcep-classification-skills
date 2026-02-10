"""
Genome Sequence Fetcher

Fetches DNA sequences and amino acid sequences with genomic coordinate mapping
using the Ensembl REST API. Designed for genome browser-like visualizations.

Author: ClinGen Project
"""

import requests
import json
from dataclasses import dataclass, field
from typing import Optional
import time


# Ensembl REST API base URL
ENSEMBL_REST = "https://rest.ensembl.org"


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
class CodingRegion:
    """Represents a coding region within an exon"""
    genomic_start: int
    genomic_end: int
    cds_start: int  # Position in CDS (1-based)
    cds_end: int
    phase: int


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
    coding_regions: list[CodingRegion] = field(default_factory=list)
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


class EnsemblAPI:
    """Client for Ensembl REST API"""

    def __init__(self, assembly: str = "GRCh38"):
        self.base_url = ENSEMBL_REST
        self.assembly = assembly
        self.session = requests.Session()
        self._last_request_time = 0
        self._rate_limit_delay = 0.1  # 100ms between requests

    def _request(self, endpoint: str, params: dict = None, headers: dict = None) -> dict | str:
        """Make rate-limited request to Ensembl API"""
        # Rate limiting
        elapsed = time.time() - self._last_request_time
        if elapsed < self._rate_limit_delay:
            time.sleep(self._rate_limit_delay - elapsed)

        url = f"{self.base_url}{endpoint}"
        default_headers = {"Content-Type": "application/json"}
        if headers:
            default_headers.update(headers)

        response = self.session.get(url, params=params, headers=default_headers)
        self._last_request_time = time.time()

        if response.status_code != 200:
            raise Exception(f"API request failed: {response.status_code} - {response.text}")

        if "application/json" in response.headers.get("Content-Type", ""):
            return response.json()
        return response.text

    def get_dna_sequence(self, chromosome: str, start: int, end: int) -> str:
        """Fetch DNA sequence for a genomic region"""
        # Remove 'chr' prefix if present (Ensembl uses numeric chromosomes)
        chrom = chromosome.replace("chr", "")
        endpoint = f"/sequence/region/human/{chrom}:{start}..{end}"
        return self._request(endpoint, headers={"Content-Type": "text/plain"})

    def get_transcript_sequence(self, transcript_id: str, seq_type: str = "cds") -> str:
        """
        Get sequence for a transcript
        seq_type: 'cds', 'cdna', 'protein'
        """
        endpoint = f"/sequence/id/{transcript_id}"
        params = {"type": seq_type}
        return self._request(endpoint, params=params, headers={"Content-Type": "text/plain"})

    def get_genes_in_region(self, chromosome: str, start: int, end: int) -> list[dict]:
        """Get all genes overlapping a genomic region"""
        chrom = chromosome.replace("chr", "")
        endpoint = f"/overlap/region/human/{chrom}:{start}-{end}"
        params = {"feature": "gene"}
        return self._request(endpoint, params=params)

    def get_transcripts_in_region(self, chromosome: str, start: int, end: int) -> list[dict]:
        """Get all transcripts overlapping a genomic region"""
        chrom = chromosome.replace("chr", "")
        endpoint = f"/overlap/region/human/{chrom}:{start}-{end}"
        params = {"feature": "transcript"}
        return self._request(endpoint, params=params)

    def get_transcript_details(self, transcript_id: str) -> dict:
        """Get detailed information about a transcript including exons"""
        endpoint = f"/lookup/id/{transcript_id}"
        params = {"expand": 1}  # Include exons
        return self._request(endpoint, params=params)

    def get_gene_by_symbol(self, symbol: str) -> dict:
        """Look up a gene by its symbol"""
        endpoint = f"/lookup/symbol/homo_sapiens/{symbol}"
        params = {"expand": 1}
        return self._request(endpoint, params=params)


class GenomeSequenceFetcher:
    """
    Main class for fetching and organizing genomic sequence data
    for genome browser-like visualizations.
    """

    def __init__(self):
        self.api = EnsemblAPI()

    def fetch_region(self, chromosome: str, start: int, end: int,
                     transcript_ids: list[str] = None) -> GenomicRegionData:
        """
        Fetch complete data for a genomic region.

        Args:
            chromosome: Chromosome name (e.g., "chr20" or "20")
            start: Start position (1-based)
            end: End position (1-based)
            transcript_ids: Optional list of specific transcript IDs to include.
                          If None, fetches all transcripts in the region.

        Returns:
            GenomicRegionData with DNA sequence, transcripts, and amino acid mappings
        """
        # Normalize chromosome name
        chrom = chromosome.replace("chr", "")
        chrom_display = f"chr{chrom}"

        # Fetch DNA sequence
        print(f"Fetching DNA sequence for {chrom_display}:{start}-{end}...")
        dna_sequence = self.api.get_dna_sequence(chrom, start, end)

        # Initialize result
        region_data = GenomicRegionData(
            chromosome=chrom_display,
            start=start,
            end=end,
            dna_sequence=dna_sequence.upper()
        )

        # Get transcripts
        if transcript_ids:
            transcripts_info = [self.api.get_transcript_details(tid) for tid in transcript_ids]
        else:
            print("Fetching transcripts in region...")
            transcripts_raw = self.api.get_transcripts_in_region(chrom, start, end)
            # Filter for protein-coding transcripts and get details
            transcripts_info = []
            for t in transcripts_raw:
                if t.get("biotype") == "protein_coding":
                    try:
                        details = self.api.get_transcript_details(t["id"])
                        transcripts_info.append(details)
                    except Exception as e:
                        print(f"Warning: Could not fetch details for {t['id']}: {e}")

        # Process each transcript
        for t_info in transcripts_info:
            transcript = self._process_transcript(t_info)
            if transcript:
                region_data.transcripts.append(transcript)

                # Calculate amino acid mappings for this transcript
                mappings = self._calculate_amino_acid_mappings(transcript, start, end)
                if mappings:
                    region_data.amino_acid_mappings[transcript.transcript_id] = mappings

        return region_data

    def _process_transcript(self, t_info: dict) -> Optional[TranscriptInfo]:
        """Process transcript data from API response"""
        try:
            # Get gene name
            gene_name = t_info.get("display_name", "").split("-")[0]
            if not gene_name and "Parent" in t_info:
                gene_name = t_info["Parent"]

            transcript = TranscriptInfo(
                transcript_id=t_info["id"],
                gene_name=gene_name,
                chromosome=f"chr{t_info['seq_region_name']}",
                strand=t_info["strand"],
                start=t_info["start"],
                end=t_info["end"],
                cds_start=None,
                cds_end=None
            )

            # Process exons
            if "Exon" in t_info:
                for i, exon_data in enumerate(t_info["Exon"]):
                    exon = Exon(
                        exon_id=exon_data["id"],
                        start=exon_data["start"],
                        end=exon_data["end"],
                        rank=i + 1,
                        phase=exon_data.get("phase", -1),
                        end_phase=exon_data.get("end_phase", -1)
                    )
                    transcript.exons.append(exon)

                # Sort exons by position
                transcript.exons.sort(key=lambda e: e.start)

            # Get CDS boundaries if available
            if "Translation" in t_info:
                trans = t_info["Translation"]
                transcript.cds_start = trans.get("start")
                transcript.cds_end = trans.get("end")

            # Fetch CDS and protein sequences
            try:
                transcript.cds_sequence = self.api.get_transcript_sequence(
                    transcript.transcript_id, "cds"
                )
                transcript.protein_sequence = self.api.get_transcript_sequence(
                    transcript.transcript_id, "protein"
                )
            except Exception as e:
                print(f"Warning: Could not fetch sequences for {transcript.transcript_id}: {e}")

            # Calculate coding regions
            if transcript.cds_start and transcript.cds_end:
                transcript.coding_regions = self._calculate_coding_regions(transcript)

            return transcript

        except Exception as e:
            print(f"Error processing transcript: {e}")
            return None

    def _calculate_coding_regions(self, transcript: TranscriptInfo) -> list[CodingRegion]:
        """Calculate coding regions within exons"""
        coding_regions = []
        cds_position = 1

        # Sort exons based on strand
        exons = sorted(transcript.exons,
                      key=lambda e: e.start if transcript.strand == 1 else -e.start)

        for exon in exons:
            # Determine overlap with CDS
            if transcript.strand == 1:
                coding_start = max(exon.start, transcript.cds_start)
                coding_end = min(exon.end, transcript.cds_end)
            else:
                coding_start = max(exon.start, transcript.cds_start)
                coding_end = min(exon.end, transcript.cds_end)

            if coding_start <= coding_end:
                length = coding_end - coding_start + 1
                coding_region = CodingRegion(
                    genomic_start=coding_start,
                    genomic_end=coding_end,
                    cds_start=cds_position,
                    cds_end=cds_position + length - 1,
                    phase=exon.phase if exon.phase >= 0 else 0
                )
                coding_regions.append(coding_region)
                cds_position += length

        return coding_regions

    def _calculate_amino_acid_mappings(self, transcript: TranscriptInfo,
                                        region_start: int, region_end: int) -> list[AminoAcidMapping]:
        """
        Calculate amino acid to genomic coordinate mappings for a transcript
        within a specified region.
        """
        if not transcript.protein_sequence or not transcript.cds_sequence:
            return []

        mappings = []

        # Build a map from CDS position to genomic position
        cds_to_genomic = {}

        for cr in transcript.coding_regions:
            if transcript.strand == 1:
                for i, pos in enumerate(range(cr.genomic_start, cr.genomic_end + 1)):
                    cds_pos = cr.cds_start + i
                    cds_to_genomic[cds_pos] = pos
            else:
                # Reverse strand: genomic positions decrease as CDS positions increase
                for i, pos in enumerate(range(cr.genomic_end, cr.genomic_start - 1, -1)):
                    cds_pos = cr.cds_start + i
                    cds_to_genomic[cds_pos] = pos

        # Map each amino acid
        for aa_idx, amino_acid in enumerate(transcript.protein_sequence):
            aa_position = aa_idx + 1  # 1-based

            # CDS positions for this codon (1-based)
            codon_start = (aa_idx * 3) + 1
            codon_end = codon_start + 2

            # Get genomic positions
            genomic_positions = []
            for cds_pos in range(codon_start, codon_end + 1):
                if cds_pos in cds_to_genomic:
                    genomic_positions.append(cds_to_genomic[cds_pos])

            if len(genomic_positions) == 3:
                if transcript.strand == 1:
                    genomic_start = min(genomic_positions)
                    genomic_end = max(genomic_positions)
                else:
                    genomic_start = min(genomic_positions)
                    genomic_end = max(genomic_positions)

                # Check if this amino acid is within our region of interest
                if genomic_end >= region_start and genomic_start <= region_end:
                    # Get the codon sequence
                    codon = transcript.cds_sequence[codon_start-1:codon_end]

                    # Find which exon contains this codon
                    exon_id = ""
                    for exon in transcript.exons:
                        if exon.start <= genomic_start <= exon.end:
                            exon_id = exon.exon_id
                            break

                    mapping = AminoAcidMapping(
                        amino_acid=amino_acid,
                        position=aa_position,
                        codon=codon,
                        genomic_start=genomic_start,
                        genomic_end=genomic_end,
                        exon_id=exon_id
                    )
                    mappings.append(mapping)

        # Sort by genomic position
        mappings.sort(key=lambda m: m.genomic_start)

        return mappings

    def fetch_by_gene(self, gene_symbol: str, padding: int = 100) -> GenomicRegionData:
        """
        Fetch data for an entire gene with optional padding.

        Args:
            gene_symbol: Gene symbol (e.g., "ADA", "BRCA1")
            padding: Base pairs to add on each side

        Returns:
            GenomicRegionData for the gene region
        """
        print(f"Looking up gene {gene_symbol}...")
        gene_info = self.api.get_gene_by_symbol(gene_symbol)

        chrom = gene_info["seq_region_name"]
        start = gene_info["start"] - padding
        end = gene_info["end"] + padding

        # Get transcript IDs
        transcript_ids = []
        if "Transcript" in gene_info:
            for t in gene_info["Transcript"]:
                if t.get("biotype") == "protein_coding":
                    transcript_ids.append(t["id"])

        return self.fetch_region(chrom, start, end, transcript_ids)


def to_visualization_format(region_data: GenomicRegionData, compact: bool = True,
                            deduplicate: bool = True) -> dict:
    """
    Convert GenomicRegionData to a format suitable for visualization.

    Args:
        region_data: GenomicRegionData object
        compact: If True, use efficient columnar format. If False, use verbose format.
        deduplicate: If True (and compact=True), keep only one transcript per unique
                     amino acid sequence. Other transcript IDs stored in 'aliases'.

    Returns:
        Dictionary with sequence and transcript data.

    Compact format structure:
        - sequence: DNA string (position = start + index)
        - transcripts: dict with columnar amino acid data

    To reconstruct amino acid genomic positions from compact format:
        genomic_start = start + aa_offsets[i]
        genomic_end = genomic_start + 2  (for normal codons)
    """
    if compact:
        return _to_compact_format(region_data, deduplicate=deduplicate)
    else:
        return _to_verbose_format(region_data)


def _to_compact_format(region_data: GenomicRegionData, deduplicate: bool = True) -> dict:
    """
    Efficient columnar format - ~95% smaller than verbose format.

    Args:
        region_data: GenomicRegionData object
        deduplicate: If True, keep only one transcript per unique amino acid sequence
    """
    result = {
        "chromosome": region_data.chromosome,
        "start": region_data.start,
        "end": region_data.end,
        "sequence": region_data.dna_sequence,
        "transcripts": {}
    }

    # Track seen amino acid sequences for deduplication
    seen_sequences = {}  # aa_sequence -> transcript_id

    for transcript_id, mappings in region_data.amino_acid_mappings.items():
        # Find transcript info
        transcript = next(
            (t for t in region_data.transcripts if t.transcript_id == transcript_id),
            None
        )

        if not transcript or not mappings:
            continue

        # Build columnar arrays
        aa_positions = []
        aa_sequence = []
        aa_codons = []
        aa_offsets = []  # Relative to region start

        for mapping in mappings:
            aa_positions.append(mapping.position)
            aa_sequence.append(mapping.amino_acid)
            aa_codons.append(mapping.codon)
            aa_offsets.append(mapping.genomic_start - region_data.start)

        aa_seq_str = "".join(aa_sequence)

        # Deduplication: skip if we've seen this exact amino acid sequence
        if deduplicate:
            if aa_seq_str in seen_sequences:
                # Add this transcript ID to the existing entry's aliases
                existing_tid = seen_sequences[aa_seq_str]
                if "aliases" not in result["transcripts"][existing_tid]:
                    result["transcripts"][existing_tid]["aliases"] = []
                result["transcripts"][existing_tid]["aliases"].append(transcript_id)
                continue
            seen_sequences[aa_seq_str] = transcript_id

        # Get exon ranges within this region
        exons = []
        for exon in transcript.exons:
            if exon.end >= region_data.start and exon.start <= region_data.end:
                exons.append([
                    max(exon.start, region_data.start) - region_data.start,  # Relative start
                    min(exon.end, region_data.end) - region_data.start       # Relative end
                ])

        result["transcripts"][transcript_id] = {
            "gene": transcript.gene_name,
            "strand": transcript.strand,
            "exons": exons,
            "aa_positions": aa_positions,
            "aa_sequence": aa_seq_str,
            "aa_codons": aa_codons,
            "aa_offsets": aa_offsets
        }

    return result


def _to_verbose_format(region_data: GenomicRegionData) -> dict:
    """Original verbose format for backwards compatibility."""
    result = {
        "chromosome": region_data.chromosome,
        "start": region_data.start,
        "end": region_data.end,
        "coordinates": list(range(region_data.start, region_data.end + 1)),
        "dna": [],
        "transcripts": {}
    }

    # DNA sequence with positions
    for i, nucleotide in enumerate(region_data.dna_sequence):
        result["dna"].append({
            "position": region_data.start + i,
            "nucleotide": nucleotide
        })

    # Amino acid mappings per transcript
    for transcript_id, mappings in region_data.amino_acid_mappings.items():
        transcript = next(
            (t for t in region_data.transcripts if t.transcript_id == transcript_id),
            None
        )

        gene_name = transcript.gene_name if transcript else ""
        strand = transcript.strand if transcript else 1

        result["transcripts"][transcript_id] = {
            "gene_name": gene_name,
            "strand": strand,
            "amino_acids": []
        }

        for mapping in mappings:
            result["transcripts"][transcript_id]["amino_acids"].append({
                "amino_acid": mapping.amino_acid,
                "position": mapping.position,
                "codon": mapping.codon,
                "genomic_start": mapping.genomic_start,
                "genomic_end": mapping.genomic_end,
                "genomic_center": (mapping.genomic_start + mapping.genomic_end) / 2
            })

    return result


def expand_compact_format(compact_data: dict) -> dict:
    """
    Expand compact format back to full coordinates for easy iteration.

    Returns dict with:
        - All original fields
        - transcripts[id]['amino_acids']: list of dicts with full coordinates
    """
    result = {
        "chromosome": compact_data["chromosome"],
        "start": compact_data["start"],
        "end": compact_data["end"],
        "sequence": compact_data["sequence"],
        "transcripts": {}
    }

    start = compact_data["start"]

    for tid, tdata in compact_data["transcripts"].items():
        amino_acids = []
        aa_seq = tdata["aa_sequence"]

        for i in range(len(aa_seq)):
            offset = tdata["aa_offsets"][i]
            genomic_start = start + offset

            amino_acids.append({
                "amino_acid": aa_seq[i],
                "position": tdata["aa_positions"][i],
                "codon": tdata["aa_codons"][i],
                "genomic_start": genomic_start,
                "genomic_end": genomic_start + 2
            })

        result["transcripts"][tid] = {
            "gene": tdata["gene"],
            "strand": tdata["strand"],
            "exons": [[start + e[0], start + e[1]] for e in tdata["exons"]],
            "amino_acids": amino_acids
        }

    return result


def load_from_json(json_path: str) -> GenomicRegionData:
    """
    Load compact JSON format and convert to GenomicRegionData for use with plotters.

    Args:
        json_path: Path to JSON file (compact or verbose format)

    Returns:
        GenomicRegionData object compatible with genome_browser_demo.py
    """
    import json

    with open(json_path) as f:
        data = json.load(f)

    # Detect format (compact has 'sequence', verbose has 'dna')
    is_compact = "sequence" in data

    if is_compact:
        return _load_compact_json(data)
    else:
        return _load_verbose_json(data)


def _load_compact_json(data: dict) -> GenomicRegionData:
    """Load compact format JSON into GenomicRegionData."""
    region = GenomicRegionData(
        chromosome=data["chromosome"],
        start=data["start"],
        end=data["end"],
        dna_sequence=data["sequence"]
    )

    start = data["start"]

    for tid, tdata in data["transcripts"].items():
        # Create TranscriptInfo
        transcript = TranscriptInfo(
            transcript_id=tid,
            gene_name=tdata["gene"],
            chromosome=data["chromosome"],
            strand=tdata["strand"],
            start=start,
            end=data["end"],
            cds_start=None,
            cds_end=None
        )

        # Add exons
        for exon_rel in tdata.get("exons", []):
            exon = Exon(
                exon_id="",
                start=start + exon_rel[0],
                end=start + exon_rel[1],
                rank=len(transcript.exons) + 1,
                phase=0,
                end_phase=0
            )
            transcript.exons.append(exon)

        region.transcripts.append(transcript)

        # Create amino acid mappings
        mappings = []
        aa_seq = tdata["aa_sequence"]
        for i in range(len(aa_seq)):
            offset = tdata["aa_offsets"][i]
            genomic_start = start + offset

            mapping = AminoAcidMapping(
                amino_acid=aa_seq[i],
                position=tdata["aa_positions"][i],
                codon=tdata["aa_codons"][i],
                genomic_start=genomic_start,
                genomic_end=genomic_start + 2,
                exon_id=""
            )
            mappings.append(mapping)

        region.amino_acid_mappings[tid] = mappings

        # Also add mappings for aliases
        for alias_tid in tdata.get("aliases", []):
            region.amino_acid_mappings[alias_tid] = mappings

    return region


def _load_verbose_json(data: dict) -> GenomicRegionData:
    """Load verbose format JSON into GenomicRegionData."""
    region = GenomicRegionData(
        chromosome=data["chromosome"],
        start=data["start"],
        end=data["end"],
        dna_sequence="".join(d["nucleotide"] for d in data["dna"])
    )

    for tid, tdata in data["transcripts"].items():
        transcript = TranscriptInfo(
            transcript_id=tid,
            gene_name=tdata.get("gene_name", tdata.get("gene", "")),
            chromosome=data["chromosome"],
            strand=tdata["strand"],
            start=data["start"],
            end=data["end"],
            cds_start=None,
            cds_end=None
        )
        region.transcripts.append(transcript)

        mappings = []
        for aa in tdata.get("amino_acids", []):
            mapping = AminoAcidMapping(
                amino_acid=aa["amino_acid"],
                position=aa["position"],
                codon=aa["codon"],
                genomic_start=aa["genomic_start"],
                genomic_end=aa["genomic_end"],
                exon_id=""
            )
            mappings.append(mapping)

        region.amino_acid_mappings[tid] = mappings

    return region


def print_region_summary(region_data: GenomicRegionData):
    """Print a summary of the fetched region data"""
    print("\n" + "=" * 60)
    print(f"Region: {region_data.chromosome}:{region_data.start}-{region_data.end}")
    print(f"Length: {len(region_data.dna_sequence)} bp")
    print(f"DNA sequence (first 50bp): {region_data.dna_sequence[:50]}...")
    print(f"\nTranscripts found: {len(region_data.transcripts)}")

    for transcript in region_data.transcripts:
        print(f"\n  {transcript.transcript_id} ({transcript.gene_name})")
        print(f"    Strand: {'+' if transcript.strand == 1 else '-'}")
        print(f"    Exons: {len(transcript.exons)}")
        print(f"    Protein length: {len(transcript.protein_sequence)} aa")

        if transcript.transcript_id in region_data.amino_acid_mappings:
            mappings = region_data.amino_acid_mappings[transcript.transcript_id]
            print(f"    Amino acids in region: {len(mappings)}")
            if mappings:
                first_aa = mappings[0]
                last_aa = mappings[-1]
                print(f"    Range: {first_aa.amino_acid}{first_aa.position} - {last_aa.amino_acid}{last_aa.position}")

    print("=" * 60)


# Example usage and demonstration
if __name__ == "__main__":
    fetcher = GenomeSequenceFetcher()

    # Example 1: Fetch a specific region (ADA gene region from the screenshot)
    print("\n--- Example 1: Fetching specific region ---")
    region_data = fetcher.fetch_region(
        chromosome="chr20",
        start=44621000,
        end=44621200
    )
    print_region_summary(region_data)

    # Convert to visualization format
    viz_data = to_visualization_format(region_data)

    # Save to JSON for use in plotting
    output_file = "region_data.json"
    with open(output_file, "w") as f:
        json.dump(viz_data, f, indent=2)
    print(f"\nVisualization data saved to {output_file}")

    # Example 2: Fetch by gene symbol
    print("\n--- Example 2: Fetching by gene symbol ---")
    # Uncomment to test:
    # gene_data = fetcher.fetch_by_gene("ADA", padding=100)
    # print_region_summary(gene_data)

    # Print sample amino acid mappings
    print("\n--- Sample Amino Acid Mappings ---")
    for transcript_id, mappings in region_data.amino_acid_mappings.items():
        print(f"\n{transcript_id}:")
        for mapping in mappings[:10]:  # First 10
            print(f"  {mapping.amino_acid}{mapping.position}: "
                  f"{mapping.codon} @ {mapping.genomic_start}-{mapping.genomic_end}")
