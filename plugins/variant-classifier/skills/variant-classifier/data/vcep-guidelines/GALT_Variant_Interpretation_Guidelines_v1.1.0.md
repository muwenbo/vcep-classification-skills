# Comprehensive Variant Interpretation Guidelines for GALT

## ClinGen Galactosemia VCEP Specifications for GALT (Version 1.1)

**Affiliation:** Galactosemia Variant Curation Expert Panel (Galactosemia VCEP)
**Version:** 1.1
**Release Date:** July 23, 2026
**DOI:** 10.5281/zenodo.21516133
**Based on:** Richards et al., 2015 - ACMG/AMP Variant Interpretation Guidelines

---

## Table of Contents

1. [Gene and Disease Information](#1-gene-and-disease-information)
2. [Pathogenic Criteria](#2-pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PM1 - Mutational Hot Spot](#pm1---mutational-hot-spot)
   - [PM2 - Absent from Controls](#pm2---absent-from-controls)
   - [PM3 - In Trans with Pathogenic Variant](#pm3---in-trans-with-pathogenic-variant)
   - [PM4 - Protein Length Changes](#pm4---protein-length-changes)
   - [PM5 - Novel Missense at Same Residue](#pm5---novel-missense-at-same-residue)
   - [PM6 - De Novo (Assumed)](#pm6---de-novo-assumed)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
   - [PP4 - Phenotype Specificity](#pp4---phenotype-specificity)
3. [Benign Criteria](#3-benign-criteria)
   - [BA1 - Stand-Alone Benign](#ba1---stand-alone-benign)
   - [BS1 - Allele Frequency Greater Than Expected](#bs1---allele-frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (Benign)](#bs3---functional-studies-benign)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP2 - In Trans/In Cis with Pathogenic](#bp2---in-transin-cis-with-pathogenic)
   - [BP4 - Computational Evidence (Benign)](#bp4---computational-evidence-benign)
   - [BP7 - Synonymous/Intronic Variants](#bp7---synonymousintronic-variants)
4. [Not Applicable Criteria](#4-not-applicable-criteria)
5. [Rules for Combining Criteria](#5-rules-for-combining-criteria)
6. [Appendices](#6-appendices)

---

## 1. Gene and Disease Information

| Parameter | Value |
|-----------|-------|
| **Gene** | GALT (HGNC:4135) |
| **HGNC Name** | galactose-1-phosphate uridylyltransferase |
| **Reference Transcript** | NM_000155.4 |
| **Disease** | Galactosemia |
| **MONDO ID** | MONDO:0018116 |
| **Mode of Inheritance** | Autosomal recessive inheritance |

### Key Gene Characteristics

- Exons 6, 7, and 9 are in-frame; exon skipping consequences for splice site variants are specified in the VCEP PVS1 decision tree.
- The active site region spans amino acids Phe171 to Gln188.
- GALT is **not** constrained for missense variation (missense Z score: 0.91); missense variants are nonetheless a known cause of disease.
- De novo occurrence is not expected to contribute significantly to disease (only one de novo occurrence of a GALT variant has ever been reported).

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specification:** The Galactosemia VCEP will utilize SVI's PVS1 recommendation for determining applicable PVS1 strength level (Abou Tayoun et al., 2018; PMID: 30192042). Refer to the GALT VCEP modified PVS1 decision tree.

**Modification Type:** Very Strong = Disease-specific; Strong and Moderate = Disease-specific, Strength

#### General Caveats

- Beware of genes where LOF is not a known disease mechanism (e.g., GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

#### GALT PVS1 Decision Tree

##### Nonsense or Frameshift Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| Predicted to undergo NMD (*termination pre-c.1010*) | **PVS1** |
| Not predicted to undergo NMD (*variant impacts exon 11 (c.1060-1140) or last 50 nucleotides of exon 10*) + variant removes >10% of protein (*more than 38 amino acids*) | **PVS1** |
| Not predicted to undergo NMD + variant removes <10% of protein (*less than/equal to 38 amino acids*) + truncated/altered region is critical to protein function (exon 6, amino acids 171-188) | **PVS1_Strong** |
| Not predicted to undergo NMD + variant removes <10% of protein + role of region in protein function is unknown | **PVS1_Moderate** |

##### Canonical Splice Site Variants (GT-AG ±1,2)

| Condition | PVS1 Strength |
|-----------|---------------|
| Exon skipping or use of a cryptic splice site disrupts the reading frame and is predicted to undergo NMD (*donor and acceptor sites of exons 1-5, 8*) | **PVS1** |
| Exon skipping or use of a cryptic splice site preserves the reading frame (*donor and acceptor sites of exons 6, 7, 9, 10*) + truncated/altered region is critical to protein function (exon 6, amino acids 171-188) | **PVS1_Strong** |
| Exon skipping or use of a cryptic splice site preserves the reading frame + role of region in protein function is unknown | **PVS1_Moderate** |

##### Deletions (Single Exon to Full Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Full gene deletion | **PVS1** |
| Single to multi-exon deletion disrupting the reading frame and predicted to undergo NMD | **PVS1** |
| Single to multi-exon deletion disrupting the reading frame and NOT predicted to undergo NMD | **PVS1_Strong** |
| Single to multi-exon deletion preserving the reading frame | **PVS1_Strong** |

##### Duplications (≥1 Exon, Completely Contained Within Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Proven in tandem + reading frame disrupted + NMD predicted to occur | **PVS1** |
| Proven in tandem + no or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem + reading frame presumed disrupted + NMD predicted to occur | **PVS1_Strong** |
| Proven not in tandem | N/A |

##### Initiation Codon Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| Initiation codon variant | **PVS1_Strong** |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PS1** (Strong) | Applied for 1 previously established **pathogenic** missense variant, or per Table 2 in Walker et al., 2023 (PMID: 37352859) for splicing variants |
| **PS1_Moderate** | Applied for 1 previously established **likely pathogenic** variant, or per Table 2 in Walker et al., 2023 (PMID: 37352859) for splicing variants |
| **PS1_Supporting** | Applies for **splicing variants only**, using Table 2 in Walker et al., 2023 (PMID: 37352859) |

#### Requirements (all strengths)

- Splicing abnormalities (using VCEP-specified prediction algorithms or evidence from the literature) should be excluded for all missense variants.
- The other variant(s) used as evidence must also have been curated using the GALT VCEP rule specifications and must reach a pathogenic/likely pathogenic classification **without** using PS1.

#### Application to Splicing Variants

- The variant must have the same predicted impact on splicing as the previously classified variant (refer to Table 2 in Walker et al., 2023; PMID: 37352859).
- PS1 can be applied at varying strengths (strong, moderate, supporting) in conjunction with either PP3 or PVS1. PS1 strength depends on the location of the variant under assessment (within or outside the ±1,2 dinucleotide positions) and the location of the previously classified variant (within or outside the ±1,2 dinucleotide positions). Specific combinations are outlined in Table 2 of Walker et al., 2023.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **PS3_Supporting** | Applicable for up to **20% enzyme activity** in a model system |

**Modification Type:** Disease-specific

**Note:** The VCEP proposed only the supporting strength level for PS3; PS3 at Strong or Moderate is not specified by the VCEP.

#### Approved Functional Assays

All approved assays were assigned a proposed strength of "supportive" by the VCEP.

| Assay Class | PMIDs | Description |
|-------------|-------|-------------|
| Enzyme assay in *E. coli* | 10037750; 11592823; 22461411; 30172461; 3678883; 27005423 | Recombinant human GALT expressed in a GALT(-) *E. coli*; lysates or purified GALT incubated with UDP-glucose, NADP and galactose-1-phosphate; NADPH production quantified at 340 nm to derive glucose-1-phosphate released |
| Yeast assay | 18210213; 11152465; 23690308; 8421669 | Human GALT expressed in a null-background yeast strain; GALT function in soluble cell lysates tested by in vitro activity assays |
| Mammalian assay | 31392114; 20547145 | HeLa-based cell-free protein expression system, or overexpression in 293 cells, with in vitro GALT enzyme activity measurement |

#### Enzyme Activity Groups (VCEP functional evidence table)

| Group | Residual Activity (% wild-type) | Applicable Code |
|-------|--------------------------------|-----------------|
| **Group I** | Undetectable | PS3_Supporting |
| **Group II** | <1%, detectable | PS3_Supporting |
| **Group III** | 1-5% | PS3_Supporting |
| **Group IV** | >5-10% | PS3_Supporting |
| **Group V** | >10-20% | PS3_Supporting |
| **Group VI** | >20-50% | No functional code applied |
| **Group VII** | >50% | BS3_Supporting |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **PM1** (Moderate) | Applied at moderate strength for variants that occur in the **active site from Phe171 to Gln188** |

**Modification Type:** Disease-specific

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Note:** The PM2 threshold was calculated as one order of magnitude below BS1.

#### VCEP Specification

| Strength | Threshold |
|----------|-----------|
| **PM2_Supporting** | gnomAD PopMax filtering allele frequency (FAF) **≤ 0.0005 (0.05%)** |

**Modification Type:** Disease-specific, Strength

#### Requirements and Notes

- Can only be used at the supporting level.
- Use the PopMax filtering allele frequency (FAF) from gnomAD.
- PM2 is **not** considered conflicting data with BP4 or BP7.
- A curated list of GALT variants known to be pathogenic despite not fulfilling the PM2 criterion has been developed (see PM2 exception list, Appendix D).

---

### PM3 - In Trans with Pathogenic Variant

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

#### VCEP Specifications

Tables adapted from the ClinGen Sequence Variant Interpretation Recommendation for the in trans criterion (PM3), Version 1.0.

**Prerequisites:**
- The variant under investigation must meet PM2.
- Identified individuals must meet PP4.
- Pathogenicity of the variant in trans must be determined using the GALT VCEP guidelines.

| Strength | Application |
|----------|-------------|
| **PM3_VeryStrong** | Variant meets PM2, identified individuals meet PP4, and at least **4** PM3 points have been reached |
| **PM3_Strong** | Variant meets PM2, identified individuals meet PP4, and at least **2** PM3 points have been reached |
| **PM3** (Moderate) | Variant meets PM2, identified individual(s) meet PP4, and at least **1** PM3 point has been reached |
| **PM3_Supporting** | Variant meets PM2, identified individual(s) meet PP4, and at least **0.5** PM3 points have been reached |

**Modification Type:** Disease-specific, Strength

##### Points Awarded per In Trans Proband

| Classification/Zygosity of Other Variant¹ | Confirmed In Trans | Phase Unknown |
|-------------------------------------------|--------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (max point 1.0) | 0.5 | N/A |
| Uncertain significance variant (max point 0.5) | 0.25 | 0.0 |

¹All variants should be sufficiently rare (meet PM2 specification); P = Pathogenic; LP = Likely pathogenic

##### Determining Evidence Strength Level

| Total Points | Evidence Strength |
|--------------|-------------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_VeryStrong |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **PM4** (Moderate) | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants |

**Modification Type:** No change

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PM5** (Moderate) | Applied at moderate strength for **1 pathogenic variant** with no benign variation at the residue |
| **PM5_Supporting** | Applied for **1 likely pathogenic variant** with no benign variation at the residue |

**Modification Type:** Strength

#### Requirements

- Splicing abnormalities (using VCEP-specified prediction algorithms or evidence from the literature) should be excluded for all missense variants (PM5_Moderate).
- The other variant(s) used as evidence must also have been curated using the GALT VCEP rule specifications and must reach a pathogenic/likely pathogenic classification **without** PM5.
- Grantham should be used to compare the variants. The new variant must be equal or worse than the known pathogenic variant.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **PM6** (Moderate) | Paternity and maternity must be confirmed. Patient must meet PP4. |

**Modification Type:** Disease-specific

**Notes:**
- Because there has only ever been one reported de novo occurrence of a GALT variant and de novo occurrence is not expected to significantly contribute to disease, the VCEP will use PM6 and **not** PS2.
- PM6 will **not** be upgraded with number of occurrences.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

#### VCEP Specifications

Use the general recommendations from Oza AM et al., 2018 (PMID: 30311386); sufficient affected and unaffected segregations must have been counted to reach the specified likelihood.

| Strength | Likelihood | LOD Score |
|----------|------------|-----------|
| **PP1_Supporting** | 4:1 | 0.6 |
| **PP1_Moderate** | 16:1 | 1.2 |
| **PP1_Strong** | 32:1 | 1.5 |

**Modification Type:** Disease-specific, Strength

##### Autosomal Recessive LOD Score Table (Phenocopy not an issue)

Rows = affected segregations; columns = unaffected segregations.

| Affected \ Unaffected | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **0** | 0 | 0.12 | 0.25 | 0.37 | 0.5 | 0.62 | 0.75 | 0.87 | 1 | 1.12 | 1.25 |
| **1** | 0.6 | 0.73 | 0.85 | 0.98 | 1.1 | 1.23 | 1.35 | 1.48 | 1.6 | 1.73 | 1.85 |
| **2** | 1.2 | 1.33 | 1.45 | 1.58 | 1.7 | 1.83 | 1.95 | 2.08 | 2.2 | 2.33 | 2.45 |
| **3** | 1.81 | 1.93 | 2.06 | 2.18 | 2.31 | 2.43 | 2.56 | 2.68 | 2.81 | 2.93 | 3.06 |
| **4** | 2.41 | 2.53 | 2.66 | 2.78 | 2.91 | 3.03 | 3.16 | 3.28 | 3.41 | 3.53 | 3.66 |
| **5** | 3.01 | 3.14 | 3.26 | 3.39 | 3.51 | 3.63 | 3.76 | 3.88 | 4.01 | 4.13 | 4.26 |
| **6** | 3.61 | 3.74 | 3.86 | 3.99 | 4.11 | 4.24 | 4.36 | 4.49 | 4.61 | 4.74 | 4.86 |
| **7** | 4.21 | 4.34 | 4.46 | 4.59 | 4.71 | 4.84 | 4.96 | 5.09 | 5.21 | 5.34 | 5.46 |
| **8** | 4.82 | 4.94 | 5.07 | 5.19 | 5.32 | 5.44 | 5.57 | 5.69 | 5.82 | 5.94 | 6.07 |
| **9** | 5.42 | 5.54 | 5.67 | 5.79 | 5.92 | 6.04 | 6.17 | 6.29 | 6.42 | 6.54 | 6.67 |
| **10** | 6.02 | 6.15 | 6.27 | 6.4 | 6.52 | 6.65 | 6.77 | 6.9 | 7.02 | 7.15 | 7.27 |

**Strength Legend:**
- LOD 0.6-1.19: PP1_Supporting
- LOD 1.2-1.49: PP1_Moderate
- LOD ≥1.5: PP1_Strong

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **PP3_Supporting** | For **missense** variants use REVEL with a score **≥0.7** |
| **PP3_Supporting** | For **in-frame in/dels**, Provean ("deleterious") and MutationTaster ("Disease-causing") must agree |
| **PP3_Supporting** | For **non-canonical splicing** variants use SpliceAI with a score **≥0.2**; look for cryptic splice sites |

**Modification Type:** Disease-specific

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PP4_Moderate** | RBC GALT enzyme activity **<10%**; newborn screen alone would not count, confirmatory testing required; full *GALT* gene sequencing (exons and exon/intron boundaries) rather than *GALT* panel testing must have been carried out |
| **PP4** (Supporting) | RBC GALT enzyme activity **<10%**; newborn screen alone would not count, confirmatory testing required |

**Modification Type:** Moderate = Disease-specific, Strength; Supporting = Disease-specific

**Requirement:** Variants must meet PM2_Supporting for PP4 to apply at any strength.

**Note:** This VCEP does not use a point-based PP4 system.

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

#### VCEP Specification

| Strength | Threshold |
|----------|-----------|
| **BA1** (Stand Alone) | gnomAD PopMax FAF **≥ 0.01 (1%)** |

**Modification Type:** Disease-specific

##### Calculation Parameters (Whiffin/Ware Calculator)

- Prevalence: 1 in 10,000
- Penetrance: 100%
- Maximum allelic contribution: 100%
- Maximum genetic contribution: 100%

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### VCEP Specification

| Strength | Threshold |
|----------|-----------|
| **BS1** (Strong) | gnomAD PopMax FAF **≥ 0.005 (0.5%)** |

**Modification Type:** Disease-specific

##### Calculation Parameters (Whiffin/Ware Calculator)

- Prevalence: 1 in 10,000
- Penetrance: 100%
- Maximum allelic contribution: 50%
- Maximum genetic contribution: 100%

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **BS2** (Strong) | Applicable when the individual is confirmed to be **unaffected by GALT activity levels** |

**Modification Type:** Disease-specific

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **BS3_Supporting** | Applicable for **greater than 50% enzyme activity** in a model system (Group VII) |

**Modification Type:** Disease-specific

#### Requirements

- Can only be used at the supporting level (cannot apply at strong level).
- Functional assay must be in non-patient material.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **BS4** (Strong) | Individual considered unaffected with **RBC GALT enzyme activity ≥25%**, with the caveat of no bone marrow transfusions in the individual |

**Modification Type:** No change

---

### BP2 - In Trans/In Cis with Pathogenic

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **BP2_Supporting** | Observed **in cis** with a likely pathogenic or pathogenic variant **OR** observed **in trans** with a pathogenic variant in an unaffected individual with RBC GALT enzyme activity in the carrier range |

**Modification Type:** Disease-specific

#### Requirements

- Pathogenicity of the first variant must be determined using the GALT VCEP guidelines.
- Full gene sequencing including the promoter region must have been completed to apply BP2.

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **BP4_Supporting** | For **missense** variants use REVEL with a score **<0.15** |
| **BP4_Supporting** | For **in-frame in/dels**, Provean ("neutral") and MutationTaster ("polymorphism") must agree |
| **BP4_Supporting** | For **non-canonical splicing** variants use SpliceAI with a score **<0.1**; do not use if there is evidence of a cryptic splice site |

**Modification Type:** Disease-specific

---

### BP7 - Synonymous/Intronic Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **BP7_Supporting** | Use "as is", but with **no conservation requirement** |

**Modification Type:** Disease-specific

#### Requirements and Notes

- BP4 must be applied for BP7 to be used; the codes can be combined.
- Do not use for silent variants in the first nucleotide or last 3 nucleotides of the exon.
- Can also be used for intronic variants at or beyond positions +7/-21 with no predicted effect on splicing.

---

## 4. Not Applicable Criteria

The following ACMG/AMP criteria are **NOT APPLICABLE** for GALT variant interpretation:

| Criterion | Original Purpose | Reason Not Applicable |
|-----------|-----------------|----------------------|
| **PS2** | De novo (confirmed) | Because there has only ever been one reported de novo occurrence of a GALT variant and de novo occurrence is not expected to significantly contribute to disease, de novo data will be used in the PM6 code |
| **PS4** | Prevalence in affected individuals | Not applicable (no reason stated by VCEP) |
| **PP2** | Low rate of benign missense | GALT is not constrained for missense (Z score: 0.91) variants |
| **PP5** | Reputable source reports pathogenic | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |
| **BP1** | Missense in truncating disease gene | Not applicable; missense variants are also known to cause disease |
| **BP3** | In-frame deletion in repetitive region | Repetitive regions without a known function are not well-described in GALT |
| **BP5** | Alternate molecular basis for disease | Galactosemia has variable age of onset and there is variable expressivity in affected individuals |
| **BP6** | Reputable source reports benign | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |

---

## 5. Rules for Combining Criteria

### Pathogenic Classification

| Combination | Applicable Codes | Classification |
|-------------|------------------|----------------|
| 1 Very Strong AND ≥1 Strong | VS: PVS1, PM3_VeryStrong / S: PVS1_Strong, PS1, PM3_Strong, PP1_Strong | **Pathogenic** |
| 1 Very Strong AND ≥2 Moderate | M: PVS1_Moderate, PS1_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate | **Pathogenic** |
| 1 Very Strong AND 1 Moderate AND 1 Supporting | Sup: PS1_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM5_Supporting, PP1, PP3, PP4 | **Pathogenic** |
| 1 Very Strong AND ≥2 Supporting | — | **Pathogenic** |
| ≥2 Strong | PVS1_Strong, PS1, PM3_Strong, PP1_Strong | **Pathogenic** |
| 1 Strong AND ≥3 Moderate | — | **Pathogenic** |
| 1 Strong AND 2 Moderate AND ≥2 Supporting | — | **Pathogenic** |
| 1 Strong AND 1 Moderate AND ≥4 Supporting | — | **Pathogenic** |

### Likely Pathogenic Classification

| Combination | Classification |
|-------------|----------------|
| 1 Very Strong AND 1 Moderate | **Likely Pathogenic** |
| 1 Strong AND 1 Moderate | **Likely Pathogenic** |
| 1 Strong AND ≥2 Supporting | **Likely Pathogenic** |
| ≥3 Moderate | **Likely Pathogenic** |
| 2 Moderate AND ≥2 Supporting | **Likely Pathogenic** |
| 1 Moderate AND ≥4 Supporting | **Likely Pathogenic** |
| 1 Strong AND 2 Moderate | **Likely Pathogenic** |
| **1 Strong (PVS1_Strong) AND 1 Supporting (PM2_Supporting)** | **Likely Pathogenic** |

### Benign Classification

| Combination | Applicable Codes | Classification |
|-------------|------------------|----------------|
| ≥2 Strong | BS1, BS2, BS4 | **Benign** |
| 1 Stand Alone | BA1 | **Benign** |

### Likely Benign Classification

| Combination | Applicable Codes | Classification |
|-------------|------------------|----------------|
| 1 Strong AND 1 Supporting | Strong: BS1, BS2, BS4 / Supporting: BS3_Supporting, BP2, BP4, BP7 | **Likely Benign** |
| ≥2 Supporting | BS3_Supporting, BP2, BP4, BP7 | **Likely Benign** |

### Variant of Uncertain Significance (VUS)

- Criteria for benign and pathogenic are contradictory
- No criteria met
- Criteria met do not reach threshold for Likely Benign or Likely Pathogenic

**Note:** PM2 is not considered conflicting data with BP4 or BP7.

---

## 6. Appendices

### Appendix A: Key References

| Citation | PMID | Topic |
|----------|------|-------|
| Richards et al., 2015 | 25741868 | ACMG/AMP Variant Interpretation Guidelines |
| Abou Tayoun et al., 2018 | 30192042 | ClinGen SVI PVS1 Recommendations |
| Walker et al., 2023 | 37352859 | PS1/PM5 application to splicing variants (Table 2) |
| Oza et al., 2018 | 30311386 | PP1 Segregation Recommendations |
| Biesecker et al., 2018 | 29543229 | SVI recommendation not to use PP5/BP6 |
| ClinGen SVI, in trans (PM3) Recommendation v1.0 | - | PM3 point system (accessed October 2023) |

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold (gnomAD PopMax FAF) | Strength |
|-----------|-------------------------------|----------|
| BA1 | ≥0.01 (1%) | Stand Alone |
| BS1 | ≥0.005 (0.5%) | Strong |
| PM2 | ≤0.0005 (0.05%) | Supporting |

### Appendix C: Functional Assay Enzyme Activity Reference Data

Variant-level residual activity values curated by the VCEP (assay system in parentheses):

| Group | Activity (% WT) | Variants |
|-------|-----------------|----------|
| **I** (undetectable) | ≈0 | M142K, R204X, Q206R, R148Q, E202K, F171S, H132Q, I170T, L116P, L227P, L327P, P185H, Q188R, R148P, R259Q, R272H, T204X, V168L, W300X, Y34N (E. coli) |
| **II** (<1%, detectable) | 0.15-0.94 | R333W, R148W, R231H, H186P, K285N, R259W, Q169H, L195P, A320T |
| **III** (1-5%) | 1.4-4.7 | S135Y, Y323C, L139P, H31R, R67C, S135C, E58K, S135L, H321Y, S135H, M178R, S135A |
| **IV** (>5-10%) | 5.46-9.9 | Q344K, D136H, I278N, V151A, T138M, A320V, Y323D, T350A |
| **V** (>10-20%) | 10-19.13 | P295T, Y209C, D98N |
| **VI** (>20-50%) | 23.75-45.2 | H47D, E220K, A78T, D197G, S135T, R223S, L289F, P183T, Y34N (yeast) |
| **VII** (>50%) | 50-134 | E291V, R201C, A81T, E291K, T268N, E363F, D113N, R201H, V157I, L116I, N314D, R333R |

Group counts reported by the VCEP: I = 20, II = 9, III = 12, IV = 7, V = 3, VI = 9, VII = 12.

### Appendix D: PM2 Exception List

GALT variants known to be pathogenic despite not fulfilling the PM2 criterion:

| Variant | Status | Comment |
|---------|--------|---------|
| NM_000155.4(GALT):c.404C>T (p.Ser135Leu) | Does not meet PM2 | Known pathogenic variant |
| NM_000155.4(GALT):c.563A>G (p.Gln188Arg) | Does not meet PM2 | Known pathogenic variant |
| NM_000155.4(GALT):c.584T>C (p.Leu195Pro) | Does not meet PM2 | Known pathogenic variant |
| NM_000155.4(GALT):c.855G>T (p.Lys285Asn) | Does not meet PM2 | Known pathogenic variant |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.1 | July 23, 2026 | 6/11/26: Removed SVI response documents; added that PVS1 + PM2_Supporting = Likely Pathogenic; added that PM2 is not considered conflicting data with BP4 or BP7. 7/21/26: Removed documents from public view. |

---

*This document is based on the ClinGen Galactosemia Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for GALT Version 1.1 (GN158; DOI 10.5281/zenodo.21516133).*
