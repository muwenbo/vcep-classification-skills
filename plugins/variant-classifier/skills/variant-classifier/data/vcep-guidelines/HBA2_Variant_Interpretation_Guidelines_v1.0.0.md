# Comprehensive Variant Interpretation Guidelines for HBA2

## ClinGen Hemoglobinopathy VCEP Specifications for HBA2-related Alpha Thalassemia Spectrum (Version 1.0)

**Affiliation:** Hemoglobinopathy Variant Curation Expert Panel (Hemoglobinopathy VCEP)
**Version:** 1.0
**Release Date:** March 20, 2026
**Status:** Released
**DOI:** 10.5281/zenodo.21434790
**Specification:** GN173
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
   - [BS2 - Observed in Healthy Individual](#bs2---observed-in-healthy-individual)
   - [BS3 - Functional Studies (Benign)](#bs3---functional-studies-benign)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP2 - Observed in cis with Pathogenic Variant](#bp2---observed-in-cis-with-pathogenic-variant)
   - [BP4 - Computational Evidence (Benign)](#bp4---computational-evidence-benign)
   - [BP7 - Synonymous Variants](#bp7---synonymous-variants)
4. [Not Applicable Criteria](#4-not-applicable-criteria)
5. [Rules for Combining Criteria](#5-rules-for-combining-criteria)
6. [Appendices](#6-appendices)

---

## 1. Gene and Disease Information

| Parameter | Value |
|-----------|-------|
| **Gene** | HBA2 (HGNC:4824) |
| **HGNC Name** | hemoglobin subunit alpha 2 |
| **Reference Transcript** | NM_000517.6 |
| **Disease** | HBA2-related alpha thalassemia spectrum |
| **MONDO ID** | MONDO:0100562 |
| **Mode of Inheritance** | Autosomal recessive inheritance |
| **Mechanism of Disease** | Loss of function (established as a disease mechanism for haemoglobinopathies) |

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specification:**

- Use the Hemoglobinopathy VCEP PVS1 decision tree (HBA2-specific, adapted from Tayoun et al. 2018).
- Loss of function has been established as a disease mechanism for haemoglobinopathies.

**Caveats (retained from ACMG):**

- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.

#### Strength Levels Available

| Strength | Modification Type |
|----------|-------------------|
| **PVS1** (Very Strong) | No change |
| **PVS1_Strong** | Disease-specific, Gene-specific, Strength |
| **PVS1_Moderate** | Disease-specific, Gene-specific, Strength |
| **PVS1_Supporting** | Not specified by VCEP |

#### HBA2 PVS1 Decision Tree

##### Nonsense or Frameshift Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| Predicted to undergo NMD — nonsense (or frameshift-induced PTC) located 5' to p.Leu84 (c.251) | **PVS1** |
| Not predicted to undergo NMD (PTC at or 3' to p.Leu84 / c.251) + truncated/altered region is critical to protein function | **PVS1_Strong** |
| Not predicted to undergo NMD + role of region in protein function is unknown + variant removes >10% of protein | **PVS1_Strong** |
| Not predicted to undergo NMD + role of region in protein function is unknown + variant removes <10% of protein | **PVS1_Moderate** |

**Note on NMD prediction:** The borders between NMD-activating and NMD-resistant nonsense mutations in HBA2 and HBA1 are undefined (DOI: 10.1016/j.biocel.2017.07.014). Follow the recommendations published by Tayoun et al. 2018, whereby NMD prediction is based on the premature termination codon not occurring in the 3'-most exon or the 3'-most 50 bp of the penultimate exon.

##### Splice Site Variants (GT-AG ±1,2)

| Condition | PVS1 Strength |
|-----------|---------------|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD (stop codon or disruption 5' to p.Leu84 / c.251) | **PVS1** |
| Exon skipping or use of a cryptic splice site preserves reading frame | **PVS1_Strong** |

##### Initiation Codon Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| Initiation codon variant | **PVS1** |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specification:** A variant classification must have a minimum of two-star annotation in ClinVar to be considered established, or be a VCEP consensus recommendation.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PS1** (Strong) | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change | No change |
| **PS1_Moderate** | The same change of an amino acid shown to be a pathogenic variant in a paralogue gene | Disease-specific, Gene-specific, Strength |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

- Both maternal and paternal samples must be tested and shown to be the biological parents of the affected individual. Otherwise, identity is assumed, and not confirmed, and PM6 applies.
- Only applicable in the absence of any other established pathogenic variants. If other suspicious variants are present, then PM6 should be used instead. Should not be used in combination with PM6.
- Definition of trait phenotype is provided in Appendix 3.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PS2** (Strong) | *De novo* (both maternity and paternity confirmed) in a patient with the disease **or in a phenotypic trait individual** and no family history | Disease-specific, Gene-specific |

**Note:** No PS2/PM6 point-based system is specified by this VCEP; only the Strong (PS2) and Moderate (PM6) levels shown are defined.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specification:** The list of approved functional studies is provided in Appendix 2 (Functional Studies).

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PS3_Supporting** | *In vitro* or *in vivo* functional studies supportive of a damaging effect on the gene, gene product, expression levels and protein function | Disease-specific, Gene-specific, Strength |

**Note:** PS3 is only available at Supporting strength for HBA2. PS3_Strong and PS3_Moderate are not specified by the VCEP.

#### Approved Functional Assays (Appendix 2)

The following functional studies are approved by the Haemoglobinopathy VCEP. The panel will be constantly assessing available evidence for potential approval of additional assays.

**Assay #1 — Haemoglobin stability test**

| Field | Value |
|-------|-------|
| Measured parameter | Hb stability |
| Readout description | Reduced stability, precipitation in isopropanol or after heating at 50 °C |
| Readout type | Qualitative |
| Deleterious result range | Presence of precipitate, visible to the naked eye |
| Deleterious result strength | **PS3_Supporting** |
| Benign result range | Clear; possibly <5% precipitate at 50 °C/30 min |
| Benign result strength | **BS3_Supporting** |
| Notes | False-positive or doubtful results if HbF levels >3%, and by prolonged storage due to methaemoglobin formation. Hyper-unstable Hb variants are rapidly destroyed, hence not readily detected by stability tests. In these cases, no functional evidence should be applied. |
| References | Dacie and Lewis Practical Haematology, 9th Ed. |

**Assay #2 — Biosynthesis assay**

| Field | Value |
|-------|-------|
| Measured parameter | Globin synthesis |
| Readout description | Change in biosynthetic ratio of globins (Thalassaemia) |
| Readout type | Quantitative |
| Deleterious result range | α0 thal trait: β/α 1.44 (1.22–1.82); HbH: β/α 2.30 (1.80–2.95) |
| Deleterious result strength | **PS3_Supporting** |
| Benign result range | β/α 0.96 (0.78–1.14) |
| Benign result strength | **BS3_Supporting** |
| Notes | β/α values apply for subjects ≥2 years of age |
| References | Old J. et al., Prevention of Thalassaemias and Other Haemoglobin Disorders: Vol. 2: Laboratory Protocols, 2nd Ed. |

**Assay #3 — Haemoglobin electrophoresis, HPLC**

| Field | Value |
|-------|-------|
| Measured parameter | Detection and quantification of variant haemoglobins |
| Readout description | Change in electrophoretic mobilities, or change in relative peak area and rate of elution (retention time) AND quantification |
| Readout type | Quantitative |
| Deleterious result range | Not concordant with normal chromatogram or readout. Hb X <15% |
| Deleterious result strength | **PS3_Supporting** |
| Benign result range | Concordant with normal chromatogram or readout |
| Benign result strength | **BS3_Supporting** |
| Notes | Do not apply only for the detection of variant haemoglobins, or for the quantification of normal haemoglobins A, F and A2 |
| References | Dacie and Lewis Practical Haematology, 9th Ed. |

**Assay #4 — In vitro splicing assay**

| Field | Value |
|-------|-------|
| Measured parameter | Alternative RNA splicing |
| Readout description | Splicing pattern with i) autoradiograms of radiolabeled minigene constructs, ii) long-read RNA sequencing |
| Readout type | Quantitative |
| Deleterious result range | Abnormal splice product detected (wild-type and aberrant transcripts are present) |
| Deleterious result strength | **PS3_Supporting** |
| Benign result range | No abnormal splice product detected (only wild-type RNA transcript is present) |
| Benign result strength | **BS3_Supporting** |
| Notes | Beware of abnormal transcripts that lead to truncated proteins (PP4) without functional consequences, and cell systems where NMD is not active |
| References | PMID: 24549662 |

**Assay #5 — In vitro cell-based assay**

| Field | Value |
|-------|-------|
| Measured parameter | Gene expression (luciferase/fluorescence, RNA, protein) |
| Readout description | Transfection of erythroid cell cultures (e.g., K562, HEL, HUDEP-2) with constructs bearing i) reporter cassettes with mutated promoter, 5'UTR and enhancer sequences or ii) a cloned mutant human globin gene. Show changes in gene expression using appropriate methods |
| Readout type | Qualitative / Quantitative |
| Deleterious result range | Changes in the expression level of the reporter gene or transgene in comparison to normal levels |
| Deleterious result strength | **PS3_Supporting** |
| Benign result range | No changes in the expression level of the reporter gene or transgene in comparison to normal levels |
| Benign result strength | **BS3_Supporting** |
| Notes | Also applies to RNA studies with cells from heterozygous or homozygous probands (wild-type, aberrant transcript detection) |
| References | Not specified |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.
**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specification:** Strength of evidence is determined by points according to Appendix 3 (Evaluation of phenotypes in heterozygotes).

| Strength | Point Requirement | Modification Type |
|----------|-------------------|-------------------|
| **PS4_VeryStrong** | ≥16 points | Disease-specific, Gene-specific, Strength |
| **PS4** (Strong) | 3.5–15.99 points | Disease-specific, Gene-specific |
| **PS4_Moderate** | 1.5–3.49 points | Disease-specific, Gene-specific, Strength |
| **PS4_Supporting** | 0.5–1.49 points | Disease-specific, Gene-specific, Strength |

#### Appendix 3: Evaluation of Phenotypes in Heterozygotes (PS4 Point Table)

**Note:** When evaluating cases be aware of potential complex genotype interactions.

Disease: alpha thalassemia [AR]

| Evidence | Parameter | Impact threshold | Alternative terms | Points per case | Max | Comment |
|----------|-----------|------------------|-------------------|-----------------|-----|---------|
| Reduced MCV; Reduced MCH | MCV (fL); MCH (pg) | <79; <27 | Microcytosis; Hypochromia | 0.15 | 1.5 | Primarily for thalassaemias and thalassaemic Hb variants. Do not use if the RBC count is decreased or iron deficiency is present |
| Reduced MCV; Reduced MCH; Normal HbA2 | MCV (fL); MCH (pg); HbA2 (%) | <79; <27; <3 (normal) | Microcytosis; Hypochromia | 0.15 | 1.5 | Caution needed for other possible causes, e.g. iron deficiency, beta+ and delta thalassaemia or large beta-locus deletions. Do not use if the RBC count is decreased or iron deficiency is present |
| Reduced MCV; Reduced MCH; Normal or increased RBC count | MCV (fL); MCH (pg); RBC (10^12/L) | <79; <27; 4.7–6.1 for men (normal), 4.2–5.4 for women (normal) | Microcytosis; Hypochromia | 0.2 | 1.6 | Primarily for thalassaemias and thalassaemic Hb variants. Do not use if there is an indication of recent correction of iron deficiency |
| Reduced MCV; Reduced MCH excluding iron deficiency (i.e. normal serum ferritin, transferrin saturation, TIBC) | MCV (fL); MCH (pg) | <79; <27 | Microcytosis; Hypochromia | 0.3 | 3 | Primarily for thalassaemias and thalassaemic Hb variants |

\* Only consider independent (unrelated) cases. Multiple cases in a family are counted as one.
\*\* Do NOT use multiple point levels for the same case.

##### Point Sum and Evidence Strength

| Supporting | Moderate | Strong | Very Strong |
|------------|----------|--------|-------------|
| 0.5–1.49 | 1.5–3.49 | 3.5–15.99 | ≥16 |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specification:**

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PM1** (Moderate) | Located in a mutational hot spot and/or critical and well-established functional domain without benign variation. HBA2-specific regions: <br>• AHSP binding (α32R, α104H, α118F, α120P) <br>• Poly(A) signals: AATAAA sequence | Disease-specific, Gene-specific |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification:** Position of reported variant must have sufficient coverage (>= 20x) in the population database.

| Strength | Threshold | Modification Type |
|----------|-----------|-------------------|
| **PM2_Supporting** | Allele frequency **<0.0001 (0.01%)** in gnomAD | Disease-specific, Gene-specific, Strength |

---

### PM3 - In Trans with Pathogenic Variant

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

- Strength is determined using the ClinGen SVI guidelines ([SVI proposal for PM3 criterion, version 1.0](https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf)).
- Both variants must meet the PM2_Supporting specification, i.e. be sufficiently rare, unless they are in the exception list (Appendix 4), or present in gnomAD with <20x genomic coverage.
- Phase is confirmed *in trans* by testing both or one parent, and the pathogenicity of the variant on the other allele must have at least 2-star rating in ClinVar or VCEP consensus recommendation.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PM3_VeryStrong** | For recessive disorders, detected *in trans* with a pathogenic or likely pathogenic variant in an affected patient. Strength is determined using the ClinGen SVI guidelines | Strength |
| **PM3_Strong** | As above; strength determined using ClinGen SVI guidelines | Strength |
| **PM3** (Moderate) | As above; strength determined using ClinGen SVI guidelines | No change |
| **PM3_Supporting** | As above; strength determined using ClinGen SVI guidelines | Strength |

**Note:** This VCEP does not restate the PM3 point table; point assignment and strength thresholds follow the ClinGen SVI PM3 recommendation (version 1.0) referenced above.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

- Relevant for stop codon mutations leading to elongated α-chains (e.g., Hb Constant Spring) and in-frame deletions of a complete codon (leading to deletion of a single amino acid in an otherwise functional haemoglobin variant).
- Should not be used if PVS1 has been applied.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PM4** (Moderate) | Protein length changes as a result of in-frame deletions/insertions in a non-repeat region or stop-loss variants | No change |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

- Beware of changes that impact splicing rather than at the amino acid/protein level. Assess potential for creation of exonic splicing event using *in silico* splicing prediction tools, as described in PP3/BP4.
- A previously established variant as pathogenic must have at least 2-star rating in ClinVar or VCEP consensus recommendation.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PM5** (Moderate) | Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before, **or base change at a non-coding position and previous pathogenic mutation has been seen before**. Examples: Arg156His is pathogenic; now you observe Arg156Cys. Non-coding variant g.15300G>C is pathogenic, now you observe g.15300G>A. | Disease-specific, Gene-specific |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

- In contrast to PS2, identity testing was NOT performed in parental samples to confirm identity, which is assumed.
- Should not be used in combination with PS2.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PM6** (Moderate) | Assumed *de novo*, but without confirmation of paternity and maternity | No change |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

- LOD score for recessive disorder can be estimated from the tables in Appendix 1 (Segregation Analysis), based on the number of affected and unaffected individuals.
- Caution needed when counting segregations in the presence of other possible disease-causing variants. Compound heterozygous individuals are counted only if phase is confirmed to be *in trans*.

| Strength | LOD Score Requirement | Likelihood | Modification Type |
|----------|-----------------------|------------|-------------------|
| **PP1_Strong** | LOD score >2.1 | 128:1 | Disease-specific, Gene-specific, Strength |
| **PP1_Moderate** | LOD score >1.5 | 32:1 | Disease-specific, Gene-specific, Strength |
| **PP1** (Supporting) | LOD score >0.9 | 8:1 | Disease-specific, Gene-specific |

#### Appendix 1: Autosomal Recessive LOD Score Table

Phenocopy or diagnostic clarity is a minor concern.

| Affected segregations \ Unaffected segregations | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
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

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specification:**

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **PP3** (Supporting) | Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).<br>• **Missense:** REVEL score > 0.8 **OR** SpliceAI > 0.3. If REVEL score is not available, use CADD PHRED score > 23.5<br>• **Non-coding, synonymous, in-frame indels, stop-lost:** CADD PHRED score > 12 **OR** SpliceAI DS > 0.3<br>• Should **not** be used for LOF variants considered in PVS1 | Disease-specific, Gene-specific |

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification:**

- Use the Filtering AF, such as Popmax FAF from gnomAD. If the variant is present at high frequency in the non-continental population (e.g., Ashkenazi Jews), you can calculate the filtering allele frequency using a 95% confidence interval by selecting "Inverse AF" at http://cardiodb.org/allelefrequencyapp/
- Variants in Appendix 4 are excluded from this criterion.

| Strength | Threshold |
|----------|-----------|
| **BA1** (Stand Alone) | Allele frequency **≥0.005 (0.5%)** in a studied general population with **≥2000 alleles** and variant present in **≥5 alleles** |

##### Calculation Parameters (for α-haemoglobinopathies, autosomal recessive)

- Prevalence: 1/1000 (the highest reported prevalence of the disease)
- Genetic heterogeneity: 75% (HBA2 is affected in around 75% of pathogenic variants – from IthaGenes database)
- Allelic heterogeneity: 15% (i.e. a single variant responsible for all of cases)
- Penetrance: 80% (to account for silent variants and for underdiagnosis of Hb H disease)

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification:**

- Use the Filtering AF, such as Popmax FAF from gnomAD. If the variant is present at high frequency in the non-continental population (e.g. Ashkenazi Jews), you can calculate the filtering allele frequency using a 95% confidence interval by selecting "Inverse AF" at http://cardiodb.org/allelefrequencyapp/
- Variants in Appendix 4 are excluded from this criterion.

| Strength | Threshold |
|----------|-----------|
| **BS1** (Strong) | Allele frequency **≥0.001 (0.1%)** in a studied general population with **≥2000 alleles** and variant present in **≥5 alleles** |

##### Calculation Parameters (for α-haemoglobinopathies, autosomal recessive)

- Prevalence: 1/3000 (the highest reported prevalence of the disease)
- Genetic heterogeneity: 75% (HBA2 is affected in around 75% of pathogenic variants – from IthaGenes database)
- Allelic heterogeneity: 5% (variants in the exclusion list are not considered)
- Penetrance: 80% (to account for silent variants and for underdiagnosis of Hb H disease)

---

### BS2 - Observed in Healthy Individual

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

- Normal haematological values are provided in Appendix 3.
- The healthy individual must be well-phenotyped/well-documented to rule out any mild symptoms and ensure that the individual is unaffected. A full-blood count and Hb characterization are required to exclude variants and/or abnormal quantities.
- In compound heterozygous individuals, only established pathogenic variants should be considered (i.e. at least 2-star rating in ClinVar).
- Applies to subjects over 2 years of age.
- **BS2:** Only applicable if no coinheritance is detected of an HBB pathogenic variant.
- **BS2_P (Supporting):** Only applicable if no well-established disease-modifying mutations are detected.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **BS2** (Strong) | Two independent occurrences in individuals (asymptomatic or with trait phenotype) for a recessive (homozygous or compound heterozygous) disorder, with full penetrance expected at early age | Disease-specific, Gene-specific |
| **BS2_Supporting** | Observation in one individual (asymptomatic or with trait phenotype) for a recessive (homozygous or compound heterozygous) disorder, with full penetrance expected at early age | Disease-specific, Gene-specific, Strength |

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specification:** The list of approved functional studies can be found in Appendix 2 (Functional Studies) — see [PS3 section](#ps3---functional-studies).

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **BS3_Supporting** | *In vivo* or *in vitro* functional studies show no damaging effect on gene, gene product, expression levels and protein function | Disease-specific, Gene-specific, Strength |

**Note:** BS3 is only available at Supporting strength for HBA2.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **BS4** (Strong) | Lack of segregation in affected members of a family | No change |

---

### BP2 - Observed in cis with Pathogenic Variant

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

**VCEP Specifications:**

- Do not use when the variant has only ever been observed *in cis* with a pathogenic variant as its significance/severity in isolation is unknown.
- Only applies when the phenotype is not more severe than when either of the two variants are seen in isolation.
- Use only if in cis with variants classified as pathogenic in ClinVar with at least two-star rating.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **BP2** (Supporting) | Observed *in cis* with a pathogenic variant in any inheritance pattern | No change |

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **BP4** (Supporting) | Multiple lines of computational evidence suggest no impact on gene or gene product.<br>• **Missense:** REVEL score < 0.7 **AND** SpliceAI DS ≤ 0.3 (if REVEL score is not available, use CADD PHRED score ≤ 20, instead)<br>• **Non-coding, synonymous, in-frame indels, stop-lost:** CADD PHRED score ≤ 11 **AND** SpliceAI DS ≤ 0.3 | Disease-specific, Gene-specific |

---

### BP7 - Synonymous Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

**VCEP Specification:** Synonymous variant with no impact on splicing (SpliceAI ≤0.3) AND GERP++ <0 for conservation.

| Strength | Application | Modification Type |
|----------|-------------|-------------------|
| **BP7** (Supporting) | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved | No change |

---

## 4. Not Applicable Criteria

The following ACMG/AMP criteria are **NOT APPLICABLE** for HBA2 variant interpretation:

| Criterion | Original Purpose | Reason Not Applicable |
|-----------|-----------------|----------------------|
| **PP2** | Missense in gene with low rate of benign missense variation | Not applicable per VCEP |
| **PP4** | Phenotype/family history highly specific for disease | Not applicable per VCEP |
| **PP5** | Reputable source reports pathogenic | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |
| **BP1** | Missense in truncating disease gene | Not applicable per VCEP |
| **BP3** | In-frame deletions/insertions in a repetitive region without known function | Not applicable per VCEP |
| **BP5** | Variant found in a case with an alternate molecular basis for disease | Not applicable per VCEP |
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
| 1 Strong AND 2 Moderate | **Likely Pathogenic** |

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

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| **BA1** | Allele frequency ≥0.005 (0.5%) in a studied general population with ≥2000 alleles and variant present in ≥5 alleles | Stand Alone |
| **BS1** | Allele frequency ≥0.001 (0.1%) in a studied general population with ≥2000 alleles and variant present in ≥5 alleles | Strong |
| **PM2_Supporting** | Allele frequency <0.0001 (0.01%) in gnomAD (position must have ≥20x coverage) | Supporting |

### Appendix B: Variants Excluded from BA1, BS1 and PM3 (Appendix 4 of the specification)

Variants excluded from criteria BA1, BS1, and PM3 that require PM2_Supporting to be met:

| HGVS name | ithaID | Common name | Regions with high prevalence | PMIDs |
|-----------|--------|-------------|------------------------------|-------|
| NM_000517.6(HBA2):c.95+2_95+6delTGAGG | 359 | IVS I-1 (-5 bp) GAGGTGAGG>GAGG ----- donor | Mediterranean, Middle-East | 26261699, 27199182 |

\*ithaID: ID assigned by the IthaGenes database; access using https://www.ithanet.eu/db/ithagenes?ithaID=&lt;ithaID&gt;

### Appendix C: Key References

| Citation | PMID | Topic |
|----------|------|-------|
| Richards S, Aziz N et al. Standards and guidelines for the interpretation of sequence variants. *Genet Med* (2015) 17(5):405-24 | 25741868 | ACMG/AMP Variant Interpretation Guidelines |
| Abou Tayoun AN, Pesaran T et al. Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. *Hum Mutat* (2018) 39(11):1517-1524 | 30192042 | ClinGen SVI PVS1 Recommendations |
| ClinGen SVI VCEP Review Committee | 29543229 | PP5/BP6 not for use |
| In vitro splicing assay reference (Appendix 2) | 24549662 | Functional evidence |
| Variant exclusion list (Appendix 4) | 26261699, 27199182 | HBA2 c.95+2_95+6delTGAGG |

### Appendix D: Supplementary Documents in the Specification

| Document | Content |
|----------|---------|
| PVS1 decision tree | HBA2-specific recommendations for application of PVS1 (adapted from Tayoun et al. 2018) |
| Appendix 1 — Segregation analysis | LOD score table for autosomal recessive segregation (PP1) |
| Appendix 2 — Functional studies | Approved PS3/BS3 assays |
| Appendix 3 — Evaluation of phenotypes in heterozygotes | PS4 point table; normal haematological values used for BS2 |
| Appendix 4 — Exclusion variants | Variants excluded from BA1, BS1, PM3 |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | March 20, 2026 | Initial release of the ClinGen Hemoglobinopathy VCEP specifications for HBA2 |

---

*This document is based on the ClinGen Hemoglobinopathy Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for HBA2 Version 1.0 (GN173; DOI: 10.5281/zenodo.21434790).*
