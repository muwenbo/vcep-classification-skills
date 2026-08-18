# Comprehensive Variant Interpretation Guidelines for SLC6A8

## ClinGen Cerebral Creatine Deficiency Syndromes VCEP Specifications for SLC6A8 (Version 2.1)

**Affiliation:** Cerebral Creatine Deficiency Syndromes VCEP (CCDS VCEP)
**Version:** 2.1
**Release Date:** 7/6/2026
**DOI:** 10.5281/zenodo.21421641
**Based on:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015 (ACMG/AMP)

**Specification Description (verbatim):** Cerebral Creatine Deficiency Syndromes Variant Curation Expert Panel ACMG Classification Rules Specified for Solute Carrier Family 6, Member 8 (SLC6A8; Creatine Transporter) Summary of ACMG-AMP Criteria for SLC6A8 Variants. General: variant curation for SLC6A8 uses the Bayesian point-based approach as described by Tavtigian, 2020 (PMID: 32720330). See "Bayesian points system" attachment and disregard "Rules for Combining Criteria" at the end of this document.

**Release Notes (v2.1):** Removed the attached document with the response to the SVI.

---

## Table of Contents

1. [Gene and Disease Information](#1-gene-and-disease-information)
2. [Pathogenic Criteria](#2-pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PS4 - Prevalence in Affected](#ps4---prevalence-in-affected)
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
   - [BP4 - Computational Evidence (Benign)](#bp4---computational-evidence-benign)
   - [BP5 - Alternate Molecular Basis](#bp5---alternate-molecular-basis)
   - [BP7 - Synonymous/Intronic Variants](#bp7---synonymousintronic-variants)
4. [Not Applicable Criteria](#4-not-applicable-criteria)
5. [Rules for Combining Criteria (Bayesian Points System)](#5-rules-for-combining-criteria-bayesian-points-system)
6. [Appendices](#6-appendices)

---

## 1. Gene and Disease Information

| Parameter | Value |
|-----------|-------|
| **Gene** | SLC6A8 (HGNC:11055) |
| **HGNC Name** | solute carrier family 6 member 8 |
| **Reference Transcript** | NM_005629.4 |
| **Disease** | creatine transporter deficiency |
| **MONDO ID** | MONDO:0010305 |
| **Mode of Inheritance** | X-linked inheritance |
| **Keywords** | human biology, genomics, variant, variant classification, clingen, disease, standards, SLC6A8, NM_005629.4, X-linked inheritance, creatine transporter deficiency |

**Note on point values:** Each criterion below lists the **Default Point Value** assigned by the VCEP. Points are summed across all evidence codes and the classification is determined on the Bayesian scale (see [Section 5](#5-rules-for-combining-criteria-bayesian-points-system)).

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats (from source):**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specification (identical text at all four strength levels):**
- See attached PVS1 decision tree, adapted from Tayoun, et.al. 2018 [PMID:30192042] for nonsense, frameshift, predictions for canonical splice variants, deletions, duplications and initiation codon variants.
- See attached PVS1 decision tree, adapted from Walker, et. al. 2023 [PMID:37352859] for observed RNA splicing defects from functional splicing assays (minigene assay, RNA Sequencing, transcriptome analysis, etc) [PMID: 39418753]

#### Strength Levels and Default Point Values

| Strength | Default Point Value | Modification Type |
|----------|--------------------|-------------------|
| **PVS1** (Very Strong) | 8 | Gene-specific |
| **PVS1_Strong** | 4 | Gene-specific |
| **PVS1_Moderate** | 2 | Gene-specific |
| **PVS1_Supporting** | 1 | Gene-specific |

#### SLC6A8-Specific PVS1 Decision Tree

SLC6A8-specific annotations are shown in the attached decision tree (`SLC6A8_PVS1_v2.1_033026`) in red.

##### Nonsense or Frameshift Variants

| Condition | PVS1 Strength |
|-----------|---------------|
| Predicted to undergo NMD (**variants at or before c.1716, NM_005629**) + Exon is present in biologically-relevant transcript(s) (NM_005629) | **PVS1** |
| Predicted to undergo NMD + Exon is absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD (**variants after c.1716, NM_005629**) + Truncated/altered region is critical to protein function (**n/a for SLC6A8**) | PVS1_Strong (shaded/not applicable for SLC6A8) |
| Not predicted to undergo NMD + Role of region unknown + LoF variants in this exon are frequent in the general population and/or exon absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD + Role of region unknown + LoF variants not frequent and exon present + Variant removes >10% of protein | **PVS1_Strong** |
| Not predicted to undergo NMD + Role of region unknown + LoF variants not frequent and exon present + Variant removes <10% of protein | **PVS1_Moderate** |

##### GT--AG ±1,2 Splice Sites (Predicted)

| Condition | PVS1 Strength |
|-----------|---------------|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD (**exons 1, 3, 4, 6, 7, 8, 10, 11**) + Exon present in biologically-relevant transcript(s) | **PVS1** |
| Same, but exon is absent from biologically-relevant transcript(s) | N/A |
| Exon skipping or use of a cryptic splice site preserves reading frame (**exons 2, 5, 9, 12, 13**) + Truncated/altered region is critical to protein function (**exons 2, 5**) | **PVS1_Strong** |
| Preserves reading frame + Role of region in protein function is unknown (**exons 9, 12, 13**) + LoF variants frequent in general population and/or exon absent from biologically-relevant transcript(s) | N/A |
| Preserves reading frame + Role unknown + LoF variants not frequent and exon present + Variant removes >10% of protein | **PVS1_Strong** |
| Preserves reading frame + Role unknown + LoF variants not frequent and exon present + Variant removes <10% of protein | **PVS1_Moderate** |

##### Deletions (Single Exon to Full Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Full gene deletion | **PVS1** |
| Single to multi exon deletion - disrupts reading frame and is predicted to undergo NMD + Exon present in biologically-relevant transcript(s) | **PVS1** |
| Same, but exon absent from biologically-relevant transcript(s) | N/A |
| Disrupts reading frame and NOT predicted to undergo NMD + Truncated/altered region is critical to protein function | **PVS1_Strong** |
| Disrupts reading frame, NOT predicted NMD (or preserves reading frame) + Role unknown + LoF variants frequent in general population and/or exon absent from biologically-relevant transcript(s) | N/A |
| Role unknown + LoF variants not frequent and exon present + Variant removes >10% of protein | **PVS1_Strong** |
| Role unknown + LoF variants not frequent and exon present + Variant removes <10% of protein | **PVS1_Moderate** |
| Single to multi exon deletion - preserves reading frame + Truncated/altered region is critical to protein function (**exons 1, 2, 5, 6**) | **PVS1_Strong** |

##### Duplications (≥1 Exon in Size, Must Be Completely Contained Within Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Proven in tandem + Reading frame disrupted and NMD predicted to occur | **PVS1** |
| Proven in tandem or presumed in tandem + No or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem + Reading frame presumed disrupted and NMD predicted to occur | **PVS1_Strong** |
| Proven not in tandem | N/A |

##### Initiation Codon Variants

Next in-frame methionine: **p.M59**

| Condition | PVS1 Strength |
|-----------|---------------|
| No known alternative start codon in other transcripts + ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon | **PVS1_Moderate** |
| No known alternative start codon in other transcripts + No pathogenic variant(s) upstream of closest potential in-frame start codon | **PVS1_Supp** |
| Different functional transcript uses alternative start codon | N/A |

##### RNA (Observed) - Functional Splicing Data (minigene, RNASeq, transcriptome analysis, etc.)

| Condition | PVS1 Strength |
|-----------|---------------|
| Proportion of affected transcripts complete or near complete (**≥70% transcripts with altered splicing**) + Splicing defect shown to lead to out-of-frame consequence leading to NMD | **PVS1** |
| ≥70% altered + Splicing defect leads to in-frame loss of region fully including p.Phe66-Leu81 OR p.Val305-Thr325* | **PVS1_Strong** |
| ≥70% altered + Splicing defect leads to in-frame loss of amino acids not including p.Phe66-Leu81 OR p.Val305-Thr325* | **PVS1_Supp** |
| Proportion of affected transcripts incomplete (**<70 or ≥40% transcripts with altered splicing**) + Splicing defect shown to lead to out-of-frame consequence leading to NMD | **PVS1_Strong** |
| <70 or ≥40% altered + Splicing defect leads to in-frame loss of region fully including p.Phe66-Leu81 OR p.Val305-Thr325 | **PVS1_Moderate** |
| <70 or ≥40% altered + Splicing defect leads to in-frame loss of amino acids not including p.Phe66-Leu81 OR p.Val305-Thr325 | n/a |
| No variant specific splicing impact observed, or <40% of transcripts altered | N/A, use predictive codes (PP3, BP7) |

\* Amino acids p.Phe66-Leu81 and p.Val305-Thr325 make the creatine binding interface of SLC6A8 and are necessary for creatine binding [PMID:37891751].

*Note: the range notation "<70 or ≥40%" is reproduced verbatim from the decision tree.*

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Default Point Value | Application |
|----------|--------------------|-------------|
| **PS1** (Strong) | 4 | PS1 is applicable as described. PS1 may also be applicable for intronic variants in the canonical splice consensus sequence or in the splice region. See "PS1_SpliceVariants" for applicable points, from Walker, et.al. PMID:37352859. Splice AI score must be <0.1 for both the variant under review and the previously reported variant to apply this code. |
| **PS1_Moderate** | 2 | PS1 is applicable as described. PS1_Moderate may also be applicable for intronic variants in the canonical splice consensus sequence or in the splice region. See "PS1_SpliceVariants" for applicable points. |
| **PS1_Supporting** | 1 | PS1 is applicable as described. PS1_Supp may also be applicable for intronic variants in the canonical splice consensus sequence or in the splice region. See "PS1_SpliceVariants" for applicable points. |

Modification type: General recommendation (all three strengths).

#### PS1 for Splice Variants (Attachment: "SLC6A8 PS1 Splice Variants")

Table below from Table 2 of Walker, et.al, 2023 [PMID:37352859].

**General comments:**
- Splice prediction from SpliceAI must match the predicted event of the reported Pathogenic / Likely Pathogenic variant, including:
  - Both variants predicted to lead to the same effect - ie, exon skipping of the same exon, enhanced use of a cryptic splice motif, intron retention with same predicted effect
  - The strength of the prediction for the variant under review must be of similar or higher strength than the previously reported variant

**Table 2. PS1 code weights for variants with same predicted splicing event as a known (likely) pathogenic variant**

| Variant under assessment (VUA) | Baseline computational/predictive code applicable to VUA | Position of comparison variant relative to VUA | PS1 code applicable to VUA with P comparison variant | with LP comparison variant |
|---|---|---|---|---|
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | same nucleotide | PS1 | PS1_Moderate |
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | within same splice donor/acceptor motif (including at ±1,2 positions) | PS1_Moderate | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | within same splice donor/acceptor ±1,2 dinucleotide | PS1_Supporting | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | within same splice donor/acceptor region, but outside ±1,2 dinucleotide<sup>a</sup> | PS1_Supporting | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | within same splice donor/acceptor ±1,2 dinucleotide | PS1 | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | within same splice donor/acceptor motif, but outside ±1,2 dinucleotide<sup>a</sup> | PS1_Moderate | PS1_Supporting |

*Footnote marker "a" appears in the source table; its footnote text is not reproduced in the attachment.*

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### VCEP Specifications

| Strength | Default Point Value | Application |
|----------|--------------------|-------------|
| **PS2** (Strong) | 4 | Is applicable in the case of a hemizygous male or a heterozygous female minimally meeting PP4_Supporting with a de novo variant:<br>• confirmation of maternity only is sufficient in male probands<br>• confirmation of both maternity and paternity is necessary in female probands |
| **PS2_Moderate** | 2 | Is applicable in the case of a newly hemizygous male with variant identified de novo in asymptomatic mother when one of the following conditions are met:<br>• Identified in male proband minimally meeting PP4_Supporting if the biological mother (asymptomatic or affected) has a de novo SLC6A8 variant confirmed by parental testing in her parents<br>• Identified in male proband minimally meeting PP4_Supporting if the biological mother (asymptomatic or affected) has a mosaic SLC6A8 (≤30% variant allele frequency) |

Modification type: Disease-specific,None (Strong); Disease-specific,Strength (Moderate).

**Note:** No PS2_VeryStrong or PS2_Supporting level is specified by this VCEP. No generic PS2/PM6 point-accrual table is specified by this VCEP.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:** Variants demonstrated by functional assays to alter splicing should not be scored under PS3 criteria. Please see PVS1 (above) and PVS1 decision tree (attached) to apply appropriate strength for variants with functional splicing data. Decision tree for variants with observed RNA splicing defects adapted from Walker, et.al 2023 [PMID:37352859].

| Strength | Default Point Value | Application |
|----------|--------------------|-------------|
| **PS3_Moderate** | 2 | Creatine transport deficient mouse models have biochemical findings including reduced/absent creatine in brain [PMID:21249153, 25485098, 33389772], which has been recapitulated in brain-specific creatine transport knockout models [PMID:22751104]. PS3_Moderate is applicable when the variant under review is used to generate a mouse knock-in model and assessment of brain creatine demonstrates significantly reduced or absent brain creatine when compared to wildtype littermates. |
| **PS3_Supporting** | 1 | Creatine transport assay using site directed mutagenesis to introduce the variant under review into *SLC6A8* deficient cell line, and results in <10% creatine transport compared to wildtype cells when using ≤125uM creatine, or ≤25% when using creatine >125uM. |

Modification type: Gene-specific (Moderate); Disease-specific,Strength (Supporting).

**Note:** PS3 at Strong or Very Strong is not specified by this VCEP.

#### Approved Functional Assays (Attachment: "SLC6A8 Functional Assay SVI documentation", sheet "Cell survival assay")

| PMID | DOI / link | Author | Year | Approved assay | Proposed strength |
|------|-----------|--------|------|----------------|-------------------|
| 22281021 | 10.1016/j.ymgme.2011.12.022 | Betsalel | 2012 | Y | PS3_Supporting (<10% using ≤125uM creatine, or ≤25% using >125uM), BS3_Supporting ≥50% |
| 17465020 | 10.1002/humu.20532 | Rosenberg | 2007 | y | PS3_Supporting (<10% using ≤125uM creatine, or ≤25% using >125uM), BS3_Supporting ≥50% |

**Assay details (verbatim, including source typos):**

| Attribute | Betsalel 2012 (PMID 22281021) | Rosenberg 2007 (PMID 17465020) |
|-----------|-------------------------------|--------------------------------|
| Assay (general description) | Site directed mutagenesis, plasmids transfected into SLC6A8 deficient fibroblasts in triplicate. Creatnine uptake capacity tested by incubation with 25uM creatine, cells harvested and intracellular creatine measued by stable isotop dilution GC-MS. | site directed mutagenesis to introduce variants into pCR2.1-SLC6A8 |
| Material used | Engineered variants, pEGFP-N1 vector, SLC6A8 deficient fibroblasts tranfected (in triplicate) with vector, wildtype, and empty vector | SLC6A8 deficient primary fibroblasts (hemizygous for p.Arg514X) |
| Readout type | Quantitative (creatine uptake), Qualitative (Western blot) | Quantitative |
| Readout description | Intracellular creatine content measured by stable isotope dilution GC-MS | Creatine uptake measured by SID-GCMS |
| Biological replicates | met | met |
| Technical replicates | met, triplicate | met |
| Basic positive control | met, WT DNA transfected for each line | met |
| Basic negative control | met; empty vector tranfected for each line | met |
| Validation controls P/LP (#) | 3 | 4 |
| Validation controls B/LB (#) | 3 | 0 |
| Statistical analysis | Results displated as percent creatine uptake compared to wildtype, standard error to triplicate transfection | Triplicate measurements of creatine uptake (pmol Cr/ug protein) |
| Threshold for normal readout | *(blank in source)* | *(blank in source)* |
| Threshold for abnormal readout | <10% wt activity | <10 pmol Cr/ug protein |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:**
- Note 1: Relative risk or OR, as obtained from case-control studies, is >5.0, and the confidence interval around the estimate of relative risk or OR does not include 1.0. See the article for detailed guidance.
- Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.
- Note 3: A single individual cannot be counted for both PP4 and PS4. Use the individual with the highest possible PP4 evidence under that code and use PS4 to count additional affected individuals.

| Strength | Default Point Value | Application |
|----------|--------------------|-------------|
| **PS4_VeryStrong** | 8 | • 8 independent probands with elevated urine creatine/creatinine ratio on one occasion at minimum, in addition to any proband used for PP4.<br>• Affected females may be counted if meeting PP4_Supporting<br>• Variant must meet PM2_Supporting criterion for PS4 to apply. |
| **PS4** (Strong) | 4 | • 4 independent probands with elevated urine creatine/creatinine ratio on one occasion at minimum, in addition to any proband used for PP4.<br>• Affected females may be counted if meeting PP4_Supporting<br>• Variant must meet PM2_Supporting criterion for PS4 to apply. |
| **PS4_Moderate** | 2 | • 2 independent probands with elevated urine creatine/creatinine ratio on one occasion at minimum, in addition to any proband used for PP4.<br>• Affected females may be counted if meeting PP4_Supporting<br>• Variant must meet PM2_Supporting criterion for PS4 to apply. |
| **PS4_Supporting** | 1 | • 1 independent proband with elevated urine creatine/creatinine ratio on one occasion at minimum, in addition to any proband used for PP4.<br>• Variant must meet PM2_Supporting criterion for PS4 to apply. |

Modification type: Gene-specific,Strength (Very Strong); Disease-specific (Strong); Strength (Moderate, Supporting).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:** PM2 at Moderate strength level is not applicable per SVI recommendations.

| Strength | Default Point Value | Threshold |
|----------|--------------------|-----------|
| **PM2_Supporting** | 1 | Applicable when Grpmax Filtering Allele Frequency is **≤0.00002 (0.002%)** AND **0 homo- or hemizygotes** are present in the most current version of gnomAD available at the time of curation |

Modification type: Disease-specific.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Default Point Value | Application |
|----------|--------------------|-------------|
| **PM4** (Moderate) | 2 | Protein length changes as a result of in-frame deletions/insertions in a non-repeat region or stop-loss variants. |

Modification type: None.

**Note:** PM4_Supporting is not specified by this VCEP.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

| Strength | Default Point Value | Application |
|----------|--------------------|-------------|
| **PM5** (Moderate) | 2 | • Same as described.<br>• Splice AI score must be <0.1 for both the variant under review and the previously reported variant to apply this code. |
| **PM5_Supporting** | 1 | Novel missense change at an amino acid residue where a different missense change determined to be Likely pathogenic has been seen before. Example: Arg156His is Likely pathogenic; now you observe Arg156Cys |

Modification type: Gene-specific (Moderate); Strength (Supporting).

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

| Strength | Default Point Value | Application |
|----------|--------------------|-------------|
| **PM6** (Moderate) | 2 | See criteria in PS2. |

Modification type: No change.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**
- Based on Biesecker, 2024 [PMID:38103548], the following strength levels are applicable for SLC6A8 - segregations include:
  - variant positive, phenotype positive males
  - variant negative, phenotype negative males
  - variant positive, phenotype positive females
  - variant positive asymptomatic females should NOT be counted
- Total locus evidence for PP1+PP4 must be capped at 5.0 points per allele

| Strength | Default Point Value | Segregations |
|----------|--------------------|--------------|
| **PP1_Strong** | 4 | 4 segregations |
| **PP1_Moderate** | 2 | 2 segregations |
| **PP1** (Supporting) | 1 | 1 segregations |

Modification type: Strength (Strong, Moderate); Disease-specific (Supporting).

**Note:** No LOD-score table is specified by this VCEP; segregation counts are used directly.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

| Strength | Default Point Value | Application |
|----------|--------------------|-------------|
| **PP3** (Supporting) | 1 | • Applicable for missense variants with **REVEL >0.75**<br>• Applicable for canonical splice, splice region, or deep intronic variants with **SpliceAI delta score ≥0.20** |

Modification type: General recommendation.

**Note:** No PP3_Moderate or PP3_Strong level is specified by this VCEP.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** See attached PP4 table for phenotypes in males and/or female probands required to meet PP4 criteria. Point total for applicable PP4 criteria should be summed.

#### PP4 Strength Thresholds

| Sum of PP4 Points | PP4 Strength | Default Point Value |
|-------------------|--------------|--------------------|
| 1-2 points | **PP4** (+1, Supporting) | 1 |
| 3 points | **PP4_Moderate** (+2) | 2 |
| 4 points | **PP4_Strong** (+4) | 4 |

Modification type: Disease-specific (Strong, Supporting); Strength (Moderate).

#### Requirements (all strengths)

- An individual used to assign PP4, at any weight, cannot be also included for PS4 count. If multiple unrelated probands with the variant have been identified, it is recommended that the case with the highest PP4 points is assigned the appropriate weight for PP4, and the other cases are used for PS4.
- Variant must meet PM2_Supporting for PP4 to apply at any strength.
- Total locus evidence for PP1+PP4 must be capped at 5.0 points per allele.

#### Additional Requirements for PP4_Strong

- Two or more data types are required to reach strong.
- For PP4 to be applied at strong, full *SLC6A8* gene sequencing, including all coding exons and intron/exon boundaries must have been carried out. If not, downgrade by one strength level.

#### PP4 Point Table - Males (`SLC6A8_v2_PP4 (males)`)

| Investigations | Description | Points |
|----------------|-------------|--------|
| Urine biochemical analytes | Elevated urine creatine/creatinine ratio on one occasion in the absence of creatine supplementation | 1 |
| Urine biochemical analytes | Elevated urine creatine/creatinine ratio on more than one occasion in the absence of creatine supplementation | 2 |
| Brain magnetic resonance spectroscopy (MRS) | Significantly decreased creatine peak\* | 3 |
| Creatine uptake studies | Deficient creatine uptake (<10% of normal controls) in patient cells when using ≤125uM creatine; Deficient creatine uptake (≤25% normal controls) in patient cells when using >125uM creatine^. | 3 |

\* With absent guanidinoacetate peak, if reported.
^ If multiple studies are performed for a specific variant with conflicting results, points should be scored based on a study using ≤125uM creatine

- Variant must meet PM2_Supporting for PP4 to apply at any strength.
- For PP4 to be applied at strong, full SLC6A8 gene sequencing, including all coding exons and intron/exon boundaries, must have been carried out. If not, downgrade to Moderate

#### PP4 Point Table - Females (`SLC6A8_v2_PP4 (females)`)

| Investigations | Description | Points |
|----------------|-------------|--------|
| Urine biochemical analytes | Elevated urine creatine/creatinine ratio on one occasion in the absence of creatine supplementation | 1 |
| Brain magnetic resonance spectroscopy (MRS) | Decreased creatine peak | 3 |
| Creatine uptake studies | Deficient creatine uptake (<10% of normal controls) in patient cells when using ≤125uM creatine; Deficient creatine uptake (≤25% normal controls) in patient cells when using >125uM creatine^. | 3 |
| Genetic testing modality | Variant identified by exome sequencing or genome sequencing and no other potentially causitive Pathogenic / Likely Pathogenic variants identified in different gene | 2 |

^ If multiple studies are performed for a specific variant with conflicting results, points should be scored based on a study using ≤125uM creatine

- Variant must meet PM2_Supporting for PP4 to apply at any strength.
- For PP4 to be applied at strong, full SLC6A8 gene sequencing, including all coding exons and intron/exon boundaries, must have been carried out. If not, downgrade to Moderate

*Source typo preserved: "causitive" (female table).*

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

| Strength | Default Point Value | Threshold |
|----------|--------------------|-----------|
| **BA1** (Stand Alone) | Not Applicable | Applicable when Grpmax Filtering Allele Frequency is **≥0.002 (0.2%)** OR **≥10 homo- or hemizygotes** (or the sum of total hemi- and homozygotes) are present in the most current version of gnomAD available at the time of curation. |

Modification type: Disease-specific.

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

| Strength | Default Point Value | Threshold |
|----------|--------------------|-----------|
| **BS1** (Strong) | -4 | Applicable when Grpmax Filtering Allele Frequency is **≥0.0002 (0.02%)** |

Modification type: Disease-specific.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

| Strength | Default Point Value | Application |
|----------|--------------------|-------------|
| **BS2** (Strong) | -4 | Applicable when the variant is observed in **≥2 homo- or hemizygotes** in the most current version of gnomAD available at the time of curation OR the variant is identified in a male with documented normal urine creatine/creatinine ratio<br>• BS1 and BS2 should not be co-applied based on the number of homo- or hemizygotes present in gnomAD |
| **BS2_Supporting** | -1 | Can be used if the variant is identified in a male with creatine transport studies **≥80%** compared to wildtype if **≤125uM creatine** was used in the study. |

Modification type: Gene-specific (both).

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** BS3 is not applicable at Strong strength level.

| Strength | Default Point Value | Application |
|----------|--------------------|-------------|
| **BS3_Supporting** | -1 | • Creatine transport assay demonstrating **≥50% normal transport activity** compared to controls when using **≤125uM creatine**. Any study using >125uM creatine for creatine transporter assays cannot be used as Benign evidence.<br>• RT-PCR evidence demonstrating no observable effect of splicing for canonical splice, splice region, and deep intronic variants<br>• Expression assay demonstrating wildtype transcript levels |

Modification type: Disease-specific,Strength.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

| Strength | Default Point Value | Application |
|----------|--------------------|-------------|
| **BS4** (Strong) | -4 | Asymptomatic, variant positive females should NOT be used as benign segregation evidence |

Modification type: None.

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

| Strength | Default Point Value | Application |
|----------|--------------------|-------------|
| **BP4** (Supporting) | -1 | • **REVEL score ≤ 0.20**<br>• For variants potentially impacting splicing, **Splice AI score <0.10** |

Modification type: General recommendation.

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

| Strength | Default Point Value | Application |
|----------|--------------------|-------------|
| **BP5** (Supporting) | -1 | Use as described. |

Modification type: None.

---

### BP7 - Synonymous/Intronic Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

| Strength | Default Point Value | Application |
|----------|--------------------|-------------|
| **BP7** (Supporting) | -1 | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site<br>• **SpliceAI score ≤0.10**<br>• May also be applied in conjunction with PB4 for an intronic variant outside the splice region (beyond -4bp or +7 bp) |

Modification type: Gene-specific.

*Source typo preserved: "PB4" — almost certainly intended to be "BP4".*

---

## 4. Not Applicable Criteria

| Criterion | Status | Comment (verbatim) |
|-----------|--------|--------------------|
| **PM1** | Not Applicable | Not applicable |
| **PM3** | Not Applicable | SLC6A8 is an X-linked gene, therefore PM3 is not applicable |
| **PP2** | Not Applicable | Not applicable, Missense Z score is 3.05 (o/e =0.46). |
| **PP5** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229) |
| **BP1** | Not Applicable | Not applicable, truncating and missense variants have been reported in affected patients. |
| **BP2** | Not Applicable | Not applicable, SLC6A8 is an X-linked gene |
| **BP3** | Not Applicable | Not applicable, SLC6A8 is a transmembrane protein with no repetitive regions of unknown function. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229) |

---

## 5. Rules for Combining Criteria (Bayesian Points System)

Per the specification description: variant curation for SLC6A8 uses the **Bayesian point-based approach** as described by Tavtigian, 2020 (PMID: 32720330). The "Rules for Combining Criteria" section at the end of the ClinGen specification document is to be **disregarded**; use the Bayesian points system below.

### Bayesian Points per Criterion Strength (Attachment: "Bayesian Points System - CCDS VCEP")

Assign Bayesian points for each criteria awarded as follows. Total points should be summed across all evidence codes.

| | Supporting | Moderate | Strong | Very Strong |
|---|---|---|---|---|
| **Pathogenic** | +1 | +2 | +4 | +8 |
| **Benign** | -1 | -2 | -4 | -8 |

### Classification by Total Points

Determine the variant classification by the sum of the points from the evidence collected according to the following Bayesian scale:

| Total points | Variant Classification |
|---|---|
| ≥10 | Pathogenic |
| 6 to 9 | Likely Pathogenic |
| -1 to 5 | Variant of Uncertain Significance |
| -2 to -6 | Likely Benign |
| ≤-7 | Benign |

*The "Point Based Variant Classification Categories" table in the main specification document lists the same ranges as: Pathogenic 10; Likely Pathogenic 6 - 9; Uncertain Significance -1 - 5; Likely Benign -6 - -2; Benign -7.*

**Note:** BA1 is stand-alone (Default Point Value listed as "Not Applicable") and classifies a variant as Benign independent of the point total.

---

## 6. Appendices

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold (gnomAD Grpmax Filtering Allele Frequency) | Additional Requirement | Strength | Points |
|-----------|------------------------------------------------------|------------------------|----------|--------|
| **BA1** | ≥0.002 (0.2%) | OR ≥10 homo-/hemizygotes (or sum of total hemi- and homozygotes) | Stand Alone | n/a |
| **BS1** | ≥0.0002 (0.02%) | - | Strong | -4 |
| **BS2** | - | ≥2 homo-/hemizygotes in gnomAD, OR male with documented normal urine creatine/creatinine ratio | Strong | -4 |
| **PM2_Supporting** | ≤0.00002 (0.002%) | AND 0 homo- or hemizygotes | Supporting | +1 |

### Appendix B: In Silico Thresholds Summary

| Tool | Pathogenic Direction | Benign Direction |
|------|---------------------|------------------|
| REVEL (missense) | PP3: >0.75 | BP4: ≤0.20 |
| SpliceAI (canonical splice, splice region, deep intronic) | PP3: delta score ≥0.20 | BP4: <0.10; BP7: ≤0.10 |
| SpliceAI (for PS1 / PM5 application) | Must be <0.1 for both the variant under review and the previously reported variant | - |

### Appendix C: Criterion Point Value Summary

| Criterion | Very Strong | Strong | Moderate | Supporting |
|-----------|-------------|--------|----------|------------|
| PVS1 | 8 | 4 | 2 | 1 |
| PS1 | - | 4 | 2 | 1 |
| PS2 | - | 4 | 2 | - |
| PS3 | - | - | 2 | 1 |
| PS4 | 8 | 4 | 2 | 1 |
| PM2 | - | - | Not applicable per SVI | 1 |
| PM4 | - | - | 2 | - |
| PM5 | - | - | 2 | 1 |
| PM6 | - | - | 2 | - |
| PP1 | - | 4 | 2 | 1 |
| PP3 | - | - | - | 1 |
| PP4 | - | 4 | 2 | 1 |
| BA1 | Stand Alone (Not Applicable point value) | - | - | - |
| BS1 | - | -4 | - | - |
| BS2 | - | -4 | - | -1 |
| BS3 | - | Not applicable | - | -1 |
| BS4 | - | -4 | - | - |
| BP4 | - | - | - | -1 |
| BP5 | - | - | - | -1 |
| BP7 | - | - | - | -1 |

### Appendix D: Key References

| Citation | PMID | Topic |
|----------|------|-------|
| Richards et al., 2015 | 25741868 | ACMG/AMP Variant Interpretation Guidelines |
| Tavtigian et al., 2020 | 32720330 | Bayesian point-based classification framework |
| Tayoun et al., 2018 | 30192042 | ClinGen SVI PVS1 recommendations / decision tree |
| Walker et al., 2023 | 37352859 | RNA splicing evidence; PS1 code weights for splice variants |
| — | 39418753 | Observed RNA splicing defects from functional splicing assays |
| Biesecker, 2024 | 38103548 | PP1 segregation strength levels |
| ClinGen SVI VCEP Review Committee | 29543229 | PP5 and BP6 not for use |
| — | 37891751 | p.Phe66-Leu81 and p.Val305-Thr325 form the creatine binding interface |
| Betsalel et al., 2012 | 22281021 | Approved creatine transport assay |
| Rosenberg et al., 2007 | 17465020 | Approved creatine transport assay |
| — | 21249153, 25485098, 33389772 | Creatine transport deficient mouse models |
| — | 22751104 | Brain-specific creatine transport knockout models |

### Appendix E: Source Documents

| File | Content |
|------|---------|
| ClinGen_ACMG_Specifications_SLC6A8_v2.1.pdf | Main specification |
| SLC6A8_PVS1_v2.1_033026 (downloaded as SLC6A8_PVS1_v2.pdf) | PVS1 decision tree |
| SLC6A8 PP4 V2.xlsx | PP4 point tables (males, females) |
| SLC6A8 Functional Assay SVI documentation.xlsx | PS3/BS3 approved assays |
| SLC6A8_Bayesian Points System_033026.docx | Bayesian points system and classification scale |
| SLC6A8 PS1 Splice Variants.docx | PS1 code weights for splice variants (Walker 2023 Table 2) |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 2.1 | 7/6/2026 | Removed the attached document with the response to the SVI. |

---

*This document is based on the ClinGen Cerebral Creatine Deficiency Syndromes Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for SLC6A8 Version 2.1 (https://cspec.genome.network/cspec/ui/svi/doc/GN027).*
