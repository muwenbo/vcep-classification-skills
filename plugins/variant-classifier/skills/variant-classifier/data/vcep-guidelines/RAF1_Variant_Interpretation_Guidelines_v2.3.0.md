# ClinGen RASopathy Expert Panel Variant Interpretation Guidelines for RAF1

**Version:** 2.3.0
**Released:** 12/3/2024
**Affiliation:** RASopathy VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

**Release Notes:** Submitting Pilot Rules. All pilot variants are attached in the LZTR1 submission. "Observed in ≥5 probands" removed from PM5 at Moderate strength.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | RAF1 (HGNC:9829) |
| **HGNC Name** | Raf-1 proto-oncogene, serine/threonine kinase |
| **Transcript** | NM_002880.4 |
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

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

Caveats:
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:**

***Not Applicable***

**Comments:** Not applicable. Loss of function is not an established disease mechanism for RAF1-associated RASopathy. The disease mechanism is gain-of-function.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

Example: Val->Leu caused by either G>C or G>T in the same codon.

Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Applicable for observed analogous residue positions in *BRAF* and *RAF1*. | Analogous Gene |

> **Supplement format:** `Analogous Residues.xlsx` supplies an image-only alignment of NP_001361187.1 and NP_001341618.1. It does **not** provide a discrete BRAF↔RAF1 residue-pair table. Use the distributed alignment itself; do not infer an exhaustive mapping from this guideline.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PM6 (see Reference 1) and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

#### PS2/PM6 Point System (Per Proband)

| Phenotypic Consistency | Confirmed *de novo* (PS2) | Assumed *de novo* (PM6) |
|------------------------|:-------------------------:|:-----------------------:|
| Phenotype is consistent with a RASopathy* | 2 | 1 |
| Limited phenotypic information** | 1 | 0.5 |
| Phenotype not consistent with RASopathy | 0 | 0 |

\*Exclusive of prenatal cases

\*\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.

#### Evidence Strength Thresholds

> **Source discrepancy — do not resolve silently:** The PDF's displayed PS2 criterion block lists only Very Strong (4), Strong (2), and Moderate (1), while its displayed PM6 block lists only Strong (2), Moderate (1), and Supporting (0.5). The VCEP-distributed `PS2_PM6 Scoring.jpg` extends the common scale to all four strengths for either criterion, explicitly including **PS2_Supporting at 0.5** and **PM6_VeryStrong at 4**. The scoring image prints exact point values without comparator symbols. Both source presentations are reproduced below; the distributed package does not state which controls when they differ.

| Points | Strength Level |
|--------|----------------|
| 0.5 | Supporting (PS2_Supporting or PM6_Supporting) |
| 1.0 | Moderate (PS2_Moderate or PM6) |
| 2.0 | Strong (PS2 or PM6_Strong) |
| 4.0 | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Very Strong** | 4 Points | Strength |
| **Strong** | 2 Points | None |
| **Moderate** | 1 Point | Strength |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Approved assays are available in the supplemental materials.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Two or more different approved assays | Disease-specific, Gene-specific, Strength |
| **Supporting** | One approved assay | Disease-specific, Gene-specific, Strength |

#### Approved Assay Instances for RAF1

| Assay | Applicable Genes | PMID | Readout | Approved Strength |
|-------|-------------------|------|---------|-------------------|
| **MEK Activation Assay** | RAF1 (and other RASopathy genes) | 17603482 (Razzaque 2007) | pMEK/MEK ratio basally and/or after RTK stimulation; abnormal = constitutively active, increased phosphorylation, and/or prolonged phosphorylation | PS3_Supporting; BS3_NA |
| **ERK Activation Assay** | RAF1 (and other RASopathy genes) | 17603482, 17603483 (Razzaque, Pandit 2007) | pERK/ERK ratio basally and/or after RTK stimulation; abnormal = constitutively active, increased phosphorylation, and/or prolonged phosphorylation | PS3_Supporting; BS3_NA |
| **RAF1 Kinase Activity** | RAF1 | 17603482, 17603483 (Razzaque, Pandit 2007) | Phosphorylation of substrate in a coupled kinase assay; abnormal = increased substrate phosphorylation | PS3_Supporting; BS3_NA |

> **Note:** Each approved assay counts as PS3_Supporting. Two or more different approved assays = PS3_Moderate. BS3 is not applicable for RAF1 functional studies.

> **General workbook guidance:** The performing laboratory is expected to validate each assay with appropriate controls (PMID: 31892348). Because most assays are semi-quantitative, abnormal results are compared with controls of known status. Pathway-specific assays may use controls from any RASopathy gene; gene-specific assays require gene-specific controls. Assays not listed in the workbook are presumed to lack sufficient historical evidence and may only be sufficient for PS3_Supporting or BS3_Supporting. Animal models and variant-specific assays are excluded from the approved list. Two or more **unique assay types** support PS3_Moderate.

**MEK Activation Assay Details (RAF1 column):**
- **Source:** PMID 17603482; DOI 10.1038/ng2078; Razzaque, 2007
- **Material:** HEK293T/17 cells “Transfected with with” [sic] 4.5 μg plasmid DNA and Lipofectamine LTX reagent
- **Readout:** Semi-quantitative (Qualitative); pMEK/MEK ratio basally and/or after RTK stimulation
- **Replicates:** Biological replicates not met; technical replicates met, with data representing three independent experiment [sic]
- **Controls:** WT positive control; vector negative control; P/LP controls S257L, P261S, P261A, V263A, and L613V; no B/LB controls
- **Statistics and thresholds:** No statistical analysis; normal WT pattern versus constitutively active, increased phosphorylation protein, and/or prolonged phosphorylation

**ERK Activation Assay Details (RAF1 column):**
- **Source:** PMIDs 17603482 and 17603483; DOIs 10.1038/ng2078 and 10.1038/ng2073; Razzaque and Pandit, 2007
- **Material:** HEK293T/17 cells “Transfected with with” [sic] 4.5 μg plasmid DNA and Lipofectamine LTX reagent
- **Readout:** Semi-quantitative (Qualitative); pERK/ERK ratio basally and after RTK stimulation
- **Replicates:** Biological replicates not met; technical replicates met, with data representing three independent experiment [sic]
- **Controls:** WT positive control; vector negative control; P/LP controls S257L, P261S, P261A, V263A, L613V, and T491I; D486N (NA) listed as the B/LB control
- **Statistics and thresholds:** No statistical analysis; normal WT pattern versus constitutively active, increased phosphorylation protein, and/or prolonged phosphorylation

**RAF1 Kinase Activity Assay Details:**
- **Source:** PMIDs 17603482 and 17603483; DOIs 10.1038/ng2078 and 10.1038/ng2073; Razzaque and Pandit, 2007
- **Material:** HEK293 cells transfected at 70% confluence with 4.5 μg plasmid DNA and Lipofectamine LTX reagent
- **Readout type:** Semi-quantitative (Qualitative)
- **Readout:** Phosphorylation of substrate in a coupled kinase assay; normal = normal substrate phosphorylation; abnormal = increased substrate phosphorylation
- **Biological replicates:** Not met
- **Technical replicates:** Met; three independent experiments
- **Positive control:** WT
- **Negative control:** Vector/Nontransfected
- **Validation controls P/LP:** S257L (P), P261A (P/LP), P261S (P), V263A (P/LP), L613V (P)
- **Validation controls B/LB:** D486N (NA) and T491I (P) — kinase impaired
- **Statistical analysis:** None

> **Workbook inconsistency:** In the `RAF1 Kinase Activity` sheet, the row headed “Validation controls B/LB (#)” lists two kinase-impaired variants, but labels D486N as NA and **T491I as P**, not B/LB. The `ERK Activation Assay` sheet separately places T491I among P/LP controls. These source entries are reported without reclassification.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.

Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** Strength adjustment using point-based scoring for autosomal dominant cases with phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

#### PS4 Point System (Per Proband)

| Phenotypic Consistency | Points per Proband |
|------------------------|:------------------:|
| Individual well-phenotyped with features of a RASopathy | 1 |
| Limited phenotypic information compatible with RASopathy* | 0.5 |
| No clinical information or isolated clinical features | 0 |
| Well-phenotyped but consistent with non-RASopathy disorder** | -1 |

\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.

\*\*Negative points for PS4 represent proband affected with a non-RASopathy congenital disorder rather than a healthy individual (BS2). This typically applies to probands tested by exome analysis with multiple other clinical features supporting a distinct syndromic disorder (e.g. CHARGE, CdLS).

#### PS4 Evidence Strength Thresholds

| Points | Strength Level |
|--------|----------------|
| ≥1.0 | PS4_Supporting |
| ≥3.0 | PS4_Moderate |
| ≥5.0 | PS4 (Strong) |

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | ≥5 points | Disease-specific |
| **Moderate** | ≥3 points | Strength |
| **Supporting** | ≥1 points | Strength |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation. PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Applicable only to critical and well-established functional domains available in the supplementary table: **CR2 domain [AA 251-266/exon7], exon 14, exon 17**. Not applicable to specific amino acid residues (see PM5). | Gene-specific |

> **Important:** PM1 and PM5 may be used in conjunction at moderate levels. PM1 may **not** be applied if PM5_Strong is applied, to avoid overweighting.

> **Distributed-package limitation:** Although the PDF says the domains are available in a supplementary table, the RAF1 package contains no dedicated PM1 domain table. The three locations above are transcribed from the PDF criterion row itself.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | The variant must be absent from controls (gnomAD). | Strength |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

***Not Applicable***

**Comments:** Not applicable. RAF1-associated RASopathy follows autosomal dominant inheritance.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | No known repetitive areas in gene. Use as described. | General recommendation |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

Example: Arg156His is pathogenic; now you observe Arg156Cys.

Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** Applicable for observed analogous residue positions in *BRAF* and *RAF1*. PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | ≥2 different [likely] pathogenic residues changes at the same codon observed in ≥5 probands. | Analogous Gene, Strength |
| **Moderate** | 1 [likely] pathogenic residue change at the same codon. | Analogous Gene, Disease-specific |

> **Note:** Analogous residue positions between BRAF and RAF1 are applicable for this criterion. When PM5_Strong is applied, PM1 may **not** be applied to avoid overweighting.

> **Source wording:** “residues changes” is preserved verbatim from the PDF and appears to be a typographical error.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PS2 (see Reference 1) and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

Use the same point-based system as PS2 — see [PS2/PM6 Point System](#ps2pm6-point-system-per-proband) above.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | 2 Points | Strength |
| **Moderate** | 1 Point | None |
| **Supporting** | 0.5 Points | Strength |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** Segregation in more than one family is recommended.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | ≥7 informative meioses | Strength |
| **Moderate** | ≥5 informative meioses | Strength |
| **Supporting** | ≥3 informative meioses | Disease-specific |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**

***Not Applicable***

**Comments:** Not applicable because missense z score is <3.09 in gnomAD.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:** For missense variants: REVEL ≥ 0.7. For splicing impact, predicted outcome must match disease mechanism.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | For missense variants: REVEL ≥ 0.7. For splicing impact, predicted outcome must match disease mechanism. | Disease-specific |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

***Not Applicable***

**Comments:** Not applicable, see PS4.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:**

***Not Applicable***

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PubMed: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Stand Alone** | gnomAD filtering allele frequency **≥0.05%** | Disease-specific |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | gnomAD filtering allele frequency **≥0.025%** | Disease-specific |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** Strength adjustment using point-based scoring based on phenotypic specifications. Phenotypic specifications: based on healthy homozygote or heterozygote individuals, reduced points for apparently unaffected heterozygous individuals, applicable to parent or sibling samples during clinical family evaluations.

#### BS2 Point System (Per Individual)

| Phenotypic Consistency | Points per Individual |
|------------------------|:---------------------:|
| Healthy homozygous individual assessed for a RASopathy | -3 |
| Healthy heterozygous individual assessed for a RASopathy | -1 |
| No phenotypic information other than "unaffected" heterozygote* | -0.25 |
| No clinical information or nonspecific clinical features | 0 |

\*Typically applicable to parental or sibling samples during clinical family evaluations.

#### BS2 Evidence Strength Thresholds

> **Source contradiction — do not resolve silently:** The PDF body assigns **BS2 Strong at -4 points** and **BS2 Supporting at -1 point**. The VCEP-distributed `BS2 Scoring.jpg` instead assigns **BS2 Strong at -3.0 points**, Supporting at -1, and says Moderate is not available. Neither presentation prints a comparator for these strength totals. The body values and image values are both reproduced below; the distributed package does not say which is operative.

| Points | Strength Level |
|--------|----------------|
| -1 points | Supporting (BS2_Supporting) |
| N/A | Moderate (N/A) |
| -3.0 points | Strong (BS2) |

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | -4 Points | Strength |
| **Supporting** | -1 Point | Strength |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

***Not Applicable***

**Comments:** Approved functional studies are available for each individual gene in the supplemental material. Additional functional studies can be submitted to the expert panel for approval. BS3 is not applicable for RAF1 as all approved assays specify BS3_NA.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:** Lack of segregation in affected members of a family.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Requires only one informative meiosis. | General recommendation |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specifications |
|-----------|--------|----------------|
| **BP1** | Applicable (Modified) | Truncating, LOF variant in a gene for which primarily missense, GOF variants are known to cause disease. This rule has contraindications for use with RASopathies. Given the disease mechanism is gain-of-function for RASopathies, BP1 should be used for any truncating variant (nonsense, frameshift, affects canonical splice sites, initiation codon, entire gene or multi-exon deletion) in genes without established LOF correlation to disease. See the supplemental material regarding dosage sensitivity information for each individual gene and potential association to disorders associated with LOF variants. **(Supporting)** |
| **BP2** | Applicable (Modified) | Points are awarded for an alternative molecular cause of a RASopathy in the same gene (and/or in conjunction with BP5) and the phenotype is consistent with expected severity of the RASopathy. **Supporting:** ≥(-1) Point; **Moderate:** ≥(-2) Points; **Strong:** ≥(-4) Points. |
| **BP3** | Not Applicable | No known benign repetitive areas in RASopathy genes. |
| **BP4** | Applicable (Modified) | For missense variants: REVEL ≤0.3. For splicing variants: predicted outcome is negligible or does not match disease mechanism. **(Supporting)** |
| **BP5** | Applicable (Modified) | Points are awarded for an alternative molecular cause of a RASopathy in a different gene (and/or in conjunction with BP2) and the phenotype is consistent with expected severity of the RASopathy. Points are also awarded for phenotypes inconsistent with a RASopathy and fully explained by a different causative variant (e.g. WES testing). **Supporting:** ≥(-1) Point; **Moderate:** ≥(-2) Points; **Strong:** ≥(-4) Points. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PubMed: 29543229) |
| **BP7** | Applicable | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. This rule is also applicable for intronic positions (except canonical splice sites) or non-coding variants and should be used in conjunction with BP4. **(Supporting)** |

> **Distributed-package limitation (BP1):** The PDF directs users to supplemental dosage-sensitivity information and gene-specific disorders associated with LoF variants. No dedicated dosage-sensitivity or RAF1 LoF-disorder table is present in the distributed RAF1 package. Do not infer the missing information.

#### BP5/BP2 Point System (Per Individual)

| Phenotypic Consistency | Points per Individual |
|------------------------|:---------------------:|
| Phenotype inconsistent with a RASopathy and causative variant has been identified, **-or-** Molecular cause of a RASopathy is identified in a different RASopathy gene, **-or-** Molecular cause of a RASopathy is identified in *trans* or *cis* with the variant being classified | -1 |
| Phenotype inconsistent with a RASopathy and no causative variant identified/reported | 0 |

#### BP5/BP2 Evidence Strength Thresholds

> **Source contradiction — do not resolve silently:** The PDF body assigns Strong at **≥(-4)**, Moderate at **≥(-2)**, and Supporting at **≥(-1)** for both BP2 and BP5. The VCEP-distributed `BP5_BP2 Scoring.jpg` instead assigns Strong at **-3.0**, says Moderate is **N/A**, and assigns Supporting at **-1**. The body explicitly prints inclusive `≥` operators; the image prints exact values with no comparator symbols. The criterion summary above preserves the PDF-body values, while the table below reproduces the supplied image. The distributed package does not identify an operative presentation.

| Points | Strength Level |
|--------|----------------|
| -1 points | Supporting (BP5/BP2) |
| N/A | Moderate (N/A) |
| -3.0 points | Strong (BP5_Strong / BP2_Strong) |

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PS2_VeryStrong)* **AND** ≥1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* |
| 1 Very Strong *(PS2_VeryStrong)* **AND** ≥2 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Very Strong *(PS2_VeryStrong)* **AND** 1 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* **AND** 1 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3)* |
| 1 Very Strong *(PS2_VeryStrong)* **AND** ≥2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3)* |
| ≥2 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** ≥3 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** 2 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* **AND** ≥2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** 1 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* **AND** ≥4 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3)* |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong *(PS2_VeryStrong)* **AND** 1 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** 1 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* |
| 1 Strong *(PS1, PS2, PS4, PM5_Strong, PM6_Strong, PP1_Strong)* **AND** ≥2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3)* |
| ≥3 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* |
| 2 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* **AND** ≥2 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3)* |
| 1 Moderate *(PS2_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)* **AND** ≥4 Supporting *(PS3_Supporting, PS4_Supporting, PM2_Supporting, PM6_Supporting, PP1, PP3)* |

### Benign Classification

| Criteria Combination |
|---------------------|
| ≥2 Strong *(BS1, BS2, BS4, BP2_Strong, BP5_Strong)* |
| 1 Stand Alone *(BA1)* |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong *(BS1, BS2, BS4, BP2_Strong, BP5_Strong)* **AND** 1 Supporting *(BS2_Supporting, BP1, BP2, BP4, BP5, BP7)* |
| ≥2 Supporting *(BS2_Supporting, BP1, BP2, BP4, BP5, BP7)* |
| 1 Strong *(BS1, BS2, BS4, BP2_Strong, BP5_Strong)* |
| 1 Strong *(BS1)* |

---

## Appendices

### Appendix A: Criteria Applicability Summary

| Criterion | Status | Max Strength |
|-----------|--------|--------------|
| PVS1 | Not Applicable | — |
| PS1 | Applicable | Strong |
| PS2 | Applicable (Point-based) | Very Strong |
| PS3 | Applicable (Modified) | Moderate |
| PS4 | Applicable (Point-based) | Strong |
| PM1 | Applicable (Gene-specific domains) | Moderate |
| PM2 | Applicable (Supporting only) | Supporting |
| PM3 | Not Applicable | — |
| PM4 | Applicable | Moderate |
| PM5 | Applicable (Analogous Gene) | Strong |
| PM6 | Applicable (Point-based) | Strong in PDF criterion block; scoring image also labels Very Strong |
| PP1 | Applicable | Strong |
| PP2 | Not Applicable | — |
| PP3 | Applicable | Supporting |
| PP4 | Not Applicable | — |
| PP5 | Not Applicable | — |
| BA1 | Applicable | Stand Alone |
| BS1 | Applicable | Strong |
| BS2 | Applicable (Point-based) | Strong |
| BS3 | Not Applicable | — |
| BS4 | Applicable | Strong |
| BP1 | Applicable (Modified) | Supporting |
| BP2 | Applicable (Point-based) | Strong |
| BP3 | Not Applicable | — |
| BP4 | Applicable | Supporting |
| BP5 | Applicable (Point-based) | Strong |
| BP6 | Not Applicable | — |
| BP7 | Applicable | Supporting |

### Appendix B: PM1 Functional Domains for RAF1

> **⚠️ NOT IN DISTRIBUTED PACKAGE — could not be source-verified.** The existing guideline labeled exons 14 and 17 as “Kinase domain,” but the distributed PDF identifies only **exon 14** and **exon 17**, without a domain name, and the package contains no dedicated PM1 supplemental table. The plausible labels are retained below only as unverified local context; the PDF wording is authoritative.

| PDF wording | Amino Acid Range | Exon | Unverified existing label |
|-------------|------------------|------|---------------------------|
| CR2 domain | AA 251-266 | Exon 7 | CR2 domain |
| Domain not specified | — | Exon 14 | Kinase domain |
| Domain not specified | — | Exon 17 | Kinase domain |

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.05% (gnomAD FAF) | Stand Alone |
| BS1 | ≥0.025% (gnomAD FAF) | Strong |
| PM2 | Absent from gnomAD | Supporting |

### Appendix D: Approved Functional Studies Summary for RAF1

| Assay | Gene(s) | PS3 Strength | BS3 Strength |
|-------|---------|-------------|-------------|
| MEK Activation Assay | RAF1 | Supporting | N/A |
| ERK Activation Assay | RAF1 | Supporting | N/A |
| RAF1 Kinase Activity | RAF1 | Supporting | N/A |

> **Scoring:** One approved assay = PS3_Supporting. Two or more different approved assays = PS3_Moderate. BS3 is not applicable for any RAF1 assay.

The workbook also contains other RASopathy-gene assay columns plus hidden template/example, comparison, AKT, animal-model, and myristoylation sheets. Those sheets were inspected but do not define additional approved RAF1 assay types. The hidden animal-model sheet lists RAF1 mouse models but marks animal models “weight less”; the workbook `READ ME` says animal models are excluded from the approved assays.

### Appendix E: Computational Predictors

| Predictor | Pathogenic Threshold (PP3) | Benign Threshold (BP4) |
|-----------|---------------------------|------------------------|
| REVEL | ≥0.7 | ≤0.3 |

For splicing impact: predicted outcome must match disease mechanism (PP3) or predicted outcome is negligible/does not match disease mechanism (BP4).

### Appendix F: Reference PMIDs

| PMID | Reference |
|------|-----------|
| 29543229 | Citation supplied by the PDF for the PP5/BP6 non-use recommendation |
| 17603482 | Razzaque et al., 2007 — RAF1 functional studies |
| 17603483 | Pandit et al., 2007 — RAF1 functional studies |

### Appendix G: References

1. ClinGen SVI Proposal for De Novo Criteria: https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf

### Appendix H: Source-Fidelity Notes

The following source conflicts and package gaps remain unresolved because the VCEP-distributed materials do not choose between them:

1. `PS2_PM6 Scoring.jpg` includes PS2_Supporting and PM6_VeryStrong, while those strengths are absent from the respective displayed criterion blocks in the PDF. The PDF's criteria-combination rules name PS2_VeryStrong, but not PM6_VeryStrong.
2. The PDF body assigns BS2 Strong at -4; `BS2 Scoring.jpg` assigns it at -3.0.
3. The PDF body assigns BP2/BP5 Strong ≥(-4), Moderate ≥(-2), and Supporting ≥(-1); `BP5_BP2 Scoring.jpg` instead gives Strong -3.0, Moderate N/A, and Supporting -1 without comparator symbols.
4. `Approved Functional Studies.xlsx` lists T491I (P) in a RAF1 kinase row headed “Validation controls B/LB (#),” while its ERK sheet lists T491I among P/LP controls.
5. The PDF cites a PM1 supplementary table and BP1 dosage-sensitivity supplement that are not present as dedicated files in the distributed RAF1 package.
6. `Analogous Residues.xlsx` supplies an image alignment but no discrete BRAF↔RAF1 residue map. Its hidden SOS1/SOS2 working sheets do not define RAF1 analogous positions.

These are reports of the distributed sources, not reconciliations or inferred rules.

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| 2.3.0 | 12/3/2024 | Submitting Pilot Rules. "Observed in ≥5 probands" removed from PM5 at Moderate strength. |

**Document corrections (2026-08-07), source-verified against `ClinGen_ACMG_Specifications_RAF1_v2.3.pdf`, `Analogous Residues.xlsx`, `Approved Functional Studies.xlsx`, `BP5_BP2 Scoring.jpg`, `BS2 Scoring.jpg`, `PS2_PM6 Scoring.jpg`, and `PS4 Scoring.jpg`. No change to the underlying ClinGen specification version.**

- Reported, without resolving, the PS2/PM6 strength mismatch between the PDF criterion blocks and `PS2_PM6 Scoring.jpg`.
- Reported the BS2 threshold conflict (PDF -4 versus image -3.0) and the BP2/BP5 conflict (PDF ≥-4/≥-2/≥-1 versus image -3/N/A/-1), preserving each source's comparator semantics.
- Added the complete RAF1-relevant assay set and validation limitations from `Approved Functional Studies.xlsx`, including the source's inconsistent placement of T491I under a B/LB-labeled RAF1 kinase row.
- Clarified that `Analogous Residues.xlsx` contains an image alignment, not a discrete residue-pair table, and that its hidden SOS working sheets are not RAF1 rules.
- Marked the absent PM1 and BP1 referenced supplements as distributed-package limitations; retained the existing plausible “Kinase domain” labels only under the required unverified-content warning.
- Restored and flagged the PDF's apparent PM5 typo, “residues changes.”

---

*This document was compiled from ClinGen RASopathy VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
