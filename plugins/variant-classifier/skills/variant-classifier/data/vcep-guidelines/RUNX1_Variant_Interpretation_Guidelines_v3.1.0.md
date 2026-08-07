# ClinGen Myeloid Malignancy VCEP Variant Interpretation Guidelines for RUNX1

**Version:** 3.1
**Released:** 2/13/2026
**Affiliation:** Myeloid Malignancy VCEP (MM-VCEP)
**DOI:** 10.5281/zenodo.21421484
**Type (as stated by VCEP):** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015
**Description (as stated by VCEP):** MM-VCEP Specifications for RUNX1 Variant Curation
**Rights Holder:** The Clinical Genome Resource (ClinGen)
**Source basis:** ClinGen Criteria Specification Registry record GN008 (`ClinGen_ACMG_Specifications_RUNX1_v3.1.pdf`) plus the six supplementary files distributed with it. Everything below is transcribed from those files; nothing is supplied from generic ACMG/AMP or SVI material.

---

## Release Notes (verbatim from the specification)

> (1) New gnomAD MAF threshold for PM2_supporting ≤ 0.00005 to account for larger population in gnomAD v4.
>
> (2) Upgraded strength of PM1 to PM1_strong when used for missense variants at the following residues: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204. Added a caveat to not use PM5/PS1 at any level if PM1 was applied.
>
> (3) Upgraded strength of PM4 to PM4_strong when used for missense variants at the following residues: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204. Added an allowance to use PM4 for stop-loss variants.
>
> (4) Established PVS1_variable (RNA) and BP7_variable (RNA) to be used when RNA data is available for splicing variants. PS1 is now able to be used for splicing variants with the same predicted splicing event as a known pathogenic/likely pathogenic splicing variant.
>
> (5) Conservation data is no longer considered when applying BP7. BP7 is limited to intronic variants, and synonymous variants which don't occur in the last 3 nucleotides preceding a canonical donor splice site or the first nucleotide following a canonical acceptor splice site.
>
> (6) Revised PM5 to account for Grantham scores when evaluating missense variants.

> **Source note (flagged, not corrected):** release note (3) says PM4 was upgraded "when used for **missense** variants" at those 13 residues. PM4 is a protein-length criterion and the PM4 body of the specification applies PM4_strong to **in-frame deletion/insertion** variants impacting those residues. The release-note wording appears to be a copy of release note (2); transcribed as written.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | RUNX1 (HGNC:10471) |
| **HGNC Name** | RUNX family transcription factor 1 |
| **Transcript** | NM_001754.4 (RUNX1c) |
| **Disease** | hereditary thrombocytopenia and hematologic cancer predisposition syndrome (MONDO:0011071) |
| **Inheritance** | Autosomal dominant inheritance |
| **Genomic reference used in the CNV decision tree** | NC_000021.9 |

**Keywords (verbatim):** human biology genomics variant classification clingen disease standards RUNX1 NM_001754.4 (RUNX1c) Autosomal dominant inheritance hereditary thrombocytopenia and hematologic cancer predisposition syndrome

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PS4 - Prevalence in Affected](#ps4---prevalence-in-affected)
   - [PM1 - Mutational Hot Spot](#pm1---mutational-hot-spot)
   - [PM2 - Absent from Controls](#pm2---absent-from-controls)
   - [PM3 - In Trans with Pathogenic](#pm3---in-trans-with-pathogenic)
   - [PM4 - Protein Length Changes](#pm4---protein-length-changes)
   - [PM5 - Novel Missense at Same Residue](#pm5---novel-missense-at-same-residue)
   - [PM6 - De Novo (Assumed)](#pm6---de-novo-assumed)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP2 - Missense in Constrained Gene](#pp2---missense-in-constrained-gene)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
   - [PP4 - Phenotype Specificity](#pp4---phenotype-specificity)
   - [PP5 - Reputable Source](#pp5---reputable-source)
2. [Benign Criteria](#benign-criteria)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications — MM-VCEP notes (verbatim):**

(1) We recommend using RUNX1 isoform c as the default transcript (NM_001754.4), since this is the isoform used for annotation by most clinical laboratories.

(2) Three major isoforms (a, b, c) are expressed by use of two promoters and alternative splicing. Expression of the short human RUNX1a isoform has been shown to favor expansion of the hematopoietic stem cell (HSC) pool, whereas expression of the full length RUNX1b and RUNX1c isoforms function to promote hematopoietic differentiation. *RUNX1* LOF variants are a common mechanism of disease in familial platelet disorder with predisposition to acute myeloid leukemia (FPD/AML). C-terminal truncating variants not predicted to undergo nonsense-mediated mRNA decay (NMD) are classified as **PVS1_strong**, deletions of exon 1-3, presumably only affecting RUNX1 isoform c, meet **PVS1_moderate**.

(3) Most splicing effects are based on predictions. The rules can be modified in the future if new functional evidence becomes available. The rules can be modified in the future when RNA evidence becomes available using Walker et al., 2023, PMID: 37352859 as a guide; modification of strength should be based on the quality of the RNA study where:

1. Comparison to a control is necessary
2. Patient RNA is better than minigene assays
3. Primers are designed to capture the possibility of multi-exonic/multi-cassette events
4. NMD inhibitors (e.g., puromycin, proprietary molecule found in PAXgene tubes), particularly when the predicted effect is nonsense-mediated decay, are used
5. Quantification of the effect by SNP analysis is better than PSI (percent splicing index) analysis is better than capillary electrophoresis is better than estimation by gel band density
6. Multiple studies are better than a single study

\*Caution should be used in modifying strength when the effect of the splicing impact is incomplete ("leaky" splice site) or unclear.

**RUNX1 Specification:**

Per modified *RUNX1* PVS1 decision tree for single-nucleotide variants (SNVs) and CNVs and table of splicing effects.
Strength-modified: **PVS1, PVS1_Strong, PVS1_Moderate**

**PVS1_Variable (RNA):** When RNA/splicing data is available for a variant, apply PVS1 at the appropriate strength level based on the predicted effect of the aberrant mRNA on protein translation as it corresponds to the PVS1_Variable splicing table. Strength may also be modified based on the quality of the RNA analysis (as described above). For "leaky" splice sites, strength level should be decreased by one if a near-complete impact is demonstrated, but no code should be applied if an incomplete impact is demonstrated. Refer to Walker et al., 2023, PMID: 37352859 for additional guidance.

> **Flagged gap:** the specification refers to a "**PVS1_Variable splicing table**". No table with that name is distributed with GN008. The distributed splicing table is titled *Summary of splicing effects* ([Appendix C](#appendix-c--summary-of-splicing-effects-canonical-splice-site-variants)) and covers canonical GT-AG ±1,2 sites only. Whether these are the same table is not stated by the VCEP. Not specified by this VCEP beyond the referenced Walker et al., 2023 guidance.

Applicable variant classes listed by the VCEP:
- SNVs, Indels/Delins, Splicing Variants → [*RUNX1* PVS1 decision tree for SNVs](#appendix-a--runx1-pvs1-decision-tree-for-snvs)
- CNVs → [*RUNX1* PVS1 decision tree for CNVs](#appendix-b--runx1-pvs1-decision-tree-for-cnvs)
- Canonical Splice Site Variants (see Supplemental Table) → [Summary of splicing effects](#appendix-c--summary-of-splicing-effects-canonical-splice-site-variants)

#### Strength Levels

| Strength | Criteria | Default point value | Modification type |
|----------|----------|---------------------|-------------------|
| **Very Strong (PVS1)** | Per modified RUNX1 PVS1 decision tree for SNVs and CNVs and table of splicing effects. | 8 | Gene-specific |
| **Strong (PVS1_Strong)** | Per modified RUNX1 PVS1 decision tree for SNVs and CNVs and table of splicing effects. | 4 | Gene-specific, Strength |
| **Moderate (PVS1_Moderate)** | Per modified RUNX1 PVS1 decision tree for SNVs and CNVs and table of splicing effects. | 2 | Gene-specific, Strength |
| **Supporting** | Not specified by this VCEP as a standalone PVS1 tier (PVS1_Supporting appears only as an *input* code in the PS1 splicing application table, Appendix D). | — | — |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val→Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications — MM-VCEP notes (verbatim):**

(1) The previously established pathogenic variant must be reviewed by the MM-VCEP and asserted pathogenic/likely pathogenic before this rule can be applied.

(2) For missense variants, RNA data or agreement in splicing predictor show no impact on splicing.

(3) For splice site variants, do not apply this code except for variants in the canonical donor/acceptor ("dinucleotide") sites, the U2 donor motif (last 3 bases of the exon and 6 nucleotides of the intron), or the U2 acceptor motif (20 nucleotides of the intron and 1st base of the exon). Splicing predictions for the variant being evaluated and the known pathogenic/likely pathogenic (as assessed by VCEP rules) should match before consideration of the criterion, with at least similar scores. Do not apply for +2G>C variants.

**RUNX1 Specification:**

| Strength | Criteria | Default point value | Modification type |
|----------|----------|---------------------|-------------------|
| **Strong (PS1)** | *Missense:* Same amino acid change as a previously established **pathogenic** variant regardless of nucleotide change. *Splice site:* **PS1_Variable** — follow recommendations from the ClinGen SVI Splicing Subgroup (Walker et al., 2023, PMID: 37352859). | 4 | General recommendation, Strength |
| **Moderate (PS1_Moderate)** | *Missense:* Same amino acid change as a previously established **likely pathogenic** variant regardless of nucleotide change. *Splice site:* **PS1_Variable** — follow recommendations from the ClinGen SVI Splicing Subgroup (Walker et al., 2023, PMID: 37352859). | 2 | General recommendation, Strength |

The specification distributes the SVI splicing subgroup weighting table as the supplementary file **PS1 splicing application** — transcribed in full at [Appendix D](#appendix-d--ps1-splicing-application-svi-table-2).

**Interaction caveat (stated under PM5):** PS1 cannot be used at any level if PM1 was applied.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications — MM-VCEP notes (verbatim):**

(1) The FPD/AML phenotype is not highly specific and there is substantial genetic heterogeneity. We thus concluded that due to the lack of a highly specific phenotype and genetic heterogeneity, the maximum allowable value is 1 point contributing to the overall score.

(2) The phenotype of a deleterious *RUNX1* mutation encompasses at least one of the following three criteria:

1. **Mild to moderate thrombocytopenia with normal platelet size and volume in the absence of other causative factors** such as autoimmune (e.g. antibodies against platelet surface antigens) or drug-related thrombocytopenia.
2. **Platelet ultrastructural and/or functional defects** including platelet alpha or dense granule secretion defects or impaired platelet aggregation - particularly in response to collagen and epinephrine.
3. Diagnosis of a **hematologic malignancy, most commonly affecting the myeloid lineage causing acute myeloid leukemia (AML) or myelodysplastic syndrome (MDS)**, less frequently involving the lymphoid lineage manifesting as T-acute lymphoblastic leukemia (T-ALL). There are rare case-reports of patients with germline *RUNX1* mutations and mixed myeloproliferative syndromes/MDS such as chronic myelomonocytic leukemia, as well as case-reports of patients with B-ALL, and hairy-cell leukemia.

(3) No family history is defined as the absence of the variant and any of the *RUNX1*-phenotypic criteria in first and second-degree relatives.

(4) The maximum allowable strength by combining **PS2** and **PM6** is to apply one moderate or two supporting rules (the maximum allowable value is still 1 point).

**RUNX1 Specification:**

Following the ClinGen Sequence Variant Interpretation (SVI) Working Group guidance, *de novo RUNX1* variants will be scored at the third tier of the point-based system ("Phenotype consistent with gene but not highly specific and high genetic heterogeneity") with maximum allowable value of 1 point contributing to overall score:

| Strength | Criteria | Default point value | Modification type |
|----------|----------|---------------------|-------------------|
| **Moderate (PS2_Moderate)** | ≥ 2 proven *de novo* occurrences (both maternity and paternity confirmed) in patients with FPD/AML phenotype. | 2 | Disease-specific, Strength |
| **Supporting (PS2_Supporting)** | 1 proven *de novo* occurrence (both maternity and paternity confirmed) in a patient with FPD/AML phenotype. | 1 | Disease-specific, Strength |

> **De novo point matrix:** The VCEP does **not** reproduce the SVI de novo points-per-occurrence matrix. It only states that *RUNX1* is scored at the **third tier** of the SVI point-based system, with a cap of 1 point. Not specified by this VCEP; consult the referenced ClinGen SVI Working Group guidance.
>
> **Internal tension (flagged):** the tier cap is "maximum allowable value is 1 point", yet PS2_Moderate carries a default point value of 2. The specification does not reconcile these; both are transcribed as written.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications — MM-VCEP notes (verbatim):**

1. **Transactivation assays** demonstrating altered transactivation compared to wildtype (wt) are often performed as functional studies to evaluate the pathogenicity of a *RUNX1* variant. Promoter sequences of *M-CSFR*, *PF4*, *C-FMS* and *GZMB*, containing consensus *RUNX1* binding sites TGTGGT, have been used for this purpose. The transactivation assay must include wt and known pathogenic controls, as well as co-expression with CBFâ.
2. Data from **secondary assays** are frequently used to evaluate an altered function of mutant RUNX1. Electrophoretic mobility shift assays and yeast hybrid assays are performed to demonstrate decreased DNA binding affinity, and co-immunoprecipitation assays, fluorescence resonance energy transfer assays and affinity assays can demonstrate diminished heterodimerization ability of mutant RUNX1 with CBFâ. Abnormal cellular localization of mutant RUNX1 can be shown by immunofluorescence and cell-fractionation with Western Blot. Sorted primary hematopoietic stem and progenitor cells can be used for demonstration of reduced colony-forming potential and xenotransplantation experiments may reveal abnormal function of mutant RUNX1 *in vivo*.

> **Source typo (flagged, preserved):** "CBFâ" appears where "CBFβ" is intended — a mojibake artifact present in the source PDF. Transcribed verbatim.

**RUNX1 Specification:**

| Strength | Criteria | Default point value | Modification type |
|----------|----------|---------------------|-------------------|
| **Strong (PS3)** | Transactivation assays demonstrating altered transactivation (<20% of wt, and/or reduced to levels similar to well established pathogenic variants such as R201Q or R166Q) AND data from a secondary assay demonstrating altered function. Not applicable if variant meets **PVS1**. If variant meets **PVS1_strong**, upgrade to **PVS1**. | 4 | Gene-specific, Strength |
| **Moderate (PS3_Moderate)** | Transactivation assays demonstrating altered transactivation (<20% of wt and/or reduced to levels similar to well established pathogenic variants such as R201Q or R166Q) OR ≥ 2 secondary assays demonstrating altered function. | 2 | Gene-specific, Strength |
| **Supporting (PS3_Supporting)** | Transactivation assays demonstrating enhanced transactivation (>115% of wt). | 1 | Gene-specific, Strength |

#### Approved Assay Instances

The VCEP names assay *types* (above) but distributes no list of approved assay instances, publications, or per-assay calibrations. Not specified by this VCEP.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance. Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications — MM-VCEP notes (verbatim):**

(1) There is currently no published *RUNX1* case control study. The criteria of a case control study can be added into the rules, if such a study will be published in the future. The original ACMG/AMP criterion states that in the absence of a published case-control study, the observation of the variant in multiple unrelated patients with the same phenotype and its absence in controls, may be used. The MM-VCEP created a "quasi-case-control study" with the estimated number of probands worldwide and the overall gnomAD population as control cohort. In order to apply this code, the proband has to meet the *RUNX1*-phenotypic criteria (see **PS2**) and the variant has to be either absent from gnomAD or only present once.

**RUNX1 Specification:**

| Strength | Criteria | Default point value | Modification type |
|----------|----------|---------------------|-------------------|
| **Strong (PS4)** | ≥ 4 probands meeting at least one of the *RUNX1*-phenotypic criteria (OR 127.1). | 4 | Disease-specific, Strength |
| **Moderate (PS4_Moderate)** | 2-3 probands meeting at least one of the *RUNX1*-phenotypic criteria (OR 63.5-95.3). | 2 | Disease-specific, Strength |
| **Supporting (PS4_Supporting)** | 1 proband meeting at least one of the *RUNX1*-phenotypic criteria (OR 31.8). | 1 | Disease-specific, Strength |

**Comparator note:** the proband thresholds are inclusive at the stated counts (≥ 4; 2-3; 1). The gnomAD gate is "absent from gnomAD or only present once" (i.e. allele count ≤ 1).

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications — MM-VCEP notes (verbatim):**

1. The Runt homology domain (RHD) has been established as highly conserved DNA binding domain without any benign variation in ClinVar. Thirteen somatic and/or germline mutational hotspots within the RHD have been identified: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204.
2. Variants in other parts of the RHD (amino acid (AA) 89-204) have been described as likely pathogenic/pathogenic before. There was additional evidence of germline pathogenic/likely pathogenic *RUNX2* variants affecting AA 89 and 94 (PMID 17290219), a gene with a Runt Homology Domain that has 90% sequence homology with *RUNX1*. AA 89 is also still part of the b-sheet of the CBF heterodimerization domain, which is functionally important. Thus, we prompt to establish PM1_supporting with reduced strength-level for these variants.
3. No reported germline *RUNX1* mutations in AA residues 77-88 of the RHD to date. If there is more evidence available, this region may be expanded in the future to other parts of the RHD or the protein.

**RUNX1 Specification:**

| Strength | Criteria | Default point value | Modification type |
|----------|----------|---------------------|-------------------|
| **Strong (PM1_strong)** | Variant affecting one of the following 13 AA residues within the RHD: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204. | 4 | Gene-specific, Strength |
| **Supporting (PM1_Supporting)** | Variant affecting one of the other AA residues 89-204 within the RHD. | 1 | Gene-specific, Strength |
| **Moderate** | Not specified by this VCEP (no PM1 tier at default moderate strength is listed). | — | — |

**Interaction caveat:** PM5 and PS1 cannot be used at any strength level if PM1 was applied (stated in the release notes and in the PM5 caveats).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications — MM-VCEP notes (verbatim):**

1. New gnomAD MAF threshold for PM2_supporting ≤ 0.00005 to account for larger population in gnomAD v4. The mean coverage of *RUNX1* in the population database used should be at least 20x.

**RUNX1 Specification:**

| Strength | Criteria | Default point value | Modification type |
|----------|----------|---------------------|-------------------|
| **Supporting (PM2_Supporting)** | Minor allele frequency **≤ 0.00005** with **at least 2000 alleles** tested around and **20x** coverage at the position. | 1 | Gene-specific, Strength |

**Caveat (verbatim):** \*We recommend evaluating PM2_supporting using the GrpMax FAF when it is available in gnomAD v4.1.0. If a GrpMax FAF value is not available, we recommend requiring that all subpopulations meet the PM2_supporting threshold.

**Comparator record:** MAF threshold is **inclusive** (≤ 0.00005). Allele-count and coverage gates are inclusive ("at least 2000 alleles", "20x coverage").

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**Status: NOT APPLICABLE.**

MM-VCEP notes: FPD/AML is inherited in an autosomal dominant manner, thus PM3 is not applicable.

No PM3 point system exists in this specification.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications — MM-VCEP notes (verbatim):**

1. The RHD has been established as highly conserved DNA binding domain without any benign variation in ClinVar. Thirteen somatic and/or germline mutational hotspots within the RHD have been identified: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204.
2. Variants in other parts of the RHD (AA 89-204) have been described as likely pathogenic/pathogenic before. There was additional evidence of germline pathogenic/likely pathogenic *RUNX2* variants affecting AA 89 and 94 (PMID 17290219), a gene with a Runt Homology Domain that has 90% sequence homology with *RUNX1*. AA 89 is also still part of the b-sheet of the CBF heterodimerization domain, which is functionally important. Thus, we prompt to establish PM4_supporting with reduced strength-level for these variants.
3. No reported germline *RUNX1* mutations in AA residues 77-88 of the RHD to date. If there is more evidence available, this region may be expanded in the future to other parts of the RHD or the protein.

**RUNX1 Specification:**

| Strength | Criteria | Default point value | Modification type |
|----------|----------|---------------------|-------------------|
| **Strong (PM4_strong)** | *In-frame/indel variants:* In-frame deletion/insertion impacting at least one of the following AA residues within the RHD: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204. *Stop loss variants:* **PM4** — Stop-loss variant causing a protein extension. | 4 | Gene-specific, Strength |
| **Moderate** | In-frame deletion/insertion impacting at least one of the following amino acid residues within the RHD: R107, K110, A134, R162, R166, S167, R169, G170, K194, T196, D198, R201, R204. | 2 | Gene-specific, Strength |
| **Supporting (PM4_Supporting)** | In-frame deletion/insertion impacting at least one of the other AA residues 89-204 within the RHD. | 1 | Gene-specific, Strength |

> **Internal inconsistency (flagged, not reconciled):** the **Strong** and **Moderate** rows carry the **same** 13-residue criterion text with different point values (4 vs 2). The "RUNX1 Specification" narrative lists only PM4_strong and PM4_Supporting for in-frame/indel variants, plus PM4 for stop-loss. The Moderate tier is present in the strength table but has no counterpart in the narrative. Both are transcribed as they appear.
>
> **Also flagged:** the stop-loss rule is written as bare "**PM4**" (nominal moderate strength for that code) but is listed inside the **Strong** block with a default point value of 4. The specification does not state which applies to stop-loss variants.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications — MM-VCEP notes (verbatim):**

1. RNA data or SpliceAI ≤ 0.20
2. The previously established pathogenic variant must be reviewed by the MM-VCEP and asserted pathogenic/likely pathogenic before this rule can be applied.
3. For missense variants, the Grantham score of the alternate residue of the new variant should be equal or higher to that of the alternate residue of the known pathogenic/likely pathogenic variant. [Grantham score table] (Grantham, 1974, PMID: 4843792)
4. There are at least two nonsense/frameshift variants that were curated as pathogenic in each exon (exons 3-7) without applying PM5_Supporting.

The Grantham matrix distributed with the specification is transcribed at [Appendix E](#appendix-e--grantham-score-table).

**RUNX1 Specification:**

| Strength | Criteria | Default point value | Modification type |
|----------|----------|---------------------|-------------------|
| **Strong (PM5_Strong)** | Missense change at an AA residue where ≥ 2 different missense changes which have been determined to be **pathogenic** before (after accounting for Grantham scores). | 4 | Strength |
| **Moderate (PM5)** | Missense change at an AA residue where a different missense change which has been determined to be **pathogenic** before (after accounting for Grantham scores). | 2 | Strength |
| **Supporting (PM5_Supporting)** | Missense change at an AA residue where a different missense change which has been determined to be **likely pathogenic** before (after accounting for Grantham scores). **PM5_Supporting** is also applied to nonsense/frameshift variants that are downstream of c.98 (in transcript NM_001754.4). | 1 | Strength |

**Caveats (verbatim, applied to all three tiers):**

\*Of note, the variant must not impact splicing based on RNA assay or SpliceAI ≤ 0.20.

\*The nonsense/frameshift variants before c.98 only affect one of the *RUNX1* functional transcript. PVS1 is also not **appliable** in this region based on the *RUNX1* PVS1 decision tree.

\*PM5 cannot be used if PM1 was applied at any strength level.

> **Source typo (flagged, preserved):** "appliable" appears in place of "applicable" in every occurrence of the second caveat (three times in the PDF). Transcribed verbatim.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications — MM-VCEP notes (verbatim):**

(1) FPD/AML phenotype is not highly specific and there is substantial genetic heterogeneity. We thus concluded that due to the lack of a highly specific phenotype and genetic heterogeneity, the maximum allowable value is 1 point contributing to the overall score.

(2) The phenotype of a deleterious RUNX1 mutation encompasses at least one of the three phenotypic criteria (see PS2).

(3) No family history is defined as the absence of the variant and any of the RUNX1-phenotypic criteria in first and second-degree relatives.

(4) The maximum allowable strength by combining PS2 and PM6 is to apply one moderate or two supporting rules (the maximum allowable value is still 1 point).

**RUNX1 Specification:**

Following the SVI guidance, assumed *de novo RUNX1* variants will be scored at the third tier of the point-based system with maximum allowable value of 1 point contributing to overall score:

| Strength | Criteria | Default point value | Modification type |
|----------|----------|---------------------|-------------------|
| **Moderate (PM6)** | ≥ 4 assumed *de novo* occurrences (without confirmation of maternity and paternity) in patients with FPD/AML phenotype. | 2 | Disease-specific, Strength |
| **Supporting (PM6_Supporting)** | 2 or 3 assumed *de novo* occurrences (without confirmation of maternity and paternity) in patients with FPD/AML phenotype. | 1 | Disease-specific, Strength |

> **Gap (flagged):** the specification gives no code for a **single** assumed *de novo* occurrence. Not specified by this VCEP.
>
> The SVI de novo points matrix itself is not reproduced by this VCEP; only the tier assignment ("third tier") and the 1-point cap are given. Consult the referenced ClinGen SVI guidance.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications — MM-VCEP notes (verbatim):**

1. The MM-VCEP adopted the approach being taken by other ClinGen-EPs and supported by the SVI and other work with additional meioses supporting higher evidence levels based on calculated LOD scores of 0.9, 1.5 and 2.1, respectively, with three or four meioses for **PP1**, five or six meioses for **PP1_moderate** and seven or more meioses for **PP1_strong**.
2. Affected individuals show at least one of the *RUNX1*-phenotypic criteria (see **PS2**).
3. Only genotype and phenotype positive individuals and obligate carriers are counted.
4. The MM-VCEP waived the ACMG/AMP recommendations for demonstrating co-segregation in more than one family given that many *RUNX1* variants are unique to families and do not occur in other unrelated families.

**RUNX1 Specification:**

| Strength | Criteria | LOD equivalent (per MM-VCEP note 1) | Default point value | Modification type |
|----------|----------|-------------------------------------|---------------------|-------------------|
| **Strong (PP1_Strong)** | **≥ 7** meioses observed within one or across multiple families. | 2.1 | 4 | Disease-specific, Strength |
| **Moderate (PP1_Moderate)** | **5 or 6** meioses observed within one or across multiple families. | 1.5 | 2 | Disease-specific, Strength |
| **Supporting (PP1)** | **3 or 4** meioses observed within one or across multiple families. | 0.9 | 1 | Disease-specific, Strength |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**Status: NOT APPLICABLE.**

MM-VCEP notes: The recommended cutoff for PP2 by the SVI is a missense constraint z score of ≥ 3.09 which was not met by RUNX1 (2.48 on ExAC and 2.08 on gnomAD). In addition, there are 9 benign/likely benign missense RUNX1 variants in ClinVar.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications — MM-VCEP notes (verbatim):**

1. For *in-silico* evaluation of missense variants, the MM-VCEP recommends using REVEL, a meta-predictor combining 13 individual tools with high sensitivity and specificity and that has recently demonstrated highest performance compared to any individual tool or other ensemble methods.
2. The threshold of REVEL is based on the evaluation of 25 germline PATH/LPATH and 25 BEN/LBEN missense variants in *RUNX1*. With the comparison of 11 different ensemble in-silico predictors (BayesDel AF, CADD, Condel, DANN, Eigen, FATHMM-MKL, MetaLR, MetaSVM, REVEL, UMD predictor, VEST) and their respective AUC, REVEL was found to be among the highest performing tools (AUC=1) and the new threshold for PP3 and BP4 was based on the REVEL scores at 90% sensitivity and 90% specificity, respectively.
3. We compared the performance of the new splice predictor SpliceAI and MES, which has been shown to be the highest performing tool pre-SpliceAI by using a test set of 202 variants in genes associated with inherited hematologic malignancies/AA/BMF or cytopenia. The thresholds for PP3 and BP4 were established based on the SpliceAI score at 90% sensitivity (PP3, ≥ 0.38) and 90% specificity (BP4, ≤ 0.20).
4. For some variant types that REVEL or SpliceAI scores are not available, multiple other predictors in agreements can be used in PP3.
5. **PP3** cannot be applied for canonical splice site variants.

> **Source note (flagged):** MM-VCEP note 2 lists 11 named predictors but says "11 different ensemble in-silico predictors" while naming BayesDel AF, CADD, Condel, DANN, Eigen, FATHMM-MKL, MetaLR, MetaSVM, REVEL, UMD predictor, VEST — that is 11 names, consistent.

**RUNX1 Specification:**

| Strength | Criteria | Default point value | Modification type |
|----------|----------|---------------------|-------------------|
| **Supporting (PP3)** | *Missense variants:* REVEL score **≥ 0.88** OR SpliceAI **≥ 0.38**, including the creation of cryptic novel splice sites. *Synonymous and intronic (intron 4-8) variants:* SpliceAI **≥ 0.38**, including the creation of cryptic novel splice sites. | 1 | Disease-specific, Gene-specific |

**Caveats (verbatim):**

\*Do not use for variants with a predicted splicing effect that is proven by RNA analysis. See **PVS1_Variable (RNA)**.

\*Do not use for for canonical splice site variants.

> **Source typo (flagged, preserved):** "Do not use **for for** canonical splice site variants" — duplicated word in the source. Transcribed verbatim.
>
> **Threshold discrepancy (flagged):** MM-VCEP note 2 says the REVEL threshold was set at 90% sensitivity; the operative PP3 threshold is REVEL ≥ 0.88. The specification does not restate the sensitivity-derived value elsewhere.

**Comparator record:** PP3 thresholds are **inclusive** (≥ 0.88 REVEL; ≥ 0.38 SpliceAI). Intronic applicability is limited to introns 4-8.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**Status: NOT APPLICABLE.**

MM-VCEP notes: The FPD/AML phenotype is rather unspecific and can be caused by a number of other inherited predisposition syndromes, somatic mutations or environmental factors that are insufficient to meet the original ACMG/AMP rule PP4.

No PP4 point system exists in this specification.

---

### PP5 - Reputable Source

**Status: NOT APPLICABLE.**

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PubMed: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications — MM-VCEP notes (verbatim):**

FPD/AML with germline *RUNX1* mutation is a rare disorder. The phenotype of carriers of a germline *RUNX1* mutation includes three criteria (mild to moderate thrombocytopenia, platelet ultrastructural and/or functional defects and diagnosis of a hematologic malignancy). Of these three criteria, thrombocytopenia is the most common feature. Most clinical laboratories establish their platelet count reference values by measuring samples from at least 120 healthy individuals and identifying the most outlying 5% of observed values. Most often, these outlying observations are split evenly between the ends of the test result distribution in the reference population, 2.5% at each end of the distribution, resulting in a two-sided reference interval. Using this approach, the prevalence of thrombocytopenia can be defined as 1 in 40 (lower 2.5%) in general population. The penetrance in families with *RUNX1* germline mutation is high to near-complete. We identified a family with a penetrance of 85% among known carriers of the mutation as the pedigree with the lowest penetrance to date. So far, no founder mutations in *RUNX1* have been reported, *de novo* variants are rare but have been described. The MM-VCEP modified **BA1** using extremely conservative values to account for the unknown prevalence and disease attribution to *RUNX1*. In order to obtain a *RUNX1*-specific population allele frequency for **BA1**, we utilized the Whiffin/Ware calculator (http://cardiodb.org/allelefrequencyapp/) with a prevalence of 1 in 40, a conservative unascertained penetrance estimate of 85%, an allelic heterogeneity of 100% and a maximum genetic heterogeneity of 10%. A 95% confidence interval was used to develop the threshold. The threshold developed for application of **BA1** as a stand-alone criterion is a minor allele frequency of equal to or higher than 0.0015 (0.15%).

The MM-VCEP also adopted the SVI recommendation that the variant be present in any general continental population dataset with a minimum number of 2,000 alleles and variant present in ≥ 5 alleles.

**RUNX1 Specification:**

| Strength | Criteria | Default point value | Modification type |
|----------|----------|---------------------|-------------------|
| **Stand Alone (BA1)** | Minor allele frequency **≥ 0.0015 (0.15%)** in any general continental population dataset with **≥ 2,000 alleles** tested and variant present in **≥ 5 alleles**. | Not Applicable | Disease-specific |

**Comparator record:** all three BA1 gates are **inclusive** (≥ 0.0015; ≥ 2,000 alleles tested; ≥ 5 alleles observed).

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications — MM-VCEP notes (verbatim):**

Similarly, for the **BS1** calculation, we utilized the Whiffin/Ware calculator (http://cardiodb.org/allelefrequencyapp/) with a prevalence of 1 in 40, a conservative unascertained penetrance estimate of 85%, an allelic heterogeneity of 100% and a maximum genetic heterogeneity of 1% (one magnitude lower than for **BA1**). A 95% confidence interval was used to develop the threshold. We developed a range for application of **BS1** for variants with a minor allele frequency between 0.00015 (0.015%) and 0.0015 (0.15%).

1. The MM-VCEP also adopted the SVI recommendation that the variant be present in any general continental population dataset with a minimum number of 2,000 alleles and variant present in ≥ 5 alleles.
2. The variant can be classified as likely benign based on **BS1** alone if there is no contradictory evidence supporting pathogenicity.

**RUNX1 Specification:**

| Strength | Criteria | Default point value | Modification type |
|----------|----------|---------------------|-------------------|
| **Strong (BS1)** | Minor allele frequency **between 0.00015 (0.015%) and 0.0015 (0.15%)** in any general continental population dataset with **≥ 2,000 alleles** tested and variant present in **≥ 5 alleles**. | -4 | Disease-specific |

**Comparator record (flagged):** the BS1 range is written as "between 0.00015 and 0.0015" with **no explicit comparators** — the specification does not state whether either endpoint is inclusive. The upper endpoint 0.0015 is the same value at which BA1 is explicitly inclusive (≥ 0.0015), so a MAF of exactly 0.0015 falls in both rules as written. Not specified by this VCEP; not reconciled here. The allele-count gates are inclusive (≥ 2,000; ≥ 5).

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**Status: NOT APPLICABLE.**

MM-VCEP notes: BS2 is not applicable since FPD/AML patients display incomplete penetrance and the average age of onset of hematologic malignancies is 33 years.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications — MM-VCEP notes:** identical to the PS3 notes (transactivation assays and secondary assays; see [PS3](#ps3---functional-studies)).

**RUNX1 Specification:**

| Strength | Criteria | Default point value | Modification type |
|----------|----------|---------------------|-------------------|
| **Strong (BS3)** | Transactivation assays demonstrating normal transactivation (**80-115% of wt**) AND data from a secondary assay demonstrating normal function. | -4 | Gene-specific, Strength |
| **Supporting (BS3_Supporting)** | Transactivation assays demonstrating normal transactivation (**80-115% of wt**). | -1 | Gene-specific, Strength |

**Comparator record (flagged):** "80-115% of wt" is written without comparators. Read against PS3 (<20% of wt for altered; >115% of wt for enhanced), the range 20%-80% of wt is not covered by any BS3 or PS3 rule. The specification does not address this gap; not filled here.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications — MM-VCEP notes:** This code should only be applied for genotype-negative, phenotype-positive family members.

| Strength | Criteria | Default point value | Modification type |
|----------|----------|---------------------|-------------------|
| **Strong (BS4)** | Applicable when observed in **≥ 2** informative meioses. | -4 | General recommendation |

**Comparator record:** inclusive (≥ 2).

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | **Not Applicable** | MM-VCEP notes: BP1 is not applicable for RUNX1, because both truncating and missense variants cause FPD/AML. |
| **BP2** | **Specified — Supporting (-1 point; modification type: None)** | Applied per original ACMG/AMP wording: "Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern." MM-VCEP notes: BP2 is applicable per the original ACMG/AMP guidelines. *In vivo*, mice lacking Runx1 die during mid-embryonic development. Biallelic pathogenic variants in *RUNX1* have never been reported in FPD/AML patients. A variant *in trans* with a known pathogenic variant or observation of the variant in the homozygous state in individuals without FPD/AML phenotype can be considered supporting benign evidence. |
| **BP3** | **Not Applicable** | MM-VCEP notes: RUNX1 does not contain a repetitive region without known function. BP3 is therefore deemed not applicable. |
| **BP4** | **Specified — Supporting (-1 point; Disease-specific, Gene-specific)** | *Missense variants:* **REVEL score < 0.50 AND SpliceAI ≤ 0.20**. *Synonymous and Intronic variants:* **SpliceAI ≤ 0.20**. MM-VCEP notes are identical to the PP3 notes 1-3 (REVEL/SpliceAI calibration). |
| **BP5** | **Not Applicable** | BP5 is not applicable. In rare circumstances, a patient can carry two pathogenic variants in genes predisposing to hematologic malignancies. |
| **BP6** | **Not Applicable** | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PubMed: 29543229). |
| **BP7** | **Specified — Supporting (-1 point; Disease-specific, Gene-specific)** | See full text below. |

**Comparator record for BP4:** REVEL gate is **strict** (< 0.50); SpliceAI gate is **inclusive** (≤ 0.20). Note that REVEL values in the interval [0.50, 0.88) fall between BP4 and PP3 and trigger neither.

#### BP7 - full specification

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

**MM-VCEP notes (verbatim):**

1. Conservation is no longer a requirement for BP7 based on its limited predicted power and recommendations from the ClinGen SVI Splicing Subgroup (Cheung et al., 2019, 30503770; Walker et al., 2023, PMID: 37352859).
2. Splicing effects are currently based solely on predictions. The rules can be modified in the future if RNA evidence becomes available using Walker et al., 2023, PMID: 37352859 as a guide; modification of strength should be based on the quality of the RNA study where:
   1. Comparison to a control is necessary
   2. Patient RNA is better than minigene assays
   3. Primers are designed to capture the possibility of multi-exonic/multi-cassette events
   4. NMD inhibitors (e.g., puromycin, proprietary molecule found in PAXgene tubes), particularly when the predicted effect is nonsense-mediated decay, are used
   5. Quantification of the effect by SNP analysis is better than PSI (percent splicing index) analysis is better than capillary electrophoresis is better than estimation by gel band density
   6. Multiple studies are better than a single study

\* Caution should be used in modifying strength when the effect of the splicing impact is incomplete ("leaky" splice site) or unclear.

**RUNX1 Specification:**

**BP7:** Applicable for
- Synonymous variants – excluding those in the last 3 nucleotides preceding a canonical donor splice site or the first nucleotide following a canonical acceptor splice site – with SpliceAI Δ scores **≤ 0.20**.
- Intronic variants with SpliceAI Δ scores **≤ 0.20**.

**BP7_Variable (RNA):**
- Applicable for variants with RNA data, with weighting based on the quality of the available RNA data.

> **Gap (flagged):** BP7_Variable (RNA) states that weighting depends on RNA data quality but gives no weighting scale. Not specified by this VCEP; the referenced external guidance is Walker et al., 2023 (PMID: 37352859).

**Comparator record:** SpliceAI Δ gate is **inclusive** (≤ 0.20).

---

## Rules for Combining Criteria

The specification declares its framework **Type** as "Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015" and distributes the following point-range table.

### Point Based Variant Classification Categories (verbatim from the specification)

| Category | Point Ranges |
|----------|--------------|
| Pathogenic | 10 |
| Likely Pathogenic | 6 - 9 |
| Uncertain Significance | 0 - 5 |
| Likely Benign | -6 - -1 |
| Benign | -7 |

**Additional Notes:** *(the specification's "Additional Notes" field for this table is empty)*

> **Comparator record (flagged):** the Pathogenic and Benign rows show a **single value** ("10", "-7") with no comparator. In the Tavtigian framework these are conventionally open-ended (≥ 10 and ≤ -7), but the specification does not write the comparator. Transcribed as printed; not inferred.

### Default point values assigned by this VCEP

Collected from the per-criterion "Default Point Value" fields in the specification. This is the VCEP's own points-to-code mapping; there is **no** separate points-to-strength ladder in this specification.

| Code | Points | Code | Points |
|------|--------|------|--------|
| PVS1 | 8 | PP1_Strong | 4 |
| PVS1_Strong | 4 | PP1_Moderate | 2 |
| PVS1_Moderate | 2 | PP1 | 1 |
| PS1 | 4 | PP3 | 1 |
| PS1_Moderate | 2 | BA1 | Not Applicable (stand alone) |
| PS2_Moderate | 2 | BS1 | -4 |
| PS2_Supporting | 1 | BS3 | -4 |
| PS3 | 4 | BS3_Supporting | -1 |
| PS3_Moderate | 2 | BS4 | -4 |
| PS3_Supporting | 1 | BP2 | -1 |
| PS4 | 4 | BP4 | -1 |
| PS4_Moderate | 2 | BP7 | -1 |
| PS4_Supporting | 1 | BP7_Variable (RNA) | -1 |
| PM1_strong | 4 | PM4_strong | 4 |
| PM1_Supporting | 1 | PM4 (moderate tier) | 2 |
| PM2_Supporting | 1 | PM4_Supporting | 1 |
| PM5_Strong | 4 | PM6 | 2 |
| PM5 | 2 | PM6_Supporting | 1 |
| PM5_Supporting | 1 | | |

### Caps and interaction rules stated by the VCEP

- **PS2 + PM6 combined:** maximum allowable strength is one moderate **or** two supporting rules; the maximum allowable value is 1 point. (Stated in both PS2 and PM6 notes.)
- **PM1 exclusivity:** if PM1 is applied at any strength level, **PM5 and PS1 cannot be used at any level**.
- **PS3 / PVS1 interaction:** PS3 (Strong) is not applicable if the variant meets PVS1; if the variant meets PVS1_strong, upgrade to PVS1.
- **PP3 / PVS1_Variable interaction:** do not use PP3 for variants with a predicted splicing effect proven by RNA analysis.
- **PP3 / canonical splice sites:** PP3 cannot be applied for canonical splice site variants.
- **BS1 standalone:** a variant can be classified as likely benign based on BS1 alone if there is no contradictory evidence supporting pathogenicity.

No other rules for combining criteria appear in this specification or its supplementary files.

---

## Appendices

All five appendices below are direct transcriptions of files distributed with GN008. Appendix F is a lookup dataset.

### Appendix A — RUNX1 PVS1 decision tree for SNVs

Source file: `RUNX1 PVS1 decision tree for SNVs.png` (transcribed in full).

**Root:** RUNX1 (NM_001754.4), Nonsense or Frameshift

```
RUNX1 (NM_001754.4) Nonsense or Frameshift
├── Predicted to undergo NMD
│   ├── Exon is absent from RUNX1 isoform a and b
│   │     └── c.1–c.97  ────────────────────────────────►  NA
│   └── Exon is present in all biologically relevant transcripts
│         └── Nonsense:        c.98–c.916
│             Frameshift (−1): c.98–c.758
│             Frameshift (+1): c.98–c.779   ─────────────►  PVS1
└── Not predicted to undergo NMD
      └── Truncated/altered region is critical to protein function
            └── Nonsense:        c.917–c.1440
                Frameshift (−1): c.759–c.1440
                Frameshift (+1): c.780–c.1440  ──────────►  PVS1_Strong
```

| Branch | Condition | Coordinate range (NM_001754.4) | Outcome |
|--------|-----------|-------------------------------|---------|
| Predicted to undergo NMD → exon absent from RUNX1 isoform a and b | — | c.1–c.97 | **NA** |
| Predicted to undergo NMD → exon present in all biologically relevant transcripts | Nonsense | c.98–c.916 | **PVS1** |
| Predicted to undergo NMD → exon present in all biologically relevant transcripts | Frameshift (−1) | c.98–c.758 | **PVS1** |
| Predicted to undergo NMD → exon present in all biologically relevant transcripts | Frameshift (+1) | c.98–c.779 | **PVS1** |
| Not predicted to undergo NMD → truncated/altered region is critical to protein function | Nonsense | c.917–c.1440 | **PVS1_Strong** |
| Not predicted to undergo NMD → truncated/altered region is critical to protein function | Frameshift (−1) | c.759–c.1440 | **PVS1_Strong** |
| Not predicted to undergo NMD → truncated/altered region is critical to protein function | Frameshift (+1) | c.780–c.1440 | **PVS1_Strong** |

> **Apparent VCEP inconsistency (flagged):** the PVS1 narrative states that "deletions of exon 1-3, presumably only affecting RUNX1 isoform c, meet **PVS1_moderate**", but this SNV tree assigns **NA** to the corresponding c.1–c.97 region, and the CNV tree (Appendix B) contains no exon 1-3 branch producing PVS1_Moderate. The PM5 caveats reinforce the tree ("PVS1 is also not appliable in this region based on the RUNX1 PVS1 decision tree"). The specification does not reconcile the narrative with the trees.
>
> Also note the tree does **not** cover splice, initiation-codon, or in-frame variant classes; canonical splice site variants are routed to Appendix C instead.

### Appendix B — RUNX1 PVS1 decision tree for CNVs

Source file: `RUNX1 PVS1 decision tree for CNVs.png` (transcribed in full).

**Root:** RUNX1 (NC_000021.9) single or multi-exon deletion

```
RUNX1 (NC_000021.9) single or multi-exon deletion
├── Full gene deletion ─────────────────────────────► Pathogenic Classification
├── Disrupts reading frame ─────────────────────────► Follow the same predictions under
│                                                      the RUNX1 PVS1 decision tree for SNVs
└── Preserves reading frame or impact on reading frame is unknown
      ├── Truncated/altered region is critical to protein function*  ──► PVS1_Strong
      └── Role of region in protein function is unknown
            └── LOF variants in this exon are not frequent in population
                and exon is present in biologically relevant transcript
                  └── Variant removes <10% of protein#  ─────────────► PVS1_Moderate
```

| Branch | Outcome |
|--------|---------|
| Full gene deletion | **Pathogenic Classification** |
| Disrupts reading frame | Follow the same predictions under the RUNX1 PVS1 decision tree for SNVs |
| Preserves reading frame / impact unknown → Truncated/altered region is critical to protein function\* | **PVS1_Strong** |
| Preserves reading frame / impact unknown → Role of region in protein function is unknown → LOF variants in this exon are not frequent in population and exon is present in biologically relevant transcript → Variant removes <10% of protein# | **PVS1_Moderate** |

> **Unresolved footnotes (flagged):** the CNV tree carries footnote markers **\*** (on "Truncated/altered region is critical to protein function") and **#** (on "Variant removes <10% of protein"). **No footnote text is present** anywhere in the image or in the specification PDF. The meaning of these markers is not specified by this VCEP.
>
> **Note also:** the "Full gene deletion" branch outputs a **classification** ("Pathogenic Classification"), not a PVS1 strength code — this is the only terminal node in either tree that does so. Transcribed as drawn.
>
> **Comparator record:** the protein-removal gate is **strict** (<10% of protein).

### Appendix C — Summary of splicing effects (canonical splice site variants)

Source file: `Summary of splicing effects.png` (transcribed in full). Covers GT-AG ±1,2 canonical splice sites of introns 2-8. Coordinates are given as the exonic/intronic boundary position in NM_001754.4 notation as printed.

| Intron | GT-AG 1,2 Splice site | Location | Predicted or published effects | Classification |
|--------|----------------------|----------|-------------------------------|----------------|
| Intron 2 | Donor | c.58 | Only affect isoform c, but not isoform a and b | **N/A** |
| Intron 2 | Acceptor | c.59 | Only affect isoform c, but not isoform a and b | **N/A** |
| Intron 3 | Donor | c.97 | Only affect isoform c, but not isoform a and b | **N/A** |
| Intron 3 | Acceptor | c.98 | Only affect isoform c, but not isoform a and b | **N/A** |
| Intron 3 | Acceptor | c.98 | If Skip Exon 4 with frameshift on isoform c AND cause nonsense/frameshift on isoform a/b | **PVS1** |
| Intron 4 | Donor | c.351 | Skip Exon 4 with frameshift | **PVS1** |
| Intron 4 | Acceptor | c.352 | Skip Exon 5 with frameshift OR Use of Cryptic splice acceptor with a frameshift, PMID: 10508512. | **PVS1** |
| Intron 5 | Donor | c.508 | Skip Exon 5 with frameshift OR Use of Cryptic splice donor with a frameshift, PMID: 11830488. | **PVS1** |
| Intron 5 | Acceptor | c.509 | Skip Exon 6 with In frame Δ171-205 and G170 (GGG->GGA), deletion in RHD. | **PVS1_Strong** |
| Intron 6 | Donor | c.613 | Skip Exon 6 with In frame Δ171-205 and G170 (GGG->GGA), deletion in RHD. | **PVS1_Strong** |
| Intron 6 | Acceptor | c.614 | Skip Exon 7 with In frame Δ206-269 and R205N (AGG->AAT), remove 13% of protein. | **PVS1_Strong** |
| Intron 7 | Donor | c.805 | Skip Exon 7 with In frame Δ206-269 and R205N (AGG->AAT), remove 13% of protein. | **PVS1_Strong** |
| Intron 7 | Acceptor | c.806 | Skip Exon 8 with In frame Δ270-323 and D269A (GAT->GCG), deletion in TAD. | **PVS1_Strong** |
| Intron 8 | Donor | c.967 | Skip Exon 8 with In frame Δ270-323 and D269A (GAT->GCG), deletion in TAD. | **PVS1_Strong** |
| Intron 8 | Acceptor | c.968 | Likely use of cryptic site, the last exon contains 33% of protein. | **PVS1_Strong** |

> **Notes on this table (flagged):**
> - The c.98 acceptor appears **twice** with different outcomes (N/A and PVS1) depending on the isoform a/b consequence. This is as drawn, not a transcription error.
> - Intron 5 rows: the **donor** at c.508 and the **acceptor** at c.509 are both listed, but the acceptor row's effect text ("Skip Exon 6…") is grouped under the Intron 5 label while the same effect text recurs for the Intron 6 donor at c.613. Similarly for introns 6/7 and 7/8. The pairing convention (donor of intron N and acceptor of intron N−1 sharing a predicted skip event) is not explained in the source.
> - No footnote or legend accompanies the image beyond the header row.
> - Introns 1 and 9 (if any) are not covered.

### Appendix D — PS1 splicing application (SVI Table 2)

Source file: `PS1 splicing application.jpg` (transcribed in full). Header as printed: *"Table 2. PS1 code weights for variants with same predicted splicing event as a known (likely) pathogenic variant"*.

| Variant under assessment (VUA) | Baseline computational/predictive code applicable to VUA | Position of comparison variant relative to VUA | PS1 code — with P comparison variant | PS1 code — with LP comparison variant |
|---|---|---|---|---|
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | same nucleotide | PS1 | PS1_Moderate |
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | within same splice donor/acceptor motif (including at ±1,2 positions) | PS1_Moderate | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | within same splice donor/acceptor ±1,2 dinucleotide | PS1_Supporting | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | within same splice donor/acceptor region, but outside ±1,2 dinucleotide<sup>a</sup> | PS1_Supporting | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate or PVS1_Supporting | within same splice donor/acceptor ±1,2 dinucleotide | PS1 | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate or PVS1_Supporting | within same splice donor/acceptor motif, but outside ±1,2 dinucleotide<sup>a</sup> | PS1_Moderate | PS1_Supporting |

**Table footnotes (verbatim):**

> Prerequisite for all: the predicted event of the VUA must precisely match the predicted event of the comparison (likely) pathogenic variant (e.g., both predicted to lead to exon skipping, or both to lead to enhanced use of a cryptic splice motif, AND the strength of the prediction for the VUA must be of similar or higher strength than the strength of the prediction for the comparison [likely] pathogenic variant). For an exonic variant, predicted or proven functional effect of missense substitution(s) encoded by the VUA and (likely) pathogenic variant should also be considered before application of this code. Dinucleotide positions refer to donor and acceptor dinucleotides in reference transcript(s) used for curation. Designated donor and acceptor motif ranges should be based on position weight matrices for intron category (see methods). For GT-AG introns these are defined as follows: the donor motif, last 3 bases of the exon and 6 nucleotides of intronic sequence adjacent to the exon; acceptor motif, first base of the exon and 20 nucleotides upstream from the exon boundary. Consider other motif ranges for non-GT-AG introns.
>
> <sup>a</sup>If relevant, splicing assay data for a pathogenic variant outside a ±1,2 dinucleotide position may be used to update a PVS1 decision tree and hence the applicable PVS1 code for a ±1,2 dinucleotide variant.

> **Note:** This is a reproduction of the ClinGen SVI Splicing Subgroup table (Walker et al., 2023, PMID: 37352859), distributed by the MM-VCEP as its PS1_Variable reference. The MM-VCEP adds no RUNX1-specific modification to it.

### Appendix E — Grantham score table

Source file: `Grantham score table.png` (transcribed in full). This is Table 2 of Grantham R., *Science* 1974;185(4154):862-864 (PMID: 4843792), distributed unmodified. Used by PM5 note 3: the Grantham score of the alternate residue of the new variant must be **equal or higher** than that of the alternate residue of the known pathogenic/likely pathogenic variant.

Half-matrix as printed (columns left to right; row label at right in the source):

| Row \ Col | Arg | Leu | Pro | Thr | Ala | Val | Gly | Ile | Phe | Tyr | Cys | His | Gln | Asn | Lys | Asp | Glu | Met | Trp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Ser** | 110 | 145 | 74 | 58 | 99 | 124 | 56 | 142 | 155 | 144 | 112 | 89 | 68 | 46 | 121 | 65 | 80 | 135 | 177 |
| **Arg** | | 102 | 103 | 71 | 112 | 96 | 125 | 97 | 97 | 77 | 180 | 29 | 43 | 86 | 26 | 96 | 54 | 91 | 101 |
| **Leu** | | | 98 | 92 | 96 | 32 | 138 | 5 | 22 | 36 | 198 | 99 | 113 | 153 | 107 | 172 | 138 | 15 | 61 |
| **Pro** | | | | 38 | 27 | 68 | 42 | 95 | 114 | 110 | 169 | 77 | 76 | 91 | 103 | 108 | 93 | 87 | 147 |
| **Thr** | | | | | 58 | 69 | 59 | 89 | 103 | 92 | 149 | 47 | 42 | 65 | 78 | 85 | 65 | 81 | 128 |
| **Ala** | | | | | | 64 | 60 | 94 | 113 | 112 | 195 | 86 | 91 | 111 | 106 | 126 | 107 | 84 | 148 |
| **Val** | | | | | | | 109 | 29 | 50 | 55 | 192 | 84 | 96 | 133 | 97 | 152 | 121 | 21 | 88 |
| **Gly** | | | | | | | | 135 | 153 | 147 | 159 | 98 | 87 | 80 | 127 | 94 | 98 | 127 | 184 |
| **Ile** | | | | | | | | | 21 | 33 | 198 | 94 | 109 | 149 | 102 | 168 | 134 | 10 | 61 |
| **Phe** | | | | | | | | | | 22 | 205 | 100 | 116 | 158 | 102 | 177 | 140 | 28 | 40 |
| **Tyr** | | | | | | | | | | | 194 | 83 | 99 | 143 | 85 | 160 | 122 | 36 | 37 |
| **Cys** | | | | | | | | | | | | 174 | 154 | 139 | 202 | 154 | 170 | 196 | 215 |
| **His** | | | | | | | | | | | | | 24 | 68 | 32 | 81 | 40 | 87 | 115 |
| **Gln** | | | | | | | | | | | | | | 46 | 53 | 61 | 29 | 101 | 130 |
| **Asn** | | | | | | | | | | | | | | | 94 | 23 | 42 | 142 | 174 |
| **Lys** | | | | | | | | | | | | | | | | 101 | 56 | 95 | 110 |
| **Asp** | | | | | | | | | | | | | | | | | 45 | 160 | 181 |
| **Glu** | | | | | | | | | | | | | | | | | | 126 | 152 |
| **Met** | | | | | | | | | | | | | | | | | | | 67 |

The matrix is symmetric: read Grantham(X,Y) from whichever of the two cells is populated.

**Caption printed beneath the matrix (verbatim):**

> Table 2. Difference D for each amino acid pair (10). The mean chemical distance from the three-property formula (see text) D̄<sub>epn</sub> = 100 (D<sub>ij</sub> values have been multiplied by 50.723 to make this mean possible). Linear regression of RSF and log RSF on these D values gives correlation coefficients of −.66 and −.72, respectively. Previous difference indexes give correlation coefficients against RSF of −.34 (minimum base changes), −.42 (Sneath difference), and −.49 (Epstein formula). In each case, correlation is between the two sets (difference and RSF) of 190 values (3, 4, 7).

### Appendix F — MM-VCEP RUNX1 Pilot Results (lookup dataset)

Source file: `MM-VCEP RUNX1 Pilot Results.xlsx`, single worksheet named **Results**. Opened and read in full with openpyxl.

**Structure — 9 populated columns:**

| # | Column header |
|---|---------------|
| 1 | Variant Information |
| 2 | ClinVar ID |
| 3 | CA ID (if needed) |
| 4 | ClinVar classification |
| 5 | ClinVar Star Level |
| 6 | Curator 1 |
| 7 | Curator 2 |
| 8 | MM-VCEP Classification |
| 9 | Codes applied by MM-VCEP |

**Contents:** 20 variant rows (the sheet is padded to row 970 with empty rows; columns 10-25 are entirely empty). This is a **pilot validation lookup**: it records how the MM-VCEP applied its own rules to 20 pre-selected variants during specification piloting. It is **not** a classification lookup for general use, and it defines no rule, threshold, or code weight. Because the dataset is small it is reproduced in full below; nothing here overrides the criteria above.

**MM-VCEP classification distribution:** VUS 8, Likely Pathogenic 4, Pathogenic 3, Likely Benign 3, Benign 2.

| Variant | ClinVar ID / CA ID | ClinVar classification | Stars | Curator 1 | Curator 2 | MM-VCEP | Codes applied by MM-VCEP |
|---|---|---|---|---|---|---|---|
| NM_001754.5(RUNX1):c.1441T>G (p.Ter481Gly) | 3336849 | Uncertain significance | 3 stars | VUS | VUS | VUS | PM2_supporting, PS4_supporting, PM4 |
| NM_001754.5(RUNX1):c.484A>G (p.Arg162Gly) | 376022 | Pathogenic | 3 stars | Pathogenic | Pathogenic | Pathogenic | PM2_supporting, PP3, PM1_strong, PS3_moderate, PS4_supporting, PP1 |
| NM_001754.5(RUNX1):c.485G>A (p.Arg162Lys) | 376021 | Likely Pathogenic | 3 stars | Likely Pathogenic | Likely Pathogenic | Likely Pathogenic | PM2_supporting, PP3, PM1_strong, PS4_moderate, PP1 |
| NM_001754.5(RUNX1):c.582A>C (p.Lys194Asn) | 561250 | Likely Pathogenic | 3 stars | Likely Pathogenic | Likely Pathogenic | Likely Pathogenic | PM2_supporting, PM1_strong, PP1, PS4_supporting |
| NM_001754.5(RUNX1):c.581_586del (p.Lys194_Ile195del) | 570999 | Uncertain significance | 3 stars | VUS | VUS | VUS | PM2_supporting, PM4_strong |
| NM_001754.5(RUNX1):c.592G>A (p.Asp198Asn) | 3340076 | Likely Pathogenic | 3 stars | Likely Pathogenic | Likely Pathogenic | Likely Pathogenic | PM2_supporting, PP3, PM1_strong, PS4_supporting |
| NM_001754.5(RUNX1):c.596G>C (p.Gly199Ala) | 2029256 | Uncertain significance | 3 stars | VUS | VUS | VUS | PM2_supporting, PP3, PM1_supporting |
| NM_001754.5(RUNX1):c.314A>C (p.His105Pro) | 561233 | Likely Pathogenic | 3 stars | VUS | VUS | VUS | PM2_supporting, PP3, PM1_supporting, PS4_supporting |
| NM_001754.5(RUNX1):c.466G>A (p.Ala156Thr) | 2091067 | Uncertain significance | 1 star | VUS | VUS | VUS | PM2_supporting, PP3, PM1_supporting |
| NM_001754.5(RUNX1):c.1308C>T (p.Ser436=) | 1592483 | Uncertain significance | 3 stars | Likely Benign | Likely Benign | Likely Benign | PM2_supporting, BP4, BP7 |
| NM_001754.5(RUNX1):c.891C>T (p.His297=) | 1114376 | Uncertain significance | 3 stars | Likely Benign | Likely Benign | Likely Benign | BP4, BP7 |
| NM_001754.5(RUNX1):c.969G>A (p.Thr323=) | 646645 | Likely benign | 1 star | VUS | VUS | VUS | None |
| NM_001754.5(RUNX1):c.510G>T (p.Gly170=) | 835308 | Likely benign | 3 stars | Likely Benign | Likely Benign | Likely Benign | PM2_supporting, BP4, BP7 |
| NM_001754.5(RUNX1):c.508+4C>T | 1465512 | Likely benign | 1 star | VUS | VUS | VUS | BP4 |
| NM_001754.5(RUNX1):c.351+5T>C | 463992 | Likely benign | 3 stars | VUS | VUS | VUS | PM2_supporting, BP4 |
| NM_001754.5(RUNX1):c.968-2A>G | CA410148836 | *(blank)* | *(blank)* | Pathogenic | Pathogenic | Pathogenic | PM2_supporting, PVS1_strong, PS1 |
| NM_001754.5(RUNX1):c.351+1G>C | 409822 | Uncertain significance | 3 stars | Pathogenic | Pathogenic | Pathogenic | PVS1, PM2_supporting, PS1 |
| NM_001754.5(RUNX1):c.292del (p.Leu98SerfsTer24) | 561231 | `Pathogenic ` *(trailing space in source)* | 3 stars | Likely Pathogenic | Likely Pathogenic | Likely Pathogenic | PM2_supporting, PM5_supporting, PVS1 |
| NM_001754.5(RUNX1):c.*484T>C | 339864 | Benign | 3 stars | Benign | Benign | Benign | BA1, BP2 |
| NM_001754.5(RUNX1):c.1338C>T (p.Leu446=) | 561227 | Benign | 3 stars | Benign | Benign | Benign | `BS1. BP4, BP7, BP2` *(period in place of comma, verbatim)* |

> **Discrepancies in this file (flagged, not corrected):**
> - Every variant is written against transcript **NM_001754.5**, while the specification designates **NM_001754.4** as the RUNX1 transcript.
> - Row `c.968-2A>G` has no ClinVar ID and no ClinVar classification/star level; a Concept/Canonical Allele ID (CA410148836) is given instead.
> - Row `c.292del` ClinVar classification cell contains a trailing space (`"Pathogenic "`).
> - Row `c.1338C>T` codes field uses a period instead of a comma: `BS1. BP4, BP7, BP2`.
> - Row `c.969G>A` has MM-VCEP classification VUS with the codes field literally reading `None`.
> - The file gives no column for total points, so the point arithmetic behind each MM-VCEP call cannot be checked from this file alone.

---

## References (verbatim from the specification)

1. Walker LC, Hoya M, Wiggins GAR, et al. Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing: Recommendations from the ClinGen SVI Splicing Subgroup. *Am J Hum Genet.* 2023;110(7):1046-1067. doi:10.1016/j.ajhg.2023.06.002
2. Matheny CJ, Speck ME, Cushing PR, et al. Disease mutations in RUNX1 and RUNX2 create nonfunctional, dominant-negative, or hypomorphic alleles. *EMBO J.* 2007;26(4):1163-1175. doi:10.1038/sj.emboj.7601568
3. Grantham R. Amino acid difference formula to help explain protein evolution. *Science.* 1974;185(4154):862-864. doi:10.1126/science.185.4154.862
4. Tavtigian SV, Harrison SM, Boucher KM, Biesecker LG. Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines. *Hum Mutat.* 2020;41(10):1734-1737. doi:10.1002/humu.24088
5. Walker LC Hoya M et al. Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing: Recommendations from the ClinGen SVI Splicing Subgroup. *Am J Hum Genet* (2023) 110 (7) p. 1046-1067. 10.1016/j.ajhg.2023.06.002 · PMID 37352859
6. Matheny CJ Speck ME et al. Disease mutations in RUNX1 and RUNX2 create nonfunctional, dominant-negative, or hypomorphic alleles. *EMBO J* (2007) 26 (4) p. 1163-75. 10.1038/sj.emboj.7601568 · PMID 17290219
7. Grantham R. Amino acid difference formula to help explain protein evolution. *Science* (1974) 185 (4154) p. 862-4. 10.1126/science.185.4154.862 · PMID 4843792
8. Walker LC Hoya M et al. Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing: Recommendations from the ClinGen SVI Splicing Subgroup. *Am J Hum Genet* (2023) 110 (7) p. 1046-1067. 10.1016/j.ajhg.2023.06.002 · PMID 37352859
9. Walker LC Hoya M et al. Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing: Recommendations from the ClinGen SVI Splicing Subgroup. *Am J Hum Genet* (2023) 110 (7) p. 1046-1067. 10.1016/j.ajhg.2023.06.002 · PMID 37352859

> **Flagged:** the reference list contains duplicates — entries 1, 5, 8 and 9 are the same Walker et al. 2023 paper; entries 2 and 6 are the same Matheny et al. paper; entries 3 and 7 are the same Grantham paper. Transcribed as printed.

Additional PMIDs cited in the body but not in the reference list: 30503770 (Cheung et al., 2019, cited under BP7), 29543229 (SVI VCEP Review Committee, cited under PP5/BP6), 10508512 and 11830488 (cited in the Summary of splicing effects table), 17290219 (cited under PM1/PM4, also reference 6).

---

## Version History

| Version | Released | Notes |
|---------|----------|-------|
| 3.1 | 2/13/2026 | Current version. Release notes reproduced at the top of this document. |
| Earlier versions | — | Not distributed with the GN008 v3.1 package; version history prior to 3.1 is not specified in these source files. |

---

## Source File Inventory

| File | Type | Status |
|------|------|--------|
| `ClinGen_ACMG_Specifications_RUNX1_v3.1.pdf` | PDF, 18 pages | Read in full |
| `MM-VCEP RUNX1 Pilot Results.xlsx` | Excel, 1 sheet "Results" | Read in full (openpyxl); Appendix F |
| `RUNX1 PVS1 decision tree for SNVs.png` | Image | Transcribed in full; Appendix A |
| `RUNX1 PVS1 decision tree for CNVs.png` | Image | Transcribed in full; Appendix B |
| `Summary of splicing effects.png` | Image | Transcribed in full; Appendix C |
| `PS1 splicing application.jpg` | Image | Transcribed in full; Appendix D |
| `Grantham score table.png` | Image | Transcribed in full; Appendix E |
| `GN008_data.json` | Download metadata | Not source material (ignored per skill instructions) |

No source file failed to open. No source content was inferred, reconstructed, or supplied from outside these files.

---

*This document was compiled from the ClinGen VCEP specification GN008 (RUNX1 v3.1) and its distributed supplementary files. For the most current version, please refer to the ClinGen website.*
