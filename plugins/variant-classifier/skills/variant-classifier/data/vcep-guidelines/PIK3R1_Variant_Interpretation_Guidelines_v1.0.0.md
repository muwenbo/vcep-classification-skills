# Comprehensive Variant Interpretation Guidelines for PIK3R1

## ClinGen Antibody Deficiencies VCEP Specifications for PIK3R1 (Version 1.0)

**Affiliation:** ClinGen Antibody Deficiencies Variant Curation Expert Panel (Antibody Deficiencies VCEP; ClinGen affiliation 50095)
**Version:** 1.0
**Release Date:** April 29, 2026
**DOI:** 10.5281/zenodo.21434763
**Based on:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015 ACMG/AMP Variant Interpretation Guidelines

---

## Table of Contents

1. [Gene and Disease Information](#1-gene-and-disease-information)
2. [Pathogenic Criteria](#2-pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo (Confirmed and Assumed)](#ps2---de-novo-confirmed-and-assumed)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PS4 - Prevalence in Affected](#ps4---prevalence-in-affected)
   - [PM2 - Absent from Controls](#pm2---absent-from-controls)
   - [PM4 - Protein Length Changes](#pm4---protein-length-changes)
   - [PM5 - Novel Missense at Same Residue](#pm5---novel-missense-at-same-residue)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
   - [PP4 - Phenotype Specificity](#pp4---phenotype-specificity)
3. [Benign Criteria](#3-benign-criteria)
   - [BA1 - Stand-Alone Benign](#ba1---stand-alone-benign)
   - [BS1 - Allele Frequency Greater Than Expected](#bs1---allele-frequency-greater-than-expected)
   - [BS3 - Functional Studies (Benign)](#bs3---functional-studies-benign)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP4 - Computational Evidence (Benign)](#bp4---computational-evidence-benign)
   - [BP5 - Alternate Molecular Basis](#bp5---alternate-molecular-basis)
   - [BP7 - Synonymous/Intronic Variants](#bp7---synonymousintronic-variants)
4. [Not Applicable Criteria](#4-not-applicable-criteria)
5. [Rules for Combining Criteria](#5-rules-for-combining-criteria)
6. [Appendices](#6-appendices)

---

## 1. Gene and Disease Information

| Parameter | Value |
|-----------|-------|
| **Gene** | PIK3R1 (HGNC:8979) |
| **HGNC Name** | Phosphoinositide-3-kinase regulatory subunit 1 |
| **Reference Transcript** | NM_181523.3 (MANE) |
| **Disease** | PIK3R1-related immunodeficiency and SHORT syndrome |
| **MONDO ID** | MONDO:1060136 |
| **Mode of Inheritance** | Autosomal dominant inheritance |

### Key Gene Characteristics

- The Antibody Deficiencies GCEP has changed the curated disease term from "immunodeficiency 36 with lymphoproliferation" (MONDO:0014453) to **"PIK3R1-related immunodeficiency and SHORT syndrome" (MONDO:1060136)**.
- Three biologically-relevant transcripts are recognized: **NM_181523.3 (MANE)**, **NM_181504.4**, and **NM_181524.2**. The three isoforms differ at the N-terminus.
- Two alternative start codons are known downstream of codon 306 of PIK3R1 in the MANE transcript encoding the p85α isoform (PMID: 28802037).
- The gnomAD v2.1.1 missense Z score for PIK3R1 (Z = 2.72) suggests this gene is **not** constrained for missense variation; both benign and pathogenic missense variants are present in PIK3R1.
- Variants published only in association with **autosomal recessive agammaglobulinemia 7** are outside the scope of these specifications (that condition has not been lumped with the autosomal dominant condition evaluated here).

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**General Caveats:** Beware of genes where LOF is not a known disease mechanism; use caution interpreting LOF variants at the extreme 3' end of a gene; use caution with splice variants predicted to lead to exon skipping but leaving the remainder of the protein intact; use caution in the presence of multiple transcripts.

#### Strength Levels

| Strength | Points | Criteria |
|----------|--------|----------|
| **PVS1** (Very Strong) | 8 | • Nonsense or frameshift variant introducing a premature stop codon between **c.917 and c.1890**, predicted to trigger NMD, where the exon is present in **all 3** biologically-relevant transcripts (NM_181523.3, NM_181504.4, NM_181524.2)<br>• Canonical splicing variant predicted to result in skipping of **exon 8, 10, or 12**, which would disrupt the frame and be predicted to trigger NMD |
| **PVS1_Strong** | 4 | • Nonsense or frameshift variant introducing a premature stop between **codons 631 and 645**, predicted to trigger NMD but located **45 nucleotides or less** from the NMD prediction boundary, where the exon is present in all 3 biologically-relevant transcripts<br>• Nonsense or frameshift variant introducing a premature stop between **codons 646 and 718** that is **not** predicted to trigger NMD but disrupts the **cSH2 domain**<br>• Canonical splicing variant predicted to result in skipping of in-frame **exon 9 or 11** (nSH2 domain), in-frame **exon 13 or 14** (iSH2 domain), or either in-frame **exon 15** or out-of-frame **exon 16** (cSH2 domain; PMID: 38043374) |
| **PVS1_Moderate** | 2 | • Nonsense or frameshift variant introducing a premature stop between **codons 719 and 724** that is **not** predicted to trigger NMD and does **not** disrupt the cSH2 domain |
| **PVS1_Supporting** | — | Not specified by VCEP |

#### PIK3R1-Specific Exclusions (apply at every strength level)

- **Transcript-restricted PTCs:** If a nonsense or frameshift variant introduces a premature stop codon between **c.4 and c.916**, predicted to trigger NMD, but the exon is present **only** in the MANE transcript NM_181523.3 and absent from NM_181504.4 and NM_181524.2, **do not apply PVS1 at any strength** in the context of this gene-disease relationship (MONDO:1060136). Such variants have so far been published only in association with autosomal recessive agammaglobulinemia 7, which is outside the scope of the current specifications.
- **Initiation codon variants:** **Do not apply PVS1 at any strength** for initiation codon variants. Two known alternative start codons are located after codon 306 of PIK3R1 in the MANE transcript encoding the p85α isoform (PMID: 28802037). Although known disease-causing variants exist upstream of these alternative start codons, indicating that disruption of the p85α isoform alone is sufficient to cause disease, these variants have so far been published only in association with agammaglobulinemia 7 with autosomal recessive inheritance and are not considered applicable to the current specifications.
- **Exon 1-7 skipping:** If a canonical splicing variant is predicted to result in skipping of exon 1 (non-coding), exon 2 (contains the start codon for the MANE transcript), exon 3 (in-frame), exon 4 (in-frame), exon 5 (in-frame), exon 6 (out-of-frame), or exon 7 (out-of-frame), **do not apply PVS1 at any strength** in the context of MONDO:1060136 (same rationale as above).
- **RNA evidence route:** If a missense, synonymous, or intronic variant outside of the canonical splice sites has a **SpliceAI score >0.2** and has been confirmed to cause complete or near-complete disruption of splicing within the mRNA in a study of patient RNA or minigene assay, **avoid PP3 and PS3_Supporting** and evaluate **PVS1(RNA)** instead (PMID: 37352859).

*Modification type: Gene-specific. See [Appendix D](#appendix-d-pvs1-decision-tree-summary) for the full decision tree and the PIK3R1 exon map.*

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Points | Application |
|----------|--------|-------------|
| **PS1** (Strong) | 4 | Missense variants where the other variant was classified **Pathogenic** by VCEP standards **without using PS1**. Splicing predictions (by SpliceAI) should remain the same for WT and both mutant alleles. |
| **PS1_Moderate** | 2 | Missense variants where the other variant was classified **Likely Pathogenic** by VCEP standards **without using PS1**. Splicing predictions (by SpliceAI) should remain the same for WT and both mutant alleles. |
| **PS1_Supporting** | 1 | Canonical splice variants or variants predicted to disrupt splicing, per the splicing PS1 matrix below. |

#### PS1 for Splice Variants

PS1 may be used for canonical splice variants or variants predicted to disrupt splicing when the predicted impact is the same as a previously classified P / LP variant. The appropriate PS1 strength level is determined (adapted from Table 2 in PMID: 37352859) by the locations of the variant under assessment and the comparison variant within the splice donor or splice acceptor motif, as well as the classification of the comparison variant as Pathogenic vs. Likely Pathogenic.

**Note:** PS1 strength is reduced for variants disrupting a canonical splice site adjacent to an out-of-frame exon because PVS1 (Very Strong) has already been applied.

| Location of variant under assessment | Adjacent exon | Computational or LoF code met by variant under assessment | Position of comparison variant relative to variant under assessment | Code met if comparison variant is **Pathogenic** | Code met if comparison variant is **Likely Pathogenic** |
|---|---|---|---|---|---|
| Outside of +1/-1/+2/-2 dinucleotide positions | 8, 9, 10, 11, 12, 13, 14, or 15 | PP3 | At same nucleotide | **PS1** (d) | **PS1_Moderate** (b) |
| Outside of +1/-1/+2/-2 dinucleotide positions | 8, 9, 10, 11, 12, 13, 14, or 15 | PP3 | Within same splice donor/acceptor motif (including at +1/+2/-1/-2 positions) | **PS1_Moderate** (c) | **PS1_Supporting** (a) |
| Within +1/-1/+2/-2 dinucleotide positions | 8, 10, or 12 | PVS1 | Within same +1/+2/-1/-2 dinucleotide | **PS1_Supporting** (f) | N/A (e) |
| Within +1/-1/+2/-2 dinucleotide positions | 8, 10, or 12 | PVS1 | Within same splice donor/acceptor motif but outside of +1/+2/-1/-2 dinucleotide | **PS1_Supporting** (j) | **PS1_Supporting** (i) |
| Within +1/-1/+2/-2 dinucleotide positions | 9, 11, 13, 14, or 15 | PVS1_Strong | Within same +1/+2/-1/-2 dinucleotide | **PS1** (h) | N/A (g) |
| Within +1/-1/+2/-2 dinucleotide positions | 9, 11, 13, 14, or 15 | PVS1_Strong | Within same splice donor/acceptor motif but outside of +1/+2/-1/-2 dinucleotide | **PS1_Moderate** (l) | **PS1_Supporting** (k) |

*Modification type: General recommendation, Strength.*

---

### PS2 - De Novo (Confirmed and Assumed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

#### VCEP Specifications

- For PS2, both maternity and paternity must be confirmed, with no family history of disease.
- **Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.
- **This code is also used in place of PM6** for assumed *de novo* occurrences without confirmation of paternity and maternity. PM6 is Not Applicable for PIK3R1.

#### Determining Phenotypic Consistency

The "phenotypic consistency" row used on the SVI point-counting table below is chosen for each proband by the number of phenotype points scored by that proband on the **PS4 scoring system (Table 3)**:

| Proband's PS4 phenotype points and genotyping | Phenotypic consistency row to use |
|---|---|
| (A) ≥4 but <6 phenotype points **and lacks** genotyping to rule out variants in the *PIK3CD* locus | "Phenotype consistent with gene but not highly specific and high genetic heterogeneity" |
| (B) ≥6 phenotype points **but lacks** genotyping to rule out variants in the *PIK3CD* locus | "Phenotype consistent with gene but not highly specific and high genetic heterogeneity" |
| (C) ≥10 phenotype points **AND has** genotyping to rule out variants in the *PIK3CD* locus | "Phenotype highly specific for gene" |

#### Points Awarded per De Novo Occurrence (Table 1)

| Phenotypic Consistency | Confirmed de novo | Assumed de novo |
|------------------------|-------------------|-----------------|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity* | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

*Maximum allowable value of 1 may contribute to overall score.

#### Determining Evidence Strength Level (Table 2)

| Total Points | Evidence Strength | Points Awarded |
|--------------|-------------------|----------------|
| 0.5 | PS2_Supporting | 1 |
| 1 | PS2_Moderate | 2 |
| 2 | PS2 (Strong) | 4 |
| 4 | PS2_VeryStrong | 8 |

*Modification type: Disease-specific.*

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

#### VCEP Specifications

| Strength | Points | Application |
|----------|--------|-------------|
| **PS3** (Strong) | 4 | • PS3 may potentially be applied at the default strength level of Strong for evidence from an **animal model** expressing the variant of interest and recapitulating the immunodeficiency phenotype (PMID: 26974159, PMID: 28632845).<br>• PS3 will be applied for an abnormal result in an approved *in vitro* assay with an **OddsPath >18.7** (PMID: 31892348). One example has been found in the literature: ratio of variant enrichment in pS6-high and/or pAKT-high T cells vs. pS6-low and/or pAKT-low T cells (PMID: 40543502). |
| **PS3_Moderate** | 2 | Abnormal result in an approved *in vitro* assay with **at least 11 known pathogenic or benign variant controls** (classified using these specifications, PMID: 31892348). |
| **PS3_Supporting** | 1 | Abnormal result in an approved *in vitro* assay. Approved assay classes and specific assay instances are listed below. |

#### Approved Assay Instances for PS3_Supporting

| Assay Class | PMIDs |
|-------------|-------|
| Lipid kinase activity | 28167755 |
| AKT kinase activity | 23810379, 25133428, 25488983, 28167755 |
| Protein binding | 25488983 |
| Conformational dynamics | 28167755 |

#### Assays Excluded from PS3_Supporting

- **mRNA splicing assays** showing exon 11 skipping that affect all or nearly all transcripts (PMID: 27221134, PMID: 25133428, PMID: 25488983) are **not** used for PS3_Supporting; these can be used in combination with a SpliceAI prediction of disruption of a splice donor / acceptor site to meet **PVS1_Strong (RNA)** instead.
- **pAKT assays in patient cells with endogenous PIK3R1** (patient T blast cells and patient dermal fibroblasts) are considered part of **PP4**, not PS3_Supporting.

*Modification type: Disease-specific (Strong, Supporting); Gene-specific (Moderate).*

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

#### VCEP Specifications

| Strength | Points | Application (Table 4) |
|----------|--------|-------------|
| **PS4** (Strong) | 4 | **Four or more** independent probands meet the phenotype scoring criteria in Table 3 and the genetic testing requirements below. |
| **PS4_Moderate** | 2 | **2-3** independent probands meet the phenotype scoring criteria in Table 3 and the genetic testing requirements below. |
| **PS4_Supporting** | 1 | **One** proband meets the phenotype scoring criteria in Table 3 and the genetic testing requirements below. |

#### Requirements (apply at all strength levels)

- A proband used for PP4 or PP4_Moderate **cannot** also be included in PS4 at any strength.
- Point strength has been determined based on a survey of clinical experts, with the goal of quantifying the degree to which a proband's phenotypes are specific to PIK3R1-related immunodeficiency. Phenotypes have been grouped into categories such as "respiratory findings" or "gastrointestinal disease" to prioritize the diversity of systems affected. Probands receive full points for at least one reported feature in the category. Points per category have been tailored to reward those considered most characteristic of and prevalent within patients with PIK3R1-related immunodeficiency.
- A proband must reach **≥6 points** in the phenotype scoring criteria (Table 3) **and**, at minimum, a primary immunodeficiency or antibody gene testing panel must have identified **no likely pathogenic or pathogenic variants in the *PIK3CD* locus** in order to be counted toward PS4.
  - Genome or exome sequencing is acceptable in lieu of a gene panel.
  - For genes associated with autosomal recessive disorders, carrier status is acceptable.
- If **no gene testing panel** was performed, additional phenotypic features (reaching **≥10 points**) are required to count the proband toward PS4.
- Scoring of probands with previous genetic testing should be prioritized, particularly in the event of scoring historical or rare probands/variants.
- In order to be evaluated for this criterion, the variant **must not meet BS1 or BA1**.

*See [Appendix C](#appendix-c-table-3---ps4--pp4-phenotype-scoring-criteria) for the full Table 3 phenotype scoring rubric.*

*Modification type: Disease-specific, Strength.*

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes, or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

#### VCEP Specification

| Strength | Points | Threshold |
|----------|--------|-----------|
| **PM2_Supporting** | 1 | Total allele frequency **<0.00000132** across all populations in **gnomAD v4.1.0** |

##### Calculation Parameters (Whiffin/Ware Calculator)

Threshold determined using the Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/), with the prevalence estimated for primary immunodeficiency and the inheritance tailored to the autosomal dominant mode of inheritance:

- Prevalence: 1 in 4000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 1
- Penetrance: 0.95

*Modification type: Disease-specific, Strength.*

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **PM4** (Moderate) | 2 | • **In-frame deletion** resulting in a protein length change greater than or equal to 2 amino acids, if at least one of the deleted nucleotides is highly conserved (**PhyloP score ≥2.0**)<br>• **In-frame insertion** resulting in a protein length change greater than or equal to 2 amino acids, if at least one of the adjacent amino acids is highly conserved (**PhyloP score ≥2.0**)<br>• **Stop-loss variant** resulting in the addition of **2 or more amino acids** to the C-terminus |

#### Additional Requirements

- This code is **mutually exclusive with PVS1** (PMID: 30192042) and **with PP3** (in order not to double-count *in silico* predictor data).
- The region of the protein affected by the variant is key to consider. If only benign or likely benign variants are known to be located within this region, the region is polymorphic and PM4 does not apply.

*Modification type: Disease-specific, Strength.*

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **PM5** (Moderate) | 2 | Missense variant where another missense variant encoding a different amino acid change in the same codon was classified **Pathogenic** by Antibody Deficiencies VCEP specifications for PIK3R1 without using PM5 |
| **PM5_Supporting** | 1 | Missense variant where another missense variant encoding a different amino acid change in the same codon was classified **Likely Pathogenic** by Antibody Deficiencies VCEP specifications for PIK3R1 without using PM5 |

#### Additional Requirements (both strength levels)

- Neither the variant of interest nor the comparison variant should be predicted to affect splicing (**all SpliceAI Δ scores <0.2** for both variants).
- The variant of interest must have a **higher Grantham score** than the comparison variant (https://en.wikipedia.org/wiki/Amino_acid_replacement#Grantham's_distance).
- Do not apply at a codon where any benign variants are known.
- In order to be evaluated for this criterion, the variant **must not meet BS1 or BA1**.

*Modification type: Clarification.*

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specification:** Use ClinGen SVI recommendations for the co-segregation criterion (PMID: 30311386) to determine the appropriate evidence strength based on the LOD score calculated by counting the number of affected individuals in a family (minus the proband) that are positive for the variant.

| Strength | Points | Application |
|----------|--------|-------------|
| **PP1_Strong** | 4 | Variant co-segregates with the affected phenotype across **at least 4 meioses**, either in one family or combined across multiple unrelated families |
| **PP1_Moderate** | 2 | Variant co-segregates with the affected phenotype across the proband and **two affected first degree relatives**, across the proband and **one affected second degree relative**, or across **two unrelated probands and one affected first degree relative each** (2 meioses total) |
| **PP1_Supporting** | 1 | Variant co-segregates with the affected phenotype across the proband and **one affected first degree relative** (1 meiosis) |

#### Additional Requirements (all strength levels)

- PP1 requires each family member to reach **at least 6 points in the PS4 counting rubric (Table 3)** in order to be considered affected for the purpose of counting co-segregations.
- PP1 should **not** be applied when a variant also has population data meeting **BA1 or BS1**, since a common variant may appear to segregate with the disease by chance.

*Modification type: General recommendation, Strength.*

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many *in silico* algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **PP3** (Supporting) | 1 | • **Missense variant** with both **REVEL ≥0.644** and **CADD ≥26.0**<br>• **Missense, synonymous, or intronic variant** outside the +/-1,2 dinucleotide positions predicted as damaging using SpliceAI (**Δ score for donor gain, donor loss, acceptor gain, or acceptor loss ≥0.2**; PMID: 37352859) |

#### Notes

- Splice impact must be assessed for every missense, small in-frame insertion and/or deletion, synonymous, or intronic variant.
- The VCEP will try to determine during the pilot whether higher strength levels of PP3 are appropriate for PIK3R1 variants.

*Modification type: Disease-specific.*

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **PP4_Moderate** | 2 | Proband scores **≥10 phenotype points** in the PS4 counting rubric (Table 3) **AND** has genotyping that did not identify an alternative basis for disease at the *PIK3CD* locus **AND** has **patient cell-based evidence of abnormally high activity of the disease-relevant PI3K delta pathway** |
| **PP4** (Supporting) | 1 | Proband scores **≥10 phenotype points** in the PS4 counting rubric (Table 3) **AND** has genotyping that did not identify an alternative basis for disease at the *PIK3CD* locus |

#### Patient Cell-Based Evidence (for PP4_Moderate)

Patient cell-based experiments generally isolate T cells from affected and unaffected patients and often perform stimulation by anti-CD3 and anti-CD28 antibodies, followed by assessment of PI3K delta pathway function using western blotting or flow cytometry in combination with phospho-specific antibodies. These methods detect levels of **AKT phosphorylation at Ser473 or Thr308** (PMID: 25133428, PMID: 25488983) and/or **S6 phosphorylation at Ser235/Ser236 or Ser240/Ser244** (PMID: 25488983). Phosphorylation may be upregulated in cells from the affected patient relative to the healthy control.

#### Additional Requirements (both strength levels)

- A proband used for PP4 or PP4_Moderate **cannot** be included in PS4.
- In order to be evaluated for this criterion, the variant **must not meet BS1 or BA1**.

*Modification type: Disease-specific.*

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes, or Exome Aggregation Consortium.

#### VCEP Specification

| Strength | Threshold |
|----------|-----------|
| **BA1** (Stand Alone) | **GrpMax filtering allele frequency ≥0.00316** in gnomAD v4.1.0 |

- If GrpMax filtering allele frequency is not listed for the variant, this code is applicable to the **maximum allele frequency among the five major continental populations** (African / African-American, East Asian, European non-Finnish, Latino / Admixed-American, or South Asian).

##### Calculation Parameters (Whiffin/Ware Calculator)

- Inheritance: **biallelic** (in order to generate a higher / more stringent threshold that would rule out a variant as a credible cause of either autosomal dominant or autosomal recessive disease)
- Prevalence: **1 in 100,000** (calculated at 1 in 7,500,000 based on the USIDNET cohort, PMID: 34352450, but adjusted based on expectation that cases are actually more common, resulting in a much more frequent / more aggressive prevalence estimate of 1 in 100,000 in order to generate a more conservative estimate)
- Allelic heterogeneity: 1
- Genetic heterogeneity: 1
- Penetrance: 1

**Note:** The values cited above (e.g., complete penetrance) are not asserted to be true for this condition. Rather, they are used in order to derive the most rigorous thresholds possible for a disease for which there are incomplete population epidemiology data.

*Default point value: Not Applicable (stand-alone). Modification type: Disease-specific.*

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### VCEP Specification

| Strength | Points | Threshold |
|----------|--------|-----------|
| **BS1** (Strong) | -4 | **GrpMax filtering allele frequency ≥0.000316** in gnomAD v4.1.0 |

- If GrpMax filtering allele frequency is not listed for the variant, this code is applicable to the **maximum allele frequency among the five major continental populations** (African / African-American, East Asian, European non-Finnish, Latino / Admixed-American, or South Asian).
- The BS1 threshold was derived by decreasing the BA1 cutoff (≥0.00316) by **one order of magnitude**.

*Modification type: Disease-specific.*

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established *in vitro* or *in vivo* functional studies show no damaging effect on protein function or splicing.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **BS3** (Strong) | -4 | • BS3 may potentially be applied at the default strength level of Strong for evidence from an **animal model** expressing the variant of interest and failing to recapitulate the phenotype. Animal models will be reviewed on a case-by-case basis by the VCEP to determine the appropriate strength level.<br>• BS3 will be applied for a non-damaging result in an approved *in vitro* assay with an **OddsPath <0.053** (PMID: 31892348). **No such assays have yet been identified in the PIK3R1 literature.** |
| **BS3_Moderate** | -2 | Non-damaging result in an approved *in vitro* assay with **at least 11 known pathogenic or benign variant controls** (classified using these specifications, PMID: 31892348). While one such *in vitro* assay has been identified in the PIK3R1 literature (PMID: 40543502), the authors have recommended rewarding a non-damaging result in their assay of the ratio of enrichment of the variant in pS6-high and/or pAKT-high T cells vs. pS6-low and/or pAKT-low T cells for **BS3_Supporting**, based on their calculated OddsPath of 0.25. |
| **BS3_Supporting** | -1 | • Normal result in **at least two different** approved *in vitro* assays. Approved assay classes and specific assay instances: lipid kinase activity (PMID: 28167755); AKT kinase activity (PMID: 23810379, 25133428, 25488983, 28167755); protein binding (PMID: 25488983); conformational dynamics (PMID: 28167755).<br>• **OR** a normal result in the following approved *in vitro* assay: ratio of variant enrichment in pS6-high and/or pAKT-high T cells vs. pS6-low and/or pAKT-low T cells (PMID: 40543502, OddsPath 0.25). |

*Modification type: Disease-specific.*

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e., cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **BS4** (Strong) | -4 | Met at the default level of strength when **at least 2 affected family members** do not harbor the variant |
| **BS4_Supporting** | -1 | Met if **only 1 affected family member** does not harbor the variant |

#### Additional Requirements (both strength levels)

- Use caution in case the phenotype is not highly specific. Each affected family member lacking the variant must reach **at least 6 points in the PS4 scoring table (Table 3)** to be considered for this code.

*Modification type: Disease-specific, Strength.*

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many *in silico* algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **BP4** (Supporting) | -1 | • **Missense variant** with both **REVEL ≤0.290** and **CADD ≤21.5**, as well as SpliceAI Δ scores for donor gain, donor loss, acceptor gain, and acceptor loss **<0.1**<br>• **Synonymous or intronic variants** not predicted to impact splicing by SpliceAI (Δ scores for donor gain, donor loss, acceptor gain, and acceptor loss **<0.1**; PMID: 37352859) |

#### Notes

- BP4 can be used in combination with BP7 for synonymous or intronic variants without being considered double-counting (PMID: 37352859).
- The VCEP will try to determine during the pilot whether higher strength levels of BP4 are appropriate for PIK3R1 variants.

*Modification type: Disease-specific.*

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **BP5** (Supporting) | -1 | **At least 2 cases** with an alternative molecular basis for disease are required, to mitigate the reliance on assertions of variant pathogenicity in genes outside the purview of the Antibody Deficiencies VCEP |

*Modification type: Disease-specific.*

---

### BP7 - Synonymous/Intronic Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **BP7_Strong (RNA)** | -4 | Met by variants with **experimental evidence of no impact on splicing** |
| **BP7** (Supporting) | -1 | • **Synonymous variants** (except those located in the first nucleotide of an exon or last 3 nucleotides of an exon) not predicted to impact splicing by SpliceAI (all Δ scores **<0.1**; PMID: 37352859)<br>• **Intronic variants** (outside of the +1 to +6 and -1 to -20 positions relative to the exon) not predicted to impact splicing by SpliceAI (all Δ scores **<0.1**; PMID: 37352859) |

#### Notes

- BP7 can be used in combination with BP4 for synonymous or intronic variants without being considered double-counting (PMID: 37352859).

*Modification type: Clarification.*

---

## 4. Not Applicable Criteria

The following ACMG/AMP criteria are **NOT APPLICABLE** for PIK3R1 variant interpretation:

| Criterion | Original Purpose | Reason Not Applicable |
|-----------|-----------------|----------------------|
| **PM1** | Mutational hot spot / critical domain | Marked Not Applicable by the VCEP (no comment provided) |
| **PM3** | In trans with pathogenic variant | Not applicable, as this code is specific to recessive disorders |
| **PM6** | Assumed de novo | Not applicable. When a variant has apparent de novo origin and paternity and maternity are suspected but not confirmed, use the **PS2** code instead of PM6 |
| **PP2** | Low rate of benign missense | Does not apply. The gnomAD v2.1.1 missense Z score for PIK3R1 (Z = 2.72) suggests this gene is not constrained for missense variation. Both benign and pathogenic missense variants are present in PIK3R1 |
| **PP5** | Reputable source reports pathogenic | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |
| **BS2** | Observed in healthy adult | Does not apply due to incomplete penetrance and variable expressivity of disease |
| **BP1** | Missense in truncating disease gene | Not applicable, as pathogenic PIK3R1 variants are not limited to truncating variants, but can be missense as well |
| **BP2** | In trans/in cis with pathogenic variant | Do not use this criterion. BP2 is considered not applicable, as the field at present does not understand all of the potential allelic mechanisms associated with PIK3R1 variants, so that the possibility of diverse combinatorial variant effects cannot be excluded. This has been described for other inborn errors of immunity genes |
| **BP3** | In-frame deletion in repetitive region | Not applicable, as repetitive regions of unknown function are not known within PIK3R1 |
| **BP6** | Reputable source reports benign | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |

---

## 5. Rules for Combining Criteria

The Antibody Deficiencies VCEP has adopted the **Bayesian points scale** for all criteria combinations (PMID: 29300386), including in scenarios where a variant has met a combination of pro-pathogenic and pro-benign evidence codes. The point scale and classification categories come from Tables 2 and 3 of PMID: 32720330.

### Point Values for ACMG/AMP Strength of Evidence Categories

| Evidence Strength | Pathogenic Points | Benign Points |
|-------------------|-------------------|---------------|
| Indeterminate | 0 | 0 |
| Supporting | +1 | -1 |
| Moderate | +2 | -2 |
| Strong | +4 | -4 |
| Very Strong | +8 | -8 |

### Point-Based Variant Classification Categories

| Category | Point Range |
|----------|-------------|
| **Pathogenic** | ≥10 |
| **Likely Pathogenic** | 6 to 9 |
| **Uncertain Significance** | 0 to 5 |
| **Likely Benign** | -1 to -6 |
| **Benign** | ≤ -7 |

**Note (from PMID: 32720330):** Operationally, the prior probability should be understood to be infinitesimally greater than 0.10. This makes the posterior probability of the ACMG likely pathogenic combining rules infinitesimally greater than 0.90, so that the likely pathogenic rules work properly, and it enforces a requirement for some evidence of benign effect for sequence variants to be classified as likely benign.

---

## 6. Appendices

### Appendix A: Summary of Criterion Strengths and Default Point Values

| Criterion | Applicable Strengths (default points) |
|-----------|----------------------------------------|
| PVS1 | Very Strong (8), Strong (4), Moderate (2) |
| PS1 | Strong (4), Moderate (2), Supporting (1) |
| PS2 | Very Strong (8), Strong (4), Moderate (2), Supporting (1) |
| PS3 | Strong (4), Moderate (2), Supporting (1) |
| PS4 | Strong (4), Moderate (2), Supporting (1) |
| PM1 | Not Applicable |
| PM2 | Supporting (1) |
| PM3 | Not Applicable |
| PM4 | Moderate (2) |
| PM5 | Moderate (2), Supporting (1) |
| PM6 | Not Applicable (use PS2) |
| PP1 | Strong (4), Moderate (2), Supporting (1) |
| PP2 | Not Applicable |
| PP3 | Supporting (1) |
| PP4 | Moderate (2), Supporting (1) |
| PP5 | Not Applicable |
| BA1 | Stand Alone |
| BS1 | Strong (-4) |
| BS2 | Not Applicable |
| BS3 | Strong (-4), Moderate (-2), Supporting (-1) |
| BS4 | Strong (-4), Supporting (-1) |
| BP1 | Not Applicable |
| BP2 | Not Applicable |
| BP3 | Not Applicable |
| BP4 | Supporting (-1) |
| BP5 | Supporting (-1) |
| BP6 | Not Applicable |
| BP7 | Strong (RNA) (-4), Supporting (-1) |

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold (gnomAD v4.1.0) | Strength |
|-----------|---------------------------|----------|
| **BA1** | GrpMax filtering allele frequency ≥0.00316 | Stand Alone |
| **BS1** | GrpMax filtering allele frequency ≥0.000316 | Strong |
| **PM2** | Total allele frequency across all populations <0.00000132 | Supporting |

### Appendix C: Table 3 - PS4 / PP4 Phenotype Scoring Criteria

Phenotype points can only be awarded **once for each clinical criterion, clinical immunophenotype, or patient cell-based assay**, even if multiple examples of qualifying findings are present.

#### Clinical Criteria

| Phenotype Points | Clinical criteria | Examples of qualifying findings and phenotypes |
|---|---|---|
| **4 points** | Recurrent sinopulmonary infections and/or their sequelae | (A) Clinical history of recurrent sinopulmonary (upper and lower respiratory tract) infections such as sinusitis, otitis, pneumonia/pneumonitis, bronchitis, bronchiectasis, or abnormal pulmonary function test<br>(B) Imaging / pathology findings of bronchiectasis, mosaic attenuation, peribronchial inflammation, air-space opacities, bronchial wall thickening, volume loss, or atelectasis |
| **4 points** | Nonmalignant lymphoproliferation | (A) Hepatosplenomegaly<br>(B) Lymphadenopathy |
| **3 points** | Severe, persistent, recurrent, atypical, opportunistic viral infections | (A) Herpesviral infections<br>(B) Skin warts |
| **2 points** | Pre- (IUGR) or post-natal failure to thrive / short stature with Z-score <-2 | |
| **2 points** | Lymphoma | |
| **2 points** | Dysmorphic facial features | (A) Triangular face (B) Prominent forehead (C) Large low-set ears (D) Deep-set eyes (E) Hypoplastic or thin nostrils (F) Low-hanging columella (G) Micrognathia (H) Downturned mouth |
| **1 point** | Neurodevelopmental delay and neuropsychiatric disorders | |
| **1 point** | Non-infectious gastrointestinal or hepatobiliary disease | (A) Enteropathy (B) Hepatopathy (C) Autoimmune hepatitis (D) Inflammatory bowel disease (E) Primary sclerosing cholangitis (F) Enterocolitis (G) Celiac disease (H) Atrophic gastritis (I) Lymphocytic / microscopic colitis (J) Exocrine pancreatic insufficiency (K) Pernicious anemia |
| **1 point** | Other organ-/tissue-specific autoimmune/inflammatory disease not explicitly mentioned in other categories | (A) Endocrinopathies (e.g. Type I diabetes, autoimmune thyroiditis) (B) Vasculitis (C) Arthritis (D) Serositis (E) Glomerulonephritis (F) Inflammatory skin disease (e.g. erythema nodosum, dermatitis) (G) Inflammatory eye disease (e.g. uveitis) (H) Systemic lupus erythematosus-like features |
| **1 point** | Endocrinopathy | (A) Insulin resistance (B) Diabetes mellitus |
| **1 point** | Aged/progeroid appearance / wrinkled and thin skin / lipodystrophy or lipoatrophy | |
| **1 point** | Dental anomalies | (A) Delayed tooth eruption (B) Microdontia (C) Hypodontia (D) Enamel hypoplasia |
| **1 point** | Structural eye abnormalities | (A) Rieger anomaly (B) Posterior embryotoxon (C) Glaucoma (D) Ocular depression |
| **0.5 points** | Connective tissue abnormalities | (A) Inguinal hernias (B) Hyperextensible skin (C) Hyperflexible joints |
| **0.5 points** | Malignancy (nonlymphoma) | |

#### Clinical Immunophenotypic Data

| Phenotype Points | Clinical immunophenotypic data | Examples of qualifying findings and phenotypes |
|---|---|---|
| **2 points** | Increased proportion of early transitional T1/T2 B cells | Increased proportion of CD27low CD24bright CD38bright cells |
| **2 points** | Increased proportion of follicular helper T cells | |
| **1 point** | Decreased proportion of switched memory B cells | |
| **1 point** | Increased expression of senescent T markers | (A) Increased CD57+ (B) Increased KLRG1 (C) Lack of CD27/28 |
| **1 point** | Increased immature B cells | Increased CD10+ B cells |
| **1 point** | Histopath findings with lymphoid hyperplasia | Nodular lymphoid hyperplasia |
| **1 point** | Immune-mediated cytopenias | |
| **0.5 points** | Low IgG levels | |
| **0.5 points** | Elevated IgM levels | |
| **0.5 points** | Lymphopenia | |
| **0.5 points** | Abnormal TBNK levels | |
| **0.5 points** | Peripheral eosinophilia | |
| **0.5 points** | Serum IgE >500 kU/L | |

#### Patient Cell-Based Assay Data

| Phenotype Points | Patient cell-based assay data | Examples of qualifying findings |
|---|---|---|
| **2 points\*** | AKT assay with endogenous PIK3R1 | (A) Elevated ratios of phospho-AKT (Ser473) and/or phospho-AKT (Thr308) to total AKT\*\*<br>(B) Elevated phospho-S6 (Ser235/Ser236) and/or phospho-S6 (Ser240/Ser244) to total S6\*\* |

\*Avoid applying points from patient cell-based assay data to PP4, which already incorporates these data as rationale for an upgrade from PP4 to PP4_Moderate.

\*\*This is the expected finding for studies in patient T cells, whereas it is not yet clear how to interpret findings from non-immune cells like dermal fibroblasts, including decreased pAKT and/or decreased PIK3CD protein levels.

### Appendix D: PVS1 Decision Tree Summary

#### Nonsense or Frameshift Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| Predicted to undergo NMD (PTC between c.4 and c.1935) + exon present in all 3 biologically-relevant transcripts (NM_181523.3, NM_181504.4, NM_181524.2); PTC between c.917 and c.1890 | **PVS1** |
| Predicted to undergo NMD + exon present in all 3 biologically-relevant transcripts but variant close to NMD prediction boundary (between c.1891 and c.1935) | **PVS1_Strong** |
| Predicted to undergo NMD + exon present only in the MANE transcript NM_181523.3 (PTC between c.4 and c.916) | N/A |
| Exon absent from biologically-relevant transcript (NM_181523.3) | N/A |
| Not predicted to undergo NMD (PTC between codons 646 and 724) + truncated/altered region critical to protein function (disrupts the cSH2 domain between codons 646 and 718) | **PVS1_Strong** |
| Not predicted to undergo NMD + role of region unknown + LoF variants in this exon are frequent in the general population and/or exon absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD + role unknown + LoF variants not frequent in general population and exon present in biologically-relevant transcript(s) + variant removes >10% of protein | N/A |
| Not predicted to undergo NMD + role unknown + variant removes <10% of protein (truncation between codons 719 and 724) | **PVS1_Moderate** |

#### Deletions (Single Exon to Full Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Full gene deletion | **PVS1** |
| Disrupts reading frame + predicted NMD + exon present in all 3 biologically-relevant transcripts, including exon 8, 10, or 12, predicted to disrupt frame and trigger NMD | **PVS1** |
| Disrupts reading frame + predicted NMD + exon present only in the MANE transcript NM_181523.3 (including exon 6 or 7) | N/A |
| Exon absent from the MANE transcript (NM_181523.3) | N/A |
| Disrupts reading frame + NOT predicted to undergo NMD (including single exon 2 or 16 deletion) + truncated/altered region critical to protein function (including deletion of exon 16 encoding the cSH2 domain) | **PVS1_Strong** |
| Disrupts reading frame + NOT predicted NMD + relevance of region to autosomal dominant disease unknown (including single exon deletion of exon 1, 2, 3, 4, or 5, each present only in NM_181523.3) | N/A |
| Preserves reading frame (including single exon deletion of exon 1, 3, 4, 5, 9, 11, 13, 14, or 15) + truncated/altered region critical to protein function (including deletion of exon 9 or 11 encoding the nSH2 domain, exon 13 or 14 encoding the iSH2 domain, or exon 15 encoding the cSH2 domain) | **PVS1_Strong** |

#### Duplications (≥1 exon, completely contained within the gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Proven in tandem + reading frame disrupted and NMD predicted for all 3 biologically-relevant transcripts | **PVS1** |
| Proven in tandem + reading frame disrupted and NMD predicted for MANE transcript NM_181523.3 only | N/A |
| Proven in tandem + no or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem + reading frame presumed disrupted and NMD predicted for all 3 biologically-relevant transcripts | **PVS1_Strong** |
| Presumed in tandem + reading frame presumed disrupted and NMD predicted for NM_181523.3 transcript only | N/A |
| Proven not in tandem | N/A |

#### Initiation Codon Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| No known alternative start codon in other transcripts (not true for PIK3R1: the 3 isoforms differ at the N-term) | N/A |
| Different functional transcript uses alternative start codon (true for PIK3R1), with ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon (Met176) | N/A |
| Different functional transcript uses alternative start codon, with no pathogenic variant(s) upstream of closest potential in-frame start codon (Met176) | N/A |

#### PIK3R1 Exon Map: PVS1 Code Strength for Splicing Defect Leading to Predicted or Proven Exon Loss

| Exon | Strength if reading frame preserved | Strength if reading frame disrupted | Rationale |
|------|-------------------------------------|-------------------------------------|-----------|
| 1 | N/A (A) | N/A (A) | 5' UTR region - no splicing alteration predicted or use of a cryptic splice motif does not impact the coding region |
| 2 | N/A (B) | N/A (B) | Exon skipping or use of a cryptic splice motif eliminates the start codon and parts of the SH3 domain but alternative start codons are known |
| 3 | N/A (C) | N/A (C) | Preserves reading frame and disrupts only 1 out of 3 disease-relevant transcripts |
| 4 | N/A (C) | N/A (C) | Preserves reading frame and disrupts only 1 out of 3 disease-relevant transcripts |
| 5 | N/A (C) | N/A (C) | Preserves reading frame and disrupts only 1 out of 3 disease-relevant transcripts |
| 6 | N/A (D) | N/A (D) | Disrupts reading frame of 1 out of 3 disease-relevant transcripts |
| 7 | N/A (D) | N/A (D) | Disrupts reading frame of 1 out of 3 disease-relevant transcripts |
| 8 | — | **Very Strong** (E) | Disrupts reading frame of all 3 disease-relevant transcripts |
| 9 | **Strong** (F) | **Very Strong** (E) | (F) Preserves reading frame but disrupts the N-SH2 domain within all 3 disease-relevant transcripts |
| 10 | — | **Very Strong** (E) | Disrupts reading frame of all 3 disease-relevant transcripts |
| 11 | **Strong** (G) | **Very Strong** (E) | (G) Preserves reading frame but disrupts the Inter-SH2 domain within all 3 disease-relevant transcripts |
| 12 | — | **Very Strong** (E) | Disrupts reading frame of all 3 disease-relevant transcripts |
| 13 | **Strong** (G) | — | Preserves reading frame but disrupts the Inter-SH2 domain within all 3 disease-relevant transcripts |
| 14 | **Strong** (G) | — | Preserves reading frame but disrupts the Inter-SH2 domain within all 3 disease-relevant transcripts |
| 15 | **Strong** (H) | — | Preserves reading frame but disrupts the C-SH2 domain within all 3 disease-relevant transcripts |
| 16 | — | **Strong** (I) | Disrupts reading frame and the C-SH2 domain of all 3 disease-relevant transcripts |

#### Splicing Prediction Data Only (no RNA data)

| Location of variant | Code applied | Comparison variant situation | Result |
|---|---|---|---|
| Outside donor/acceptor ±1,2 dinucleotide positions | PP3 applied | No appropriate comparison P/LP variant in this splice region | PP3 |
| Outside donor/acceptor ±1,2 | PP3 applied | P variant at this nt position with same predicted impact | PP3 + PS1 |
| Outside donor/acceptor ±1,2 | PP3 applied | LP variant at this nt position with same predicted impact | PP3 + PS1_M |
| Outside donor/acceptor ±1,2 | PP3 applied | P variant within the same splice region with same predicted impact | PP3 + PS1_M |
| Outside donor/acceptor ±1,2 | PP3 applied | LP variant within the same splice region with same predicted impact | PP3 + PS1_Supp. |
| Outside donor/acceptor ±1,2 | Not applied (prediction inconclusive) | — | N/A (consider protein impact if relevant) |
| Outside donor/acceptor ±1,2 | BP4 applied | Silent / intronic | BP4 + BP7 |
| Outside donor/acceptor ±1,2 | BP4 applied | Other variant types / positions | BP4 (only if protein impact ruled out) |
| At donor/acceptor ±1,2 | PVS1 applied (predicted to skip exon 8, 10, or 12) | No appropriate comparison P/LP variant in this splice region | PVS1 |
| At donor/acceptor ±1,2 | PVS1 applied | P variant at this nt position or in same donor/acceptor ±1,2 dinucleotide with same predicted impact | PVS1 + PS1_Supp. |
| At donor/acceptor ±1,2 | PVS1 applied | P / LP variant within the same splice region but outside donor/acceptor ±1,2 dinucleotide, with same predicted impact | PVS1 + PS1_Supp. |
| At donor/acceptor ±1,2 | PVS1_Strong applied (predicted to skip exon 9, 11, 13, 14, 15, or 16) | No appropriate comparison P/LP variant within this splice region | PVS1_Strength |
| At donor/acceptor ±1,2 | PVS1_Strong applied | P variant at this nt position or in same donor/acceptor ±1,2 dinucleotide with same predicted impact | PVS1_Strength + PS1 |
| At donor/acceptor ±1,2 | PVS1_Strong applied | P variant within the same splice region, but outside donor/acceptor ±1,2 dinucleotide, with same predicted impact | PVS1_Strength + PS1_M |
| At donor/acceptor ±1,2 | PVS1_Strong applied | LP variant within the same splice region, but outside donor/acceptor ±1,2 dinucleotide, with same predicted impact | PVS1_Strength + PS1_Supp. |
| At donor/acceptor ±1,2 | PVS1 not applicable (predicted to skip exon 1, 2, 3, 4, 5, 6, or 7) | — | Not applied |

#### RNA / Splicing Data

| Situation | Result |
|---|---|
| No variant-specific observed impact + silent/intronic → BP7_S (RNA) applied | BP7_S (RNA) + prediction (PP3/BP4) |
| No variant-specific observed impact + other variant types/positions → protein impact can be ruled out (based on functional and/or clinical data) | BP7_S (RNA) + prediction (PP3/BP4) |
| No variant-specific observed impact + other variant types/positions → protein impact cannot be ruled out | Document as "BP7_S (RNA)" Not Met to indicate that data was present and reviewed |
| Variant-specific impact (compared to controls) + evidence of complete production of alternative transcript(s) from variant allele | Keep strength level; determine PVS1 (RNA) weight from combined analysis; PP3/BP4 and PS3 not applicable |
| Variant-specific impact + evidence of near-complete production of alternative transcript(s) from variant allele | Reduce strength by 1 level; determine PVS1 (RNA) weight from combined analysis; PP3/BP4 and PS3 not applicable |
| Variant-specific impact + evidence of incomplete production of alternative transcript(s) from variant allele | Reduce strength by 1 level; PVS1 (RNA) and BP7_S (RNA) not applicable, but PP3/BP4 and PS3 can be applied |

### Appendix E: Approved Functional Assay Summary

| Assay Class | PMIDs | Strengths Available |
|-------------|-------|---------------------|
| AKT kinase activity (exogenous PIK3R1) | 23810379, 25133428, 25488983, 28167755 | PS3_Supporting, BS3_Supporting |
| Lipid kinase activity | 28167755, 39835783 | PS3_Supporting, BS3_Supporting |
| PIK3CD protein binding | 25488983 | PS3_Supporting, BS3_Supporting |
| Conformational dynamics (HDX-MS) | 28167755 | PS3_Supporting, BS3_Supporting |
| Ratio of variant enrichment in pS6-high / pAKT-high vs. pS6-low / pAKT-low T cells (base-editing screen) | 40543502 | PS3 (Strong; OddsPath 26.0), BS3_Supporting (OddsPath 0.25) |
| Knock-in mouse model | 26974159, 28632845 | PS3 (Strong), BS3 (Strong) - reviewed case-by-case |
| mRNA splicing assays | 27221134, 25133428, 25488983 | **Not** approved for PS3_Supporting; used toward PVS1_Strong (RNA) |
| pAKT assay in patient cells with endogenous PIK3R1 | 25133428, 25488983, 39835783 | **Not** approved for PS3/BS3; considered part of PP4 |

### Appendix F: Key References

| Topic | PMID |
|-------|------|
| ACMG/AMP Variant Interpretation Guidelines (Richards et al., 2015) | 25741868 |
| Bayesian points scale for combining criteria (Tavtigian et al., 2018) | 29300386 |
| Point-based classification categories (Tavtigian et al., 2020) | 32720330 |
| ClinGen SVI PVS1 recommendations (Tayoun et al., 2018) | 30192042 |
| ClinGen SVI co-segregation recommendations (PP1) | 30311386 |
| ClinGen SVI recommendations against PP5/BP6 | 29543229 |
| SVI splicing recommendations / PS1 splice matrix (Walker et al., 2023) | 37352859 |
| OddsPath framework for functional evidence (Brnich et al., 2020) | 31892348 |
| PIK3R1 alternative start codons | 28802037 |
| PIK3R1 cSH2 domain / exon 16 | 38043374 |
| USIDNET cohort prevalence data | 34352450 |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | April 29, 2026 | Initial release. Changes between draft and final pilot specifications: **PP4** - revised scoring of clinical phenotypes and additional lab phenotypes, partly to better match the independently generated scoring system for the closely related gene *PIK3CD*. **PVS1** - revised to exclude PVS1 scoring for variants that do not impact all three disease-relevant transcripts, as these have been published in relation to an autosomal recessive condition not yet lumped with the present autosomal dominant condition. **PP3 / BP4** - updated *in silico* thresholds per reviewer recommendations to adopt the Pejaver et al. thresholds for REVEL and CADD; CADD thresholds made slightly more strict to tailor them for better performance in the PIK3R1 pilot. REVEL updated to >0.644 (PP3) and <0.290 (BP4); CADD updated to >26.0 (PP3) and <21.5 (BP4). **PM5** - added the caveat that the variant of interest must have a higher Grantham score than the Pathogenic comparison variant. |

---

*This document is based on the ClinGen Antibody Deficiencies Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for PIK3R1 Version 1.0 (https://cspec.genome.network/cspec/ui/svi/doc/GN160).*
