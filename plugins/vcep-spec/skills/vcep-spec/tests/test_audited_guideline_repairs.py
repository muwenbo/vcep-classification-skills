import re
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

    def test_hht_pvs1_trees_preserve_gene_specific_routes_and_source_gaps(self):
        acvrl1 = guideline("ACVRL1_Variant_Interpretation_Guidelines_v1.1.0.md")
        eng = guideline("ENG_Variant_Interpretation_Guidelines_v1.1.0.md")

        self.assertIn("ACVRL1 ≤ codon 442 → PVS1", acvrl1)
        self.assertIn("ACVRL1 ≤ codon 490 → PVS1_Strong", acvrl1)
        self.assertIn("ACVRL1 → PVS1_Moderate", acvrl1)
        self.assertIn("13 of the slide's 51 connectors", acvrl1)
        self.assertNotIn("last 50bp of penultimate exon", acvrl1)

        self.assertIn("ENG ≤ codon 601", eng)
        self.assertIn("Variant removes >10% of protein → PVS1_Strong", eng)
        self.assertIn("ENG → PVS1_Strong", eng)
        self.assertIn("15 of the slide's 51 connectors", eng)
        self.assertNotIn("Variant removes ≥10% of protein → PVS1_Strong", eng)
        self.assertNotIn("11179217", eng)

    def test_hht_shared_attachments_are_fully_transcribed_without_harmonizing_conflicts(self):
        for gene in ("ACVRL1", "ENG"):
            text = guideline(f"{gene}_Variant_Interpretation_Guidelines_v1.1.0.md")

            self.assertEqual(text.count("Approved: Y; Proposed:"), 39)
            self.assertIn("columns B:F of **Intracellular signaling assays** are hidden", text)
            self.assertIn("Normal: 20-24 hours; Abnormal: <48 hours", text)
            self.assertIn("Normal: Variants with <0.01% frequency", text)
            self.assertIn("population at >0.01% frequency", text)
            self.assertIn("Proposed: PS3; BS3_Supporting", text)
            self.assertIn("normal protein expression cannot be used as benign evidence", text)
            self.assertIn("### Document corrections (2026-08-11)", text)

            for source in (
                f"ClinGen_ACMG_Specifications_{gene}_v1.1.pdf",
                f"{gene} PVS1 Decision Tree.pptx",
                "HHT Phenotype.docx",
                "HHT Functional Assays.xlsx",
            ):
                self.assertIn(source, text)

    def test_atm_transcribes_pvs1_and_functional_attachments_literally(self):
        text = guideline("ATM_Variant_Interpretation_Guidelines_v1.5.0.md")

        self.assertIn("10.5281/zenodo.21421592", text)
        self.assertIn("c.-31+1G>A/C/T", text)
        self.assertIn("c.2467-2A>C/T", text)
        self.assertIn("c.6199-2A>C/G/T", text)
        self.assertIn("c.6347+2T>C", text)
        self.assertIn("c.7515+2C>T", text)
        self.assertIn("Source proposes % survival <10 at 4 days", text)
        self.assertIn("Source proposes % survival >10 at 4 days", text)
        self.assertIn("Approval cell: blank", text)
        self.assertIn("workbook's radiosensitivity proposal says no weight", text)
        self.assertNotIn("PVS1_Strength(RNA)", text)

        for source in (
            "ClinGen_ACMG_Specifications_ATM_v1.5.pdf",
            "ATM PVS1.pdf",
            "ATM PS1.pdf",
            "ATM PM3_BP2.pdf",
            "ATM PS3_BS3.xlsx",
        ):
            self.assertIn(source, text)

    def test_palb2_restores_operational_tables_and_flags_source_conflicts(self):
        text = guideline("PALB2_Variant_Interpretation_Guidelines_v1.2.0.md")

        self.assertIn("10.5281/zenodo.21433968", text)
        self.assertIn("ENST00000261584.9", text)
        self.assertIn("Same donor/acceptor dinucleotide | PS1_Supporting | N/A", text)
        self.assertIn("p.Met296", text)
        self.assertIn("c.48+1G>A/C/T", text)
        self.assertIn("c.3350+2C>A/G", text)
        self.assertIn("c.108+2T>C", text)
        self.assertIn("| Phenotype consistent with PALB2-related FA | 2.0 | 1.0 |", text)
        self.assertIn("| First cancer onset >50 years", text)
        self.assertIn("| First cancer onset 40-50 years", text)
        self.assertIn("removes <10% (>356 nt)", text)
        self.assertNotIn("| **FATKIN** |", text)

        for source in (
            "ClinGen_ACMG_Specifications_PALB2_v1.2.pdf",
            "ClinGen HBOP ACMG Specifications PALB2 version 1.2.docx",
        ):
            self.assertIn(source, text)

    def test_gatm_restores_the_shipped_pvs1_tree_without_silently_resolving_it(self):
        text = guideline("GATM_Variant_Interpretation_Guidelines_v2.0.0.md")

        self.assertIn("10.5281/zenodo.21421625", text)
        self.assertIn("exon present in biologically relevant `NM_001482.3`", text)
        self.assertIn("LoF variant is frequent in general population, or exon is absent", text)
        self.assertIn("Different functional transcript uses an alternative start", text)
        self.assertIn("conflicts with the core PDF's unconditional Moderate assignment", text)
        self.assertIn("`*985` [sic]", text)
        self.assertIn("Values strictly above 15% and below 30% are not assigned", text)
        self.assertNotIn("#### PM3 Point System", text)
        self.assertNotIn("| Indeterminate | 16-29% of normal |", text)

        for source in (
            "ClinGen_ACMG_Specifications_GATM_v2.0.pdf",
            "Appendix 1_GATM (AGAT) _ PVS1 decision tree.pptx",
            "Appendix 2_GATM (AGAT) _ exons.xlsx",
            "Appendix 3_GATM (AGAT) _ functional studies.xlsx",
            "Appendix 4_GATM (AGAT) _ MAFs.pptx",
        ):
            self.assertIn(source, text)

    def test_gamt_transcribes_all_appendices_and_marks_package_conflicts(self):
        text = guideline("GAMT_Variant_Interpretation_Guidelines_v2.0.0.md")

        self.assertIn("10.5281/zenodo.21421631", text)
        self.assertIn("sole worksheet is named `GAA_PVS1`", text)
        self.assertIn("Proven in tandem, no known impact on reading frame and NMD", text)
        self.assertIn("Presumed in tandem, no known impact on reading frame and NMD", text)
        self.assertIn("`*333` [sic]", text)
        self.assertIn("P/LP `n=20`, VUS `n=24`, and B/LB `n=3`", text)
        self.assertIn("normal and abnormal thresholds were `Not provided`", text)
        self.assertIn("older wording that non-canonical +3/-3 variants could meet PS3", text)
        self.assertIn("0.773-0.932; the source does not state endpoint operators", text)
        self.assertNotIn("#### PM3 Point System", text)
        self.assertNotIn("| <1 | PP4 not met |", text)

        for source in (
            "ClinGen_ACMG_Specifications_GAMT_v2.0.pdf",
            "Appendix 1_GAMT.xlsx",
            "Appendix 2_GAMT functional studies.xlsx",
            "Appendix 3_GAMT MAF thresholds.pptx",
            "Appendix 4_GAMT REVEL scores.pptx",
            "GAMT PVS1 flowchart.xlsx",
        ):
            self.assertIn(source, text)

    def test_round14_remaining_specs_record_every_distributed_source(self):
        packages = {
            "PAH_Variant_Interpretation_Guidelines_v2.0.0.md": (
                "ClinGen_ACMG_Specifications_PAH_v2.0.pdf",
                "PAH PP3 REVEL data explanation.docx",
                "PAH PP3 REVEL data explanation (3).docx",
                "PAH PS3 functional data.xlsx",
                "PAH PVS1 decision tree.pdf",
            ),
            "MYOC_Variant_Interpretation_Guidelines_v2.1.0.md": (
                "ClinGen_ACMG_Specifications_MYOC_v2.1.pdf", "Table 3.jpg",
            ),
            "DICER1_Variant_Interpretation_Guidelines_v1.4.0.md": (
                "ClinGen_ACMG_Specifications_DICER1_v1.4.pdf",
                "Evidence Criteria Combinations.jpg", "PP4 Flowchart and Second Hits.jpg",
                "PVS1.pdf", "Phenotype Table.jpg", "Table for Tallying Proband Points.jpg",
            ),
            "F8_Variant_Interpretation_Guidelines_v2.0.0.md": (
                "ClinGen_ACMG_Specifications_F8_v2.0.pdf", "F8 Approved Functional Assays.xlsx",
                "F8 Decision Tree for PVS1 Rule Code.pptx", "F8_F9 Pilot Study Results.xlsx",
                "Guidance for Combined De Novo Rule Code (PS2_PM6).docx",
                "Guidance for Combining Pathogenic and Benign Rule Codes.docx",
            ),
            "VHL_Variant_Interpretation_Guidelines_v1.1.0.md": (
                "ClinGen_ACMG_Specifications_VHL_v1.1.pdf", "Denovo-Confirmed-and-Not-Confirmed.jpg",
                "Functional Assay Documentation.xlsx", "Germline and Somatic Hotspots.jpg",
                "Meiosis.jpg", "PS4 Cut-Offs.jpg", "Proband Scoring.jpg", "VHL PVS1 Decision Tree.jpg",
            ),
            "VWF_Variant_Interpretation_Guidelines_v1.0.0.md": (
                "ClinGen_ACMG_Specifications_VWF_v1.0.pdf", "Introduction to von Willebrand disease.docx",
                "VWD 2A_2M_2N functional assays.xlsx", "VWD Type 2 Rule Set Instructions for Use.docx",
                "VWD type 2 List of Approved Functional Assays.xlsx", "VWD type 2 PP4 rule guidance.docx",
                "VWD type 2 PS2_PM6 rule guidance.docx",
            ),
            "VWF_Type2N_Variant_Interpretation_Guidelines_v1.0.0.md": (
                "ClinGen_ACMG_Specifications_VWF_v1.0.pdf", "Intro the VWD.docx",
                "SVI Recommendations for PM3.docx", "VWD 2N functional assays.xlsx",
                "VWD Type 2 Rule Set Instructions for Use.docx", "VWD type 2 PS2_PM6 rule guidance.docx",
            ),
            "IDUA_Variant_Interpretation_Guidelines_v1.2.0.md": (
                "ClinGen_ACMG_Specifications_IDUA_v1.2.pdf", "Appendix 1_PVS1 strength_IDUA.xlsx",
                "Appendix 2_PVS1_Decision Tree_IDUA.pptx", "Appendix 3_Functional assays.xlsx",
                "Appendix 4_PM3 points system_IDUA.pdf", "Appendix 5_PP1 guidance_IDUA.pdf",
            ),
            "RPGR_Variant_Interpretation_Guidelines_v1.0.0.md": (
                "ClinGen_ACMG_Specifications_RPGR_v1.0.pdf",
                "PS3 Functional Evidence - RPGR Specifications.xlsx", "PVS1 Decision Tree for RPGR.pptx",
                "Phenotype Features - RPGR Specifications.docx", "RPGR PVS1 and PVS1 (RNA) Decision Tree.pdf",
                "Standard Operating Procedure - RPGR- V.7.pdf", "c.730A-T Variant Report.pdf",
            ),
            "KCNQ1_Variant_Interpretation_Guidelines_v1.0.0.md": (
                "ClinGen_ACMG_Specifications_KCNQ1_v1.0.pdf", "KCNQ1 PS3 BS3 strength overview.pptx",
                "KCNQ1 PVS1 Decision Tree.pptx", "KCNQ1 Rule Combination Guidance.docx",
                "PS3 BS3 functional assays KCNQ1.xlsx", "Updated results of KCNQ1 pilot curations.xlsx",
            ),
            "RPE65_Variant_Interpretation_Guidelines_v1.0.0.md": (
                "ClinGen_ACMG_Specifications_RPE65_v1.0.pdf", "PM3 Tables.pdf",
                "PP3 performance of multiple prediction models.pdf", "PS2 PM6 Tables.pdf",
                "PS3 Approved functional assays.xlsx", "RPE65 Pilot Variants, Sept.11, 2023.xlsx",
                "RPE65 Rule combination rules.pdf", "RPE65-specific PVS1 Decision Tree.pdf",
            ),
            "RS1_Variant_Interpretation_Guidelines_v1.0.0.md": (
                "ClinGen_ACMG_Specifications_RS1_v1.0.pdf", "RS1 Functional Evidence Assays for PS3 _ BS3.xlsx",
                "RS1 PS2_PM6 Tables.pdf", "RS1 PVS1 Decision Tree.pdf",
            ),
            "PIK3CD_Variant_Interpretation_Guidelines_v1.0.0.md": (
                "ClinGen_ACMG_Specifications_PIK3CD_v1.0.pdf", "PIK3CD_pilot_results.xlsx",
                "Phenotype scoring criteria per affected individual (PS4 and PP4).jpg",
                "Points system to reach final classification.pdf",
                "Recommendation for determining the appropriate PS4 evidence strength level based on the number of affected individuals meeting the phenotype criteria .jpg",
                "Summary_of_PIK3CD_updates.docx", "Tables 1 & 2.jpg",
            ),
            "ABCA4_Variant_Interpretation_Guidelines_v1.0.0.md": (
                "ClinGen_ACMG_Specifications_ABCA4_v1.0.pdf", "ABCA4 Functional assay Guidance.xlsx",
                "Functional assay Guidance.xlsx", "ABCA4 PM3 Guidance.docx",
                "ABCA4 PP4 Proband Scoring Table.pptx", "ABCA4 PS2 Guidance.docx",
                "ABCA4 PVS1 Flowchart.pdf", "BS1 Exclusion Variants.docx",
            ),
            "AIPL1_Variant_Interpretation_Guidelines_v1.0.0.md": (
                "ClinGen_ACMG_Specifications_AIPL1_v1.0.pdf", "AIPL1 Rule combination rules.pdf",
                "AIPL1-specific PVS1 Decision Tree.pdf", "PM3 Tables.pdf", "PS2_PM6 Tables.pdf",
                "PS3 Approved Functional assays.xlsx",
            ),
        }

        self.assertEqual(len(packages), 15)
        for filename, sources in packages.items():
            text = guideline(filename)
            self.assertIn("## Document corrections (2026-08-17)", text)
            for source in sources:
                self.assertIn(source, text, f"{filename} omits {source}")

    def test_round14_preserves_exact_thresholds_conflicts_and_provenance(self):
        rpe65 = guideline("RPE65_Variant_Interpretation_Guidelines_v1.0.0.md")
        aipl1 = guideline("AIPL1_Variant_Interpretation_Guidelines_v1.0.0.md")
        type2n = guideline("VWF_Type2N_Variant_Interpretation_Guidelines_v1.0.0.md")
        pah = guideline("PAH_Variant_Interpretation_Guidelines_v2.0.0.md")
        idua = guideline("IDUA_Variant_Interpretation_Guidelines_v1.2.0.md")
        abca4 = guideline("ABCA4_Variant_Interpretation_Guidelines_v1.0.0.md")

        for text in (rpe65, aipl1):
            self.assertIn("prints only the four exact totals above", text)
            self.assertNotIn("| 0.50 - 0.75 |", text)
            self.assertNotIn("| 2.0 - 3.75 | PM3_Strong", text)
        self.assertIn("does not provide `≥` operators", type2n)
        self.assertNotIn("| ≥0.5 | Supporting |", type2n)
        self.assertIn("core PDF defines PP3_Supporting as REVEL `0.644–0.733`", pah)
        self.assertIn("explanation.docx` describe the 30-variant review bin as `0.644–0.773`", pah)
        self.assertIn("| 36413997 | Pejaver et al |", idua)
        self.assertNotIn("| 3641399 | Pejaver et al |", idua)
        self.assertIn("**Source panel:** ClinGen ABCA4 Variant Curation Expert Panel", abca4)
        self.assertNotIn("**Prepared by:** ClinGen ABCA4 Variant Curation Expert Panel", abca4)
        self.assertNotIn("**Last Updated:** January 2026", abca4)

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


def _has_complete_oza_grid(text: str) -> bool:
    """True if text contains a complete 0-10 x 0-10 Oza recessive LOD grid:
    a header row 0..10 followed by 11 data rows labelled 0..10."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip().strip("*") for c in line.strip().strip("|").split("|")]
        nums = [c for c in cells if re.fullmatch(r"\d+", c)]
        if nums[:11] != [str(n) for n in range(11)]:
            continue
        labels = []
        j = i + 1
        while j < len(lines) and lines[j].strip().startswith("|"):
            rcells = [c.strip().strip("*") for c in lines[j].strip().strip("|").split("|")]
            if set("".join(rcells)) <= set("-: "):
                j += 1
                continue
            if re.fullmatch(r"\d+", rcells[0]):
                labels.append(rcells[0])
            else:
                break
            j += 1
        if labels == [str(n) for n in range(11)]:
            return True
    return False


class PP1SegregationGridTests(unittest.TestCase):
    """The PP1 co-segregation LOD grids were silently truncated in several
    specs before the 2026-08 remediation (handoff §8). These lock the fixes:
    specs that reproduce the recessive Oza 4b grid must carry the complete
    11x11 lookup, and the congenital-myopathy specs whose packages ship no
    grid must keep their explicit no-substitution guard."""

    COMPLETE_GRID_SPECS = (
        "ADA_Variant_Interpretation_Guidelines_v2.2.0.md",
        "DCLRE1C_Variant_Interpretation_Guidelines_v2.2.0.md",
        "IL7R_Variant_Interpretation_Guidelines_v2.2.0.md",
        "IL2RG_Variant_Interpretation_Guidelines_v2.2.0.md",
        "JAK3_Variant_Interpretation_Guidelines_v2.3.0.md",
        "ACADVL_Variant_Interpretation_Guidelines_v2.2.0.md",
    )

    def test_recessive_oza_grid_is_complete_11x11(self):
        for name in self.COMPLETE_GRID_SPECS:
            with self.subTest(guideline=name):
                self.assertTrue(
                    _has_complete_oza_grid(guideline(name)),
                    f"{name}: PP1 recessive LOD grid is truncated or missing",
                )

    def test_ryr1_specs_refuse_generic_oza_grid_substitution(self):
        for name in (
            "RYR1_AR_Variant_Interpretation_Guidelines_v2.0.0.md",
            "RYR1_AD_Variant_Interpretation_Guidelines_v2.0.0.md",
        ):
            with self.subTest(guideline=name):
                text = guideline(name)
                self.assertIn("Do not substitute a generic Oza et al. grid", text)
                self.assertFalse(
                    _has_complete_oza_grid(text),
                    f"{name}: carries an Oza grid its package does not distribute",
                )


if __name__ == "__main__":
    unittest.main()
