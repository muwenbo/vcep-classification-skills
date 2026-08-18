# Comprehensive Variant Interpretation Guidelines for FOXG1

## ClinGen Rett and Angelman-like Disorders VCEP Specifications for FOXG1 (Version 6.0)

**Affiliation:** Rett and Angelman-like Disorders VCEP
**Version:** 6.0
**Release Date:** 5/1/2026
**DOI:** 10.5281/zenodo.21421688
**Type:** Richards et al., 2015 - Combining rules
**Based on:** Richards et al., 2015 - ACMG/AMP Variant Interpretation Guidelines
**Specification URL:** https://cspec.genome.network/cspec/ui/svi/doc/GN035

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
   - [BP3 - In-frame Indel in Repetitive Region](#bp3---in-frame-indel-in-repetitive-region)
   - [BP4 - Computational Evidence (Benign)](#bp4---computational-evidence-benign)
   - [BP5 - Alternate Molecular Basis](#bp5---alternate-molecular-basis)
   - [BP7 - Synonymous (Silent) Variants](#bp7---synonymous-silent-variants)
4. [Not Applicable Criteria](#4-not-applicable-criteria)
5. [Rules for Combining Criteria](#5-rules-for-combining-criteria)
6. [Appendices](#6-appendices)

---

## 1. Gene and Disease Information

| Parameter | Value |
|-----------|-------|
| **Gene** | FOXG1 (HGNC:3811) |
| **HGNC Name** | forkhead box G1 |
| **Reference Transcript** | NM_005249.4 |
| **Disease** | FOXG1 disorder |
| **MONDO ID** | MONDO:0100040 |
| **Mode of Inheritance** | Autosomal dominant inheritance |

**Keywords (from specification):** human biology genomics variant, variant classification, clingen disease standards, FOXG1, NM_005249.4, Autosomal dominant inheritance, FOXG1 disorder

**Rights Holder:** The Clinical Genome Resource (ClinGen)

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats (original ACMG):**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:** Refer to PVS1 flow chart for additional guidance.

#### Strength Levels

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Very Strong (PVS1)** | Null variant in a gene where loss of function is a known mechanism of disease. Use as defined by ClinGen SVI working group (PMID: 30192042). PVS1 is applicable for: null variants up to p.S468¹; a full gene deletion. | Disease-specific |
| **Strong (PVS1_Strong)** | Null variant in a gene where loss of function is a known mechanism of disease. PVS1_Strong is applicable for any truncating variant from p.G469 to p.Q480². | Disease-specific |
| **Moderate (PVS1_Moderate)** | Null variant in a gene where loss of function is a known mechanism of disease. PVS1_Moderate is applicable for any truncating variant distal of p.Q480. | Disease-specific |
| **Supporting (PVS1_Supporting)** | Null variant in a gene where loss of function is a known mechanism of disease. PVS1_Supporting is applicable for initiation codon variants in *FOXG1*. | Disease-specific |

¹ Reference 1 (Snoeijen-Schouwenaars FM, van Ool JS et al., PMID: 30525188)
² Reference 2 (Lindy AS, Stosser MB et al., PMID: 29655203)

See [Appendix A: PVS1 Flowchart](#appendix-a-pvs1-flowchart-foxg1-nm_0052494) for the gene-specific decision tree.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (PS1)** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. | None |

**PS1_Moderate:** Not specified by VCEP.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### VCEP Specifications

- Applicable to all genes in affected individuals identified as mosaic for the variant (as the presence of a variant in the mosaic state is confirmatory of the variant being de novo).
- Because of the very high de novo rate of pathogenic variants in FOXG1, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

*(Note: the phrase "can be attributed the highest value points" appears verbatim in the source; the wording appears to be missing "to" but is reproduced here as published.)*

#### Strength Levels

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Very Strong (PS2_Very Strong)** | De novo (maternity and paternity confirmed) in a patient with the disease and no family history. ≥2 independent occurrences of PS2. OR ≥2 independent occurrences of PM6 and one occurrence of PS2. Evidence from literature must be fully evaluated to support independent events. | None |
| **Strong (PS2)** | De novo (maternity and paternity confirmed) in a patient with the disease and no family history. 1 occurrence of PS2. | None |

**PS2_Moderate / PS2_Supporting:** Not specified by VCEP.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

#### VCEP Specifications

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (PS3)** | Well-established in vitro or in vivo functional studies supportive of a damaging effect. RNA studies that demonstrate abnormal splicing and an out-of-frame transcript. Do not use for canonical splice site variants and when PVS1 is used. | Disease-specific |
| **Supporting (PS3_Supporting)** | Well-established in vitro or in vivo functional studies supportive of a damaging effect. RNA studies that demonstrate abnormal splicing and an inframe product (unless it affects an in-frame exon specified in the PVS1 section). See included table for acceptable functional studies. | Disease-specific |

**PS3_Moderate:** Not specified by VCEP.

#### Approved Assay Instances (FOXG1 Functional Assays)

| Name of assay | Measured Parameter | Expected Deleterious Result Range (PS3_Supporting) | Expected Benign Result Range (BS3) | References |
|---------------|--------------------|----------------------------------------------------|------------------------------------|------------|
| Subcellular localization | Immunofluorescence staining pattern | Abnormal staining pattern such as nuclear speckles or nuclear and cytoplasmic localization instead of homogenous distribution throughout the nucleus | Not recommended | PMID: 21280142, 22091895 |
| CDKN1A expression | CDKN1A mRNA level quantitation | Increase of CDKN1A expression by ~30% | Not recommended | PMID: 21280142 |
| Chromatin localization | Chromocenter/nucleoplasmic ratios of fluorescence intensity | Ratio greater than 0.52 indicating more dispersed within chromatin compared to wild type (ratio of 0.45) | Not recommended | PMID: 22091895 |
| Stability of chromatin binding | Strip-FRAP (fluorescence recovery after photobleaching) | Decrease in chromatin affinity, t2 of <2 seconds compared to 3 seconds or greater (wild type) | Not recommended | PMID: 22091895 |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

#### VCEP Specifications

- Detailed phenotype not needed. Need to confirm patient is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.
- Patient can be published OR an internal case OR observed at an outside lab (i.e. via ClinVar) OR described in the reputable databases (RettBASE). However independent case has to be confirmed to be a different patient than yours (compare gender/age).
- Do not use this criterion for variants where BS1 is applied or where PM2 does not apply.

#### Strength Levels

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (PS4)** | 5+ observations. | Strength |
| **Moderate (PS4_Moderate)** | 3-4 observations. | Strength |
| **Supporting (PS4_Supporting)** | Use for 2nd independent occurrence. | Strength |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

#### VCEP Specifications

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate (PM1)** | Located in a mutational hot spot and/or critical and well-established functional domain. Forkhead: aa 181-275³,⁴ | Disease-specific |

³ Reference 3 (Ariani F, Hayek G et al., PMID: 18571142)
⁴ Reference 4 (Mitter D, Pringsheim M et al., PMID: 28661489)

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
**Caveat:** Population data for indels may be poorly called by next generation sequencing.

#### VCEP Specifications

If PVS1 is also applicable, variant can be classified as likely pathogenic.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting (PM2_Supporting)** | Absent/rare from controls in an ethnically-matched cohort population sample. Use if absent, zero observations in control databases. | Strength |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### VCEP Specifications

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate (PM4)** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. Do not use PM4 for in-frame deletions/insertions in the Histidine-rich region (p.37-p.57), Proline- and Glutamine-rich region (p.58-p.86) and Proline-rich region (p.105-p.112). | Disease-specific |
| **Supporting (PM4_Supporting)** | Smaller in-frame events (< 3 amino acid residues) unless they occur in a functionally important region (see PM1 for functionally important domains for each gene). | Strength |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (PM5_Strong)** | Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. ≥2 different missense changes affecting the amino acid residue. Do not apply PM1 in these situations. | Strength |
| **Moderate (PM5)** | Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. A Grantham or BLOSUM score comparison can be used to determine if the variant is predicted to be as or more damaging than the established pathogenic variant. | None |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

#### VCEP Specifications

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Very Strong (PM6_Very Strong)** | Confirmed de novo without confirmation of paternity and maternity. ≥4 independent occurrences of PM6. Evidence from literature must be fully evaluated to support independent events. | Strength |
| **Strong (PM6_Strong)** | Confirmed de novo without confirmation of paternity and maternity. ≥2 independent occurrences of PM6. Evidence from literature must be fully evaluated to support independent events. | Strength |
| **Moderate (PM6)** | Confirmed de novo without confirmation of paternity and maternity. 1 occurrence of PM6. | None |

*(Note: the PM6 strength descriptions read "Confirmed de novo without confirmation of paternity and maternity" verbatim in the source, although PM6 addresses assumed de novo; reproduced here as published.)*

See also the PS2 VCEP specification above regarding the high de novo rate in FOXG1 (1 point per proband for assumed de novo).

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
**Note:** May be used as stronger evidence with increasing segregation data.

#### VCEP Specifications

Note: individuals must have disease consistent with reported phenotype (even if on the mild end of spectrum of the disease).

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (PP1_Strong)** | Co-segregation with disease in multiple affected family members. ≥5 informative meiosis | Strength |
| **Moderate (PP1_Moderate)** | Co-segregation with disease in multiple affected family members. 3-4 informative meiosis | Strength |
| **Supporting (PP1)** | Co-segregation with disease in multiple affected family members. 2 informative meiosis | Strength |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

#### VCEP Specifications

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting (PP3)** | Multiple lines of computational evidence support a deleterious effect on the gene or gene product. For missense variants use REVEL with a score ≥ 0.644. For splice site variants use SpliceAI with a score ≥ 0.2. | General recommendation |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

#### VCEP Specifications

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting (PP4)** | Phenotype specific for disease with single genetic etiology. See gene specific clinical phenotype guidelines. | Disease-specific |

**No point-based PP4 system is specified by this VCEP.** See [Appendix B: FOXG1 Clinical Phenotype Guideline](#appendix-b-foxg1-clinical-phenotype-guideline).

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

#### VCEP Specifications

The frequency cutoffs are based on MECP2 expected disease allele frequency (1 in 10,000 for the disease prevalence / (1.5 alleles [assumes 50/50 male/female ratio] * 0.8 for 80% penetrance)). MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Stand Alone (BA1)** | Use large population databases (i.e. gnomAD). Use if variant is present at ≥0.000083 (0.0083%) in any sub-population. Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles. | Disease-specific |

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### VCEP Specifications

The frequency cutoffs are based on MECP2 expected disease allele frequency divided by 10-fold. MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (BS1)** | Use large population databases (i.e. gnomAD). Use if variant is present at ≥0.0000083 (0.00083%) and <0.000083 (0.0083%) in any sub-population. Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles. | Disease-specific |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

#### VCEP Specifications

- Should be applied in cases where the healthy adult is devoid of neurodevelopmental phenotypes.
- Best to use with internal curated data that includes clinical information or published patients that have been phenotyped.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (BS2)** | Observed in the heterozygous/hemizygous state in a healthy adult. 2 unaffected (related or unrelated) heterozygotes. | Strength |
| **Supporting (BS2_Supporting)** | Observed in the heterozygous/hemizygous state in a healthy adult. 1 unaffected (related or unrelated) heterozygote | Strength |

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

#### VCEP Specifications

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (BS3)** | Well-established in vitro or in vivo functional studies shows no damaging effect on protein function. RNA functional studies that demonstrate no impact on splicing and transcript composition. It can be downgraded based on quality of data. Not applicable for other functional studies. | Disease-specific |

**Note:** In the FOXG1 Functional Assays table, all four protein-level assays list "Not recommended" for the Expected Benign Result Range (BS3).

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.
**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

#### VCEP Specifications

Need to confirm that the family member is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (BS4)** | Lack of segregation in affected members of a family. Absent in a similarly affected family member, when seen in two or more families | Strength |
| **Supporting (BS4_Supporting)** | Lack of segregation in affected members of a family. Absent in a similarly affected family member | Strength |

---

### BP2 - In Trans with Pathogenic Variant

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

#### VCEP Specifications

Knock-out results in embryonic lethality/drastic phenotype⁵

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting (BP2)** | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder; or observed in cis with a pathogenic variant in any inheritance pattern. Applicable for *in trans* state | Disease-specific |

⁵ Reference 5 (Hanashima C, Li SC et al., PMID: 14704420)

---

### BP3 - In-frame Indel in Repetitive Region

**Original ACMG Summary:** In frame-deletions/insertions in a repetitive region without a known function.

#### VCEP Specifications

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting (BP3)** | In-frame deletions/insertions in a repetitive region without a known function. Inframe expansions or deletions in *FOXG1* repetitive regions: poly His (p.His47-p.His57), poly Gln (p.Gln70-p.Gln73) and poly Pro (p.Pro58-p.Pro61; p.Pro65-p.Pro69; p.Pro74-p.Pro80). BP3 is applicable if there are in-frame deletions/duplications in a repetitive region where other in-frame deletions/duplications have been observed with an overall frequency commensurate with the BA1 threshold for this gene. | Disease-specific |

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc).
**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

#### VCEP Specifications

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting (BP4)** | For missense variants use REVEL with a score ≤ 0.290. For splice site variants use SpliceAI with a score ≤ 0.1. | General recommendation |

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

#### VCEP Specifications

- For example if a variant in *FOXG1* is identified in a patient with lissencephaly in whom a pathogenic variant is identified in the *PAFAH1B1* gene.
- Do not apply if variant is de novo.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (BP5_Strong)** | Variant found in a case with an alternate molecular basis for disease. ≥3 cases with alternate molecular basis for disease. | Strength |
| **Supporting (BP5)** | Variant found in a case with an alternate molecular basis for disease. 1 case with alternate molecular basis for disease. | Disease-specific |

*(Note: the spec provides Strong for ≥3 cases and Supporting for 1 case; the 2-case scenario is not addressed.)*

---

### BP7 - Synonymous (Silent) Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

#### VCEP Specifications

For silent variants BP4 and BP7 can be added.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting (BP7)** | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. Defined 'not highly conserved' regions in BP7 as those with PhastCons score <1 and/or PhyloP score <0.1 and/or the variant is the reference nucleotide in one primate and/or three mammal species. For splice site variants use SpliceAI with a score ≤ 0.1. | None |

---

## 4. Not Applicable Criteria

| Criterion | Original Purpose | Reason Not Applicable |
|-----------|-----------------|----------------------|
| **PM3** | In trans with pathogenic variant (recessive disorders) | Not applicable for FOXG1. |
| **PP2** | Missense variant in gene with low rate of benign missense variation | Not applicable for FOXG1. |
| **PP5** | Reputable source reports variant as pathogenic | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP1** | Missense variant in a gene for which primarily truncating variants are known to cause disease | Not applicable for FOXG1. |
| **BP6** | Reputable source reports variant as benign | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |

---

## 5. Rules for Combining Criteria

### Pathogenic Classification

| Combination | Applicable Criteria |
|-------------|---------------------|
| 1 Very Strong **AND** ≥1 Strong | Very Strong: PVS1, PS2_Very Strong, PM6_Very Strong; Strong: PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong |
| 1 Very Strong **AND** ≥2 Moderate | Very Strong: PVS1, PS2_Very Strong, PM6_Very Strong; Moderate: PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting | Supporting: PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4 |
| 1 Very Strong **AND** ≥2 Supporting | — |
| ≥2 Strong | Strong: PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong |
| 1 Strong **AND** ≥3 Moderate | — |
| 1 Strong **AND** 2 Moderate **AND** ≥2 Supporting | — |
| 1 Strong **AND** 1 Moderate **AND** ≥4 Supporting | — |

### Likely Pathogenic Classification

| Combination |
|-------------|
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** ≥2 Supporting |
| ≥3 Moderate |
| 2 Moderate **AND** ≥2 Supporting |
| 1 Moderate **AND** ≥4 Supporting |
| 1 Strong **AND** 2 Moderate |

### Benign Classification

| Combination | Applicable Criteria |
|-------------|---------------------|
| ≥2 Strong | BS1, BS2, BS3, BS4, BP5_Strong |
| 1 Stand Alone | BA1 |
| 1 Strong **AND** 3 Supporting | Strong: BS1, BS2, BS3, BS4, BP5_Strong; Supporting: BS2_Supporting, BS4_Supporting, BP2, BP3, BP4, BP5, BP7 |

### Likely Benign Classification

| Combination | Applicable Criteria |
|-------------|---------------------|
| ≥2 Supporting | BS2_Supporting, BS4_Supporting, BP2, BP3, BP4, BP5, BP7 |
| 1 Strong | BS1, BS2, BS3, BS4, BP5_Strong |

### Criteria Strength Groupings (as listed in the specification)

| Strength | Criteria |
|----------|----------|
| **Very Strong** | PVS1, PS2_Very Strong, PM6_Very Strong |
| **Strong (pathogenic)** | PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong |
| **Moderate** | PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate |
| **Supporting (pathogenic)** | PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4 |
| **Stand Alone** | BA1 |
| **Strong (benign)** | BS1, BS2, BS3, BS4, BP5_Strong |
| **Supporting (benign)** | BS2_Supporting, BS4_Supporting, BP2, BP3, BP4, BP5, BP7 |

---

## 6. Appendices

### Appendix A: PVS1 Flowchart (FOXG1, NM_005249.4)

#### Nonsense or Frameshift

| Condition | PVS1 Strength |
|-----------|---------------|
| Not predicted to undergo NMD (single exon gene) → Upstream of most distal de novo LOF variant (p.S468) | **PVS1** |
| Not predicted to undergo NMD (single exon gene) → Downstream of most distal de novo LOF variant (p.S468) | **PVS1_Strong** |
| Not predicted to undergo NMD (single exon gene) → Downstream of most distal de novo non-truncating variant (p.Q480) | **PVS1_Moderate** |

#### GT-AG 1,2 Splice Sites

| Condition | PVS1 Strength |
|-----------|---------------|
| Single exon gene | **N/A** |

#### Deletion (Single Exon to Full Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Full gene deletion | **PVS1** |

#### Duplication (≥1 exon in size and must be completely contained within gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Single exon gene | **N/A** |

#### Initiation Codon

| Condition | PVS1 Strength |
|-----------|---------------|
| No known alternative start codon in other medically relevant transcripts → No pathogenic variant(s) upstream of closest potential in-frame start codon | **PVS1_Supp** |

---

### Appendix B: FOXG1 Clinical Phenotype Guideline

Used for PP4.

#### Core phenotype (need to be met for PP4)

- Microcephaly
- Severe intellectual disability
- Dyskinesia
- No period of normal development
- Neonatal hypotonia

#### Additional features

*(do not need to be met for PP4, however in the absence of one core phenotype, two or more supportive phenotypes can be used in its place)*

- Abnormal brain imaging (e.g. partial agenesis of the corpus callosum, simplified gyral pattern, reduced white matter volume)
- Delayed motor development
- Impairment of postnatal growth
- Stereotypies
- Generalized seizures
- GE reflux
- Poor sleep pattern
- Unexplained episodes of crying
- Recurrent aspiration

---

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold (any sub-population, gnomAD) | Strength |
|-----------|----------------------------------------|----------|
| BA1 | ≥0.000083 (0.0083%) | Stand Alone |
| BS1 | ≥0.0000083 (0.00083%) and <0.000083 (0.0083%) | Strong |
| PM2_Supporting | Absent (zero observations) in control databases | Supporting |

Allele frequency thresholds require the frequency to be met in any general continental population dataset of at least 2,000 observed alleles.

---

### Appendix D: Reference PMIDs

| # | Citation | PMID |
|---|----------|------|
| 1 | Snoeijen-Schouwenaars FM, van Ool JS et al. Diagnostic exome sequencing in 100 consecutive patients with epilepsy and intellectual disability. *Epilepsia* (2019) 60 (1) p. 155-164. doi:10.1111/epi.14618 | 30525188 |
| 2 | Lindy AS, Stosser MB et al. Diagnostic outcomes for genetic testing of 70 genes in 8565 patients with epilepsy and neurodevelopmental disorders. *Epilepsia* (2018) 59 (5) p. 1062-1071. doi:10.1111/epi.14074 | 29655203 |
| 3 | Ariani F, Hayek G et al. FOXG1 is responsible for the congenital variant of Rett syndrome. *Am J Hum Genet* (2008) 83 (1) p. 89-93. doi:10.1016/j.ajhg.2008.05.015 | 18571142 |
| 4 | Mitter D, Pringsheim M et al. FOXG1 syndrome: genotype-phenotype association in 83 patients with FOXG1 variants. *Genet Med* (2018) 20 (1) p. 98-108. doi:10.1038/gim.2017.75 | 28661489 |
| 5 | Hanashima C, Li SC et al. Foxg1 suppresses early cortical cell fate. *Science* (2004) 303 (5654) p. 56-9. doi:10.1126/science.1090674 | 14704420 |
| 6 | Pejaver V, Byrne AB et al. Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria. *Am J Hum Genet* (2022) 109 (12) p. 2163-2177. doi:10.1016/j.ajhg.2022.10.013 | 36413997 |
| — | Tayoun AN et al. (ClinGen SVI PVS1 recommendations, cited in PVS1) | 30192042 |
| — | ClinGen SVI VCEP Review Committee (PP5/BP6 not for use) | 29543229 |
| — | FOXG1 functional assays (subcellular localization, CDKN1A expression) | 21280142 |
| — | FOXG1 functional assays (chromatin localization, Strip-FRAP) | 22091895 |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 6.0 | 5/1/2026 | 1 Strong AND 3 Supporting added to benign criteria code. 1 Strong added to likely benign criteria code. |

---

*This document was compiled from the ClinGen Rett and Angelman-like Disorders Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for FOXG1 Version 6.0 (GN035) and its supplementary files. For the most current version, please refer to the ClinGen website.*
