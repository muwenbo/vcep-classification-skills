# Comprehensive Variant Interpretation Guidelines for HBB

## ClinGen Hemoglobinopathy VCEP Specifications for beta-thalassemia HBB/LCRB (Version 1.0.0)

**Affiliation:** Hemoglobinopathy Variant Curation Expert Panel (Hemoglobinopathy VCEP)
**Version:** 1.0 (spec description: Version 1.0.0)
**Release Date:** March 20, 2026
**DOI:** 10.5281/zenodo.21434787
**Based on:** Richards et al., 2015 - ACMG/AMP Variant Interpretation Guidelines (Combining rules)

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
   - [PM3 - In Trans with Pathogenic Variant](#pm3---in-trans-with-pathogenic-variant)
   - [PM4 - Protein Length Changes](#pm4---protein-length-changes)
   - [PM5 - Novel Missense at Same Residue](#pm5---novel-missense-at-same-residue)
   - [PM6 - De Novo (Assumed)](#pm6---de-novo-assumed)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
3. [Benign Criteria](#3-benign-criteria)
   - [BA1 - Stand-Alone Benign](#ba1---stand-alone-benign)
   - [BS1 - Allele Frequency Greater Than Expected](#bs1---allele-frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (Benign)](#bs3---functional-studies-benign)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP2 - Observed in cis with Pathogenic Variant](#bp2---observed-in-cis-with-pathogenic-variant)
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
| **Gene** | HBB (HGNC:4827) |
| **HGNC Name** | hemoglobin subunit beta |
| **Reference Transcript** | NM_000518.5 |
| **Disease** | beta-thalassemia HBB/LCRB |
| **MONDO ID** | MONDO:0013517 |
| **Mode of Inheritance** | Autosomal recessive inheritance |
| **Mechanism of Disease** | Loss of function (established as a disease mechanism for haemoglobinopathies) |

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specifications:**
- Use the Hemoglobinopathy VCEP PVS1 decision tree.
- Loss of function has been established as a disease mechanism for haemoglobinopathies.

#### General Caveats

- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact

#### Strength Levels

| Strength | Application |
|----------|-------------|
| **PVS1** (Very Strong) | Null variant in a gene where LOF is a known mechanism of disease (no change from ACMG); assign via the HBB PVS1 decision tree |
| **PVS1_Strong** | Assigned via the HBB PVS1 decision tree (disease-specific, gene-specific, strength modification) |
| **PVS1_Moderate** | Assigned via the HBB PVS1 decision tree (disease-specific, gene-specific, strength modification) |
| **PVS1_Supporting** | Not specified by VCEP |

#### HBB PVS1 Decision Tree (Appendix A)

##### Nonsense or Frameshift Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| Predicted to undergo NMD: nonsense (or frameshift-induced PTC) located at or between p.Val24 (c.70) and p.Ala87 (c.261) | **PVS1** |
| Not predicted to undergo NMD (PTC 5' of p.Glu23 (c.69), or at or 3' of p.Thr88 (c.262)) + truncated/altered region is critical to protein function | **PVS1_Strong** |
| Not predicted to undergo NMD + role of region in protein function is unknown + variant removes >10% of protein | **PVS1_Strong** |
| Not predicted to undergo NMD + role of region in protein function is unknown + variant removes <10% of protein | **PVS1_Moderate** |

##### Splice Site Variants (GT-AG ±1,2)

| Condition | PVS1 Strength |
|-----------|---------------|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD (stop codon or disruption at or between p.Val24 (c.70) and p.Ala87 (c.261)) | **PVS1** |
| Exon skipping or use of a cryptic splice site preserves reading frame | **PVS1_Strong** |

##### Initiation Codon Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| Variant in the initiation codon | **PVS1** |

**NMD boundaries:** NMD boundaries for HBB are published by Peixeiro et al., 2011 (doi: 10.3324/haematol.2010.039206). Exon 1 = codons 1-23 (NMD-escaping, short protein, effective proteolysis); exon 2 = codons 24-87 (NMD, no protein; recessive, heterozygotes asymptomatic); exon 3 = codons 88-146 (NMD-escaping; long truncated protein with ineffective proteolysis leads to a dominant phenotype with severely affected heterozygotes).

The HBB PVS1 decision tree is adapted from Tayoun et al., 2018.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

A variant classification must have a minimum of two-star annotation in ClinVar to be considered established, or be a VCEP consensus recommendation.

| Strength | Application |
|----------|-------------|
| **PS1_Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change (no change from ACMG) |
| **PS1_Moderate** | Not specified by VCEP |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### VCEP Specifications

- Both maternal and paternal sample must be tested and shown to be the biological parents of the affected individual. Otherwise, identity is assumed, and not confirmed, and PM6 applies.
- Only applicable in the absence of any other established pathogenic variants. If other suspicious variants are present, then PM6 should be used instead. Should not be used in combination with PM6.
- Definition of trait phenotype is provided in Appendix 3 (see [Appendix C](#appendix-c-ps4-phenotype-evaluation-in-heterozygotes)).

| Strength | Application |
|----------|-------------|
| **PS2_Strong** | De novo (both maternity and paternity confirmed) in a patient with the disease **or in a phenotypic trait individual** and no family history |

**Note:** No point-based PS2/PM6 system is specified by this VCEP. Only the Strong level is defined for PS2; PS2_VeryStrong, PS2_Moderate and PS2_Supporting are not specified by the VCEP.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

#### VCEP Specifications

The list of approved functional studies is provided in Appendix 2 (Functional Studies), reproduced in [Appendix B](#appendix-b-approved-functional-studies-appendix-2) below.

| Strength | Application |
|----------|-------------|
| **PS3_Strong** | Not specified by VCEP |
| **PS3_Moderate** | Not specified by VCEP |
| **PS3_Supporting** | In vitro or in vivo functional studies supportive of a damaging effect on the gene, gene product, expression levels and protein function |

All five approved assays yield **PS3_Supporting** as the maximum deleterious strength.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

#### VCEP Specifications

Strength of evidence is determined by points according to Appendix 3 (Evaluation of phenotypes in heterozygotes), reproduced in [Appendix C](#appendix-c-ps4-phenotype-evaluation-in-heterozygotes) below.

| Strength | Points Required |
|----------|-----------------|
| **PS4_VeryStrong** | ≥16 points |
| **PS4_Strong** | 3.5 - 15.99 points |
| **PS4_Moderate** | 1.5 - 3.49 points |
| **PS4_Supporting** | 0.5 - 1.49 points |

**Note:** When evaluating cases, be aware of potential complex genotype interactions. Only independent (unrelated) cases should be considered; multiple cases in a family are counted as one. Do NOT use multiple point levels for the same case.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PM1_Moderate** | Variant located in one of the following HBB regulatory elements: <br>• TATAA box (-30 to -26 from transcription initiation, i.e., c.-80 to c.-76) <br>• Poly(A) signals: AATAAA sequence |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes, or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

#### VCEP Specifications

Position of the reported variant must have sufficient coverage (**≥20x**) in the population database.

| Strength | Threshold |
|----------|-----------|
| **PM2_Supporting** | Allele frequency **<0.0001 (0.01%)** in gnomAD |

---

### PM3 - In Trans with Pathogenic Variant

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

#### VCEP Specifications

- Strength is determined using the ClinGen SVI guidelines (https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf).
- Both variants must meet the PM2_Supporting specification, i.e., be sufficiently rare, **unless** they are in the exception list (Appendix 4, see [Appendix D](#appendix-d-variants-excluded-from-ba1-bs1-and-pm3-appendix-4)), or present in gnomAD with <20x genomic coverage.
- Phase is confirmed in trans by testing both or one parent, and the pathogenicity of the variant on the other allele must have at least 2-star rating in ClinVar or be a VCEP consensus recommendation.

| Strength | Application |
|----------|-------------|
| **PM3_VeryStrong** | For recessive disorders, detected in trans with a pathogenic or likely pathogenic variant in an affected patient; strength determined using the ClinGen SVI guidelines |
| **PM3_Strong** | As above; strength determined using the ClinGen SVI guidelines |
| **PM3** (Moderate) | As above; strength determined using the ClinGen SVI guidelines (no change from ACMG) |
| **PM3_Supporting** | As above; strength determined using the ClinGen SVI guidelines |

**Note:** The VCEP does not restate the SVI point table or the point-to-strength thresholds in this specification; refer directly to the linked ClinGen SVI PM3 proposal (version 1) for point assignment.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### VCEP Specifications

PM4 should not be used if PVS1 has been applied.

| Strength | Application |
|----------|-------------|
| **PM4_Moderate** | Protein length changes as a result of in-frame deletions/insertions in a non-repeat region |
| **PM4_Supporting** | Not specified by VCEP |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

- Beware of changes that impact splicing rather than at the amino acid/protein level. Assess potential for creation of an exonic splicing event using in silico splicing prediction tools, as described in PP3/BP4.
- A previously established pathogenic variant must have at least 2-star rating in ClinVar or be a VCEP consensus recommendation.

| Strength | Application |
|----------|-------------|
| **PM5_Moderate** | Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before, **or** base change at a non-coding position where a previous pathogenic mutation has been seen before |

**Examples:**
- Arg156His is pathogenic; now you observe Arg156Cys.
- Non-coding variant g.15300G>C is pathogenic; now you observe g.15300G>A.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

#### VCEP Specifications

In contrast to PS2, identity testing was NOT performed in parental samples to confirm identity, which is assumed. Should not be used in combination with PS2.

| Strength | Application |
|----------|-------------|
| **PM6** (Moderate) | Assumed de novo, but without confirmation of paternity and maternity (no change from ACMG) |

**Note:** No point-based PS2/PM6 system is specified by this VCEP.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

#### VCEP Specifications

- LOD score for recessive disorder can be estimated from the tables in Appendix 1 (Segregation Analysis), based on the number of affected and unaffected individuals (see [Appendix E](#appendix-e-segregation-analysis-lod-scores-appendix-1)).
- Caution is needed when counting segregations in the presence of other possible disease-causing variants. Compound heterozygous individuals are counted only if phase is confirmed to be in trans.

#### PP1 Thresholds

| Strength | Likelihood | LOD Score |
|----------|------------|-----------|
| **PP1_Supporting** | 8:1 | >0.9 |
| **PP1_Moderate** | 32:1 | >1.5 |
| **PP1_Strong** | 128:1 | >2.1 |

*Applicable where phenocopy or diagnostic clarity is a minor concern.*

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

#### VCEP Specifications

| Strength | Thresholds |
|----------|------------|
| **PP3_Supporting** | **Missense:** REVEL score >0.8 **OR** SpliceAI >0.3. If REVEL score is not available, use CADD PHRED score >23.5. <br>**Non-coding, synonymous, in-frame indels, stop-lost:** CADD PHRED score >12 **OR** SpliceAI DS >0.3 |

**Restriction:** PP3 should not be used for LOF variants considered in PVS1.

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes, or Exome Aggregation Consortium.

#### VCEP Specifications

Use the Filtering AF, such as Popmax FAF from gnomAD. If the variant is present at high frequency in a non-continental population (e.g., Ashkenazi Jews), the filtering allele frequency can be calculated using a 95% confidence interval by selecting "Inverse AF" at http://cardiodb.org/allelefrequencyapp/.

| Strength | Threshold |
|----------|-----------|
| **BA1** (Stand Alone) | Allele frequency **≥0.005 (0.5%)** in a studied general population with ≥2000 alleles **and** variant present in ≥5 alleles |

##### Calculation Assumptions (β-haemoglobinopathies, autosomal recessive)

- Prevalence: 1/1000 (the highest reported prevalence of the disease)
- Genetic heterogeneity: 100% (only one gene involved in disease causality)
- Allelic heterogeneity: 15% (variants in the exclusion list are not considered)
- Penetrance: 90% (to account for silent variants)

**Exclusion:** Variants in Appendix 4 are excluded from this criterion (see [Appendix D](#appendix-d-variants-excluded-from-ba1-bs1-and-pm3-appendix-4)).

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### VCEP Specifications

Use the Filtering AF, such as Popmax FAF from gnomAD. If the variant is present at high frequency in a non-continental population (e.g., Ashkenazi Jews), the filtering allele frequency can be calculated using a 95% confidence interval by selecting "Inverse AF" at http://cardiodb.org/allelefrequencyapp/.

| Strength | Threshold |
|----------|-----------|
| **BS1_Strong** | Allele frequency **≥0.001 (0.1%)** in a studied general population with ≥2000 alleles **and** variant present in ≥5 alleles |

##### Calculation Assumptions (β-haemoglobinopathies, autosomal recessive)

- Prevalence: 1/3000 (the highest reported prevalence of the disease)
- Genetic heterogeneity: 100% (only one gene involved in disease causality)
- Allelic heterogeneity: 5% (variants in the exclusion list are not considered)
- Penetrance: 90% (to account for silent variants)

**Exclusion:** Variants in Appendix 4 are excluded from this criterion (see [Appendix D](#appendix-d-variants-excluded-from-ba1-bs1-and-pm3-appendix-4)).

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

#### VCEP Specifications

- Normal haematological values are provided in Appendix 3.
- The healthy individual must be well-phenotyped/well-documented to rule out any mild symptoms and ensure that the individual is unaffected. A full-blood count and Hb characterization are required to exclude variants and/or abnormal quantities.
- In compound heterozygous individuals, only established pathogenic variants should be considered (i.e., at least 2-star rating in ClinVar).
- Applies to subjects over 2 years of age.
- **BS2:** Only applicable if no coinheritance is detected of an HBA1/HBA2 pathogenic variant.
- **BS2_P:** Only applicable if no well-established disease-modifying mutations are detected.

| Strength | Application |
|----------|-------------|
| **BS2_Strong** | Two independent occurrences in individuals (asymptomatic or with trait phenotype) for a recessive (homozygous or compound heterozygous) disorder, with full penetrance expected at early age |
| **BS2_Supporting** | Observation in one individual (asymptomatic or with trait phenotype) for a recessive (homozygous or compound heterozygous) disorder, with full penetrance expected at early age |

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

#### VCEP Specifications

The list of approved functional studies is provided in Appendix 2 (Functional Studies), reproduced in [Appendix B](#appendix-b-approved-functional-studies-appendix-2) below.

| Strength | Application |
|----------|-------------|
| **BS3_Strong** | Not specified by VCEP |
| **BS3_Supporting** | In vivo or in vitro functional studies show no damaging effect on gene, gene product, expression levels and protein function |

All five approved assays yield **BS3_Supporting** as the maximum benign strength.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e., cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

| Strength | Application |
|----------|-------------|
| **BS4_Strong** | Lack of segregation in affected members of a family (no change from ACMG) |

---

### BP2 - Observed in cis with Pathogenic Variant

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder, or observed in cis with a pathogenic variant in any inheritance pattern.

#### VCEP Specifications

- Do not use when the variant has only ever been observed in cis with a pathogenic variant, as its significance/severity in isolation is unknown.
- Only applies when the phenotype is not more severe than when either of the two variants is seen in isolation.
- Use only if in cis with variants classified as pathogenic in ClinVar with at least two-star rating.

| Strength | Application |
|----------|-------------|
| **BP2_Supporting** | Observed in cis with a pathogenic variant in any inheritance pattern (no change from ACMG) |

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

#### VCEP Specifications

| Strength | Thresholds |
|----------|------------|
| **BP4_Supporting** | **Missense:** REVEL score <0.7 **AND** SpliceAI DS ≤0.3 (if REVEL score is not available, use CADD PHRED score ≤20 instead). <br>**Non-coding, synonymous, in-frame indels, stop-lost:** CADD PHRED score ≤11 **AND** SpliceAI DS ≤0.3 |

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

#### VCEP Specifications

This is about phenotypes that are COMPLETELY explained by variants in different genes. Specifically:
- Duplication of the α-locus can result in a β-thalassaemia intermedia phenotype
- Variants in *SUPT5H* that can cause a β-thalassemia phenotype

| Strength | Application |
|----------|-------------|
| **BP5_Supporting** | Variant found in a case with an alternate molecular basis for disease (no change from ACMG) |

---

### BP7 - Synonymous Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

#### VCEP Specifications

Synonymous variant with no impact on splicing (**SpliceAI ≤0.3**) **AND GERP++ <0** for conservation.

| Strength | Application |
|----------|-------------|
| **BP7_Supporting** | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved (no change from ACMG) |

---

## 4. Not Applicable Criteria

The following ACMG/AMP criteria are **NOT APPLICABLE** for HBB variant interpretation:

| Criterion | Original Purpose | Reason Not Applicable |
|-----------|-----------------|----------------------|
| **PP2** | Low rate of benign missense variation | Marked "Not Applicable" by the VCEP (no reason given) |
| **PP4** | Phenotype specificity | Marked "Not Applicable" by the VCEP (no reason given) |
| **PP5** | Reputable source reports pathogenic | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |
| **BP1** | Missense in truncating disease gene | Marked "Not Applicable" by the VCEP (no reason given) |
| **BP3** | In-frame deletion/insertion in repetitive region | Marked "Not Applicable" by the VCEP (no reason given) |
| **BP6** | Reputable source reports benign | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |

---

## 5. Rules for Combining Criteria

### Pathogenic Classification

| Combination | Classification |
|-------------|----------------|
| 1 Very Strong AND ≥1 Strong | **Pathogenic** |
| 1 Very Strong AND ≥2 Moderate | **Pathogenic** |
| 1 Very Strong AND 1 Moderate AND 1 Supporting | **Pathogenic** |
| 1 Very Strong AND ≥2 Supporting | **Pathogenic** |
| ≥2 Strong | **Pathogenic** |
| 1 Strong AND ≥3 Moderate | **Pathogenic** |
| 1 Strong AND 2 Moderate AND ≥2 Supporting | **Pathogenic** |
| 1 Strong AND 1 Moderate AND ≥4 Supporting | **Pathogenic** |
| ≥2 Very Strong (PVS1) | **Pathogenic** |
| ≥2 Very Strong (PVS1, PS4_Very Strong, PM3_Very Strong) | **Pathogenic** |

### Likely Pathogenic Classification

| Combination | Classification |
|-------------|----------------|
| 1 Very Strong AND 1 Moderate | **Likely Pathogenic** |
| 1 Strong AND 1 Moderate | **Likely Pathogenic** |
| 1 Strong AND ≥2 Supporting | **Likely Pathogenic** |
| ≥3 Moderate | **Likely Pathogenic** |
| 2 Moderate AND ≥2 Supporting | **Likely Pathogenic** |
| 1 Moderate AND ≥4 Supporting | **Likely Pathogenic** |

### Benign Classification

| Combination | Classification |
|-------------|----------------|
| ≥2 Strong | **Benign** |
| 1 Stand Alone (BA1) | **Benign** |

### Likely Benign Classification

| Combination | Classification |
|-------------|----------------|
| 1 Strong AND 1 Supporting | **Likely Benign** |
| ≥2 Supporting | **Likely Benign** |

### Variant of Uncertain Significance (VUS)

- Criteria for benign and pathogenic are contradictory
- No criteria met
- Criteria met do not reach threshold for Likely Benign or Likely Pathogenic

---

## 6. Appendices

### Appendix A: HBB PVS1 Decision Tree

HBB-specific recommendations for application of PVS1, adapted from Tayoun et al., 2018.

```
Nonsense or Frameshift *
├── Predicted to undergo NMD
│   (PTC located at or between p.Val24 (c.70) and p.Ala87 (c.261))     → PVS1
└── Not predicted to undergo NMD
    (PTC located 5' of p.Glu23 (c.69), or at or 3' of p.Thr88 (c.262))
    ├── Truncated/altered region is critical to protein function        → PVS1_Strong
    └── Role of region in protein function is unknown
        ├── Variant removes >10% of protein                             → PVS1_Strong
        └── Variant removes <10% of protein                             → PVS1_Moderate

GT--AG 1,2 splice sites
├── Exon skipping or use of a cryptic splice site disrupts reading
│   frame and is predicted to undergo NMD (stop codon or disruption
│   at or between p.Val24 (c.70) and p.Ala87 (c.261))                   → PVS1
└── Exon skipping or use of a cryptic splice site preserves
    reading frame                                                      → PVS1_Strong

Initiation Codon                                                       → PVS1
```

*NMD boundaries for HBB are published by Peixeiro et al., 2011 (doi: 10.3324/haematol.2010.039206).

| Region | Codons | NMD | Consequence |
|--------|--------|-----|-------------|
| Exon 1 | 1-23 | No NMD | Short protein, effective proteolysis → recessive, heterozygotes asymptomatic |
| Exon 2 | 24-87 | NMD | No protein → recessive, heterozygotes asymptomatic |
| Exon 3 (5' part, >55 nt upstream of last exon-exon junction) | 88-146 | No NMD | Short protein, effective proteolysis → recessive, heterozygotes asymptomatic |
| Exon 3 (further downstream) | 88-146 | No NMD | Long truncated protein, ineffective proteolysis → dominant, heterozygotes severely affected |

---

### Appendix B: Approved Functional Studies (Appendix 2)

The following functional studies are approved by the Haemoglobinopathy VCEP. The panel will be constantly assessing available evidence for potential approval of additional assays.

| # | Assay | Measured Parameter | Readout Type | Deleterious Result Range (PS3) | PS3 Strength | Benign Result Range (BS3) | BS3 Strength |
|---|-------|--------------------|--------------|-------------------------------|--------------|---------------------------|--------------|
| 1 | Haemoglobin stability test | Hb stability | Qualitative | Presence of precipitate, visible to the naked eye | PS3_Supporting | Clear; possibly <5% precipitate at 50 °C/30 min | BS3_Supporting |
| 2 | Biosynthesis assay | Globin synthesis | Quantitative | β-thal trait: β/α 0.50 (0.38-0.62) | PS3_Supporting | β/α 0.96 (0.78-1.14) | BS3_Supporting |
| 3 | Haemoglobin electrophoresis, HPLC | Detection and quantification of variant haemoglobins | Quantitative | Not concordant with normal chromatogram or readout. Hb X <35% | PS3_Supporting | Concordant with normal chromatogram or readout | BS3_Supporting |
| 4 | In vitro splicing assay | Alternative RNA splicing | Quantitative | Abnormal splice product detected (wild-type and aberrant transcripts are present) | PS3_Supporting | No abnormal splice product detected (only wild-type RNA transcript is present) | BS3_Supporting |
| 5 | In vitro cell-based assay | Gene expression (luciferase/fluorescence, RNA, protein) | Qualitative / Quantitative | Changes in the expression level of the reporter gene or transgene in comparison to normal levels | PS3_Supporting | No changes in the expression level of the reporter gene or transgene in comparison to normal levels | BS3_Supporting |

#### Assay Notes and References

| # | Notes | References |
|---|-------|------------|
| 1 | Reduced stability, precipitation in isopropanol or after heating at 50 °C. False-positive or doubtful results if HbF levels >3%, and by prolonged storage due to methaemoglobin formation. Hyper-unstable Hb variants are rapidly destroyed, hence not readily detected by stability tests; in these cases, no functional evidence should be applied. | Dacie and Lewis Practical Haematology, 9th Ed. |
| 2 | Change in biosynthetic ratio of globins (thalassaemia). β/α values apply for subjects ≥2 years of age. | Old J. et al., Prevention of Thalassaemias and Other Haemoglobin Disorders: Vol. 2: Laboratory Protocols, 2nd Ed. |
| 3 | Change in electrophoretic mobilities, or change in relative peak area and rate of elution (retention time) AND quantification. Do not apply only for the detection of variant haemoglobins, or for the quantification of normal haemoglobins A, F and A2. | Dacie and Lewis Practical Haematology, 9th Ed. |
| 4 | Splicing pattern with (i) autoradiograms of radiolabeled minigene constructs, (ii) long-read RNA sequencing. Beware of abnormal transcripts that lead to truncated proteins (PP4) without functional consequences, and cell systems where NMD is not active. | PMID: 24549662 |
| 5 | Transfection of erythroid cell cultures (e.g., K562, HEL, HUDEP-2) with constructs bearing (i) reporter cassettes with mutated promoter, 5'UTR and enhancer sequences or (ii) a cloned mutant human globin gene. Also applies to RNA studies with cells from heterozygous or homozygous probands (wild-type, aberrant transcript detection). | Not provided |

---

### Appendix C: PS4 Phenotype Evaluation in Heterozygotes

Evaluation of phenotypes in heterozygotes for beta-thalassemia HBB/LCRB [AR].

**Note:** When evaluating cases be aware of potential complex genotype interactions.

| Evidence | Parameter | Impact Threshold | Alternative Terms | Points per Case | Max | Comment |
|----------|-----------|------------------|-------------------|-----------------|-----|---------|
| Reduced MCV, Reduced MCH, Increased HbA2 | MCV (fL), MCH (pg), HbA2 (%) | <79, <27, >3.5 | Microcytosis, Hypochromia | 1.5 | 16 | For beta-thal trait only. Very specific phenotype. Caution needed for the presence of another pathogenic variant in the beta globin locus or in HIV-positive patients on antiretroviral therapy (ART) |
| Reduced MCV, Reduced MCH | MCV (fL), MCH (pg) | <79, <27 | Microcytosis, Hypochromia | 0.15 | 1.5 | Primarily for thalassaemias and thalassaemic Hb variants. Do not use if the RBC count is decreased or iron deficiency is present |
| Reduced MCV, Reduced MCH, Normal or increased RBC count | MCV (fL), MCH (pg), RBC (10^12/L) | <79, <27, 4.7-6.1 for men (normal); 4.2-5.4 for women (normal) | Microcytosis, Hypochromia | 0.2 | 1.6 | Primarily for thalassaemias and thalassaemic Hb variants. Do not use if there is an indication of recent correction of iron deficiency |
| Reduced MCV, Reduced MCH excluding iron deficiency (i.e., normal serum ferritin, transferrin saturation, TIBC) | MCV (fL), MCH (pg) | <79, <27 | Microcytosis, Hypochromia | 0.3 | 3 | Primarily for thalassaemias and thalassaemic Hb variants |

\* Only consider independent (unrelated) cases. Multiple cases in a family are counted as one.
\*\* Do NOT use multiple point levels for the same case.

#### Point Sum and Evidence Strength

| Supporting | Moderate | Strong | Very Strong |
|------------|----------|--------|-------------|
| 0.5 - 1.49 | 1.5 - 3.49 | 3.5 - 15.99 | ≥16 |

---

### Appendix D: Variants Excluded from BA1, BS1, and PM3 (Appendix 4)

Variants excluded from criteria BA1, BS1, and PM3 that require PM2_Supporting to be met.

| HGVS name | ithaID | Common name | Regions with high prevalence | PMIDs |
|-----------|--------|-------------|------------------------------|-------|
| NM_000518.5(HBB):c.92+5G>C | 107 | IVS I-5 (G>C) | Middle East, South-East Asia | 9576331, 18294253, 12752111, 26865931 |
| NM_000518.5(HBB):c.-79A>G | 25 | -29 (A>G) | Jamaica | 10691857 |
| NM_000518.5(HBB):c.79G>A | 88 | CD 26 GAG>AAG [Glu>Lys] (Hb E) | South-East Asia | 26402558, 24488783 |
| NM_000518.5(HBB):c.92G>C | 100 | CD 30 (G>C) or IVS I (-1) AGG>ACG (Arg>Thr) | India, Pakistan, Maldives | 23162295 |
| NM_000518.5(HBB):c.118C>T | 142 | CD 39 (CAG>TAG) | Mediterranean | 1734721, 21353607, 18096416 |
| NM_000518.5(HBB):c.126_129delCTTT | 147 | CD 41/42 (-TTCT or -CTTT or -TCTT) | South-East Asia | 24534675, 26079343 |
| NM_000518.5(HBB):c.20A>T | 824 | CD 6 GAG>GTG [Glu>Val] (Hb S) | Africa, South-East Asia, Mediterranean | 28361595, 21353607, 26984585 |
| NM_000518.5(HBB):c.19G>A | 810 | CD 6 GAG>AAG [Glu>Lys] (Hb C) | Africa, South-East Asia | 2606477 |
| NM_000518.5(HBB):c.364G>C | 1217 | CD 121 GAA>CA [Glu>Gln] (Hb D-Punjab) | Middle-East, South Asia | Not provided |
| NM_000518.5(HBB):c.27dupG | 62 | CD 8/9 +G | Middle East | 22460247, 16533735 |
| NM_000518.5(HBB):c.92+1G>A | 101 | IVS I-1 G>A | Mediterranean, Middle-East | 21353607, 27199182, 18096416, 29637841 |
| NM_000518.5(HBB):c.93-21G>A | 113 | IVS I-110 G>A | Mediterranean, Middle-East | 27199182, 21353607 |
| NM_000518.5(HBB):c.92+6T>C | 111 | IVS I-6 (T>C) | Mediterranean, Middle-East | 25408857, 21353607 |

*ithaID: ID assigned by the IthaGenes database; access using https://www.ithanet.eu/db/ithagenes?ithaID=&lt;ithaID&gt;*

---

### Appendix E: Segregation Analysis LOD Scores (Appendix 1)

Applicable where phenocopy or diagnostic clarity is a minor concern.

| | Supporting | Moderate | Strong |
|---|-----------|----------|--------|
| **Likelihood** | 8:1 | 32:1 | 128:1 |
| **LOD Score** | 0.9 | 1.5 | 2.1 |
| **Autosomal recessive threshold** | See table below | See table below | See table below |

#### Autosomal Recessive LOD Score Table

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

---

### Appendix F: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| **BA1** | Allele frequency ≥0.005 (0.5%) in a studied general population with ≥2000 alleles and variant present in ≥5 alleles | Stand Alone |
| **BS1** | Allele frequency ≥0.001 (0.1%) in a studied general population with ≥2000 alleles and variant present in ≥5 alleles | Strong |
| **PM2** | Allele frequency <0.0001 (0.01%) in gnomAD; position must have ≥20x coverage | Supporting |

---

### Appendix G: Key References

| Citation | PMID | Topic |
|----------|------|-------|
| Richards S, Aziz N, et al. Genet Med (2015) 17(5):405-24 | 25741868 | ACMG/AMP Variant Interpretation Guidelines |
| Abou Tayoun AN, Pesaran T, et al. Hum Mutat (2018) 39(11):1517-1524 | 30192042 | ClinGen SVI PVS1 Recommendations |
| Peixeiro I, et al. Haematologica (2011); doi: 10.3324/haematol.2010.039206 | - | NMD boundaries for HBB |
| ClinGen SVI PM3 proposal, version 1 | - | In trans criterion (PM3) point system |
| ClinGen SVI VCEP Review Committee | 29543229 | PP5 and BP6 not for use |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 (1.0.0) | March 20, 2026 | Initial release of the ClinGen Hemoglobinopathy VCEP specifications for HBB |

---

*This document is based on the ClinGen Hemoglobinopathy Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for HBB Version 1.0 (https://cspec.genome.network/cspec/ui/svi/doc/GN170; DOI 10.5281/zenodo.21434787)*
