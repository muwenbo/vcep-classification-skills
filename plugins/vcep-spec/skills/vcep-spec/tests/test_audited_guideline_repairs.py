import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
GUIDELINES = (
    ROOT
    / "plugins"
    / "variant-classifier"
    / "skills"
    / "variant-classifier"
    / "data"
    / "vcep-guidelines"
)


def guideline(name: str) -> str:
    return (GUIDELINES / name).read_text(encoding="utf-8")


class AuditedGuidelineRepairTests(unittest.TestCase):
    def test_tp53_pp3_bp4_tree_keeps_c0_c15_under_bayesdel_positive_branch(self):
        text = guideline("TP53_Variant_Interpretation_Guidelines_v2.4.0.md")
        self.assertIn("aGVGD class **C0-C15** AND BayesDel **≥ 0.16**", text)
        self.assertIn("BayesDel ≥ 0.16 + aGVGD C0-C15 → *No evidence*", text)
        self.assertNotIn("aGVGD class **C0-C15** AND BayesDel **< 0.16**", text)
        self.assertNotIn("BayesDel < 0.16 + aGVGD C0-C15 → *No evidence*", text)

    def test_myh7_does_not_claim_a_vcep_ps2_pm6_point_system(self):
        text = guideline("MYH7_Variant_Interpretation_Guidelines_v2.0.0.md")
        self.assertNotIn("#### PS2/PM6 Point System", text)
        self.assertNotIn("#### Evidence Strength Thresholds", text)
        self.assertIn(
            "| PS2 | Applicable | Strong only | Refer to SVI guidance; no point system is specified by GN002 |",
            text,
        )
        self.assertIn(
            "| PM6 | Applicable | Moderate only | Refer to SVI guidance; no point system is specified by GN002 |",
            text,
        )

    def test_hearing_loss_removes_unsourced_classification_machinery(self):
        text = guideline("Hearing_Loss_VCEP_Variant_Interpretation_Guidelines_v2.0.0.md")
        self.assertIn("| TECTA | Nonsyndromic SNHL, AD/AR | Yes |", text)
        self.assertNotIn("Yes (AR only)", text)
        self.assertIn("Fisher Exact or Chi-Squared analysis shows statistical increase in cases over controls", text)
        self.assertNotIn("with a P value that is <=0.05", text)
        self.assertIn("| Supporting | 2 affected relatives | 1 affected relative |", text)
        self.assertIn("| Moderate | 4 affected relatives | 2 affected relatives |", text)
        self.assertIn("| Strong | 5 affected relatives | 3 affected relatives |", text)
        self.assertNotIn("#### AR Segregation LOD Score Table", text)
        self.assertNotIn("### Appendix D: Variant Exclusion List", text)
        self.assertNotIn("PVS1 AND PM2_Supporting", text)
        self.assertIn("GN005 does not specify general rules for combining criteria", text)

    def test_apc_transcribes_pvs1_and_phenotype_supplements(self):
        text = guideline("APC_Variant_Interpretation_Guidelines_v2.1.0.md")
        self.assertIn("codon 49 through codon 2645", text)
        self.assertIn("Full-gene deletion", text)
        self.assertIn("Exons 3, 4, 5, 10, 12, 15, and 16", text)
        self.assertIn("Proven in tandem and reading frame disrupted", text)
        self.assertIn("Initiation-codon variant", text)
        self.assertIn("c.136-1G>A,C,T", text)
        self.assertIn("c.1959-1G>A", text)
        self.assertIn("**maximum 1 phenotype point per proband**", text)
        self.assertIn("20–99 colorectal adenomas at age ≤20 years", text)
        self.assertIn("≥100 colorectal adenomas at age ≤30 years", text)
        self.assertIn("| ≥1 | 2 | 1 |", text)
        self.assertIn("| 0.5 | 1 | 0.5 |", text)
        self.assertNotIn("Additional points based on context", text)

    def test_brca1_includes_exon_and_rna_weighting_rules(self):
        text = guideline("BRCA1_Variant_Interpretation_Guidelines_v1.2.0.md")
        self.assertIn("Full-gene deletion is stand-alone pathogenic evidence", text)
        self.assertIn("E8(9)", text)
        self.assertIn("E9(10)", text)
        self.assertIn("PVS1_N/A", text)
        self.assertIn("PM5_N/A", text)
        self.assertIn("exon 7(8)", text)
        self.assertIn("PVS1_N/A (RNA)", text)
        self.assertIn("BP7_Strong (RNA)", text)
        self.assertIn("last 3 bases of the exon and 6 intronic nucleotides", text)
        self.assertIn("first base of the exon and 20 upstream intronic nucleotides", text)
        self.assertNotIn("partial loss of function, apply as PVS1_Moderate (RNA)", text)
        self.assertNotIn("minor impact, apply as PVS1_Supporting (RNA)", text)

    def test_brca2_transcribes_table4_instead_of_deferring_to_the_excel_file(self):
        """GN097 punted to "separate Excel file" in six places; Table 4 and
        Supplementary Table 1 are the actual source of PVS1/PM5_PTC weights."""
        text = guideline("BRCA2_Variant_Interpretation_Guidelines_v1.2.0.md")

        self.assertIn("#### Table 4 — BRCA2 codes by exon", text)
        self.assertIn("#### Table 4 — canonical splice site (±1,2) codes", text)
        self.assertIn("#### Supplementary Table 1 — BRCA2 PM5_PTC weights", text)
        self.assertNotIn("(separate Excel file)", text)
        self.assertNotIn("(separate Excel spreadsheet)", text)

        # All 27 exons carry a rule row.
        self.assertEqual(text.count("\n| **E"), 27)

        # Exon-specific weights that differ from the majority; a generic ladder
        # would flatten these.
        self.assertIn("| **E4** |", text)
        self.assertIn("PM5 (PTC)", text)          # E4 is Moderate, not Strong
        self.assertIn("PM5_N/A", text)            # E6 and E12 grant nothing
        self.assertIn("PM5_Supporting (PTC)", text)  # E21, E26

        # E27's rule is conditional on where the termination codon falls.
        self.assertIn("`<p.T3310` → PVS1", text)
        self.assertIn("`>p.E3309` → PVS1_N/A", text)

    def test_brca2_pm5_ptc_attributes_weight_to_the_termination_codon_exon(self):
        """The source read-me is explicit that this is not the variant's exon."""
        text = guideline("BRCA2_Variant_Interpretation_Guidelines_v1.2.0.md")
        self.assertIn("the exon in which the termination codon occurs", text)
        self.assertNotIn("Weight determined by exon where the nucleotide change occurs", text)

    def test_brca1_and_brca2_are_separate_guidelines(self):
        """The combined BRCA1_BRCA2 file duplicated BRCA1 content that had
        already been repaired separately, so the two diverged."""
        import json

        registry = json.loads(
            (
                ROOT / "plugins" / "variant-classifier" / "skills"
                / "variant-classifier" / "data" / "vcep_registry.json"
            ).read_text(encoding="utf-8")
        )["specifications"]
        by_id = {e["spec_id"]: e for e in registry}

        self.assertEqual(
            by_id["GN092"]["guideline_file"],
            "BRCA1_Variant_Interpretation_Guidelines_v1.2.0.md",
        )
        self.assertEqual(
            by_id["GN097"]["guideline_file"],
            "BRCA2_Variant_Interpretation_Guidelines_v1.2.0.md",
        )
        self.assertFalse(
            (GUIDELINES / "BRCA1_BRCA2_Variant_Interpretation_Guidelines_v1.2.md").exists()
        )

    def test_every_guideline_filename_uses_three_part_versions(self):
        """GN097's old filename was the corpus's only x.y violation, and it
        slipped through because verification checked the version field only."""
        import re

        offenders = [
            p.name for p in GUIDELINES.glob("*.md")
            if not re.search(r"v\d+\.\d+\.\d+\.md$", p.name)
        ]
        self.assertEqual(offenders, [])

    def test_generation_workflow_does_not_supply_generic_fallback_rules(self):
        template = (
            ROOT / "plugins" / "vcep-spec" / "skills" / "vcep-spec" / "template.md"
        ).read_text(encoding="utf-8")
        skill = (
            ROOT / "plugins" / "vcep-spec" / "skills" / "vcep-spec" / "SKILL.md"
        ).read_text(encoding="utf-8")

        self.assertIn("{PS2_PM6_POINT_SYSTEM_IF_SPECIFIED}", template)
        self.assertIn("{COMBINING_RULES_IF_SPECIFIED}", template)
        self.assertNotIn("#### PS2/PM6 Point System", template)
        self.assertNotIn("1 Very Strong **AND** ≥1 Strong", template)
        self.assertNotIn("**Based on:** Richards et al.", template)
        self.assertIn("Never fill a source gap with generic ACMG/AMP", skill)
        self.assertIn("placeholders are not evidence", skill)


if __name__ == "__main__":
    unittest.main()
