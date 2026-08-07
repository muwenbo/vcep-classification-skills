#!/usr/bin/env python3
"""
VEP Annotation Script

Query Ensembl VEP REST API for comprehensive variant annotation, with the
GeneBe public API as an automatic fallback when Ensembl is unavailable.
Supports HGVS notation, rsID, and genomic coordinates.

Usage:
    python vep_annotate.py "NM_000546.6:c.215C>G"
    python vep_annotate.py rs1042522
    python vep_annotate.py "chr17:7674220:C:T"
    python vep_annotate.py "17-7674220-C-T"
    python vep_annotate.py "chr4-1808989-A-T" --assembly hg19
    python vep_annotate.py "17-7674220-C-T" --source genebe
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

# GeneBe public API (fallback annotation source, no auth required at this volume)
GENEBE_API_URL = "https://api.genebe.net/cloud/api-public/v1"
# NCBI E-utilities, used only to resolve rsIDs for the GeneBe path
NCBI_EUTILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

# Consequence terms ordered most->least severe (Ensembl calculated variant
# consequence ranking). Used to derive most_severe_consequence and impact for
# sources that do not report them.
CONSEQUENCE_SEVERITY = [
    "transcript_ablation", "splice_acceptor_variant", "splice_donor_variant",
    "stop_gained", "frameshift_variant", "stop_lost", "start_lost",
    "transcript_amplification", "feature_elongation", "feature_truncation",
    "inframe_insertion", "inframe_deletion", "missense_variant",
    "protein_altering_variant", "splice_donor_5th_base_variant",
    "splice_region_variant", "splice_donor_region_variant",
    "splice_polypyrimidine_tract_variant", "incomplete_terminal_codon_variant",
    "start_retained_variant", "stop_retained_variant", "synonymous_variant",
    "coding_sequence_variant", "mature_miRNA_variant", "5_prime_UTR_variant",
    "3_prime_UTR_variant", "non_coding_transcript_exon_variant",
    "intron_variant", "NMD_transcript_variant", "non_coding_transcript_variant",
    "coding_transcript_variant", "upstream_gene_variant",
    "downstream_gene_variant", "TFBS_ablation", "TFBS_amplification",
    "TF_binding_site_variant", "regulatory_region_ablation",
    "regulatory_region_amplification", "regulatory_region_variant",
    "intergenic_variant", "sequence_variant",
]

CONSEQUENCE_IMPACT = {
    **{t: "HIGH" for t in CONSEQUENCE_SEVERITY[:10]},
    **{t: "MODERATE" for t in ("inframe_insertion", "inframe_deletion",
                               "missense_variant", "protein_altering_variant")},
    **{t: "LOW" for t in ("splice_donor_5th_base_variant", "splice_region_variant",
                          "splice_donor_region_variant",
                          "splice_polypyrimidine_tract_variant",
                          "incomplete_terminal_codon_variant",
                          "start_retained_variant", "stop_retained_variant",
                          "synonymous_variant")},
}


def most_severe(terms: List[str]) -> str:
    """Pick the most severe consequence term from a list."""
    if not terms:
        return ""
    return min(terms, key=lambda t: CONSEQUENCE_SEVERITY.index(t)
               if t in CONSEQUENCE_SEVERITY else len(CONSEQUENCE_SEVERITY))


def impact_for(terms: List[str]) -> str:
    """Derive the VEP impact rating from consequence terms."""
    return CONSEQUENCE_IMPACT.get(most_severe(terms), "MODIFIER")

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
    # --- Predictors only reported by the GeneBe fallback ---
    bayesdel_noaf_score: Optional[float] = None
    bayesdel_noaf_prediction: Optional[str] = None
    phylop100way_score: Optional[float] = None
    dbscsnv_ada_score: Optional[float] = None


@dataclass
class ColocatedVariant:
    """Known variant at the same position"""
    id: str
    allele_string: Optional[str] = None
    clinical_significance: List[str] = field(default_factory=list)
    pubmed_ids: List[int] = field(default_factory=list)
    frequencies: Dict[str, float] = field(default_factory=dict)


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
    # Which API produced this annotation: "ensembl_vep" or "genebe"
    annotation_source: str = "ensembl_vep"
    # Assembly of the *input* coordinates (may differ from `assembly` if lifted over)
    input_assembly: Optional[str] = None
    # Third-party automated ACMG call (GeneBe only). Advisory context, NOT a
    # VCEP classification - never substitute this for the skill's own workflow.
    external_acmg: Optional[Dict[str, Any]] = None
    # ClinVar review status / submission summary (GeneBe only)
    clinvar_review_status: Optional[str] = None
    clinvar_conditions: List[str] = field(default_factory=list)

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
            "annotation_source": self.annotation_source,
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

        if self.input_assembly and self.input_assembly != self.assembly:
            result["input_assembly"] = self.input_assembly
            result["lifted_over"] = True
        if self.clinvar_review_status:
            result["clinvar_review_status"] = self.clinvar_review_status
        if self.clinvar_conditions:
            result["clinvar_conditions"] = self.clinvar_conditions
        if self.external_acmg:
            result["external_acmg"] = self.external_acmg

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
            if canonical.bayesdel_noaf_score is not None:
                ct["bayesdel_noaf"] = {"score": canonical.bayesdel_noaf_score,
                                       "prediction": canonical.bayesdel_noaf_prediction}
            if canonical.phylop100way_score is not None:
                ct["phylop100way"] = canonical.phylop100way_score
            if canonical.dbscsnv_ada_score is not None:
                ct["dbscsnv_ada"] = canonical.dbscsnv_ada_score
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

        colocated_variants.append(ColocatedVariant(
            id=cv.get("id", ""),
            allele_string=cv.get("allele_string"),
            clinical_significance=cv.get("clin_sig", []),
            pubmed_ids=cv.get("pubmed", []),
            frequencies=frequencies,
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


class GeneBeClient:
    """Client for the GeneBe public annotation API (Ensembl VEP fallback).

    GeneBe only accepts genomic coordinates, so HGVS is resolved through its
    /hgvs endpoint and rsIDs through NCBI E-utilities first. Results are always
    reported on GRCh38 - hg19 input is lifted over by GeneBe.
    """

    def __init__(self, base_url: str = GENEBE_API_URL, assembly: str = "hg38"):
        self.base_url = base_url
        self.assembly = assembly
        self.session = create_session()
        self._last_request_time = 0

    def _rate_limit(self):
        elapsed = time.time() - self._last_request_time
        if elapsed < RATE_LIMIT_DELAY:
            time.sleep(RATE_LIMIT_DELAY - elapsed)
        self._last_request_time = time.time()

    def _get(self, url: str, params: Dict) -> Any:
        self._rate_limit()
        try:
            response = self.session.get(url, params=params, timeout=60)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"GeneBe API request failed: {e}")
        except ValueError as e:
            raise RuntimeError(f"GeneBe API returned non-JSON response: {e}")

    def resolve_hgvs(self, hgvs: str) -> Tuple[str, int, str, str]:
        """Resolve HGVS notation to genomic coordinates via GeneBe /hgvs."""
        data = self._get(f"{self.base_url}/hgvs",
                         {"hgvs": hgvs, "genome": self.assembly})
        if not data or not isinstance(data, list):
            raise RuntimeError(f"GeneBe could not resolve HGVS: {hgvs}")
        entry = data[0]
        if entry.get("errorMsg"):
            raise RuntimeError(f"GeneBe could not resolve HGVS {hgvs}: {entry['errorMsg']}")
        return str(entry["chr"]), int(entry["pos"]), entry["ref"], entry["alt"]

    def resolve_rsid(self, rsid: str) -> Tuple[str, int, str, str]:
        """Resolve an rsID to GRCh38 coordinates via NCBI dbSNP esummary.

        GeneBe has no rsID endpoint, so this hop is required. dbSNP reports
        SPDI (0-based); multi-allelic rsIDs use the first alternate allele.
        """
        self._rate_limit()
        data = self._get(f"{NCBI_EUTILS_URL}/esummary.fcgi", {
            "db": "snp", "id": rsid.lower().lstrip("rs"), "retmode": "json",
        })
        doc = (data.get("result") or {}).get(rsid.lower().lstrip("rs"))
        if not doc or not doc.get("spdi"):
            raise RuntimeError(f"dbSNP has no coordinates for {rsid}")
        spdis = doc["spdi"].split(",")
        if len(spdis) > 1:
            print(f"Warning: {rsid} is multi-allelic; using first alternate allele",
                  file=sys.stderr)
        _, pos0, ref, alt = spdis[0].split(":")
        chrom = str(doc.get("chr") or "")
        return chrom, int(pos0) + 1, ref, alt

    def annotate_genomic(self, chrom: str, pos: int, ref: str, alt: str) -> Dict:
        """Annotate a variant by genomic coordinates."""
        chrom = str(chrom)
        if not chrom.startswith("chr"):
            chrom = f"chr{chrom}"
        return self._get(f"{self.base_url}/variant", {
            "chr": chrom, "pos": pos, "ref": ref, "alt": alt,
            "genome": self.assembly, "useRefseq": "true",
        })

    def annotate(self, notation: str) -> Dict:
        """Annotate a variant using auto-detected notation format."""
        format_type = VariantNotation.detect_format(notation)

        if format_type == "genomic":
            chrom, pos, ref, alt = VariantNotation.parse_genomic(notation)
        elif format_type == "hgvs":
            chrom, pos, ref, alt = self.resolve_hgvs(notation)
        elif format_type == "rsid":
            if self.assembly != "hg38":
                raise RuntimeError(
                    "rsID lookup via the GeneBe fallback resolves GRCh38 "
                    "coordinates only; use --assembly hg38 or supply coordinates"
                )
            chrom, pos, ref, alt = self.resolve_rsid(notation)
        else:
            raise ValueError(f"Unrecognized variant notation format: {notation}")

        return self.annotate_genomic(chrom, pos, ref, alt)


def _variant_class(ref: str, alt: str) -> str:
    """Derive a VEP-style variant_class from ref/alt alleles."""
    if len(ref) == len(alt):
        return "SNV" if len(ref) == 1 else "substitution"
    if len(ref) < len(alt):
        return "insertion"
    return "deletion"


def parse_genebe_response(response: Dict, input_notation: str,
                          input_assembly: str = "hg38") -> VEPAnnotation:
    """Parse a GeneBe /variant response into the shared VEPAnnotation schema.

    GeneBe reports predictors at variant level rather than per transcript, so
    those scores are attached to every transcript consequence.
    """
    variants = (response or {}).get("variants") or []
    if not variants:
        msg = (response or {}).get("message") or "no variants returned"
        raise ValueError(f"Empty GeneBe response: {msg}")

    v = variants[0]

    # Variant-level predictors, replicated onto each transcript consequence
    predictors = {
        "revel_score": v.get("revel_score"),
        "alphamissense_pathogenicity": v.get("alphamissense_score"),
        "alphamissense_class": v.get("alphamissense_prediction"),
        "bayesdel_noaf_score": v.get("bayesdelnoaf_score"),
        "bayesdel_noaf_prediction": v.get("bayesdelnoaf_prediction"),
        "phylop100way_score": v.get("phylop100way_score"),
        "dbscsnv_ada_score": v.get("dbscsnv_ada_score"),
    }
    if v.get("spliceai_max_score") is not None:
        # GeneBe reports only the max delta score, not the four DS_* components
        predictors["spliceai"] = {
            "max_score": v["spliceai_max_score"],
            "prediction": v.get("spliceai_max_prediction"),
            "source": "genebe",
        }

    transcript_consequences = []
    for c in v.get("consequences", []):
        terms = c.get("consequences", []) or []
        transcript = c.get("transcript", "") or ""
        aa_ref, aa_alt = c.get("aa_ref"), c.get("aa_alt")
        hgvs_c, hgvs_p = c.get("hgvs_c"), c.get("hgvs_p")
        protein_id = c.get("protein_id")

        transcript_consequences.append(TranscriptConsequence(
            transcript_id=transcript,
            gene_symbol=c.get("gene_symbol", "") or "",
            gene_id=f"HGNC:{c['gene_hgnc_id']}" if c.get("gene_hgnc_id") else "",
            consequence_terms=terms,
            impact=impact_for(terms),
            biotype=c.get("biotype", "") or "",
            canonical=bool(c.get("canonical")),
            # GeneBe marks a MANE pair by naming the partner transcript
            mane_select=c.get("mane_select") is not None,
            mane_plus_clinical=c.get("mane_plus") is not None,
            amino_acids=f"{aa_ref}/{aa_alt}" if aa_ref and aa_alt else None,
            protein_start=c.get("aa_start"),
            protein_end=c.get("aa_end") or c.get("aa_start"),
            protein_id=protein_id,
            hgvsc=f"{transcript}:{hgvs_c}" if hgvs_c else None,
            hgvsp=f"{protein_id or transcript}:{hgvs_p}" if hgvs_p else None,
            strand=1 if c.get("strand") else -1,
            source="RefSeq" if transcript.startswith(("NM_", "NR_", "XM_")) else "Ensembl",
            **predictors,
        ))

    # Collapse GeneBe's flat ClinVar/gnomAD fields into a single colocated variant
    frequencies = {}
    if v.get("gnomad_genomes_af") is not None:
        frequencies["gnomadg"] = v["gnomad_genomes_af"]
    if v.get("gnomad_exomes_af") is not None:
        frequencies["gnomade"] = v["gnomad_exomes_af"]

    colocated_variants = []
    if v.get("dbsnp") or frequencies or v.get("clinvar_classification"):
        colocated_variants.append(ColocatedVariant(
            id=v.get("dbsnp") or "",
            allele_string=f"{v.get('ref')}/{v.get('alt')}",
            clinical_significance=(
                [v["clinvar_classification"]] if v.get("clinvar_classification") else []
            ),
            frequencies=frequencies,
        ))

    external_acmg = None
    if v.get("acmg_classification"):
        external_acmg = {
            "source": "GeneBe automated ACMG (advisory only - not a VCEP call)",
            "classification": v["acmg_classification"],
            "score": v.get("acmg_score"),
            "criteria": [c for c in (v.get("acmg_criteria") or "").split(",") if c],
            "by_gene": v.get("acmg_by_gene") or [],
        }

    ref, alt = v.get("ref", ""), v.get("alt", "")
    pos = int(v.get("pos", 0))
    # VEP reports the most severe consequence across all transcripts; GeneBe's
    # `effect` covers only its own selected transcript, so take the union.
    terms = sorted({t for tc in transcript_consequences for t in tc.consequence_terms}
                   or {t for t in (v.get("effect") or "").split(",") if t})

    return VEPAnnotation(
        input=input_notation,
        assembly="GRCh38",
        input_assembly="GRCh37" if input_assembly == "hg19" else "GRCh38",
        chromosome=str(v.get("chr", "")),
        start=pos,
        end=pos + max(len(ref) - 1, 0),
        strand=1,
        allele_string=f"{ref}/{alt}",
        most_severe_consequence=most_severe(terms),
        variant_class=_variant_class(ref, alt),
        transcript_consequences=transcript_consequences,
        colocated_variants=colocated_variants,
        annotation_source="genebe",
        external_acmg=external_acmg,
        clinvar_review_status=v.get("clinvar_review_status"),
        clinvar_conditions=[
            d for d in (v.get("clinvar_disease") or "").split(",") if d
        ],
    )


def annotate_variant(notation: str, source: str = "auto",
                     assembly: str = "hg38") -> VEPAnnotation:
    """Annotate a variant, falling back from Ensembl VEP to GeneBe.

    source: "auto" (Ensembl, then GeneBe on failure), "ensembl", or "genebe".
    """
    if source in ("auto", "ensembl"):
        if assembly != "hg38" and source == "ensembl":
            raise ValueError(
                "Ensembl VEP REST is GRCh38-only here; use --source genebe "
                "or auto for hg19 input"
            )
        if assembly == "hg38":
            try:
                return parse_vep_response(VEPClient().annotate(notation))
            except (RuntimeError, ValueError) as e:
                if source == "ensembl":
                    raise
                print(f"Ensembl VEP failed ({e}); falling back to GeneBe",
                      file=sys.stderr)
        else:
            print(f"Assembly {assembly} not supported by Ensembl VEP path; "
                  "using GeneBe", file=sys.stderr)

    client = GeneBeClient(assembly=assembly)
    return parse_genebe_response(client.annotate(notation), notation, assembly)


def extract_pmids(annotation: VEPAnnotation) -> List[int]:
    """Extract all PMIDs from VEP annotation"""
    return annotation.pmids


def extract_clinical_info(annotation: VEPAnnotation) -> Dict[str, Any]:
    """Extract clinically relevant information from VEP annotation"""
    canonical = annotation.get_canonical_consequence()

    result = {
        "annotation_source": annotation.annotation_source,
        "gene_symbol": annotation.gene_symbol,
        "chromosome": annotation.chromosome,
        "position": annotation.start,
        "consequence": annotation.most_severe_consequence,
        "variant_class": annotation.variant_class,
        "rsid": annotation.rsid,
        "clinical_significance": annotation.clinical_significance,
        "gnomad_af": annotation.gnomad_af,
        "pmids": annotation.pmids,
        "clinvar_review_status": annotation.clinvar_review_status,
        "external_acmg": annotation.external_acmg,
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
            "bayesdel_noaf": {"score": canonical.bayesdel_noaf_score, "prediction": canonical.bayesdel_noaf_prediction}
                if canonical.bayesdel_noaf_score is not None else None,
            "phylop100way": canonical.phylop100way_score,
            "dbscsnv_ada": canonical.dbscsnv_ada_score,
        })

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Annotate genetic variants using Ensembl VEP REST API "
                    "(GeneBe public API as automatic fallback)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "NM_000546.6:c.215C>G"
  %(prog)s rs1042522
  %(prog)s "chr17:7674220:C:T"
  %(prog)s "17-7674220-C-T"
  %(prog)s "NM_000546.6:c.215C>G" --json -o annotation.json
  %(prog)s "chr4-1808989-A-T" --assembly hg19     # GeneBe lifts over to GRCh38
  %(prog)s "17-7674220-C-T" --source genebe       # force the fallback source
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
    parser.add_argument(
        "--source",
        choices=["auto", "ensembl", "genebe"],
        default="auto",
        help="Annotation source: auto (Ensembl VEP, GeneBe on failure), "
             "ensembl (no fallback), or genebe (default: auto)"
    )
    parser.add_argument(
        "--assembly",
        choices=["hg38", "hg19"],
        default="hg38",
        help="Assembly of the input coordinates. hg19 routes to GeneBe, which "
             "lifts results over to GRCh38 (default: hg38)"
    )

    args = parser.parse_args()

    try:
        # Detect and display format
        format_type = VariantNotation.detect_format(args.variant)
        print(f"Detected format: {format_type}", file=sys.stderr)

        # Query the annotation source (with fallback when source=auto)
        annotation = annotate_variant(args.variant, args.source, args.assembly)
        print(f"Annotation source: {annotation.annotation_source}", file=sys.stderr)

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
                f"Source: {annotation.annotation_source}",
                f"Gene: {info['gene_symbol']}",
                f"Consequence: {info['consequence']}",
                f"Location: chr{info['chromosome']}:{info['position']} ({annotation.assembly})",
                f"Variant Class: {info.get('variant_class', 'N/A')}",
                "",
            ]
            if annotation.input_assembly and annotation.input_assembly != annotation.assembly:
                lines.insert(5, f"(input given on {annotation.input_assembly}, lifted over)")

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
            if info.get("clinvar_review_status"):
                lines.append(f"ClinVar Review Status: {info['clinvar_review_status']}")
            if annotation.clinvar_conditions:
                lines.append(f"ClinVar Conditions: {', '.join(annotation.clinvar_conditions)}")

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
                am = info["alphamissense"]
                lines.append(f"AlphaMissense: {am['class']} ({am['pathogenicity']})"
                             if am.get("class") else f"AlphaMissense: {am['pathogenicity']}")
            if info.get("clinpred") is not None:
                lines.append(f"ClinPred: {info['clinpred']:.6f}")
            if info.get("eve"):
                lines.append(f"EVE: {info['eve']['class']} ({info['eve']['score']:.4f})")
            if info.get("blosum62") is not None:
                lines.append(f"BLOSUM62: {info['blosum62']}")
            if info.get("bayesdel_noaf"):
                bd = info["bayesdel_noaf"]
                lines.append(f"BayesDel (noAF): {bd['prediction']} ({bd['score']})")
            if info.get("phylop100way") is not None:
                lines.append(f"phyloP100way: {info['phylop100way']}")

            # Splicing
            if info.get("spliceai"):
                sa = info["spliceai"]
                lines.append("\n--- SpliceAI ---")
                if sa.get("source") == "genebe":
                    # GeneBe reports only the max delta score
                    lines.append(f"  max delta score = {sa.get('max_score')} ({sa.get('prediction')})")
                else:
                    lines.append(f"  Gene: {sa.get('SYMBOL', 'N/A')}")
                    lines.append(f"  DS_AG={sa.get('DS_AG', 0):.2f}  DS_AL={sa.get('DS_AL', 0):.2f}  DS_DG={sa.get('DS_DG', 0):.2f}  DS_DL={sa.get('DS_DL', 0):.2f}")
                    lines.append(f"  DP_AG={sa.get('DP_AG', 0)}  DP_AL={sa.get('DP_AL', 0)}  DP_DG={sa.get('DP_DG', 0)}  DP_DL={sa.get('DP_DL', 0)}")
            if info.get("dbscsnv_ada") is not None:
                lines.append(f"dbscSNV ada: {info['dbscsnv_ada']:.4f}")

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

            if info.get("pmids"):
                lines.append(f"\nAssociated PMIDs: {', '.join(str(p) for p in info['pmids'])}")

            # Third-party automated ACMG call - context only, never a VCEP verdict
            if info.get("external_acmg"):
                ea = info["external_acmg"]
                lines.append("\n--- External automated ACMG (GeneBe) ---")
                lines.append("  ADVISORY ONLY - not a VCEP classification. Do not")
                lines.append("  substitute for this skill's own criteria evaluation.")
                lines.append(f"  Classification: {ea['classification']} (score {ea.get('score')})")
                if ea.get("criteria"):
                    lines.append(f"  Criteria: {', '.join(ea['criteria'])}")

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
