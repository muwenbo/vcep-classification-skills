# ClinGen RASopathy Expert Panel Variant Interpretation Guidelines for BRAF

**Version:** 2.3.0
**Released:** 12/3/2024
**Affiliation:** RASopathy VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | BRAF (HGNC:1097) |
| **HGNC Name** | B-Raf proto-oncogene, serine/threonine kinase |
| **Transcript** | NM_004333.6 |
| **Disease** | RASopathy (MONDO:0021060) |
| **Inheritance** | Autosomal dominant |

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

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Not Applicable** | Loss of function is not a known mechanism of disease for BRAF-related RASopathies. The disease mechanism is gain-of-function. |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

*Example:* Val->Leu caused by either G>C or G>T in the same codon.

*Caveat:* Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Applicable for observed analogous residue positions in *BRAF* and *RAF1*. |

**Modification Type:** Analogous Gene

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

*Note:* Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PM6 and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests such as WES).

#### PS2/PM6 Point System (Per Proband)

| Phenotypic Consistency | Confirmed *de novo* (PS2) | Assumed *de novo* (PM6) |
|------------------------|---------------------------|-------------------------|
| Phenotype is consistent with a RASopathy* | 2 | 1 |
| Limited phenotypic information** | 1 | 0.5 |
| Phenotype not consistent with RASopathy | 0 | 0 |

*\*Exclusive of prenatal cases*

*\*\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.*

#### PS2/PM6 Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| 0.5 | Supporting (PS2_Supporting or PM6_Supporting) |
| 1.0 | Moderate (PS2_Moderate or PM6) |
| 2.0 | Strong (PS2 or PM6_Strong) |
| 4.0 | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |

> **Source discrepancy (unresolved):** `PS2_PM6 Scoring.jpg` names PS2_Supporting and PM6_VeryStrong, but `ClinGen_ACMG_Specifications_BRAF_v2.3.pdf` does not define either strength. The PDF defines PS2 at Moderate, Strong, and Very Strong and PM6 at Supporting, Moderate, and Strong. Both sources print exact point values without threshold comparators. The image-only strength names are reported without extending the PDF criteria.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

*Note:* Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Approved assays are available in the supplemental materials.

| Strength | Criteria |
|----------|----------|
| **Moderate** | Two or more different approved assays |
| **Supporting** | One approved assay |

**Modification Type:** Disease-specific, Gene-specific, Strength

#### Approved Assay Instances for BRAF

The workbook requires performing-laboratory validation and appropriate controls (PMID 31892348). Most assays are semi-quantitative; results are judged relative to known-status controls. Unlisted assays may only support PS3_Supporting or BS3_Supporting, although all approved BRAF columns explicitly state BS3_NA. Animal models and variant-specific assays are excluded by the workbook's READ ME.

##### 1. BRAF Kinase Activity Assay — PS3_Supporting; BS3_NA

- Source: Rodriguez-Viciana (2006), PMID 16439621, DOI 10.1126/science.1124642.
- Material/readout: HEK293T cells transfected with empty vector, WT B-Raf, or B-Raf mutants; semi-quantitative/qualitative phosphorylation of myelin basic protein in a coupled MEK/ERK2 kinase assay.
- Replication and controls: biological replicates not met; technical replicates met (aggregate of duplicates); WT positive control and vector negative control met; no statistical analysis.
- P/LP validation controls: Q257R (P), S467A (P), L485F (P), K499E (P/LP).
- `Validation controls B/LB` row: E501G (P/LP), G596V (P).
- Normal: normal MBP phosphorylation. Abnormal: increased MBP phosphorylation.

##### 2. MEK Activation Assay — PS3_Supporting; BS3_NA

- Sources: Rodriguez-Viciana (2006) and Sarkozy (2009), PMIDs 16439621 and 19206169, DOI 10.1126/science.1124642 and 10.1002/humu.20955.
- Material/readout: HEK293 cells transiently transfected with WT or variant; semi-quantitative/qualitative pMEK/MEK ratio basally and/or after RTK stimulation.
- Replication and controls: biological and technical replicates met (three independent experiments, each performed in duplicate); WT positive and vector negative controls met; no statistical analysis.
- P/LP validation controls: T241P (P/LP), Q257R (P), S467A (P), L485F (P), K499E (P/LP), W531C (P), L597V (P), T599R (P), K601Q (P).
- `Validation controls B/LB` row: E275K (P/LP), G466E (LP/VUS), G466V (P/LP), G469E (P), E501G (P/LP), D594V (P), G596V (P).
- Normal: normal WT pattern. Abnormal: abnormal pattern indicating constitutively active, increased phosphorylation protein, and/or prolonged phosphorylation.

##### 3. ERK Activation Assay — PS3_Supporting; BS3_NA

- Sources: Rodriguez-Viciana (2006) and Sarkozy (2009), PMIDs 16439621 and 19206169, DOI 10.1126/science.1124642 and 10.1002/humu.20955.
- Material/readout: HEK293 cells transiently transfected with WT or variant; semi-quantitative/qualitative pERK/ERK ratio basally and after RTK stimulation.
- Replication and controls: biological and technical replicates met (three independent experiments, each performed in duplicate); WT positive and vector negative controls met; no statistical analysis.
- P/LP validation controls: Q257R (P), S467A (P), L485F (P), K499E (P/LP), T599R (P), K601Q (P).
- `Validation controls B/LB` row: T241P (P/LP), E275K (P/LP), G466V (P/LP), G466E (LP/VUS), G469E (P), E501G (P/LP), W531C (P), D594V (P), G596V (P), L597V (P).
- Normal: normal WT pattern. Abnormal: constitutively active, increased phosphorylation protein, and/or prolonged phosphorylation.

> **Source control conflict:** Across all three approved BRAF assays, entries in rows labelled `Validation controls B/LB` are themselves labelled P, P/LP, or LP/VUS. The labels and their row placement are transcribed without reclassifying or moving the controls.

> **Workbook contradiction (unresolved):** The READ ME excludes animal models, but the hidden BRAF `Animal Models` column says `Approved assay (y/n): y` and gives the non-ACMG phrase `Proposed strength: weight less`. The animal models are not included among the three approved assay types because the workbook's operative policy excludes them; the contradictory hidden entry is reported rather than silently reconciled.

> **Workbook scope note:** BRAF has no RAS Activation Assay column. The hidden AKT sheet is explicitly unapproved and NRAS-only; the hidden cell-survival sheet is dummy example data (PMID 1234567, Jones, 1985); and the hidden myristoylation material is excluded by workbook policy.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

*Note 1:* Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

*Note 2:* In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** Strength adjustment using point-based scoring for autosomal dominant cases with phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information.

#### PS4 Point System (Per Proband)

| Phenotypic Consistency | Points per Proband |
|------------------------|-------------------|
| Individual well-phenotyped with features of a RASopathy | 1 |
| Limited phenotypic information compatible with RASopathy* | 0.5 |
| No clinical information or isolated clinical features | 0 |
| Well-phenotyped but consistent with non-RASopathy disorder** | -1 |

*\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.*

*\*\*Negative points for PS4 represent proband affected with a non-RASopathy congenital disorder rather than a healthy individual (BS2). This typically applies to probands tested by exome analysis with multiple other clinical features supporting a distinct syndromic disorder (e.g. CHARGE, CdLS).*

#### PS4 Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| ≥1.0 | Supporting (PS4_Supporting) |
| ≥3.0 | Moderate (PS4_Moderate) |
| ≥5.0 | Strong (PS4) |

> **Comparator note:** The inclusive `≥` thresholds come from `ClinGen_ACMG_Specifications_BRAF_v2.3.pdf`. `PS4 Scoring.jpg` prints exact 1.0, 3.0, and 5.0 values without comparators. The image's omission is reported rather than used to remove the PDF operators.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation. PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.

| Strength | Criteria |
|----------|----------|
| **Moderate** | Applicable only to critical and well-established functional domains: **Exon 6**, **Exon 11**, **P-loop [AA 459-474]**, **CR3 activation segment [AA 594-627]**. Not applicable to specific amino acid residues (see PM5). |

**Modification Type:** Gene-specific

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

*Caveat:* Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | The variant must be absent from controls (gnomAD). |

**Modification Type:** Strength

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

*Note:* This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Not Applicable** | BRAF-related RASopathies follow autosomal dominant inheritance. This criterion is not applicable. |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | No known repetitive areas in gene. Use as described for in-frame deletions/insertions in a non-repeat region or stop-loss variants. |

**Modification Type:** General recommendation

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

*Example:* Arg156His is pathogenic; now you observe Arg156Cys.

*Caveat:* Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** Applicable for observed analogous residue positions in *BRAF* and *RAF1*. PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥2 different [likely] pathogenic residues changes at the same codon observed in ≥5 probands |
| **Moderate** | 1 [likely] pathogenic residue change at the same codon |

**Modification Type:** Analogous Gene, Strength (Strong), Disease-specific (Moderate)

> **Source wording note:** The typo `residues changes` is preserved verbatim. The release note removed `observed in ≥5 probands` only from PM5 at Moderate strength; it remains in the Strong row.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PS2 and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests such as WES).

| Strength | Criteria |
|----------|----------|
| **Strong** | 2 Points |
| **Moderate** | 1 Point |
| **Supporting** | 0.5 Points |

*See [PS2/PM6 Point System](#ps2pm6-point-system-per-proband) above for point scoring details.*

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

*Note:* May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** Segregation in more than one family is recommended.

| Strength | Criteria |
|----------|----------|
| **Strong** | ≥7 informative meioses |
| **Moderate** | ≥5 informative meioses |
| **Supporting** | ≥3 informative meioses |

**Modification Type:** Strength (Strong, Moderate), Disease-specific (Supporting)

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Missense z score is >3.09 in gnomAD |

**Modification Type:** Disease-specific

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

*Caveat:* As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | For missense variants: **REVEL ≥0.7**. For splicing impact, predicted outcome must match disease mechanism. |

**Modification Type:** Disease-specific

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Not Applicable** | Not applicable, see PS4 for phenotype-based scoring. |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Not Applicable** | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229) |

---

## Benign Criteria

### BA1 - Allele Frequency >5%

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

**VCEP Specifications:** Strength adjustment using point-based scoring based on phenotypic specifications. Phenotypic specifications: based on healthy homozygote or heterozygote individuals, reduced points for apparently unaffected heterozygous individuals, applicable to parent or sibling samples during clinical family evaluations.

#### BS2 Point System (Per Individual)

| Phenotypic Consistency | Points per Individual |
|------------------------|----------------------|
| Healthy homozygous individual assessed for a RASopathy | -3 |
| Healthy heterozygous individual assessed for a RASopathy | -1 |
| No phenotypic information other than "unaffected" heterozygote* | -0.25 |
| No clinical information or nonspecific clinical features | 0 |

*\*Typically applicable to parental or sibling samples during clinical family evaluations.*

#### BS2 Evidence Strength Thresholds

`ClinGen_ACMG_Specifications_BRAF_v2.3.pdf` defines:

| Points | Strength Level |
|--------|----------------|
| -1 point (operator unstated) | Supporting (BS2_Supporting) |
| -4 points (operator unstated) | Strong (BS2) |

`BS2 Scoring.jpg` defines:

| Points | Strength Level |
|--------|----------------|
| -1 point (operator unstated) | Supporting (BS2_Supporting) |
| N/A | Moderate |
| -3.0 points (operator unstated) | Strong (BS2) |

> **Source contradiction (unresolved):** BS2 Strong is -4 points in the PDF but -3.0 points in the attached image. Neither source supplies an inclusive or strict comparator. Both presentations are retained without inventing `≤`.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Not Applicable** | Approved functional studies are available for each individual gene in the supplemental material. Additional functional studies can be submitted to the expert panel for approval. The approved BRAF assays do not currently support BS3 application. |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

*Caveat:* The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Requires only one informative meiosis (lack of segregation with disease) |

**Modification Type:** General recommendation

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Modified | Truncating, LOF variant in a gene for which primarily missense, GOF variants are known to cause disease. This rule has contraindications for use with RASopathies. Given the disease mechanism is gain-of-function, BP1 should be used for any truncating variant (nonsense, frameshift, affects canonical splice sites, initiation codon, entire gene or multi-exon deletion) in genes without established LOF correlation to disease. See supplemental material regarding dosage sensitivity. |
| **BP2** | Modified | Points are awarded for an alternative molecular cause of a RASopathy in the same gene (and/or in conjunction with BP5) and the phenotype is consistent with expected severity of the RASopathy. **Strong:** ≥ (-4) Points; **Moderate:** ≥ (-2) Points; **Supporting:** ≥ (-1) Point |
| **BP3** | Not Applicable | No known benign repetitive areas in RASopathy genes. |
| **BP4** | Modified | For missense variants: **REVEL ≤0.3**. For splicing variants: predicted outcome is negligible or does not match disease mechanism. |
| **BP5** | Modified | Points are awarded for an alternative molecular cause of a RASopathy in a different gene (and/or in conjunction with BP2) and the phenotype is consistent with expected severity of the RASopathy. Points are also awarded for phenotypes inconsistent with a RASopathy and fully explained by a different causative variant (e.g. WES testing). **Strong:** ≥ (-4) Points; **Moderate:** ≥ (-2) Points; **Supporting:** ≥ (-1) Point |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229) |
| **BP7** | Modified | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. This rule is also applicable for intronic positions (except canonical splice sites) or non-coding variants and should be used in conjunction with BP4. |

> **Unavailable referenced material (BP1):** The specification refers to supplemental dosage-sensitivity information, but no dosage-sensitivity document is present in the complete BRAF package. No BRAF-specific dosage claim is inferred.

> **Source presentation note (BP4):** The PDF's VCEP summary includes the missense and splicing rules, while the Supporting row repeats only the missense rule. Both source statements are retained without treating the shorter row as a retraction.

#### BP5/BP2 Point System

| Phenotypic Consistency | Points per Individual |
|------------------------|----------------------|
| Phenotype inconsistent with a RASopathy and causative variant has been identified, **-or-** Molecular cause of a RASopathy is identified in a different RASopathy gene, **-or-** Molecular cause of a RASopathy is identified in *trans* or *cis* with the variant being classified | -1 |
| Phenotype inconsistent with a RASopathy and no causative variant identified/reported | 0 |

#### BP5/BP2 Evidence Strength Thresholds

`ClinGen_ACMG_Specifications_BRAF_v2.3.pdf` defines both BP2 and BP5 as:

| Points | Strength Level |
|--------|----------------|
| ≥(-1) | Supporting |
| ≥(-2) | Moderate |
| ≥(-4) | Strong |

`BP5_BP2 Scoring.jpg` instead defines:

| Points | Strength Level |
|--------|----------------|
| -1 point (operator unstated) | Supporting (BP5/BP2) |
| N/A | Moderate |
| -3.0 points (operator unstated) | Strong (BP5_Strong/BP2_Strong) |

> **Source contradiction (unresolved):** The PDF and image disagree on Moderate availability and the Strong value. The PDF explicitly uses `≥`; the image supplies no comparator. Both are reported without harmonization or an invented image operator.

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PS2_VeryStrong) **AND** ≥1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Very Strong (PS2_VeryStrong) **AND** ≥2 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Very Strong (PS2_VeryStrong) **AND** 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** 1 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3) |
| 1 Very Strong (PS2_VeryStrong) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3) |
| ≥2 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** ≥3 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 2 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3) |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PS2_VeryStrong) **AND** 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3) |
| ≥3 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 2 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3) |
| 1 Moderate (PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** ≥4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP2, PP3) |

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

---

## Appendices

### Appendix A: PM1 Functional Domains for BRAF

| Domain | Amino Acid Range | Notes |
|--------|------------------|-------|
| Exon 6 | - | Critical functional domain |
| Exon 11 | - | Critical functional domain |
| P-loop | AA 459-474 | Critical functional domain |
| CR3 activation segment | AA 594-627 | Critical functional domain |

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.05% gnomAD filtering allele frequency | Stand Alone |
| BS1 | ≥0.025% gnomAD filtering allele frequency | Strong |
| PM2 | Absent from gnomAD | Supporting |

### Appendix C: Computational Prediction Thresholds

| Criterion | Tool | Threshold | Strength |
|-----------|------|-----------|----------|
| PP3 | REVEL | ≥0.7 | Supporting (Pathogenic) |
| BP4 | REVEL | ≤0.3 | Supporting (Benign) |
| PP2 | gnomAD missense z-score | >3.09 | Supporting (Pathogenic) |

### Appendix D: Analogous Genes

PS1 and PM5 may be applied using observed analogous residue positions between:
- **BRAF**
- **RAF1**

Refer to the "Analogous Residues" supplementary documentation for specific residue mappings.

The visible `RAF alignment ` sheet contains two embedded full-protein alignment images. They print accessions NP_001361187.1 (ending at residue 807) and NP_001341618.1 (ending at residue 668), but do not print gene labels beside the accessions. The specification identifies the analogous genes as BRAF and RAF1. The workbook does not identify pathogenic residues or provide an approved codon-by-codon PM5 list.

> **Package scope note:** The hidden sheets `SOS variants from HGMD` and `SOS variants case counts` contain unrelated SOS1/SOS2 counts and unfinished notes. They are not BRAF/RAF1 evidence.

### Appendix E: Approved Functional Studies Summary

| Assay | Gene | PS3 Strength | BS3 Strength |
|-------|------|--------------|--------------|
| BRAF Kinase Activity | BRAF | Supporting | N/A |
| MEK Activation Assay | BRAF | Supporting | N/A |
| ERK Activation Assay | BRAF | Supporting | N/A |

**Note:** Two or more different approved assays are required for PS3_Moderate.

### Appendix F: References

1. ACMG/AMP original criteria reproduced by the specification (Richards et al., 2015).

2. ClinGen Sequence Variant Interpretation VCEP Review Committee recommendation cited by the specification: PMID 29543229.

3. SVI Recommendation for de novo criteria: https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf

4. BRAF functional-assay source cited by `Approved Functional Studies.xlsx`: Rodriguez-Viciana (2006), PMID 16439621, DOI 10.1126/science.1124642.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.3.0 | 2026-08-07 | **Document corrections.** Replaced generic, source-contradicting MEK/ERK assay prose with exact BRAF kinase, MEK, and ERK citations, methods, strengths, controls, and mixed-control findings from `Approved Functional Studies.xlsx`; documented its hidden animal-model contradiction and excluded sheets; restored the PDF's PS4 `≥` comparators and PM5_Strong typo/qualifier from `ClinGen_ACMG_Specifications_BRAF_v2.3.pdf`; reported unresolved PS2/PM6, BS2, and BP2/BP5 differences verified against the PDF, `PS2_PM6 Scoring.jpg`, `PS4 Scoring.jpg`, `BS2 Scoring.jpg`, and `BP5_BP2 Scoring.jpg`; removed unsupported decimal frequency conversions and full bibliographic provenance; restored the omitted general one-Strong Likely Benign rule; verified both embedded BRAF/RAF1 alignment images and excluded unrelated hidden SOS sheets from `Analogous Residues.xlsx`; documented the absent BP1 dosage-sensitivity attachment after checking the complete package. |
| 2.3.0 | 12/3/2024 | Submitting Pilot Rules. All pilot variants are attached in the LZTR1 submission. "Observed in ≥5 probands" removed from PM5 at Moderate strength. |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
