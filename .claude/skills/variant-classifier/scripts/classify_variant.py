#!/usr/bin/env python3
"""
Variant Classification Script

Apply ACMG/AMP criteria to classify genetic variants. Uses VCEP-specific thresholds
when available, falling back to standard ACMG criteria otherwise.

Usage:
    python classify_variant.py --annotation vep_result.json
    python classify_variant.py --annotation vep_result.json --vcep-spec vcep_info.json
    python classify_variant.py --annotation vep_result.json --evidence evidence.json -o report.md
"""

import argparse
import json
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Default paths
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "data"
ACMG_CRITERIA_FILE = DATA_DIR / "acmg_criteria.json"
TEMPLATE_DIR = SCRIPT_DIR.parent / "templates"


# ACMG criteria strength levels and point values
STRENGTH_POINTS = {
    "very_strong": 8,
    "strong": 4,
    "moderate": 2,
    "supporting": 1,
}

# Standard ACMG criteria by category
PATHOGENIC_CRITERIA = {
    "PVS1": {"strength": "very_strong", "category": "null_variant"},
    "PS1": {"strength": "strong", "category": "same_aa_change"},
    "PS2": {"strength": "strong", "category": "de_novo"},
    "PS3": {"strength": "strong", "category": "functional"},
    "PS4": {"strength": "strong", "category": "prevalence"},
    "PM1": {"strength": "moderate", "category": "hotspot"},
    "PM2": {"strength": "moderate", "category": "absent_population"},
    "PM3": {"strength": "moderate", "category": "in_trans"},
    "PM4": {"strength": "moderate", "category": "protein_length"},
    "PM5": {"strength": "moderate", "category": "novel_missense"},
    "PM6": {"strength": "moderate", "category": "de_novo_assumed"},
    "PP1": {"strength": "supporting", "category": "cosegregation"},
    "PP2": {"strength": "supporting", "category": "missense_constraint"},
    "PP3": {"strength": "supporting", "category": "computational"},
    "PP4": {"strength": "supporting", "category": "phenotype"},
    "PP5": {"strength": "supporting", "category": "reputable_source"},
}

BENIGN_CRITERIA = {
    "BA1": {"strength": "standalone", "category": "high_frequency"},
    "BS1": {"strength": "strong", "category": "frequency"},
    "BS2": {"strength": "strong", "category": "healthy_adults"},
    "BS3": {"strength": "strong", "category": "functional"},
    "BS4": {"strength": "strong", "category": "no_segregation"},
    "BP1": {"strength": "supporting", "category": "missense_only_truncating"},
    "BP2": {"strength": "supporting", "category": "in_trans_cis"},
    "BP3": {"strength": "supporting", "category": "inframe_repeat"},
    "BP4": {"strength": "supporting", "category": "computational"},
    "BP5": {"strength": "supporting", "category": "alternate_cause"},
    "BP6": {"strength": "supporting", "category": "reputable_source"},
    "BP7": {"strength": "supporting", "category": "silent"},
}


@dataclass
class CriterionEvaluation:
    """Evaluation of a single ACMG criterion"""
    criterion: str
    met: bool
    strength: str
    points: int
    evidence: str
    source: str = "computational"  # computational, case, literature, vcep
    vcep_modified: bool = False
    notes: Optional[str] = None


@dataclass
class ClassificationResult:
    """Complete variant classification result"""
    variant: str
    gene: str
    classification: str
    confidence: str
    pathogenic_points: int
    benign_points: int
    pathogenic_criteria: List[CriterionEvaluation] = field(default_factory=list)
    benign_criteria: List[CriterionEvaluation] = field(default_factory=list)
    vcep_spec_used: Optional[str] = None
    notes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary"""
        return {
            "variant": self.variant,
            "gene": self.gene,
            "classification": self.classification,
            "confidence": self.confidence,
            "pathogenic_points": self.pathogenic_points,
            "benign_points": self.benign_points,
            "pathogenic_criteria": [
                {
                    "criterion": c.criterion,
                    "met": c.met,
                    "strength": c.strength,
                    "points": c.points,
                    "evidence": c.evidence,
                    "source": c.source,
                    "vcep_modified": c.vcep_modified,
                    "notes": c.notes,
                }
                for c in self.pathogenic_criteria if c.met
            ],
            "benign_criteria": [
                {
                    "criterion": c.criterion,
                    "met": c.met,
                    "strength": c.strength,
                    "points": c.points,
                    "evidence": c.evidence,
                    "source": c.source,
                    "vcep_modified": c.vcep_modified,
                    "notes": c.notes,
                }
                for c in self.benign_criteria if c.met
            ],
            "vcep_spec_used": self.vcep_spec_used,
            "notes": self.notes,
        }


def load_acmg_criteria(criteria_file: Path = ACMG_CRITERIA_FILE) -> Dict[str, Any]:
    """Load ACMG criteria thresholds from JSON file"""
    if criteria_file.exists():
        with open(criteria_file) as f:
            return json.load(f)
    return get_default_acmg_criteria()


def get_default_acmg_criteria() -> Dict[str, Any]:
    """Return default ACMG criteria thresholds"""
    return {
        "population_frequency": {
            "BA1": 0.05,  # 5% - standalone benign
            "BS1": 0.01,  # 1% - strong benign (gene-dependent)
            "PM2_supporting": 0.0001,  # Rare/absent for supporting
            "PM2_moderate": 0.00001,  # Very rare for moderate
        },
        "computational": {
            "sift_deleterious": 0.05,  # Score <= this is deleterious
            "polyphen_damaging": 0.85,  # Score >= this is probably damaging
            "polyphen_possibly": 0.15,  # Score >= this is possibly damaging
            "cadd_deleterious": 25,  # CADD PHRED >= this is deleterious
            "revel_pathogenic": 0.7,  # REVEL >= this supports pathogenic
            "revel_benign": 0.15,  # REVEL <= this supports benign
            "spliceai_high": 0.5,  # SpliceAI >= this is high impact
            "spliceai_moderate": 0.2,  # SpliceAI >= this is moderate
        },
        "combining_rules": {
            "pathogenic": {
                "pvs1_ps1": "Pathogenic",
                "pvs1_pm1_pm2": "Pathogenic",
                "ps1_ps2": "Pathogenic",
                "ps1_3pm": "Pathogenic",
                "2pm_2pp": "Likely Pathogenic",
            },
            "benign": {
                "ba1": "Benign (standalone)",
                "2bs": "Benign",
                "1bs_1bp": "Likely Benign",
            }
        },
        "point_thresholds": {
            "pathogenic": 10,  # Points needed for Pathogenic
            "likely_pathogenic": 6,  # Points needed for Likely Pathogenic
            "likely_benign": -6,  # Points needed for Likely Benign
            "benign": -10,  # Points needed for Benign
        }
    }


class VariantClassifier:
    """ACMG/AMP variant classifier with VCEP support"""

    def __init__(self, acmg_criteria: Optional[Dict] = None, vcep_spec: Optional[Dict] = None):
        self.acmg = acmg_criteria or get_default_acmg_criteria()
        self.vcep = vcep_spec
        self.criteria_evaluated: List[CriterionEvaluation] = []

    def evaluate_pvs1(self, annotation: Dict, consequence: str) -> CriterionEvaluation:
        """
        Evaluate PVS1 - Null variant in gene where LOF is mechanism.

        Applies to: nonsense, frameshift, canonical splice sites (+/-1,2),
        initiation codon, single/multi-exon deletion
        """
        null_consequences = {
            "stop_gained", "frameshift_variant", "splice_donor_variant",
            "splice_acceptor_variant", "start_lost", "transcript_ablation"
        }

        is_null = consequence in null_consequences

        # Check for VCEP-specific modifications
        strength = "very_strong"
        vcep_modified = False
        notes = None

        if self.vcep:
            # VCEP may downgrade PVS1 based on various factors
            pvs1_spec = self.vcep.get("pvs1", {})
            if pvs1_spec.get("requires_nmd_prediction"):
                notes = "VCEP: NMD prediction required"

        evidence = f"Consequence: {consequence}"
        points = STRENGTH_POINTS.get(strength, 0) if is_null else 0

        return CriterionEvaluation(
            criterion="PVS1",
            met=is_null,
            strength=strength,
            points=points,
            evidence=evidence,
            vcep_modified=vcep_modified,
            notes=notes,
        )

    def evaluate_population_frequency(
        self,
        gnomad_af: Optional[float],
        max_pop_af: Optional[float] = None
    ) -> List[CriterionEvaluation]:
        """
        Evaluate population frequency criteria: BA1, BS1, PM2.
        """
        evaluations = []
        thresholds = self.acmg["population_frequency"]

        # Use max population AF if available, otherwise overall AF
        af = max_pop_af if max_pop_af is not None else gnomad_af

        # BA1 - Standalone benign (AF > 5%)
        ba1_threshold = thresholds.get("BA1", 0.05)
        if self.vcep:
            ba1_threshold = self.vcep.get("BA1_threshold", ba1_threshold)

        ba1_met = af is not None and af > ba1_threshold
        evaluations.append(CriterionEvaluation(
            criterion="BA1",
            met=ba1_met,
            strength="standalone",
            points=-8 if ba1_met else 0,  # Standalone benign
            evidence=f"AF: {af:.2e}" if af else "AF: N/A",
            source="computational",
            vcep_modified=self.vcep is not None and "BA1_threshold" in self.vcep,
        ))

        # BS1 - Strong benign (AF > 1% or gene-specific)
        bs1_threshold = thresholds.get("BS1", 0.01)
        if self.vcep:
            bs1_threshold = self.vcep.get("BS1_threshold", bs1_threshold)

        bs1_met = af is not None and af > bs1_threshold and not ba1_met
        evaluations.append(CriterionEvaluation(
            criterion="BS1",
            met=bs1_met,
            strength="strong",
            points=-4 if bs1_met else 0,
            evidence=f"AF: {af:.2e}, threshold: {bs1_threshold}" if af else "AF: N/A",
            source="computational",
            vcep_modified=self.vcep is not None and "BS1_threshold" in self.vcep,
        ))

        # PM2 - Absent or rare
        pm2_threshold = thresholds.get("PM2_supporting", 0.0001)
        if self.vcep:
            pm2_threshold = self.vcep.get("PM2_threshold", pm2_threshold)

        pm2_met = af is None or af < pm2_threshold
        pm2_strength = "supporting"  # Default to supporting (ACMG update 2018)

        evaluations.append(CriterionEvaluation(
            criterion="PM2",
            met=pm2_met,
            strength=pm2_strength,
            points=1 if pm2_met else 0,
            evidence=f"AF: {af:.2e}" if af else "Absent from gnomAD",
            source="computational",
            vcep_modified=self.vcep is not None and "PM2_threshold" in self.vcep,
        ))

        return evaluations

    def evaluate_computational(
        self,
        sift_score: Optional[float],
        sift_pred: Optional[str],
        polyphen_score: Optional[float],
        polyphen_pred: Optional[str],
        cadd_phred: Optional[float] = None,
        revel_score: Optional[float] = None,
        spliceai_max: Optional[float] = None,
    ) -> List[CriterionEvaluation]:
        """
        Evaluate computational prediction criteria: PP3, BP4, BP7.
        """
        evaluations = []
        thresholds = self.acmg["computational"]

        # Count pathogenic and benign predictions
        path_predictions = 0
        benign_predictions = 0
        evidence_parts = []

        # SIFT
        if sift_score is not None:
            if sift_score <= thresholds.get("sift_deleterious", 0.05):
                path_predictions += 1
                evidence_parts.append(f"SIFT: {sift_pred} ({sift_score:.3f})")
            else:
                benign_predictions += 1
                evidence_parts.append(f"SIFT: {sift_pred} ({sift_score:.3f})")

        # PolyPhen
        if polyphen_score is not None:
            if polyphen_score >= thresholds.get("polyphen_damaging", 0.85):
                path_predictions += 1
                evidence_parts.append(f"PolyPhen: {polyphen_pred} ({polyphen_score:.3f})")
            elif polyphen_score < thresholds.get("polyphen_possibly", 0.15):
                benign_predictions += 1
                evidence_parts.append(f"PolyPhen: {polyphen_pred} ({polyphen_score:.3f})")

        # CADD
        if cadd_phred is not None:
            if cadd_phred >= thresholds.get("cadd_deleterious", 25):
                path_predictions += 1
                evidence_parts.append(f"CADD: {cadd_phred:.1f}")
            elif cadd_phred < 15:
                benign_predictions += 1
                evidence_parts.append(f"CADD: {cadd_phred:.1f}")

        # REVEL
        if revel_score is not None:
            if revel_score >= thresholds.get("revel_pathogenic", 0.7):
                path_predictions += 1
                evidence_parts.append(f"REVEL: {revel_score:.3f}")
            elif revel_score <= thresholds.get("revel_benign", 0.15):
                benign_predictions += 1
                evidence_parts.append(f"REVEL: {revel_score:.3f}")

        # SpliceAI
        if spliceai_max is not None:
            if spliceai_max >= thresholds.get("spliceai_high", 0.5):
                path_predictions += 1
                evidence_parts.append(f"SpliceAI: {spliceai_max:.3f}")
            elif spliceai_max < thresholds.get("spliceai_moderate", 0.2):
                benign_predictions += 1
                evidence_parts.append(f"SpliceAI: {spliceai_max:.3f}")

        evidence = "; ".join(evidence_parts) if evidence_parts else "No computational data"

        # PP3 - Multiple lines of computational evidence support pathogenic
        pp3_met = path_predictions >= 2 and benign_predictions == 0
        evaluations.append(CriterionEvaluation(
            criterion="PP3",
            met=pp3_met,
            strength="supporting",
            points=1 if pp3_met else 0,
            evidence=evidence,
            source="computational",
        ))

        # BP4 - Multiple lines of computational evidence support benign
        bp4_met = benign_predictions >= 2 and path_predictions == 0
        evaluations.append(CriterionEvaluation(
            criterion="BP4",
            met=bp4_met,
            strength="supporting",
            points=-1 if bp4_met else 0,
            evidence=evidence,
            source="computational",
        ))

        return evaluations

    def evaluate_case_evidence(
        self,
        de_novo_confirmed: bool = False,
        de_novo_assumed: bool = False,
        cosegregation: bool = False,
        case_count: int = 0,
        in_trans_pathogenic: bool = False,
        phenotype_specific: bool = False,
    ) -> List[CriterionEvaluation]:
        """
        Evaluate case-level evidence criteria: PS2, PM6, PP1, PS4, PM3, PP4.
        These typically require manual curation from cases or literature.
        """
        evaluations = []

        # PS2 - De novo (confirmed parentage)
        evaluations.append(CriterionEvaluation(
            criterion="PS2",
            met=de_novo_confirmed,
            strength="strong",
            points=4 if de_novo_confirmed else 0,
            evidence="De novo with confirmed parentage" if de_novo_confirmed else "Not observed",
            source="case",
        ))

        # PM6 - Assumed de novo (without confirmed parentage)
        evaluations.append(CriterionEvaluation(
            criterion="PM6",
            met=de_novo_assumed and not de_novo_confirmed,
            strength="moderate",
            points=2 if (de_novo_assumed and not de_novo_confirmed) else 0,
            evidence="De novo assumed (parentage not confirmed)" if de_novo_assumed else "Not observed",
            source="case",
        ))

        # PP1 - Cosegregation with disease
        evaluations.append(CriterionEvaluation(
            criterion="PP1",
            met=cosegregation,
            strength="supporting",
            points=1 if cosegregation else 0,
            evidence="Cosegregation observed" if cosegregation else "No cosegregation data",
            source="case",
        ))

        # PS4 - Significantly increased in affected vs controls
        ps4_met = case_count >= 4  # Simplified threshold
        evaluations.append(CriterionEvaluation(
            criterion="PS4",
            met=ps4_met,
            strength="strong" if case_count >= 4 else "moderate",
            points=4 if case_count >= 4 else (2 if case_count >= 2 else 0),
            evidence=f"{case_count} unrelated affected individuals" if case_count > 0 else "No case data",
            source="case",
        ))

        # PM3 - In trans with pathogenic variant (recessive)
        evaluations.append(CriterionEvaluation(
            criterion="PM3",
            met=in_trans_pathogenic,
            strength="moderate",
            points=2 if in_trans_pathogenic else 0,
            evidence="In trans with pathogenic variant" if in_trans_pathogenic else "Not observed",
            source="case",
        ))

        # PP4 - Phenotype highly specific for gene
        evaluations.append(CriterionEvaluation(
            criterion="PP4",
            met=phenotype_specific,
            strength="supporting",
            points=1 if phenotype_specific else 0,
            evidence="Phenotype specific for gene" if phenotype_specific else "Not assessed",
            source="case",
        ))

        return evaluations

    def combine_criteria(
        self,
        pathogenic_criteria: List[CriterionEvaluation],
        benign_criteria: List[CriterionEvaluation]
    ) -> Tuple[str, str, int, int]:
        """
        Combine criteria using point-based system to determine classification.

        Returns: (classification, confidence, path_points, benign_points)
        """
        # Calculate points
        path_points = sum(c.points for c in pathogenic_criteria if c.met)
        benign_points = sum(abs(c.points) for c in benign_criteria if c.met)

        # Check for BA1 (standalone benign)
        ba1_met = any(c.criterion == "BA1" and c.met for c in benign_criteria)
        if ba1_met:
            return "Benign", "Standalone (BA1)", 0, benign_points

        thresholds = self.acmg.get("point_thresholds", {})

        net_points = path_points - benign_points

        # Determine classification
        if net_points >= thresholds.get("pathogenic", 10):
            classification = "Pathogenic"
            confidence = "High" if net_points >= 12 else "Standard"
        elif net_points >= thresholds.get("likely_pathogenic", 6):
            classification = "Likely Pathogenic"
            confidence = "Standard"
        elif net_points <= thresholds.get("benign", -10):
            classification = "Benign"
            confidence = "High" if net_points <= -12 else "Standard"
        elif net_points <= thresholds.get("likely_benign", -6):
            classification = "Likely Benign"
            confidence = "Standard"
        else:
            classification = "Uncertain Significance"
            confidence = "Conflicting" if (path_points > 0 and benign_points > 0) else "Insufficient"

        return classification, confidence, path_points, benign_points

    def classify(
        self,
        annotation: Dict,
        case_evidence: Optional[Dict] = None,
        splice_prediction: Optional[Dict] = None,
    ) -> ClassificationResult:
        """
        Classify a variant using available evidence.

        Args:
            annotation: VEP annotation data
            case_evidence: Optional case-level evidence
            splice_prediction: Optional splice prediction results

        Returns:
            ClassificationResult with classification and criteria
        """
        pathogenic_criteria = []
        benign_criteria = []
        notes = []

        # Extract basic info
        variant = annotation.get("input", annotation.get("variant", "Unknown"))
        gene = annotation.get("gene_symbol", annotation.get("gene", "Unknown"))
        consequence = annotation.get("most_severe_consequence", "")

        # Get canonical transcript data
        canonical = annotation.get("canonical_transcript", {})
        if not canonical and annotation.get("transcript_consequences"):
            for tc in annotation["transcript_consequences"]:
                if tc.get("canonical"):
                    canonical = tc
                    break
            if not canonical:
                canonical = annotation["transcript_consequences"][0]

        # Evaluate PVS1
        pvs1 = self.evaluate_pvs1(annotation, consequence)
        pathogenic_criteria.append(pvs1)

        # Evaluate population frequency
        gnomad_af = annotation.get("gnomad_af")
        freq_criteria = self.evaluate_population_frequency(gnomad_af)
        for c in freq_criteria:
            if c.criterion.startswith("P"):
                pathogenic_criteria.append(c)
            else:
                benign_criteria.append(c)

        # Evaluate computational predictions
        sift_score = canonical.get("sift", {}).get("score") if canonical.get("sift") else None
        sift_pred = canonical.get("sift", {}).get("prediction") if canonical.get("sift") else None
        polyphen_score = canonical.get("polyphen", {}).get("score") if canonical.get("polyphen") else None
        polyphen_pred = canonical.get("polyphen", {}).get("prediction") if canonical.get("polyphen") else None

        # Get splice prediction max score
        spliceai_max = None
        if splice_prediction:
            spliceai_data = splice_prediction.get("spliceai", {})
            spliceai_max = spliceai_data.get("max_score")

        comp_criteria = self.evaluate_computational(
            sift_score, sift_pred, polyphen_score, polyphen_pred,
            spliceai_max=spliceai_max
        )
        for c in comp_criteria:
            if c.criterion.startswith("P"):
                pathogenic_criteria.append(c)
            else:
                benign_criteria.append(c)

        # Evaluate case evidence if provided
        if case_evidence:
            case_criteria = self.evaluate_case_evidence(
                de_novo_confirmed=case_evidence.get("de_novo_confirmed", False),
                de_novo_assumed=case_evidence.get("de_novo_assumed", False),
                cosegregation=case_evidence.get("cosegregation", False),
                case_count=case_evidence.get("case_count", 0),
                in_trans_pathogenic=case_evidence.get("in_trans_pathogenic", False),
                phenotype_specific=case_evidence.get("phenotype_specific", False),
            )
            for c in case_criteria:
                if c.criterion.startswith("P"):
                    pathogenic_criteria.append(c)
                else:
                    benign_criteria.append(c)

        # Combine and classify
        classification, confidence, path_points, benign_points = self.combine_criteria(
            pathogenic_criteria, benign_criteria
        )

        # Add VCEP note if used
        vcep_spec_used = None
        if self.vcep:
            vcep_spec_used = self.vcep.get("title", "VCEP specification")
            notes.append(f"Classification used {vcep_spec_used}")

        return ClassificationResult(
            variant=variant,
            gene=gene,
            classification=classification,
            confidence=confidence,
            pathogenic_points=path_points,
            benign_points=benign_points,
            pathogenic_criteria=pathogenic_criteria,
            benign_criteria=benign_criteria,
            vcep_spec_used=vcep_spec_used,
            notes=notes,
        )


def generate_report(
    result: ClassificationResult,
    annotation: Dict,
    template_path: Optional[Path] = None
) -> str:
    """
    Generate a markdown classification report.
    """
    lines = [
        "# Variant Classification Report",
        "",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Variant Summary",
        "",
        f"| Field | Value |",
        f"|-------|-------|",
        f"| Variant | {result.variant} |",
        f"| Gene | {result.gene} |",
        f"| Classification | **{result.classification}** |",
        f"| Confidence | {result.confidence} |",
        "",
    ]

    if annotation.get("chromosome"):
        lines.extend([
            f"| Chromosome | {annotation['chromosome']} |",
            f"| Position | {annotation.get('start', 'N/A')} |",
        ])

    if annotation.get("rsid"):
        lines.append(f"| rsID | {annotation['rsid']} |")

    if annotation.get("gnomad_af") is not None:
        lines.append(f"| gnomAD AF | {annotation['gnomad_af']:.2e} |")

    lines.extend([
        "",
        "## VCEP Specification Status",
        "",
    ])

    if result.vcep_spec_used:
        lines.extend([
            f"**VCEP Specification Applied:** {result.vcep_spec_used}",
            "",
            "Gene-specific thresholds from the VCEP were used in this classification.",
        ])
    else:
        lines.extend([
            "**No VCEP specification available for this gene.**",
            "",
            "Standard ACMG/AMP criteria were applied.",
        ])

    lines.extend([
        "",
        "## Classification Criteria",
        "",
        "### Evidence Summary",
        "",
        f"| Category | Points |",
        f"|----------|--------|",
        f"| Pathogenic | +{result.pathogenic_points} |",
        f"| Benign | -{result.benign_points} |",
        f"| **Net Score** | **{result.pathogenic_points - result.benign_points}** |",
        "",
    ])

    # Pathogenic criteria table
    met_path = [c for c in result.pathogenic_criteria if c.met]
    if met_path:
        lines.extend([
            "### Pathogenic Criteria Met",
            "",
            "| Criterion | Strength | Points | Evidence |",
            "|-----------|----------|--------|----------|",
        ])
        for c in met_path:
            vcep_flag = " (VCEP)" if c.vcep_modified else ""
            lines.append(f"| {c.criterion}{vcep_flag} | {c.strength} | +{c.points} | {c.evidence} |")
        lines.append("")

    # Benign criteria table
    met_benign = [c for c in result.benign_criteria if c.met]
    if met_benign:
        lines.extend([
            "### Benign Criteria Met",
            "",
            "| Criterion | Strength | Points | Evidence |",
            "|-----------|----------|--------|----------|",
        ])
        for c in met_benign:
            vcep_flag = " (VCEP)" if c.vcep_modified else ""
            lines.append(f"| {c.criterion}{vcep_flag} | {c.strength} | -{abs(c.points)} | {c.evidence} |")
        lines.append("")

    # Evidence details
    lines.extend([
        "## Evidence Details",
        "",
        "### Population Frequency",
        "",
    ])

    if annotation.get("gnomad_af") is not None:
        lines.append(f"- gnomAD global AF: {annotation['gnomad_af']:.2e}")
    else:
        lines.append("- Variant absent from gnomAD")

    lines.extend([
        "",
        "### Computational Predictions",
        "",
    ])

    canonical = annotation.get("canonical_transcript", {})
    if canonical.get("sift"):
        lines.append(f"- SIFT: {canonical['sift']['prediction']} ({canonical['sift']['score']})")
    if canonical.get("polyphen"):
        lines.append(f"- PolyPhen: {canonical['polyphen']['prediction']} ({canonical['polyphen']['score']})")

    # Literature sources
    if annotation.get("pmids"):
        lines.extend([
            "",
            "## Literature Sources",
            "",
        ])
        for pmid in annotation["pmids"]:
            lines.append(f"- PMID: {pmid}")

    # Notes and recommendations
    lines.extend([
        "",
        "## Recommendations",
        "",
    ])

    if result.classification in ["Pathogenic", "Likely Pathogenic"]:
        lines.append("- Consider clinical implications for patient management")
        lines.append("- Family screening may be indicated based on inheritance pattern")
    elif result.classification in ["Benign", "Likely Benign"]:
        lines.append("- Variant unlikely to be disease-causing")
    else:
        lines.append("- Additional evidence may be needed for definitive classification")
        lines.append("- Consider functional studies or case-level data if available")

    if result.notes:
        lines.extend([
            "",
            "## Additional Notes",
            "",
        ])
        for note in result.notes:
            lines.append(f"- {note}")

    lines.extend([
        "",
        "---",
        "*This report was generated using ACMG/AMP criteria.*",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Classify genetic variants using ACMG/AMP criteria",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --annotation vep_result.json
  %(prog)s --annotation vep_result.json --vcep-spec vcep_info.json
  %(prog)s --annotation vep_result.json --evidence case_evidence.json -o report.md
        """,
    )
    parser.add_argument(
        "--annotation", "-a",
        required=True,
        help="VEP annotation JSON file"
    )
    parser.add_argument(
        "--vcep-spec", "-v",
        help="VCEP specification JSON file"
    )
    parser.add_argument(
        "--evidence", "-e",
        help="Case evidence JSON file"
    )
    parser.add_argument(
        "--splice", "-s",
        help="Splice prediction JSON file"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path"
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output as JSON instead of report"
    )
    parser.add_argument(
        "--acmg-criteria",
        type=Path,
        default=ACMG_CRITERIA_FILE,
        help=f"Path to ACMG criteria JSON file (default: {ACMG_CRITERIA_FILE})"
    )

    args = parser.parse_args()

    try:
        # Load annotation
        with open(args.annotation) as f:
            annotation = json.load(f)

        # Load VCEP spec if provided
        vcep_spec = None
        if args.vcep_spec:
            with open(args.vcep_spec) as f:
                vcep_spec = json.load(f)

        # Load case evidence if provided
        case_evidence = None
        if args.evidence:
            with open(args.evidence) as f:
                case_evidence = json.load(f)

        # Load splice predictions if provided
        splice_prediction = None
        if args.splice:
            with open(args.splice) as f:
                splice_prediction = json.load(f)

        # Load ACMG criteria
        acmg_criteria = load_acmg_criteria(args.acmg_criteria)

        # Classify variant
        classifier = VariantClassifier(acmg_criteria, vcep_spec)
        result = classifier.classify(annotation, case_evidence, splice_prediction)

        # Generate output
        if args.json:
            output = json.dumps(result.to_dict(), indent=2)
        else:
            output = generate_report(result, annotation)

        # Write output
        if args.output:
            with open(args.output, "w") as f:
                f.write(output)
            print(f"Report saved to {args.output}", file=sys.stderr)
        else:
            print(output)

        return 0

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
