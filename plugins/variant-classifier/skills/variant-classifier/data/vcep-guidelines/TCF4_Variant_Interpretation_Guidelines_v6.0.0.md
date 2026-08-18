# Comprehensive Variant Interpretation Guidelines for TCF4

## ClinGen Rett and Angelman-like Disorders Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for TCF4 (Version 6.0)

**Affiliation:** Rett and Angelman-like Disorders VCEP
**Version:** 6.0
**Released:** 5/1/2026
**DOI:** 10.5281/zenodo.21421651
**Type:** Richards et al., 2015 - Combining rules
**Based on:** Richards et al., 2015 - ACMG/AMP Variant Interpretation Guidelines

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
   - [BP2 - In Trans / In Cis with Pathogenic](#bp2---in-trans--in-cis-with-pathogenic)
   - [BP3 - In-Frame Indels in Repetitive Region](#bp3---in-frame-indels-in-repetitive-region)
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
| **Gene** | TCF4 (HGNC:11634) |
| **HGNC Name** | transcription factor 4 |
| **Reference Transcript** | NM_001083962.1 |
| **Disease** | Pitt-Hopkins syndrome |
| **MONDO ID** | MONDO:0012589 |
| **Mode of Inheritance** | Autosomal dominant inheritance |
| **Rights Holder** | The Clinical Genome Resource (ClinGen) |

**Keywords:** human biology genomics variant, variant classification, clingen disease standards, TCF4, NM_001083962.1, Autosomal dominant inheritance, Pitt-Hopkins syndrome

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats (original ACMG):**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

#### VCEP Specifications

Refer to PVS1 flow chart for additional guidance.

For intragenic deletions/duplications that are predicted to result in a product that preserves the reading frame:

- For single exon in-frame deletions assign the same strength (PVS1) as for splice site variants that preserve reading frame indicated above.
- For multiple exon in-frame deletions PVS1 can be assigned to deletions that include single in-frame exons in the PVS1 category listed in the splice site section above OR if the exon contains a functionally important domain as specified in PM1.
- Given the extensive data available for TCF4, classifications for single or multi-exon in-frame deletions are assigned as PVS1 or PVS1_strong. Refer to PVS1 flow chart for additional guidance.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | Null variant in a gene where loss of function is a known mechanism of disease. Use as defined by ClinGen SVI working group (PMID:30192042). PVS1 can be applied for: (1) Null variants up to p.E643, which corresponds to the distal most de novo truncating variant in an affected patient reported to date; (2) Any frameshift variant that results in a read-through of the stop codon; (3) Canonical splice site variants predicted to result in an out-of-frame product; (4) Canonical splice site variants or single in-frame deletions predicted to preserve the reading frame (exon 15); (5) In-frame deletions including the PM1 functional domains (p.E564_V617 (bHLH)); (6) Deletions and duplications ≥1 exon in size (that are completely contained within the *TCF4* gene) where the reading frame is disrupted and NMD is predicted to occur; (7) Exon skipping or single exon deletion of exon 19 predicted to disrupt the reading frame but is not predicted to undergo NMD; (8) A full gene deletion. *(Modification type: Disease-specific)* |
| **Strong (PVS1_Strong)** | PVS1_Strong is applicable for single to multi exon deletions that preserve the reading frame and the variant removes <10% of the protein. *(Modification type: Disease-specific)* |
| **Moderate (PVS1_Moderate)** | PVS1_Moderate is applicable for any truncating variant distal of p.E643 and for single exon deletions that involve just non-coding exon 20. *(Modification type: Disease-specific)* |
| **Supporting (PVS1_Supporting)** | PVS1_Supporting is applicable for initiation codon variants in *TCF4*. *(Modification type: Disease-specific)* |

See [Appendix A: PVS1 Flowchart](#appendix-a-pvs1-flowchart-tcf4-nm_0010839621) for the full decision tree.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
**Example:** Val->Leu caused by either G>C or G>T in the same codon.
**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **Strong (PS1)** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. *(Modification type: None)* |
| **Moderate** | Not specified by VCEP |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### VCEP Specifications

- Applicable to all genes in affected individuals identified as mosaic for the variant (as the presence of a variant in the mosaic state is confirmatory of the variant being de novo).
- Because of the very high de novo rate of pathogenic variants in TCF4, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PS2_Very Strong)** | De novo (maternity and paternity confirmed) in a patient with the disease and no family history. ≥2 independent occurrences of PS2. OR ≥2 independent occurrences of PM6 and one occurrence of PS2. Evidence from literature must be fully evaluated to support independent events. *(Modification type: Strength)* |
| **Strong (PS2)** | De novo (maternity and paternity confirmed) in a patient with the disease and no family history. *(Modification type: None)* |
| **Moderate** | Not specified by VCEP (see PM6) |
| **Supporting** | Not specified by VCEP |

**Note:** The v6.0 specification does not provide a full SVI-style phenotypic-consistency point grid for PS2/PM6; only the point attribution described above (2 points confirmed de novo / 1 point assumed de novo) and the occurrence-count strength rules are given.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **Strong (PS3)** | Well-established in vitro or in vivo functional studies supportive of a damaging effect. RNA studies that demonstrate abnormal splicing and an out-offrame transcript. Do not use for canonical splice site variants and when PVS1 is used. *(Modification type: Disease-specific)* |
| **Moderate** | Not specified by VCEP |
| **Supporting (PS3_Supporting)** | Well-established in vitro or in vivo functional studies supportive of a damaging effect. RNA studies that demonstrate abnormal splicing and an inframe product (unless it affects an in-frame exon specified in the PVS1 section). See included table for acceptable functional studies. *(Modification type: Disease-specific)* |

> **Source typo preserved:** the PS3 Strong bullet reads "out-offrame transcript" in the source specification (rendered without the hyphen in "out-of-frame").

#### Approved Assay Instances (TCF4 Functional Assays supplementary table)

| Name of assay | Measured Parameter | Expected Deleterious Result Range (PS3_Supporting) | Expected Benign Result Range (BS3) | References |
|---------------|--------------------|----------------------------------------------------|-------------------------------------|------------|
| Subcellular localization assay | Subcellular distribution | Localization different compared to wild type TCF4 (e.g. accumulated in nuclear dots, no nuclear accumulation) | Not recommended | PMID: 22460224, 22777675 |
| Homogenous time-resolved fluorescence assay for measurement of protein-protein interaction | Homodimer formation (with itself) and heterodimer formation (with other bHLH transcription factors) | Localization different compared to wild type TCF4 (e.g. accumulated in nuclear dots, no nuclear accumulation) | Not recommended | PMID: 22777675 |
| Luciferase assay for measurement of transcriptional activity | Transcriptional activation of E-box containing promoter reporter constructs | p-value <0.05 compared to wild type luciferase activity | Not recommended | PMID: 17436255, 19235238, 22460224, 22777675 |
| Electrophoretic mobility shift assay (EMSA) | DNA binding activity of homo- and heterodimers | Comparison to wild type possible however no robust threshold available | Not recommended | PMID: 22460224 |
| Western blot | Protein expression and stability | Comparison to wild type possible however no robust threshold available | Not recommended | PMID: 22460224 |
| Co-fractionation | Localization to the chromatin | p-value < 0.05 compared to wild type TCF4. Localization to the soluble fraction | Not recommended | PMID: 22460224 |

> **Apparent source error flagged:** the "Expected Deleterious Result Range" entry for the homogenous time-resolved fluorescence (protein-protein interaction) assay duplicates the subcellular localization wording ("Localization different compared to wild type TCF4...") rather than describing a dimerization readout. Reproduced verbatim.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

#### VCEP Specifications

- Detailed phenotype not needed. Need to confirm patient is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.
- Patient can be published OR an internal case OR observed at an outside lab (i.e. via ClinVar). However, the independent case has to be confirmed to be a different patient than yours (compare gender/age).
- Do not use this criterion for variants where BS1 is applied or where PM2 does not apply.

| Strength | Criteria |
|----------|----------|
| **Strong (PS4)** | 5+ observations. *(Modification type: Strength)* |
| **Moderate (PS4_Moderate)** | 3-4 observations. *(Modification type: Strength)* |
| **Supporting (PS4_Supporting)** | Use for 2nd independent occurrence. *(Modification type: Strength)* |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **Moderate (PM1)** | Located in a mutational hot spot and/or critical and well-established functional domain. Basic Helix-Loop-Helix domain (bHLH): aa 564-617 (References 3, 2) *(Modification type: Disease-specific)* |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
**Caveat:** Population data for indels may be poorly called by next generation sequencing.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **Supporting (PM2_Supporting)** | Absent/rare from controls in an ethnically-matched cohort population sample. Use if absent, zero observations in control databases. *(Modification type: Strength)* |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.
**Note:** This requires testing of parents (or offspring) to determine phase.

**Status:** **Not Applicable.** Comment: Not applicable for TCF4.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **Moderate (PM4)** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. *(Modification type: None)* |
| **Supporting (PM4_Supporting)** | Smaller in-frame events (< 3 amino acid residues) unless they occur in a functionally important region (see PM1 for functionally important domains for each gene). *(Modification type: Strength)* |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
**Example:** Arg156His is pathogenic; now you observe Arg156Cys.
**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **Strong (PM5_Strong)** | Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. ≥2 different missense changes affecting the amino acid residue. Do not apply PM1 in these situations. *(Modification type: Strength)* |
| **Moderate (PM5)** | Missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. A Grantham or BLOSUM score comparison can be used to determine if the variant is predicted to be as or more damaging than the established pathogenic variant. *(Modification type: None)* |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

#### VCEP Specifications

- Evidence from literature must be fully evaluated to support independent events.
- Because of the very high de novo rate of pathogenic variants in *TCF4*, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

| Strength | Criteria |
|----------|----------|
| **Very Strong (PM6_Very Strong)** | Confirmed de novo without confirmation of paternity and maternity. ≥4 independent occurrences of PM6. *(Modification type: Strength)* |
| **Strong (PM6_Strong)** | Confirmed de novo without confirmation of paternity and maternity. ≥2 independent occurrences of PM6. *(Modification type: Strength)* |
| **Moderate (PM6)** | Confirmed de novo without confirmation of paternity and maternity. *(Modification type: No change)* |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
**Note:** May be used as stronger evidence with increasing segregation data.

#### VCEP Specifications

Note: individuals must have disease consistent with reported phenotype (even if on the mild end of spectrum of the disease).

| Strength | Criteria |
|----------|----------|
| **Strong (PP1_Strong)** | Co-segregation with disease in multiple affected family members. ≥5 informative meiosis *(Modification type: Strength)* |
| **Moderate (PP1_Moderate)** | Co-segregation with disease in multiple affected family members. 3-4 informative meiosis *(Modification type: Strength)* |
| **Supporting (PP1)** | Co-segregation with disease in multiple affected family members. 2 informative meiosis *(Modification type: Strength)* |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **Supporting (PP3)** | Multiple lines of computational evidence support a deleterious effect on the gene or gene product. For missense variants use REVEL with a score ≥ 0.644. For splice site variants use SpliceAI with a score ≥ 0.2. *(Modification type: Clarification)* |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **Supporting (PP4)** | Phenotype specific for disease with single genetic etiology. See gene specific clinical phenotype guidelines. *(Modification type: Disease-specific)* |

**Note:** No point-based PP4 scoring system is specified for TCF4. PP4 is applied at Supporting only, based on the clinical phenotype guidelines below.

#### TCF4 Clinical Phenotype Guidelines

**Core phenotype (need to be met for PP4):**
- Global developmental delay
- Intellectual disability
- Behavioral problems (anxiety)
- Hand flapping
- Characteristic Facial Features (become more apparent with age)
- Deeply set eyes with prominent supraorbital ridges
- Mildly up-slanted palpebral fissures
- Broad nasal root, wide nasal ridge, and wide nasal base with enlarged nostrils
- Overhanging or depressed nasal tip, which may be pointed
- Short philtrum
- Thick vermilion of the lower lip, which is often everted
- Widely spaced teeth

**Supportive criteria (do not need to be met for PP4, however in the absence of one core phenotype, two or more supportive phenotypes can be used in its place):**
- Prominence of the lower face with a well-developed chin, with age the lower face becomes more prominent and facial features may coarsen
- Mildly cupped ears with over folded helices
- In some individuals, wide mouth with downturned corners and exaggerated Cupid's bow or tented vermilion of the upper lip
- Happy, excitable, frequent smiling, laughter
- Episodic periodic breathing

**Additional notes:** If information is provided such that a phenotype of Pitt Hopkins syndrome is suspected, with specific minimal features used for the diagnosis, then this can be used for PP4 in lieu of the specific clinical features listed.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**Status:** **Not Applicable.** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**Status:** **Not Applicable.** Comment: Not applicable for TCF4.

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

#### VCEP Specifications

The frequency cutoffs are based on MECP2 expected disease allele frequency (1 in 10,000 for the disease prevalence / (1.5 alleles [assumes 50/50 male/female ratio] * 0.8 for 80% penetrance)). MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

| Strength | Criteria |
|----------|----------|
| **Stand Alone (BA1)** | Allele frequency above 0.05%. Use large population databases (i.e. gnomAD). Use if variant is present at ≥0.000083 (0.0083%) in any sub-population. Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles. *(Modification type: Disease-specific)* |

> **Internal inconsistency in source flagged:** the BA1 headline states "Allele frequency above 0.05%" while the operative bullet gives ≥0.000083 (0.0083%). Both reproduced verbatim; the bullet threshold (0.000083) is the actionable cutoff.

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### VCEP Specifications

The frequency cutoffs are based on MECP2 expected disease allele frequency divided by 10-fold. MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

| Strength | Criteria |
|----------|----------|
| **Strong (BS1)** | Allele frequency greater than expected for disease. Use large population databases (i.e. gnomAD). Use if variant is present at ≥0.0000083 (0.00083%) and <0.000083 (0.0083%) in any sub-population. Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles. *(Modification type: Disease-specific)* |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

#### VCEP Specifications

- Should be applied in cases where the healthy adult is devoid of neurodevelopmental phenotypes.
- Best to use with internal curated data that includes clinical information or published patients that have been phenotyped.

| Strength | Criteria |
|----------|----------|
| **Strong (BS2)** | Observed in the heterozygous/hemizygous state in a healthy adult. 2 unaffected (related or unrelated) heterozygotes *(Modification type: Strength)* |
| **Supporting (BS2_Supporting)** | Observed in the heterozygous/hemizygous state in a healthy adult. 1 unaffected (related or unrelated) heterozygote *(Modification type: Strength)* |

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **Strong (BS3)** | Well-established in vitro or in vivo functional studies shows no damaging effect on protein function. RNA functional studies that demonstrate no impact on splicing and transcript composition. It can be downgraded based on quality of data. Not applicable for other functional studies. *(Modification type: Disease-specific)* |

**Note:** In the TCF4 Functional Assays table, the Expected Benign Result Range for every listed protein-level assay is "Not recommended" — BS3 is therefore restricted to RNA functional studies.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.
**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

#### VCEP Specifications

Need to confirm that the family member is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.

| Strength | Criteria |
|----------|----------|
| **Strong (BS4)** | Lack of segregation in affected members of a family. Absent in a similarly affected family member, when seen in two or more families. Need to confirm that the family member is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum. *(Modification type: Strength)* |
| **Supporting (BS4_Supporting)** | Lack of segregation in affected members of a family. Absent in a similarly affected family member. *(Modification type: Strength)* |

---

### BP2 - In Trans / In Cis with Pathogenic

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

#### VCEP Specifications

Knock out of *TCF4* results in embryonic lethality/drastic phenotype. (Reference 4)

| Strength | Criteria |
|----------|----------|
| **Supporting (BP2)** | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder; or observed in cis with a pathogenic variant in any inheritance pattern. Applicable for *TCF4* for *in trans* state. *(Modification type: Disease-specific)* |

---

### BP3 - In-Frame Indels in Repetitive Region

**Original ACMG Summary:** In frame-deletions/insertions in a repetitive region without a known function.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **Supporting (BP3)** | In-frame deletions/insertions in a repetitive region without a known function. BP3 is applicable if there are in-frame deletions/duplications in a repetitive region where other in-frame deletions/duplications have been observed with an overall frequency commensurate with the BA1 threshold for this gene. *(Modification type: None)* |

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc).
**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

#### VCEP Specifications

| Strength | Criteria |
|----------|----------|
| **Supporting (BP4)** | Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc.). For missense variants use REVEL with a score ≤ 0.290. For splice site variants use SpliceAI with a score ≤ 0.1. *(Modification type: General recommendation)* |

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

#### VCEP Specifications

- For example if a variant in *TCF4* is identified in a patient with lissencephaly in whom a pathogenic variant is identified in the *PAFAH1B1* gene.
- Do not apply if variant is de novo.

| Strength | Criteria |
|----------|----------|
| **Strong (BP5_Strong)** | Variant found in a case with an alternate molecular basis for disease. ≥3 cases with alternate molecular basis for disease. *(Modification type: Strength)* |
| **Supporting (BP5)** | Variant found in a case with an alternate molecular basis for disease. 1 case with alternate molecular basis for disease. *(Modification type: Disease-specific)* |

---

### BP7 - Synonymous Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

#### VCEP Specifications

For silent variants BP4 and BP7 can be added.

| Strength | Criteria |
|----------|----------|
| **Supporting (BP7)** | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. Defined 'not highly conserved' regions in BP7 as those with PhastCons score <1 and/or PhyloP score <0.1 and/or the variant is the reference nucleotide in one primate and/or three mammal species. For splice site variants use SpliceAI with a score ≤ 0.1. *(Modification type: None)* |

---

## 4. Not Applicable Criteria

| Criterion | Original Purpose | Reason Not Applicable |
|-----------|-----------------|----------------------|
| **PM3** | In trans with pathogenic variant (recessive) | Not applicable for TCF4 |
| **PP2** | Missense in gene with low benign missense rate | Not applicable for TCF4 |
| **PP5** | Reputable source reports pathogenic | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |
| **BP1** | Missense in gene where truncating variants cause disease | Not applicable for TCF4 |
| **BP6** | Reputable source reports benign | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |

---

## 5. Rules for Combining Criteria

### Pathogenic Classification

| Combination | Applicable Codes |
|-------------|------------------|
| 1 Very Strong **AND** ≥1 Strong | Very Strong: PVS1, PS2_Very Strong, PM6_Very Strong / Strong: PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong |
| 1 Very Strong **AND** ≥2 Moderate | Very Strong: PVS1, PS2_Very Strong, PM6_Very Strong / Moderate: PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting | Supporting: PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4 |
| 1 Very Strong **AND** ≥2 Supporting | Supporting: PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4 |
| ≥2 Strong | PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong |
| 1 Strong **AND** ≥3 Moderate | — |
| 1 Strong **AND** 2 Moderate **AND** ≥2 Supporting | — |
| 1 Strong **AND** 1 Moderate **AND** ≥4 Supporting | — |

### Likely Pathogenic Classification

| Combination | Applicable Codes |
|-------------|------------------|
| 1 Very Strong **AND** 1 Moderate | Very Strong: PVS1, PS2_Very Strong, PM6_Very Strong / Moderate: PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate |
| 1 Strong **AND** 1 Moderate | Strong: PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong |
| 1 Strong **AND** ≥2 Supporting | Supporting: PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4 |
| ≥3 Moderate | PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate |
| 2 Moderate **AND** ≥2 Supporting | — |
| 1 Moderate **AND** ≥4 Supporting | — |

### Benign Classification

| Combination | Applicable Codes |
|-------------|------------------|
| ≥2 Strong | BS1, BS2, BS3, BS4, BP5_Strong |
| 1 Stand Alone | BA1 |
| 1 Strong **AND** 3 Supporting | Strong: BS1, BS2, BS3, BS4, BP5_Strong / Supporting: BS2_Supporting, BS4_Supporting, BP2, BP3, BP4, BP5, BP7 |

### Likely Benign Classification

| Combination | Applicable Codes |
|-------------|------------------|
| ≥2 Supporting | BS2_Supporting, BS4_Supporting, BP2, BP3, BP4, BP5, BP7 |
| 1 Strong | BS1, BS2, BS3, BS4, BP5_Strong |

---

## 6. Appendices

### Appendix A: PVS1 Flowchart (TCF4, NM_001083962.1)

#### Nonsense or Frameshift Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| Predicted to undergo NMD + Exon is present in biologically-relevant transcript(s) | **PVS1** |
| Predicted to undergo NMD + Exon is absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD + Upstream of most de novo distal LOF variant (p.E643); Frameshift that results in a read-through of the stop codon | **PVS1** |
| Not predicted to undergo NMD + Downstream of the most distal de novo LOF variant (p.E643) but does not result in a read-through of the stop codon | **PVS1_Moderate** |

#### GT-AG ±1,2 Splice Sites

| Condition | PVS1 Strength |
|-----------|---------------|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD + Exon is present in biologically-relevant transcript(s) | **PVS1** |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD + Exon is absent from biologically-relevant transcript(s) | N/A |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD (Exon 19) + Truncated/altered region is critical to protein function (Exon 19) | **PVS1** |
| Exon skipping or use of a cryptic splice site preserves reading frame (Exon 15) + Truncated/altered region is critical to protein function (Exon 15) | **PVS1** |

#### Deletions (Single Exon to Full Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Full gene deletion | **PVS1** |
| Single to multi exon deletion – Disrupts reading frame and is predicted to undergo NMD + Exon is present in biologically-relevant transcript(s) | **PVS1** |
| Single to multi exon deletion – Disrupts reading frame and is predicted to undergo NMD + Exon is absent from biologically-relevant transcript(s) | N/A |
| Single to multi exon deletion – Disrupts reading frame and is NOT predicted to undergo NMD (Exon 19) + Truncated/altered region is critical to protein function (Exon 19) | **PVS1** |
| Single to multi exon deletion – Preserves reading frame (Single exon 15 deletion; Other in-frame combinations) + Role of region in protein function is unknown + LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) + Variant removes >10% of protein | **PVS1** |
| Single to multi exon deletion – Preserves reading frame + Role of region unknown + LoF variants not frequent and exon present in biologically-relevant transcript(s) + Variant removes <10% of protein | **PVS1_Strong** |
| Single to multi exon deletion – Preserves reading frame + Truncated/altered region is critical to protein function (Exon 15 + any in-frame combination that includes the PM1 functional domain p.E564_V617 (bHLH)) | **PVS1** |
| Single exon deletion involving non-coding exon 20 | **PVS1_Moderate** |

#### Duplications (≥1 Exon in Size, Completely Contained Within Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Proven in tandem + Reading frame disrupted and NMD predicted to occur | **PVS1** |
| Proven in tandem + No or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem + Reading frame presumed disrupted and NMD predicted to occur | **PVS1_Strong** |
| Proven not in tandem | N/A |

#### Initiation Codon

| Condition | PVS1 Strength |
|-----------|---------------|
| No known alternative start codon in other medically relevant transcripts + No pathogenic variant(s) upstream of closest potential in-frame start codon | **PVS1_Supp** |

---

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | ≥0.000083 (0.0083%) in any sub-population | Stand Alone |
| BS1 | ≥0.0000083 (0.00083%) and <0.000083 (0.0083%) in any sub-population | Strong |
| PM2 | Absent; zero observations in control databases | Supporting |

Frequency criteria require the allele frequency to be met in any general continental population dataset of at least 2,000 observed alleles (BA1 and BS1).

---

### Appendix C: In Silico Thresholds Summary

| Criterion | Tool | Threshold |
|-----------|------|-----------|
| PP3 (missense) | REVEL | ≥ 0.644 |
| PP3 (splice site) | SpliceAI | ≥ 0.2 |
| BP4 (missense) | REVEL | ≤ 0.290 |
| BP4 (splice site) | SpliceAI | ≤ 0.1 |
| BP7 (splice site) | SpliceAI | ≤ 0.1 |
| BP7 (conservation) | PhastCons / PhyloP | PhastCons <1 and/or PhyloP <0.1 and/or reference nucleotide in one primate and/or three mammal species |

---

### Appendix D: References (from the specification)

| # | Citation | Journal / Year | PMID |
|---|----------|----------------|------|
| 1 | Whalen S, Héron D et al. Novel comprehensive diagnostic strategy in Pitt-Hopkins syndrome: clinical score and further delineation of the TCF4 mutational spectrum. | Hum Mutat (2012) 33(1) p. 64-72. 10.1002/humu.21639 | 22045651 |
| 2 | Amiel J, Rio M et al. Mutations in TCF4, encoding a class I basic helix-loop-helix transcription factor, are responsible for Pitt-Hopkins syndrome, a severe epileptic encephalopathy associated with autonomic dysfunction. | Am J Hum Genet (2007) 80(5) p. 988-93. 10.1086/515582 | 17436254 |
| 3 | Flora A, Garcia JJ et al. The E-protein Tcf4 interacts with Math1 to regulate differentiation of a specific subset of neuronal progenitors. | Proc Natl Acad Sci U S A (2007) 104(39) p. 15382-7. 10.1073/pnas.0707456104 | 17878293 |
| 4 | Mary L, Piton A et al. Disease-causing variants in TCF4 are a frequent cause of intellectual disability: lessons from large-scale sequencing approaches in diagnosis. | Eur J Hum Genet (2018) 26(7) p. 996-1006. 10.1038/s41431-018-0096-4 | 29695756 |
| 5 | Pejaver V, Byrne AB et al. Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria. | Am J Hum Genet (2022) 109(12) p. 2163-2177. 10.1016/j.ajhg.2022.10.013 | 36413997 |

Additional PMIDs cited in criteria text: 30192042 (ClinGen SVI PVS1 recommendations), 29543229 (ClinGen SVI VCEP Review Committee, PP5/BP6 not for use). Functional assay PMIDs: 17436255, 19235238, 22460224, 22777675.

---

### Appendix E: Supplementary Files in the Specification

| File | Description |
|------|-------------|
| Clinical Phenotype Guidelines for TCF4 | Phenotype guidelines for TCF4 mentioned in PP4 |
| PVS1 Flowchart for TCF4 | Gene-specific PVS1 decision tree |
| TCF4 Functional Assays | Acceptable functional assays for PS3/BS3 |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 6.0 | 5/1/2026 | 1 Strong AND 3 Supporting added to benign criteria code. 1 Strong added to likely benign criteria code. |

---

*This document was compiled from the ClinGen Rett and Angelman-like Disorders Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for TCF4 Version 6.0 (https://cspec.genome.network/cspec/ui/svi/doc/GN032). For the most current version, please refer to the ClinGen website.*
