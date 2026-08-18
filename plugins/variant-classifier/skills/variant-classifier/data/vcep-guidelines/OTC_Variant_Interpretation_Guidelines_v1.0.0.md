# Comprehensive Variant Interpretation Guidelines for OTC

## ClinGen Urea Cycle Disorders VCEP Specifications for OTC (Version 1.0)

**Affiliation:** Urea Cycle Disorders Variant Curation Expert Panel (UCD VCEP)
**Version:** 1.0
**Release Date:** February 27, 2026
**DOI:** 10.5281/zenodo.21434759
**Based on:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015 ACMG/AMP Variant Interpretation Guidelines

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
| **Gene** | OTC (HGNC:8512) |
| **HGNC Name** | ornithine transcarbamylase |
| **Reference Transcript** | NM_000531.6 |
| **Disease** | Ornithine carbamoyltransferase deficiency |
| **MONDO ID** | MONDO:0010703 |
| **Mode of Inheritance** | X-linked inheritance |

### General Comments

The UCD VCEP uses the Bayesian point system as described by Tavtigian, 2020 (PMID: 32720330). Each piece of evidence, pathogenic and benign, is converted to points; points are summed and the total determines the final classification (see [Rules for Combining Criteria](#5-rules-for-combining-criteria)).

| Evidence Strength | Pathogenic Points | Benign Points |
|-------------------|-------------------|---------------|
| Indeterminate | 0 | 0 |
| Supporting | 1 | -1 |
| Moderate | 2 | -2 |
| Strong | 4 | -4 |
| Very Strong | 8 | -8 |

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

#### VCEP Specifications

- **c.955 is the boundary for nonsense mediated decay (NMD).** Nonsense or frameshift variants including or upstream of c.955 are expected to undergo NMD and lead to loss of OTC.
- PVS1 is applicable to initiation codon variants and all canonical splice variants as suggested in Tayoun et al., 2018, as the c.1A>T sequence variant, resulting in p.M1L amino acid substitution, causes severe neonatal disease (PMID: 16786505).
- Removal of one or more exons that are spliced in-frame (exons 6, 7, 8, 9 and 10) will prevent folding of the protein lacking amino acids encoded by those exons (PMIDs: 19475717, 1627356, 23278509, 16786505).
- **PVS1 is applicable to frameshift and nonsense sequence variants upstream of c.1033 in OTC.**
  - The H11 alpha helix of OTC (encoded by amino acids 322-344) is critical for the correct folding of OTC protein (PMID: 9852088).
  - Several variants predicted to escape NMD, but which alter the H11 alpha helix, are reported in males with severe, early onset, neonatal OTC deficiency: p.S321* (PMID: 11793468), p.E328* (PMID: 16786505), p.W332* (PMIDs: 16786505, 8112735), p.Phe324Glnfs*16 (PMID: 35211578), demonstrating the critical nature of this region of OTC. Given this, the UCD VCEP sets the PVS1 boundary at the end of the H11 alpha helix at nucleotide c.1032.
  - **PVS1 is applicable for nonsense, frameshift, and splice variants affecting nucleotide c.1032 and upstream.**

#### PVS1_RNA

See the attached OTC VCEP PVS1 Decision Tree, adapted from Walker et al., 2023 (PMID: 37352859), for observed RNA splicing defects from functional splicing assays (minigene assay, RNA sequencing, transcriptome analysis, etc.) (PMID: 39418753).

#### Strength Levels

| Strength | Application | Default Points |
|----------|-------------|----------------|
| **PVS1** (Very Strong) | See the OTC VCEP PVS1 Decision Tree (summarized below) | 8 |
| **PVS1_Strong** | Applicable for nonsense, frameshift, and splice variants affecting nucleotide c.1033 and downstream. Several variants downstream of c.1032 leading to frameshift, stop-loss, and protein extension are reported in affected individuals in the literature, demonstrating the critical role of the C-terminal region of OTC for protein function (PMIDs: 9143919, 39256843, 23278509, 34014557, 34014569). See the OTC VCEP PVS1 Decision Tree | 4 |
| **PVS1_Moderate** | See the OTC VCEP PVS1 Decision Tree (PVS1_RNA branch only) | 2 |
| **PVS1_Supporting** | Not applicable — removed from the OTC specification (this strength is not used in the PVS1 flowchart) | — |

#### PVS1 Decision Tree Summary (OTC-specific)

##### Nonsense or Frameshift Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| Predicted to undergo NMD (upstream of and including c.955) + exon present in biologically-relevant transcript (NM_000531.6) | **PVS1** |
| Predicted to undergo NMD + exon absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD + truncated/altered region critical to protein function (c.956-1032) | **PVS1** |
| Not predicted to undergo NMD + truncated/altered region critical to protein function (amino acids 345-354; c.1033-1062) | **PVS1_Strong** |

##### Splice Site Variants (GT-AG ±1,2)

| Condition | PVS1 Strength |
|-----------|---------------|
| Exon skipping or cryptic splice site disrupts reading frame + predicted NMD + exon present in biologically-relevant transcript | **PVS1** |
| Exon skipping or cryptic splice site disrupts reading frame + predicted NMD + exon absent from biologically-relevant transcript | N/A |
| Disrupts reading frame + NOT predicted to undergo NMD (cryptic splice sites in exons 9 and 10) + truncated/altered region upstream of and including c.1032 critical to protein function (exons 9 and 10) | **PVS1** |
| Disrupts reading frame + NOT predicted to undergo NMD + truncated/altered region downstream of and including c.1033 (exon 10) | **PVS1_Strong** |
| Preserves reading frame (exons 6, 7, 8, 9, 10 are predicted to be spliced in-frame) + truncated/altered region critical to protein function (exons 6, 7, 8) | **PVS1** |
| Preserves reading frame + truncated/altered region critical to protein function (exons 9, 10) including nucleotides upstream of and including c.1032 | **PVS1** |
| Preserves reading frame + truncated/altered region critical to protein function (exon 10) including nucleotide c.1033 or downstream | **PVS1_Strong** |

##### Deletions (Single Exon to Full Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Full gene deletion | **PVS1** |
| Disrupts reading frame + predicted NMD + exon present in biologically-relevant transcript | **PVS1** |
| Disrupts reading frame + predicted NMD + exon absent from biologically-relevant transcript | N/A |
| Disrupts reading frame + NOT predicted to undergo NMD + truncated/altered region critical to protein function (exons 9, 10) including nucleotides upstream of and including c.1032 | **PVS1** |
| Disrupts reading frame + NOT predicted to undergo NMD + truncated/altered region critical to protein function (exon 10) including nucleotide c.1033 or downstream | **PVS1_Strong** |
| Preserves reading frame + truncated/altered region critical to protein function (exons 6, 7, 8) | **PVS1** |
| Preserves reading frame + truncated/altered region critical to protein function (exons 9, 10) including nucleotides upstream of and including c.1032 | **PVS1** |
| Preserves reading frame + truncated/altered region critical to protein function (exon 10) including nucleotide c.1033 or downstream | **PVS1_Strong** |

##### Duplications (≥1 Exon, Completely Contained Within Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Proven in tandem + reading frame disrupted + NMD predicted to occur | **PVS1** |
| Proven in tandem + no or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem + reading frame presumed disrupted + NMD predicted to occur | **PVS1** |
| Presumed in tandem + no or unknown impact on reading frame and NMD | N/A |
| Proven not in tandem | N/A |

##### Initiation Codon Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| No known alternative start codon in other transcripts + ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon (p.Met56) | **PVS1** |

##### PVS1_RNA (Observed Functional Splicing Data: Minigene, RNASeq, Transcriptome Analysis, etc.)

| Condition | PVS1 Strength |
|-----------|---------------|
| Proportion of affected transcripts complete or near complete + splicing defect leads to out-of-frame or PTC consequence resulting in NMD | **PVS1** |
| Proportion of affected transcripts complete or near complete + in-frame loss/alteration of amino acids including nucleotides upstream of and including c.1032 | **PVS1** |
| Proportion of affected transcripts complete or near complete + in-frame loss/alteration of amino acids including nucleotides c.1033 and downstream | **PVS1_Strong** |
| Proportion of affected transcripts incomplete + splicing defect leads to out-of-frame or PTC consequence resulting in NMD | **PVS1_Strong** |
| Proportion of affected transcripts incomplete + in-frame loss/alteration of amino acids including nucleotides upstream of and including c.1032 | **PVS1_Strong** |
| Proportion of affected transcripts incomplete + in-frame loss/alteration of amino acids including nucleotides c.1033 and downstream | **PVS1_Moderate** |
| No variant-specific splicing impact observed, or <20% of transcripts altered | N/A — use predictive codes (PP3, BP7) |

##### OTC Splicing Table (NM_000531.6)

For all variants involving either the +1 or +2 position of GT donor splice sites, the exon immediately 5' of the variant is predicted to be skipped; for all variants involving either the -1 or -2 position of AG acceptor splice sites, the exon immediately 3' of the variant is predicted to be skipped, unless indicated otherwise by RT-PCR or in silico prediction.

| Exon | First coding nt | Last coding nt | Exon length (nt) | Divisible by 3? | Consequence if skipped | PVS1 strength if exon skipped/deleted |
|------|-----------------|----------------|------------------|-----------------|------------------------|----------------------------------------|
| 1 | 1 | 77 | 77 | No | Out of frame | **PVS1** (exon 1 encodes the initiation methionine and 25 amino acids of the mitochondrial targeting sequence) |
| 2 | 78 | 216 | 139 | No | Out of frame | **PVS1** (frameshift, PTC, NMD) |
| 3 | 217 | 298 | 82 | No | Out of frame | **PVS1** (frameshift, PTC, NMD) |
| 4 | 299 | 386 | 88 | No | Out of frame | **PVS1** (frameshift, PTC, NMD) |
| 5 | 387 | 540 | 154 | No | Out of frame | **PVS1** (frameshift, PTC, NMD) |
| 6 | 541 | 663 | 123 | Yes | In frame | **PVS1** (encodes alpha-helices 6 and 6a and beta-sheets 6 and 7, essential for 3D structure) |
| 7 | 664 | 717 | 54 | Yes | In frame | **PVS1** (encodes alpha-helix 7, critical for 3D structure) |
| 8 | 718 | 867 | 150 | Yes | In frame | **PVS1** (contains the SMG motif, essential for ornithine binding) |
| 9 | 868 | 1005 | 138 | Yes | In frame | **PVS1** (contains the HCLP and ENR motifs essential for catalytic activity) |
| 10 | 1006 | 1062 | 57 | Yes | In frame | **PVS1** if prior to c.1033 (H11 alpha helix, c.964-1032, amino acids 322-344); **PVS1_Strong** if the variant affects c.1033 and downstream |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

To avoid applying evidence for variants that potentially impact splicing, the SpliceAI score must be checked for both the reported variant and the variant under review. **PS1 at any strength is only applicable if SpliceAI for both variants is ≤0.2.**

| Strength | Application | Default Points |
|----------|-------------|----------------|
| **PS1_Strong** | Applicable when the previously reported variant is classified as **Pathogenic** using these OTC specifications | 4 |
| **PS1_Moderate** | Applicable when the previously reported variant is classified as **Likely Pathogenic** using these OTC specifications | 2 |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

#### VCEP Specifications

- Individuals meeting **PP4_Moderate** criteria can be counted as "Phenotype highly specific for gene". Individuals meeting **PP4_Supporting** criteria can be counted as "Phenotype consistent with gene but not highly specific".
- **Confirmation of maternity only is sufficient to award full de novo points in male probands** given the X-linked inheritance pattern of OTC.
- A cumulative score should be calculated across all de novo or suspected de novo occurrences for the variant under review, including occurrences in the literature as well as individual clinical cases meeting the respective PP4 criteria.
- Adapted from the SVI recommended PS2/PM6 strength guidelines.

##### Points Awarded per Proband

| Phenotypic Consistency | De novo with maternity confirmed | Presumed de novo without confirmed maternity |
|------------------------|----------------------------------|----------------------------------------------|
| Phenotype highly specific for gene (PP4_Moderate met) | 2 | 1 |
| Phenotype consistent with gene but not highly specific (PP4_Supporting met) | 1 | 0.5 |

Sum de novo occurrences across all individuals and determine the PS2/PM6 strength level using the SVI recommended scoring system.

| Strength | Default Points |
|----------|----------------|
| **PS2_VeryStrong** | 8 |
| **PS2** (Strong) | 4 |
| **PS2_Moderate** | 2 |
| **PS2_Supporting** | 1 |

*Note: The OTC specification and its attached PS2/PM6 scoring document define only the two phenotypic-consistency rows above (points per proband) and direct curators to the SVI recommended scoring system for converting summed points to a strength level; explicit summed-point-to-strength cut-offs are not restated in the OTC-specific documents.*

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

#### VCEP Specifications

- **Yeast growth assays** in which the ARG3 open reading frame of a yeast strain is replaced with the OTC coding sequence, and site-directed mutagenesis is used to introduce the variant of interest (PMID: 37146589), can be used at **PS3_Moderate** or **PS3_Supporting** based on the % of growth compared to wildtype strains (see the attached Functional Assay spreadsheet).
- **PS3_Supporting** is also applicable as recommended by Brnich et al. (PMID: 31892348) for functional evidence from assays using non-patient-derived material. Enzyme activity must be measured in non-patient-derived cell lines, when site-directed mutagenesis has been used to introduce the variant of interest into a plasmid.
- **PS3 evidence is not applicable for assays performed in patient-derived cell lines or tissues.** PP4 evidence should be utilized for enzyme activity assays performed in patient-derived cells.
- Per Walker et al., 2023 (PMID: 37352859), evidence for observed impact on splicing as determined by splicing assays (RNASeq, minigene assay, etc.) should use PVS1 (RNA) evidence; therefore **PS3 is not applicable for these assays**.

| Strength | Application | Default Points |
|----------|-------------|----------------|
| **PS3** (Strong) | **Not applicable for OTC enzyme activity assays.** Use PS3_Moderate and PS3_Supporting below | 4 |
| **PS3_Moderate** | Yeast growth assays — applicable when growth of the ARG3 variant strain is **≤50%** compared to wildtype strains | 2 |
| **PS3_Supporting** | Yeast growth assays — applicable when growth of the ARG3 variant strain is **>50% and ≤65%** compared to wildtype strains. Enzyme activity in non-patient-derived cell lines — applicable if enzyme activity of the variant under review is **<20%** compared to wildtype | 1 |

#### Approved Functional Assays

| Assay | Reference | Description | Strengths Available |
|-------|-----------|-------------|---------------------|
| Yeast growth (complementation) assay | Lo et al., 2023; PMID: 37146589 | Growth of yeast cells in the absence of arginine as a proxy for human OTC function; human OTC coding sequence codon-optimized for *S. cerevisiae*, replacing ARG3 | PS3_Moderate, PS3_Supporting, BS3_Moderate, BS3_Supporting |
| Cell survival / expressed OTC activity assay | Kogo, 1998 (PMID: 9609999); Lee, 1989 (PMID: 2556444); Matsuura, 1994 (PMID: 8112735) | In vitro expression of OTC cDNA constructs in COS1/COS7 cell lines with site-directed mutagenesis; OTC activity measured colorimetrically; abnormal readout <20% wildtype | PS3_Supporting (BS3 not applied) |

#### Yeast Growth Assay Thresholds (PMID: 37146589)

| Relative Growth vs. Wildtype | Evidence |
|------------------------------|----------|
| 0 to ≤50% | **PS3_Moderate** |
| >50% to ≤65% | **PS3_Supporting** |
| >65% to <80% | **BS3_Supporting** |
| ≥80% | **BS3_Moderate** |

**Exception:** The yeast growth assay does not apply to variants in the SMG motif (amino acids 264-276), or to missense variants with potential splicing impact.

**Assay validation:** 71 P/LP variants with functional validation in mammalian systems and 7 B/LB variants (p.Lys46Arg, p.Gly50Ala, p.Thr150Ile, p.Thr150Asn, p.Leu166Phe, p.His255Arg, p.Gln270Arg) were used as validation controls.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

#### VCEP Specifications

- **To avoid double counting, an individual reported in the literature cannot be counted for both PP4 and PS4 evidence.** PS4 criteria can be applied for the occurrence of any individual for which PP4 criteria were met, but were NOT used as evidence.
- Pathogenic variants in OTC are often private mutations at conserved amino acid residues. However, several recurrent variants have been reported in large cohort studies (see Supplemental Table 1; PMID: 26059767).

| Strength | Application | Default Points |
|----------|-------------|----------------|
| **PS4_VeryStrong** | 8 additional male or female probands observed — must meet PP4 criteria and/or have documented hyperammonemia or metabolic decompensation under physiological stress to be counted | 8 |
| **PS4** (Strong) | 4 additional male or female probands observed — same requirement | 4 |
| **PS4_Moderate** | 2 additional male or female probands observed — same requirement | 2 |
| **PS4_Supporting** | One additional male or female proband observed — same requirement | 1 |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

#### VCEP Specifications

- Rationale from Shi et al. (PMIDs: 9852088, 10813810, 11237854), which identified important structural regions for proper enzyme function including substrate binding sites and active sites of the enzyme. Based on this and information from UniProt (P00480), the regions below are designated as important functional domains, and variants at these amino acids have been reported in affected individuals in the literature (Supp. Table 1, PMID: 26059767).
- **If PM1 and PP3 are utilized for the same variant, the total strength of PP3 + PM1 can be used at a maximum strength level of Strong (+4 points).**

| Strength | Application | Default Points |
|----------|-------------|----------------|
| **PM1_Moderate** | The variant affects one of the critical residues listed below | 2 |

##### Critical Residues within OTC

| Region | Amino Acids |
|--------|-------------|
| Carbamoylphosphate binding site | Ser-90, Thr-91, Arg-92, Thr-93, His-117, Arg-141, His-168, Gln-171, Leu-304, Arg-330 |
| Ornithine binding site | Leu-163, Asn-198, Asn-199, Asp-263, Ser-267, Met-268 |
| Catalytic site | His-302, Cys-303, Leu-304 |
| Conserved amino acids important for OTC structure and function | Arg-277 (affects Km for ornithine; PMIDs: 9175746, 9065786); Pro-305 (cis-proline stabilizing the HCLP motif; PMID: 9852088); Gly-269 (part of the mobile SMG loop; PMID: 8544185) |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes, or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

#### VCEP Specification

PM2 is used at a Supporting level of evidence per SVI guidance.

| Strength | Threshold | Default Points |
|----------|-----------|----------------|
| **PM2_Supporting** | Grpmax Filtering Allele Frequency **<0.000015 (0.0015%)** AND **≤1 homo- or hemizygote** in the most current version of gnomAD available at the time of curation | 1 |

**Rationale:** The most common pathogenic variant in population databases is p.Arg40Cys, which is associated with late-onset OTC deficiency (PMIDs: 23209112, 7860066, 11260212, others) and present in 17 heterozygotes and 6 hemizygotes in gnomAD v4.0.0 (Mino Allele frequency = 0.001586% in European populations). Other commonly reported pathogenic variants (p.Arg277Trp, p.Arg141Gln, p.Arg141Ter) are rare or absent in population databases, therefore a threshold of 0.0015% is set for PM2_Supporting.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### VCEP Specification

| Strength | Application | Default Points |
|----------|-------------|----------------|
| **PM4_Moderate** | Applicable as described for in-frame loss or gain of **≥1 amino acid but less than an entire exon**. For in-frame deletions or insertions ≥1 exon, defer to the PVS1 flowchart | 2 |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

To avoid applying evidence for variants that potentially impact splicing, the SpliceAI score must be checked for both the reported variant and the variant under review. PM5 is only applicable if SpliceAI for both variants is **≤0.2**.

| Strength | Application | Default Points |
|----------|-------------|----------------|
| **PM5_Moderate** | The variant under review occurs at the same amino acid as a variant classified **Pathogenic** using these OTC specifications | 2 |
| **PM5_Supporting** | The variant under review occurs at the same amino acid as a variant classified **Likely Pathogenic** using these OTC specifications | 1 |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

#### VCEP Specifications

Use the PS2/PM6 criteria described under [PS2](#ps2---de-novo-confirmed). Occurrences of de novo and presumed de novo are summed for a final PS2/PM6 evidence strength.

| Strength | Default Points |
|----------|----------------|
| **PM6_Strong** | 4 |
| **PM6** (Moderate) | 2 |
| **PM6_Supporting** | 1 |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

#### VCEP Specifications

- For segregation evidence, consider **unaffected, variant-negative males as informative**.
- To be counted as an "affected" relative, the variant-positive individual must minimally meet **PP4_Supporting** criteria or have documented hyperammonemia and/or metabolic decompensation under physiological stress.

| Strength | Application | Default Points |
|----------|-------------|----------------|
| **PP1_Strong** | ≥5 informative segregations | 4 |
| **PP1_Moderate** | 3-4 informative segregations | 2 |
| **PP1** (Supporting) | 2 informative segregations | 1 |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

#### VCEP Specifications

- **Missense variants:** the weight to apply for PP3 follows the specifications in Pejaver et al., 2022 (PMID: 36413997). The UCD VCEP uses the **REVEL** score for OTC variants.
- Per Walker et al. (PMID: 37352859), **PP3_Supporting** is applicable for splice region and intronic variants with a SpliceAI delta score **≥0.20**.
- For in-frame deletions and insertions, defer to PM4 criteria.
- **If PP3 and PM1 are utilized for the same variant, the total strength of PP3 + PM1 can be used at a maximum strength level of Strong (+4 points).**

| Strength | Threshold | Default Points |
|----------|-----------|----------------|
| **PP3_Strong** | Missense variants — REVEL score **≥0.932** | 4 |
| **PP3_Moderate** | Missense variants — REVEL score **≥0.773 and <0.932** | 2 |
| **PP3** (Supporting) | Missense variants — REVEL score **≥0.644 and <0.773**; Splice region and intronic variants — SpliceAI delta score **≥0.20** | 1 |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

#### VCEP Specifications

- Calculate proband phenotype points based on the OTC_PP4_Points table below and use the total points to award PP4 strength.
- **The same proband cannot be used for both PP4 and PS4 criteria.** In the event of multiple probands reported/present with the same variant under review, use the proband with the highest phenotype points for PP4 evidence, and the remaining proband(s) minimally meeting the PS4 required phenotype to score PS4.

##### Point Thresholds

| Total Proband Phenotype Points | PP4 Strength | Default Points |
|--------------------------------|--------------|----------------|
| ≥1.5 points | **PP4_Moderate** | 2 |
| >0.5 to <1.5 points | **PP4** (Supporting) | 1 |

##### Evidence Point Table (OTC PP4 Points)

| Type of Evaluation | Description | Points |
|--------------------|-------------|--------|
| Ammonia | Elevated ammonia / hyperammonemia with no additional information | 0.25 |
| Plasma amino acids / ammonia | Elevated glutamine AND normal citrulline **OR** elevated ammonia AND normal citrulline | 0.5 |
| Plasma amino acids / ammonia | Elevated glutamine AND low citrulline **OR** elevated ammonia AND low citrulline | 0.75 |
| Urine orotic acid | Elevated urine orotic acid and/or uracil | 1 |
| Enzyme activity in patient-derived cells* with normal enzyme activity in parallel control sample | Deficient (<20% wildtype) | 2 |

*Patient-derived cells can be from a male or female proband. Normal enzyme activity in female-derived cells should NOT be considered evidence against pathogenicity.

**Note on elevated ammonia:** Elevated ammonia is almost always observed in OTC deficiency but is highly heterogeneous with other primary and secondary causes. The 0.25-point value is not sufficient in isolation to award PP4 evidence or to upgrade PP4 from Supporting to Moderate, but ensures curators document that hyperammonemia was present. Absolute cut-offs for "elevated ammonia" are not specified; the VCEP defers to the reporting authors, clinicians, or laboratories using their internally validated age-specific reference values.

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes, or Exome Aggregation Consortium.

#### VCEP Specification

BA1 is equivalent to **-8 points** on the Bayesian scale.

| Strength | Threshold | Default Points |
|----------|-----------|----------------|
| **BA1** (Stand Alone) | Allele frequency above **0.010000 (1.0%)**, Grpmax Filtering Allele Frequency, **OR ≥10 (female) homozygotes or (male) hemizygotes** in the most current version of gnomAD available at the time of curation | -8 |

**Rationale:** The incidence of OTC deficiency is as high as 1:14,000 (0.007%), however other studies suggest a prevalence of 1:70,000 (PMID: 24006547). The most common pathogenic variant in population databases is p.Arg40Cys, associated with late-onset OTC deficiency (PMIDs: 23209112, 7860066, 11260212, others), present in 17 heterozygotes and 6 hemizygotes in gnomAD v4.0.0 (allele frequency = 0.001546%, PopMax frequency = 0.00436325% in European populations).

##### BA1 Exception List for OTC

Variants known to be associated with late-onset OTC deficiency may be present at a frequency higher than expected for a pathogenic variant in OTC, and with homozygotes and/or hemizygotes in population databases. Known variants for which the benign population codes (BA1, BS1, BS2) are **not applicable**:

- p.Arg40Cys
- p.Ala208Thr

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### VCEP Specification

| Strength | Threshold | Default Points |
|----------|-----------|----------------|
| **BS1** (Strong) | Allele frequency **>0.002000 (0.2%)**, Grpmax Filtering Allele Frequency, in the most current version of gnomAD available at the time of curation | -4 |

**Note:** BS1 and BS2 cannot both be applied if the same or overlapping dataset(s) are used to assess population data.

##### BS1 Exception List for OTC

- p.Arg40Cys
- p.Ala208Thr

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

#### VCEP Specification

| Strength | Application | Default Points |
|----------|-------------|----------------|
| **BS2** (Strong) | The variant is observed in **>5 (female) homozygotes or 5 (male) hemizygotes** in the most current version of gnomAD available at the time of curation | -4 |

**Note:** BS1 and BS2 cannot both be applied if the same or overlapping dataset(s) are used to assess population data.

##### BS2 Exception List for OTC

- p.Arg40Cys
- p.Ala208Thr

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

#### VCEP Specification

Yeast growth assays in which the ARG3 open reading frame of a yeast strain is replaced with the human OTC coding sequence, and site-directed mutagenesis is used to introduce the variant of interest (PMID: 37146589), can be used at BS3_Moderate or BS3_Supporting based on the % of growth compared to strains containing wildtype ARG3 (see the attached Functional Assay spreadsheet).

| Strength | Application | Default Points |
|----------|-------------|----------------|
| **BS3_Moderate** | Growth of the variant strain is **≥80%** compared to strains containing the wildtype OTC gene | -2 |
| **BS3_Supporting** | Growth of the variant strain is **>65% and <80%** compared to strains containing the wildtype OTC gene | -1 |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

#### VCEP Specifications

- Females with pathogenic OTC variants have highly variable phenotypes and may be asymptomatic with normal biochemical values, or be variably affected depending upon X-chromosome inactivation and other physiological and environmental factors. Given this, **absence of a phenotype or biochemical abnormality in a female carrier of the variant under review should not be counted towards benign evidence** (PMIDs: 9831349, 26059767).
- Late-onset OTC deficiency is documented and well known for specific variants in OTC; an unaffected male counted as benign evidence should have a reported age at, or above, that of other affected males in the same family.
- Known late-onset variants in OTC: **p.Arg40Cys, p.Lys88Asn, p.Ala208Thr, p.Glu273del, p.Leu301Phe**

| Strength | Application | Default Points |
|----------|-------------|----------------|
| **BS4_Supporting** | Presence of the variant under review in an unaffected male of a family if the age of the unaffected male is at or above the age of onset for other affected males in the family | -1 |

---

### BP2 - In Trans / In Cis with Pathogenic

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

#### VCEP Specification

| Strength | Application | Default Points |
|----------|-------------|----------------|
| **BP2** (Supporting) | Applicable in females for whom OTC deficiency is diagnosed and the variant under review is identified in trans or in cis with a known pathogenic variant, or if the variant under review is identified in cis in a male with OTC deficiency | -1 |

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

#### VCEP Specifications

- **Missense variants:** the weight to apply for BP4 follows the specifications in Pejaver et al., 2022 (PMID: 36413997). The UCD VCEP uses the **REVEL** score for OTC variants.
- Per Walker et al. (PMID: 37352859), **BP4_Supporting** is applicable for splice variants outside the donor/acceptor dinucleotides with no predicted impact on splicing by SpliceAI (delta score <0.1).
- Per Walker et al. (PMID: 37352859), **BP4_Supporting** is applicable for synonymous variants with SpliceAI <0.1 if the variant is outside the first nucleotide of an exon and the last three nucleotides of an exon.

| Strength | Threshold | Default Points |
|----------|-----------|----------------|
| **BP4_Strong** | Missense variants — REVEL score **≤0.016** | -4 |
| **BP4_Moderate** | Missense variants — REVEL score **>0.016 and ≤0.183** | -2 |
| **BP4** (Supporting) | Missense variants — REVEL score **>0.183 and ≤0.290**; splice region and intronic variants — SpliceAI delta score **<0.1**; synonymous variants — SpliceAI delta score **<0.1** if the variant is not within the first or last three nucleotides of an exon | -1 |

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

#### VCEP Specification

| Strength | Application | Default Points |
|----------|-------------|----------------|
| **BP5** (Supporting) | Applicable when the variant of interest is identified in a male with an alternative molecular etiology of elevated hyperammonemia, including biallelic pathogenic/likely pathogenic variants in autosomal recessive disease, or a pathogenic/likely pathogenic variant for autosomal dominant or X-linked disease | -1 |

---

### BP7 - Synonymous/Intronic Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

#### VCEP Specifications

- Applicable as described in Walker et al., 2023 (PMID: 37352859) for splicing or intronic variants with experimental evidence (RNASeq, minigene assay, etc.) demonstrating no effect on splicing.
- For synonymous variants, **BP4_Supporting must be met for BP7_Supporting to be applicable**.

| Strength | Application | Default Points |
|----------|-------------|----------------|
| **BP7_Strong** (BP7_strong (RNA)) | Applicable for potential splicing or intronic variants with experimental evidence demonstrating no splicing effect of the variant under review | -4 |
| **BP7** (Supporting) | Splicing/intronic variant — applicable for intronic variants with SpliceAI <0.10 if the variant under review is outside the splice region +7/-21 nucleotides. Synonymous variants — applicable when BP4_Supporting is met and only if the synonymous variant is outside the first base of an exon and the last 3 bases of an exon | -1 |

---

## 4. Not Applicable Criteria

| Criterion | Original Purpose | Reason Not Applicable |
|-----------|-----------------|----------------------|
| **PM3** | In trans with pathogenic variant (recessive) | Not applicable, as OTC is an X-linked gene and biallelic females are sufficiently rare |
| **PP2** | Missense in constrained gene | Not applicable; gnomAD (05/2021) expected missense 131.9, observed missense 89, for Z = 1.33 (o/e = 0.67) |
| **PP5** | Reputable source reports pathogenic | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |
| **BP1** | Missense in truncating disease gene | Not applicable; pathogenic missense variants have been documented for OTC deficiency |
| **BP3** | In-frame deletion/insertion in repetitive region | Not applicable; OTC does not contain repetitive regions without known function |
| **BP6** | Reputable source reports benign | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |

---

## 5. Rules for Combining Criteria

Variant classification follows the point system as outlined by Tavtigian, 2020 (PMID: 32720330). Points for each piece of evidence, both pathogenic and benign, are summed. The resulting total defines the classification of the variant according to the following point ranges:

| Category | Point Range |
|----------|-------------|
| **Pathogenic** | ≥10 |
| **Likely Pathogenic** | 6 to 9 |
| **Uncertain Significance** | 0 to 5 |
| **Likely Benign** | -1 to -6 |
| **Benign** | ≤-7 |

### Evidence Strength to Points Conversion

| Evidence Strength | Pathogenic | Benign |
|-------------------|------------|--------|
| Indeterminate | 0 | 0 |
| Supporting | 1 | -1 |
| Moderate | 2 | -2 |
| Strong | 4 | -4 |
| Very Strong | 8 | -8 |

### Combination Caps and Interactions

- **PM1 + PP3:** If PM1 and PP3 are utilized for the same variant, the total strength of PP3 + PM1 can be used at a maximum strength level of Strong (+4 points).
- **PP4 vs. PS4:** The same proband cannot be counted for both PP4 and PS4.
- **BS1 vs. BS2:** BS1 and BS2 cannot both be applied if the same or overlapping dataset(s) are used to assess population data.
- **BP4 → BP7:** For synonymous variants, BP4_Supporting must be met for BP7_Supporting to be applicable.
- **PS3 vs. PVS1_RNA:** Splicing assay evidence is scored under PVS1 (RNA), not PS3.
- **PS3 vs. PP4:** Enzyme activity assays performed in patient-derived cells are scored under PP4, not PS3.

---

## 6. Appendices

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold (Grpmax Filtering Allele Frequency, gnomAD) | Additional Requirement | Strength |
|-----------|------------------------------------------------------|------------------------|----------|
| **BA1** | >0.010000 (1.0%) | OR ≥10 (female) homozygotes or (male) hemizygotes | Stand Alone (-8) |
| **BS1** | >0.002000 (0.2%) | — | Strong (-4) |
| **BS2** | — | >5 (female) homozygotes or 5 (male) hemizygotes | Strong (-4) |
| **PM2** | <0.000015 (0.0015%) | AND ≤1 homo- or hemizygote | Supporting (+1) |

**Exception list (BA1/BS1/BS2 not applicable):** p.Arg40Cys, p.Ala208Thr

### Appendix B: In Silico Thresholds Summary

| Criterion | Variant Type | Threshold |
|-----------|--------------|-----------|
| PP3_Strong | Missense | REVEL ≥0.932 |
| PP3_Moderate | Missense | REVEL ≥0.773 and <0.932 |
| PP3_Supporting | Missense | REVEL ≥0.644 and <0.773 |
| PP3_Supporting | Splice region / intronic | SpliceAI delta score ≥0.20 |
| BP4_Strong | Missense | REVEL ≤0.016 |
| BP4_Moderate | Missense | REVEL >0.016 and ≤0.183 |
| BP4_Supporting | Missense | REVEL >0.183 and ≤0.290 |
| BP4_Supporting | Splice region / intronic / synonymous | SpliceAI delta score <0.1 |
| BP7_Supporting | Intronic | SpliceAI <0.10 and outside splice region +7/-21 |
| PS1 / PM5 gating | Any | SpliceAI ≤0.2 for both the reported variant and the variant under review |

*Note: The supplementary "UCD VCEP BP4 table OTC" document (dated 10/2023) additionally lists a BP4_Very Strong tier at REVEL ≤0.003 with BP4_Strong at ≤0.016 and >0.003. The released CSpec v1.0 specification does not include a BP4_Very Strong tier and defines BP4_Strong as REVEL ≤0.016; the CSpec values are used above.*

### Appendix C: Key References

| Citation | PMID | Topic |
|----------|------|-------|
| Richards et al., 2015 | 25741868 | ACMG/AMP Variant Interpretation Guidelines |
| Tavtigian et al., 2020 | 32720330 | Bayesian point system used for OTC classification |
| Abou Tayoun et al., 2018 | 30192042 | ClinGen SVI PVS1 recommendations |
| Walker et al., 2023 | 37352859 | RNA/splicing evidence (PVS1_RNA, PP3, BP4, BP7) |
| Pejaver et al., 2022 | 36413997 | Calibration of in silico predictors (REVEL thresholds) |
| Brnich et al., 2020 | 31892348 | Functional assay evidence framework |
| Lo et al., 2023 | 37146589 | OTC yeast growth (ARG3 complementation) assay |
| Shi et al. | 9852088, 10813810, 11237854 | OTC structural/functional domains (PM1) |
| Caldovic et al., 2015 | 26059767 | OTC variant spectrum (Supplemental Table 1) |
| Summar et al., 2013 | 24006547 | OTC deficiency prevalence |
| ClinGen SVI | 29543229 | PP5/BP6 not for use |
| ClinGen SVI PM2 recommendation | — | PM2 at Supporting strength |

### Appendix D: Supporting Documents in the Specification

| Document | Content |
|----------|---------|
| OTC PVS1 Decision Tree_110425 | Gene-specific PVS1 flowchart including PVS1_RNA |
| OTC splicing table_093025 | Predicted consequence and PVS1 strength per exon |
| OTC PS2.PM6 scoring_093025 | De novo points per proband |
| OTC PP4 points_093025 | Phenotype point table |
| OTC_Functional_Assay_120825 | Yeast growth assay and cell survival assay evaluation |
| Points System OTC | Bayesian points scale and classification ranges |
| UCD VCEP PP3 table OTC / UCD VCEP BP4 table OTC | REVEL thresholds |
| OTC Pilot data_110425 | Pilot variant classifications |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | February 27, 2026 | Initial release of the ClinGen Urea Cycle Disorders VCEP OTC specifications |

---

*This document is based on the ClinGen Urea Cycle Disorders Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for OTC Version 1.0 (CSpec GN156; DOI 10.5281/zenodo.21434759).*
