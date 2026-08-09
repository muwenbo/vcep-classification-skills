# ClinGen Congenital Myopathies Expert Panel Variant Interpretation Guidelines for MTM1

**Version:** 1.0.0
**Released:** 8/7/2024
**Affiliation:** Congenital Myopathies VCEP
**Source DOI:** 10.5281/zenodo.21434749
**Distributed source files verified:** `ClinGen_ACMG_Specifications_MTM1_v1.0.pdf`; `MTM1 PVS1 guidance.pptx`; `MTM1 approved functional assays.xlsx`

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | MTM1 (HGNC:7448) |
| **HGNC Name** | myotubularin 1 |
| **Transcript** | NM_000252.3 |
| **Disease** | Centronuclear myopathy (MONDO:0018947) |
| **Inheritance** | X-linked inheritance |

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

**VCEP Specifications:** See PVS1 flowchart (gene-specific modification). MTM1 uses the biologically-relevant transcript NM_000252.3.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | See PVS1 flowchart below |
| **Strong (PVS1_Strong)** | See PVS1 flowchart below |
| **Moderate (PVS1_Moderate)** | See PVS1 flowchart below |
| **Supporting** | See PVS1 flowchart below. Its initiation-codon outcome is printed literally as `PVS1_Supp`; the package does not define or expand the abbreviation. |

> **Unresolved flowchart gaps:** Footnote markers `a`, `b`, `c`, and `d` are not defined in the slide or its speaker notes. Every protein-removal branch uses strict `>10%` and `<10%`; exactly 10% has no path. The “critical to protein function” branch is annotated `(no specified regions)`; no critical regions should be inferred.

#### PVS1 Decision Tree for MTM1

**Nonsense or Frameshift Variants:**

- Predicted to undergo NMD (source text `up to c.1593, p.531` with undefined marker `b`) AND exon present in NM_000252.3 → **PVS1**.
- Predicted to undergo NMD AND exon absent from biologically relevant transcript(s) → **N/A**.
- Not predicted to undergo NMD:
  - Truncated/altered region critical to protein function (`no specified regions`) → **PVS1_Strong**.
  - Region role unknown + LoF variants frequent in the general population and/or exon absent → **N/A**.
  - Region role unknown + LoF variants not frequent AND exon present + removes strictly >10% → **PVS1_Strong**.
  - Region role unknown + LoF variants not frequent AND exon present + removes strictly <10% → **PVS1_Moderate**.

The source does not say whether “up to” is inclusive.

**Canonical Splice Site Variants (literal source text `GT--AG 1,2 splice sites` with undefined marker `a`):**

- Exon skipping/cryptic splice use disrupts reading frame AND NMD is predicted: exon present → **PVS1**; exon absent → **N/A**.
- The same frame-disrupting consequence without predicted NMD follows the complete critical-region, frequency, exon-presence, and strict-percentage logic above.
- A frame-preserving consequence (source: `In frame exons: 2, 5-15`) follows that same complete logic: critical region → **PVS1_Strong**; frequent LoF and/or absent exon → **N/A**; non-frequent LoF AND present exon with >10% removed → **PVS1_Strong**; with <10% removed → **PVS1_Moderate**.

**Deletions (single exon to full gene):**

- Full-gene deletion → **PVS1** with undefined marker `d`.
- Frame-disrupting deletion with predicted NMD: exon present → **PVS1**; exon absent → **N/A**.
- Frame-disrupting deletion without predicted NMD, and frame-preserving deletion, follow the complete critical-region, frequency, exon-presence, and strict-percentage logic above: critical region → **PVS1_Strong**; frequent LoF and/or absent exon → **N/A**; non-frequent LoF AND present exon with >10% removed → **PVS1_Strong**; with <10% removed → **PVS1_Moderate**.

**Duplications (>=1 exon, completely contained within gene):**

- Proven in tandem + disrupted frame and NMD predicted → **PVS1**.
- Proven or presumed in tandem + no or unknown impact on reading frame and NMD → **N/A**.
- Presumed in tandem + presumed disrupted frame and NMD predicted → **PVS1_Strong**.
- Proven not in tandem → **N/A**.

**Initiation Codon Variants:**

- Different functional transcript uses alternative start codon → **N/A**.
- No known alternative start codon + >=1 pathogenic variant upstream of closest potential in-frame start codon → **PVS1_Moderate**.
- No known alternative start codon + no pathogenic variants upstream → literal **`PVS1_Supp`**.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | No change - use as originally described |
| **Strong** | De novo (both maternity and paternity confirmed) in a patient with the disease and no family history |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | May only be considered for **variant-specific mouse models**. Currently, no other assays are applicable at this strength. (Disease-specific modification) |
| **Moderate** | Where indicated, some of the assays from PS3_Supporting may be stacked to reach Moderate Strength (Gene-specific modification) |
| **Supporting** | Five assay categories are suggested in the core PDF (see below). The workbook separately marks each populated instance approved at Supporting. Additional assays may be used only under the stated validation conditions. |

#### PS3_Supporting Assay Categories

The core PDF suggests the following five categories for PS3_Supporting:

1. **Phosphatase Activity**
   - **Abnormal Readout:** Reduced phosphatase activity (measured via levels of PtdIns and PtdIns5p or increased levels of precursors)
   - **References:** PMID: 10900271, 14660569, 21135508, 12646134, 23071445

2. **Myotubularin Localization**
   - **Abnormal Readout:** Altered localization (presence in spots/aggregates/extensions, loss of cytoplasmic localization)
   - **References:** PMID: 17651088, 12118066, 20682747

3. **Myotubularin Translocation**
   - **Abnormal Readout:** Loss of MTM1 recruitment to late endosomal compartment following EGF stimulation
   - **Reference:** PMID: 14722070

4. **Intracellular Trafficking**
   - **Abnormal Readout:** Reduced localization/trafficking of receptor proteins (trafficking of endosomal cargo is thought to require phosphoinositide conversion and may be disrupted by defective MTM1 activity)
   - **References:** PMID: 14722070, 26760201

5. **Protein and Lipid Association**
   - **Abnormal Readout:** Decreased association with known binding partner (BIN1, Desmin, hVPS34-PI 3-Kinase, MTMR12, Phosphoinositide, or EEA Membrane association)
   - **References:** PMID: 23917616, 21135508, 17651088, 23818870, 14722070

**Important Notes:**
- **Myotubularin Localization and Myotubularin Translocation should NOT be stacked** because they may not be assessing independent biological function
- The source says other Supporting assays may be stacked “where indicated,” but neither the core PDF nor workbook indicates which other categories or instances may be stacked. Do not infer permitted combinations.
- If not listed above, PS3_Supporting may be used for other functional analyses if:
  - The assay has been validated by a known pathogenic and benign variant AND
  - There is plausible reason that the function the assay is testing relates to the phenotype AND
  - The assay conditions are likely to mimic the physiological environment

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Notes:**
- Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0
- In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence

**VCEP Specifications:** X-linked case counts are adopted from the Rett and Angelman-like disorders VCEP (PMID: 34837432). PS4 can be used to count cases for both affected males (XY) and females (XX). **Females must meet PP4 to be counted towards PS4.**

| Strength | Case Count |
|----------|------------|
| **Strong (PS4)** | 5+ cases |
| **Moderate (PS4_Moderate)** | 3-4 cases |
| **Supporting (PS4_Supporting)** | 2 cases |

The source defines no PS4 band for zero or one qualifying case; no lower band is inferred.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** *Not Applicable*

**Comments:** There are no defined hotspots or critical functional domains in MTM1 at this time.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specification (Supporting only):**

| Strength | Criteria |
|----------|----------|
| **Supporting** | PM2_Supporting may be applied if the minor allele frequency in population databases of at least 2000 alleles is **absent** (1 observation allowed in females only) |

> **Source wording tension:** “absent” and “1 observation allowed in females only” appear together in the criterion. The package does not reconcile them.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** *Not Applicable*

**Comments:** Biallelic case counts should not be used for MTM1 (X-linked inheritance).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** No change - use as originally described.

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

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Strong** | No change - use as originally described |
| **Moderate** | Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before |
| **Supporting** | No change - use as originally described |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Strong** | No change - use as originally described |
| **Moderate** | Assumed de novo, but without confirmation of paternity and maternity |
| **Supporting** | No change - use as originally described |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** X-linked segregation counts adopted from the Rett and Angelman-like disorders VCEP (PMID: 34837432)

| Strength | Segregation Count |
|----------|-------------------|
| **Strong (PP1_Strong)** | At least 5 segregations |
| **Moderate (PP1_Moderate)** | 3-4 segregations |
| **Supporting (PP1)** | 2 segregations |

The source defines no PP1 strength for zero or one segregation; no lower band is inferred.

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** *Not Applicable*

**Comments:** MTM1 is not a gene that is constrained for missense variation. Hence PP2 is not applicable.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | PP3 is met if **REVEL score >= 0.7** OR if the variant is predicted to impact splicing using **SpliceAI score >= 0.5** |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | See criteria below for affected males and carrier females |

#### PP4 Criteria for Affected Males

Must be **negative for BIN1, RYR1, and DNM2 variants** AND have:

- Muscle biopsy with rounded muscle fibers with a single centrally located nucleus surrounded by a halo devoid of contractile elements, but containing mitochondria

#### PP4 Criteria for Carrier Females

Must have a **panel test for neuromuscular disease to rule out other causes** AND:

- Observation of myopathy (may be asymmetric) AND at least 1 other feature:
  - Unilateral skeletal asymmetry
  - Narrow, elongated face
  - High arched palate

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification (Stand Alone):**

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **>= 0.000016**. All continental gnomAD populations used should have at least 2000 alleles and >1 observation. |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**

| Strength | Criteria |
|----------|----------|
| **Strong** | The minor allele frequency using the filtering allele frequency of either exomes or genomes in gnomAD is **>= 0.0000016**. All continental gnomAD populations used should have at least 2000 alleles and >1 observation. |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Strong** | Observed in a healthy adult individual for an X-linked (hemizygous) disorder, with full penetrance expected at an early age |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** *Not Applicable*

**Comments:** The VCEP has decided that lack of demonstrated effect in a functional assay should not count against the pathogenicity of an MTM1 variant because of the numerous possible functions of myotubularin; therefore all specified functional assays will only be used as evidence for pathogenicity.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:** No change - use as originally described.

| Strength | Criteria |
|----------|----------|
| **Strong** | Lack of segregation in affected members of a family |
| **Moderate** | No change - use as originally described |
| **Supporting** | No change - use as originally described |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | *Not Applicable* | Both missense and truncating variants in MTM1 are disease-causing |
| **BP2** | Applicable | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern. No change - use as originally described. |
| **BP3** | *Not Applicable* | There are no regions in MTM1 where BP3 would apply |
| **BP4** | Applicable | BP4 is met if **REVEL score <= 0.15** OR if the variant is **not predicted to impact splicing using SpliceAI** |
| **BP5** | Applicable | Variant found in a case with an alternate molecular basis for disease. No change - use as originally described. |
| **BP6** | *Not Applicable* | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| **BP7** | Applicable | A synonymous variant for which **SpliceAI** predicts no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved |

---

## Rules for Combining Criteria

> **Unresolved source contradiction:** PVS1 is applicable at four strengths and the core directs users to the distributed flowchart, but every published Pathogenic/Likely Pathogenic combination omits PVS1. The only Very Strong criterion named in those combinations is `PS2_Very Strong`. The tables below preserve that omission rather than silently adding PVS1.

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (`PS2_Very Strong`) **AND** >= 1 Strong (PS1, PS2, PS3, PS4, PM4_Strong, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Very Strong (`PS2_Very Strong`) **AND** >= 2 Moderate (PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate) |
| 1 Very Strong (`PS2_Very Strong`) **AND** 1 Moderate **AND** 1 Supporting (PS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
| 1 Very Strong (`PS2_Very Strong`) **AND** >= 2 Supporting |
| >= 2 Strong |
| 1 Strong **AND** >= 3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** >= 2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** >= 4 Supporting |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (`PS2_Very Strong`) **AND** 1 Moderate |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** >= 2 Supporting |
| >= 3 Moderate |
| 2 Moderate **AND** >= 2 Supporting |
| 1 Moderate **AND** >= 4 Supporting |
| 1 Strong **AND** 2 Moderate |

### Benign Classification

| Criteria Combination |
|---------------------|
| >= 2 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) **AND** 1 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7) |
| >= 2 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7) |

---

## Appendices

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >= 0.000016 | Stand Alone |
| BS1 | >= 0.0000016 | Strong |
| PM2 | Absent (1 observation allowed in females only) | Supporting |

**Note:** All thresholds use gnomAD filtering allele frequency from exomes or genomes. All continental gnomAD populations used should have at least 2000 alleles and >1 observation.

### Appendix B: Computational Prediction Thresholds

| Criterion | Tool | Threshold | Interpretation |
|-----------|------|-----------|----------------|
| PP3 | REVEL | >= 0.7 | Supports pathogenicity |
| PP3 | SpliceAI | >= 0.5 | Supports splicing impact |
| BP4 | REVEL | <= 0.15 | Supports benign |
| BP4 | SpliceAI | No impact predicted | Supports benign |

### Appendix C: Distributed Functional-Workbook Instances

`MTM1 approved functional assays.xlsx` contains 19 populated assay instances. Every instance is marked approved `Y`, proposed `Supporting`, with zero P/LP and zero B/LB validation controls. `Proposed strength (modified)` is blank except for the three phosphatase anomalies explicitly preserved below. Biological replication, technical replication, controls and statistical limitations remain operative; approval does not erase them.

#### Protein and lipid association

1. **BIN1 membrane tubulation — PMID 23917616; literal DOI cell `DOI: 10.1038/embor.2013.119`; Royer...Laporte, 2013.** C2C12 cells expressing BIN1 plus WT/variant MTM1 were “evaluted” [sic] for tubule generation/length. Quantitative readout: percentage of cells with tubules and long:short ratio. Biological replicates not met; technical replicates met (two independent experiments, 200 cells each). Positive WT MTM1 and negative BIN1-only controls met. Statistics: unpaired Student's t test or one-way ANOVA plus Bonferroni's Multiple Comparison Test for length-tubule measurement. Normal: WT-like BIN1 tubulation enhancement; abnormal: reduced percentage and/or long:short ratio. Variants: C375S, D278A, R421Q. Notes blank.

2. **BIN1 BAR binding — PMID 23917616; same DOI/authors/year.** Binding of WT/variant “MTM” [sic] to GST-BIN1 BAR by co-immunoprecipitation in C2C12 cells expressing GST-BIN1 BAR and WT/variant MTM1. Qualitative MTM1-band readout. Biological and technical replicates not met. Positive WT MTM1 and negative GST-only pull-down controls met. No statistical analysis. Normal: WT-like MTM1 band intensity; abnormal: decreased intensity. Variants: C375S, D278A, R421Q. Notes blank.

3. **Desmin association — PMID 21135508; literal DOI cell `DOI: 10.1172/JCI44021`; Hnia...Laporte, 2011.** WT/mutant myotubularins co-expressed with Desmin in COS-1 cells and immunoprecipitated. Semi-quantitative Desmin-band association. Biological/technical replicates not met; positive WT MTM1 and negative GST-only controls met. Mann-Whitney U or unpaired Student's test. Normal/abnormal: WT-like versus decreased Desmin band intensity/binding. Variants: H181A, Y206A, S209A, K255A, K269A. Note preserves `resdidues` [sic]: alanine scan of five expected interaction residues, not necessarily seen in XLMTM-affected individuals; Desmin levels also studied in XLMTM myoblasts.

4. **hVPS34 association — PMID 17651088; literal DOI cell `DOI: 10.1111/j.1600-0854.2007.00586.x`; Cao...Stein, 2007.** FLAG-MTM1/hVPS34 co-IP in BHK cells to detect MTM1 in the hVPS15/`hVP34` [sic] complex. Semi-quantitative hVPS34 band. Biological replicates not met; two independent technical experiments met. Positive co-expression and negative single-expression controls met. t-test. Normal/abnormal: WT-like versus decreased hVPS34 band. Variant p.Cys375Ser; note says this phosphatase-dead variant has reduced hVPS34.

5. **MTMR12 association — PMID 23818870; literal DOI cell `DOI: 10.1371/journal.pgen.1003583`; Gupta...Beggs, 2013.** COS7 co-expression and IP of WT/mutant myotubularin with MTMR12-GFP. Semi-quantitative MTMR12 band. Biological/technical replicates not met; WT positive control met; negative control not met. Parametric two-tailed Student t-test. Normal/abnormal: WT-like versus decreased MTMR12 band. Variants C375S, R421Q, P205L, R184G, R69C, V49F. Note: MTMR12 levels also studied in XLMTM myotubes.

6. **EEA membrane association/activity readout — PMID 17651088; same DOI/authors/year.** EEA1 and 2xFYVE levels in BHK cells overexpressing WT/variant MTM1, with reduced staining indicating increased MTM1 activity. Quantitative EEA1 and 2xFYVE/Rab7 fluorescence. Biological replicates not met; three experiments/20 cells each met. WT positive and mock-transfected negative controls met; t-test. Normal is a significant fluorescence decrease; abnormal is no significant decrease. Variant p.Cys375Ser; note says it does not affect PI(3)P levels.

7. **Phosphoinositide binding — PMID 14722070; literal DOI cell `DOI: 10.1074/jbc.M312294200`; Tsujita...Takenawa, 2004.** ELISA binding of GST-myotubularin GRAM-domain fusion proteins to different amounts of `PtdInd` [sic] or PtdIns(3,5)P₂. Quantitative colorimetric readout at 492 nm. Biological replicates not met; average of three technical experiments met. WT-GRAM positive and GST-only negative controls met; no statistics. Normal WT-like binding; abnormal reduced binding. Variants Val49Phe, Arg69Cys, Leu70Phe, Leu87Pro. Note: Figure 1f.

#### Intracellular trafficking

8. **EGFR retention — PMID 14722070; same DOI/authors/year.** COS-7 cells overexpressing WT/variant Myc-MTM1, starved then EGF-treated for 180 minutes; undegraded internalized EGFR by immunofluorescence or western blot. Quantitative number of retaining cells. Biological replicates not met; technical replicates not reported. Positive control is literally `Not met? (only overexpression of myotubularin was tested)`; negative is literally `Met (vector only? or is vector only positive control?)`. No statistics. Normal threshold is unknown because overexpression increases retained EGFR; abnormal-threshold cell is blank. Variants Val49Phe, Gly378Arg. Note: Figure 3e.

9. **Transferrin-receptor trafficking — PMID 26760201; literal DOI cell `DOI: 10.1038/nature16516`; Ketel...Haucke, 2016.** MTM1-depleted HeLa cells were “tranfected” [sic] with WT/variant MTM1; perinuclear recycling-endosomal transferrin receptor localization examined. Quantitative percentage of cells with perinuclear TfR. Biological replicates not met; three experiments with 15-30 images each met. WT positive and GFP-only negative controls met; unpaired two-tailed t-test. Normal WT-like percentage; abnormal significant reduction. Variants P205L, R241L, C375S, Y397C. Notes blank.

#### Myotubularin localization and translocation

10. **Rab5/Rab7 colocalization — PMID 17651088; same DOI/authors/year as above.** Immunofluorescence of WT/variant MTM1-overexpressing A431 cells versus early/late endosomal Rab5/Rab7. Qualitative colocalization. Biological replicates not met; three technical experiments met. Endogenous/overexpressed MTM1 positive control met; negative not met; no statistics. Normal/abnormal: colocalization versus loss. Variant p.Cys375Ser; note says the phosphatase-dead variant localizes normally.

11. **Cytoskeletal/cytosolic fraction western blot — PMID 12118066; literal DOI cell `DOI: 10.1242/jcs.115.15.3105`; LaPorte...Mandel, 2002.** HeLa cells expressing WT/variant MTM1; semi-quantitative MTM1 band in cytoskeletal/cytosolic fractions. Biological/technical replicates not met; WT positive control met; negative not met; no statistics. Variants R241C, D278A, C375S, D377A, D380A, R421Q; notes blank. The workbook unexpectedly assigns this instance the normal threshold `Wild type-like subcellular localization (cytoplasmic network and plasma membrane)` and abnormal threshold `Altered MTM1 subcellular localization`.

12. **Subcellular/membrane-ruffle immunofluorescence — PMID 12118066; same DOI/authors/year.** WT/variant MTM1 in HeLa and/or COS cells, including Rac1-induced membrane ruffles. Qualitative cytoplasmic network, plasma membrane, nuclear/perinuclear spots, cytoplasmic dots and extensions. Biological/technical replicates not met; WT positive met; negative not met; no statistics. Variant D278A; note says this substrate-trapping variant has altered distribution. The workbook unexpectedly assigns this instance fraction-level thresholds: normal `Wild type-like levels of MTM1 in cytoskeletal and cytosolic fractions`; abnormal `Altered levels of MTM1 in cytoskeletal and cytosolic fractions`.

> **Workbook threshold conflict:** The two PMID 12118066 threshold pairs appear cross-assigned relative to their assay descriptions/readouts. They are reported exactly as populated and are not swapped here.

13. **Canine punctate-localization assay — PMID 20682747; literal DOI cell `DOI: 10.1073/pnas.1003677107`; Beggs...Shelton, 2010.** The assay-description cell is blank. Material: COS-1 cells transfected with WT/variant GFP-myotubularin. Quantitative percentage of cells with aggregated punctate dots. Biological replication met (two independent plasmid preparations/construct); technical replication met (several independent transfections, 500 cells/construct). WT positive met; negative not met; no statistics. Normal WT-like percentage; abnormal increased percentage. Variant `Canine MTM1 N155K`; note links it to affected Labrador Retrievers.

14. **EGF-dependent translocation — PMID 14722070; same DOI/authors/year.** COS-7 cells expressing WT/variant GFP-MTM1, starved and EGF-treated 40 minutes; localization by immunofluorescence. Quantitative count of cells showing late-endosomal translocation. Biological replicates not met; >50 cells from three experiments met. WT positive and GFP-only/ΔGRAM negative controls met; no statistics. Normal WT-like translocation; abnormal `Reduced transloation` [sic]. Variant Val49Phe. Note: Figure 2e.

#### Phosphatase activity

15. **pNPP/PI(3)P phosphatase — PMID 10900271; literal DOI cell `DOI: 10.1073/pnas.160255697`; Taylor...Dixon, 2000.** Recombinant WT/variant myotubularin; qualitative activity relative to WT. Biological/technical replicates not met; WT positive met; negative not met; no statistics. Normal WT-like activity; abnormal reduced activity. Variants P205L, R241L, S376N, G378R, Y397C. Notes blank.

16. **L6-myotube lipid assay — PMID 14660569; literal DOI cell `DOI: https://doi.org/10.1074/jbc.M311071200`; Tronchère...Payrastre, 2004.** NaCl-treated L6 myotubes expressing WT/variant MTM1; lipids extracted for mass assay or TLC/HPLC. Quantitative PtdIns(5)P or PtdIns(3,5)P. Biological replicates not met; two technical experiments met. WT positive met; GFP negative met although results not shown; no statistics. Normal WT-like PtdIns(5)P production; abnormal reduced PtdIns(5)P and increased PtdIns(3,5)P. Variant D278A. Notes blank.

17. **COS-1 PtdIns(3,5)P2 assay — PMID 21135508; same DOI/authors/year as Desmin.** WT/mutant myotubularins with Desmin in COS-1 cells, immunostained for PtdIns(3,5)P2. Semi-quantitative lipid level. Biological replicates not met; two technical experiments met. Positive `wild type MTM1FL` and negative MTM1-knockout controls met; Mann-Whitney U or unpaired Student’s test. Normal `MTMFL (wild type)-like` [sic] level; abnormal increased level. `Variants evaluated` is blank; the workbook instead places `H181A, Y206A, S209A, K255A, K269A, C375S, R184G, P205L, R241C, R421Q` in `Proposed strength (modified)`.

18. **Purified-protein phosphate-release assay — PMID 12646134; literal DOI cell `DOI: 10.1016/s0960-9822(03)00132-5`; Schaletzky...Barr, 2003.** Inorganic phosphate released from PtdIns(3)P with/without PtdIns(5)P by purified WT/variant myotubularin. Quantitative Pᵢ. Biological/technical replicates not met; WT positive met; negative not met; no statistics. Normal WT-like phosphate; abnormal decreased phosphate. `Variants evaluated` blank; `Proposed strength (modified)` contains C375S, R69C, R184G, K114A.

19. **Yeast cellular-lipid assay — PMID 23071445; literal DOI cell `DOI: 10.1371/journal.pgen.1002965`; Amoasii...Friant, 2012.** PtdIns3P/PtdIns5P in ymr1Δ yeast expressing WT/variant MTM1. Quantitative lipid level. Biological replicates not met; two technical experiments met. WT positive and empty-plasmid negative controls met; no statistics. Normal WT-like PtdIns3P/PtdIns5P; abnormal increased PtdIns3P or decreased PtdIns5P. `Variants evaluated` blank; `Proposed strength (modified)` contains C375S, V49F, R69C, N180K, R421Q.

> **Workbook row anomaly:** For instances 17-19, variant lists are populated under `Proposed strength (modified)` and the `Variants evaluated` cells are blank. The values are not silently moved. All other instances have blank modified-strength cells.

**Stacking restriction:** Myotubularin Localization and Myotubularin Translocation should NOT be stacked. No other permitted stacking combinations are specified.

### Appendix D: Reference PMIDs

| PMID | Citation |
|------|----------|
| 23917616 | Royer B, Hnia K et al. The myotubularin-amphiphysin 2 complex in membrane tubulation and centronuclear myopathies. EMBO Rep (2013) 14(10):907-15. DOI: 10.1038/embor.2013.119 |
| 21135508 | Hnia K, Tronchère H et al. Myotubularin controls desmin intermediate filament architecture and mitochondrial dynamics in human and mouse skeletal muscle. J Clin Invest (2011) 121(1):70-85. DOI: 10.1172/JCI44021 |
| 17651088 | Cao C, Laporte J et al. Myotubularin lipid phosphatase binds the hVPS15/hVPS34 lipid kinase complex on endosomes. Traffic (2007) 8(8):1052-67. DOI: 10.1111/j.1600-0854.2007.00586.x |
| 14722070 | Tsujita K, Itoh T et al. Myotubularin regulates the function of the late endosome through the gram domain-phosphatidylinositol 3,5-bisphosphate interaction. J Biol Chem (2004) 279(14):13817-24. DOI: 10.1074/jbc.M312294200 |
| 26760201 | Ketel K, Krauss M et al. A phosphoinositide conversion mechanism for exit from endosomes. Nature (2016) 529(7586):408-12. DOI: 10.1038/nature16516 |
| 23818870 | Gupta VA, Hnia K et al. Loss of catalytically inactive lipid phosphatase myotubularin-related protein 12 impairs myotubularin stability and promotes centronuclear myopathy in zebrafish. PLoS Genet (2013) 9(6):e1003583. DOI: 10.1371/journal.pgen.1003583 |
| 12118066 | Laporte J, Blondeau F et al. The PtdIns3P phosphatase myotubularin is a cytoplasmic protein that also localizes to Rac1-inducible plasma membrane ruffles. J Cell Sci (2002) 115(Pt 15):3105-17. DOI: 10.1242/jcs.115.15.3105 |
| 20682747 | Beggs AH, Böhm J et al. MTM1 mutation associated with X-linked myotubular myopathy in Labrador Retrievers. Proc Natl Acad Sci USA (2010) 107(33):14697-702. DOI: 10.1073/pnas.1003677107 |
| 10900271 | Taylor GS, Maehama T et al. Myotubularin, a protein tyrosine phosphatase mutated in myotubular myopathy, dephosphorylates the lipid second messenger, phosphatidylinositol 3-phosphate. Proc Natl Acad Sci USA (2000) 97(16):8910-5. DOI: 10.1073/pnas.160255697 |
| 14660569 | Tronchère H, Laporte J et al. Production of phosphatidylinositol 5-phosphate by the phosphoinositide 3-phosphatase myotubularin in mammalian cells. J Biol Chem (2004) 279(8):7304-12. DOI: 10.1074/jbc.M311071200 |
| 12646134 | Schaletzky J, Dove SK et al. Phosphatidylinositol-5-phosphate activation and conserved substrate specificity of the myotubularin phosphatidylinositol 3-phosphatases. Curr Biol (2003) 13(6):504-9. DOI: 10.1016/s0960-9822(03)00132-5 |
| 23071445 | Amoasii L, Bertazzi DL et al. Phosphatase-dead myotubularin ameliorates X-linked centronuclear myopathy phenotypes in mice. PLoS Genet (2012) 8(10):e1002965. DOI: 10.1371/journal.pgen.1002965 |
| 22068590 | Pierson CR, Dulin-Smith AN et al. Modeling the human MTM1 p.R69C mutation in murine Mtm1 results in exon 4 skipping and a less severe myotubular myopathy phenotype. Hum Mol Genet (2012) 21(4):811-25. DOI: 10.1093/hmg/ddr512 |
| 34837432 | McKnight D, Bean L et al. Recommendations by the ClinGen Rett/Angelman-like expert panel for gene-specific variant interpretation methods. Hum Mutat (2022) 43(8):1097-1113. DOI: 10.1002/humu.24302 |
| 29543229 | Bare PMID supplied by the core PDF for the PP5/BP6 recommendation; no bibliographic expansion is supplied. |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 8/7/2024 | Initial release |
| 1.0.0 | 2026-08-09 | **Document corrections.** Verified all criteria, exact PS4/PP1/frequency comparators, combination rules, DOI and 14 full references against `ClinGen_ACMG_Specifications_MTM1_v1.0.pdf`; removed unsupported frequency percentage conversions, the fabricated mouse-model assay row, the source-contradicting PMID 29543229 expansion, and the invented PVS1 inclusion in classification combinations, while documenting the core's unresolved omission of PVS1, unmapped zero/one PS4/PP1 counts, and the PM2 “absent”/one-female-observation tension. Verified every shape, connector and speaker note in `MTM1 PVS1 guidance.pptx`; restored exon-presence, frequency/exon, splice, deletion, duplication and initiation-codon paths, corrected the two reversed initiation outcomes, and documented undefined `a`-`d` markers, the exact-10% gap, `no specified regions`, literal `GT--AG`/`PVS1_Supp`, and ambiguous `up to` boundary. Verified every populated cell across all ten sheets and 19 assay instances in `MTM1 approved functional assays.xlsx`; restored the complete assay methods, materials, readouts, replication, controls, zero validation counts, statistics, thresholds, strengths, variants and notes, preserving questioned/blank fields, cross-assigned localization thresholds, misplaced phosphatase variant lists and source typos. No change to the underlying ClinGen specification version. |

---

*This document was compiled from ClinGen VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to the ClinGen website.*
