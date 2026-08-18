# Comprehensive Variant Interpretation Guidelines for SLC9A6

## ClinGen Rett and Angelman-like Disorders VCEP Specifications for SLC9A6 (Version 6.0)

**Affiliation:** Rett and Angelman-like Disorders Variant Curation Expert Panel (Rett and Angelman-like Disorders VCEP)
**Version:** 6.0
**Release Date:** May 1, 2026
**DOI:** 10.5281/zenodo.21421661
**Based on:** Richards et al., 2015 - ACMG/AMP Variant Interpretation Guidelines (Combining rules)

**Release Notes (v6.0):**
- 1 Strong AND 3 Supporting added to benign criteria code.
- 1 Strong added to likely benign criteria code.

---

## Table of Contents

1. [Gene and Disease Information](#1-gene-and-disease-information)
2. [Pathogenic Criteria](#2-pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PS4 - Prevalence in Affected](#ps4---prevalence-in-affected)
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
   - [BP3 - In-frame Indels in Repetitive Region](#bp3---in-frame-indels-in-repetitive-region)
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
| **Gene** | SLC9A6 (HGNC:11079) |
| **HGNC Name** | solute carrier family 9 member A6 |
| **Reference Transcript** | NM_006359.2 |
| **Disease** | Christianson syndrome |
| **MONDO ID** | MONDO:0010278 |
| **Mode of Inheritance** | X-linked inheritance |
| **Mechanism of Disease** | Loss of function (knock out of *SLC9A6* results in disease but viable phenotype) |

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

#### VCEP Specifications

Refer to PVS1 flow chart for additional guidance.

For intragenic deletions/duplications that are predicted to result in a product that preserves reading frame:
- For single exon in-frame deletions assign the same strength (PVS1, PVS1_strong, or PVS1_moderate) as for splice site variants that preserve reading frame indicated above.
- For multiple exon in-frame deletions, PVS1 can be assigned to deletions that include single in-frame exons in the PVS1 category above (exon 3 or exon 10).

#### Strength Levels

| Strength | Application |
|----------|-------------|
| **PVS1** (Very Strong) | Null variant in a gene where loss of function is a known mechanism of disease. Use as defined by ClinGen SVI working group (PMID: 30192042). PVS1 is applicable for: null variants up to p.A563; canonical splice site variants predicted to result in an out-of-frame product; canonical splice site variants predicted to preserve the reading frame (exon 10); multiple in-frame exon deletions that include exon 10; single exon 3 or 10 in-frame deletion that preserves the reading frame (Note: This gene has no PM1 functional domains); deletions and duplications ≥1 exon in size (that are completely contained within the *SLC9A6* gene) where the reading frame is disrupted and NMD is predicted to occur; a full gene deletion |
| **PVS1_Strong** | Applicable for: any truncating variant from p.C564 to p.T601; canonical splice site variants that flank exon 3 (in-frame exon) |
| **PVS1_Moderate** | Applicable for: any truncating variant between p.Y602 to p.A669; any frameshift variant that results in a read-through of the stop codon |
| **PVS1_Supporting** | Applicable for initiation codon variants in *SLC9A6* |

**Modification Type:** Disease-specific (all strength levels)

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PS1** (Strong) | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. |

**Modification Type:** None (used as originally defined by ACMG/AMP)

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### VCEP Specifications

- Applicable to all genes in affected individuals identified as mosaic for the variant (as the presence of a variant in the mosaic state is confirmatory of the variant being de novo).
- Because of the very high de novo rate of pathogenic variants in *SLC9A6*, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

#### Strength Levels

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PS2_VeryStrong** | ≥2 independent occurrences of PS2. OR ≥2 independent occurrences of PM6 and one occurrence of PS2. Evidence from literature must be fully evaluated to support independent events. | General recommendation |
| **PS2** (Strong) | 1 occurrence of PS2 | None |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

#### VCEP Specifications

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PS3** (Strong) | RNA studies that demonstrate abnormal splicing and an out-of-frame transcript. Do not use for canonical splice site variants and when PVS1 is used. | Disease-specific |
| **PS3_Supporting** | RNA studies that demonstrate abnormal splicing and an inframe product (unless it affects an in-frame exon specified in the PVS1 section). | Disease-specific |

**Note:** No PS3_Moderate level is defined by this VCEP. No specific functional assay instances (e.g. calibrated protein-level assays) are listed in this specification; only RNA/splicing studies are described.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

#### VCEP Specifications

- Detailed phenotype not needed. Need to confirm patient is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.
- Patient can be published OR an internal case OR observed at an outside lab (i.e. via ClinVar) OR described in the reputable databases. However independent case has to be confirmed to be a different patient than yours (compare gender/age).
- Do not use this criterion for variants where BS1 is applied or where PM2 does not apply.

#### Strength Levels

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PS4** (Strong) | 5+ observations. | Strength |
| **PS4_Moderate** | 3-4 observations. | Strength |
| **PS4_Supporting** | Use for 2nd independent occurrence. | Strength |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
**Caveat:** Population data for indels may be poorly called by next generation sequencing.

#### VCEP Specification

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PM2_Supporting** | Absent/rare from controls in an ethnically-matched cohort population sample. Use if absent, zero observations in control databases. | Strength |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### VCEP Specifications

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PM4** (Moderate) | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. | No change |
| **PM4_Supporting** | Smaller in-frame events (< 3 amino acid residues). | Strength |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PM5_Strong** | Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. ≥2 different missense changes affecting the amino acid residue. Do not apply PM1 in these situations. | Strength |
| **PM5** (Moderate) | Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. A Grantham or BLOSUM score comparison can be used to determine if the variant is predicted to be as or more damaging than the established pathogenic variant. | None |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

#### VCEP Specifications

Because of the very high de novo rate of pathogenic variants in *SLC9A6*, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

#### Strength Levels

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PM6_VeryStrong** | ≥4 independent occurrences of PM6. Evidence from literature must be fully evaluated to support independent events. | Strength |
| **PM6_Strong** | ≥2 independent occurrences of PM6. Evidence from literature must be fully evaluated to support independent events. | Strength |
| **PM6** (Moderate) | 1 occurrence of PM6 | None |

*Note: the spec labels each PM6 strength row with the descriptor "Confirmed de novo without confirmation of paternity and maternity" (verbatim from source).*

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
**Note:** May be used as stronger evidence with increasing segregation data.

#### VCEP Specifications

Note: individuals must have disease consistent with reported phenotype (even if on the mild end of spectrum of the disease).

#### Strength Levels

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PP1_Strong** | ≥5 informative meiosis | Strength |
| **PP1_Moderate** | 3-4 informative meiosis | Strength |
| **PP1** (Supporting) | 2 informative meiosis | Strength |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

#### VCEP Specification

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PP3** (Supporting) | For missense variants use REVEL with a score ≥ 0.664. For splice site variants use SpliceAI with a score ≥ 0.2. | General recommendation |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

#### VCEP Specification

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PP4** (Supporting) | Phenotype specific for disease with single genetic etiology. See gene specific clinical phenotype guidelines. | Disease-specific |

*No point-based PP4 system is specified by this VCEP.*

#### SLC9A6 Clinical Phenotype Guidelines

**Core phenotype (need to be met for PP4):**
- Global developmental delay
- Intellectual disability
- Epilepsy
- Autistic spectrum disorder
- Ataxia
- Craniofacial dysmorphism

**Supportive criteria** (do not need to be met for PP4, however in the absence of one core phenotype, two or more supportive phenotypes can be used in its place):
- Happy, excitable, frequent smiling, laughter
- Angelman-like features
- Microcephaly

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

#### VCEP Specifications

The frequency cutoffs are based on MECP2 expected disease allele frequency (1 in 10,000 for the disease prevalence / (1.5 alleles [assumes 50/50 male/female ratio] * 0.8 for 80% penetrance)). MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **BA1** (Stand Alone) | Use large population databases (i.e. gnomAD). Use if variant is present at **≥0.000083 (0.0083%)** in any sub-population. Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles. | Disease-specific |

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### VCEP Specifications

The frequency cutoffs are based on MECP2 expected disease allele frequency divided by 10 fold. MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **BS1** (Strong) | Use large population databases (i.e. gnomAD). Use if variant is present at **≥0.0000083 (0.00083%) and <0.000083 (0.0083%)** in any sub-population. Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles. | Disease-specific |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

#### VCEP Specifications

- Should be applied in cases where the healthy adult is devoid of neurodevelopmental phenotypes.
- Best to use with internal curated data that includes clinical information or published patients that have been phenotyped.

#### Strength Levels

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **BS2** (Strong) | Observed in the heterozygous/hemizygous state in a healthy adult. 2 unaffected (related or unrelated) hemizygotes | Strength |
| **BS2_Supporting** | Observed in the heterozygous/hemizygous state in a healthy adult. 1 unaffected (related or unrelated) hemizygote | Strength |

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

#### VCEP Specification

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **BS3** (Strong) | Well-established in vitro or in vivo functional studies shows no damaging effect on protein function. RNA functional studies that demonstrate no impact on splicing and transcript composition. It can be downgraded based on quality of data. Not applicable for other functional studies. | Disease-specific |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.
**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

#### VCEP Specifications

Need to confirm that the family member is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **BS4** (Strong) | Absent in a similarly affected family member, when seen in two or more families | Strength |
| **BS4_Supporting** | Absent in a similarly affected family member | Strength |

---

### BP2 - In Trans / In Cis with Pathogenic Variant

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

#### VCEP Specifications

Knock out of *SLC9A6* results in disease but viable phenotype (PMID: 21964919).

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **BP2** (Supporting) | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder; or observed in cis with a pathogenic variant in any inheritance pattern. BP2 is not applicable for SLC9A6 for *in trans* state. | Disease-specific |

---

### BP3 - In-frame Indels in Repetitive Region

**Original ACMG Summary:** In frame-deletions/insertions in a repetitive region without a known function.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **BP3** (Supporting) | In-frame deletions/insertions in a repetitive region without a known function. BP3 is applicable if there are in-frame deletions/duplications in a repetitive region where other in-frame deletions/duplications have been observed with an overall frequency commensurate with the BA1 threshold for this gene. | None |

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc).
**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **BP4** (Supporting) | For missense variants use REVEL with a score ≤ 0.290. For splice site variants use SpliceAI with a score ≤ 0.1. | General recommendation |

---

### BP5 - Alternate Molecular Basis for Disease

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

#### VCEP Specifications

- For example if a variant in *SLC9A6* is identified in a patient with lissencephaly in whom a pathogenic variant is identified in the *PAFAH1B1* gene.
- The variant should be in the hemizygous state in the case with an alternate molecular basis for disease for this criteria to be used.
- Do not apply if variant is de novo.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **BP5_Strong** | ≥3 cases with alternate molecular basis for disease. | Strength |
| **BP5** (Supporting) | 1 case with alternate molecular basis for disease | Disease-specific |

*Note: the source does not define a level for exactly 2 cases.*

---

### BP7 - Synonymous (Silent) Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

#### VCEP Specifications

For silent variants BP4 and BP7 can be added.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **BP7** (Supporting) | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. Defined 'not highly conserved' regions in BP7 as those with PhastCons score <1 and/or PhyloP score <0.1 and/or the variant is the reference nucleotide in one primate and/or three mammal species. For splice site variants use SpliceAI with a score ≤ 0.1. | None |

---

## 4. Not Applicable Criteria

| Criterion | Original Purpose | Reason Not Applicable |
|-----------|-----------------|----------------------|
| **PM1** | Mutational hot spot / critical functional domain | Not applicable for SLC9A6. |
| **PM3** | In trans with pathogenic variant (recessive) | Not applicable for SLC9A6. |
| **PP2** | Missense in gene with low benign missense rate | Not applicable for SLC9A6. |
| **PP5** | Reputable source reports pathogenic | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP1** | Missense in a gene where truncating variants cause disease | Not applicable for SLC9A6. |
| **BP6** | Reputable source reports benign | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |

---

## 5. Rules for Combining Criteria

### Pathogenic Classification

| Combination | Applicable Codes | Classification |
|-------------|------------------|----------------|
| 1 Very Strong AND ≥1 Strong | Very Strong: PVS1, PS2_Very Strong, PM6_Very Strong; Strong: PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong | **Pathogenic** |
| 1 Very Strong AND ≥2 Moderate | Moderate: PVS1_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate | **Pathogenic** |
| 1 Very Strong AND 1 Moderate AND 1 Supporting | Supporting: PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4 | **Pathogenic** |
| 1 Very Strong AND ≥2 Supporting | — | **Pathogenic** |
| ≥2 Strong | — | **Pathogenic** |
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

### Benign Classification

| Combination | Applicable Codes | Classification |
|-------------|------------------|----------------|
| ≥2 Strong | BS1, BS2, BS3, BS4, BP5_Strong | **Benign** |
| 1 Stand Alone | BA1 | **Benign** |
| 1 Strong AND 3 Supporting | Strong: BS1, BS2, BS3, BS4, BP5_Strong; Supporting: BS2_Supporting, BS4_Supporting, BP2, BP3, BP4, BP5, BP7 | **Benign** |

### Likely Benign Classification

| Combination | Applicable Codes | Classification |
|-------------|------------------|----------------|
| ≥2 Supporting | BS2_Supporting, BS4_Supporting, BP2, BP3, BP4, BP5, BP7 | **Likely Benign** |
| 1 Strong | BS1, BS2, BS3, BS4, BP5_Strong | **Likely Benign** |

### Variant of Uncertain Significance (VUS)

- Criteria for benign and pathogenic are contradictory
- No criteria met
- Criteria met do not reach threshold for Likely Benign or Likely Pathogenic

---

## 6. Appendices

### Appendix A: PVS1 Flowchart Summary (SLC9A6, NM_006359.2)

#### Nonsense or Frameshift Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| Predicted to undergo NMD + Exon present in biologically-relevant transcript(s) | **PVS1** |
| Predicted to undergo NMD + Exon absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD + Role of region unknown + Variant removes >10% of protein (occurs between p.C564-p.T601) | **PVS1_Strong** |
| Not predicted to undergo NMD + Role of region unknown + Variant removes <10% of protein (occurs between p.Y602-p.A669); Frameshift that results in a read-through of the stop codon | **PVS1_Moderate** |

#### Splice Site Variants (GT-AG ±1,2)

| Condition | PVS1 Strength |
|-----------|---------------|
| Exon skipping / cryptic splice site disrupts reading frame + predicted NMD + Exon present in biologically-relevant transcript(s) | **PVS1** |
| Exon skipping / cryptic splice site disrupts reading frame + predicted NMD + Exon absent from biologically-relevant transcript(s) | N/A |
| Disrupts reading frame + NOT predicted NMD + Role unknown + LoF variants in exon not frequent in general population and exon present in biologically-relevant transcript(s) + Variant removes >10% of protein | **PVS1_Strong** |
| Preserves reading frame (exons 3, 10) + Role unknown (exon 3) + LoF variants in exon not frequent in general population and exon present in biologically-relevant transcript(s) | **PVS1_Strong** (exon 3) |
| Preserves reading frame + Truncated/altered region critical to protein function (exon 10) | **PVS1** (exon 10) |

#### Deletions (Single Exon to Full Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Full gene deletion | **PVS1** |
| Disrupts reading frame + predicted NMD + Exon present in biologically-relevant transcript(s) | **PVS1** |
| Disrupts reading frame + predicted NMD + Exon absent from biologically-relevant transcript(s) | N/A |
| Disrupts reading frame + NOT predicted NMD + Role unknown + LoF variants not frequent in population and exon present in biologically-relevant transcript(s) + Variant removes >10% of protein | **PVS1_Strong** |
| Disrupts reading frame + NOT predicted NMD + Role unknown + LoF variants not frequent in population and exon present in biologically-relevant transcript(s) + Variant removes <10% of protein | **PVS1_Moderate** |
| Preserves reading frame (single exon 3 or 10 deletion; other in-frame combinations) + Truncated/altered region critical to protein function (exon 3 or exon 10; Note: this gene has no PM1 functional domains) | **PVS1** |

#### Duplications (≥1 Exon, Completely Contained Within Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Proven in tandem + Reading frame disrupted and NMD predicted to occur | **PVS1** |
| Proven in tandem + No or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem + Reading frame presumed disrupted and NMD predicted to occur | **PVS1_Strong** |
| Proven not in tandem | N/A |

#### Initiation Codon Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| No known alternative start codon in other medically relevant transcripts + No pathogenic variant(s) upstream of closest potential in-frame start codon | **PVS1_Supporting** |

---

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold (any sub-population) | Strength |
|-----------|-------------------------------|----------|
| BA1 | ≥0.000083 (0.0083%) | Stand Alone |
| BS1 | ≥0.0000083 (0.00083%) and <0.000083 (0.0083%) | Strong |
| PM2 | Absent (zero observations in control databases) | Supporting |

Allele frequency must be met in any general continental population dataset of at least 2,000 observed alleles (BA1 and BS1).

---

### Appendix C: Computational Thresholds Summary

| Criterion | Tool | Threshold |
|-----------|------|-----------|
| PP3 (missense) | REVEL | ≥ 0.664 |
| PP3 (splice site) | SpliceAI | ≥ 0.2 |
| BP4 (missense) | REVEL | ≤ 0.290 |
| BP4 (splice site) | SpliceAI | ≤ 0.1 |
| BP7 (splice site) | SpliceAI | ≤ 0.1 |
| BP7 (conservation) | PhastCons / PhyloP | PhastCons <1 and/or PhyloP <0.1 and/or reference nucleotide in one primate and/or three mammal species |

---

### Appendix D: References (from the specification)

| # | Citation | Journal / Year | PMID |
|---|----------|----------------|------|
| 1 | Strømme P, Dobrenis K et al. X-linked Angelman-like syndrome caused by Slc9a6 knockout in mice exhibits evidence of endosomal-lysosomal dysfunction. | Brain (2011) 134 (Pt 11) p. 3369-83 | 21964919 |
| 2 | Tarpey PS, Smith R et al. A systematic, large-scale resequencing screen of X-chromosome coding exons in mental retardation. | Nat Genet (2009) 41 (5) p. 535-43 | 19377476 |
| 3 | Masurel-Paulet A, Piton A et al. A new family with an SLC9A6 mutation expanding the phenotypic spectrum of Christianson syndrome. | Am J Med Genet A (2016) 170 (8) p. 2103-10 | 27256868 |
| 4 | Gilfillan GD, Selmer KK et al. SLC9A6 mutations cause X-linked mental retardation, microcephaly, epilepsy, and ataxia, a phenotype mimicking Angelman syndrome. | Am J Hum Genet (2008) 82 (4) p. 1003-10 | 18342287 |
| 5 | Pejaver V, Byrne AB et al. Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria. | Am J Hum Genet (2022) 109 (12) p. 2163-2177 | 36413997 |

Additional PMID cited in the specification: 29543229 (ClinGen SVI VCEP Review Committee — PP5/BP6 not for use); 30192042 (ClinGen SVI PVS1 recommendations).

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 6.0 | May 1, 2026 | 1 Strong AND 3 Supporting added to benign criteria code. 1 Strong added to likely benign criteria code. |

---

*This document is based on the ClinGen Rett and Angelman-like Disorders Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for SLC9A6 Version 6.0 (https://cspec.genome.network/cspec/ui/svi/doc/GN033).*
