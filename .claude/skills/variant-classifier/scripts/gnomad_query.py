#!/usr/bin/env python3
"""
Unified gnomAD Query Module

Query gnomAD for variant population frequency data using the GraphQL API.
Supports three query modes:
- Single variant by ID (e.g., "17-7674220-C-T")
- All variants in a gene (e.g., "TP53")
- All variants in a genomic region (e.g., chr17:7661779-7687538)

Usage:
    # As CLI
    python gnomad_query.py variant 17-7674220-C-T
    python gnomad_query.py gene TP53
    python gnomad_query.py region 17:7674200-7674400

    # As module
    from gnomad_query import GnomadClient
    client = GnomadClient()
    variant = client.query_variant("17-7674220-C-T")
    variants = client.query_gene("TP53")
    variants = client.query_region("17", 7674200, 7674400)
"""

import argparse
import json
import logging
import re
import sys
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# gnomAD GraphQL API endpoint
GNOMAD_API_URL = "https://gnomad.broadinstitute.org/api"

# Dataset to reference genome mapping
DATASET_GENOME_MAP = {
    "gnomad_r4": "GRCh38",
    "gnomad_r3": "GRCh38",
    "gnomad_r2_1": "GRCh37",
    "gnomad_r2_1_non_neuro": "GRCh37",
    "gnomad_r2_1_non_cancer": "GRCh37",
    "gnomad_r2_1_non_topmed": "GRCh37",
}


@dataclass
class PopulationFrequency:
    """Population-specific frequency data"""
    id: str
    ac: int = 0
    an: int = 0
    ac_hom: int = 0
    ac_hemi: int = 0

    @property
    def af(self) -> Optional[float]:
        """Calculate allele frequency"""
        return self.ac / self.an if self.an > 0 else None


@dataclass
class FrequencyData:
    """Frequency data from exome or genome"""
    ac: Optional[int] = None
    an: Optional[int] = None
    ac_hom: Optional[int] = None
    ac_hemi: Optional[int] = None
    filters: List[str] = field(default_factory=list)
    populations: List[PopulationFrequency] = field(default_factory=list)

    @property
    def af(self) -> Optional[float]:
        """Calculate allele frequency"""
        if self.ac is not None and self.an and self.an > 0:
            return self.ac / self.an
        return None

    def get_population_af(self, pop_id: str) -> Optional[float]:
        """Get allele frequency for a specific population"""
        for pop in self.populations:
            if pop.id == pop_id:
                return pop.af
        return None


@dataclass
class TranscriptConsequence:
    """Transcript consequence annotation"""
    gene_id: Optional[str] = None
    gene_symbol: Optional[str] = None
    transcript_id: Optional[str] = None
    hgvsc: Optional[str] = None
    hgvsp: Optional[str] = None
    consequence: Optional[str] = None
    canonical: bool = False


@dataclass
class InSilicoPredictor:
    """In silico prediction score"""
    id: str
    value: str

    @property
    def score(self) -> Optional[float]:
        """Parse value as float if possible"""
        try:
            return float(self.value)
        except (ValueError, TypeError):
            return None


@dataclass
class VariantInfo:
    """Comprehensive variant information from gnomAD"""
    variant_id: str
    chrom: str
    pos: int
    ref: str
    alt: str

    # Identifiers
    rsids: List[str] = field(default_factory=list)

    # Frequency data
    exome: Optional[FrequencyData] = None
    genome: Optional[FrequencyData] = None

    # Annotations (available in single variant query)
    transcript_consequences: List[TranscriptConsequence] = field(default_factory=list)
    in_silico_predictors: List[InSilicoPredictor] = field(default_factory=list)

    # Shortcut annotations (available in region/gene queries)
    gene_symbol: Optional[str] = None
    consequence: Optional[str] = None
    transcript_id: Optional[str] = None
    hgvsc: Optional[str] = None
    hgvsp: Optional[str] = None

    @property
    def rsid(self) -> Optional[str]:
        """Get first rsID if available"""
        return self.rsids[0] if self.rsids else None

    @property
    def exome_af(self) -> Optional[float]:
        """Get exome allele frequency"""
        return self.exome.af if self.exome else None

    @property
    def genome_af(self) -> Optional[float]:
        """Get genome allele frequency"""
        return self.genome.af if self.genome else None

    @property
    def max_af(self) -> Optional[float]:
        """Get maximum allele frequency across exome and genome"""
        afs = [af for af in [self.exome_af, self.genome_af] if af is not None]
        return max(afs) if afs else None

    @property
    def joint_af(self) -> Optional[float]:
        """Calculate joint allele frequency (combined exome + genome)"""
        exome_ac = self.exome.ac if self.exome and self.exome.ac is not None else 0
        exome_an = self.exome.an if self.exome and self.exome.an else 0
        genome_ac = self.genome.ac if self.genome and self.genome.ac is not None else 0
        genome_an = self.genome.an if self.genome and self.genome.an else 0

        total_an = exome_an + genome_an
        if total_an > 0:
            return (exome_ac + genome_ac) / total_an
        return None

    def get_canonical_consequence(self) -> Optional[TranscriptConsequence]:
        """Get canonical transcript consequence"""
        if self.transcript_consequences:
            canonical = next(
                (tc for tc in self.transcript_consequences if tc.canonical),
                self.transcript_consequences[0]
            )
            return canonical
        return None

    def get_predictor_score(self, predictor_id: str) -> Optional[float]:
        """Get in silico predictor score by ID (e.g., 'cadd', 'revel_max')"""
        for pred in self.in_silico_predictors:
            if pred.id == predictor_id:
                return pred.score
        return None

    def get_max_population_af(self, source: str = "exome") -> Optional[Tuple[str, float]]:
        """Get maximum population AF and the population ID"""
        freq_data = self.exome if source == "exome" else self.genome
        if not freq_data or not freq_data.populations:
            return None

        max_pop = None
        max_af = 0.0
        for pop in freq_data.populations:
            # Skip sex-stratified populations (XX, XY)
            if pop.id.endswith("_XX") or pop.id.endswith("_XY") or pop.id in ("XX", "XY"):
                continue
            if pop.af is not None and pop.af > max_af:
                max_af = pop.af
                max_pop = pop.id

        return (max_pop, max_af) if max_pop else None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            "variant_id": self.variant_id,
            "chrom": self.chrom,
            "pos": self.pos,
            "ref": self.ref,
            "alt": self.alt,
            "rsids": self.rsids,
            "rsid": self.rsid,
            "gene_symbol": self.gene_symbol or (self.get_canonical_consequence().gene_symbol if self.get_canonical_consequence() else None),
            "consequence": self.consequence or (self.get_canonical_consequence().consequence if self.get_canonical_consequence() else None),
            "hgvsc": self.hgvsc or (self.get_canonical_consequence().hgvsc if self.get_canonical_consequence() else None),
            "hgvsp": self.hgvsp or (self.get_canonical_consequence().hgvsp if self.get_canonical_consequence() else None),
            "exome_ac": self.exome.ac if self.exome else None,
            "exome_an": self.exome.an if self.exome else None,
            "exome_af": self.exome_af,
            "genome_ac": self.genome.ac if self.genome else None,
            "genome_an": self.genome.an if self.genome else None,
            "genome_af": self.genome_af,
            "max_af": self.max_af,
            "joint_af": self.joint_af,
        }


@dataclass
class GeneInfo:
    """Gene information from gnomAD"""
    gene_id: str
    symbol: str
    name: Optional[str] = None
    chrom: Optional[str] = None
    start: Optional[int] = None
    stop: Optional[int] = None
    variants: List[VariantInfo] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            "gene_id": self.gene_id,
            "symbol": self.symbol,
            "name": self.name,
            "chrom": self.chrom,
            "start": self.start,
            "stop": self.stop,
            "variant_count": len(self.variants),
        }


class GnomadQueryError(Exception):
    """Custom exception for gnomAD query errors"""
    pass


class GnomadClient:
    """
    Client for querying gnomAD GraphQL API.

    Supports three query modes:
    - query_variant(): Query a single variant by ID
    - query_gene(): Query all variants in a gene
    - query_region(): Query all variants in a genomic region

    Example:
        client = GnomadClient()

        # Query single variant
        variant = client.query_variant("17-7674220-C-T")
        print(f"AF: {variant.max_af}")

        # Query gene
        gene = client.query_gene("TP53")
        print(f"Found {len(gene.variants)} variants in {gene.symbol}")

        # Query region
        variants = client.query_region("17", 7674200, 7674400)
        rare = [v for v in variants if v.max_af and v.max_af < 0.001]
    """

    def __init__(self, api_url: str = GNOMAD_API_URL):
        self.api_url = api_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "User-Agent": "gnomad-query/1.0",
        })

    def _execute_query(self, query: str, timeout: int = 60) -> Dict[str, Any]:
        """Execute a GraphQL query and return the response data."""
        try:
            response = self.session.post(
                self.api_url,
                json={"query": query},
                timeout=timeout
            )
            response.raise_for_status()
            data = response.json()

            if "errors" in data:
                error_msg = "; ".join([e.get("message", str(e)) for e in data["errors"]])
                raise GnomadQueryError(f"GraphQL errors: {error_msg}")

            return data.get("data", {})

        except requests.RequestException as e:
            raise GnomadQueryError(f"Network error: {str(e)}")
        except json.JSONDecodeError as e:
            raise GnomadQueryError(f"Invalid JSON response: {str(e)}")

    @staticmethod
    def parse_variant_id(variant_id: str) -> Tuple[str, int, str, str]:
        """
        Parse variant ID into components.

        Supports formats:
        - 1-12345-A-T (gnomAD format)
        - chr1:12345:A:T
        - 1:12345:A>T

        Returns:
            Tuple of (chromosome, position, reference, alternate)
        """
        # Remove 'chr' prefix if present
        variant_id = variant_id.replace("chr", "")

        patterns = [
            r"^(\w+)-(\d+)-([ATCGN]+)-([ATCGN]+)$",  # 1-12345-A-T (gnomAD format)
            r"^(\w+)[:](\d+)[:]([ATCGN]+)[:]([ATCGN]+)$",  # 1:12345:A:T
            r"^(\w+)[:](\d+)[:]([ATCGN]+)>([ATCGN]+)$",  # 1:12345:A>T
            r"^(\w+)[_](\d+)[_]([ATCGN]+)[_]([ATCGN]+)$",  # 1_12345_A_T
        ]

        for pattern in patterns:
            match = re.match(pattern, variant_id.upper())
            if match:
                chrom, pos, ref, alt = match.groups()
                return chrom, int(pos), ref, alt

        raise ValueError(f"Unable to parse variant ID: {variant_id}")

    @staticmethod
    def normalize_variant_id(variant_id: str) -> str:
        """Normalize variant ID to gnomAD format (chrom-pos-ref-alt)"""
        chrom, pos, ref, alt = GnomadClient.parse_variant_id(variant_id)
        return f"{chrom}-{pos}-{ref}-{alt}"

    @staticmethod
    def parse_region(region_str: str) -> Tuple[str, int, int]:
        """
        Parse region string into components.

        Supports formats:
        - chr1:12345-67890
        - 1:12345-67890
        - 1-12345-67890

        Returns:
            Tuple of (chromosome, start, stop)
        """
        region_str = region_str.replace("chr", "")

        patterns = [
            r"^(\w+):(\d+)-(\d+)$",  # 1:12345-67890
            r"^(\w+)-(\d+)-(\d+)$",  # 1-12345-67890
        ]

        for pattern in patterns:
            match = re.match(pattern, region_str)
            if match:
                chrom, start, stop = match.groups()
                return chrom, int(start), int(stop)

        raise ValueError(f"Unable to parse region: {region_str}")

    def _parse_frequency_data(self, data: Optional[Dict]) -> Optional[FrequencyData]:
        """Parse frequency data from API response"""
        if not data:
            return None

        populations = []
        for pop in data.get("populations", []):
            populations.append(PopulationFrequency(
                id=pop.get("id", ""),
                ac=pop.get("ac", 0),
                an=pop.get("an", 0),
                ac_hom=pop.get("ac_hom", 0),
                ac_hemi=pop.get("ac_hemi", 0),
            ))

        return FrequencyData(
            ac=data.get("ac"),
            an=data.get("an"),
            ac_hom=data.get("ac_hom"),
            ac_hemi=data.get("ac_hemi"),
            filters=data.get("filters", []),
            populations=populations,
        )

    def _parse_variant_from_region_or_gene(self, data: Dict) -> VariantInfo:
        """Parse variant data from region or gene query response"""
        variant_id = data.get("variantId", "")
        parts = variant_id.split("-")

        if len(parts) >= 4:
            chrom, pos, ref, alt = parts[0], int(parts[1]), parts[2], "-".join(parts[3:])
        else:
            chrom = data.get("chrom", "")
            pos = data.get("pos", 0)
            ref = data.get("ref", "")
            alt = data.get("alt", "")

        return VariantInfo(
            variant_id=variant_id,
            chrom=chrom,
            pos=pos,
            ref=ref,
            alt=alt,
            rsids=data.get("rsids", []),
            exome=self._parse_frequency_data(data.get("exome")),
            genome=self._parse_frequency_data(data.get("genome")),
            gene_symbol=data.get("gene_symbol"),
            consequence=data.get("consequence"),
            transcript_id=data.get("transcript_id"),
            hgvsc=data.get("hgvsc"),
            hgvsp=data.get("hgvsp"),
        )

    def _parse_variant_from_single_query(self, data: Dict) -> VariantInfo:
        """Parse variant data from single variant query response"""
        variant_id = data.get("variantId", "")
        parts = variant_id.split("-")

        if len(parts) >= 4:
            chrom, pos, ref, alt = parts[0], int(parts[1]), parts[2], "-".join(parts[3:])
        else:
            chrom = data.get("chrom", "")
            pos = data.get("pos", 0)
            ref = data.get("ref", "")
            alt = data.get("alt", "")

        # Parse transcript consequences
        transcript_consequences = []
        for tc in data.get("transcript_consequences", []):
            transcript_consequences.append(TranscriptConsequence(
                gene_id=tc.get("gene_id"),
                gene_symbol=tc.get("gene_symbol"),
                transcript_id=tc.get("transcript_id"),
                hgvsc=tc.get("hgvsc"),
                hgvsp=tc.get("hgvsp"),
                consequence=tc.get("major_consequence"),
                canonical=tc.get("canonical", False),
            ))

        # Parse in silico predictors
        in_silico_predictors = []
        for pred in data.get("in_silico_predictors", []) or []:
            in_silico_predictors.append(InSilicoPredictor(
                id=pred.get("id", ""),
                value=pred.get("value", ""),
            ))

        return VariantInfo(
            variant_id=variant_id,
            chrom=chrom,
            pos=pos,
            ref=ref,
            alt=alt,
            rsids=data.get("rsids", []),
            exome=self._parse_frequency_data(data.get("exome")),
            genome=self._parse_frequency_data(data.get("genome")),
            transcript_consequences=transcript_consequences,
            in_silico_predictors=in_silico_predictors,
        )

    # =========================================================================
    # Single Variant Query
    # =========================================================================

    def query_variant(
        self,
        variant_id: str,
        dataset: str = "gnomad_r4",
    ) -> Optional[VariantInfo]:
        """
        Query gnomAD for a single variant by ID.

        This query returns detailed information including transcript consequences
        and in silico predictor scores.

        Args:
            variant_id: Variant identifier (e.g., "17-7674220-C-T", "chr17:7674220:C:T")
            dataset: gnomAD dataset (gnomad_r4 for GRCh38, gnomad_r2_1 for GRCh37)

        Returns:
            VariantInfo object if found, None if variant not in gnomAD

        Example:
            variant = client.query_variant("17-7674220-C-T")
            if variant:
                print(f"AF: {variant.max_af}")
                print(f"CADD: {variant.get_predictor_score('cadd')}")
        """
        normalized_id = self.normalize_variant_id(variant_id)
        logger.info(f"Querying gnomAD for variant: {normalized_id} (dataset: {dataset})")

        query = """
        {
          variant(variantId: "%s", dataset: %s) {
            variantId
            chrom
            pos
            ref
            alt
            rsids
            exome {
              ac
              an
              ac_hom
              ac_hemi
              filters
              populations {
                id
                ac
                an
                ac_hom
                ac_hemi
              }
            }
            genome {
              ac
              an
              ac_hom
              ac_hemi
              filters
              populations {
                id
                ac
                an
                ac_hom
                ac_hemi
              }
            }
            transcript_consequences {
              gene_id
              gene_symbol
              transcript_id
              hgvsc
              hgvsp
              major_consequence
              canonical
            }
            in_silico_predictors {
              id
              value
            }
          }
        }
        """ % (normalized_id, dataset)

        try:
            data = self._execute_query(query)
            variant_data = data.get("variant")

            if not variant_data:
                logger.info(f"Variant {normalized_id} not found in gnomAD")
                return None

            return self._parse_variant_from_single_query(variant_data)

        except GnomadQueryError as e:
            # Check if this is just a "not found" error
            if "not found" in str(e).lower():
                return None
            raise

    # =========================================================================
    # Gene Query
    # =========================================================================

    def query_gene(
        self,
        gene_symbol: str,
        dataset: str = "gnomad_r4",
        reference_genome: str = "GRCh38",
    ) -> Optional[GeneInfo]:
        """
        Query gnomAD for all variants in a gene.

        Args:
            gene_symbol: Gene symbol (e.g., "TP53", "BRCA1")
            dataset: gnomAD dataset version
            reference_genome: Reference genome (GRCh38 or GRCh37)

        Returns:
            GeneInfo object with variants, None if gene not found

        Example:
            gene = client.query_gene("TP53")
            print(f"Found {len(gene.variants)} variants")
            rare = [v for v in gene.variants if v.max_af and v.max_af < 0.001]
        """
        logger.info(f"Querying gnomAD for gene: {gene_symbol} (dataset: {dataset})")

        query = """
        {
          gene(gene_symbol: "%s", reference_genome: %s) {
            gene_id
            symbol
            name
            chrom
            start
            stop
            variants(dataset: %s) {
              variantId
              pos
              ref
              alt
              rsids
              gene_symbol
              consequence
              transcript_id
              hgvsc
              hgvsp
              exome {
                ac
                an
                ac_hom
                ac_hemi
                filters
                populations {
                  id
                  ac
                  an
                }
              }
              genome {
                ac
                an
                ac_hom
                ac_hemi
                filters
                populations {
                  id
                  ac
                  an
                }
              }
            }
          }
        }
        """ % (gene_symbol, reference_genome, dataset)

        data = self._execute_query(query, timeout=120)
        gene_data = data.get("gene")

        if not gene_data:
            logger.info(f"Gene {gene_symbol} not found")
            return None

        variants = [
            self._parse_variant_from_region_or_gene(v)
            for v in gene_data.get("variants", [])
        ]

        logger.info(f"Found {len(variants)} variants in {gene_symbol}")

        return GeneInfo(
            gene_id=gene_data.get("gene_id", ""),
            symbol=gene_data.get("symbol", ""),
            name=gene_data.get("name"),
            chrom=gene_data.get("chrom"),
            start=gene_data.get("start"),
            stop=gene_data.get("stop"),
            variants=variants,
        )

    # =========================================================================
    # Region Query
    # =========================================================================

    def query_region(
        self,
        chrom: str,
        start: int,
        stop: int,
        dataset: str = "gnomad_r4",
        reference_genome: str = "GRCh38",
    ) -> List[VariantInfo]:
        """
        Query gnomAD for all variants in a genomic region.

        Args:
            chrom: Chromosome (e.g., "17", "X") without "chr" prefix
            start: Start position (1-based, inclusive)
            stop: Stop position (1-based, inclusive)
            dataset: gnomAD dataset version
            reference_genome: Reference genome (GRCh38 or GRCh37)

        Returns:
            List of VariantInfo objects

        Example:
            variants = client.query_region("17", 7674200, 7674400)
            for v in variants:
                print(f"{v.variant_id}: AF={v.max_af}")
        """
        # Remove chr prefix if present
        chrom = chrom.replace("chr", "")

        logger.info(f"Querying gnomAD for region {chrom}:{start}-{stop} (dataset: {dataset})")

        query = """
        {
          region(chrom: "%s", start: %d, stop: %d, reference_genome: %s) {
            chrom
            start
            stop
            variants(dataset: %s) {
              variantId
              pos
              ref
              alt
              rsids
              gene_symbol
              consequence
              transcript_id
              hgvsc
              hgvsp
              exome {
                ac
                an
                ac_hom
                ac_hemi
                filters
                populations {
                  id
                  ac
                  an
                }
              }
              genome {
                ac
                an
                ac_hom
                ac_hemi
                filters
                populations {
                  id
                  ac
                  an
                }
              }
            }
          }
        }
        """ % (chrom, start, stop, reference_genome, dataset)

        data = self._execute_query(query, timeout=120)
        region_data = data.get("region")

        if not region_data:
            logger.info(f"No data for region {chrom}:{start}-{stop}")
            return []

        variants = [
            self._parse_variant_from_region_or_gene(v)
            for v in region_data.get("variants", [])
        ]

        logger.info(f"Found {len(variants)} variants in region")
        return variants

    def query_region_string(
        self,
        region: str,
        dataset: str = "gnomad_r4",
        reference_genome: str = "GRCh38",
    ) -> List[VariantInfo]:
        """
        Query gnomAD for all variants in a region specified as a string.

        Args:
            region: Region string (e.g., "17:7674200-7674400", "chr17:7674200-7674400")
            dataset: gnomAD dataset version
            reference_genome: Reference genome

        Returns:
            List of VariantInfo objects
        """
        chrom, start, stop = self.parse_region(region)
        return self.query_region(chrom, start, stop, dataset, reference_genome)


# =============================================================================
# CLI Interface
# =============================================================================

def format_variant_line(v: VariantInfo) -> str:
    """Format a variant for display"""
    af_str = f"{v.max_af:.2e}" if v.max_af else "N/A"
    gene = v.gene_symbol or (v.get_canonical_consequence().gene_symbol if v.get_canonical_consequence() else "")
    cons = v.consequence or (v.get_canonical_consequence().consequence if v.get_canonical_consequence() else "")
    return f"{v.variant_id}\t{af_str}\t{cons}\t{gene}"


def cmd_variant(args):
    """Handle variant subcommand"""
    client = GnomadClient()
    variant = client.query_variant(args.variant_id, args.dataset)

    if not variant:
        print(f"Variant {args.variant_id} not found in gnomAD")
        return

    if args.output:
        with open(args.output, "w") as f:
            json.dump(variant.to_dict(), f, indent=2)
        print(f"Results saved to {args.output}")
    else:
        print(f"\nVariant: {variant.variant_id}")
        print(f"rsID: {variant.rsid or 'N/A'}")
        print(f"\nFrequencies:")
        print(f"  Exome AF:  {variant.exome_af:.2e}" if variant.exome_af else "  Exome AF:  N/A")
        print(f"  Genome AF: {variant.genome_af:.2e}" if variant.genome_af else "  Genome AF: N/A")
        print(f"  Max AF:    {variant.max_af:.2e}" if variant.max_af else "  Max AF:    N/A")

        tc = variant.get_canonical_consequence()
        if tc:
            print(f"\nCanonical transcript:")
            print(f"  Gene: {tc.gene_symbol}")
            print(f"  Transcript: {tc.transcript_id}")
            print(f"  Consequence: {tc.consequence}")
            print(f"  HGVSc: {tc.hgvsc}")
            print(f"  HGVSp: {tc.hgvsp}")

        if variant.in_silico_predictors:
            print(f"\nIn silico predictors:")
            for pred in variant.in_silico_predictors:
                print(f"  {pred.id}: {pred.value}")


def cmd_gene(args):
    """Handle gene subcommand"""
    client = GnomadClient()
    gene = client.query_gene(args.gene_symbol, args.dataset, args.genome)

    if not gene:
        print(f"Gene {args.gene_symbol} not found")
        return

    # Apply filters
    variants = gene.variants
    if args.max_af is not None:
        variants = [v for v in variants if v.max_af is None or v.max_af <= args.max_af]
    if args.min_af is not None:
        variants = [v for v in variants if v.max_af is not None and v.max_af >= args.min_af]

    if args.output:
        output = {
            "gene": gene.to_dict(),
            "query": {"dataset": args.dataset, "reference_genome": args.genome},
            "variant_count": len(variants),
            "variants": [v.to_dict() for v in variants],
        }
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2)
        print(f"Results saved to {args.output}")
    else:
        print(f"\nGene: {gene.symbol} ({gene.gene_id})")
        print(f"Location: chr{gene.chrom}:{gene.start}-{gene.stop}")
        print(f"Variants: {len(variants)}")
        print(f"\nvariant_id\tmax_af\tconsequence\tgene")
        print("-" * 80)
        for v in variants[:args.limit]:
            print(format_variant_line(v))
        if len(variants) > args.limit:
            print(f"\n... and {len(variants) - args.limit} more variants")


def cmd_region(args):
    """Handle region subcommand"""
    client = GnomadClient()

    if args.region:
        variants = client.query_region_string(args.region, args.dataset, args.genome)
        region_str = args.region
    else:
        chrom = args.chrom.replace("chr", "")
        variants = client.query_region(chrom, args.start, args.stop, args.dataset, args.genome)
        region_str = f"{chrom}:{args.start}-{args.stop}"

    # Apply filters
    if args.max_af is not None:
        variants = [v for v in variants if v.max_af is None or v.max_af <= args.max_af]
    if args.min_af is not None:
        variants = [v for v in variants if v.max_af is not None and v.max_af >= args.min_af]

    if args.output:
        output = {
            "query": {
                "region": region_str,
                "dataset": args.dataset,
                "reference_genome": args.genome,
            },
            "variant_count": len(variants),
            "variants": [v.to_dict() for v in variants],
        }
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2)
        print(f"Results saved to {args.output}")
    else:
        print(f"\nRegion: {region_str}")
        print(f"Variants: {len(variants)}")
        print(f"\nvariant_id\tmax_af\tconsequence\tgene")
        print("-" * 80)
        for v in variants[:args.limit]:
            print(format_variant_line(v))
        if len(variants) > args.limit:
            print(f"\n... and {len(variants) - args.limit} more variants")


def main():
    parser = argparse.ArgumentParser(
        description="Query gnomAD for variant population frequency data",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s variant 17-7674220-C-T
  %(prog)s variant "chr17:7674220:C:T" --dataset gnomad_r2_1
  %(prog)s gene TP53
  %(prog)s gene BRCA1 --max-af 0.001 --output brca1_rare.json
  %(prog)s region 17:7674200-7674400
  %(prog)s region --chrom 17 --start 7674200 --stop 7674400
        """,
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Variant subcommand
    variant_parser = subparsers.add_parser("variant", help="Query a single variant by ID")
    variant_parser.add_argument("variant_id", help="Variant ID (e.g., 17-7674220-C-T)")
    variant_parser.add_argument("--dataset", default="gnomad_r4",
        choices=["gnomad_r4", "gnomad_r3", "gnomad_r2_1"], help="gnomAD dataset")
    variant_parser.add_argument("--output", "-o", help="Output JSON file")
    variant_parser.set_defaults(func=cmd_variant)

    # Gene subcommand
    gene_parser = subparsers.add_parser("gene", help="Query all variants in a gene")
    gene_parser.add_argument("gene_symbol", help="Gene symbol (e.g., TP53, BRCA1)")
    gene_parser.add_argument("--dataset", default="gnomad_r4",
        choices=["gnomad_r4", "gnomad_r3", "gnomad_r2_1"], help="gnomAD dataset")
    gene_parser.add_argument("--genome", default="GRCh38",
        choices=["GRCh38", "GRCh37"], help="Reference genome")
    gene_parser.add_argument("--max-af", type=float, help="Filter by max AF")
    gene_parser.add_argument("--min-af", type=float, help="Filter by min AF")
    gene_parser.add_argument("--limit", type=int, default=50, help="Max variants to display")
    gene_parser.add_argument("--output", "-o", help="Output JSON file")
    gene_parser.set_defaults(func=cmd_gene)

    # Region subcommand
    region_parser = subparsers.add_parser("region", help="Query all variants in a region")
    region_group = region_parser.add_mutually_exclusive_group(required=True)
    region_group.add_argument("region", nargs="?", help="Region (e.g., 17:7674200-7674400)")
    region_group.add_argument("--chrom", help="Chromosome")
    region_parser.add_argument("--start", type=int, help="Start position")
    region_parser.add_argument("--stop", type=int, help="Stop position")
    region_parser.add_argument("--dataset", default="gnomad_r4",
        choices=["gnomad_r4", "gnomad_r3", "gnomad_r2_1"], help="gnomAD dataset")
    region_parser.add_argument("--genome", default="GRCh38",
        choices=["GRCh38", "GRCh37"], help="Reference genome")
    region_parser.add_argument("--max-af", type=float, help="Filter by max AF")
    region_parser.add_argument("--min-af", type=float, help="Filter by min AF")
    region_parser.add_argument("--limit", type=int, default=50, help="Max variants to display")
    region_parser.add_argument("--output", "-o", help="Output JSON file")
    region_parser.set_defaults(func=cmd_region)

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Validate region args
    if args.command == "region" and args.chrom and (args.start is None or args.stop is None):
        parser.error("--start and --stop are required with --chrom")

    try:
        args.func(args)
    except GnomadQueryError as e:
        logger.error(f"Query failed: {e}")
        sys.exit(1)
    except ValueError as e:
        logger.error(f"Invalid input: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
