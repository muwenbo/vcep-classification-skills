#!/usr/bin/env python3
"""
VEP Annotation Script

Query Ensembl VEP REST API for comprehensive variant annotation.
Supports HGVS notation, rsID, and genomic coordinates.

Usage:
    python vep_annotate.py "NM_000546.6:c.215C>G"
    python vep_annotate.py rs1042522
    python vep_annotate.py "chr17:7674220:C:T"
    python vep_annotate.py "17-7674220-C-T"
"""

import argparse
import json
import re
import sys
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


# Ensembl REST API configuration
ENSEMBL_REST_URL = "https://rest.ensembl.org"
RATE_LIMIT_DELAY = 0.1  # 100ms between requests

# Shared VEP plugin/option parameters for POST requests
VEP_POST_PARAMS = {
    "AlphaMissense": 1,
    "Blosum62": 1,
    "CADD": 1,
    "ClinPred": 1,
    "DosageSensitivity": 1,
    "EVE": 1,
    "Enformer": 1,
    "GeneSplicer": 1,
    "Geno2MP": 1,
    "LOEUF": 1,
    "LoF": 1,
    "NMD": 1,
    "Paralogues": "clnsig=pathogenic,clnsig_match=exact,fields=all",
    "Phenotypes": 1,
    "REVEL": 1,
    "RiboseqORFs": 1,
    "SpliceAI": 2,
    "UTRAnnotator": 1,
    "dbNSFP": "transcript_match=1",
    "distance": 5000,
    "merged": 1,
    "protein": 1,
    "uniprot": 1,
    "minimal": 1,
    "hgvs": 1,
    "canonical": 1,
    "mane": 1,
    "variant_class": 1,
}


@dataclass
class TranscriptConsequence:
    """Parsed transcript consequence from VEP"""
    transcript_id: str
    gene_symbol: str
    gene_id: str
    consequence_terms: List[str]
    impact: str
    biotype: str
    canonical: bool = False
    mane_select: bool = False
    mane_plus_clinical: bool = False
    amino_acids: Optional[str] = None
    codons: Optional[str] = None
    protein_start: Optional[int] = None
    protein_end: Optional[int] = None
    protein_id: Optional[str] = None
    hgvsc: Optional[str] = None
    hgvsp: Optional[str] = None
    # SIFT / PolyPhen
    sift_score: Optional[float] = None
    sift_prediction: Optional[str] = None
    polyphen_score: Optional[float] = None
    polyphen_prediction: Optional[str] = None
    # CADD
    cadd_phred: Optional[float] = None
    cadd_raw: Optional[float] = None
    # REVEL
    revel_score: Optional[float] = None
    # AlphaMissense
    alphamissense_pathogenicity: Optional[float] = None
    alphamissense_class: Optional[str] = None
    # Blosum62
    blosum62: Optional[int] = None
    # ClinPred
    clinpred: Optional[float] = None
    # EVE
    eve_score: Optional[float] = None
    eve_class: Optional[str] = None
    # SpliceAI
    spliceai: Optional[Dict[str, Any]] = None
    # LOEUF
    loeuf: Optional[float] = None
    # DosageSensitivity
    phaplo: Optional[float] = None
    ptriplo: Optional[float] = None
    # LoF (LOFTEE)
    lof: Optional[str] = None
    lof_filter: Optional[str] = None
    lof_flags: Optional[str] = None
    lof_info: Optional[str] = None
    # NMD
    nmd: Optional[str] = None
    # Phenotypes (from VEP Phenotypes plugin)
    phenotypes: Optional[List[Dict[str, Any]]] = None
    # UniProt
    uniprot_isoform: Optional[List[str]] = None
    swissprot: Optional[List[str]] = None
    trembl: Optional[List[str]] = None
    uniparc: Optional[List[str]] = None
    # Distance (for upstream/downstream variants)
    distance: Optional[int] = None
    # Strand
    strand: Optional[int] = None
    # Source (Ensembl or RefSeq, from merged mode)
    source: Optional[str] = None


@dataclass
class ColocatedVariant:
    """Known variant at the same position"""
    id: str
    allele_string: Optional[str] = None
    clinical_significance: List[str] = field(default_factory=list)
    pubmed_ids: List[int] = field(default_factory=list)
    frequencies: Dict[str, float] = field(default_factory=dict)
    phenotypes: List[str] = field(default_factory=list)


@dataclass
class VEPAnnotation:
    """Complete VEP annotation result"""
    input: str
    assembly: str
    chromosome: str
    start: int
    end: int
    strand: int
    allele_string: str
    most_severe_consequence: str
    variant_class: Optional[str] = None
    transcript_consequences: List[TranscriptConsequence] = field(default_factory=list)
    colocated_variants: List[ColocatedVariant] = field(default_factory=list)

    @property
    def gene_symbol(self) -> Optional[str]:
        """Get gene symbol from canonical or first transcript"""
        canonical = self.get_canonical_consequence()
        return canonical.gene_symbol if canonical else None

    @property
    def rsid(self) -> Optional[str]:
        """Get rsID if available"""
        for cv in self.colocated_variants:
            if cv.id.startswith("rs"):
                return cv.id
        return None

    @property
    def pmids(self) -> List[int]:
        """Get all PMIDs from colocated variants"""
        pmids = []
        for cv in self.colocated_variants:
            pmids.extend(cv.pubmed_ids)
        return sorted(set(pmids))

    @property
    def clinical_significance(self) -> List[str]:
        """Get clinical significance from colocated variants"""
        clin_sig = []
        for cv in self.colocated_variants:
            clin_sig.extend(cv.clinical_significance)
        return list(set(clin_sig))

    @property
    def gnomad_af(self) -> Optional[float]:
        """Get gnomAD allele frequency (prefer genome over exome)"""
        for cv in self.colocated_variants:
            if cv.frequencies:
                for key in ["gnomadg", "gnomade", "gnomad"]:
                    if key in cv.frequencies:
                        return cv.frequencies[key]
        return None

    def get_canonical_consequence(self) -> Optional[TranscriptConsequence]:
        """Get the best transcript consequence with merged Ensembl + RefSeq data.

        In merged mode, the same gene may have both Ensembl and RefSeq transcripts.
        We prefer the RefSeq MANE Select for clinical HGVSc/HGVSp, but some scores
        (e.g. REVEL) are only available on Ensembl transcripts. This method picks the
        RefSeq MANE Select and backfills missing scores from the Ensembl counterpart.
        """
        if not self.transcript_consequences:
            return None

        # Find RefSeq MANE Select (NM_ prefix)
        refseq_mane = None
        for tc in self.transcript_consequences:
            if tc.mane_select and tc.transcript_id.startswith("NM_"):
                refseq_mane = tc
                break

        # Find Ensembl MANE Select (ENST prefix)
        ensembl_mane = None
        for tc in self.transcript_consequences:
            if tc.mane_select and tc.transcript_id.startswith("ENST"):
                ensembl_mane = tc
                break

        # If we have both, use RefSeq but backfill scores from Ensembl
        if refseq_mane and ensembl_mane:
            score_fields = [
                "revel_score", "polyphen_score", "polyphen_prediction",
                "loeuf", "lof", "lof_filter", "lof_flags", "lof_info", "nmd",
            ]
            for field in score_fields:
                if getattr(refseq_mane, field) is None and getattr(ensembl_mane, field) is not None:
                    setattr(refseq_mane, field, getattr(ensembl_mane, field))
            return refseq_mane

        # If only one MANE Select available, use it
        if refseq_mane:
            return refseq_mane
        if ensembl_mane:
            return ensembl_mane

        # Fall back to canonical
        for tc in self.transcript_consequences:
            if tc.canonical:
                return tc
        # Fall back to first
        return self.transcript_consequences[0]

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        canonical = self.get_canonical_consequence()
        result = {
            "input": self.input,
            "assembly": self.assembly,
            "chromosome": self.chromosome,
            "start": self.start,
            "end": self.end,
            "strand": self.strand,
            "allele_string": self.allele_string,
            "variant_class": self.variant_class,
            "most_severe_consequence": self.most_severe_consequence,
            "gene_symbol": self.gene_symbol,
            "rsid": self.rsid,
            "pmids": self.pmids,
            "clinical_significance": self.clinical_significance,
            "gnomad_af": self.gnomad_af,
            "all_transcript_count": len(self.transcript_consequences),
            "colocated_variant_count": len(self.colocated_variants),
        }

        if canonical:
            ct = {
                "transcript_id": canonical.transcript_id,
                "protein_id": canonical.protein_id,
                "hgvsc": canonical.hgvsc,
                "hgvsp": canonical.hgvsp,
                "amino_acids": canonical.amino_acids,
                "codons": canonical.codons,
                "protein_position": canonical.protein_start,
                "consequence_terms": canonical.consequence_terms,
                "impact": canonical.impact,
                "biotype": canonical.biotype,
                "mane_select": canonical.mane_select,
                "canonical": canonical.canonical,
            }
            # In-silico predictors (only include if data present)
            if canonical.sift_score is not None:
                ct["sift"] = {"score": canonical.sift_score, "prediction": canonical.sift_prediction}
            if canonical.polyphen_score is not None:
                ct["polyphen"] = {"score": canonical.polyphen_score, "prediction": canonical.polyphen_prediction}
            if canonical.cadd_phred is not None:
                ct["cadd"] = {"phred": canonical.cadd_phred, "raw": canonical.cadd_raw}
            if canonical.revel_score is not None:
                ct["revel"] = canonical.revel_score
            if canonical.alphamissense_pathogenicity is not None:
                ct["alphamissense"] = {"pathogenicity": canonical.alphamissense_pathogenicity, "class": canonical.alphamissense_class}
            if canonical.blosum62 is not None:
                ct["blosum62"] = canonical.blosum62
            if canonical.clinpred is not None:
                ct["clinpred"] = canonical.clinpred
            if canonical.eve_score is not None:
                ct["eve"] = {"score": canonical.eve_score, "class": canonical.eve_class}
            if canonical.spliceai is not None:
                ct["spliceai"] = canonical.spliceai
            if canonical.loeuf is not None:
                ct["loeuf"] = canonical.loeuf
            if canonical.phaplo is not None or canonical.ptriplo is not None:
                ct["dosage_sensitivity"] = {"phaplo": canonical.phaplo, "ptriplo": canonical.ptriplo}
            if canonical.lof is not None:
                ct["lof"] = {"lof": canonical.lof, "filter": canonical.lof_filter, "flags": canonical.lof_flags, "info": canonical.lof_info}
            if canonical.nmd is not None:
                ct["nmd"] = canonical.nmd
            if canonical.phenotypes:
                ct["phenotypes"] = canonical.phenotypes
            if canonical.distance is not None:
                ct["distance"] = canonical.distance
            # UniProt
            uniprot = {}
            if canonical.swissprot:
                uniprot["swissprot"] = canonical.swissprot
            if canonical.trembl:
                uniprot["trembl"] = canonical.trembl
            if canonical.uniparc:
                uniprot["uniparc"] = canonical.uniparc
            if canonical.uniprot_isoform:
                uniprot["isoform"] = canonical.uniprot_isoform
            if uniprot:
                ct["uniprot"] = uniprot

            result["canonical_transcript"] = ct

        return result


def create_session() -> requests.Session:
    """Create a requests session with retry logic."""
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update({
        "Content-Type": "application/json",
        "Accept": "application/json",
    })
    return session


class VariantNotation:
    """Variant notation parser and classifier"""

    HGVS_PATTERN = re.compile(
        r'^(N[MRC]_\d+\.\d+)(?:\(([\w-]+)\))?:([cgpmn])\.(.+)$'
    )
    RSID_PATTERN = re.compile(r'^rs\d+$', re.IGNORECASE)
    GENOMIC_PATTERNS = [
        re.compile(r'^(?:chr)?(\w+)[:-](\d+)[:-]([ATCGN]+)[:-]([ATCGN]+)$', re.IGNORECASE),  # chr17:123:C:T
        re.compile(r'^(?:chr)?(\w+)[:-](\d+)[:-]([ATCGN]+)>([ATCGN]+)$', re.IGNORECASE),  # chr17:123:C>T
        re.compile(r'^(\w+)-(\d+)-([ATCGN]+)-([ATCGN]+)$', re.IGNORECASE),  # 17-123-C-T
    ]

    @classmethod
    def detect_format(cls, notation: str) -> str:
        """
        Detect the format of variant notation.

        Returns: "hgvs", "rsid", "genomic", or "unknown"
        """
        notation = notation.strip()

        if cls.HGVS_PATTERN.match(notation):
            return "hgvs"

        if cls.RSID_PATTERN.match(notation):
            return "rsid"

        for pattern in cls.GENOMIC_PATTERNS:
            if pattern.match(notation):
                return "genomic"

        return "unknown"

    @classmethod
    def parse_hgvs(cls, notation: str) -> Dict[str, str]:
        """Parse HGVS notation into components"""
        match = cls.HGVS_PATTERN.match(notation)
        if not match:
            raise ValueError(f"Invalid HGVS notation: {notation}")

        return {
            "transcript": match.group(1),
            "gene": match.group(2),
            "type": match.group(3),  # c, g, or p
            "change": match.group(4),
        }

    @classmethod
    def parse_genomic(cls, notation: str) -> Tuple[str, int, str, str]:
        """Parse genomic notation into components (chrom, pos, ref, alt)"""
        notation = notation.strip()

        for pattern in cls.GENOMIC_PATTERNS:
            match = pattern.match(notation)
            if match:
                chrom, pos, ref, alt = match.groups()
                return chrom.replace("chr", ""), int(pos), ref.upper(), alt.upper()

        raise ValueError(f"Invalid genomic notation: {notation}")


class VEPClient:
    """Client for Ensembl VEP REST API"""

    def __init__(self, base_url: str = ENSEMBL_REST_URL):
        self.base_url = base_url
        self.session = create_session()
        self._last_request_time = 0

    def _rate_limit(self):
        """Implement rate limiting"""
        elapsed = time.time() - self._last_request_time
        if elapsed < RATE_LIMIT_DELAY:
            time.sleep(RATE_LIMIT_DELAY - elapsed)
        self._last_request_time = time.time()

    def _request(self, endpoint: str, method: str = "GET",
                 data: Dict = None, params: Dict = None) -> Dict:
        """Make a request to the VEP API"""
        self._rate_limit()

        url = f"{self.base_url}{endpoint}"

        try:
            if method == "GET":
                response = self.session.get(url, params=params, timeout=60)
            else:
                response = self.session.post(url, json=data, timeout=60)

            if response.status_code == 429:
                # Rate limited - wait and retry
                wait_time = int(response.headers.get("Retry-After", 60))
                print(f"Rate limited. Waiting {wait_time}s...", file=sys.stderr)
                time.sleep(wait_time)
                return self._request(endpoint, method, data, params)

            response.raise_for_status()
            return response.json()

        except requests.RequestException as e:
            raise RuntimeError(f"VEP API request failed: {e}")

    def annotate_hgvs(self, hgvs: str) -> Dict:
        """Annotate variant using HGVS notation (POST endpoint)"""
        endpoint = "/vep/human/hgvs"
        data = {"hgvs_notations": [hgvs], **VEP_POST_PARAMS}
        return self._request(endpoint, method="POST", data=data)

    def annotate_rsid(self, rsid: str) -> Dict:
        """Annotate variant using rsID (POST endpoint)"""
        endpoint = "/vep/human/id"
        data = {"ids": [rsid], **VEP_POST_PARAMS}
        return self._request(endpoint, method="POST", data=data)

    def annotate_genomic(self, chrom: str, pos: int, ref: str, alt: str) -> Dict:
        """Annotate variant using genomic coordinates (POST endpoint)"""
        endpoint = "/vep/human/region"
        # VCF-like format: chrom pos id ref alt qual filter info
        vcf_variant = f"{chrom} {pos} . {ref} {alt} . . ."
        data = {"variants": [vcf_variant], **VEP_POST_PARAMS}
        return self._request(endpoint, method="POST", data=data)

    def annotate(self, notation: str) -> Dict:
        """Annotate variant using auto-detected notation format"""
        format_type = VariantNotation.detect_format(notation)

        if format_type == "hgvs":
            return self.annotate_hgvs(notation)
        elif format_type == "rsid":
            return self.annotate_rsid(notation)
        elif format_type == "genomic":
            chrom, pos, ref, alt = VariantNotation.parse_genomic(notation)
            return self.annotate_genomic(chrom, pos, ref, alt)
        else:
            raise ValueError(f"Unrecognized variant notation format: {notation}")


def parse_vep_response(response: List[Dict]) -> VEPAnnotation:
    """Parse VEP API response into structured VEPAnnotation"""
    if not response:
        raise ValueError("Empty VEP response")

    data = response[0]

    # Parse transcript consequences
    transcript_consequences = []
    for tc in data.get("transcript_consequences", []):
        # Extract AlphaMissense from nested dict
        am = tc.get("alphamissense", {}) or {}

        # Extract MANE info
        mane_list = tc.get("mane", []) or []

        transcript_consequences.append(TranscriptConsequence(
            transcript_id=tc.get("transcript_id", ""),
            gene_symbol=tc.get("gene_symbol", ""),
            gene_id=tc.get("gene_id", ""),
            consequence_terms=tc.get("consequence_terms", []),
            impact=tc.get("impact", ""),
            biotype=tc.get("biotype", ""),
            canonical=tc.get("canonical", 0) == 1,
            mane_select=tc.get("mane_select") is not None or "MANE_Select" in mane_list,
            mane_plus_clinical="MANE_Plus_Clinical" in mane_list,
            amino_acids=tc.get("amino_acids"),
            codons=tc.get("codons"),
            protein_start=tc.get("protein_start"),
            protein_end=tc.get("protein_end"),
            protein_id=tc.get("protein_id"),
            hgvsc=tc.get("hgvsc"),
            hgvsp=tc.get("hgvsp"),
            sift_score=tc.get("sift_score"),
            sift_prediction=tc.get("sift_prediction"),
            polyphen_score=tc.get("polyphen_score"),
            polyphen_prediction=tc.get("polyphen_prediction"),
            cadd_phred=tc.get("cadd_phred"),
            cadd_raw=tc.get("cadd_raw"),
            revel_score=tc.get("revel"),
            alphamissense_pathogenicity=am.get("am_pathogenicity"),
            alphamissense_class=am.get("am_class"),
            blosum62=tc.get("blosum62"),
            clinpred=tc.get("clinpred"),
            eve_score=tc.get("eve_score"),
            eve_class=tc.get("eve_class"),
            spliceai=tc.get("spliceai"),
            loeuf=tc.get("loeuf"),
            phaplo=tc.get("phaplo"),
            ptriplo=tc.get("ptriplo"),
            lof=tc.get("lof"),
            lof_filter=tc.get("lof_filter"),
            lof_flags=tc.get("lof_flags"),
            lof_info=tc.get("lof_info"),
            nmd=tc.get("nmd"),
            phenotypes=tc.get("phenotypes"),
            uniprot_isoform=tc.get("uniprot_isoform"),
            swissprot=tc.get("swissprot"),
            trembl=tc.get("trembl"),
            uniparc=tc.get("uniparc"),
            distance=tc.get("distance"),
            strand=tc.get("strand"),
            source=tc.get("source"),
        ))

    # Parse colocated variants
    colocated_variants = []
    for cv in data.get("colocated_variants", []):
        # Parse frequencies
        frequencies = {}
        if "frequencies" in cv:
            freq_data = cv["frequencies"]
            # Get the alternate allele key
            for allele_key, allele_freqs in freq_data.items():
                if isinstance(allele_freqs, dict):
                    for pop_key, freq in allele_freqs.items():
                        frequencies[pop_key] = freq

        # Parse phenotypes - can be a list of dicts or an int (count)
        phenotype_data = cv.get("phenotype_or_disease", [])
        phenotypes = []
        if isinstance(phenotype_data, list):
            phenotypes = [p.get("trait") for p in phenotype_data if isinstance(p, dict) and p.get("trait")]

        colocated_variants.append(ColocatedVariant(
            id=cv.get("id", ""),
            allele_string=cv.get("allele_string"),
            clinical_significance=cv.get("clin_sig", []),
            pubmed_ids=cv.get("pubmed", []),
            frequencies=frequencies,
            phenotypes=phenotypes,
        ))

    return VEPAnnotation(
        input=data.get("input", data.get("id", "")),
        assembly=data.get("assembly_name", "GRCh38"),
        chromosome=str(data.get("seq_region_name", "")),
        start=data.get("start", 0),
        end=data.get("end", 0),
        strand=data.get("strand", 1),
        allele_string=data.get("allele_string", ""),
        most_severe_consequence=data.get("most_severe_consequence", ""),
        variant_class=data.get("variant_class"),
        transcript_consequences=transcript_consequences,
        colocated_variants=colocated_variants,
    )


def extract_pmids(annotation: VEPAnnotation) -> List[int]:
    """Extract all PMIDs from VEP annotation"""
    return annotation.pmids


def extract_clinical_info(annotation: VEPAnnotation) -> Dict[str, Any]:
    """Extract clinically relevant information from VEP annotation"""
    canonical = annotation.get_canonical_consequence()

    result = {
        "gene_symbol": annotation.gene_symbol,
        "chromosome": annotation.chromosome,
        "position": annotation.start,
        "consequence": annotation.most_severe_consequence,
        "variant_class": annotation.variant_class,
        "rsid": annotation.rsid,
        "clinical_significance": annotation.clinical_significance,
        "gnomad_af": annotation.gnomad_af,
        "pmids": annotation.pmids,
    }

    if canonical:
        result.update({
            "transcript_id": canonical.transcript_id,
            "protein_id": canonical.protein_id,
            "hgvsc": canonical.hgvsc,
            "hgvsp": canonical.hgvsp,
            "amino_acid_change": canonical.amino_acids,
            "protein_position": canonical.protein_start,
            "impact": canonical.impact,
            "sift": {"score": canonical.sift_score, "prediction": canonical.sift_prediction}
                if canonical.sift_score is not None else None,
            "polyphen": {"score": canonical.polyphen_score, "prediction": canonical.polyphen_prediction}
                if canonical.polyphen_score is not None else None,
            "cadd": {"phred": canonical.cadd_phred, "raw": canonical.cadd_raw}
                if canonical.cadd_phred is not None else None,
            "revel": canonical.revel_score,
            "alphamissense": {"pathogenicity": canonical.alphamissense_pathogenicity, "class": canonical.alphamissense_class}
                if canonical.alphamissense_pathogenicity is not None else None,
            "blosum62": canonical.blosum62,
            "clinpred": canonical.clinpred,
            "eve": {"score": canonical.eve_score, "class": canonical.eve_class}
                if canonical.eve_score is not None else None,
            "spliceai": canonical.spliceai,
            "loeuf": canonical.loeuf,
            "dosage_sensitivity": {"phaplo": canonical.phaplo, "ptriplo": canonical.ptriplo}
                if canonical.phaplo is not None or canonical.ptriplo is not None else None,
            "lof": canonical.lof,
            "nmd": canonical.nmd,
            "phenotypes": canonical.phenotypes,
        })

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Annotate genetic variants using Ensembl VEP REST API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "NM_000546.6:c.215C>G"
  %(prog)s rs1042522
  %(prog)s "chr17:7674220:C:T"
  %(prog)s "17-7674220-C-T"
  %(prog)s "NM_000546.6:c.215C>G" --json -o annotation.json
        """,
    )
    parser.add_argument(
        "variant",
        help="Variant notation (HGVS, rsID, or genomic coordinates)"
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output raw JSON"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path"
    )
    parser.add_argument(
        "--pmids-only",
        action="store_true",
        help="Only output PMIDs"
    )

    args = parser.parse_args()

    try:
        # Detect and display format
        format_type = VariantNotation.detect_format(args.variant)
        print(f"Detected format: {format_type}", file=sys.stderr)

        # Query VEP
        client = VEPClient()
        response = client.annotate(args.variant)

        # Parse response
        annotation = parse_vep_response(response)

        # Handle output
        if args.pmids_only:
            pmids = extract_pmids(annotation)
            output = "\n".join(str(p) for p in pmids)
        elif args.json:
            output = json.dumps(annotation.to_dict(), indent=2)
        else:
            # Human-readable output
            info = extract_clinical_info(annotation)
            lines = [
                f"Variant: {annotation.input}",
                f"Gene: {info['gene_symbol']}",
                f"Consequence: {info['consequence']}",
                f"Location: chr{info['chromosome']}:{info['position']}",
                f"Variant Class: {info.get('variant_class', 'N/A')}",
                "",
            ]

            if info.get("transcript_id"):
                lines.append(f"Transcript: {info['transcript_id']}")
            if info.get("protein_id"):
                lines.append(f"Protein: {info['protein_id']}")
            if info.get("hgvsc"):
                lines.append(f"HGVSc: {info['hgvsc']}")
            if info.get("hgvsp"):
                lines.append(f"HGVSp: {info['hgvsp']}")
            if info.get("amino_acid_change"):
                lines.append(f"Amino Acid Change: {info['amino_acid_change']}")
            if info.get("impact"):
                lines.append(f"Impact: {info['impact']}")

            lines.append("")

            if info.get("rsid"):
                lines.append(f"rsID: {info['rsid']}")
            if info.get("gnomad_af") is not None:
                lines.append(f"gnomAD AF: {info['gnomad_af']:.2e}")
            if info.get("clinical_significance"):
                lines.append(f"Clinical Significance: {', '.join(info['clinical_significance'])}")

            # In-silico predictors
            lines.append("\n--- In-Silico Predictors ---")
            if info.get("sift"):
                lines.append(f"SIFT: {info['sift']['prediction']} ({info['sift']['score']})")
            if info.get("polyphen"):
                lines.append(f"PolyPhen: {info['polyphen']['prediction']} ({info['polyphen']['score']})")
            if info.get("cadd"):
                lines.append(f"CADD: phred={info['cadd']['phred']}, raw={info['cadd']['raw']:.4f}")
            if info.get("revel") is not None:
                lines.append(f"REVEL: {info['revel']}")
            if info.get("alphamissense"):
                lines.append(f"AlphaMissense: {info['alphamissense']['class']} ({info['alphamissense']['pathogenicity']})")
            if info.get("clinpred") is not None:
                lines.append(f"ClinPred: {info['clinpred']:.6f}")
            if info.get("eve"):
                lines.append(f"EVE: {info['eve']['class']} ({info['eve']['score']:.4f})")
            if info.get("blosum62") is not None:
                lines.append(f"BLOSUM62: {info['blosum62']}")

            # Splicing
            if info.get("spliceai"):
                sa = info["spliceai"]
                lines.append("\n--- SpliceAI ---")
                lines.append(f"  Gene: {sa.get('SYMBOL', 'N/A')}")
                lines.append(f"  DS_AG={sa.get('DS_AG', 0):.2f}  DS_AL={sa.get('DS_AL', 0):.2f}  DS_DG={sa.get('DS_DG', 0):.2f}  DS_DL={sa.get('DS_DL', 0):.2f}")
                lines.append(f"  DP_AG={sa.get('DP_AG', 0)}  DP_AL={sa.get('DP_AL', 0)}  DP_DG={sa.get('DP_DG', 0)}  DP_DL={sa.get('DP_DL', 0)}")

            # Gene constraint
            if info.get("loeuf") is not None or info.get("dosage_sensitivity"):
                lines.append("\n--- Gene Constraint ---")
            if info.get("loeuf") is not None:
                lines.append(f"LOEUF: {info['loeuf']}")
            if info.get("dosage_sensitivity"):
                ds = info["dosage_sensitivity"]
                if ds.get("phaplo") is not None:
                    lines.append(f"pHaplo: {ds['phaplo']:.4f}")
                if ds.get("ptriplo") is not None:
                    lines.append(f"pTriplo: {ds['ptriplo']:.4f}")

            # LoF / NMD
            if info.get("lof"):
                lines.append(f"\nLoF (LOFTEE): {info['lof']}")
            if info.get("nmd"):
                lines.append(f"NMD: {info['nmd']}")

            # Phenotypes
            if info.get("phenotypes"):
                lines.append("\n--- Phenotypes ---")
                seen = set()
                for p in info["phenotypes"]:
                    pheno = p.get("phenotype", "")
                    source = p.get("source", "")
                    key = f"{pheno}|{source}"
                    if key not in seen and pheno:
                        seen.add(key)
                        lines.append(f"  [{source}] {pheno}")

            if info.get("pmids"):
                lines.append(f"\nAssociated PMIDs: {', '.join(str(p) for p in info['pmids'])}")

            output = "\n".join(lines)

        # Write output
        if args.output:
            with open(args.output, "w") as f:
                f.write(output)
            print(f"Output saved to {args.output}", file=sys.stderr)
        else:
            print(output)

        return 0

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except RuntimeError as e:
        print(f"API Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
