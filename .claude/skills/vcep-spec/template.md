# ClinGen {VCEP_NAME} Variant Interpretation Guidelines for {GENE}

**Version:** {VERSION}
**Released:** {RELEASE_DATE}
**Affiliation:** {VCEP_AFFILIATION}
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | {GENE_SYMBOL} ({HGNC_ID}) |
| **HGNC Name** | {HGNC_NAME} |
| **Transcript** | {TRANSCRIPT} |
| **Disease** | {DISEASE} ({MONDO_ID}) |
| **Inheritance** | {INHERITANCE} |

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
   - [BA1 - Allele Frequency >5%](#ba1---allele-frequency-5)
   - [BS1 - Frequency Greater Than Expected](#bs1---frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (No Effect)](#bs3---functional-studies-no-effect)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP1-BP7 - Benign Supporting](#bp1-bp7---benign-supporting)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specifications:**

{PVS1_SPECIFICATIONS}

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | {PVS1_VERY_STRONG} |
| **Strong** | {PVS1_STRONG} |
| **Moderate** | {PVS1_MODERATE} |
| **Supporting** | {PVS1_SUPPORTING} |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | {PS1_STRONG} |
| **Moderate** | {PS1_MODERATE} |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:** {PS2_SPECIFICATIONS}

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed Parental Relationships | Unconfirmed |
|------------------------|----------------------------------|-------------|
| Phenotype highly specific for gene | 2 points | 1 point |
| Phenotype consistent but not highly specific | 1 point | 0.5 points |
| Phenotype consistent + high genetic heterogeneity | 0.5 points | 0.25 points |
| Phenotype not consistent | 0 points | 0 points |

#### Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 0.5 | Supporting |
| 1.0 | Moderate |
| 2.0 | Strong |
| 4.0 | Very Strong |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | {PS3_STRONG} |
| **Moderate** | {PS3_MODERATE} |
| **Supporting** | {PS3_SUPPORTING} |

#### Approved Assay Instances

{PS3_ASSAYS}

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** {PS4_SPECIFICATIONS}

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation.

**VCEP Specifications:** {PM1_SPECIFICATIONS}

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only):**
- gnomAD popmax filtering allele frequency **<{PM2_THRESHOLD}**
- {PM2_ADDITIONAL_REQUIREMENTS}

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:** {PM3_SPECIFICATIONS}

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous (non-consanguineous) | 1.0 | 1.0 |
| Homozygous (consanguineous, max 0.5/family) | 0.5 | 0.5 |
| VUS (max 0.5 total) | 0.25 | 0.0 |

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_VeryStrong |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | {PM4_MODERATE} |
| **Supporting** | {PM4_SUPPORTING} |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specifications:** {PM5_SPECIFICATIONS}

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Same as PS2 - use point-based system above.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members.

**VCEP Specifications:** {PP1_SPECIFICATIONS}

#### PP1 Thresholds

| Strength | Likelihood | LOD Score |
|----------|------------|-----------|
| Supporting | 4:1 | 0.6 |
| Moderate | 16:1 | 1.2 |
| Strong | 32:1 | 1.5 |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** {PP2_SPECIFICATIONS}

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**VCEP Specifications:** {PP3_SPECIFICATIONS}

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** {PP4_SPECIFICATIONS}

#### PP4 Strength Thresholds

| Total Points | Strength |
|--------------|----------|
| <1 | PP4 not met |
| 1 to <2 | PP4 (Supporting) |
| 2 to <6 | PP4_Moderate |
| ≥6 | PP4_Strong |

#### PP4 Point System

{PP4_POINT_TABLE}

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** {PP5_SPECIFICATIONS}

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**
- gnomAD popmax filtering allele frequency **>{BA1_THRESHOLD}**

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- gnomAD popmax filtering allele frequency **>{BS1_THRESHOLD}**

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder.

**VCEP Specifications:** {BS2_SPECIFICATIONS}

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** {BS3_SPECIFICATIONS}

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:** {BS4_SPECIFICATIONS}

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | {BP1_STATUS} | {BP1_COMMENT} |
| **BP2** | {BP2_STATUS} | {BP2_COMMENT} |
| **BP3** | {BP3_STATUS} | {BP3_COMMENT} |
| **BP4** | {BP4_STATUS} | {BP4_COMMENT} |
| **BP5** | {BP5_STATUS} | {BP5_COMMENT} |
| **BP6** | {BP6_STATUS} | {BP6_COMMENT} |
| **BP7** | {BP7_STATUS} | {BP7_COMMENT} |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** ≥1 Strong |
| 1 Very Strong **AND** ≥2 Moderate |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting |
| 1 Very Strong **AND** ≥2 Supporting |
| ≥2 Strong |
| 1 Strong **AND** ≥3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** ≥2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** ≥4 Supporting |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** ≥2 Supporting |
| ≥3 Moderate |
| 2 Moderate **AND** ≥2 Supporting |
| 1 Moderate **AND** ≥4 Supporting |
| 1 Strong **AND** 2 Moderate |

### Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

{LIKELY_BENIGN_RULES}

---

## Appendices

### Appendix A: PVS1 Flowchart

{PVS1_FLOWCHART}

### Appendix B: Reference PMIDs

{REFERENCE_PMIDS}

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >{BA1_THRESHOLD} | Stand Alone |
| BS1 | >{BS1_THRESHOLD} | Strong |
| PM2 | <{PM2_THRESHOLD} | Supporting |

---

## Version History

{VERSION_HISTORY}

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
