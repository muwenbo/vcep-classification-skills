# Comprehensive Variant Interpretation Guidelines for CEP290

## ClinGen Leber Congenital Amaurosis/early onset Retinal Dystrophy VCEP Specifications for CEP290 (Version 1.0)

**Affiliation:** Leber Congenital Amaurosis/early onset Retinal Dystrophy VCEP
**Version:** 1.0
**Release Date:** July 2, 2026
**DOI:** 10.5281/zenodo.21434860
**Based on:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015 (ACMG/AMP Variant Interpretation Guidelines)

---

## Table of Contents

1. [Gene and Disease Information](#1-gene-and-disease-information)
2. [Pathogenic Criteria](#2-pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PM2 - Absent from Controls](#pm2---absent-from-controls)
   - [PM3 - In Trans with Pathogenic Variant](#pm3---in-trans-with-pathogenic-variant)
   - [PM4 - Protein Length Changes](#pm4---protein-length-changes)
   - [PM5 - Novel Missense at Same Residue](#pm5---novel-missense-at-same-residue)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
   - [PP4 - Phenotype Specificity](#pp4---phenotype-specificity)
3. [Benign Criteria](#3-benign-criteria)
   - [BA1 - Stand-Alone Benign](#ba1---stand-alone-benign)
   - [BS1 - Allele Frequency Greater Than Expected](#bs1---allele-frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (Benign)](#bs3---functional-studies-benign)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP2 - Observed in cis with Pathogenic Variant](#bp2---observed-in-cis-with-pathogenic-variant)
   - [BP4 - Computational Evidence (Benign)](#bp4---computational-evidence-benign)
   - [BP7 - Synonymous/Intronic Variants](#bp7---synonymousintronic-variants)
4. [Not Applicable Criteria](#4-not-applicable-criteria)
5. [Rules for Combining Criteria](#5-rules-for-combining-criteria)
6. [Appendices](#6-appendices)

---

## 1. Gene and Disease Information

| Parameter | Value |
|-----------|-------|
| **Gene** | CEP290 (HGNC:29021) |
| **HGNC Name** | centrosomal protein 290 |
| **Reference Transcript** | ENST00000552810.6 (equivalent RefSeq transcript used in supplementary documents: NM_025114.4) |
| **Disease** | CEP290-related ciliopathy |
| **MONDO ID** | MONDO:0100451 |
| **Mode of Inheritance** | Autosomal recessive inheritance |
| **Specification Type** | Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015 (point-based) |

### Key Gene Characteristics

- The CEP290 protein is 2479 amino acids in length and is encoded by 54 exons (coding sequence begins in exon 2).
- All coding exons are considered critical to protein function (Drivas et al., 2015; PMID: 26062849).
- Requirement for a truncation to remove more than 10% of total protein length does **not** apply to CEP290.
- No potential "rescue isoforms" are known.

### Phenotype Requirement for Proband-Based Codes

**All probands being considered for any pathogenic phenotype code (i.e., PP1, PP4, PM3, PM6, PS2) at any strength must have the following phenotype characteristics:**

- Absent or severely decreased rod electroretinogram response
  **OR**
- A diagnosis of Leber congenital amaurosis/early-onset retinal dystrophy (eoRD)/RP/cone-rod dystrophy (CRD)/Joubert syndrome/Meckel syndrome/Senior-Loken syndrome/Bardet-Biedl syndrome.

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specification:** See the CEP290-specific PVS1 Decision Tree, which has been modified from Walker et al., 2023 (PMID: 37352859). Use as defined by the ClinGen SVI working group (Abou Tayoun et al., 2018; PMID: 30192042) and as updated by the ClinGen SVI Splicing Subgroup (Walker et al., 2023).

#### Strength Levels

| Strength | Default Points | Application |
|----------|----------------|-------------|
| **PVS1** (Very Strong) | 8 | Nonsense or frameshift from p.2 through p.Leu2448; single to multi-exon deletions (with or without predicted NMD); full gene deletion; duplications of exons proven in tandem; variants in the initiation codon; predicted splice defects at ±1,2 in exons 2-54; PVS1(RNA) where RNA splicing data show alternative transcript production at **complete** levels relative to the normal allele |
| **PVS1_Strong** | 4 | Nonsense or frameshift from p.Ser2449 through p.Val2454; duplications of exons **presumed** in tandem; PVS1(RNA)_Strong where RNA splicing data show alternative transcript production at **near complete** levels relative to the normal allele |
| **PVS1_Moderate** | 2 | Nonsense or frameshift mutations beyond p.Val2454 |
| **PVS1_Supporting** | Not specified by VCEP | Not specified by VCEP as a distinct rule; PVS1_Supporting appears only as a possible reduced strength level within the Walker et al. splicing framework |

**Modification Type:** Gene-specific

#### Nonsense / Frameshift Variants (Decision Tree)

| Condition | PVS1 Strength |
|-----------|---------------|
| Nonsense or frameshift variants terminating at codons 2 through 2386 (expected to undergo NMD) | **PVS1** |
| Nonsense or frameshift variants from p.Asp2387 through p.Leu2448 (no NMD; truncation or frameshift in critical functional region) | **PVS1** |
| Nonsense or frameshift variants from p.Ser2449 through p.Val2454 (no NMD; truncation or frameshift in likely critical functional region) | **PVS1_Strong** |
| Nonsense or frameshift variants > p.Val2454 | **PVS1_Moderate** |

*Nonsense or frameshift variants from codon 2387 through 2479 are expected to produce transcripts that will NOT undergo NMD.*

#### Deletions (Single Exon to Full Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Full gene deletion | **PVS1** |
| Disrupts reading frame + predicted NMD + exon(s) present in biologically-relevant transcript NM_025114.4 | **PVS1** |
| Disrupts reading frame + predicted NMD + exon(s) absent from biologically-relevant transcript NM_025114.4 | N/A |
| Disrupts reading frame + NOT predicted to undergo NMD (exons 1-54 harbor pathogenic variants and all are considered critical to protein function) | **PVS1** |
| Preserves reading frame (exons 1-54 harbor pathogenic variants and all are considered critical to protein function) | **PVS1** |

#### Duplications (≥1 Exon, Completely Contained Within Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Proven in tandem + reading frame disrupted + NMD predicted to occur | **PVS1** |
| Proven in tandem or presumed in tandem + no or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem + reading frame presumed disrupted + NMD predicted to occur | **PVS1_Strong** |
| Proven not in tandem | N/A |

#### Initiation Codon Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| No known alternative start codon in other transcripts + ≥1 pathogenic variant(s) upstream of the closest potential in-frame start codon (closest in-frame Met is p.Met11) | **PVS1** |
| Different functional transcript uses alternative start codon | N/A |

**VCEP note:** The second in-frame methionine is located at residue p.Met11. There is no known study indicating that this methionine in CEP290 can be used as a start codon. Variants affecting Met1 can lead to a complete absence of the protein product. Additionally, there are multiple variants between (and including) p.Met1 and p.Met11 that have been reported as pathogenic in HGMD and ClinVar, evidence that this region of the protein is functionally important.

#### Splice Variants at the Donor/Acceptor ±1,2 Dinucleotide Positions

Predicted splice defects at ±1,2 in exons 2-54 meet **PVS1** at the default level. All exons are predicted to be essential because they meet one or more of the following criteria:

| Exons predicted to be skipped | Rationale | PVS1 Strength |
|-------------------------------|-----------|---------------|
| Out-of-frame exons 4, 5, 13, 14, 15, 16, 17, 18, 19, 20, 23, 24, 27, 28, 29, 30, 37, 38, 42, 44, 49, 50, 51, 52, 53 | Skipping disrupts the reading frame | **PVS1** (default) |
| In-frame exons 2, 3, 6, 7, 8, 9, 10, 11, 12, 43, 45, 46, 47, 48, 54 | Encode key domains required for CEP290 self-association | **PVS1** (default) |
| In-frame exons 22, 25, 26 | Encode key domains required for CEP290 interaction with the ciliopathy-related protein IQCB1 | **PVS1** (default) |
| In-frame exons 35, 36, 39, 41 | Each harbors previously reported pathogenic or likely pathogenic missense variants | **PVS1** (default) |
| In-frame exons 21, 31, 32, 33, 34, 40 | Each has multiple canonical splice site variants previously reported as disease-causing | **PVS1** (default) |

See [Appendix A: CEP290 PVS1 Exon Rule Table](#appendix-a-cep290-pvs1-exon-rule-table) for per-exon coordinates, domains, and NMD status.

#### RNA / Splicing Assay Data

Observed results of a splicing assay are classified in the same manner as predicted results. Use **PVS1(RNA)** if there is evidence of impact on splicing, or **BP7_Strong(RNA)** if evidence suggests no impact.

| Proportion of alternative transcript(s) (inferred to be) produced by the variant allele | Action |
|----------------------------------------------------------------------------------------|--------|
| Complete | Keep strength level (**PVS1(RNA)**, 8 points) |
| Near complete | Reduce strength by 1 level (**PVS1(RNA)_Strong**, 4 points) |
| Incomplete | Do not apply codes |

*If the background rate is considered to be at low-moderate levels suggestive of being tolerated, consider reducing PVS1(RNA) codes by an additional level.*

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

- For assessing same amino acid changes, **SpliceAI must be used** to ensure the comparison variant is not causing a splicing defect (score ≤0.1 indicates no likely defect).
- For assessing splicing impact, refer to the CEP290-specific PVS1 Decision Tree. Part (b) defines PS1 code weights for variants with the same predicted splicing event as a known pathogenic/likely pathogenic variant (Table 2 from Walker 2023).
- For sites to be considered "comparable", they should have similar SpliceAI-predicted effects (gain vs loss, site of effect).
- To avoid circularity, the code will be applied for only one of the variants.

| Strength | Default Points | Application |
|----------|----------------|-------------|
| **PS1_Strong** | 4 | Same amino acid change as a previously established **Pathogenic** variant regardless of nucleotide change. Must have one comparison variant that reaches a Pathogenic classification using this rule specification. Also: same predicted splicing impact as a previously classified Pathogenic variant — used in conjunction with PP3 for variants outside the donor/acceptor ±1,2 dinucleotide positions with a SpliceAI score ≥0.2 and a comparable nucleotide variant at the same position designated Pathogenic; or used in conjunction with PVS1 for variants at the donor/acceptor ±1,2 dinucleotide positions with a comparable variant within the same donor/acceptor ±1,2 dinucleotide designated Pathogenic |
| **PS1_Moderate** | 2 | Same amino acid change as a previously established **Likely Pathogenic** variant regardless of nucleotide change (comparison variant must reach Likely Pathogenic using this rule specification). Also: same predicted splicing impact as a previously classified Likely Pathogenic variant — used in conjunction with PP3 for variants outside the ±1,2 dinucleotide positions with SpliceAI ≥0.2 and a comparable nucleotide variant at the same position designated Likely Pathogenic; used in conjunction with PP3 for variants outside the ±1,2 dinucleotide positions but within the same donor/acceptor motif (including the ±1,2 positions) designated Pathogenic; used in conjunction with PVS1_(reduced strength) for variants at the ±1,2 dinucleotide positions with a comparable variant within the same motif (but outside the ±1,2 dinucleotide) designated Pathogenic |
| **PS1_Supporting** | 1 | Used in conjunction with PP3 for variants outside the donor/acceptor ±1,2 dinucleotide positions with a SpliceAI score ≥0.2 and a comparable nucleotide variant within the same motif designated Likely Pathogenic. Also used in conjunction with PVS1 or PVS1_(reduced strength) for variants at the donor/acceptor ±1,2 dinucleotide positions with a comparable Likely Pathogenic or Pathogenic variant either within the same splice donor/acceptor motif outside the ±1,2 dinucleotide, or at the ±1,2 dinucleotide |

**Modification Type:** Gene-specific (Strong); Gene-specific, Strength (Moderate, Supporting)

#### PS1 Code Weights for Splicing (Table 2 from Walker et al., 2023)

| Variant under assessment (VUA) | Baseline computational/predictive code applicable to VUA | Position of comparison variant relative to VUA | PS1 code with **P** comparison variant | PS1 code with **LP** comparison variant |
|--------------------------------|----------------------------------------------------------|-----------------------------------------------|----------------------------------------|-----------------------------------------|
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | Same nucleotide | PS1 | PS1_Moderate |
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | Within same splice donor/acceptor motif (including at ±1,2 positions) | PS1_Moderate | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | Within same splice donor/acceptor ±1,2 dinucleotide | PS1_Supporting | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | Within same splice donor/acceptor region, but outside ±1,2 dinucleotide | PS1_Supporting | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | Within same splice donor/acceptor ±1,2 dinucleotide | PS1 | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | Within same splice donor/acceptor motif, but outside ±1,2 dinucleotide | PS1_Moderate | PS1_Supporting |

**Prerequisite for all:** The predicted event of the VUA must precisely match the predicted event of the comparison (likely) pathogenic variant (e.g., both predicted to lead to exon skipping, or both to enhanced use of a cryptic splice motif), AND the strength of the prediction for the VUA must be of similar or higher strength than the strength of the prediction for the comparison (likely) pathogenic variant.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

#### VCEP Specifications

- Use the point table from the **SVI Recommendation for De Novo Criteria (PS2 & PM6) - Version 1.1**.
- **Individuals must have 2 variants to consider scoring one for de novo.**
- Each proband with a de novo variant is awarded a point value based upon phenotypic consistency and confirmed or assumed parental relationships (Table 1). The combined point value of all de novo occurrences is then compared to Table 2 to determine the applicable evidence strength level.
- Probands must meet the [phenotype requirement for proband-based codes](#phenotype-requirement-for-proband-based-codes).

##### Mapping Phenotypic Consistency to PP4

| PP4 status of the proband | "Phenotypic consistency" category to use |
|---------------------------|------------------------------------------|
| Does not meet PP4 | Option 3: "Phenotype consistent with gene but not highly specific and high genetic heterogeneity" |
| Meets PP4 at the Supporting level | Option 2: "Phenotype consistent with gene but not highly specific" |
| Meets PP4 at the Moderate level | Option 1: "Phenotype highly consistent for gene" |

##### Table 1 - Points Awarded per De Novo Occurrence

| Phenotypic Consistency | Confirmed de novo | Assumed de novo |
|------------------------|-------------------|-----------------|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity* | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

*Maximum allowable value of 1 may contribute to overall score.

##### Table 2 - Evidence Strength Level (as specified by this VCEP)

| Total Points | Evidence Strength | Default Points |
|--------------|-------------------|----------------|
| 0.50 - 0.75 | **PS2_Supporting** | 1 |
| 1.00 - 1.75 | **PS2_Moderate** | 2 |
| 2.00 - 3.75 | **PS2_Strong** | 4 |
| ≥4 | **PS2_VeryStrong** | 8 |

**Modification Type:** Gene-specific

**Note:** PM6 is Not Applicable for CEP290 — use the PS2 code in lieu of PM6 for de novo variants (assumed de novo occurrences are scored in the "Assumed de novo" column of Table 1).

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

#### VCEP Specifications

| Strength | Default Points | Application |
|----------|----------------|-------------|
| **PS3_Supporting** | 1 | Well-established in vitro or in vivo functional studies supportive of a damaging effect. **Not applicable for splicing effects** (replaced by PVS1_Strength (RNA)). See the approved assay table below. |
| **PS3_Moderate** | Not specified by VCEP | Not specified by VCEP |
| **PS3_Strong** | Not specified by VCEP | Not specified by VCEP |

**Modification Type:** Gene-specific, Strength

#### Approved Functional Assays

Studies reviewed by the VCEP (PS3 Approved Functional Assays table):

| Assay class | Reference | PMID | Approved | Proposed strength |
|-------------|-----------|------|----------|-------------------|
| Decreased CEP290 expression (anti-CEP290 western blot of patient fibroblasts) | Shimada et al., 2017 | 28700940 | Yes | **PS3_Supporting** |
| Decreased CEP290 expression (anti-CEP290 western blot of patient fibroblasts) | Drivas et al., 2015 | 26062849 | Yes | **PS3_Supporting** |
| CEP290 splicing defects (minigene assay) | Garanto et al., 2015 | 25761237 | Yes | Informs PVS1 (not PS3) |
| Defects in ciliary structure (RPE1 cells; iPSC-derived retinal organoids) | Corral-Serrano et al., 2023 | 37371046 | Yes | Informs strength of PVS1 (not PS3) |
| CEP290 localization to the ciliary base; impaired Sonic hedgehog pathway signaling | Kilander et al., 2018 | 30478281 | No | Not applicable |
| Loss of CEP290 interaction with NPHP2 (co-immunoprecipitation) | Baye et al., 2011 | 21257638 | No | Not applicable |
| Absent or incomplete nonsense-mediated decay of CEP290 (qPCR) | Esteve-Garcia et al., 2024 | 39766851 | No | Not applicable (best used to inform the level of PVS1) |

##### Approved Assay Thresholds

| Assay (PMID) | Threshold for normal readout | Threshold for abnormal readout |
|--------------|------------------------------|--------------------------------|
| Decreased CEP290 expression (28700940) | Expression level (quantified western blot signal) equivalent to the "Normal" unaffected control | Expression level between 0% and 50% of the "Normal" unaffected control |
| Decreased CEP290 expression (26062849) | Expression level equivalent to the unaffected "Controls" | Expression level between 0% and 55% of the unaffected "Controls" |
| Defects in ciliary structure — RPE1 cells (37371046) | Percentage ciliation and ciliary length (quantified anti-ARL13b signal) equivalent to the "WT" unedited control | Percentage ciliation and ciliary length reduced by approximately 30-50% each relative to the "WT" unedited control |
| Defects in ciliary structure — retinal organoids (37371046) | Percentage ciliation and ciliary length equivalent to the "WT" unedited control | Percentage ciliation and ciliary length reduced by approximately 30-40% each relative to the "WT" unedited control, and more similar to the "LCA10" affected-patient control |
| CEP290 splicing defects (25761237) | Single band corresponding to the normally spliced transcript | Presence of a second band in addition to the normal band, corresponding to the aberrantly spliced transcript |

**VCEP notes:**
- For the expression assays, results are attributable to a single variant only when the proband is homozygous (e.g., c.2991+1655A>G); results from compound heterozygous probands or from apparent null variants are less applicable to PS3_Supporting and more applicable to informing the strength of PVS1.
- The VCEP would consider future in vitro minigene/midigene assays or RNA-seq assays for PVS1(RNA) instead of PS3, per Walker et al. (PMID: 37352859).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

#### VCEP Specification

| Strength | Default Points | Threshold |
|----------|----------------|-----------|
| **PM2_Supporting** | 1 | gnomAD **total allele frequency ≤ 6.0 x 10⁻⁴** |

**Modification Type:** Disease-specific, Strength

##### Derivation and Caveats

- The cutoff value of 6.0 x 10⁻⁴ is set just above the FAF of the most common pathogenic CEP290 variant (p.Ile556AsnfsTer20) and below the Whiffin-Ware calculation for the maximum credible population allele frequency for the disease.
- This rule should **not** be applied if the variant would otherwise meet criteria for a benign classification, as rarity of the variant should not outweigh other types of benign evidence.

---

### PM3 - In Trans with Pathogenic Variant

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

#### VCEP Specifications

- Use the SVI recommendations for the PM3 criterion (svi_proposal_for_pm3_criterion_-_version_1.pdf).
- Each proband is awarded a point value based upon phasing of the two variants in question (confirmed in trans versus unknown) and classification of the variant on the other allele (Table 1). The combined point value of all proband occurrences is summed and compared to Table 2 to determine the applicable evidence strength level.
- Both variants must be classified using these rule specifications, but to avoid circularity the code is only applied to one of the variants.
- Probands must meet the [phenotype requirement for proband-based codes](#phenotype-requirement-for-proband-based-codes).

##### Table 1 - Points Awarded per In Trans Occurrence

| Classification/Zygosity of other variant* | Confirmed in trans | Phase unknown |
|-------------------------------------------|--------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (max point 1.0) | 0.5 | N/A |
| Uncertain significance variant on other allele (max point 0.5) | 0.25 | 0.0 |

*All variants should be sufficiently rare (meet PM2 specification).

##### Table 2 - Evidence Strength Level (as specified by this VCEP)

| Total Points from Table 1 | Evidence Strength | Default Points |
|---------------------------|-------------------|----------------|
| 0.5 - 0.75 | **PM3_Supporting** | 1 |
| 1 - 1.75 | **PM3 (Moderate)** | 2 |
| 2 - 3.75 | **PM3_Strong** | 4 |
| ≥4 | **PM3_VeryStrong** | 8 |

**Modification Type:** Disease-specific

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### VCEP Specifications

| Strength | Default Points | Application |
|----------|----------------|-------------|
| **PM4_Moderate** | 2 | Protein length change of **≥2 amino acids** that leads to loss of at least one conserved residue (PhyloP >2.0) or insertion of new amino acids adjacent to at least one conserved residue (PhyloP >2.0) |
| **PM4_Supporting** | 1 | Protein length change of **1 amino acid** that leads to loss of at least one conserved residue (PhyloP >2.0) or insertion of a new amino acid adjacent to at least one conserved residue (PhyloP >2.0) |

**Modification Type:** Gene-specific (Moderate); Gene-specific, Strength (Supporting)

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

#### VCEP Specifications

- Apply only for missense variants for which the amino acid change itself is the expected mechanism of disease. To avoid circularity, the code will be applied for only one of the variants.
- **SpliceAI scores should be <0.20** for both the variant under curation and the comparison variant.
- Variants with a SpliceAI score >0.2 should instead be evaluated as variants impacting splicing, and would meet PP3 and could also meet PS1 (at the appropriate level). See CEP290-specific PVS1 Decision Tree part (b) (Table 2 from Walker 2023).

| Strength | Default Points | Application |
|----------|----------------|-------------|
| **PM5_Moderate** | 2 | Must have one comparison variant that reaches a **Pathogenic** classification using this rule specification |
| **PM5_Supporting** | 1 | Must have one comparison variant that reaches a **Likely Pathogenic** classification using this rule specification |

**Modification Type:** None (Moderate); Strength (Supporting)

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

#### VCEP Specifications

- For moderate and strong codes, segregations can be added across multiple families, with each having a proband + at least one affected relative.
- Evidence that this variant and another CEP290 variant are in trans is required at every strength level.
- Probands must meet the [phenotype requirement for proband-based codes](#phenotype-requirement-for-proband-based-codes).

| Strength | Default Points | Application |
|----------|----------------|-------------|
| **PP1_Strong** | 4 | Requires segregation in one proband plus **≥3** similarly affected relatives |
| **PP1_Moderate** | 2 | Requires segregation in one proband plus **2** similarly affected relatives |
| **PP1_Supporting** | 1 | Requires segregation in one proband plus **1** similarly affected relative |

**Modification Type:** Disease-specific, Strength

**Note:** No LOD-score-based thresholds are specified by this VCEP.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

#### VCEP Specifications

- PP3 should **not** be used to evaluate variants at canonical splice sites. For canonical splice sites, apply PVS1(splicing).
- For non-canonical sites, if the SpliceAI score is ≥0.2, apply PP3 (splicing) instead.
- Score ranges are based on calculations in Pejaver et al., 2022 (PMID: 36413997).

| Strength | Default Points | Application |
|----------|----------------|-------------|
| **PP3_Moderate** | 2 | Missense variant: CADD score **≥ 28.1**. Splice variants use PP3 only at the Supporting level. |
| **PP3_Supporting** | 1 | Missense variant: CADD score **25.3 - 28.09**. Untranslated region variant: CADD score **≥ 20.0**. Predicted splicing variant: SpliceAI (max distance set to 500 bp) highest delta score **≥ 0.2**. |

**Modification Type:** Gene-specific, Strength (Moderate); Gene-specific (Supporting)

#### SpliceAI Flowchart (based on Walker 2023, Figure 4)

For variants located **outside** of the donor/acceptor ±1,2 dinucleotide positions:

| SpliceAI Δ score | Code |
|------------------|------|
| ≤ 0.1 | **BP4** (then assess BP7 based on variant location) |
| > 0.1 and < 0.2 | **PP3 N/A (splicing)** — consider missense/indel predictions for exonic variants |
| ≥ 0.2 | **PP3** |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

#### VCEP Specifications

A point system determines whether there is enough information about a proband's phenotype to qualify for use of this code. Review eligible phenotype characteristics and add up points for each finding.

- This code can be used for a **single proband**.
- A proband must have **two CEP290 variants** to consider applying PP4 (phase is not considered here).
- **Caveat:** PP4 should not be applied if the variant meets either BA1 or BS1.
- Do not include a proband with a suspected diagnosis of more than one retinal dystrophy.

##### Point Thresholds

| Total Phenotype Points | PP4 Strength | Default Points |
|------------------------|--------------|----------------|
| 4 - 7.5 | **PP4 (Supporting)** | 1 |
| ≥ 8 | **PP4_Moderate** (additionally, at least one specific criterion must be met — see below) | 2 |

**Modification Type:** Disease-specific, Strength (Moderate); Disease-specific (Supporting)

##### Required for Use of PP4 (0.5 points each)

| Finding | Points |
|---------|--------|
| Absent or severely decreased rod electroretinogram (ERG) responses | 0.5 |
| **-OR-** Clinical diagnosis of one: Leber congenital amaurosis/early-onset retinal dystrophy (eoRD)/RP/cone-rod dystrophy (CRD)/Joubert syndrome/Meckel syndrome/Senior-Loken syndrome/Bardet-Biedl syndrome | 0.5 |

##### Specific CEP290 Phenotype Findings List

| Finding | Points |
|---------|--------|
| Previous gene panel testing that did not provide an alternative explanation for visual impairment | 2 |
| Previous exome or genome NGS testing that did not provide an alternative explanation for visual impairment | 4 |
| Participation in a gene therapy trial: study with strict inclusion criteria and subsequent positive results, details not reported | 2 |
| Participation in a gene therapy trial: study with strict inclusion criteria and documented "Significant" improvement of FST or other measure of dark-adapted vision after treatment with CEP290 gene therapy (supporting information required from the treating clinician if sufficient detail is not included in the published report) | 8 |

##### Consistent with CEP290 Phenotype Findings List (0.5 or 1 point each)

**Ocular:**

| Finding | Points |
|---------|--------|
| Congenital / infantile onset | 0.5 |
| Severely reduced visual acuity or no fixation | 0.5 |
| No clear progression in first decade | 0.5 |
| Preserved outer retinal structure relative to vision loss on OCT | 1 |
| Poor peripheral vision | 0.5 |
| Nyctalopia | 0.5 |
| Photophobia | 0.5 |
| Attenuation of retinal blood vessels | 0.5 |
| Optic disc pallor | 0.5 |
| Pigmentary retinopathy / RPE atrophy / bone spicules | 0.5 |
| Nystagmus | 0.5 |
| Eye poking / oculodigital sign | 0.5 |

**Additional:**

| Finding | Points |
|---------|--------|
| Molar tooth sign and/or cerebellar vermis hypoplasia | 1 |
| Occipital encephalocele / Dandy Walker malformation | 0.5 |
| Developmental delay / intellectual disabilities | 0.5 |
| Polydactyly (usually postaxial) | 0.5 |
| Portal fibrosis / hepatobiliary ductal plate malformation | 0.5 |
| Cystic kidney disease / juvenile nephronophthisis / urine concentration defect | 0.5 |
| Obesity | 0.5 |
| Hypotonia / ataxia | 0.5 |
| Psychomotor delay | 0.5 |
| Oculomotor apraxia | 0.5 |
| Infantile / in utero death (requires NGS / WES genotyping) | 0.5 |

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

#### VCEP Specification

| Strength | Default Points | Threshold |
|----------|----------------|-----------|
| **BA1** (Stand Alone) | Not Applicable | gnomAD **Grpmax FAF > 0.016** (use Grpmax FAF if available; use large population databases, i.e., gnomAD) |

**Derivation:** The BA1 value was derived by increasing the BS1 lower cutoff (>0.0016) by one order of magnitude.

**Modification Type:** Disease-specific

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### VCEP Specification

| Strength | Default Points | Threshold |
|----------|----------------|-----------|
| **BS1_Strong** | -4 | Allele frequency of **0.0016 - 0.016** (use gnomAD Grpmax FAF if available) |

**Derivation:** The maximum credible population allele frequency for the disease, based on the Whiffin-Ware calculator, is 1.6 x 10⁻³. This assumes a population frequency of 1 in 2000 individuals, genetic heterogeneity = 20%, penetrance of 100%, allele heterogeneity of 1.

**Modification Type:** Disease-specific

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

#### VCEP Specification

| Strength | Default Points | Application |
|----------|----------------|-------------|
| **BS2_Strong** | -4 | Variant is present in **≥3 homozygotes** without any features of the phenotype. This rule applies to individuals found in the literature who have been well-phenotyped and are unaffected by age 40. Alternatively, this strength can be applied if the variant is present in **≥6 homozygotes in gnomAD v.4.1.0 or later**. |
| **BS2_Supporting** | -1 | Variant is present in **≥3 homozygotes in gnomAD v.4.1.0 or later** |

**Modification Type:** Disease-specific, Strength

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

#### VCEP Specification

| Strength | Default Points | Application |
|----------|----------------|-------------|
| **BS3_Supporting** | -1 | **Not applicable for splicing effects** (replaced by BP7_Strong (RNA)) |

**Modification Type:** Gene-specific, Strength

**Note:** See the [PS3 approved assay table](#approved-functional-assays) for the assays reviewed by the VCEP and the thresholds for a normal readout.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

#### VCEP Specification

| Strength | Default Points | Application |
|----------|----------------|-------------|
| **BS4_Strong** | -4 | One or both variants are absent in a similarly affected family member |

**Modification Type:** Clarification

---

### BP2 - Observed in cis with Pathogenic Variant

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

#### VCEP Specification

| Strength | Default Points | Application |
|----------|----------------|-------------|
| **BP2_Supporting** | -1 | Observed **in cis** with a Pathogenic variant. Use the code if the variant of interest is in cis with a Pathogenic or Likely Pathogenic variant. The other variant must meet a Likely Pathogenic or Pathogenic classification using these rule specifications. |

**Modification Type:** Disease-specific

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

#### VCEP Specifications

- Only applicable if **both** the CADD and SpliceAI scores are below cutoffs.
- Score ranges are based on calculations in Pejaver et al., 2022 (PMID: 36413997).

| Strength | Default Points | Application |
|----------|----------------|-------------|
| **BP4_Moderate** | -2 | Missense variant: CADD score of **≤0.15**. In addition, the highest SpliceAI delta score should also be below the cutoff of 0.1. |
| **BP4_Supporting** | -1 | Missense variant: CADD score between **0.151 - 17.3**. In addition, the highest SpliceAI delta score should also be below the cutoff of 0.1. For a silent/intronic variant outside the designated splice region (conservatively at or beyond positions +7/-21) and synonymous (silent) exonic variants located outside of the first and the last 3 bases of the exon, BP4 can be met if the highest of the four SpliceAI delta scores is below the cutoff of **≤0.1**. Note that BP7 can be met as well. |

**Modification Type:** Gene-specific, Strength (Moderate); Gene-specific (Supporting)

*Note: the CADD cutoffs for BP4_Moderate (≤0.15) and BP4_Supporting (0.151 - 17.3) are reproduced verbatim from the specification.*

---

### BP7 - Synonymous/Intronic Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

#### VCEP Specifications

- BP4 and BP7 can be added unless the variant is in an excluded region.
- **Evolutionary conservation is not considered informative** for application of this code.

| Strength | Default Points | Application |
|----------|----------------|-------------|
| **BP7_Strong** | -4 | **BP7_Strong (RNA)** — used to designate capture of splicing data (not BS3). See the CEP290-specific PVS1 Decision Tree for weighting and combining with other codes. |
| **BP7_Supporting** | -1 | Use not only for synonymous variants but also for intronic variants located outside of the donor/acceptor ±1,2 dinucleotide positions. If the SpliceAI score is ≤0.1, apply BP4 followed by assessment of BP7. |

**Modification Type:** Disease-specific (Strong); Gene-specific (Supporting)

##### Positions Excluded from BP7

- Synonymous substitutions at the first base of an exon
- Synonymous substitutions in the last 3 bases of an exon
- +1 through +7 of donor sequence
- -1 through -21 of acceptor sequence

---

## 4. Not Applicable Criteria

The following ACMG/AMP criteria are **NOT APPLICABLE** for CEP290 variant interpretation:

| Criterion | Original Purpose | Reason Not Applicable |
|-----------|-----------------|----------------------|
| **PS4** | Prevalence in affected individuals | Not Applicable (no reason stated by VCEP) |
| **PM1** | Mutational hot spot / critical domain | Not Applicable (no reason stated by VCEP) |
| **PM6** | De novo (assumed) | Use the PS2 code in lieu of this code for de novo variants |
| **PP2** | Missense in constrained gene | Not applicable for CEP290 |
| **PP5** | Reputable source reports pathogenic | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |
| **BP1** | Missense in truncating disease gene | Not applicable for CEP290 |
| **BP3** | In-frame indel in repetitive region | No repetitive regions with unknown function |
| **BP5** | Alternate molecular basis for disease | Due to the high genetic heterogeneity and limited phenotypic specificities of retinal dystrophies, this rule should not be used. Additionally, the presence of this variant could simply represent carrier status. |
| **BP6** | Reputable source reports benign | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |

---

## 5. Rules for Combining Criteria

This specification uses the **point-based (Tavtigian et al., 2020 Bayesian) classification system**. Sum the default point values of all applied criteria (pathogenic codes positive, benign codes negative) and compare the total to the table below.

### Point-Based Variant Classification Categories

| Category | Point Range |
|----------|-------------|
| **Pathogenic** | ≥ 10 |
| **Likely Pathogenic** | 6 - 9 |
| **Uncertain Significance** | 0 - 5 |
| **Likely Benign** | -6 to -1 |
| **Benign** | ≤ -7 |

*The specification lists the Pathogenic and Benign categories as "10" and "-7" respectively; these are the open-ended upper/lower bounds of the Tavtigian point scale.*

**Note:** BA1 is a stand-alone benign criterion with a default point value of "Not Applicable" — a variant meeting BA1 is classified **Benign** irrespective of the point total.

### Default Point Values by Criterion

| Criterion | Very Strong | Strong | Moderate | Supporting |
|-----------|-------------|--------|----------|------------|
| PVS1 | 8 | 4 | 2 | — |
| PS1 | — | 4 | 2 | 1 |
| PS2 | 8 | 4 | 2 | 1 |
| PS3 | — | — | — | 1 |
| PM2 | — | — | — | 1 |
| PM3 | 8 | 4 | 2 | 1 |
| PM4 | — | — | 2 | 1 |
| PM5 | — | — | 2 | 1 |
| PP1 | — | 4 | 2 | 1 |
| PP3 | — | — | 2 | 1 |
| PP4 | — | — | 2 | 1 |
| BA1 | Stand Alone (Not Applicable) | — | — | — |
| BS1 | — | -4 | — | — |
| BS2 | — | -4 | — | -1 |
| BS3 | — | — | — | -1 |
| BS4 | — | -4 | — | — |
| BP2 | — | — | — | -1 |
| BP4 | — | — | -2 | -1 |
| BP7 | — | -4 | — | -1 |

---

## 6. Appendices

### Appendix A: CEP290 PVS1 Exon Rule Table

Based on the proposal by Walker et al. 2023 with the following CEP290-specific modifications:

1. All exons are considered to be "critical to protein function" based on either frameshifts, pathogenic variants having been identified flanking them (exons 2-8 and 11-53), or being required for CEP290 self-association (exons 9-10).
2. Requirement for being more than 10% of total protein length does not apply.
3. ATG initiation site is located in exon 2.
4. No potential "rescue isoforms" are known.

| Exon | c.start | c.end | Length (bp) | aa start | aa end | Protein domains | PVS1 strength | Exon skipping leads to |
|------|---------|-------|-------------|----------|--------|-----------------|---------------|------------------------|
| 1 | -344 | -28 | 317 | | | | NA | |
| 2 | -27 | 102 | 129 | 1 | 34 | self-association | PVS1 | In frame/no nmd |
| 3 | 103 | 180 | 78 | 35 | 60 | CCI, self-association | PVS1 | In frame/no nmd |
| 4 | 181 | 250 | 70 | 61 | 84 | CCI, self-association | PVS1 | fs/nmd |
| 5 | 251 | 297 | 47 | 84 | 99 | CCI, self-association | PVS1 | fs/nmd |
| 6 | 298 | 441 | 144 | 100 | 147 | CCI, self-association | PVS1 | In frame/no nmd |
| 7 | 442 | 495 | 54 | 148 | 165 | CCI, self-association | PVS1 | In frame/no nmd |
| 8 | 496 | 516 | 21 | 166 | 172 | CCI, self-association | PVS1 | In frame/no nmd |
| 9 | 517 | 669 | 153 | 173 | 223 | CCI, self-association | PVS1 | In frame/no nmd |
| 10 | 670 | 852 | 183 | 224 | 284 | CCI, TM I, self-association | PVS1 | In frame/no nmd |
| 11 | 853 | 942 | 90 | 285 | 314 | CCI, self-association | PVS1 | In frame/no nmd |
| 12 | 943 | 1065 | 123 | 315 | 355 | CCI, self-association | PVS1 | In frame/no nmd |
| 13 | 1066 | 1189 | 124 | 356 | 397 | CCI, TM II, self-association | PVS1 | fs/nmd |
| 14 | 1190 | 1359 | 170 | 397 | 453 | CCI, self-association | PVS1 | fs/nmd |
| 15 | 1360 | 1522 | 163 | 454 | 508 | CCI, TM III, self-association | PVS1 | fs/nmd |
| 16 | 1523 | 1623 | 101 | 508 | 541 | CCI, self-association | PVS1 | fs/nmd |
| 17 | 1624 | 1711 | 88 | 542 | 571 | CCI, self-association | PVS1 | fs/nmd |
| 18 | 1712 | 1824 | 113 | 571 | 608 | CC II, self-association | PVS1 | fs/nmd |
| 19 | 1825 | 1909 | 85 | 609 | 637 | CC II, self-association | PVS1 | fs/nmd |
| 20 | 1910 | 2052 | 143 | 637 | 684 | CC II, self-association | PVS1 | fs/nmd |
| 21 | 2053 | 2217 | 165 | 685 | 739 | CC III, self-association, NPHP5 binding | PVS1 | In frame/no nmd |
| 22 | 2218 | 2367 | 150 | 740 | 789 | CC III, CC IV, NPHP5 binding | PVS1 | In frame/no nmd |
| 23 | 2368 | 2483 | 116 | 790 | 828 | CC IV, NPHP5 binding | PVS1 | fs/nmd |
| 24 | 2484 | 2586 | 103 | 828 | 862 | CC IV, NPHP5 binding | PVS1 | fs/nmd |
| 25 | 2587 | 2817 | 231 | 863 | 939 | CC IV, NPHP5 binding | PVS1 | In frame/no nmd |
| 26 | 2818 | 2991 | 174 | 940 | 997 | CC V | PVS1 | In frame/no nmd |
| 27 | 2992 | 3103 | 112 | 998 | 1035 | CC V | PVS1 | fs/nmd |
| 28 | 3104 | 3309 | 206 | 1035 | 1103 | CC VI | PVS1 | fs/nmd |
| 29 | 3310 | 3461 | 152 | 1104 | 1154 | CC VI, CC VII | PVS1 | fs/nmd |
| 30 | 3462 | 3573 | 112 | 1154 | 1191 | CC VII | PVS1 | fs/nmd |
| 31 | 3574 | 4029 | 456 | 1192 | 1343 | CC VIII, CC IX, KID I | PVS1 | In frame/no nmd |
| 32 | 4030 | 4194 | 165 | 1344 | 1398 | CC IX | PVS1 | In frame/no nmd |
| 33 | 4195 | 4302 | 108 | 1399 | 1434 | CC IX | PVS1 | In frame/no nmd |
| 34 | 4303 | 4437 | 135 | 1435 | 1479 | CC X | PVS1 | In frame/no nmd |
| 35 | 4438 | 4704 | 267 | 1480 | 1568 | CC X, CC XI | PVS1 | In frame/no nmd |
| 36 | 4705 | 4812 | 108 | 1569 | 1604 | CC XI | PVS1 | In frame/no nmd |
| 37 | 4813 | 5012 | 200 | 1605 | 1671 | CC XII | PVS1 | fs/nmd |
| 38 | 5013 | 5226 | 214 | 1671 | 1742 | CC XII, MM binding | PVS1 | fs/nmd |
| 39 | 5227 | 5364 | 138 | 1743 | 1788 | CC XII, MM binding | PVS1 | In frame/no nmd |
| 40 | 5365 | 5586 | 222 | 1789 | 1862 | CC XII, MM binding | PVS1 | In frame/no nmd |
| 41 | 5587 | 5709 | 123 | 1863 | 1903 | CC XII, KID II, MM binding, MM binding | PVS1 | In frame/no nmd |
| 42 | 5710 | 5855 | 146 | 1904 | 1952 | CC XII, KID III, BP_NLS, MM binding | PVS1 | fs/nmd |
| 43 | 5856 | 6011 | 156 | 1952 | 2004 | CC XII, MM binding | PVS1 | In frame/no nmd |
| 44 | 6012 | 6135 | 124 | 2004 | 2045 | CC XII | PVS1 | fs/nmd |
| 45 | 6136 | 6270 | 135 | 2046 | 2090 | CC XIII | PVS1 | In frame/no nmd |
| 46 | 6271 | 6357 | 87 | 2091 | 2119 | CC XIII, P-loop | PVS1 | In frame/no nmd |
| 47 | 6358 | 6522 | 165 | 2120 | 2174 | CC XIII | PVS1 | In frame/no nmd |
| 48 | 6523 | 6645 | 123 | 2175 | 2215 | CC XIII, KID IV | PVS1 | In frame/no nmd |
| 49 | 6646 | 6818 | 173 | 2216 | 2273 | CC XIII | PVS1 | fs/nmd |
| 50 | 6819 | 6960 | 142 | 2273 | 2320 | CC XIII | PVS1 | fs/nmd |
| 51 | 6961 | 7034 | 74 | 2321 | 2345 | CC XIII | PVS1 | fs/nmd |
| 52 | 7035 | 7129 | 95 | 2345 | 2377 | CC XIII | PVS1 | fs/nmd |
| 53 | 7130 | 7209 | 80 | 2377 | 2403 | CC XIII, KID V | PVS1 | fs/nmd |
| 54 | 7210 | *171 | 402 | 2404 | 2479 | CC XIII, KID VI | PVS1 | NA |

*Abbreviations: CC, coiled-coil domain; TM, tropomyosin homology domain; KID, RepA/Rep+ protein KID; NLS_BP, bipartite nuclear localization signal; P-loop, ATP/GTP-binding site motif A (P-loop); MM, microtubule/membrane binding. Total protein length: 2479 amino acids.*

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Points |
|-----------|-----------|----------|--------|
| BA1 | gnomAD Grpmax FAF > 0.016 | Stand Alone | Not Applicable |
| BS1 | Allele frequency 0.0016 - 0.016 (gnomAD Grpmax FAF) | Strong | -4 |
| PM2 | gnomAD total allele frequency ≤ 6.0 x 10⁻⁴ | Supporting | 1 |

### Appendix C: Key References

| Citation | PMID | Topic |
|----------|------|-------|
| Richards et al., 2015 | 25741868 | ACMG/AMP Variant Interpretation Guidelines |
| Abou Tayoun et al., 2018 | 30192042 | ClinGen SVI PVS1 recommendations |
| Walker et al., 2023 | 37352859 | ClinGen SVI Splicing Subgroup recommendations |
| Kilander et al., 2018 | 30478281 | CEP290 variant disrupts primary cilium integrity and Sonic Hedgehog machinery |
| Baye et al., 2011 | 21257638 | N-terminal CEP290 restores vision in zebrafish model |
| Shimada et al., 2017 | 28700940 | In vitro modeling using ciliopathy-patient-derived cells |
| Esteve-Garcia et al., 2024 | 39766851 | Expanding the clinical spectrum of CEP290 variants |
| Garanto et al., 2015 | 25761237 | Species-dependent splice recognition of a cryptic exon |
| Corral-Serrano et al., 2023 | 37371046 | Eupatilin improves cilia defects in human CEP290 ciliopathy models |
| Drivas et al., 2015 | 26062849 | Basal exon skipping and genetic pleiotropy |
| Pejaver et al., 2022 | 36413997 | Calibration of computational tools; ClinGen PP3/BP4 recommendations |
| ClinGen SVI De Novo Criteria (PS2 & PM6) Version 1.1 | - | https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf |
| ClinGen SVI PM3 Criterion Version 1 | - | https://clinicalgenome.org/site/assets/files/3717/svi_proposal_for_pm3_criterion_-_version_1.pdf |
| ClinGen SVI VCEP Review Committee (PP5/BP6) | 29543229 | Criteria not for use |

### Appendix D: Supplementary Documents

| Document | Description | Date |
|----------|-------------|------|
| PS3 Approved Functional Assays | Description of all functional assays to be used for consideration of the PS3 rule | March 13, 2026 |
| CEP290-specific PVS1 Decision Tree | CEP290-specific PVS1 decision tree and other modified codes based on Walker 2023; sub-parts (a) through (c) include detailed descriptions of rules for variants that are likely to be spliceogenic or for which effects on splicing have been considered | March 12, 2026 |
| PS2/PM6 Tables | Point table from SVI Recommendation for De Novo Criteria (PS2 & PM6) - Version 1.1 | - |
| PM3 Tables | PM3: Table 1 - points awarded per in trans occurrence; Table 2 - evidence strength levels | - |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | July 2, 2026 | Initial released version |

---

*This document is based on the ClinGen Leber Congenital Amaurosis/early onset Retinal Dystrophy Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for CEP290 Version 1.0 (https://cspec.genome.network/cspec/ui/svi/doc/GN226)*
