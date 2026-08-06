# Comprehensive Variant Interpretation Guidelines for MECP2

## ClinGen Rett and Angelman-like Disorders VCEP Specifications for MECP2 (Version 6.0)

**Affiliation:** Rett and Angelman-like Disorders VCEP
**Version:** 6.0
**Release Date:** May 1, 2026
**DOI:** 10.5281/zenodo.21421705
**Based on:** Richards et al., 2015 - ACMG/AMP Variant Interpretation Guidelines (Combining rules)

**Release Notes (v6.0):** 1 Strong AND 3 Supporting added to benign criteria code. 1 Strong added to likely benign criteria code.

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
   - [BP2 - In Trans with Pathogenic Variant](#bp2---in-trans-with-pathogenic-variant)
   - [BP3 - In-Frame Indels in Repetitive Region](#bp3---in-frame-indels-in-repetitive-region)
   - [BP4 - Computational Evidence (Benign)](#bp4---computational-evidence-benign)
   - [BP5 - Alternate Molecular Basis](#bp5---alternate-molecular-basis)
   - [BP7 - Synonymous Variants](#bp7---synonymous-variants)
4. [Not Applicable Criteria](#4-not-applicable-criteria)
5. [Rules for Combining Criteria](#5-rules-for-combining-criteria)
6. [Appendices](#6-appendices)

---

## 1. Gene and Disease Information

| Parameter | Value |
|-----------|-------|
| **Gene** | MECP2 (HGNC:6990) |
| **HGNC Name** | methyl-CpG binding protein 2 |
| **Reference Transcript** | NM_004992.3 |
| **Disease** | Rett syndrome |
| **MONDO ID** | MONDO:0010726 |
| **Mode of Inheritance** | X-linked inheritance |

**Keywords (from specification):** human biology, genomics, variant, variant classification, clingen, disease standards, MECP2, NM_004992.3, X-linked inheritance, Rett syndrome

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

#### General Caveats

- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

#### VCEP Specifications

Initiation codon variants are not applicable due to the MECP2E1 alternative isoform that excludes exon 1 with an alterante start codon. *[sic — "alterante" appears as such in the source specification]*

For intragenic deletions/duplications that are predicted to result in a product that preserves reading frame:

- For single exon in-frame deletions, assign the same strength (PVS1 or PVS1_moderate) as for splice site variants that preserve reading frame indicated above.
- For multiple exon in-frame deletions, PVS1 can be assigned to deletions that include single in-frame exons in the PVS1 category listed in the splice site section above OR if the exon contains a functionally important domain as specified in PM1.
- Given the extensive data available for MECP2, classifications for single or multi-exon in-frame deletions are assigned as PVS1 or PVS1_strong. Refer to PVS1 flow chart for additional guidance.

#### Strength Levels

| Strength | Application |
|----------|-------------|
| **PVS1** (Very Strong) | Null variant in a gene where loss of function is a known mechanism of disease. Use as defined by ClinGen SVI working group (PMID: 30192042). PVS1 is applicable for: null variants up to p.E472; any frameshift variant that results in a read-through of the stop codon; canonical splice site variants predicted to result in an out-of-frame product; canonical splice site variants or single in-frame deletions predicted to preserve the reading frame (exon 3); a full gene deletion. PVS1 is **not** applicable for initiation codons. *(Modification type: Disease-specific)* |
| **PVS1_Strong** | Canonical splice site variants or deletions (single exon to full gene deletion) resulting in exon skipping or use of a cryptic splice site that disrupts reading frame and is **NOT** predicted to undergo NMD, but the truncated/altered region is critical to protein function (exon 4). *(Modification type: Disease-specific, Strength)* |
| **PVS1_Moderate** | Applicable for any truncating variant distal of p.E472. *(Modification type: Disease-specific, Strength)* |
| **PVS1_Supporting** | Not specified by VCEP |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PS1** (Strong) | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. *(Modification type: None)* |
| **PS1_Moderate** | Not specified by VCEP |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### VCEP Specifications

Applicable to all genes in affected individuals identified as mosaic for the variant (as the presence of a variant in the mosaic state is confirmatory of the variant being de novo). Because of the very high de novo rate of pathogenic variants in MECP2, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

#### Strength Levels

| Strength | Application |
|----------|-------------|
| **PS2_VeryStrong** | De novo (maternity and paternity confirmed) in a patient with the disease and no family history: ≥2 independent occurrences of PS2, **or** ≥2 independent occurrences of PM6 and one occurrence of PS2. *(Modification type: None)* |
| **PS2** (Strong) | De novo (maternity and paternity confirmed) in a patient with the disease and no family history: 1 occurrence of PS2. *(Modification type: None)* |
| **PS2_Moderate / PS2_Supporting** | Not specified by VCEP |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PS3** (Strong) | Well-established in vitro or in vivo functional studies supportive of a damaging effect. RNA studies that demonstrate abnormal splicing and an out-offrame transcript. Do not use for canonical splice site variants and when PVS1 is used. *(Modification type: Disease-specific)* *[sic — "out-offrame" appears as such in the source specification]* |
| **PS3_Moderate** | Not specified by VCEP |
| **PS3_Supporting** | Well-established in vitro or in vivo functional studies supportive of a damaging effect. RNA studies that demonstrate abnormal splicing and an inframe product (unless it affects an in-frame exon specified in the PVS1 section). See included table for approved functional studies. *(Modification type: Disease-specific)* |

#### Approved Functional Assays (MECP2 Functional Assays supplementary file)

| Name of assay | Measured Parameter | Expected Deleterious Result Range (PS3_Supporting) | Expected Benign Result Range (BS3) | References |
|---------------|--------------------|-----------------------------------------------------|-------------------------------------|------------|
| MECP2 chromatin binding assay | Localization of MECP2 to highly methylated heterochromatic loci by quantitative immunofluorescence assay (MECP2 and DAPI co-localization) | MECP2 is distributed diffusely (no clustering pattern) | Not recommended | PMID: 27929079, 23770565, 29718204 |
| MECP2 in vitro binding assay | Association of MECP2 with NCoR/SMRT co-repressors | Abolished interaction by co-immunoprecipitation assay | Not recommended | PMID: 23770565, 29718204 |
| In vitro transcription repression assay | Luciferase activity in cell lysates co-expressing target reporters and wt or mutant MECP2 effector proteins | Abolished transcription repression activity in cells transfected with the effector construct expressing mutant MECP2 compared to constructs expressing wild type MECP2 | Not recommended | PMID: 23452848 |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

- **Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
- **Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

#### VCEP Specifications

- Detailed phenotype not needed. Need to confirm patient is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.
- Patient can be published OR an internal case OR observed at an outside lab (i.e. via ClinVar) OR described in the reputable databases (RettBASE). However, independent case has to be confirmed to be a different patient than yours (compare gender/age).
- Do not use this criterion for variants where BS1 is applied or where PM2 does not apply.

| Strength | Application |
|----------|-------------|
| **PS4** (Strong) | 5+ observations. *(Modification type: Strength)* |
| **PS4_Moderate** | 3-4 observations. *(Modification type: Strength)* |
| **PS4_Supporting** | Use for 2nd independent occurrence. *(Modification type: Strength)* |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PM1** (Moderate) | Located in a mutational hot spot and/or critical and well-established functional domain: Methyl-DNA binding (MBD): aa 90-162; Transcriptional repression domain (TRD): aa 302-306. *(Modification type: Disease-specific)* |

**Note:** Do not apply PM1 in situations where PM5_Strong is applied (see PM5).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **PM2_Supporting** | Absent/rare from controls in an ethnically-matched cohort population sample. Use if absent, zero observations in control databases. *(Modification type: Strength)* |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PM4_Strong** | Protein length changes due to stop-loss variants. PM4_Strong is applicable to stop-loss variants in *MECP2*, as several stop loss variants in this gene has been described in affected individuals (reference 2: Erlandson A Hallberg B et al., PMID 11469283). *(Modification type: Disease-specific)* |
| **PM4** (Moderate) | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. Do not use PM4 for in-frame deletions/insertions in the Proline-rich region of gene (p.381-p.405). *(Modification type: Disease-specific)* |
| **PM4_Supporting** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. Smaller in-frame events (< 3 amino acid residues) unless they occur in a functionally important region (see PM1 for functionally important domains for each gene). *(Modification type: Strength)* |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PM5_Strong** | Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before: ≥2 different missense changes affecting the amino acid residue. Do not apply PM1 in these situations. *(Modification type: Strength)* |
| **PM5** (Moderate) | Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. A Grantham or BLOSUM score comparison can be used to determine if the variant is predicted to be as or more damaging than the established pathogenic variant. *(Modification type: None)* |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

#### VCEP Specifications

Because of the very high de novo rate of pathogenic variants in MECP2, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

| Strength | Application |
|----------|-------------|
| **PM6_VeryStrong** | Confirmed de novo without confirmation of paternity and maternity: ≥4 independent occurrences of PM6. Evidence from literature must be fully evaluated to support independent events. *(Modification type: Strength)* |
| **PM6_Strong** | Confirmed de novo without confirmation of paternity and maternity: ≥2 independent occurrences of PM6. Evidence from literature must be fully evaluated to support independent events. *(Modification type: Strength)* |
| **PM6** (Moderate) | Confirmed de novo without confirmation of paternity and maternity: 1 occurrence of PM6. *(Modification type: None)* |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

#### VCEP Specifications

**Note:** Individuals must have disease consistent with reported phenotype (even if on the mild end of spectrum of the disease).

| Strength | Application |
|----------|-------------|
| **PP1_Strong** | Co-segregation with disease in multiple affected family members: ≥5 informative meiosis. *(Modification type: Strength)* |
| **PP1_Moderate** | Co-segregation with disease in multiple affected family members: 3-4 informative meiosis. *(Modification type: Strength)* |
| **PP1** (Supporting) | Co-segregation with disease in multiple affected family members: 2 informative meiosis. *(Modification type: Strength)* |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **PP3** (Supporting) | Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). For missense variants use REVEL with a score ≥ 0.644. For splice site variants use SpliceAI with a score ≥ 0.2. *(Modification type: General recommendation)* |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **PP4** (Supporting) | Phenotype specific for disease with single genetic etiology. See gene specific clinical phenotype guidelines. *(Modification type: Disease-specific)* |

#### MECP2 Clinical Phenotype Guidelines

**Core phenotype (need to be met for PP4)**

- Regression of developmental progress and loss of at least 2 of 4 of following
- Loss, partial or complete of fine motor skills (hand use)
- Loss, partial or complete of spoken communication
- Abnormal (dyspraxic) or absent gait
- Stereotypies

**Supportive Criteria** (do not need to be met for PP4, however in the absence of one core phenotype, two or more supportive phenotypes can be used in its place)

- Periodic breathing (breath-holding/hyperventilation) when awake
- Bruxism when awake
- Impaired sleep pattern
- Abnormal muscle tone
- Peripheral vasomotor disturbances
- Scoliosis/kyphosis
- Growth retardation (small stature)
- Small, cold hands and feet
- Inappropriate laughing/screaming spells
- Diminished response to pain
- Intense eye communication ("eye pointing")

**Additional notes:** If information is provided such that a phenotype of Rett syndrome is suspected, with specific minimal features used for the diagnosis, then this can be used for PP4 in lieu of the specific clinical features listed.

**Note:** No PP4 point system is specified by this VCEP; PP4 is applied at Supporting strength only.

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

#### VCEP Specifications

The frequency cutoffs are based on MECP2 expected disease allele frequency (1 in 10,000 for the disease prevalence / (1.5 alleles [assumes 50/50 male/female ratio] * 0.8 for 80% penetrance)). MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

| Strength | Threshold |
|----------|-----------|
| **BA1** (Stand Alone) | Use large population databases (i.e. gnomAD). Use if variant is present at **≥0.000083 (0.0083%)** in any sub-population. Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles. *(Modification type: Disease-specific)* |

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### VCEP Specifications

The frequency cutoffs are based on MECP2 expected disease allele frequency divided by 10-fold. MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

| Strength | Threshold |
|----------|-----------|
| **BS1** (Strong) | Use large population databases (i.e. gnomAD). Use if variant is present at **≥0.0000083 (0.00083%)** and **<0.000083 (0.0083%)** in any sub-population. Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles. *(Modification type: Disease-specific)* |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

#### VCEP Specifications

- Should be applied in cases where the healthy adult is devoid of neurodevelopmental phenotypes.
- Best to use with internal curated data that includes clinical information or published patients that have been phenotyped.

| Strength | Application |
|----------|-------------|
| **BS2** (Strong) | Observed in the heterozygous/hemizygous state in a healthy adult: 2 unaffected (related or unrelated) heterozygotes or hemizygotes. *(Modification type: Strength)* |
| **BS2_Supporting** | Observed in the heterozygous/hemizygous state in a healthy adult: 1 unaffected (related or unrelated) heterozygote or hemizygote. *(Modification type: Strength)* |

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

#### VCEP Specification

| Strength | Application |
|----------|-------------|
| **BS3** (Strong) | Well-established in vitro or in vivo functional studies shows no damaging effect on protein function. RNA functional studies that demonstrate no impact on splicing and transcript composition. It can be downgraded based on quality of data. Not applicable for other functional studies. *(Modification type: Disease-specific)* |

**Note:** For all three approved protein-level functional assays (chromatin binding, in vitro binding, in vitro transcription repression), the "Expected Benign Result Range (BS3)" is listed as **Not recommended** in the MECP2 Functional Assays table.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

#### VCEP Specifications

Need to confirm that the family member is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.

| Strength | Application |
|----------|-------------|
| **BS4** (Strong) | Lack of segregation in affected members of a family: absent in a similarly affected family member, when seen in two or more families. *(Modification type: Strength)* |
| **BS4_Supporting** | Lack of segregation in affected members of a family: absent in a similarly affected family member. *(Modification type: Strength)* |

---

### BP2 - In Trans with Pathogenic Variant

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

#### VCEP Specifications

Knock out of MECP2 results in embryonic lethality/drastic phenotype (reference 1: Guy J Hendrich B et al., PMID 11242117).

| Strength | Application |
|----------|-------------|
| **BP2** (Supporting) | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder. *(Modification type: Disease-specific)* |

---

### BP3 - In-Frame Indels in Repetitive Region

**Original ACMG Summary:** In frame-deletions/insertions in a repetitive region without a known function.

| Strength | Application |
|----------|-------------|
| **BP3** (Supporting) | In-frame deletions/insertions in a repetitive region without a known function. BP3 is applicable if there are in-frame deletions/duplications in a repetitive region where other in-frame deletions/duplications have been observed with an overall frequency commensurate with the BA1 threshold for this gene. *(Modification type: None)* |

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

| Strength | Application |
|----------|-------------|
| **BP4** (Supporting) | Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc). For missense variants use REVEL with a score ≤ 0.290. For splice site variants use SpliceAI with a score ≤ 0.1. *(Modification type: None)* |

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

#### VCEP Specifications

- For example, if a variant in MECP2 is identified in a patient with lissencephaly in whom a pathogenic variant is identified in the PAFAH1B1 gene.
- Do **not** apply if variant is de novo.

| Strength | Application |
|----------|-------------|
| **BP5_Strong** | Variant found in a case with an alternate molecular basis for disease: ≥3 cases with alternate molecular basis for disease. *(Modification type: Strength)* |
| **BP5** (Supporting) | Variant found in a case with an alternate molecular basis for disease: 1 case with alternate molecular basis for disease. *(Modification type: Disease-specific)* |

**Note:** The specification does not define a strength for exactly 2 cases with an alternate molecular basis for disease.

---

### BP7 - Synonymous Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

#### VCEP Specifications

For silent variants BP4 and BP7 can be added.

| Strength | Application |
|----------|-------------|
| **BP7** (Supporting) | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. Defined 'not highly conserved' regions in BP7 as those with PhastCons score <1 and/or PhyloP score <0.1 and/or the variant is the reference nucleotide in one primate and/or three mammal species. For splice site variants use SpliceAI with a score ≤ 0.1. *(Modification type: None)* |

---

## 4. Not Applicable Criteria

| Criterion | Original Purpose | Reason Not Applicable |
|-----------|-----------------|----------------------|
| **PM3** | For recessive disorders, detected in trans with a pathogenic variant | Not applicable for MECP2. |
| **PP2** | Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease | Not applicable for MECP2. |
| **PP5** | Reputable source recently reports variant as pathogenic | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP1** | Missense variant in a gene for which primarily truncating variants are known to cause disease | Not applicable for MECP2. |
| **BP6** | Reputable source recently reports variant as benign | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |

---

## 5. Rules for Combining Criteria

### Pathogenic Classification

| Combination |
|-------------|
| 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) **AND** ≥ 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) **AND** ≥ 2 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) **AND** 1 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** 1 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4) |
| 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) **AND** ≥ 2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4) |
| ≥ 2 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** ≥ 3 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong **AND** 2 Moderate **AND** ≥ 2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** ≥ 4 Supporting |

### Likely Pathogenic Classification

| Combination |
|-------------|
| 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) **AND** 1 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 1 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong **AND** ≥ 2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4) |
| ≥ 3 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 2 Moderate **AND** ≥ 2 Supporting |
| 1 Moderate **AND** ≥ 4 Supporting |
| 1 Strong **AND** 2 Moderate |

### Benign Classification

| Combination |
|-------------|
| ≥ 2 Strong (BS1, BS2, BS3, BS4, BP5_Strong) |
| 1 Stand Alone (BA1) |
| 1 Strong (BS1, BS2, BS3, BS4, BP5_Strong) **AND** 3 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP3, BP4, BP5, BP7) |

### Likely Benign Classification

| Combination |
|-------------|
| ≥ 2 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP3, BP4, BP5, BP7) |
| 1 Strong (BS1, BS2, BS3, BS4, BP5_Strong) |

---

## 6. Appendices

### Appendix A: PVS1 Flowchart for MECP2 (NM_004992.3)

#### Nonsense or Frameshift Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| Predicted to undergo NMD + Exon is present in biologically-relevant transcript(s) | **PVS1** |
| Predicted to undergo NMD + Exon is absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD + Upstream of most distal de novo LOF variant (p.E472) OR a frameshift variant that results in a read-through of the stop codon | **PVS1** |
| Not predicted to undergo NMD + Downstream of most distal de novo LOF variant (p.E472) | **PVS1_Moderate** |

#### GT-AG ±1,2 Splice Site Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD + Exon is present in biologically-relevant transcript(s) | **PVS1** |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD + Exon is absent from biologically-relevant transcript(s) | N/A |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD (Exon 4) + Truncated/altered region is critical to protein function (Exon 4) | **PVS1_Strong** |
| Exon skipping or use of a cryptic splice site preserves reading frame (Exon 3) + Truncated/altered region is critical to protein function (Exon 3) | **PVS1** |

#### Deletions (Single Exon to Full Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Full gene deletion | **PVS1** |
| Single to multi exon deletion – disrupts reading frame and is predicted to undergo NMD + Exon is present in biologically-relevant transcript(s) | **PVS1** |
| Single to multi exon deletion – disrupts reading frame and is predicted to undergo NMD + Exon is absent from biologically-relevant transcript(s) | N/A |
| Single to multi exon deletion – disrupts reading frame and is NOT predicted to undergo NMD (Exon 4) + Truncated/altered region is critical to protein function (Exon 4) | **PVS1_Strong** |
| Single to multi exon deletion – preserves reading frame (Exon 3) + Truncated/altered region is critical to protein function (Exon 3) | **PVS1** |

#### Duplications (≥1 Exon in Size, Must Be Completely Contained Within Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Proven in tandem + Reading frame disrupted and NMD predicted to occur | **PVS1** |
| Proven in tandem / Presumed in tandem + No or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem + Reading frame presumed disrupted and NMD predicted to occur | **PVS1_Strong** |
| Proven not in tandem | N/A |

#### Initiation Codon

| Condition | PVS1 Strength |
|-----------|---------------|
| Different functional transcript (MECP2E1) uses alternative start codon | N/A |

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.000083 (0.0083%) in any sub-population | Stand Alone |
| BS1 | ≥0.0000083 (0.00083%) and <0.000083 (0.0083%) in any sub-population | Strong |
| PM2_Supporting | Absent; zero observations in control databases | Supporting |

Both BA1 and BS1 require that the allele frequency is met in any general continental population dataset of at least 2,000 observed alleles.

### Appendix C: In Silico Thresholds Summary

| Criterion | Tool | Threshold |
|-----------|------|-----------|
| PP3 (missense) | REVEL | ≥ 0.644 |
| PP3 (splice site) | SpliceAI | ≥ 0.2 |
| BP4 (missense) | REVEL | ≤ 0.290 |
| BP4 (splice site) | SpliceAI | ≤ 0.1 |
| BP7 (splice site) | SpliceAI | ≤ 0.1 |
| BP7 (conservation) | PhastCons / PhyloP | PhastCons <1 and/or PhyloP <0.1 and/or variant is reference nucleotide in one primate and/or three mammal species |

### Appendix D: References (from specification)

| # | Citation | Journal / Year | PMID |
|---|----------|----------------|------|
| 1 | Guy J, Hendrich B et al. A mouse Mecp2-null mutation causes neurological symptoms that mimic Rett syndrome. | Nat Genet (2001) 27(3) p. 322-6. 10.1038/85899 | 11242117 |
| 2 | Erlandson A, Hallberg B et al. MECP2 mutation screening in Swedish classical Rett syndrome females. | Eur Child Adolesc Psychiatry (2001) 10(2) p. 117-21. 10.1007/s007870170034 | 11469283 |
| 3 | Pejaver V, Byrne AB et al. Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria. | Am J Hum Genet (2022) 109(12) p. 2163-2177. 10.1016/j.ajhg.2022.10.013 | 36413997 |

Additional PMIDs cited within criteria: 30192042 (ClinGen SVI PVS1 recommendations, PVS1), 29543229 (ClinGen SVI VCEP Review Committee, PP5/BP6).

Functional assay PMIDs: 27929079, 23770565, 29718204 (chromatin binding; in vitro binding), 23452848 (in vitro transcription repression).

### Appendix E: Source Documents

| File | Content |
|------|---------|
| ClinGen_ACMG_Specifications_MECP2_v6.0.pdf | Main criteria specification |
| PVS1 Flowchart for MECP2.pdf | PVS1 decision flowchart |
| Clinical Phenotype Guidelines for MECP2.pdf | Phenotype guidelines referenced by PP4 |
| MECP2 Functional Assays.xlsx | Approved functional assays for PS3/BS3 |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 6.0 | May 1, 2026 | 1 Strong AND 3 Supporting added to benign criteria code. 1 Strong added to likely benign criteria code. |

---

*This document is based on the ClinGen Rett and Angelman-like Disorders Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for MECP2 Version 6.0 (DOI: 10.5281/zenodo.21421705). Source: https://cspec.genome.network/cspec/ui/svi/doc/GN036*
