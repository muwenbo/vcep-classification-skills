# ClinGen Congenital Myopathies VCEP Variant Interpretation Guidelines for DNM2

**Version:** 1.0.0
**Released:** 8/7/2024
**Affiliation:** Congenital Myopathies VCEP
**DOI:** 10.5281/zenodo.21434746
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | DNM2 (HGNC:2974) |
| **HGNC Name** | dynamin 2 |
| **Transcript** | NM_001005361.3 |
| **Disease** | Centronuclear myopathy (MONDO:0018947) |
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

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **All Levels** | **Not Applicable** |

**Comments:** Loss of function is not a mechanism of disease for DNM2-related AD Centronuclear myopathy.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. No change from original ACMG. |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Very Strong** | No change - use as originally described |
| **Strong** | De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. No change from original ACMG. |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Strong may only be considered for variant-specific mouse models. Currently, no other assays are applicable at this strength. |
| **Moderate** | The two assays from PS3_Supporting may be stacked to reach a Moderate Strength |
| **Supporting** | Two specific assays are currently suggested to be applied at Supporting (see below) |

#### PS3_Supporting specified assays

**1. Oligomerization Assay**
- **Abnormal readout:** Integration of increased dynamin stability compared to wild type dynamin
- **Normal readout:** Dynamin assembly/disassembly dynamics similar to wild type DNM2

> **Source wording note:** `Integration of increased dynamin stability` is reproduced verbatim from `ClinGen_ACMG_Specifications_DNM2_v1.0.pdf`; the source may contain a typo, but the intended wording is not specified.

**2. GTPase Activity Assay**
- **Abnormal readout:** Increased GTPase activity or increased stability compared to wild type dynamin
- **Normal readout:** GTPase activity and stability similar to wild type DNM2

> **Unresolved cross-source wording:** The core PDF allows PS3_Supporting for increased GTPase activity **or increased stability**, whereas the workbook's GTPase-activity sheet defines its abnormal threshold only as increased GTPase activity; increased stability is recorded on the oligomerization sheet. The package does not reconcile this difference.

#### Other Functional Analyses

If not listed above, it is acceptable to use PS3_Supporting for other functional analyses if:
- The assay has been validated by a known pathogenic and benign variant AND
- There is plausible reason that the function the assay is testing relates to the phenotype AND
- The assay conditions are likely to mimic the physiological environment

#### Functional-workbook assay entries

The distributed workbook assigns **Supporting** in each populated `Proposed strength` cell, but every corresponding `Approved assay (y/n)` cell is blank. It therefore does not explicitly mark any entry approved. The workbook also leaves every `Proposed strength (modified)` and `Notes` result cell blank.

| Assay entry | PMID / DOI | Author / year | Proposed Strength | Variants Evaluated |
|-------|------|--------|------|-------------------|
| **Oligomerization** | 20529869 / 10.1074/jbc.C110.130013 | Wang...Albanesi / 2010 | Supporting | p.Glu368Lys, p.Arg369Trp, p.Arg465Trp, p.Ala618Thr |
| **Oligomerization** | 24016602 / 10.1016/j.bbagen.2013.09.001 | James...Jameson / 2014 | Supporting | p.Arg369Trp |
| **GTPase Activity** | 20529869 / 10.1074/jbc.C110.130013 | Wang...Albanesi / 2010 | Supporting | p.Glu368Lys, p.Arg369Trp, p.Arg465Trp, p.Ala618Thr |

##### Oligomerization — PMID 20529869

- **Assay/material:** Recombinant wild-type or variant dynamin 2, produced by cDNA transfection into Sf9 cells to produce recombinant baculoviruses, is diluted in low-salt buffer with and without GTP. Turbidity and/or sedimentation monitor polymer assembly and GTP-dependent disassembly.
- **Readout:** Quantitative; turbidity in OD and sedimentation as percentage of protein pelleted.
- **Replication/controls:** Biological replicates not met; technical replicates met (triplicate measurements from at least two preparations of each variant); wild-type dynamin 2 is the basic positive control; basic negative control not met; one P/LP validation control (p.Arg361Ser), no B/LB validation controls.
- **Statistics:** p values reported, but no details of the statistical test are given.
- **Thresholds:** Normal is assembly/disassembly dynamics similar to wild type DNM2; abnormal is increased dynamin stability compared to wild type DNM2.

##### Oligomerization — PMID 24016602

- **Assay/material:** Fluorescence fluctuation spectroscopy in U2OS cells expressing wild-type and variant EGFP-tagged dynamin 2.
- **Readout:** `Oligomerization units`; the workbook's qualitative/quantitative field is blank.
- **Replication/controls:** Biological- and technical-replicate fields are blank; wild-type dynamin 2 is the basic positive control; basic negative control not met; no P/LP or B/LB validation controls.
- **Statistics:** Not reported.
- **Thresholds:** Normal is oligomerization dynamics similar to wild type DNM2; abnormal is increased oligomerization compared to wild type DNM2 (formation of higher-order oligomers).

##### GTPase activity — PMID 20529869

- **Assay/material:** Recombinant wild-type or variant dynamin 2, produced by cDNA transfection into Sf9 cells to produce recombinant baculoviruses, is diluted in low-salt buffer with and without PI(4,5)P2; free inorganic Pi release measures GTPase activity.
- **Readout:** Quantitative Pi release.
- **Replication/controls:** Biological replicates not met; technical replicates met (at least three experiments); wild-type dynamin 2 is the basic positive control; basic negative control not met; one P/LP validation control (p.Arg361Ser), no B/LB validation controls.
- **Statistics:** p values reported, but no details of the statistical test are given.
- **Thresholds:** Normal is GTPase activity similar to wild type DNM2; abnormal is increased GTPase activity compared to wild type DNM2.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** Please account for specific phenotype by increasing the weight of PS4 case counts.

#### Specific Phenotype Requirements

A Congenital myopathy panel should be run and negative for other variants (must include BIN1, RYR1, MTM1) **AND** at least two of these features:

1. Presence on Muscle Biopsy of: Oxidative activity and/or radial stranding with spokes on a wheel appearance with centrally nucleated muscle fibers
2. Distal weakness
3. Characteristic muscle imaging (See Figure 9 of Saade et al 2019 PMID: 31060725 for example)
4. Ophthalmoparesis and Ptosis (both of these must be observed to count this as one phenotype criteria)

#### PS4 Point System

| Proband Phenotype | Specificity | Points per Proband |
|-------------------|-------------|-------------------|
| PP4 Met | Specific | 0.5 points |
| One PP4 feature | Suggestive | 0.25 points |

#### PS4 Strength Thresholds

| Strength Level | Core-PDF wording | `DNM2 PS4 rules.pdf` wording | Comparator status |
|----------------|------------------|------------------------------|-------------------|
| PS4_Supporting | `0.25 points` | `0.25 points` | Unstated |
| PS4_Moderate | `0.5 points` | `0.5 points` | Unstated |
| PS4_Strong | `At least 1 point` | `1 points` | Core is inclusive (≥1); attachment is bare |

The source does not reconcile the different Strong wording. It does not state ranges for Moderate or Supporting, and does not assign other totals such as 0.75 points. The attachment's grammatical `1 points` is preserved verbatim.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **All Levels** | **Not Applicable** |

**Comments:** There are no defined hotspots or critical functional domains in DNM2 at this time.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

| Strength | Criteria |
|----------|----------|
| **Supporting** | PM2_Supporting may be applied if the minor allele frequency in population databases of at least 2000 alleles is absent (1 allele allowed) |

**Unresolved source wording:** The same sentence says the frequency is `absent` and that `1 allele` is allowed. The VCEP does not reconcile those statements or supply a numerical frequency threshold.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **All Levels** | **Not Applicable** |

**Comments:** Biallelic case counts should not be used for DNM2 (autosomal dominant inheritance).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** Loss of function is not a mechanism of disease for DNM2-associated centronuclear myopathy. PM4 is to be used with caution.

| Strength | Criteria |
|----------|----------|
| **Strong** | No change - use as originally described |
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants |
| **Supporting** | No change - use as originally described |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | No change - use as originally described |
| **Moderate** | Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before |
| **Supporting** | No change - use as originally described |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | No change - use as originally described |
| **Moderate** | Assumed de novo, but without confirmation of paternity and maternity |
| **Supporting** | No change - use as originally described |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** The segregation chart (adopted from Oza et al 2018 PMID:30311386) should be used to determine the strength level of the total number of affected segregations.

#### PP1 Thresholds for Autosomal Dominant

| Strength | Likelihood | LOD Score | Core-PDF criterion wording | Chart wording |
|----------|------------|-----------|----------------------------|---------------|
| Supporting | 4:1 | 0.6 | At least 2 segregations | Two affected segregations |
| Moderate | 16:1 | 1.2 | Four segregations | Four affected segregations |
| Strong | 32:1 | 1.5 | At least 5 segregations | Five affected segregations |

The core PDF uses inclusive `at least` wording for Supporting and Strong; the chart prints bare counts. The sources do not explain whether the attachment's bare values are exact thresholds or minimums.

#### Segregation Table (Phenocopy Not an Issue)

*The chart labels the columns “Unaffected recessive segregations” and states that these are general recommendations where phenocopy is not an issue.*

| Affected Segregations | 0 Unaffected | 1 Unaffected | 2 Unaffected | 3 Unaffected | 4 Unaffected | 5 Unaffected | 6 Unaffected | 7 Unaffected | 8 Unaffected | 9 Unaffected | 10 Unaffected |
|----------------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|--------------|---------------|
| 0 | 0 | 0.12 | 0.25 | 0.37 | 0.5 | 0.62 | 0.75 | 0.87 | 1 | 1.12 | 1.25 |
| 1 | 0.6 | 0.73 | 0.85 | 0.98 | 1.1 | 1.23 | 1.35 | 1.48 | 1.6 | 1.73 | 1.85 |
| 2 | 1.2 | 1.33 | 1.45 | 1.58 | 1.7 | 1.83 | 1.95 | 2.08 | 2.2 | 2.33 | 2.45 |
| 3 | 1.81 | 1.93 | 2.06 | 2.18 | 2.31 | 2.43 | 2.56 | 2.68 | 2.81 | 2.93 | 3.06 |
| 4 | 2.41 | 2.53 | 2.66 | 2.78 | 2.91 | 3.03 | 3.16 | 3.28 | 3.41 | 3.53 | 3.66 |
| 5 | 3.01 | 3.14 | 3.26 | 3.39 | 3.51 | 3.63 | 3.76 | 3.88 | 4.01 | 4.13 | 4.26 |
| 6 | 3.61 | 3.74 | 3.86 | 3.99 | 4.11 | 4.24 | 4.36 | 4.49 | 4.61 | 4.74 | 4.86 |
| 7 | 4.21 | 4.34 | 4.46 | 4.59 | 4.71 | 4.84 | 4.96 | 5.09 | 5.21 | 5.34 | 5.46 |
| 8 | 4.82 | 4.94 | 5.07 | 5.19 | 5.32 | 5.44 | 5.57 | 5.69 | 5.82 | 5.94 | 6.07 |
| 9 | 5.42 | 5.54 | 5.67 | 5.79 | 5.92 | 6.04 | 6.17 | 6.29 | 6.42 | 6.54 | 6.67 |
| 10 | 6.02 | 6.15 | 6.27 | 6.4 | 6.52 | 6.65 | 6.77 | 6.9 | 7.02 | 7.15 | 7.27 |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | DNM2 is a gene that is constrained for missense variation (gnomAD v4.1 z=4.87). PP2 may be used for missense variants. |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | PP3 is met if the **REVEL score ≥ 0.7** OR if the variant is predicted to impact splicing using **SpliceAI score ≥ 0.5** |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **All Levels** | **Not Applicable** |

**Comments:** PP4 is factored into the strength of PS4. See case counting specifications above.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **All Levels** | **Not Applicable** |

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PubMed: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **≥0.0000015**. All continental populations used in gnomAD should have at least 2000 alleles and >1 observation. |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**

| Strength | Criteria |
|----------|----------|
| **Strong** | The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **≥0.00000015**. All continental populations used in gnomAD should have at least 2000 alleles and >1 observation. |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age. No change from original ACMG. |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** BS3_Supporting is **only** met if **both** of the specified assays have WT readouts.

| Strength | Criteria |
|----------|----------|
| **Supporting** | BS3_Supporting is met if **both** of these assays have WT readouts: |

**Required Assays for BS3_Supporting:**
1. **Oligomerization Assay:** DNM2 assembly/disassembly dynamics similar to wild type DNM2
2. **GTPase Activity Assay:** GTPase activity and stability similar to wild type DNM2

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Lack of segregation in affected members of a family. No change from original ACMG. |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | Not Applicable | Both missense and truncating variants in DNM2 are disease-causing. |
| **BP2** | Applicable | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern. No change from original ACMG. Available at Supporting, Moderate, and Strong levels. |
| **BP3** | Not Applicable | There are no regions in DNM2 where BP3 would apply. |
| **BP4** | Applicable (Supporting) | BP4 is met if the **REVEL score ≤ 0.15** OR if the variant is not predicted to impact splicing using SpliceAI. |
| **BP5** | Applicable | Variant found in a case with an alternate molecular basis for disease. No change from original ACMG. Available at Supporting, Moderate, and Strong levels. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PubMed: 29543229). |
| **BP7** | Applicable (Supporting) | A synonymous variant for which SpliceAI predicts no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. |

**Unresolved source tension:** BP1 says both missense and truncating DNM2 variants are disease-causing, while PVS1 says loss of function is not a DNM2 disease mechanism. The distributed specification does not reconcile these statements; neither should be used to infer that every truncating variant acts through loss of function.

---

## Rules for Combining Criteria

**Source limitation:** The distributed combining table lists `PS3_Very Strong` and `PS4_Very Strong`, but the PS3 and PS4 criterion blocks do not define Very Strong application. It also lists PP4 at Strong, Moderate and Supporting even though PP4 is explicitly Not Applicable; lists PP3 at Strong and Moderate although its criterion block defines only Supporting; and lists `BP7_Strong` although BP7 is defined only at Supporting. Several other upgraded or downgraded labels are represented in their criterion blocks only by `No change - use as originally described`, without a separate operative definition. These conflicts and gaps are not filled here.

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PS2_Very Strong, PS3_Very Strong, PS4_Very Strong) **AND** ≥1 Strong (PS1, PS2, PS3, PS4, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP3_Strong, PP4_Strong) |
| 1 Very Strong **AND** ≥2 Moderate (PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate) |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting (PS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP2, PP3, PP4) |
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
| ≥2 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong, BP7_Strong) |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong, BP7_Strong) **AND** 1 Supporting (BS2_Supporting, BS3_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7) |
| ≥2 Supporting (BS2_Supporting, BS3_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7) |

---

## Appendices

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.0000015 | Stand Alone |
| BS1 | ≥0.00000015 | Strong |
| PM2 | Absent (1 allele allowed in ≥2000 alleles) | Supporting |

### Appendix B: Computational Predictor Thresholds

| Criterion | Tool | Pathogenic Threshold | Benign Threshold |
|-----------|------|---------------------|------------------|
| PP3/BP4 | REVEL | ≥0.7 | ≤0.15 |
| PP3/BP4 | SpliceAI | ≥0.5 | Not predicted to impact splicing |

### Appendix C: Functional-workbook Assay Summary

The distributed workbook proposes Supporting strength for these entries but leaves their `Approved assay (y/n)` result cells blank; see the full workbook transcription under PS3.

| Assay Type | PMID | Abnormal Readout | Normal Readout | Proposed Strength |
|------------|------|------------------|----------------|----------|
| Oligomerization | 20529869 | Increased dynamin stability | Assembly/disassembly similar to WT | Supporting |
| Oligomerization | 24016602 | Increased oligomerization (formation of higher-order oligomers) | Oligomerization dynamics similar to WT | Supporting |
| GTPase Activity | 20529869 | Increased GTPase activity | GTPase activity similar to WT | Supporting |

### Appendix D: Reference PMIDs

1. **Wang L, Barylko B et al.** Dynamin 2 mutants linked to centronuclear myopathies form abnormally stable polymers. *J Biol Chem* (2010) 285(30):22753-7. DOI: 10.1074/jbc.C110.130013. PMID: 20529869.
2. **James NG, Digman MA et al.** A mutation associated with centronuclear myopathy enhances the size and stability of dynamin 2 complexes in cells. *Biochim Biophys Acta* (2014) 1840(1):315-21. DOI: 10.1016/j.bbagen.2013.09.001. PMID: 24016602.
3. **Bitoun M, Durieux AC et al.** Dynamin 2 mutations associated with human diseases impair clathrin-mediated receptor endocytosis. *Hum Mutat* (2009) 30(10):1419-27. DOI: 10.1002/humu.21086. PMID: 19623537.
4. **Oza et al. (2018), PMID 30311386.** This is all the bibliographic detail supplied with the segregation chart; the prior author list, title, journal and pages were not in the distributed package and have been removed.
5. **Saade et al. (2019), PMID 31060725.** This is all the bibliographic detail supplied by the PS4 criterion; the prior title, journal and pages were not in the distributed package and have been removed.
6. **PMID 29543229.** The PP5 and BP6 blocks supply the PMID only; the prior authors, title, journal and pages were not in the distributed package and have been removed.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-08-09 | **Document corrections.** Verified the governing criteria, metadata, DOI, PS4 phenotype rules and point thresholds against `ClinGen_ACMG_Specifications_DNM2_v1.0.pdf`; restored the core DOI, reported its inclusive PS4 Strong and PP1 Supporting/Strong wording without imposing those comparators on the attachments' bare values, documented unmapped PS4 totals, retained the source's `integration` wording with a typo warning, preserved the PM2/BP1/combining-rule source tensions, and restored the three supplied reference DOIs. Verified every PS4 case-count cell and the bare attachment thresholds against `DNM2 PS4 rules.pdf`. Verified and restored all columns 0–10 and all cells of the segregation grid plus its bare-count threshold table against `Segregation Chart.pdf`. Verified every populated workbook cell against `Approved functional assays for DNM2.xlsx`; renamed the unsupported “Approved Assay Instances” claim, documented the blank approval fields, restored assay methods, materials, readouts, replication, controls, statistics, thresholds, variants and proposed strengths, and reported the core/workbook GTPase-threshold discrepancy. Removed unsupplied bibliographic expansions for Oza et al., Saade et al. and PMID 29543229. |
| 1.0.0 | 8/7/2024 | Initial release |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
