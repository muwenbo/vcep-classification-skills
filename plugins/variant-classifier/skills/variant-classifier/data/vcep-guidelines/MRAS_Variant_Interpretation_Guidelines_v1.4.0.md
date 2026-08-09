# ClinGen RASopathy Expert Panel Variant Interpretation Guidelines for MRAS

**Version:** 1.4.0
**Released:** 12/3/2024
**Affiliation:** RASopathy VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines
**DOI:** 10.5281/zenodo.21434125
**Source package reviewed:** `ClinGen_ACMG_Specifications_MRAS_v1.4.pdf`, `Analogous Residues.pdf`, `Approved Functional Studies.xlsx`, `PS2_PM6 Scoring.jpg`, `PS4 Scoring.jpg`, `BS2 Scoring.jpg`, and `BP5_BP2 Scoring.jpg`

**Release Notes:** These are the ACMG/AMP variant classification specifications developed by the RASopathy VCEP for MRAS. Pilot variants are included in the LZTR1 submission. “Observed in ≥5 probands” removed from PM5 at Moderate strength.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | MRAS (HGNC:7227) |
| **HGNC Name** | muscle RAS oncogene homolog |
| **Transcript** | NM_001085049.3 |
| **Disease** | RASopathy (MONDO:0021060) |
| **Inheritance** | Autosomal dominant inheritance |

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
   - [BA1 - Allele Frequency Stand Alone](#ba1---allele-frequency-stand-alone)
   - [BS1 - Frequency Greater Than Expected](#bs1---frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (No Effect)](#bs3---functional-studies-no-effect)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP1 - Truncating Variant in GOF Gene](#bp1---truncating-variant-in-gof-gene)
   - [BP2 - Observed in Trans/Cis](#bp2---observed-in-transcis)
   - [BP3 - In-frame in Repetitive Region](#bp3---in-frame-in-repetitive-region)
   - [BP4 - Computational Evidence (No Impact)](#bp4---computational-evidence-no-impact)
   - [BP5 - Alternate Molecular Basis](#bp5---alternate-molecular-basis)
   - [BP6 - Reputable Source (Benign)](#bp6---reputable-source-benign)
   - [BP7 - Synonymous Variant](#bp7---synonymous-variant)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | Not applicable. The VCEP gives no MRAS-specific rationale in the PVS1 row; its BP1 rule separately describes the RASopathy mechanism as gain-of-function. |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Applicable for observed analogous residue positions in HRAS, KRAS, MRAS, NRAS, RIT1, and RRAS2. |

**Modification Type:** Analogous Gene

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

Follow SVI recommendations for point-based scoring in conjunction with PM6 (see Reference 1) and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed *de novo* (PS2) | Assumed *de novo* (PM6) |
|------------------------|---------------------------|-------------------------|
| Phenotype is consistent with a RASopathy* | 2 | 1 |
| Limited phenotypic information** | 1 | 0.5 |
| Phenotype not consistent with RASopathy | 0 | 0 |

*\*Exclusive of prenatal cases*

*\*\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.*

#### Strength Ladder in `PS2_PM6 Scoring.jpg`

The image prints exact totals without inequality comparators:

| Points | Strength Level |
|--------|----------------|
| 0.5 points | Supporting (PS2_Supporting or PM6_Supporting) |
| 1.0 point | Moderate (PS2_Moderate or PM6) |
| 2.0 points | Strong (PS2 or PM6_Strong) |
| 4.0 points | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |

#### Strength Levels in the Main PDF

| Criterion | Published strengths and point totals |
|-----------|--------------------------------------|
| **PS2** | Very Strong: 4; Strong: 2; Moderate: 1 |
| **PM6** | Strong: 2; Moderate: 1; Supporting: 0.5 |

The main PDF also prints bare totals without inequality comparators.

> **SOURCE CONTRADICTION / OMISSION — do not silently resolve:** `PS2_PM6 Scoring.jpg` defines PS2 Supporting at 0.5 point and PM6 Very Strong at 4 points, but those strengths are absent from the main PDF's PS2 and PM6 strength rows. Keep the image-only tiers distinct and do not infer `>=`.

**Modification Type:** Strength

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Approved assays are available in the supplemental materials.

| Strength | Criteria |
|----------|----------|
| **Moderate** | Two or more different approved assays. |
| **Supporting** | One approved assay. |

**Modification Type:** Disease-specific, Gene-specific, Strength

#### Approved Functional Assays for MRAS

The following functional studies have been approved by the ClinGen RASopathy CDWG VCEP for application of PS3/BS3 criteria:

| Assay | General Description | Assay Specificity |
|-------|---------------------|-------------------|
| **RAS Activation Assay** | Measures the bound RAS protein that immunoprecipitated with RAF1 or RBD (synthetic) | Pathway Specific: Works for genes upstream from RAS and RAS proteins themselves |
| **MEK Activation Assay** | Measures the ratio of phosphorylated MEK to unphosphorylated MEK, basally and following RTK stimulation | Pathway Specific |
| **ERK Activation Assay** | Measures the ratio of phosphorylated ERK to unphosphorylated ERK, basally and following stimulation | Pathway Specific |

**Note:** Two or more unique assay types (i.e. RAS activation assay and MEK activation assay) for a given variant provides sufficient evidence to upgrade PS3 to the Moderate strength.

The workbook also says pathway-specific controls may come from any gene, unlisted assays may be sufficient only for PS3_Supporting/BS3_Supporting, and animal or variant-specific assays are excluded.

##### MRAS-Specific RAS Activation Assay Details

| Parameter | MRAS Specifications |
|-----------|---------------------|
| **PMID** | 28289718 |
| **DOI** | 10.1172/jci.insight.91225 |
| **Author** | Higgins |
| **Year** | 2017 |
| **Material Used** | HEK293T/17 cells: Expression of MRAS was accomplished by transfecting 10 μg MRAS WT or mutant p.Gly23Val-MRAS cDNA with the use of Effectene Transfection Reagent (Qiagen) |
| **Readout Type** | Semi-quantitative (Qualitative) |
| **Readout Description** | The ratio of GTP-MRAS to total MRAS was calculated. The relative MRAS activation for p.Gly23Val-MRAS was calculated by normalizing the WT-MRAS sample to 1. |
| **Biological Replicates** | Not met |
| **Technical Replicates** | Not met |
| **Basic Positive Control** | Met; WT-MRAS |
| **Basic Negative Control** | Not met |
| **Validation Controls (P/LP)** | G23V - Pathogenic |
| **Validation Controls (B/LB)** | None |
| **Statistical Analysis** | Two-tailed Student’s t-test |
| **Threshold (Normal)** | Normal (WT) pattern |
| **Threshold (Abnormal)** | Increased RAS/RBD complexes compared with positive control range in assay. |
| **Approved** | Y |
| **Proposed Strength** | PS3_Supporting; BS3_NA |

##### MRAS MEK Activation Assay Details

| Parameter | MRAS Specifications |
|-----------|---------------------|
| **Citation** | `Based on analogy with other RAS genes/proteins` (the PMID field contains this text) |
| **DOI / Author / Year** | Not supplied |
| **Material Used** | Engineered variants in cell lines, patient cells |
| **Readout Type** | Semi-quantitative (Qualitative) |
| **Readout Description** | pMEK/MEK ratio basally and/or after RTK stimulation |
| **Biological Replicates** | Not Met |
| **Technical Replicates** | Not Met |
| **Basic Positive Control** | Not Met |
| **Basic Negative Control** | Not Met |
| **Validation Controls (P/LP)** | 0 |
| **Validation Controls (B/LB)** | 0 |
| **Statistical Analysis** | Not supplied |
| **Threshold (Normal)** | Normal (WT) pattern |
| **Threshold (Abnormal)** | Abnormal pattern indicating constitutively active, increased phosphorylation protein, and/or prolonged phosphorylation |
| **Approved** | Y |
| **Proposed Strength** | PS3_Supporting; BS3_NA |

##### MRAS ERK Activation Assay Details

| Parameter | MRAS Specifications |
|-----------|---------------------|
| **PMID** | 28289718 |
| **DOI** | `doi:10.1172/jci.insight.91225` |
| **Author / Year** | Higgins / 2017 |
| **Material Used** | HEK293T/17 cells: expression of MRAS by transfecting 10 μg MRAS WT or mutant p.Gly23Val-MRAS cDNA with Effectene Transfection Reagent (Qiagen) according to the manufacturer’s instructions |
| **Readout Type** | Semi-quantitative (Qualitative) |
| **Readout Description** | pERK/ERK ratio basally and after stimulation, compared with controls |
| **Biological Replicates** | not met |
| **Technical Replicates** | not met |
| **Basic Positive Control** | met; WT-MRAS |
| **Basic Negative Control** | not met |
| **Validation Controls (P/LP)** | G23V - P |
| **Validation Controls (B/LB)** | 0 |
| **Statistical Analysis** | 2-tailed Student’s t test with Bonferroni multiple-significance-test correction |
| **Threshold (Normal)** | Normal (WT) Pattern |
| **Threshold (Abnormal)** | Constitutively active, increased phosphorylation protein, and/or prolonged phosphorylation |
| **Approved** | Y |
| **Proposed Strength** | PS3_Supporting; BS3_NA |

> **SOURCE QUALITY WARNING — analogy-only approval and unfinished validation:** `Approved Functional Studies.xlsx` marks all three MRAS assays approved (`Y`). The MEK entry, however, has no study citation, DOI, author, year, controls, or statistical analysis; its citation field says only “Based on analogy with other RAS genes/proteins.” RAS and ERK each use only G23V as a P/LP validation control and have no B/LB control. Replicate and negative-control fields are not met. These source values are transcribed without inventing missing evidence or overriding the published approval.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**

Strength adjustment using point-based scoring for autosomal dominant cases with phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

#### PS4 Point System

| Phenotypic Consistency | Points per Proband |
|------------------------|-------------------|
| Individual well-phenotyped with features of a RASopathy | 1 |
| Limited phenotypic information compatible with RASopathy* | 0.5 |
| No clinical information or isolated clinical features | 0 |
| Well-phenotyped but consistent with non-RASopathy disorder** | -1 |

*\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.*

*\*\*Negative points for PS4 represent proband affected with a non-RASopathy congenital disorder rather than a healthy individual (BS2). This typically applies to probands tested by exome analysis with multiple other clinical features supporting a distinct syndromic disorder. (e.g. CHARGE, CdLS)*

#### PS4 Main-PDF Strength Thresholds

The main PDF explicitly uses inclusive `>=` comparators. The image footer prints exact totals 1.0, 3.0, and 5.0 without operators.

| Points | Strength Level |
|--------|----------------|
| ≥1 points | Supporting (PS4_Supporting) |
| ≥3 points | Moderate (PS4_Moderate) |
| ≥5 points | Strong (PS4) |

**Source typo preserved:** the main PDF prints “≥1 points.”

**Modification Type:** Disease-specific

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation. **PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Applicable only to critical and well-established functional domains available in the supplementary table. Not applicable to specific amino acid residues (see PM5). |

#### MRAS Functional Domains

| Domain | Amino Acid Positions |
|--------|---------------------|
| **P-loop** | AA 20-27 |
| **Switch I (SW1)** | AA 35-50 |
| **Switch II (SW2)** | AA 67-74 |
| **SAK** | Not applicable for PM1 |

`Analogous Residues.pdf` visually aligns an MRAS sequence homologous to the highlighted HRAS 145–156 region, but the MRAS main PDF explicitly says **“no SAK.”** Sequence analogy must not be promoted to an MRAS PM1 domain.

**Modification Type:** Gene-specific

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | The variant must be absent from controls (gnomAD). |

**Modification Type:** Strength

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | Not applicable. MRAS-related RASopathy follows autosomal dominant inheritance. |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | No known repetitive areas in gene. Use as described. |

**Modification Type:** General recommendation

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

Applicable for observed analogous residue positions in HRAS, KRAS, MRAS, NRAS, RIT1, and RRAS2. **PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.**

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥2 different [likely] pathogenic residues changes at the same codon observed in ≥5 probands. |
| **Moderate** | 1 [likely] pathogenic residue change at the same codon. |

**Modification Type:** Analogous Gene, Strength

**Source typo preserved:** the Strong row prints “residues changes.”

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

Follow SVI recommendations for point-based scoring in conjunction with PS2 (see Reference 1) and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

| Strength | Criteria |
|----------|----------|
| **Strong** | 2 Points. |
| **Moderate** | 1 Point. |
| **Supporting** | 0.5 Points. |

*See PS2 section for detailed point system.*

`PS2_PM6 Scoring.jpg` additionally publishes PM6 Very Strong at exactly 4 points; the main PDF has no PM6 Very Strong row. See PS2.

**Modification Type:** Strength

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Segregation in more than one family is recommended.

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥7 informative meioses. |
| **Moderate** | ≥5 informative meioses. |
| **Supporting** | ≥3 informative meioses. |

**Modification Type:** Strength, Disease-specific

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | Not applicable because missense z score is <3.09 in gnomAD. |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | For missense variants: **REVEL ≥ 0.7**. For splicing impact, predicted outcome must match disease mechanism. |

**Modification Type:** Disease-specific

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | Not applicable, see PS4. |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PubMed: 29543229) |

---

## Benign Criteria

### BA1 - Allele Frequency Stand Alone

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | gnomAD filtering allele frequency **≥0.05%** |

**Modification Type:** Disease-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | gnomAD filtering allele frequency **≥0.025%** |

**Modification Type:** Disease-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

Strength adjustment using point-based scoring based on phenotypic specifications. Phenotypic specifications: based on healthy homozygote or heterozygote individuals, reduced points for apparently unaffected heterozygous individuals, applicable to parent or sibling samples during clinical family evaluations.

#### BS2 Point System

| Phenotypic Consistency | Points per Individual |
|------------------------|----------------------|
| Healthy homozygous individual assessed for a RASopathy | -3 |
| Healthy heterozygous individual assessed for a RASopathy | -1 |
| No phenotypic information other than "unaffected" heterozygote* | -0.25 |
| No clinical information or nonspecific clinical features | 0 |

*\*Typically applicable to parental or sibling samples during clinical family evaluations.*

#### BS2 Strength Ladder in `BS2 Scoring.jpg`

The image prints exact totals without inequality comparators:

| Points | Strength Level |
|--------|----------------|
| -1 points | Supporting (BS2_Supporting) |
| N/A | Moderate (N/A) |
| -3.0 points | Strong (BS2) |

#### BS2 Strength Levels in the Main PDF

| Strength | Published point total |
|----------|-----------------------|
| **Strong** | -4 points |
| **Supporting** | -1 point |

Neither main-PDF total carries an inequality comparator.

> **SOURCE CONTRADICTION — do not silently resolve:** BS2 Strong is -4 points in the main PDF but -3.0 points in `BS2 Scoring.jpg`. Both give Supporting at -1 point. No single operative Strong threshold can be selected.

**Modification Type:** Strength

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | The main PDF marks BS3 Not Applicable. Every MRAS assay column in `Approved Functional Studies.xlsx` explicitly records `BS3_NA`; additional functional studies may be submitted to the panel. |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Requires only one informative meiosis. |

**Modification Type:** General recommendation

---

### BP1 - Truncating Variant in GOF Gene

**Original ACMG Summary:** Missense variant in a gene for which primarily truncating variants are known to cause disease.

**VCEP Specifications:**

Truncating, LOF variant in a gene for which primarily missense, GOF variants are known to cause disease.

| Strength | Criteria |
|----------|----------|
| **Supporting** | This rule has contraindications for use with RASopathies. Given the disease mechanism is gain-of-function for RASopathies, BP1 should be used for any truncating variant (nonsense, frameshift, affects canonical splice sites, initiation codon, entire gene or multi-exon deletion) in genes without established LOF correlation to disease. The source refers to supplemental dosage-sensitivity and LoF-disorder information, but it is absent from the distributed MRAS package. |

**Modification Type:** Disease-specific

> **MISSING DISTRIBUTED MATERIAL:** `Analogous Residues.pdf`, `Approved Functional Studies.xlsx`, and the four scoring images contain no MRAS dosage-sensitivity information or LoF-associated disorder list. Do not infer or substitute generic ACMG/AMP content.

---

### BP2 - Observed in Trans/Cis

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

**VCEP Specifications:**

Points are awarded for an alternative molecular cause of a RASopathy in the same gene (and/or in conjunction with BP5) and the phenotype is consistent with expected severity of the RASopathy.

#### BP2 Point System

| Phenotypic Consistency | Points per Individual |
|------------------------|----------------------|
| Phenotype inconsistent with a RASopathy and causative variant has been identified, -or- Molecular cause of a RASopathy is identified in a different RASopathy gene, -or- Molecular cause of a RASopathy is identified in *trans* or *cis* with the variant being classified | -1 |
| Phenotype inconsistent with a RASopathy and no causative variant identified/reported | 0 |

#### BP2 Evidence Strength Thresholds

These are the main-PDF thresholds, with comparators preserved exactly:

| Points | Strength Level |
|--------|----------------|
| ≥(-1) Point | Supporting (BP2) |
| ≥(-2) Points | Moderate (BP2_Moderate) |
| ≥(-4) Points | Strong (BP2_Strong) |

**Modification Type:** Strength

`BP5_BP2 Scoring.jpg` instead publishes Supporting at exactly -1, Moderate as N/A, and Strong at exactly -3. See the unresolved source warning under BP5.

---

### BP3 - In-frame in Repetitive Region

**Original ACMG Summary:** In frame-deletions/insertions in a repetitive region without a known function.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | No known benign repetitive areas in RASopathy genes. |

---

### BP4 - Computational Evidence (No Impact)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | For missense variants: **REVEL ≤0.3**. For splicing variants: predicted outcome is negligible or does not match disease mechanism. |

**Modification Type:** Disease-specific

**Source wording note:** the VCEP summary includes both missense (`REVEL <=0.3`, inclusive) and splicing, but the strength-specific Supporting row repeats only the missense rule. Both are retained; the omission is not treated as withdrawal of the splicing statement.

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

**VCEP Specifications:**

Points are awarded for an alternative molecular cause of a RASopathy in a different gene (and/or in conjunction with BP2) and the phenotype is consistent with expected severity of the RASopathy. Points are also awarded for phenotypes inconsistent with a RASopathy and fully explained by a different causative variant (e.g. WES testing).

#### BP5 Evidence Strength Thresholds

These are the main-PDF thresholds, with comparators preserved exactly:

| Points | Strength Level |
|--------|----------------|
| ≥(-1) Point | Supporting (BP5) |
| ≥(-2) Points | Moderate (BP5_Moderate) |
| ≥(-4) Points | Strong (BP5_Strong) |

**Modification Type:** Strength

#### BP5/BP2 Strength Ladder in `BP5_BP2 Scoring.jpg`

| Points | Strength Level |
|--------|----------------|
| -1 point | Supporting (BP5/BP2) |
| N/A | Moderate |
| -3.0 points | Strong (BP5_Strong/BP2_Strong) |

The image prints exact totals without inequality comparators.

> **SOURCE CONTRADICTION — do not silently resolve:** the main PDF publishes BP2 and BP5 as Strong at `>= (-4)`, Moderate at `>= (-2)`, and Supporting at `>= (-1)`. The image instead publishes Strong at exactly -3.0, Moderate N/A, and Supporting exactly -1. The main PDF's `>=` direction on a negative evidence scale is also operationally anomalous. Both presentations are reported without selecting one.

---

### BP6 - Reputable Source (Benign)

**Original ACMG Summary:** Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:**

| Status | Comment |
|--------|---------|
| **Not Applicable** | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PubMed: 29543229) |

---

### BP7 - Synonymous Variant

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. This rule is also applicable for intronic positions (except canonical splice sites) or non-coding variants and should be used in conjunction with BP4. |

**Modification Type:** General recommendation

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PS2_Very Strong) **AND** ≥1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Very Strong (PS2_Very Strong) **AND** ≥2 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Very Strong (PS2_Very Strong) **AND** 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** 1 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |
| 1 Very Strong (PS2_Very Strong) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |
| ≥2 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** ≥3 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 2 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PS2_Very Strong) **AND** 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |
| ≥3 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 2 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |
| 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3) |

### Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) **AND** 1 Supporting (BS2_Supporting, BP1, BP2, BP4, BP5, BP7) |
| ≥2 Supporting (BS2_Supporting, BP1, BP2, BP4, BP5, BP7) |
| 1 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) |
| 1 Strong (BS1) |

**Published-rule tensions:** the combination tables list PS3_Supporting but omit the separately defined PS3_Moderate. They list BP2/BP5 Supporting and Strong but not Moderate, although the body defines Moderate and the scoring image marks Moderate N/A. The tables above remain as published; these conflicts are not harmonized.

---

## Appendices

### Appendix A: Analogous Residues

The following residues are analogous between genes associated with RASopathies. These alignments can be used for PS1 and PM5 criteria application.

#### Functional Domain Alignment

| Domain | HRAS Positions | MRAS Positions |
|--------|----------------|----------------|
| **P-loop** | AA 10-17 | AA 20-27 |
| **Switch I** | AA 25-40 | AA 35-50 |
| **Switch II** | AA 57-64 | AA 67-74 |

#### Protein Sequence Alignment Reference

| Gene | RefSeq | Notes |
|------|--------|-------|
| HRAS | NP_005334.1 | Reference gene for analogous positions |
| KRAS | NP_004976.2 | |
| MRAS | NP_036351.3 | Target gene |
| NRAS | NP_002515.1 | |
| RIT1 | NP_008843.1 | |
| RRAS2 | NP_036382.2 | |

`Analogous Residues.pdf` consists of two image-based whole-protein alignments rather than a discrete exhaustive residue-pair lookup table. It highlights HRAS-anchored P-loop, Switch I, Switch II, and HRAS 145–156 regions. For MRAS PM1, the main PDF authorizes only AA 20–27, 35–50, and 67–74 and explicitly says “no SAK”; consult the alignment for other PS1/PM5 analogous positions rather than extrapolating PM1 domains.

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Population Database |
|-----------|-----------|----------|---------------------|
| BA1 | ≥0.05% | Stand Alone | gnomAD filtering allele frequency |
| BS1 | ≥0.025% | Strong | gnomAD filtering allele frequency |
| PM2 | Absent | Supporting | gnomAD |

### Appendix C: Computational Predictor Thresholds

| Predictor | Pathogenic Threshold (PP3) | Benign Threshold (BP4) |
|-----------|---------------------------|------------------------|
| **REVEL** | ≥0.7 | ≤0.3 |

### Appendix D: MRAS Functional Domains

| Domain | Amino Acid Range |
|--------|------------------|
| **P-loop** | 20-27 |
| **Switch I (SW1)** | 35-50 |
| **Switch II (SW2)** | 67-74 |
| **SAK** | Not applicable for PM1 (“no SAK”) |

The previous functional descriptions were removed because neither the main PDF nor `Analogous Residues.pdf` supplies them.

### Appendix E: Criteria Applicability Summary

| Criterion | Status | Strength(s) Available |
|-----------|--------|----------------------|
| PVS1 | Not Applicable | - |
| PS1 | Applicable | Strong |
| PS2 | Applicable | Main PDF: Very Strong, Strong, Moderate; scoring image additionally lists Supporting |
| PS3 | Applicable | Moderate, Supporting |
| PS4 | Applicable | Strong, Moderate, Supporting |
| PM1 | Applicable | Moderate |
| PM2 | Applicable | Supporting |
| PM3 | Not Applicable | - |
| PM4 | Applicable | Moderate |
| PM5 | Applicable | Strong, Moderate |
| PM6 | Applicable | Main PDF: Strong, Moderate, Supporting; scoring image additionally lists Very Strong |
| PP1 | Applicable | Strong, Moderate, Supporting |
| PP2 | Not Applicable | - |
| PP3 | Applicable | Supporting |
| PP4 | Not Applicable | - |
| PP5 | Not Applicable | - |
| BA1 | Applicable | Stand Alone |
| BS1 | Applicable | Strong |
| BS2 | Applicable | Strong, Supporting (Strong is -4 in PDF, -3 in image) |
| BS3 | Not Applicable | - |
| BS4 | Applicable | Strong |
| BP1 | Applicable | Supporting |
| BP2 | Applicable | Main PDF: Strong, Moderate, Supporting; image: Strong/Supporting, Moderate N/A |
| BP3 | Not Applicable | - |
| BP4 | Applicable | Supporting |
| BP5 | Applicable | Main PDF: Strong, Moderate, Supporting; image: Strong/Supporting, Moderate N/A |
| BP6 | Not Applicable | - |
| BP7 | Applicable | Supporting |

---

## References

1. ClinGen SVI Proposal for De Novo Criteria v1.1: https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf

2. PMID 29543229 (cited by the source for PP5/BP6 non-use)

3. PMID 28289718; Higgins; 2017; DOI 10.1172/jci.insight.91225 (fields supplied by `Approved Functional Studies.xlsx`)

4. PMID 31892348 (cited in `Approved Functional Studies.xlsx` for functional-evidence guidance)

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 1.4.0 | 12/3/2024 | "Observed in ≥5 probands" removed from PM5 at Moderate strength. Pilot variants are included in the LZTR1 submission. |

> **⚠️ NOT IN DISTRIBUTED PACKAGE — could not be source-verified.**
>
> The prior local guideline recorded “1.1.0 — Prior — Initial specifications.” The v1.4 distributed package does not provide earlier version history, so that plausible historical note is retained here only as unverified provenance.

| Historical version | Date | Unverified local note |
|--------------------|------|-----------------------|
| 1.1.0 | Prior | Initial specifications |

**Document corrections (2026-08-07), source-verified against `ClinGen_ACMG_Specifications_MRAS_v1.4.pdf`, both rendered pages of `Analogous Residues.pdf`, every worksheet (including hidden sheets) in `Approved Functional Studies.xlsx`, `PS2_PM6 Scoring.jpg`, `PS4 Scoring.jpg`, `BS2 Scoring.jpg`, and `BP5_BP2 Scoring.jpg`. No change to the underlying ClinGen specification version.**

- **PS2/PM6 mismatch exposed:** image-only PS2 Supporting and PM6 Very Strong tiers are distinguished from the main-PDF tiers; their bare totals remain comparator-unstated.
- **PS4 comparator restored:** main-PDF inclusive `>=1 / >=3 / >=5` thresholds are separated from the image's exact 1/3/5 footer.
- **BS2 contradiction exposed:** main-PDF -4 Strong and image -3 Strong are both retained and flagged.
- **BP2/BP5 contradiction exposed:** main-PDF `>=(-4) / >=(-2) / >=(-1)` conflicts with image `-3 / N/A / -1`; the anomalous negative-score comparator direction is reported without resolution.
- **Functional evidence completed:** transcribed RAS, MEK and ERK citations, materials, controls, statistics, thresholds, approval and strength fields. The prior document omitted the MEK and ERK detail almost entirely. The analogy-only MEK approval, empty citation metadata, zero controls, unmet validation fields, and sparse RAS/ERK controls are now explicit.
- **PM1/analogy clarified:** preserved MRAS AA 20–27, 35–50, 67–74 and “no SAK”; the aligned HRAS 145–156 homolog is not promoted to an MRAS PM1 domain. Removed unsourced domain-function descriptions.
- **Missing BP1 support documented:** no distributed supplement contains MRAS dosage-sensitivity/LoF-disorder content.
- **Source wording preserved:** restored PM5 “residues changes,” flagged PS4 “≥1 points,” and recorded BP4 and combining-rule split presentations.
- **Fabricated provenance removed:** replaced the full titles/journal details previously supplied for bare or partial workbook citations with the exact PMID/author/year/DOI fields the package provides.
- **Older local history quarantined:** retained the plausible 1.1.0 note only under the required unverified-content banner because the distributed v1.4 package cannot confirm it.

---

*This document was compiled from ClinGen VCEP specifications. For the most current version, please refer to the ClinGen website.*
