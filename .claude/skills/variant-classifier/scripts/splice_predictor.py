#!/usr/bin/env python3
"""
Splice Predictor Script

Query SpliceAI and Pangolin REST APIs for splice site predictions.
Provides predictions for both splice site gain and loss.

Usage:
    python splice_predictor.py chr17 7674220 C T
    python splice_predictor.py 17-7674220-C-T
    python splice_predictor.py --variant "chr8:140300616:T:G" --json
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


# API endpoints
SPLICEAI_ENDPOINTS = {
    "37": "https://spliceai-37-xwkwwwxdwq-uc.a.run.app/spliceai/",
    "38": "https://spliceai-38-xwkwwwxdwq-uc.a.run.app/spliceai/",
}

PANGOLIN_ENDPOINTS = {
    "37": "https://pangolin-37-xwkwwwxdwq-uc.a.run.app/pangolin/",
    "38": "https://pangolin-38-xwkwwwxdwq-uc.a.run.app/pangolin/",
}

# Rate limiting settings
RATE_LIMIT_DELAY = 1.0  # 1 second between requests (API is sensitive)
MAX_RETRIES = 3


@dataclass
class SpliceAIScore:
    """SpliceAI prediction scores for a single gene/transcript"""
    gene: str
    gene_id: str
    transcript: str
    strand: str
    biotype: str
    ds_ag: float  # Delta score Acceptor Gain
    ds_al: float  # Delta score Acceptor Loss
    ds_dg: float  # Delta score Donor Gain
    ds_dl: float  # Delta score Donor Loss
    dp_ag: int  # Delta position Acceptor Gain
    dp_al: int  # Delta position Acceptor Loss
    dp_dg: int  # Delta position Donor Gain
    dp_dl: int  # Delta position Donor Loss

    @property
    def max_delta_score(self) -> float:
        """Get maximum delta score"""
        return max(self.ds_ag, self.ds_al, self.ds_dg, self.ds_dl)

    @property
    def max_effect_type(self) -> str:
        """Get the effect type with highest score"""
        scores = {
            "Acceptor Gain": self.ds_ag,
            "Acceptor Loss": self.ds_al,
            "Donor Gain": self.ds_dg,
            "Donor Loss": self.ds_dl,
        }
        return max(scores, key=scores.get)

    @property
    def significance_level(self) -> str:
        """Interpret the clinical significance of the max score"""
        max_score = self.max_delta_score
        if max_score >= 0.8:
            return "High - Strong evidence of splice disruption"
        elif max_score >= 0.5:
            return "Moderate - Likely affects splicing"
        elif max_score >= 0.2:
            return "Low - May affect splicing"
        else:
            return "Minimal - Unlikely to affect splicing"

    @property
    def predicted_effects(self) -> List[str]:
        """Get list of predicted splice effects"""
        effects = []
        if self.ds_al >= 0.5 and self.ds_dl >= 0.5:
            effects.append("Exon skipping")
        elif self.ds_al >= 0.5:
            effects.append("Acceptor site disruption")
        elif self.ds_dl >= 0.5:
            effects.append("Donor site disruption")
        if self.ds_ag >= 0.5:
            effects.append("Cryptic acceptor activation")
        if self.ds_dg >= 0.5:
            effects.append("Cryptic donor activation")

        return effects if effects else ["No significant splice effect predicted"]

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "gene": self.gene,
            "gene_id": self.gene_id,
            "transcript": self.transcript,
            "strand": self.strand,
            "biotype": self.biotype,
            "scores": {
                "DS_AG": self.ds_ag,
                "DS_AL": self.ds_al,
                "DS_DG": self.ds_dg,
                "DS_DL": self.ds_dl,
            },
            "positions": {
                "DP_AG": self.dp_ag,
                "DP_AL": self.dp_al,
                "DP_DG": self.dp_dg,
                "DP_DL": self.dp_dl,
            },
            "max_delta_score": self.max_delta_score,
            "max_effect_type": self.max_effect_type,
            "significance": self.significance_level,
            "predicted_effects": self.predicted_effects,
        }


@dataclass
class PangolinScore:
    """Pangolin prediction scores for a single gene/transcript"""
    gene: str
    gene_id: str
    transcript: str
    strand: str
    ds_sg: float  # Delta score Splice Gain
    ds_sl: float  # Delta score Splice Loss
    dp_sg: int  # Delta position Splice Gain
    dp_sl: int  # Delta position Splice Loss
    sg_ref: float  # Splice Gain reference score
    sg_alt: float  # Splice Gain alternate score
    sl_ref: float  # Splice Loss reference score
    sl_alt: float  # Splice Loss alternate score

    @property
    def max_delta_score(self) -> float:
        """Get maximum absolute delta score"""
        return max(abs(self.ds_sg), abs(self.ds_sl))

    @property
    def has_splice_gain(self) -> bool:
        """Check if variant creates a new splice site"""
        return self.ds_sg > 0.2

    @property
    def has_splice_loss(self) -> bool:
        """Check if variant disrupts an existing splice site"""
        return self.ds_sl < -0.2

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "gene": self.gene,
            "gene_id": self.gene_id,
            "transcript": self.transcript,
            "strand": self.strand,
            "scores": {
                "DS_SG": self.ds_sg,
                "DS_SL": self.ds_sl,
            },
            "positions": {
                "DP_SG": self.dp_sg,
                "DP_SL": self.dp_sl,
            },
            "reference_scores": {
                "SG_REF": self.sg_ref,
                "SL_REF": self.sl_ref,
            },
            "alternate_scores": {
                "SG_ALT": self.sg_alt,
                "SL_ALT": self.sl_alt,
            },
            "has_splice_gain": self.has_splice_gain,
            "has_splice_loss": self.has_splice_loss,
        }


@dataclass
class SplicePrediction:
    """Combined splice prediction result"""
    variant: str
    chromosome: str
    position: int
    ref: str
    alt: str
    genome: str
    spliceai_scores: List[SpliceAIScore] = field(default_factory=list)
    pangolin_scores: List[PangolinScore] = field(default_factory=list)
    spliceai_error: Optional[str] = None
    pangolin_error: Optional[str] = None

    @property
    def max_spliceai_score(self) -> Optional[float]:
        """Get maximum SpliceAI delta score across all transcripts"""
        if not self.spliceai_scores:
            return None
        return max(s.max_delta_score for s in self.spliceai_scores)

    @property
    def concordant(self) -> Optional[bool]:
        """Check if SpliceAI and Pangolin predictions are concordant"""
        if not self.spliceai_scores or not self.pangolin_scores:
            return None

        # Get primary (highest scoring) predictions
        spliceai_max = max(self.spliceai_scores, key=lambda x: x.max_delta_score)
        pangolin_primary = self.pangolin_scores[0]

        # Check for concordance
        spliceai_predicts_effect = spliceai_max.max_delta_score >= 0.2
        pangolin_predicts_effect = (
            pangolin_primary.has_splice_gain or pangolin_primary.has_splice_loss
        )

        return spliceai_predicts_effect == pangolin_predicts_effect

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "variant": self.variant,
            "chromosome": self.chromosome,
            "position": self.position,
            "ref": self.ref,
            "alt": self.alt,
            "genome": self.genome,
            "spliceai": {
                "scores": [s.to_dict() for s in self.spliceai_scores],
                "max_score": self.max_spliceai_score,
                "error": self.spliceai_error,
            },
            "pangolin": {
                "scores": [s.to_dict() for s in self.pangolin_scores],
                "error": self.pangolin_error,
            },
            "concordant": self.concordant,
        }


def create_session() -> requests.Session:
    """Create a requests session with retry logic."""
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=2,
        status_forcelist=[500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    return session


def parse_variant(variant_str: str) -> Tuple[str, int, str, str]:
    """
    Parse variant string into components.

    Supports formats:
    - chr17:7674220:C:T
    - chr17-7674220-C-T
    - 17-7674220-C-T
    - 17:7674220:C>T
    """
    patterns = [
        re.compile(r'^(?:chr)?(\w+)[:-](\d+)[:-]([ATCGN]+)[:-]([ATCGN]+)$', re.IGNORECASE),
        re.compile(r'^(?:chr)?(\w+)[:-](\d+)[:-]([ATCGN]+)>([ATCGN]+)$', re.IGNORECASE),
    ]

    for pattern in patterns:
        match = pattern.match(variant_str.strip())
        if match:
            chrom, pos, ref, alt = match.groups()
            return chrom, int(pos), ref.upper(), alt.upper()

    raise ValueError(f"Unable to parse variant: {variant_str}")


class SplicePredictor:
    """Client for SpliceAI and Pangolin APIs"""

    def __init__(self, genome: str = "38"):
        self.genome = genome
        self.session = create_session()
        self._last_request_time = 0

    def _rate_limit(self):
        """Implement rate limiting"""
        elapsed = time.time() - self._last_request_time
        if elapsed < RATE_LIMIT_DELAY:
            time.sleep(RATE_LIMIT_DELAY - elapsed)
        self._last_request_time = time.time()

    def query_spliceai(
        self,
        chrom: str,
        pos: int,
        ref: str,
        alt: str,
        distance: int = 500
    ) -> Tuple[List[SpliceAIScore], Optional[str]]:
        """
        Query SpliceAI REST API.

        Args:
            chrom: Chromosome (with or without 'chr' prefix)
            pos: Genomic position
            ref: Reference allele
            alt: Alternate allele
            distance: Maximum distance to splice site (default: 500)

        Returns:
            Tuple of (list of scores, error message if any)
        """
        self._rate_limit()

        # Normalize chromosome (API accepts both formats)
        if not chrom.startswith("chr"):
            chrom = f"chr{chrom}"

        variant = f"{chrom}-{pos}-{ref}-{alt}"
        url = SPLICEAI_ENDPOINTS[self.genome]
        params = {
            "hg": self.genome,
            "variant": variant,
            "distance": distance,
        }

        for attempt in range(MAX_RETRIES):
            try:
                response = self.session.get(url, params=params, timeout=60)

                if response.status_code == 429:
                    wait_time = 60 * (attempt + 1)
                    print(f"Rate limited. Waiting {wait_time}s...", file=sys.stderr)
                    time.sleep(wait_time)
                    continue

                response.raise_for_status()
                data = response.json()

                if "error" in data:
                    return [], data["error"]

                scores = []
                for s in data.get("scores", []):
                    scores.append(SpliceAIScore(
                        gene=s.get("gene", ""),
                        gene_id=s.get("gene_id", ""),
                        transcript=s.get("transcript", ""),
                        strand=s.get("strand", ""),
                        biotype=s.get("type", ""),
                        ds_ag=float(s.get("DS_AG", 0)),
                        ds_al=float(s.get("DS_AL", 0)),
                        ds_dg=float(s.get("DS_DG", 0)),
                        ds_dl=float(s.get("DS_DL", 0)),
                        dp_ag=int(s.get("DP_AG", 0)),
                        dp_al=int(s.get("DP_AL", 0)),
                        dp_dg=int(s.get("DP_DG", 0)),
                        dp_dl=int(s.get("DP_DL", 0)),
                    ))

                return scores, None

            except requests.RequestException as e:
                if attempt < MAX_RETRIES - 1:
                    time.sleep(2 ** attempt)
                else:
                    return [], str(e)

        return [], "Max retries exceeded"

    def query_pangolin(
        self,
        chrom: str,
        pos: int,
        ref: str,
        alt: str,
        distance: int = 500
    ) -> Tuple[List[PangolinScore], Optional[str]]:
        """
        Query Pangolin REST API.

        Args:
            chrom: Chromosome (with or without 'chr' prefix)
            pos: Genomic position
            ref: Reference allele
            alt: Alternate allele
            distance: Maximum distance to splice site (default: 500)

        Returns:
            Tuple of (list of scores, error message if any)
        """
        self._rate_limit()

        if not chrom.startswith("chr"):
            chrom = f"chr{chrom}"

        variant = f"{chrom}-{pos}-{ref}-{alt}"
        url = PANGOLIN_ENDPOINTS[self.genome]
        params = {
            "hg": self.genome,
            "variant": variant,
            "distance": distance,
        }

        for attempt in range(MAX_RETRIES):
            try:
                response = self.session.get(url, params=params, timeout=60)

                if response.status_code == 429:
                    wait_time = 60 * (attempt + 1)
                    print(f"Rate limited. Waiting {wait_time}s...", file=sys.stderr)
                    time.sleep(wait_time)
                    continue

                response.raise_for_status()
                data = response.json()

                if "error" in data:
                    return [], data["error"]

                scores = []
                for s in data.get("scores", []):
                    scores.append(PangolinScore(
                        gene=s.get("gene", ""),
                        gene_id=s.get("gene_id", ""),
                        transcript=s.get("transcript", ""),
                        strand=s.get("strand", ""),
                        ds_sg=float(s.get("DS_SG", 0)),
                        ds_sl=float(s.get("DS_SL", 0)),
                        dp_sg=int(s.get("DP_SG", 0)),
                        dp_sl=int(s.get("DP_SL", 0)),
                        sg_ref=float(s.get("SG_REF", 0)),
                        sg_alt=float(s.get("SG_ALT", 0)),
                        sl_ref=float(s.get("SL_REF", 0)),
                        sl_alt=float(s.get("SL_ALT", 0)),
                    ))

                return scores, None

            except requests.RequestException as e:
                if attempt < MAX_RETRIES - 1:
                    time.sleep(2 ** attempt)
                else:
                    return [], str(e)

        return [], "Max retries exceeded"

    def predict(
        self,
        chrom: str,
        pos: int,
        ref: str,
        alt: str,
        distance: int = 500,
        include_pangolin: bool = True
    ) -> SplicePrediction:
        """
        Get splice predictions from both SpliceAI and Pangolin.

        Args:
            chrom: Chromosome
            pos: Genomic position
            ref: Reference allele
            alt: Alternate allele
            distance: Maximum distance to splice site
            include_pangolin: Whether to query Pangolin as well

        Returns:
            SplicePrediction with results from both tools
        """
        if not chrom.startswith("chr"):
            variant_str = f"chr{chrom}-{pos}-{ref}-{alt}"
        else:
            variant_str = f"{chrom}-{pos}-{ref}-{alt}"

        result = SplicePrediction(
            variant=variant_str,
            chromosome=chrom.replace("chr", ""),
            position=pos,
            ref=ref,
            alt=alt,
            genome=f"GRCh{self.genome}",
        )

        # Query SpliceAI
        spliceai_scores, spliceai_error = self.query_spliceai(
            chrom, pos, ref, alt, distance
        )
        result.spliceai_scores = spliceai_scores
        result.spliceai_error = spliceai_error

        # Query Pangolin if requested
        if include_pangolin:
            pangolin_scores, pangolin_error = self.query_pangolin(
                chrom, pos, ref, alt, distance
            )
            result.pangolin_scores = pangolin_scores
            result.pangolin_error = pangolin_error

        return result


def interpret_scores(prediction: SplicePrediction) -> Dict[str, Any]:
    """
    Interpret splice prediction scores for clinical use.

    Returns interpretation with significance level and recommendations.
    """
    interpretation = {
        "variant": prediction.variant,
        "has_spliceai_data": len(prediction.spliceai_scores) > 0,
        "has_pangolin_data": len(prediction.pangolin_scores) > 0,
    }

    if prediction.spliceai_scores:
        primary = max(prediction.spliceai_scores, key=lambda x: x.max_delta_score)
        max_score = primary.max_delta_score

        interpretation["spliceai"] = {
            "gene": primary.gene,
            "max_score": max_score,
            "max_effect": primary.max_effect_type,
            "significance": primary.significance_level,
            "predicted_effects": primary.predicted_effects,
            "all_scores": {
                "DS_AG": primary.ds_ag,
                "DS_AL": primary.ds_al,
                "DS_DG": primary.ds_dg,
                "DS_DL": primary.ds_dl,
            }
        }

        # ACMG/AMP criteria relevance
        if max_score >= 0.5:
            interpretation["acmg_relevance"] = "PP3 supporting (computational evidence)"
        elif max_score >= 0.8:
            interpretation["acmg_relevance"] = "PP3 moderate or PVS1 considerations"
    else:
        interpretation["spliceai"] = None
        interpretation["acmg_relevance"] = "Insufficient data"

    if prediction.pangolin_scores:
        primary = prediction.pangolin_scores[0]
        interpretation["pangolin"] = {
            "gene": primary.gene,
            "ds_sg": primary.ds_sg,
            "ds_sl": primary.ds_sl,
            "splice_gain": primary.has_splice_gain,
            "splice_loss": primary.has_splice_loss,
        }
    else:
        interpretation["pangolin"] = None

    # Concordance assessment
    interpretation["concordant"] = prediction.concordant

    return interpretation


def main():
    parser = argparse.ArgumentParser(
        description="Query SpliceAI and Pangolin for splice predictions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s chr17 7674220 C T
  %(prog)s --variant "chr8-140300616-T-G"
  %(prog)s --variant "17:7674220:C:T" --json -o predictions.json
  %(prog)s chr8 140300616 T G --spliceai-only
        """,
    )
    parser.add_argument(
        "chrom",
        nargs="?",
        help="Chromosome (e.g., chr17 or 17)"
    )
    parser.add_argument(
        "pos",
        nargs="?",
        type=int,
        help="Position"
    )
    parser.add_argument(
        "ref",
        nargs="?",
        help="Reference allele"
    )
    parser.add_argument(
        "alt",
        nargs="?",
        help="Alternate allele"
    )
    parser.add_argument(
        "--variant", "-v",
        help="Variant string (e.g., chr17-7674220-C-T)"
    )
    parser.add_argument(
        "--genome", "-g",
        choices=["37", "38"],
        default="38",
        help="Genome build (default: 38)"
    )
    parser.add_argument(
        "--distance", "-d",
        type=int,
        default=500,
        help="Maximum distance to splice site (default: 500)"
    )
    parser.add_argument(
        "--spliceai-only",
        action="store_true",
        help="Only query SpliceAI (skip Pangolin)"
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output as JSON"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path"
    )

    args = parser.parse_args()

    # Parse variant
    if args.variant:
        try:
            chrom, pos, ref, alt = parse_variant(args.variant)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            return 1
    elif args.chrom and args.pos and args.ref and args.alt:
        chrom, pos, ref, alt = args.chrom, args.pos, args.ref, args.alt
    else:
        parser.error("Provide either --variant or positional arguments (chrom pos ref alt)")

    try:
        # Query APIs
        predictor = SplicePredictor(genome=args.genome)
        prediction = predictor.predict(
            chrom, pos, ref, alt,
            distance=args.distance,
            include_pangolin=not args.spliceai_only
        )

        # Format output
        if args.json:
            output = json.dumps(prediction.to_dict(), indent=2)
        else:
            interpretation = interpret_scores(prediction)

            lines = [
                f"Variant: {prediction.variant}",
                f"Genome: {prediction.genome}",
                "",
            ]

            if interpretation["spliceai"]:
                s = interpretation["spliceai"]
                lines.extend([
                    "=== SpliceAI ===",
                    f"Gene: {s['gene']}",
                    f"Max Score: {s['max_score']:.3f} ({s['max_effect']})",
                    f"Significance: {s['significance']}",
                    f"Predicted Effects: {', '.join(s['predicted_effects'])}",
                    "",
                    "Delta Scores:",
                    f"  DS_AG (Acceptor Gain): {s['all_scores']['DS_AG']:.3f}",
                    f"  DS_AL (Acceptor Loss): {s['all_scores']['DS_AL']:.3f}",
                    f"  DS_DG (Donor Gain): {s['all_scores']['DS_DG']:.3f}",
                    f"  DS_DL (Donor Loss): {s['all_scores']['DS_DL']:.3f}",
                    "",
                ])
            elif prediction.spliceai_error:
                lines.extend([
                    "=== SpliceAI ===",
                    f"Error: {prediction.spliceai_error}",
                    "",
                ])

            if interpretation.get("pangolin"):
                p = interpretation["pangolin"]
                lines.extend([
                    "=== Pangolin ===",
                    f"Gene: {p['gene']}",
                    f"DS_SG (Splice Gain): {p['ds_sg']:.3f}",
                    f"DS_SL (Splice Loss): {p['ds_sl']:.3f}",
                    f"Splice Gain Predicted: {p['splice_gain']}",
                    f"Splice Loss Predicted: {p['splice_loss']}",
                    "",
                ])
            elif prediction.pangolin_error:
                lines.extend([
                    "=== Pangolin ===",
                    f"Error: {prediction.pangolin_error}",
                    "",
                ])

            if interpretation["concordant"] is not None:
                lines.append(f"Concordance: {'Yes' if interpretation['concordant'] else 'No'}")

            if interpretation.get("acmg_relevance"):
                lines.extend([
                    "",
                    f"ACMG/AMP Relevance: {interpretation['acmg_relevance']}",
                ])

            output = "\n".join(lines)

        # Write output
        if args.output:
            with open(args.output, "w") as f:
                f.write(output)
            print(f"Output saved to {args.output}", file=sys.stderr)
        else:
            print(output)

        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
