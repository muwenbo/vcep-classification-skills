# Comprehensive Variant Interpretation Guidelines for CTLA4

## ClinGen Antibody Deficiencies VCEP Specifications for CTLA4 (Version 2.0)

**Affiliation:** Antibody Deficiencies Variant Curation Expert Panel (Antibody Deficiencies VCEP)
**Version:** 2.0
**Release Date:** 7/31/2026
**DOI:** 10.5281/zenodo.21723733
**Specification Type:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015
**Release Notes (verbatim):** "This submission includes updates to the PVS1, PM5, PS4, PP3, BP4, BP7, and PS3 codes."

---

## Table of Contents

1. [Gene and Disease Information](#1-gene-and-disease-information)
2. [Pathogenic Criteria](#2-pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PS4 - Prevalence in Affected](#ps4---prevalence-in-affected)
   - [PM1 - Mutational Hot Spot](#pm1---mutational-hot-spot)
   - [PM2 - Absent from Controls](#pm2---absent-from-controls)
   - [PM4 - Protein Length Changes](#pm4---protein-length-changes)
   - [PM5 - Novel Missense at Same Residue](#pm5---novel-missense-at-same-residue)
   - [PM6 - De Novo (Assumed)](#pm6---de-novo-assumed)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
   - [PP4 - Phenotype Specificity](#pp4---phenotype-specificity)
3. [Benign Criteria](#3-benign-criteria)
   - [BA1 - Stand-Alone Benign](#ba1---stand-alone-benign)
   - [BS1 - Allele Frequency Greater Than Expected](#bs1---allele-frequency-greater-than-expected)
   - [BS3 - Functional Studies (Benign)](#bs3---functional-studies-benign)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP4 - Computational Evidence (Benign)](#bp4---computational-evidence-benign)
   - [BP5 - Alternate Molecular Basis](#bp5---alternate-molecular-basis)
   - [BP7 - Synonymous/Intronic Variants](#bp7---synonymousintronic-variants)
4. [Not Applicable Criteria](#4-not-applicable-criteria)
5. [Rules for Combining Criteria](#5-rules-for-combining-criteria)
6. [Appendices](#6-appendices)

---

## 1. Gene and Disease Information

| Parameter | Value |
|-----------|-------|
| **Gene** | CTLA4 (HGNC:2505) |
| **HGNC Name** | cytotoxic T-lymphocyte associated protein 4 |
| **Reference Transcript** | NM_005214.5 |
| **Disease** | autoimmune lymphoproliferative syndrome due to CTLA4 haploinsuffiency* |
| **MONDO ID** | MONDO:0014493 |
| **Mode of Inheritance** | Autosomal dominant inheritance |
| **Penetrance** | Incomplete (45-70%, per VCEP) |

\*The disease name is reproduced verbatim from the specification, including the source spelling "haploinsuffiency".

### CTLA4 Domain Structure and Exon Organization

Source: "CTL4 Domains and Exons" supplementary figure (PMID: 25741868, PMID: 31298041). Protein length 223 aa; exons 1-4.

| Residues | Feature |
|----------|---------|
| 1-35 | Leader peptide |
| 36-151 | Ligand binding domain (extracellular) |
| 134-139 | MYPPPY motif (required for interaction with ligands CD80 and CD86) |
| 162-182 | Transmembrane domain |
| 187-223 | Cytoplasmic tail (regulates localization and internalization) |

Additional gene notes cited by the VCEP:
- Exon 3 is isoform-specific; it is omitted from an alternative transcript (NM_001037631.3) that encodes the soluble isoform (PMID: 40168991). Similar clinical phenotypes are associated with null variants in exon 3 and exon 2 (PMID: 25329329, PMID: 34111452).
- The transmembrane domain is necessary for CTLA4 localization to the cell surface and is the main topological feature present in the critical membrane-bound form of CTLA4 but absent from the soluble form, which does not have the same ability to prevent the disease state (PMID: 25213377).

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specification:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP caveats:**
- Use caution interpreting LOF variants at the extreme 3' end of the gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact

#### Strength Levels

| Strength | Points | Application |
|----------|--------|-------------|
| **PVS1** (Very Strong) | 8 | See Very Strong bullets below |
| **PVS1_Strong** | 4 | Truncating variants between codons 183 and 201, which are not predicted to trigger nonsense-mediated decay or to disrupt the transmembrane domain but result in C-terminal truncation of more than 10% of the protein product |
| **PVS1_Moderate** | 2 | See Moderate bullets below |
| **PVS1_Supporting** | Not specified by VCEP | Not specified by VCEP |

##### Very Strong (PVS1, default)

- For truncating variants that introduce a premature stop between codons 2 and 172, which is predicted to trigger nonsense-mediated decay, apply PVS1 at the default (very strong) level. While this recommendation already matches ClinGen guidance (PMID: 30192042), it should be mentioned that this includes truncating variants located in the isoform-specific exon 3, because similar clinical phenotypes are associated with null variants in exon 3 and exon 2 (PMID: 25329329, PMID: 34111452), despite the fact that exon 3 is omitted from an alternative transcript (NM_001037631.3) that encodes the soluble isoform (PMID: 40168991).
- For truncating variants between codons 173 and 182, which encode part of the transmembrane domain, apply PVS1 at the default (very strong) level. The transmembrane domain spans amino acids 162-182, is necessary for CTLA4 localization to the cell surface, and is the main topological feature present in the critical membrane-bound form of CTLA4 but absent from the soluble form of CTLA4 that does not have the same ability to prevent the disease state (PMID: 25213377).
- If a missense, synonymous, or intronic variant outside of the canonical splice sites has a SpliceAI score greater than or equal to 0.2 and has been confirmed to cause complete or near-complete disruption of splicing within the mRNA in a study of patient RNA or minigene assay, avoid PP3 and PS3_Supporting and evaluate PVS1 instead (PMID: 37352859).
- In order to avoid over-weighing loss-of-function evidence, PP3 and PS3 are mutually exclusive with PVS1 at the default (very strong) level. These additional codes cannot be applied for a variant that has already met PVS1.

##### Moderate (PVS1_Moderate)

- Apply PVS1_Moderate for nonsense or frameshift variants between codons 202 and 223 of CTLA4, as these are predicted not to undergo nonsense-mediated decay and to result in C-terminal truncation of less than 10% of the protein product.
- Apply PVS1_Moderate for initiation codon variants, as there are no known alternative start codons and the closest potential in-frame start codon is at codon 38. There is at least one report of an initiation codon variant that leads to CTLA4 phenotypes and though there is no direct experimental evidence of loss of expression, the authors assert that there is a proximally located N-terminal nonsense variant (34 aa away) that results in no protein product, making it unlikely that there is alternative start codon usage (PMID: 25329329).

**Modification type:** Clarification (all strength levels).

The full PVS1 decision tree is transcribed in [Appendix A](#appendix-a-pvs1-decision-tree-for-ctla4).

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specification:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

#### Strong (PS1) — 4 points

- Use PS1 for missense variants when other variant was classified pathogenic by VCEP standards without using PS1.
- Beware of changes that impact splicing rather than the amino acid (based on RNA data or splicing predictors). Splicing predictions (by SpliceAI) should remain the same for WT and both mutant alleles.
- Use at the default (PS1) level for splicing variants in combination with **PP3** if located **outside** the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 and have a comparable nucleotide variant **at the same position** that has been classified **pathogenic** by VCEP standards (PMID: 37352859).
- Use at the default (PS1) level for splicing variants in combination with **PVS1** if located **within** the splice donor/acceptor +/-1,2 dinucleotide positions with a comparable variant **within the same splice donor/acceptor +/-1,2 dinucleotide** that has been classified **pathogenic** by VCEP standards (PMID: 37352859).

#### Moderate (PS1_Moderate) — 2 points

- Use PS1_Moderate for missense variants when the other variant was classified likely pathogenic by VCEP standards without using PS1.
- Beware of changes that impact splicing rather than the amino acid (based on RNA data or splicing predictors). Splicing predictions (by SpliceAI) should remain the same for WT and both mutant alleles.
- Use at the PS1_Moderate level for splicing variants in combination with **PP3** if located **outside** the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 with a comparable nucleotide variant **at the same position** that has been classified **likely pathogenic** by VCEP standards (PMID: 37352859).
- Use at the PS1_Moderate level for splicing variants in combination with **PP3** if located **outside** the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 and with a comparable variant **within the same splice region** that has been classified **pathogenic** by VCEP standards (PMID: 37352859).
- Use at the PS1_Moderate level for splicing variants in combination with **PVS1 (at reduced strength)** if located **within** the splice donor/acceptor +/-1,2 dinucleotide positions with a comparable variant **within the same splice donor/acceptor motif (but outside the +/-1,2 dinucleotide)** that has been classified **pathogenic** by VCEP standards (PMID: 37352859).

#### Supporting (PS1_Supporting) — 1 point

- Use at the PS1_Supporting level for splicing variants in combination with **PP3** if located **outside** the splice donor/acceptor +/-1,2 dinucleotide positions that have a splice AI score ≥0.2 with a comparable nucleotide variant **within the same motif** that has been classified likely pathogenic by VCEP standards (PMID: 37352859).
- Use at the PS1_Supporting level in combination with **PVS1** for splicing variants **within** splice donor/acceptor +/-1,2 dinucleotide positions with a variant at the **same nucleotide position** or **within the same donor/acceptor +/-1,2 dinucleotide** with the same predicted impact that has been classified **pathogenic** by VCEP standards (PMID: 37352859).
- Use at the PS1_Supporting level in combination with **PVS1** for splicing variants **within** splice donor/acceptor +/-1,2 dinucleotide positions with a variant **within the same splice region, but outside the donor/acceptor +/-1,2 dinucleotide**, with the same predicted impact that has been classified **pathogenic or likely pathogenic** by VCEP standards (PMID: 37352859).
- Use at the PS1_Supporting level in combination with **PVS1 (at reduced strength)** for splicing variants **within** splice donor/acceptor +/-1,2 dinucleotide positions with a variant **within the same splice region, but outside the donor/acceptor +/-1,2 dinucleotide**, with the same predicted impact that has been classified **likely pathogenic** by VCEP standards (PMID: 37352859).

**Modification type:** Clarification (all strength levels).

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specification:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### Selecting the Phenotypic Consistency Row

The following rule is stated identically for the Very Strong (8 points), Strong (4 points), Moderate (2 points), and Supporting (1 point) levels of PS2 (and for PM6):

> The "phenotypic consistency" used on the SVI point-counting table below will be chosen for each proband by the number of phenotype points scored by the proband on the PS4 scoring system:
> - (A) If the proband scores greater than or equal to 4 and <6 phenotype points in the PS4 counting rubric, use the number of *de novo* points corresponding to "Phenotype consistent with gene but not highly specific and high genetic heterogeneity".
> - (B) If the proband scores 6 or more phenotype points in the PS4 counting rubric AND is not known to harbor biallelic *LRBA* variants, use the number of *de novo* points corresponding to "Phenotype consistent with gene but not highly specific".
> - (C) If the proband scores 10 or more phenotype points in the PS4 counting rubric AND is not known to harbor biallelic *LRBA* variants, use the number of *de novo* points corresponding to "Phenotype highly specific for gene".

**Modification type:** Disease-specific.

#### Points Awarded per De Novo Occurrence (PS2/PM6 Table 1)

| Phenotypic consistency | Confirmed de novo | Assumed de novo |
|------------------------|-------------------|-----------------|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity* | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

\*Maximum allowable value of 1 may contribute to overall score

#### Determining Evidence Strength (PS2/PM6 Table 2)

| Total Points | Evidence Strength |
|--------------|-------------------|
| 0.5 | Supporting (PS2_Supporting or PM6_Supporting) |
| 1 | Moderate (PS2_Moderate or PM6) |
| 2 | Strong (PS2 or PM6_Strong) |
| 4 | Very Strong (PS2_VeryStrong) |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specification:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

| Strength | Points | Criteria |
|----------|--------|----------|
| **PS3** (Strong) | 4 | A calculated OddsPath >18.7 is needed to upgrade any assay result showing abnormal CTLA4 function to PS3 (as recommended in PMID: 31892348). |
| **PS3_Moderate** | 2 | A minimum of 11 total P/LP and B/LB variant controls (classified using these same specifications) are needed to upgrade any assay result showing abnormal CTLA4 function to PS3_Moderate (as recommended in PMID: 31892348). |
| **PS3_Supporting** | 1 | An abnormal functional result by a *CTLA4* variant in non-patient cells in an approved assay should be applied at PS3_Supporting strength. Further details on how to interpret the assays can be found in the associated manuscript. |

**Modification type:** Gene-specific (Strong, Moderate); Disease-specific (Supporting).

#### Approved Assay Instances (in vitro, non-patient cells) for PS3_Supporting

| # | Assay class | Example PMIDs |
|---|-------------|---------------|
| 1 | Transendocytosis OR soluble CD80 and/or CD86 ligand endocytosis | 25329329, 25632005, 25367873, 27102614, 29375547, 15814706, 20870175 |
| 2 | *In vitro* T Cell Suppression | 29375547, 26478010, 25213377 |
| 3 | CTLA4 Endocytosis and Recycling | 15814706 |
| 4 | Cell surface and/or intracellular CTLA4 expression | 25367873, 14578884, 29375547, 7559643, 25213377 |

Expanded information about all published functional studies in non-patient cells (PS3/BS3) or patient cells (PS4/PP4) assessed by the VCEP can be found in the attached file entitled CTLA4_Functional Assay_Research_PS3_BS3. See [Appendix C](#appendix-c-functional-assay-curation-summary) for the per-publication approval status recorded in that file.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specification:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

| Strength | Points | Proband count required |
|----------|--------|------------------------|
| **PS4** (Strong) | 4 | Observation of the variant in at least 4 independent probands |
| **PS4_Moderate** | 2 | Observation of the variant in 2-3 independent probands |
| **PS4_Supporting** | 1 | 1 observation of the variant in a proband |

**Modification type:** Disease-specific, Strength.

#### Requirements (all strength levels)

- In order to be evaluated for this criterion, the variant must not meet BS1 or BA1. *(Stated in the Strong section.)*
- A proband would be excluded for this criterion if found to harbor homozygous or compound heterozygous *LRBA* variants that are either rare VUS or have been classified Likely Pathogenic or Pathogenic. *(Stated in the Strong section.)*
- The probands used for PS4 cannot include the same proband used for PP4.
- In order to be counted for this criterion, a proband must meet one of the following two requirements:
  - To have reported phenotypes that score a minimum of 6 phenotype points, as well as genotyping of the *LRBA* locus to confirm the absence of biallelic variants in *LRBA* that have been classified either Likely Pathogenic or Pathogenic. Note: a monoallelic *LRBA* variant can be tolerated.
  - **OR**
  - To have reported phenotypes that score a minimum of 10 phenotype points, in the absence of genotyping of the *LRBA* locus.

#### Phenotype Point System

The phenotype point rubric (also used by PS2/PM6, PP1, PP4 and BS4) contains a total of two 4-point criteria, one 3-point criterion, five 2-point criteria, and twelve 1-point criteria.

**Clinical criteria**

| Points | Finding |
|--------|---------|
| 4 | Sinopulmonary findings |
| 4 | Non-infectious gastrointestinal or hepatobiliary disease |
| 2 | Immune-mediated cytopenias |
| 2 | Nonmalignant Lymphoproliferation |
| 2 | Severe, persistent, recurrent viral infections including skin warts |
| 1 | Immune-mediated skin and hair findings |
| 1 | Endocrinopathy |
| 1 | Severe, persistent, recurrent, atypical, opportunistic bacterial, Mycobacterial or fungal infections |
| 1 | Neurological findings |
| 1 | Inflammatory findings (arthritis, vasculitis, recurrent fevers) |
| 1 | Lymphoma |

**Clinical immunophenotypic data**

| Points | Finding |
|--------|---------|
| 2 | Hypogammaglobulinemia |
| 1 | Lymphopenia |
| 1 | Abnormal TBNK levels |
| 1 | Presence of autoantibodies |
| 1 | Defective antigen-specific immune responses |
| 1 | Histopathology findings of lymphocytic / granulomatous tissue infiltration |

**Patient cell-based assay data**

| Points | Finding |
|--------|---------|
| 3 | Transendocytosis / Soluble CD80/CD86 ligand endocytosis (reduced) |
| 2 | *Ex vivo* T cell suppression (reduced) |
| 1 | Cell surface and/or intracellular CTLA4 expression (reduced) |

A more detailed form of this rubric, listing qualifying findings and phenotypes, is given in the attached "CTLA4 Phenotype Scoring Table" and is transcribed in [Appendix B](#appendix-b-ctla4-phenotype-scoring-table-qualifying-findings).

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specification:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation.

| Strength | Points | Criteria |
|----------|--------|----------|
| **PM1** (Moderate) | 2 | Met by variants in the MYPPPY domain (residues 134-139), which is required for interaction with CD80 and CD86. Not mutually exclusive with PM5. |

**Modification type:** Clarification.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification:** Absent from controls (or at extremely low frequency).

| Strength | Points | Threshold |
|----------|--------|-----------|
| **PM2_Supporting** (Supporting level only) | 1 | Met for total allele frequency lower than **1.43 x 10⁻⁷ (0.000000143)** across all populations in gnomAD v4.1.0 |

**Threshold rationale:** Based on the experts' estimate of CTLA-4 insufficiency prevalence of 1/200,000 - 1/1,000,000 people and 45-70% penetrance. The lower end of the prevalence estimate (1 in 1,000,000) and the higher end of the penetrance estimate (70%) were used for this calculation. Allelic heterogeneity of 1 and genetic heterogeneity of 1 were also assumed for the calculation.

**Modification type:** Disease-specific, Strength.

---

### PM3 - In Trans with Pathogenic Variant

**Status:** **Not Applicable.** VCEP comment: "Not applicable, as this code is specific to recessive disorders."

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specification:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Points | Criteria |
|----------|--------|----------|
| **PM4** (Moderate) | 2 | See bullets below |
| **PM4_Supporting** | Not specified by VCEP | Not specified by VCEP |

- This code is mutually exclusive with PVS1 (PMID: 30192042) and PP3 (in order not to double-count *in silico* predictor data) but can be used together with PM1.
- Met at default strength (PM4) by an in-frame deletion resulting in a protein length change greater than or equal to 2 amino acids, if at least one of the deleted nucleotides is highly conserved (PhyloP score greater than or equal to 2.0) and if SpliceAI score is <0.2.
- Met at default strength (PM4) by an in-frame insertion resulting in a protein length change greater than or equal to 2 amino acids, if at least one of the adjacent amino acids is highly conserved (PhyloP score greater than or equal to 2.0) and if SpliceAI score is <0.2.
- The region of the protein affected by the variant is key to consider. If variants within this region occur in healthy populations, the region is polymorphic. Incomplete penetrance should also be considered as a caveat for polymorphism.

**Modification type:** Disease-specific, Strength.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specification:** Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

| Strength | Points | Criteria |
|----------|--------|----------|
| **PM5** (Moderate) | 2 | See bullets below |

- Do not apply for any variant that meets BS1 or BA1.
- Not mutually exclusive with PM1.
- Comparison variant must have a Pathogenic or Likely Pathogenic classification reached using these VCEP-specified rules without using PM5.
- The variant of interest must have an equal or higher Grantham score than the Pathogenic / Likely Pathogenic comparison variant (https://en.wikipedia.org/wiki/Amino_acid_replacement#Grantham's_distance).
- SpliceAI must be used to examine both variants for lack of effect on splicing (SpliceAI Δ score <0.2).

**Modification type:** Clarification.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specification:** *De novo* in a patient with the disease and no family history. For PM6, maternity and paternity are not confirmed but assumed, with no family history of the disease.

| Strength | Points |
|----------|--------|
| **PM6_Strong** | 4 |
| **PM6** (Moderate) | 2 |
| **PM6_Supporting** | 1 |

The same phenotypic-consistency selection rule (A/B/C, based on PS4 phenotype points) and the same PS2/PM6 point tables apply — see [PS2](#ps2---de-novo-confirmed). Use the "Assumed de novo" column of Table 1.

**Modification type:** Disease-specific.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specification:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

| Strength | Points | Meioses required |
|----------|--------|------------------|
| **PP1_Strong** | 4 | Co-segregation of the variant with the affected phenotype across at least 4 meioses in one family or combined across multiple unrelated families |
| **PP1_Moderate** | 2 | Co-segregation of the variant with the affected phenotype across at least two meioses in one family or combined across multiple unrelated families |
| **PP1** (Supporting) | 1 | Co-segregation of the variant with the affected phenotype across at least one meiosis (i.e. the variant is present in the proband + an affected relative) |

**Requirements (all strength levels):**
- Due to incomplete penetrance (45-70%), PP1 will require each family member to reach at least 6 points in the PS4 counting rubric in order to be considered affected for the purpose of counting co-segregations.
- PP1 should not be applied when a variant also has population data meeting BA1 or BS1 since a common variant may appear to segregate with the disease by chance.

**Modification type:** Disease-specific, Strength.

**Note:** No LOD-score table is specified by this VCEP; strength is set by meiosis count as tabulated above.

---

### PP2 - Missense in Constrained Gene

**Status:** **Not Applicable.** VCEP comment: "Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease Not applicable, as analysis of the evolutionary constraint of CTLA4 (low missense Z-score) shows that some missense variation is tolerated (benign)."

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**VCEP Specification:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc).

| Strength | Points | Criteria |
|----------|--------|----------|
| **PP3** (Supporting) | 1 | Met at the default (PP3) level by a missense variant with **REVEL score ≥ 0.644 AND CADD PHRED score ≥ 25.3** (PMID: 36413997). Also met by missense, synonymous, or intronic variants outside the +/-1,2 dinucleotide positions that are predicted as damaging using **SpliceAI (cutoff Δ score ≥ 0.2)**. |

**Rationale (verbatim):** The above requirement for agreement between two *in silico* tools was reached following a pilot study of suspected pathogenic and suspected benign variants (assembled from ClinVar submissions and published assertions of pathogenicity). Some suspected pathogenic *CTLA4* variants fall in REVEL's benign range while some suspected benign *CTLA4* variants fall in CADD's pathogenic range. All false positive and false negative predictions in the test set could be avoided by requiring that both tools agree in order for PP3 or BP4 to be Met.

**Modification type:** Disease-specific.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specification:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

| Strength | Points | Criteria |
|----------|--------|----------|
| **PP4_Moderate** | 2 | Proband must score at least 10 phenotype points in the PS4 counting rubric **AND** have been genotyped using a method able to detect *LRBA* variants without biallelic variants found **AND** have experimental data from the patient's cells showing a functional defect in the CTLA4 pathway such as defective transendocytosis or soluble ligand endocytosis, defective Treg suppression of T cell proliferation, or reduced surface or whole cell *CTLA4* expression. |
| **PP4** (Supporting) | 1 | Proband must score at least 10 phenotype points in the PS4 counting rubric **AND** have been genotyped using a method able to detect *LRBA* variants without biallelic variants found. |

**Additional requirements (both levels):**
- This proband cannot be used for the PS4 code.
- In order to be evaluated for this criterion, the variant must not meet BS1 or BA1.

**Patient cell-based assays approved for application of PP4_Moderate:**

1. Transendocytosis or soluble ligand endocytosis (i.e. PMID: 25329329, PMID: 34111452, PMID: 28159733)
2. Treg-mediated suppression of T cell proliferation (i.e. PMID: 25213377)
3. Cell surface and/or intracellular CTLA4 expression (i.e. PMID: 25213377, PMID: 25329329, PMID: 34111452, PMID: 28159733)

**Modification type:** Gene-specific (Moderate); Disease-specific (Supporting).

**Note:** The phenotype scoring table footnote states: "Avoid applying points from patient cell-based assay data to PP4, which already incorporates these data as rationale for an upgrade from PP4 to PP4_Moderate."

---

### PP5 - Reputable Source

**Status:** **Not Applicable.** "This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229)."

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

| Strength | Points | Threshold |
|----------|--------|-----------|
| **BA1** (Stand Alone) | Not Applicable | Met for GrpMax Filtering Allele Frequency **greater than or equal to 1.11 x 10⁻⁵ (0.0000111)** in gnomAD, with **at least 5 alleles total** across all populations in gnomAD (gnomAD v4.1.0) |

**Threshold rationale:** Based on the experts' estimate of CTLA-4 insufficiency prevalence of 1/200,000 - 1/1,000,000 people and 45-70% penetrance. A higher prevalence estimate (1 in 100,000) and the lower end of the penetrance estimate (45%) were used for this calculation. Allelic heterogeneity of 1 and genetic heterogeneity of 1 were also assumed for the calculation.

**Modification type:** Disease-specific.

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification:** Allele frequency is greater than expected for disorder.

| Strength | Points | Threshold |
|----------|--------|-----------|
| **BS1** (Strong) | -4 | Met for GrpMax Filtering Allele Frequency **greater than or equal to 1.11 x 10⁻⁶ (0.00000111)** in gnomAD, with **at least 3 alleles total** across all populations in gnomAD (gnomAD v4.1.0) |

- If GrpMax filtering allele frequency is not listed for the variant, this code is evaluated in relation to the maximum allele frequency among the five major continental populations (African / African-American, East Asian, European non-Finnish, Latino / Admixed-American, or South Asian), but requires **at least 3 alleles total** across all populations in gnomAD (gnomAD v4.1.0) to be met.
- **Threshold rationale:** Based on the experts' estimate of CTLA-4 insufficiency prevalence of 1/200,000 - 1/1,000,000 people and 45-70% penetrance. An intermediate prevalence estimate (1 in 500,000) and the lower end of the penetrance estimate (45%) were used for this calculation. Allelic heterogeneity of 1 and genetic heterogeneity of 0.5 were also assumed for the calculation.

**Modification type:** Disease-specific.

---

### BS2 - Observed in Healthy Adult

**Status:** **Not Applicable.** VCEP comment: "Not applicable due to incomplete penetrance."

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specification:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

| Strength | Points | Criteria |
|----------|--------|----------|
| **BS3** (Strong) | -4 | A calculated OddsPath < 0.053 is needed to upgrade any assay result showing normal CTLA4 function to BS3 (as recommended in PMID: 31892348). |
| **BS3_Moderate** | -2 | A minimum of 11 total P/LP and B/LB variant controls (classified using these same specifications) are needed to upgrade any assay result showing normal CTLA4 function to BS3_Moderate (as recommended in PMID: 31892348). |
| **BS3_Supporting** | -1 | A normal result for a *CTLA4* variant using one of the approved assays below cannot be interpreted to mean normal CTLA4 function by itself. BS3_Supporting can only be applied when a second different assay also shows a normal result. |

**Approved in vitro assays in non-patient cells for BS3_Supporting** (although suspected benign variants are not present in all of the PMIDs below):

1. Transendocytosis OR soluble CD80 and/or CD86 ligand endocytosis (i.e. PMID: 25329329, PMID: 25632005, PMID: 25367873, PMID: 27102614, PMID: 29375547, PMID: 15814706, PMID: 20870175)
2. *In vitro* T Cell Suppression (i.e. PMID: 29375547, PMID: 26478010, PMID: 25213377)
3. CTLA4 Endocytosis and Recycling (i.e. PMID: 15814706)
4. Cell surface and/or intracellular CTLA4 expression (i.e. PMID: 25367873, PMID: 14578884, PMID: 29375547, PMID: 7559643, PMID: 25213377)

**Modification type:** Gene-specific (Strong, Moderate); Disease-specific (Supporting).

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specification:** Lack of segregation in affected members of a family.

| Strength | Points | Criteria |
|----------|--------|----------|
| **BS4** (Strong) | -4 | Lack of segregation should be identified in more than 1 affected family member. Due to incomplete penetrance (45-70%), BS4 will require each family member to reach at least 6 points in the PS4 counting rubric in order to be considered affected for the purpose of counting lack of segregation. |
| **BS4_Supporting** | -1 | If only 1 affected family member lacks segregation of the genotype, downgrade to BS4_Supporting. Due to incomplete penetrance (45-70%), BS4_Supporting will require each family member to reach at least 6 points in the PS4 counting rubric in order to be considered affected for the purpose of counting lack of segregation. |

**Modification type:** Disease-specific, Strength.

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc).

**VCEP Specification:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc.).

| Strength | Points | Criteria |
|----------|--------|----------|
| **BP4** (Supporting) | -1 | Met at the default (BP4) level by a missense variant with **REVEL ≤ 0.290, CADD PHRED score ≤ 22.7, and SpliceAI Δ score < 0.1** (PMID: 36413997). Also applicable to both synonymous variants and all intronic variants outside the +/-1,2 dinucleotide positions not predicted to impact splicing by SpliceAI (SpliceAI Δ score <0.1, PMID: 37352859). |

**Rationale:** Same two-tool agreement pilot rationale as PP3 (see above).

**Modification type:** Disease-specific.

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

**VCEP Specification:** Variant found in a case with an alternate molecular basis for disease.

| Strength | Points | Criteria |
|----------|--------|----------|
| **BP5** (Supporting) | -1 | Two such cases are required to mitigate the VCEP's concern over relying on other groups' classifications of pathogenic variants in genes such as *LRBA*. |

**Modification type:** Disease-specific.

---

### BP7 - Synonymous/Intronic Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

**VCEP Specification:** A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

| Strength | Points | Criteria |
|----------|--------|----------|
| **BP7_Strong** (RNA) | -4 | BP7_Strong (RNA) is met by variants with experimental evidence of no impact on splicing (PMID: 3735285). |
| **BP7** (Supporting) | -1 | Apply only if BP4 is met. Applicable to both synonymous variants and intronic variants not predicted to impact splicing by SpliceAI (SpliceAI Δ score <0.1, PMID: 37352859). Only applicable for intronic/non-coding variants located outside the donor/acceptor splice region (conservatively designated as intronic variants at or beyond positions +7/−21) or for synonymous exonic variants located outside of the first nucleotide or the last 3 nucleotides of the exon (PMID: 37352859). |

**Modification type:** Strength (BP7_Strong); Clarification (BP7).

---

## 4. Not Applicable Criteria

| Criterion | Reason given by the VCEP |
|-----------|--------------------------|
| **PM3** | Not applicable, as this code is specific to recessive disorders. |
| **PP2** | Not applicable, as analysis of the evolutionary constraint of CTLA4 (low missense Z-score) shows that some missense variation is tolerated (benign). |
| **PP5** | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BS2** | Not applicable due to incomplete penetrance. |
| **BP1** | Not applicable, as pathogenic CTLA4 variants are not limited to truncating variants, but can be missense as well. |
| **BP2** | Do not use this criterion. BP2 would be more applicable to a very large, polymorphic gene, while it's rarely going to come up for a short gene like CTLA4. Also, while biallelic cases have not yet been found, they exist for other IEI genes. |
| **BP3** | Not applicable, as repetitive regions of unknown function are not known within CTLA4. The most relevant known variant, NM_005214.5(CTLA4):c.110_118del, may be better evaluated as a potential splice variant (splice acceptor loss and splice acceptor gain). |
| **BP6** | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |

---

## 5. Rules for Combining Criteria

This VCEP uses a **point-based (Bayesian) classification system**. The Antibody Deficiencies VCEP adopted the Bayesian points scale for all criteria combinations (PMID: 29300386), including in scenarios where a variant has met a combination of pro-pathogenic and pro-benign evidence codes. The point scale and classification categories come from Tables 2 and 3 of PMID: 32720330.

### Point Values for ACMG/AMP Strength of Evidence Categories

| Evidence Strength | Pathogenic | Benign |
|-------------------|-----------|--------|
| Indeterminate | 0 | 0 |
| Supporting | 1 | -1 |
| Moderate | 2 | -2 |
| Strong | 4 | -4 |
| Very Strong | 8 | -8 |

### Point Based Variant Classification Categories

| Category | Point Range |
|----------|-------------|
| **Pathogenic** | ≥ 10 |
| **Likely Pathogenic** | 6 - 9 |
| **Uncertain Significance** | 0 - 5 |
| **Likely Benign** | -1 to -6 |
| **Benign** | ≤ -7 |

*(The spec registry page renders these ranges as "10", "6 - 9", "0 - 5", "-6 - -1" and "-7"; the attached "Points system to reach final classification" document reproduces Table 3 of PMID: 32720330 with the inequalities ≥10 and ≤ -7.)*

---

## 6. Appendices

### Appendix A: PVS1 Decision Tree for CTLA4

Transcribed from the attached "PVS1 Decision Tree for CTLA4" figure.

#### Nonsense or Frameshift

| Condition | Outcome |
|-----------|---------|
| Predicted to undergo NMD (PTC between codons 2 and 172) + exon present in biologically-relevant transcript (NM_005214.5) | **PVS1** |
| Predicted to undergo NMD + exon absent from biologically-relevant transcript (NM_005214.5) | N/A |
| Not predicted to undergo NMD (PTC between codons 173 and 223) + truncated/altered region critical to protein function (including truncating variants between codons 173 to 182 that encode part of the transmembrane domain) | **PVS1** |
| Not predicted to undergo NMD + role of region unknown (truncating variants between codons 183 and 223) + LoF variants in this exon are frequent in the general population and/or exon absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD + role unknown + LoF variants not frequent and exon present in biologically-relevant transcript(s) + variant removes >10% of protein | **PVS1_Strong** |
| Not predicted to undergo NMD + role unknown + LoF variants not frequent and exon present in biologically-relevant transcript(s) + variant removes <10% of protein | **PVS1_Moderate** |

#### Deletion (single exon to full gene)

| Condition | Outcome |
|-----------|---------|
| Full gene deletion | **PVS1** |
| Single to multi exon deletion - disrupts reading frame and predicted to undergo NMD + exon present in biologically-relevant transcript (NM_005214.5), including variants that delete exon 1, which would disrupt frame and be predicted to trigger NMD | **PVS1** |
| Same + exon absent from biologically-relevant transcript (NM_005214.5) | N/A |
| Single to multi exon deletion - disrupts reading frame and **NOT** predicted to undergo NMD (including single exon 3 deletion) + truncated/altered region critical to protein function | **PVS1_Strong** |
| Same + role of region unknown + LoF variants frequent in general population and/or exon absent from biologically-relevant transcript(s) | N/A |
| Same + role unknown + LoF variants not frequent and exon present in biologically-relevant transcript(s) + variant removes >10% of protein | **PVS1_Strong** |
| Same + role unknown + LoF variants not frequent and exon present + variant removes <10% of protein | N/A |
| Single to multi exon deletion - preserves reading frame (including single exon deletion of in-frame exon 2 or 4) + truncated/altered region critical to protein function (including variants that cause deletion of exon 2, which contains codons 134-139 encoding the MYPPPY motif) | **PVS1_Strong** |

#### Duplication (≥1 exon in size, must be completely contained within gene)

| Condition | Outcome |
|-----------|---------|
| Proven in tandem + reading frame disrupted and NMD predicted to occur | **PVS1** |
| Proven or presumed in tandem + no or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem + reading frame presumed disrupted and NMD predicted to occur | **PVS1_Strong** |
| Proven not in tandem | N/A |

#### Initiation Codon (no alternative start codons known in *CTLA4* at this time)

| Condition | Outcome |
|-----------|---------|
| No known alternative start codon in other transcripts + ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon | **PVS1_Moderate** |
| Different functional transcript uses alternative start codon | N/A |

#### Splicing Prediction Data Only

**Located outside donor/acceptor +/-1,2 dinucleotide positions (exonic or intronic)** — use splicing tool prediction (for missense/in-frame indel variants, also consider relevant predictions of protein impact):

| Condition | Outcome |
|-----------|---------|
| PP3 applied + no appropriate comparison P/LP variant in this splice region | PP3 |
| PP3 applied + P variant at this nt position with same predicted impact | PP3 + PS1 |
| PP3 applied + LP variant at this nt position with same predicted impact | PP3 + PS1_M |
| PP3 applied + P variant within the same splice region with same predicted impact | PP3 + PS1_M |
| PP3 applied + LP variant within the same splice region with same predicted impact | PP3 + PS1_Supp. |
| Not applied (prediction inconclusive) | N/A (consider protein impact if relevant) |
| BP4 applied + silent / intronic | BP4 + BP7 |
| BP4 applied + other variant types / positions | BP4 (only if protein impact ruled out) |

**Located at donor/acceptor +/-1,2 dinucleotide positions** — use PVS1 rules above for predicted impact:

| Condition | Outcome |
|-----------|---------|
| PVS1 applied (variants predicted to skip exon 1, disrupting initiation and frame) + no appropriate comparison P/LP variant in this splice region | PVS1 |
| PVS1 applied + P variant at this nt position or in same donor/acceptor +/-1,2 dinucleotide with same predicted impact | PVS1 + PS1_Supp. |
| PVS1 applied + P/LP variant within the same splice region, but outside donor/acceptor +/-1,2 dinucleotide, with same predicted impact | PVS1 + PS1_Supp. |
| PVS1_Strong applied (variants predicted to skip exon 2 or 4, which would disrupt critical functional domains, or exon 3, which would disrupt frame but not trigger NMD) + no appropriate comparison P/LP variant within this splice region | PVS1_Strong |
| PVS1_Strong + P variant at this nt position or in same donor/acceptor +/-1,2 dinucleotide with same predicted impact | PVS1_Strong + PS1 |
| PVS1_Strong + P variant within the same splice region, but outside donor/acceptor +/-1,2 dinucleotide, with same predicted impact | PVS1_Strong + PS1_M |
| PVS1_Strong + LP variant within the same splice region, but outside donor/acceptor +/-1,2 dinucleotide, with same predicted impact | PVS1_Strong + PS1_Supp. |
| PVS1 not applicable | Not applied |

#### RNA/Splicing Data

| Condition | Outcome |
|-----------|---------|
| No variant-specific observed impact + silent/intronic + BP7_S (RNA) applied | BP7_S (RNA) + prediction (PP3/BP4) — consider splicing predictive data |
| No variant-specific observed impact + other variant types/positions + assess pathogenicity using protein pathway + protein impact CAN be ruled out (based on functional and/or clinical data) | BP7_S (RNA) + prediction (PP3/BP4) |
| No variant-specific observed impact + protein impact CANNOT be ruled out | Document as "BP7_S (RNA)" Not Met to indicate that data was present and reviewed |
| Variant-specific impact (compared to controls), PVS1_Strength assigned to at least 1 transcript + evidence of complete production of alternative transcript(s) from variant allele | Keep strength level; determine PVS1 (RNA) weight from combined analysis but PP3/BP4 and PS3 not applicable |
| Same + evidence of near-complete production of alternative transcript(s) from variant allele | Reduce strength by 1 level; determine PVS1 (RNA) weight from combined analysis but PP3/BP4 and PS3 not applicable |
| Same + evidence of incomplete production of alternative transcript(s) from variant allele | Reduce strength by 1 level; PVS1 (RNA) and BP7_S (RNA) not applicable, but PP3/BP4 and PS3 can be applied |

---

### Appendix B: CTLA4 Phenotype Scoring Table (Qualifying Findings)

Transcribed from the attached "CTLA4 Phenotype Scoring Table". Source spellings preserved verbatim.

#### Clinical Criteria

| Points | Clinical criteria | Qualifying findings and phenotypes |
|--------|-------------------|-------------------------------------|
| 4 | Sinopulmonary infections and/or their sequelae | (A) Clinical history of; recurrent sinopulmonary (upper and lower respiratory tract) infections such as sinusitis, otitis, bronchitis, pneumonia), interstitial lung disease (lymphocytic or granulomatous), or pulmonary hypertension; (B) Abnormal PFTs; (C) Abnormal imaging studies (GGOs, mediastinal LAD, interstitial thickening, bronchiectasis, consolidation); (D) Other indicators of respiratory insufficiency or failure (i.e. prolonged ICU stay for respiratory support needs, history of lung transplant) |
| 4 | Non-infectious gastrointestinal or hepatobiliary disease | (A) Enteropathy; (B) Hepatopathy; (C) Autoimmune hepatitis; (D) Inflammatory bowel disease; (E) Primary sclerosing cholangitis; (F) Enterocolitis; (G) Celiac disease; (H) Atrophic gastritis; (I) Lymphocytic / microscopic colitis; (J) Exocrine pancreatic insufficiency; (K) Pernicious anemia |
| 2 | Immune mediated cytopenias | (A) Thrombocytopenia; (B) Anemia; (C) Hemolytic enemia [sic]; (D) Neutropenia; (E) Coombs/DAT positive (autoantibody testing may be negative) |
| 2 | Nonmalignant lymphoproliferation | (A) Lymph node swelling; (B) Lymphocytic infiltration; (C) Lymphadenopathy; (D) Splenomegaly; (E) Hepatosplenomegaly |
| 2 | Severe, persistent, recurrent viral infections including skin warts | — |
| 1 | Immunoe-mediated hair and skin findings [sic] | (A) Eczema; (B) Atopic dermatitis; (C) Psoriasiform dermatitis; (D) Alopecia; (E) Dermatitis; (F) Vitiligo; (G) Urticaria; (H) Lichenoid skin lesion |
| 1 | Neurological findings | (A) Clinical findings (seizures, aphasia, headaches, motor deficits, cerebellar ataxia, bowel/bladder, bulbar involvement, neurodevelopmental delays); (B) Imaging findings (white after hyperintensities [sic], leukoencephalopathy, leukodystrophy, deep brain involvement (BG, etc.), cerebellar atrophy, demyelinating spinal cord lesions (diffuse or focal), evidence of optic atrophy/neuritis) |
| 1 | Endocrinopathy | — |
| 1 | Severe, persistant, reucrrent, atypical opportunistic bacterial, mycobacterial, or fungal infections [sic] | — |
| 1 | Inflammatory findings | (A) Arthritis; (B) Vasculitis; (C) Recurrent fevers |
| 1 | Lymphoma | — |

#### Clinical Immunophenotypic Data

| Points | Finding |
|--------|---------|
| 2 | Hypogammaglobulinemia |
| 1 | Lymphopenia |
| 1 | Abnormal TBNK levels |
| 1 | Presence of autoantibodies |
| 1 | Defective antigen-specific immune responses |
| 1 | Histopathology findings of lymphocytic and/or granulomatous tissue infiltration |

#### Patient Cell-Based Assay Data

| Points | Assay | Qualifying finding |
|--------|-------|--------------------|
| 3* | Transendocytosis / Soluble CD80/CD86 ligand endocytosis | Reduced |
| 2* | *Ex vivo* T Cell Suppression | Reduced |
| 1* | Cell surface +/- intracellular CTLA4 expression | Reduced |

\*Avoid applying points from patient cell-based assay data to PP4, which already incorporates these data as rationale for an upgrade from PP4 to PP4_Moderate.

---

### Appendix C: Functional Assay Curation Summary

From the attached "CTLA4_Functional Assay_Research_PS3_BS3" workbook. "Approved assay" is the VCEP's per-publication determination.

#### In vitro assays in non-patient cells (eligible for PS3/BS3)

| PMID | Assay type | Approved | Proposed strength |
|------|-----------|----------|-------------------|
| 25329329 | Soluble ligand endocytosis (CHO cells) | y | PS3_supporting; BS3_supporting (in combination with a normal functional result from a second assay) |
| 25632005 | Transendocytosis (CHO donor/recipient) | n | NA |
| 25367873 | Soluble ligand endocytosis (HEK293) | y | PS3_supporting; BS3_supporting |
| 27102614 | Soluble ligand endocytosis (CHO cells) | y | PS3_supporting; BS3_supporting |
| 29375547 | Soluble ligand endocytosis (EBV-immortalized B cells) | y | PS3_supporting; BS3_supporting |
| 20870175 | Immobilized ligand binding (AND-Tg T cells) | n | NA |
| 29375547 | *In vitro* T cell suppression | y | PS3_supporting; BS3_supporting |
| 26478010 | *In vitro* T cell suppression (Jurkat, IL-2 ELISA) | y | PS3_supporting; BS3_supporting |
| 15814706 | CTLA4 endocytosis | n | NA |
| 7559643 | Cell surface expression / cell surface localization (COS cells) | y | PS3_supporting; BS3_supporting |
| 25213377 | Cell surface expression (HEK293 / donor PBMCs) | y | PS3_supporting; BS3_supporting |
| 25367873 | Cell surface expression (HEK293) | y | PS3_supporting; BS3_supporting |
| 14578884 | Cell surface expression (Jurkat, mouse CTLA4) | y | PS3_supporting; BS3_supporting |
| 29375547 | Cell surface expression (Jurkat CFP/YFP fusions) | y | PS3_supporting; BS3_supporting |

#### Patient-cell assays (PS4/PP4 only, not approved for PS3/BS3)

| PMID | Assay type | Approved for PS3/BS3 |
|------|-----------|----------------------|
| 25329329 | Transendocytosis (patient Treg cell assay) | n |
| 28159733 | Soluble ligand endocytosis (memory CD4+ T cell assay) | n |
| 34111452 | Transendocytosis (patient Treg cell assay) | n |
| 25213377 | Suppression of T cell proliferation (patient Treg assay) | n |
| 25213377 | Hyperproliferation (patient T cell assay) | n |
| 25329329 / 25213377 / 34111452 / 28159733 | CTLA4 cell surface or intracellular expression (patient cells) | n |

The VCEP note for all patient-cell entries: "This experiment assesses CTLA4 in the context of the patient genotype" (i.e., these data support PS4/PP4 rather than PS3/BS3).

---

### Appendix D: Population Frequency Thresholds Summary

| Criterion | Threshold (gnomAD v4.1.0) | Allele count requirement | Strength |
|-----------|---------------------------|--------------------------|----------|
| **BA1** | GrpMax Filtering AF ≥ 1.11 x 10⁻⁵ (0.0000111) | ≥5 alleles total across all populations | Stand Alone |
| **BS1** | GrpMax Filtering AF ≥ 1.11 x 10⁻⁶ (0.00000111) | ≥3 alleles total across all populations | Strong (-4) |
| **PM2_Supporting** | Total AF across all populations < 1.43 x 10⁻⁷ (0.000000143) | Not specified | Supporting (+1) |

---

### Appendix E: In Silico Thresholds Summary

| Criterion | Tool thresholds |
|-----------|-----------------|
| **PP3** (missense) | REVEL ≥ 0.644 **AND** CADD PHRED ≥ 25.3 |
| **PP3** (splicing) | SpliceAI Δ ≥ 0.2 (missense, synonymous, or intronic outside +/-1,2) |
| **BP4** (missense) | REVEL ≤ 0.290 **AND** CADD PHRED ≤ 22.7 **AND** SpliceAI Δ < 0.1 |
| **BP4** (synonymous/intronic) | SpliceAI Δ < 0.1 |
| **BP7** | Apply only if BP4 met; SpliceAI Δ < 0.1; intronic at/beyond +7/−21, or synonymous outside first nt and last 3 nt of exon |
| **PM4** | PhyloP ≥ 2.0 for at least one deleted nucleotide / adjacent amino acid **AND** SpliceAI < 0.2 |
| **PM5** | SpliceAI Δ < 0.2 for both variants; Grantham score of variant of interest ≥ comparison variant |
| **PVS1 (splicing evaluation)** | SpliceAI ≥ 0.2 with RNA/minigene confirmation of complete or near-complete disruption |

---

### Appendix F: Reference PMIDs Cited by This Specification

| PMID | Context |
|------|---------|
| 25741868 | Richards et al., 2015 ACMG/AMP guidelines; CTLA4 domain figure |
| 32720330 | Tavtigian et al., 2020 — Bayesian point scale, classification categories |
| 29300386 | Bayesian points scale adoption |
| 30192042 | ClinGen SVI PVS1 recommendations; PM4/PVS1 mutual exclusivity |
| 29543229 | ClinGen SVI VCEP Review Committee (PP5/BP6 not for use) |
| 31892348 | Brnich et al. — functional assay OddsPath/control recommendations (PS3/BS3) |
| 36413997 | REVEL/CADD calibration reference (PP3/BP4) |
| 37352859 | Splicing/PS1/BP7 recommendations |
| 3735285 | BP7_Strong (RNA) experimental evidence reference |
| 31298041 | CTLA4 domain structure figure |
| 40168991 | Alternative transcript NM_001037631.3 / soluble isoform |
| 25213377 | Transmembrane domain / soluble isoform; functional and patient assays |
| 25329329, 34111452 | Exon 3 / exon 2 null variant phenotypes; transendocytosis assays |
| 25632005, 25367873, 27102614, 29375547, 15814706, 20870175 | Transendocytosis / soluble ligand endocytosis assays |
| 26478010 | *In vitro* T cell suppression |
| 14578884, 7559643 | Cell surface / intracellular CTLA4 expression |
| 28159733 | Patient-cell soluble ligand endocytosis (PP4_Moderate) |

---

## Document History

| Version | Date | Notes (from the specification) |
|---------|------|--------------------------------|
| 2.0 | 7/31/2026 | "This submission includes updates to the PVS1, PM5, PS4, PP3, BP4, BP7, and PS3 codes." |

---

## Source Discrepancies and Verbatim Typos Noted

The following are reproduced as they appear in the source documents and are flagged here rather than silently corrected:

1. **Disease name spelling:** "autoimmune lymphoproliferative syndrome due to CTLA4 haploinsuffiency" (missing "c") appears both on the specification registry page and in the PDF.
2. **PVS1 codon ranges:** The PVS1 narrative assigns PVS1_Strong to "truncating variants between codons 183 and 201" and PVS1_Moderate to "nonsense or frameshift variants between codons 202 and 223", while the PVS1 decision tree describes the equivalent branch as "truncating variants between codons 183 and 223" split by whether the variant removes >10% or <10% of the protein. The two are reconcilable but not stated identically.
3. **Phenotype scoring table typos:** "Hemolytic enemia"; "Immunoe-mediated hair and skin findings"; "white after hyperintensities" (likely "white matter hyperintensities"); "Severe, persistant, reucrrent, atypical opportunistic ... infections".
4. **PS1 Supporting bullet:** the PDF renders "classified likely pathogenic" with a line-break artefact ("classified l" + "ikely pathogenic").
5. **Functional assay workbook:** column headers spell "endocysosis" (for "endocytosis").
6. **"Points system to reach final classification" attachment** is headed "…Variant Interpretation Guidelines Version 1", i.e., it was not re-versioned for this 2.0 release; its content (Tables 2 and 3 of PMID: 32720330) matches the classification categories shown on the version 2.0 specification page.
7. **PM4_Supporting, PVS1_Supporting, PM3, PP2, PP5, BS2, BP1, BP2, BP3, BP6** — no supporting-level or applicable specification is given; recorded above as "Not specified by VCEP" or Not Applicable per the VCEP's own comments.

---

*This document was compiled from the ClinGen Antibody Deficiencies Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for CTLA4 Version 2.0 (https://cspec.genome.network/cspec/ui/svi/doc/GN122) and its attached supplementary files. For the most current version, refer to the ClinGen website.*
