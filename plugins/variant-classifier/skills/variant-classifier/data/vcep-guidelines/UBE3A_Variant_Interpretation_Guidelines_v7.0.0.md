# Comprehensive Variant Interpretation Guidelines for UBE3A

## ClinGen Rett and Angelman-like Disorders VCEP Specifications for UBE3A (Version 7.0)

**Affiliation:** Rett and Angelman-like Disorders Variant Curation Expert Panel (Rett and Angelman-like Disorders VCEP)
**Version:** 7.0
**Release Date:** May 1, 2026
**Specification Type:** Richards et al., 2015 - Combining rules
**DOI:** 10.5281/zenodo.21421718
**Source:** https://cspec.genome.network/cspec/ui/svi/doc/GN037 (GN037)

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
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (Benign)](#bs3---functional-studies-benign)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP2 - In Trans / In Cis with Pathogenic Variant](#bp2---in-trans--in-cis-with-pathogenic-variant)
   - [BP3 - In-frame Indel in Repetitive Region](#bp3---in-frame-indel-in-repetitive-region)
   - [BP4 - Computational Evidence (Benign)](#bp4---computational-evidence-benign)
   - [BP5 - Alternate Molecular Basis for Disease](#bp5---alternate-molecular-basis-for-disease)
   - [BP7 - Synonymous (Silent) Variants](#bp7---synonymous-silent-variants)
4. [Not Applicable Criteria](#4-not-applicable-criteria)
5. [Rules for Combining Criteria](#5-rules-for-combining-criteria)
6. [Appendices](#6-appendices)

---

## 1. Gene and Disease Information

| Parameter | Value |
|-----------|-------|
| **Gene** | UBE3A (HGNC:12496) |
| **HGNC Name** | ubiquitin protein ligase E3A |
| **Reference Transcript** | NM_130838.2 |
| **Disease** | Angelman syndrome |
| **MONDO ID** | MONDO:0007113 |
| **Mode of Inheritance** | Autosomal dominant inheritance |

**Keywords (from specification):** human biology, genomics, variant, variant classification, clingen, disease standards, UBE3A, NM_130838.2, Autosomal dominant inheritance, Angelman syndrome

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Original ACMG Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

#### VCEP Specifications

Refer to PVS1 flow chart for additional guidance.

For intragenic deletions/duplications that are predicted to result in a product that preserves reading frame:

- For single exon in-frame deletions assign the same strength (PVS1, PVS1_strong, or PVS1_moderate) as for splice site variants that preserve reading frame indicated above.
- For multiple exon in-frame deletions PVS1 can be assigned to deletions that include single in-frame exons in the PVS1 category (listed above) OR if the exon contains a functionally important domain as specified in PM1.
- Given the extensive data available for *UBE3A*, classifications for single or multi-exon in-frame deletions are assigned as PVS1 or PVS1_strong. Refer to PVS1 flow chart for additional guidance.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **PVS1** (Very Strong) | Null variant in a gene where loss of function is a known mechanism of disease. Use as defined by ClinGen SVI working group (PMID: 30192042). PVS1 is applicable for: any truncating variant up to p.K841; any frameshift variant that results in a read-through of the stop codon; initiation codon variants; canonical splice site variants predicted to result in an out-of-frame product; intragenic deletions/duplications predicted to result in an out-of-frame product; full gene deletion. *(Modification type: Disease-specific)* |
| **PVS1_Strong** | Null variant in a gene where loss of function is a known mechanism of disease. PVS1_Strong is applicable for: any truncating variant from p.A842 to p.G850; canonical splice site variants that flank exons 7, 8 (in-frame exons). *(Modification type: Disease-specific, Strength)* |
| **PVS1_Moderate** | Null variant in a gene where loss of function is a known mechanism of disease. PVS1_Moderate is applicable for any truncating variant distal of p.G850. *(Modification type: Disease-specific, Strength)* |
| **PVS1_Supporting** | Not specified by VCEP |

Note: the p.K841 boundary is referenced to Fang P, Lev-Lehman E et al., *The spectrum of mutations in UBE3A causing Angelman syndrome*, Hum Mol Genet (1999), PMID 9887341.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **PS1** (Strong) | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. *(Modification type: None)* |
| **PS1_Moderate** | Not specified by VCEP |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### VCEP Specifications

- Applicable to all genes in affected individuals identified as mosaic for the variant (as the presence of a variant in the mosaic state is confirmatory of the variant being de novo).
- Because of the very high de novo rate of pathogenic variants in UBE3A, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **PS2_VeryStrong** | De novo (maternity and paternity confirmed) in a patient with the disease and no family history. ≥2 independent occurrences of PS2; **or** ≥2 independent occurrences of PM6 and one occurrence of PS2. Evidence from literature must be fully evaluated to support independent events. *(Modification type: None)* |
| **PS2** (Strong) | De novo (maternity and paternity confirmed) in a patient with the disease and no family history. 1 occurrence of PS2. *(Modification type: None)* |
| **PS2_Moderate / PS2_Supporting** | Not specified by VCEP |

See also [PM6 - De Novo (Assumed)](#pm6---de-novo-assumed) for the assumed de novo occurrence counts.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **PS3** (Strong) | Well-established in vitro or in vivo functional studies supportive of a damaging effect. RNA studies that demonstrate abnormal splicing and an out-of-frame transcript. Do not use for canonical splice site variants and when PVS1 is used. *(Modification type: Disease-specific)* |
| **PS3_Moderate** | Not specified by VCEP |
| **PS3_Supporting** | Well-established in vitro or in vivo functional studies supportive of a damaging effect. RNA studies that demonstrate abnormal splicing and an inframe product (unless it affects an in-frame exon specified in the PVS1 section). See included table for acceptable functional studies. *(Modification type: Disease-specific)* |

#### Approved Functional Assays (UBE3A Functional Assays table)

| Name of assay | Measured parameter | Expected deleterious result range (PS3_Supporting) | Expected benign result range (BS3) | References |
|---------------|--------------------|----------------------------------------------------|------------------------------------|------------|
| E3 ubiquitin ligase activity | E3 ubiquitin ligase activity | Loss of substrate ubiquitination | Not recommended | PMID: 15263005; 26255772 |
| UBE3A protein expression | Protein levels monitored to reflect either protein stability or levels of self degradation. | Comparison to WT possible however no robust thresholds available. | Not recommended | PMID: 26255772 |
| UBE3A nuclear localization | UBE3A subcelluar localization | Cytoplasmic localization | Not recommended | PMID: 31235931, 33607653 |

*Note: "subcelluar" is spelled as it appears in the source specification file.*

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

#### VCEP Specifications

- Detailed phenotype not needed. Need to confirm patient is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.
- Patient can be published OR an internal case OR observed at an outside lab (i.e. via ClinVar) OR described in the reputable databases (LOVD). However, the independent case has to be confirmed to be a different patient than yours (compare gender/age).
- Do not use this criterion for variants where BS1 is applied or where PM2 does not apply.

| Strength | Criteria |
|----------|----------|
| **PS4** (Strong) | 5+ observations. *(Modification type: Strength)* |
| **PS4_Moderate** | 3-4 observations. *(Modification type: Strength)* |
| **PS4_Supporting** | Use for 2nd independent occurrence. *(Modification type: Strength)* |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **PM1** (Moderate) | Located in a mutational hot spot and/or critical and well-established functional domain: 3' cysteine binding site: aa 820 (PMID 9887341). *(Modification type: Disease-specific)* |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **PM2_Supporting** | Absent/rare from controls in an ethnically-matched cohort population sample. Use if absent, zero observations in control databases. *(Modification type: Strength)* |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **PM4_Strong** | Protein length changes due to stop-loss variants. PM4_Strong is applicable to stop-loss variants in UBE3A, as several stop loss variants in this gene has been described in affected individuals (PMID 25212744). *(Modification type: Disease-specific)* |
| **PM4** (Moderate) | Protein length changes due to in-frame deletions/insertions in a non-repeat region. *(Modification type: Disease-specific)* |
| **PM4_Supporting** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. Smaller in-frame events (< 3 amino acid residues) unless they occur in a functionally important region (see PM1 for functionally important domain for this gene). *(Modification type: Strength)* |

*Note: "as several stop loss variants in this gene has been described" reproduces the grammatical error present in the source specification.*

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **PM5_Strong** | Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. ≥2 different missense changes affecting the amino acid residue. Do not apply PM1 in these situations. *(Modification type: Strength)* |
| **PM5** (Moderate) | Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. A Grantham or BLOSUM score comparison can be used to determine if the variant is predicted to be as or more damaging than the established pathogenic variant. *(Modification type: None)* |
| **PM5_Supporting** | Not specified by VCEP |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

#### VCEP Specifications

Because of the very high de novo rate of pathogenic variants in *UBE3A*, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

| Strength | Criteria |
|----------|----------|
| **PM6_VeryStrong** | Assumed de novo without confirmation of paternity and maternity. ≥4 independent occurrences of PM6. Evidence from literature must be fully evaluated to support independent events. *(Modification type: Strength)* |
| **PM6_Strong** | Assumed de novo without confirmation of paternity and maternity. ≥2 independent occurrences of PM6. Evidence from literature must be fully evaluated to support independent events. *(Modification type: Strength)* |
| **PM6** (Moderate) | Assumed de novo without confirmation of paternity and maternity. 1 occurrence of PM6. *(Modification type: None)* |
| **PM6_Supporting** | Not specified by VCEP |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

#### VCEP Specifications

Note: individuals must have disease consistent with reported phenotype (even if on the mild end of spectrum of the disease).

| Strength | Criteria |
|----------|----------|
| **PP1_Strong** | Co-segregation with disease in multiple affected family members. ≥5 informative meiosis. *(Modification type: Strength)* |
| **PP1_Moderate** | Co-segregation with disease in multiple affected family members. 3-4 informative meiosis. *(Modification type: Strength)* |
| **PP1** (Supporting) | Co-segregation with disease in multiple affected family members. 2 informative meiosis. *(Modification type: Strength)* |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **PP3** (Supporting) | Multiple lines of computational evidence support a deleterious effect on the gene or gene product. For missense variants use REVEL with a score ≥ 0.644. For splice site variants use SpliceAI with a score ≥ 0.2. *(Modification type: General recommendation)* |

Reference for computational tool calibration: Pejaver V, Byrne AB et al., *Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria*, Am J Hum Genet (2022), PMID 36413997.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **PP4** (Supporting) | Phenotype specific for disease with single genetic etiology. See gene specific clinical phenotype guidelines. *(Modification type: Disease-specific)* |

#### UBE3A Clinical Phenotype Guidelines

**Mandatory criterion:**
- Severe ID (if 5 years of age or older) or global developmental delay (if <5 years of age)

**In addition, the patient has to satisfy at least 4/5 of the following:**
- Ataxia/jerky movements
- Characteristic EEG
- Seizures
- Absent speech or less than 5 words (if at least 4 years of age)
- Frequent smiling

**Additional notes:** If information is provided such that a phenotype of Angelman syndrome is suspected, with specific minimal features used for the diagnosis, then this can be used for PP4 in lieu of the specific clinical features listed.

*Note: This VCEP does not use a point-based PP4 system; PP4 is available at Supporting strength only.*

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

#### VCEP Specifications

The frequency cutoffs are based on MECP2 expected disease allele frequency (1 in 10,000 for the disease prevalence / (1.5 alleles [assumes 50/50 male/female ratio] * 0.8 for 80% penetrance)). MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

| Strength | Criteria |
|----------|----------|
| **BA1** (Stand Alone) | Use large population databases (i.e. gnomAD). Use if variant is present at **≥0.000083 (0.0083%)** in any sub-population. Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles. *(Modification type: Disease-specific)* |

*Note: The parentheses in the frequency rationale sentence are unbalanced as published in the source specification; reproduced verbatim above.*

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### VCEP Specifications

The frequency cutoffs are based on MECP2 expected disease allele frequency divided by 10-fold. MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

| Strength | Criteria |
|----------|----------|
| **BS1** (Strong) | Use large population databases (i.e. gnomAD). Use if variant is present at **≥0.0000083 (0.00083%) and <0.000083 (0.0083%)** in any sub-population. Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles. *(Modification type: Disease-specific)* |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

#### VCEP Specifications

- Should be applied in cases where the healthy adult is devoid of neurodevelopmental phenotypes.
- Best to use with internal curated data that includes clinical information or published patients that have been phenotyped.

| Strength | Criteria |
|----------|----------|
| **BS2** (Strong) | Observed in the heterozygous/hemizygous state in a healthy adult. 4 unaffected (related and maternally inherited or unrelated) heterozygotes. *(Modification type: Strength)* |
| **BS2_Supporting** | Observed in the heterozygous/hemizygous state in a healthy adult. 2 unaffected (related and maternally inherited or unrelated) heterozygotes. *(Modification type: Strength)* |

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **BS3** (Strong) | Well-established in vitro or in vivo functional studies shows no damaging effect on protein function. RNA functional studies that demonstrate no impact on splicing and transcript composition. It can be downgraded based on quality of data. Not applicable for other functional studies. *(Modification type: Disease-specific)* |

Note: In the UBE3A Functional Assays table, BS3 is listed as "Not recommended" for all three protein-level assays (E3 ubiquitin ligase activity, UBE3A protein expression, UBE3A nuclear localization).

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

#### VCEP Specifications

Need to confirm that the family member is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.

| Strength | Criteria |
|----------|----------|
| **BS4** (Strong) | Lack of segregation in affected members of a family. Absent in a similarly affected family member, when seen in two or more families. *(Modification type: Strength)* |
| **BS4_Supporting** | Lack of segregation in affected members of a family. Absent in a similarly affected family member. *(Modification type: Strength)* |

---

### BP2 - In Trans / In Cis with Pathogenic Variant

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

#### VCEP Specifications

Knock out of *UBE3A* results in disease but viable phenotype (PMID 9808466).

| Strength | Criteria |
|----------|----------|
| **BP2** (Supporting) | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder; or observed in cis with a pathogenic variant in any inheritance pattern. BP2 is not applicable for UBE3A *in trans* state. *(Modification type: Disease-specific)* |

---

### BP3 - In-frame Indel in Repetitive Region

**Original ACMG Summary:** In frame-deletions/insertions in a repetitive region without a known function.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **BP3** (Supporting) | In-frame deletions/insertions in a repetitive region without a known function. BP3 is applicable if there are in-frame deletions/duplications in a repetitive region where other in-frame deletions/duplications have been observed with an overall frequency commensurate with the BA1 threshold for this gene. *(Modification type: None)* |

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **BP4** (Supporting) | Multiple lines of computational evidence suggest no impact on gene or gene product. For missense variants use REVEL with a score ≤ 0.290. For splice site variants use SpliceAI with a score ≤ 0.1. *(Modification type: None)* |

---

### BP5 - Alternate Molecular Basis for Disease

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

#### VCEP Specifications

- For example if a variant in *UBE3A* is identified in a patient with lissencephaly in whom a pathogenic variant is identified in the *PAFAH1B1* gene.
- Variant should also be maternally inherited in the case with an alternate molecular basis for disease for this criteria to be used.
- Do not apply if variant is de novo.

| Strength | Criteria |
|----------|----------|
| **BP5_Strong** | Variant found in a case with an alternate molecular basis for disease. ≥3 cases with alternate molecular basis for disease. *(Modification type: Strength)* |
| **BP5** (Supporting) | Variant found in a case with an alternate molecular basis for disease. 1 case with alternate molecular basis for disease. *(Modification type: Disease-specific)* |

---

### BP7 - Synonymous (Silent) Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

#### VCEP Specifications

For silent variants BP4 and BP7 can be added.

| Strength | Criteria |
|----------|----------|
| **BP7** (Supporting) | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. Defined 'not highly conserved' regions in BP7 as those with PhastCons score <1 and/or PhyloP score <0.1 and/or the variant is the reference nucleotide in one primate and/or three mammal species. For splice site variants use SpliceAI with a score ≤ 0.1. *(Modification type: None)* |

---

## 4. Not Applicable Criteria

| Criterion | Original Purpose | Reason Not Applicable |
|-----------|-----------------|----------------------|
| **PM3** | For recessive disorders, detected in trans with a pathogenic variant | Not applicable for UBE3A. |
| **PP2** | Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease | Not applicable for UBE3A. |
| **PP5** | Reputable source recently reports variant as pathogenic | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP1** | Missense variant in a gene for which primarily truncating variants are known to cause disease | Not applicable for UBE3A. |
| **BP6** | Reputable source recently reports variant as benign | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |

---

## 5. Rules for Combining Criteria

### Pathogenic Classification

| Combination |
|-------------|
| 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) **AND** ≥1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) **AND** ≥2 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) **AND** 1 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** 1 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4) |
| 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4) |
| ≥2 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** ≥3 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong **AND** 2 Moderate **AND** ≥2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** ≥4 Supporting |

### Likely Pathogenic Classification

| Combination |
|-------------|
| 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) **AND** 1 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 1 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4) |
| ≥3 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 2 Moderate **AND** ≥2 Supporting |
| 1 Moderate **AND** ≥4 Supporting |
| 1 Strong **AND** 2 Moderate |

### Benign Classification

| Combination |
|-------------|
| ≥2 Strong (BS1, BS2, BS3, BS4, BP5_Strong) |
| 1 Stand Alone (BA1) |
| 1 Strong (BS1, BS2, BS3, BS4, BP5_Strong) **AND** 3 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP3, BP4, BP5, BP7) |

### Likely Benign Classification

| Combination |
|-------------|
| ≥2 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP3, BP4, BP5, BP7) |
| 1 Strong (BS1, BS2, BS3, BS4, BP5_Strong) |

### Variant of Uncertain Significance (VUS)

- Criteria for benign and pathogenic are contradictory
- No criteria met
- Criteria met do not reach threshold for Likely Benign or Likely Pathogenic

---

## 6. Appendices

### Appendix A: PVS1 Flowchart for UBE3A (NM_130838.2)

#### Nonsense or Frameshift Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| Predicted to undergo NMD + exon is present in biologically-relevant transcript(s) | **PVS1** |
| Predicted to undergo NMD + exon is absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD + upstream of the most distal de novo LOF variant (p.K841); frameshift that results in a read-through of the stop codon | **PVS1** |
| Not predicted to undergo NMD + downstream of the most distal de novo LOF variant (p.K841) but does not result in a read-through of the stop codon | **PVS1_Strong** |
| Not predicted to undergo NMD + downstream of the most distal de novo non-truncating variant (p.G850) but does not result in a read-through of the stop codon | **PVS1_Moderate** |

#### GT-AG ±1,2 Splice Site Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD + exon is present in biologically-relevant transcript(s) | **PVS1** |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD + exon is absent from biologically-relevant transcript(s) | N/A |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD (Exon 11) + truncated/altered region is critical to protein function (Exon 11) | **PVS1** |
| Exon skipping or use of a cryptic splice site preserves reading frame (Exons 7, 8) + LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) (Exons 7, 8) | **PVS1_Strong** |

#### Deletions (Single Exon to Full Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Full gene deletion | **PVS1** |
| Single to multi exon deletion – disrupts reading frame and is predicted to undergo NMD + exon is present in biologically-relevant transcript(s) | **PVS1** |
| Single to multi exon deletion – disrupts reading frame and is predicted to undergo NMD + exon is absent from biologically-relevant transcript(s) | N/A |
| Single to multi exon deletion – disrupts reading frame and is NOT predicted to undergo NMD (Exon 11) + truncated/altered region is critical to protein function (Exon 11) | **PVS1** |
| Single to multi exon deletion – preserves reading frame (single exon 7 or 8 deletion; other in-frame combinations) + role of region in protein function is unknown + LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) + variant removes >10% of protein | **PVS1** |
| Single to multi exon deletion – preserves reading frame + role of region in protein function is unknown + LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) + variant removes <10% of protein (Exon 7) | **PVS1_Strong** |
| Single to multi exon deletion – preserves reading frame + truncated/altered region is critical to protein function (Exon 8 + any in-frame combination that includes the PM1 functional domain p.C820) | **PVS1** |

#### Duplications (≥1 exon in size, must be completely contained within gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Proven in tandem + reading frame disrupted and NMD predicted to occur | **PVS1** |
| Proven in tandem / presumed in tandem + no or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem + reading frame presumed disrupted and NMD predicted to occur | **PVS1_Strong** |
| Proven not in tandem | N/A |

#### Initiation Codon Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| No known alternative start codon in other medically relevant transcripts + initiation codon variant described in at least one affected individual with Angelman syndrome | **PVS1** |

---

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold (gnomAD, any sub-population) | Strength |
|-----------|----------------------------------------|----------|
| BA1 | ≥0.000083 (0.0083%) | Stand Alone |
| BS1 | ≥0.0000083 (0.00083%) and <0.000083 (0.0083%) | Strong |
| PM2 | Absent, zero observations in control databases | Supporting |

Allele frequency thresholds require the frequency to be met in any general continental population dataset of at least 2,000 observed alleles.

---

### Appendix C: In Silico Thresholds Summary

| Criterion | Tool | Threshold |
|-----------|------|-----------|
| PP3 (missense) | REVEL | ≥ 0.644 |
| PP3 (splice site) | SpliceAI | ≥ 0.2 |
| BP4 (missense) | REVEL | ≤ 0.290 |
| BP4 (splice site) | SpliceAI | ≤ 0.1 |
| BP7 (splice site) | SpliceAI | ≤ 0.1 |
| BP7 (conservation) | PhastCons / PhyloP | PhastCons <1 and/or PhyloP <0.1 and/or reference nucleotide in one primate and/or three mammal species |

---

### Appendix D: References (from specification)

| # | Citation | PMID |
|---|----------|------|
| 1 | Bienvenu T, Carrié A et al. MECP2 mutations account for most cases of typical forms of Rett syndrome. Hum Mol Genet (2000) 9 (9) p. 1377-84. | 10814719 |
| 2 | Erlandson A, Hallberg B et al. MECP2 mutation screening in Swedish classical Rett syndrome females. Eur Child Adolesc Psychiatry (2001) 10 (2) p. 117-21. | 11469283 |
| 3 | Fang P, Lev-Lehman E et al. The spectrum of mutations in UBE3A causing Angelman syndrome. Hum Mol Genet (1999) 8 (1) p. 129-35. | 9887341 |
| 4 | Sadikovic B, Fernandes P et al. Mutation Update for UBE3A variants in Angelman syndrome. Hum Mutat (2014) 35 (12) p. 1407-17. | 25212744 |
| 5 | Jiang YH, Armstrong D et al. Mutation of the Angelman ubiquitin ligase in mice causes increased cytoplasmic p53 and deficits of contextual learning and long-term potentiation. Neuron (1998) 21 (4) p. 799-811. | 9808466 |
| 6 | Pejaver V, Byrne AB et al. Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria. Am J Hum Genet (2022) 109 (12) p. 2163-2177. | 36413997 |

Additional PMIDs cited in the specification and supplementary files: 30192042 (ClinGen SVI PVS1 recommendations), 29543229 (ClinGen SVI VCEP Review Committee, PP5/BP6), 15263005, 26255772, 31235931, 33607653 (functional assays).

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 7.0 | May 1, 2026 | 1 Strong AND 3 Supporting added to benign criteria code. 1 Strong added to likely benign criteria code. |

---

*This document is based on the ClinGen Rett and Angelman-like Disorders Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for UBE3A Version 7.0 (DOI: 10.5281/zenodo.21421718).*
