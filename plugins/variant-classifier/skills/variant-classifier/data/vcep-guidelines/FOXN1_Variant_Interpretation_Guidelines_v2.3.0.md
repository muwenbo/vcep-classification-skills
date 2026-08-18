# ClinGen Severe Combined Immunodeficiency Disease VCEP Variant Interpretation Guidelines for FOXN1

**Version:** 2.3
**Released:** 6/1/2026
**Affiliation:** Severe Combined Immunodeficiency Disease VCEP
**Source basis:** Richards et al., 2015 - Combining rules
**DOI:** 10.5281/zenodo.21434414
**ClinGen Criteria Specification Registry ID:** GN113

**Release Notes (v2.3, verbatim from the specification):**
- PM1 update: Removed Caveat rule from Moderate strength, but kept in VCEP specification. (It was previously listed in two places which was confusing.)
  - Removed the word "BS2" from caveat text since it's 'not applicable' for this gene. Now reads "Caveat: Variant must not meet BS1 or BA1 criteria."

**General Comments (verbatim):** All observations of FOXN1 variants may be curated under this single set of specifications and classified for T-cell immunodeficiency, congenital alopecia, and nail dystrophy with semidominant inheritance.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | FOXN1 (HGNC:12765) |
| **HGNC Name** | forkhead box N1 |
| **Transcript** | NM_001369369.1 |
| **Disease** | T-cell immunodeficiency, congenital alopecia, and nail dystrophy (MONDO:0011132) |
| **Inheritance** | Semidominant inheritance |

---

## Source Inventory

Every file distributed with this specification was opened and transcribed. None failed to open.

| File | Type | Status |
|------|------|--------|
| `ClinGen_ACMG_Specifications_FOXN1_v2.3.pdf` | Main specification, 20 pages | Read in full |
| `PVS1 flowchart.pptx` | 1-slide decision tree | Read (text extraction + rendered image); transcribed in Appendix A |
| `PS1_Splice.pdf` | Table 2 from PMID 37352859 | Read; transcribed in Appendix B |
| `PS2_PM6.pdf` | ClinGen SVI *de novo* recommendation v1.1 | Read; transcribed in Appendix C |
| `PS4_PM3.pdf` | Affected Observations Scoring Guide | Read; transcribed in Appendix D |
| `PS3.xlsx` | 2 worksheets (`LuciferaseAssay`, `unpublished data`) | Read; transcribed in Appendix E |
| `FOXN1 Corrections.docx` | PM1 correction sheet | Read; transcribed in Appendix F. **Contradicts the v2.3 spec tables — see the flag in Appendix F.** |

`GN113_data.json` is download metadata and is not source material.

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
2. [Benign Criteria](#benign-criteria)
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

**VCEP Specifications:** See attached PVS1 flowchart. (Transcribed in **[Appendix A](#appendix-a--pvs1-decision-tree-transcribed-from-pvs1-flowchartpptx)**.)

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification: <br>• PVS1 can be applied to variants not predicted to undergo nonsense-mediated decay but removing/altering the critical forkhead domain (amino acids 270-367; Newman et al., 2020; PMID: 31914405) based on recommendations from Walker et. al., 2023 (PMID: 37352859). <br>*Modification Type: General recommendation, Gene-specific* |
| **Strong** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with two specifications: <br>• For variants not predicted to undergo nonsense-mediated decay, but removing >10% of protein, (i.e. variants in the last exon, exon 9, or variants in the last 50 nucleotides of the penultimate exon after c.1577, codon 526, in exon 8), at least one pathogenic variant must be present downstream in order to apply PVS1_Strong <br>• PVS1_Strong can be applied to variants not predicted to undergo nonsense-mediated decay but removing/altering the transactivation domain (amino acids 511-563; Schlake et al., 2000 PMID: 10767081). <br>*Modification Type: General recommendation, Gene-specific* |
| **Moderate** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification: <br>• For variants not predicted to undergo nonsense-mediated decay, but removing >10% of protein, (i.e. variants in the last exon, exon 9, or variants in the last 50 nucleotides of the penultimate exon after c.1577, codon 526, in exon 8), when at least one pathogenic variant is not present downstream downgrade to PVS1_Moderate <br>*Modification Type: General recommendation* |
| **Supporting** | No PVS1_Supporting row is given in the specification's strength table. PVS1_Supp does appear as an outcome in the PVS1 flowchart (Initiation Codon branch — see Appendix A). |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Applicable for a same amino acid change if previously established variant is classified as pathogenic by SCID VCEP specifications for *FOXN1*. <br><br>Can also be applied for variants with the same predicted splicing event as a known Pathogenic variant (as classified by the SCID VCEP specifications for *FOXN1*), only when the strength of the prediction for the variant under assessment is of similar or higher strength than the strength of the prediction for the comparison (Likely) Pathogenic variant (i.e., per in silico splicing tool SpliceAI). See attached instructions (from Table 2 of PMID: 37352859) for determining when PS1 should be applied at PS1_Strong, _Moderate, or _Supporting. <br>*Modification Type: Gene-specific* |
| **Moderate** | Applicable for a same amino acid change if previously established variant is classified as likely pathogenic by SCID VCEP specifications for *FOXN1*. <br><br>Can also be applied for variants with the same predicted splicing event as a known (Likely) Pathogenic variant (as classified by the SCID VCEP specifications for *FOXN1*), only when the strength of the prediction for the variant under assessment is of similar or higher strength than the strength of the prediction for the comparison (Likely) Pathogenic variant (i.e., per in silico splicing tool SpliceAI). See attached instructions (from Table 2 of PMID: 37352859) for determining when PS1 should be applied at PS1_Strong, _Moderate, or _Supporting. <br>*Modification Type: Gene-specific, Strength* |
| **Supporting** | Can be applied for variants with the same predicted splicing event as a known (Likely) Pathogenic variant (as classified by the SCID VCEP specifications for *FOXN1*), only when the strength of the prediction for the variant under assessment is of similar or higher strength than the strength of the prediction for the comparison (Likely) Pathogenic variant (i.e., per in silico splicing tool SpliceAI). See attached instructions (from Table 2 of PMID: 37352859) for determining when PS1 should be applied at PS1_Strong, _Moderate, or _Supporting. <br>*Modification Type: Gene-specific, Strength* |

The referenced splicing table is transcribed in **[Appendix B](#appendix-b--ps1-code-weights-for-splicing-variants-transcribed-from-ps1_splicepdf)**.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** See attached scoring guide.

The following guidelines should be used when determining phenotypic consistency of each proband:
- "Phenotype highly specific for gene" proband must meet PP4_Moderate criteria
- "Phenotype consistent with gene but not highly specific" proband must meet PP4 criteria
- "Phenotype consistent with gene but not highly specific and high genetic heterogeneity" proband does not meet PP4 criteria but has at least one of three core *FOXN1* deficiency features (Congenital alopecia, Nail dystrophy, T lymphopenia)

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |
| **Strong** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |
| **Moderate** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |
| **Supporting** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |

The referenced SVI point system is distributed with this specification as `PS2_PM6.pdf` and is transcribed in **[Appendix C](#appendix-c--svi-recommendation-for-de-novo-criteria-ps2--pm6-version-11-transcribed-from-ps2_pm6pdf)**. The VCEP does not restate or modify the SVI point values; it only maps its own three phenotypic-consistency tiers onto the SVI table's phenotype rows (mapping above).

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | PS3 may be applied at the strong level for evidence from an animal model expressing the variant of interest and recapitulating FOXN1 deficiency (i.e. a mouse model with T cell lymphopenia). *Modification Type: Gene-specific* |
| **Moderate** | PS3 may be applied at the moderate level based on a luciferase assay showing reduced (<50%) activity, as part of a validated assay with pathogenic and benign controls (PMID: 37419334). *Modification Type: Gene-specific, Strength* |
| **Supporting** | PS3 may be applied at the supporting level based on a luciferase assay, without sufficient validation controls, showing reduced (<50%) activity, such as those reported in PMIDs: 31566583, 33464451, 34860543. *Modification Type: Gene-specific, Strength* |

Comparator note: reduced activity threshold is **strict** (`<50%`).

#### Approved Assay Instances

See **[Appendix E](#appendix-e--ps3-approved-assays-transcribed-from-ps3xlsx)** for the full approved-assay table and the associated unpublished luciferase dataset.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** Evaluate each unrelated heterozygous affected individual with the attached Affected Observations Scoring Guide and sum points across all probands.
- Exclude the proband used to satisfy the PP4 criteria
- Caveat: variant must be sufficiently rare (meet PM2_supporting specification).

| Strength | Criteria | Comparators |
|----------|----------|-------------|
| **Very Strong** | Sum of case scores ≥8 points | ≥ inclusive |
| **Strong** | Sum of case scores 4-7.75 points | inclusive range |
| **Moderate** | Sum of case scores 2-3.75 points | inclusive range |
| **Supporting** | Sum of case scores 1-1.75 points | inclusive range |

*Modification Type (all levels): Disease-specific*

Scoring guide transcribed in **[Appendix D](#appendix-d--affected-observations-scoring-guide-ps4--pm3-transcribed-from-ps4_pm3pdf)**.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** Caveat: Variant must not meet BS1 or BA1 criteria.

| Strength | Criteria |
|----------|----------|
| **Moderate** | Applicable for variants in the DNA binding forkhead domain (amino acids 270-367), which is a well-established functional domain (Newman et al., 2020; PMID: 31914405) of *FOXN1* with low tolerance for benign variation. *Modification Type: Gene-specific* |

> **Conflict flag.** The distributed `FOXN1 Corrections.docx` reproduces PM1 with the caveat worded "Variant must not meet BS1, **BS2**, or BA1 criteria" and repeats it under the Moderate strength row. Both of those are exactly what the v2.3 release notes say were removed. The Corrections document is therefore stale relative to v2.3 and the spec's own table is operative. See [Appendix F](#appendix-f--foxn1-corrections-transcribed-from-foxn1-correctionsdocx).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:** This value is based on the HMAF of NM_001369369.1(FOXN1):c.1585del (p.Leu529fs), the most common pLOF variant present in gnomADv4.0.0 that classifies as Pathogenic based on specified guidelines.

| Strength | Criteria | Comparator |
|----------|----------|------------|
| **Supporting** | gnomAD Grpmax filtering allele frequency ≤0.00002412 | **Inclusive** (`≤`) |

*Modification Type: Gene-specific*

No PM2 at Moderate strength is specified.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.
Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Evaluate each unrelated homozygous or compound heterozygous affected individual with the attached Affected Observations Scoring Guide and sum points across all probands.
- Caveat: additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for *FOXN1*.
- Caveat: variants must be sufficiently rare (meet PM2_supporting specification).

| Strength | Criteria | Comparators |
|----------|----------|-------------|
| **Very Strong** | Sum of case scores ≥8 points | ≥ inclusive |
| **Strong** | Sum of case scores 4-7.75 points | inclusive range |
| **Moderate** | Sum of case scores 2-3.75 points | inclusive range |
| **Supporting** | Sum of case scores 1-1.75 points | inclusive range |

*Modification Type (all levels): General recommendation*

Scoring guide transcribed in **[Appendix D](#appendix-d--affected-observations-scoring-guide-ps4--pm3-transcribed-from-ps4_pm3pdf)**.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Additional requirement that when applied to deletion variants, the deleted region must contain a known pathogenic or likely pathogenic variant that is not predicted/observed to alter splicing. *Modification Type: Gene-specific* |
| **Supporting** | Additional requirement that when applied to deletion variants, the deleted region must contain a known VUS variant that is not predicted/observed to alter splicing. *Modification Type: Gene-specific, Strength* |

> **Source wording flag:** "a known VUS variant" is redundant ("variant of uncertain significance variant") in the source; transcribed verbatim.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

*For nonsense variants:*

- **PM5_Strong** — PM5 may be applied at a Strong level of evidence for any nonsense variant with 4+ points from informative variants (see point table below). PM5_Strong should be downgraded to PM5_Moderate if PVS1 is applied at any strength.
- **PM5_Moderate** — PM5 may also be applied at a Moderate level of evidence for any nonsense variant with 2+ points from informative variants (see point table below). PM5_Moderate may not be combined with PVS1_VeryStrong (should be downgraded to PM5_Supporting if PVS1_VeryStrong is applied).
- **PM5_Supporting** — Also applicable to a nonsense variant with 1 point from an informative variant (see point table). Informative variants must also be classified by these rule specifications.

*For missense variants (from the strength rows):*

| Strength | Criteria |
|----------|----------|
| **Moderate** | Applicable at default strength (PM5) if previously established variant is classified as pathogenic. |
| **Supporting** | Applicable at reduced strength of PM5_Supporting if previously established variant is classified as likely pathogenic. |

#### PM5 Nonsense Point Table

Column headings as printed: **Type of variant under assessment (VUA); Informative variant; Score**

| Type of variant under assessment (VUA) | Informative variant | Score |
|---|---|---|
| Nonsense variant predicted to lead to NMD | P/LP variant in the exon of DNA change predicted to lead to NMD | +1pt |
| Nonsense variant predicted to lead to NMD | B/LB variant in the exon predicted to lead to NMD | -2pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | P/LP variant resulting in a PTC in the same exon but downstream of VUA | +1pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | B/LB variant resulting in PTC in the same exon but upstream of the VUA | -2pt |

NMD = nonsense-mediated decay; PTC premature termination codon

> **Source wording flag:** the legend reads "PTC premature termination codon" — the "=" is missing in the source. Transcribed verbatim.

**Note (verbatim):** The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet "+1 pathogenic variant downstream" on the PVS1 flowchart. If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA. The VUA must be sufficiently rare, meet PM2_Supporting, to apply this point system. If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic without use of PM5 and without use of only PVS1 plus PM2.

*Modification Type: Gene-specific (Strong, Moderate); Gene-specific, Strength (Supporting)*

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** See attached scoring guide.

The following guidelines should be used when determining phenotypic consistency of each proband:
- "Phenotype highly specific for gene" proband must meet PP4_Moderate criteria
- "Phenotype consistent with gene but not highly specific" proband must meet PP4 criteria
- "Phenotype consistent with gene but not highly specific and high genetic heterogeneity" proband does not meet PP4 criteria but has at least one of three core *FOXN1* deficiency features (Congenital alopecia, Nail dystrophy, T lymphopenia)

| Strength | Criteria |
|----------|----------|
| **Strong** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |
| **Moderate** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |
| **Supporting** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |

Note: unlike PS2, PM6 has no Very Strong row in the specification, although PM6_VeryStrong exists in the SVI table (Appendix C) and PM6_VeryStrong appears in the Rules for Combining Criteria code lists. See **[Internal Inconsistencies](#internal-inconsistencies-and-source-gaps)**.

See **[Appendix C](#appendix-c--svi-recommendation-for-de-novo-criteria-ps2--pm6-version-11-transcribed-from-ps2_pm6pdf)**.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** The estimated LOD (Z) score is calculated as follows:

> Z = log₁₀{1/[(0.25)^x (0.5)^y]}

- **x** is the number of affected relatives with at least one core feature (see top three bullet/sub-bullet points of PP4) harboring biallelic *FOXN1* variants (confirmed by genetic analysis), not including the proband
- **y** is the number of affected relatives with at least one core feature (see top three bullet/sub-bullet points of PP4) harboring a heterozygous *FOXN1* variant (confirmed by genetic analysis or an obligate carrier), not including the proband

| Strength | Criteria | Comparators |
|----------|----------|-------------|
| **Strong** | 32:1 likelihood ratio (LOD score **≥1.5**, summed across all families with segregation evidence) per recommendations from PMID: 30311386 Table 4a | ≥ inclusive |
| **Moderate** | 16:1 likelihood ratio (LOD score **1.2-<1.5**, summed across all families with segregation evidence) per recommendations from PMID: 30311386 Table 4a | lower bound inclusive, upper bound strict |
| **Supporting** | 4:1 likelihood ratio (LOD score **0.6-<1.2**, summed across all families with segregation evidence) per recommendations from PMID: 30311386 Table 4a | lower bound inclusive, upper bound strict |

*Modification Type (all levels): General recommendation*

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable.** Comment: "Does not apply, FOXN1 does not have a low rate of benign missense variation, with a missense constraint score of Z=0.66."

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

| Strength | Criteria | Comparators |
|----------|----------|-------------|
| **Moderate** | Moderate evidence can be applied for a REVEL score of **≥0.932**, downgraded from the recommendation of Strong in Pejaver et al., 2022 (PMID: 36413997). | ≥ inclusive |
| **Supporting** | • Supporting evidence can be applied for a REVEL score of **≥0.644 (to <0.932)**, based on recommendations of Pejaver et al., 2022 (PMID: 36413997).<br>• Also applicable to missense, synonymous, or intronic variants predicted to impact splicing by SpliceAI Δ score **≥0.2** | lower bound inclusive; upper bound strict; SpliceAI ≥ inclusive |

*Modification Type (both levels): General recommendation*

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** PP4 applicability and strength is determined by the total points accumulated by a single affected individual according to the list below:

**Core Features**
- Congenital, or early-onset, alopecia or absent eyebrows (0.25pt)
- Nail dystrophy (0.25pt)
- Absent/very low T cell number of <0.05x10^9/L (0.5pt) OR if >0.05x10^9/L then:
  - Low T cell number for age 0.05-1.0x10^9/L  OR T- B+ [NK+]* SCID OR Poor/absent proliferative response to phytohemagglutinin (PHA) (0.25pt)
  - Abnormal TRECs OR <20% of CD4+ T cells are naïve (naïve T cells should be measured via CD3/CD4/CD45RA, or with additional naive markers) OR low CD8+ T cell number relative to age-matched controls (0.25pt)

**Additional Features**
- Development of T cells in an artificial thymic organoid (ATO) system (0.25pt)
- Transplant of thymic tissue corrects T cell deficiency (0.5pt)
- SCID gene panel or exome/genome sequencing (0.5pt), with no other variant of interest

\*Absent NK cells would not be consistent with a FOXN1 specific phenotype, however if absence/presence of NK cells is not noted, points may still be awarded if SCID gene panel or exome/genome sequencing has ruled out alternative causes

| Strength | Criteria | Comparators |
|----------|----------|-------------|
| **Moderate** | Patient score of **≥2 points** | ≥ inclusive |
| **Supporting** | Patient score of **1-<2 points** | lower bound inclusive, upper bound strict |

*Modification Type (both levels): Disease-specific, Gene-specific*

Comparator note within the core-feature list: the absent/very low T cell branch uses **strict** `<0.05x10^9/L` for 0.5pt and **strict** `>0.05x10^9/L` for the alternative branch; TRECs branch uses **strict** `<20%`.

> **Source gap flag:** the two branches leave the value exactly 0.05x10^9/L unassigned (neither `<` nor `>` covers it). Transcribed as written; not reconciled.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable.** "This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee." (PubMed: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:** Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:
- Prevalence: 1:5,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.01
- Penetrance: 10%

| Strength | Criteria | Comparator |
|----------|----------|------------|
| **Stand Alone** | gnomAD Grpmax filtering allele frequency **>0.00447** | **Strict** (`>`) |

*Modification Type: Gene-specific*

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:** Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:
- Prevalence: 1:50,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.01
- Penetrance: 10%

| Strength | Criteria | Comparator |
|----------|----------|------------|
| **Strong** | gnomAD Grpmax filtering allele frequency **>0.00141** OR a bottle-necked population with a MAF **>0.00141** may be used for this criterion. Caveat: If the variant is known to be a founder variant in the bottle-necked population do not consider the frequency in that population for BS1. | **Strict** (`>`) |

*Modification Type: Gene-specific*

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** **Not Applicable.** Comment: "Does not apply due to reduced penetrance."

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** **Not Applicable.** Comment: "There is not a well-established functional study which can rule out all damaging effects on protein function."

(Consistent with the PS3 worksheet, which records "BS3 not applied" for every approved assay — see Appendix E.)

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

| Strength | Criteria |
|----------|----------|
| **Strong** | Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation. *Modification Type: None* |

> **Source note:** the BS4 Strong row restates the ACMG caveat verbatim and adds no VCEP-specific rule. No LOD-score threshold for BS4 is given. Transcribed as written.

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | "Does not apply." |
| **BP2** | Specified (Supporting) | Applicable only when observed in cis with a pathogenic variant in any inheritance pattern, with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for *FOXN1*. *Modification Type: Disease-specific* |
| **BP3** | Not Applicable | "Does not apply." |
| **BP4** | Specified (Supporting) | • Supporting evidence can be applied for a REVEL score of **<0.290** based on recommendations of Pejaver et al., 2022 (PMID: 36413997).<br>• Also applicable to synonymous or intronic variants not predicted to impact splicing by SpliceAI Δ score **≤0.1**<br>*Comparators: REVEL strict (`<`); SpliceAI inclusive (`≤`).* *Modification Type: General recommendation* |
| **BP5** | Specified (Supporting) | "Use with no specification." *Modification Type: None* |
| **BP6** | Not Applicable | "This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee." (PubMed: 29543229) |
| **BP7** | Specified (Supporting) | A synonymous variant, or deep intronic variant affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions, for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site (SpliceAI Δ score **≤0.1**) AND the nucleotide is not highly conserved. *Comparator: inclusive (`≤`).* *Modification Type: General recommendation* |

---

## Rules for Combining Criteria

Transcribed verbatim from the "Rules for Combining Criteria" section of the specification. Parenthetical lists are the codes the VCEP designates as satisfying each slot.

**Type:** Richards et al., 2015 - Combining rules

### Pathogenic

| # | Rule |
|---|------|
| 1 | **1 Very Strong** (PVS1, PS2_Very Strong, PS4_Very Strong, PM3_Very Strong) **AND ≥ 1 Strong** (PVS1_Strong, PS1, PS2, PS3, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong) |
| 2 | **1 Very Strong** (PVS1, PS2_Very Strong, PS4_Very Strong, PM3_Very Strong) **AND ≥ 2 Moderate** (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate) |
| 3 | **1 Very Strong** (PVS1, PS2_Very Strong, PS4_Very Strong, PM3_Very Strong) **AND 1 Moderate** (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate) **AND 1 Supporting** (PS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
| 4 | **1 Very Strong** (PVS1, PS2_Very Strong, PS4_Very Strong, PM3_Very Strong) **AND ≥ 2 Supporting** (PS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
| 5 | **≥ 2 Strong** (PVS1_Strong, PS1, PS2, PS3, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong) |
| 6 | **1 Strong** (PVS1_Strong, PS1, PS2, PS3, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND ≥ 3 Moderate** (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP3_Moderate, PP4_Moderate) |
| 7 | **1 Strong** **AND 2 Moderate AND ≥ 2 Supporting** (same code lists as above) |
| 8 | **1 Strong** **AND 1 Moderate AND ≥ 4 Supporting** (same code lists as above) |

### Likely Pathogenic

| # | Rule |
|---|------|
| 1 | **1 Very Strong AND 1 Moderate** |
| 2 | **1 Strong AND 1 Moderate** |
| 3 | **1 Strong AND ≥ 2 Supporting** |
| 4 | **≥ 3 Moderate** |
| 5 | **2 Moderate AND ≥ 2 Supporting** |
| 6 | **1 Moderate AND ≥ 4 Supporting** |
| 7 | **1 Strong AND 2 Moderate** |
| 8 | **1 Very Strong AND 1 Supporting** |

(Code lists per slot are identical to those given under Pathogenic.)

### Benign

| # | Rule |
|---|------|
| 1 | **≥ 2 Strong** (BS1, BS4) |
| 2 | **1 Stand Alone** (BA1) |

### Likely Benign

| # | Rule |
|---|------|
| 1 | **≥ 2 Supporting** (BP2, BP4, BP5, BP7) |
| 2 | **1 Strong** (BS1, BS4) |

> **Note on the Likely Pathogenic list:** rules 2 and 7 in the source both begin "1 Strong AND ... Moderate" (1 Moderate and 2 Moderate respectively); rule 7 is subsumed by Pathogenic rule 6 only at ≥3 Moderate, so both are retained as printed. No point-based (Tavtigian) classification system is specified anywhere in this package.

---

## Appendices

### Appendix A — PVS1 Decision Tree (transcribed from `PVS1 flowchart.pptx`)

Single slide. Five top-level variant-type branches. Transcription below follows the arrows in the rendered slide.

**Branch 1: Nonsense or Frameshift**

| Condition | Sub-condition | Sub-sub-condition | Outcome |
|---|---|---|---|
| Predicted to undergo NMD ᵇ | Exon is present in biologically-relevant transcript(s) | — | **PVS1** |
| Predicted to undergo NMD ᵇ | Exon is absent from biologically-relevant transcript(s) | — | **N/A** |
| Not predicted to undergo NMD ᵇ (i.e. premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon [c.1577 (codon 526) in exon 8]) | Truncated/altered region is critical to protein function | Occurs within the forkhead domain (amino acids 270-367) | **PVS1** |
| " | Truncated/altered region is critical to protein function | Occurs within the transactivation domain (amino acids 511-563) | **PVS1_Strong** |
| " | Role of region in protein function is unknown | LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) | **N/A** |
| " | Role of region in protein function is unknown | LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) → Variant removes >10% of protein → 1+ pathogenic variant present downstream | **PVS1_Strong** |
| " | " | ... → Variant removes >10% of protein → No known downstream pathogenic variants | **PVS1_Moderate** |
| " | " | ... → Variant removes <10% of protein | **PVS1_Moderate** |

**Branch 2: GT--AG 1,2 splice sites ᵃ**

| Condition | Sub-condition | Sub-sub-condition | Outcome |
|---|---|---|---|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD ᵇ | Exon is present in biologically-relevant transcript(s) | — | **PVS1** |
| " | Exon is absent from biologically-relevant transcript(s) | — | **N/A** |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is **NOT** predicted to undergo NMD ᵇ (i.e. premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon [c.1577 (codon 526) in exon 8]) | Truncated/altered region is critical to protein function | Occurs within the forkhead domain (amino acids 270-367) | **PVS1** |
| " | " | Occurs within the transactivation domain (amino acids 511-563) | **PVS1_Strong** |
| " | Role of region in protein function is unknown | LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) | **N/A** |
| " | " | LoF variants in this exon are not frequent ... → Variant removes >10% of protein → 1+ pathogenic variant present within deleted/truncated region | **PVS1_Strong** |
| " | " | ... → Variant removes >10% of protein → No known pathogenic variants within deleted/truncated region | **PVS1_Moderate** |
| " | " | ... → Variant removes <10% of protein | **PVS1_Moderate** |
| Exon skipping or use of a cryptic splice site preserves reading frame | Truncated/altered region is critical to protein function | Occurs within the forkhead domain (amino acids 270-367) | **PVS1** |
| " | " | Occurs within the transactivation domain (amino acids 511-563) | **PVS1_Strong** |

**Branch 3: Deletion (Single exon to full gene)**

| Condition | Sub-condition | Sub-sub-condition | Outcome |
|---|---|---|---|
| Full gene deletion | — | — | **PVS1** ᵈ |
| Single to multi exon deletion – Disrupts reading frame and is predicted to undergo NMD ᵇ | Exon is present in biologically-relevant transcript(s) | — | **PVS1** |
| " | Exon is absent from biologically-relevant transcript(s) | — | **N/A** |
| Single to multi exon deletion – Disrupts reading frame and is **NOT** predicted to undergo NMD ᵇ (i.e. premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon [c.1577 (codon 526) in exon 8]) | Truncated/altered region is critical to protein function | Occurs within the forkhead domain (amino acids 270-367) | **PVS1** |
| " | " | Occurs within the transactivation domain (amino acids 511-563) | **PVS1_Strong** |
| " | Role of region in protein function is unknown | LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) | **N/A** |
| " | " | LoF variants in this exon are not frequent ... → Variant removes >10% of protein → 1+ pathogenic variant present within deleted region | **PVS1_Strong** |
| " | " | ... → Variant removes >10% of protein → No known pathogenic variants within deleted region | **PVS1_Moderate** |
| " | " | ... → Variant removes <10% of protein | **PVS1_Moderate** |
| Single to multi exon deletion – Preserves reading frame | Truncated/altered region is critical to protein function | Occurs within the forkhead domain (amino acids 270-367) | **PVS1** |
| " | " | Occurs within the transactivation domain (amino acids 511-563) | **PVS1_Strong** |

**Branch 4: Duplication (≥1 exon in size and must be completely contained within gene)**

| Condition | Sub-condition | Outcome |
|---|---|---|
| Proven in tandem | Reading frame disrupted and NMD predicted to occur | **PVS1** |
| Proven in tandem | No or unknown impact on reading frame and NMD | **N/A** |
| Presumed in tandem | Reading frame presumed disrupted and NMD predicted to occur | **PVS1_Strong** |
| Proven not in tandem | — | **N/A** |

> Note on the Duplication branch: the slide draws arrows from both "Proven in tandem" and "Presumed in tandem" into the middle row; the three outcome rows as laid out are PVS1 / N/A / PVS1_Strong as tabulated. "Presumed in tandem" has no separate "no/unknown impact" row.

**Branch 5: Initiation Codon**

| Condition | Sub-condition | Outcome |
|---|---|---|
| No known alternative start codon in other transcripts | ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon (Met28) | **PVS1_Moderate** |
| No known alternative start codon in other transcripts | No pathogenic variant(s) upstream of closest potential in-frame start codon (Met28) | **PVS1_Supp** |
| Different functional transcript uses alternative start codon | — | **N/A** |

**Superscript markers present on the slide:** ᵃ (on "GT--AG 1,2 splice sites"), ᵇ (on every "NMD" reference), ᵈ (on the full-gene-deletion "PVS1" outcome).

> **Source gap flag:** the footnote definitions for markers **a**, **b**, and **d** are not present anywhere on the slide or in its speaker notes. They cannot be recovered from the distributed file and are **not specified by this VCEP** in the material provided.

**Speaker note on the slide (verbatim):** "PLEASE NOTE - Download as a Powerpoint or make a copy of this slide and save elsewhere - this is a template for general use."

---

### Appendix B — PS1 Code Weights for Splicing Variants (transcribed from `PS1_Splice.pdf`)

**Title as printed:** "Table 2  PS1 code weights for variants with same predicted splicing event as a known (likely) pathogenic variant". Sourced from PMID: 37352859 (Walker et al., 2023).

| Variant under assessment (VUA) | Baseline computational/predictive code applicable to VUA | Position of comparison variant relative to VUA | PS1 code with **P** comparison variant | PS1 code with **LP** comparison variant |
|---|---|---|---|---|
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | same nucleotide | PS1 | PS1_Moderate |
| Located outside splice donor/acceptor ±1,2 dinucleotide positions | PP3 | within same splice donor/acceptor motif (including at ±1,2 positions) | PS1_Moderate | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | within same splice donor/acceptor ±1,2 dinucleotide | PS1_Supporting | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1 | within same splice donor/acceptor region, but outside ±1,2 dinucleotide ᵃ | PS1_Supporting | PS1_Supporting |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | within same splice donor/acceptor ±1,2 dinucleotide | PS1 | N/A |
| Located at splice donor/acceptor ±1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | within same splice donor/acceptor motif, but outside ±1,2 dinucleotide ᵃ | PS1_Moderate | PS1_Supporting |

**Prerequisite for all (verbatim):** the predicted event of the VUA must precisely match the predicted event of the comparison (likely) pathogenic variant (e.g., both predicted to lead to exon skipping, or both to lead to enhanced use of a cryptic splice motif, AND the strength of the prediction for the VUA must be of similar or higher strength than the strength of the prediction for the comparison [likely] pathogenic variant). For an exonic variant, predicted or proven functional effect of missense substitution(s) encoded by the VUA and (likely) pathogenic variant should also be considered before application of this code. Dinucleotide positions refer to donor and acceptor dinucleotides in reference transcript(s) used for curation. Designated donor and acceptor motif ranges should be based on position weight matrices for intron category (see methods). For GT-AG introns these are defined as follows: the donor motif, last 3 bases of the exon and 6 nucleotides of intronic sequence adjacent to the exon; acceptor motif, first base of the exon and 20 nucleotides upstream from the exon boundary. Consider other motif ranges for non-GT-AG introns.

**Footnote a (verbatim):** If relevant, splicing assay data for a pathogenic variant outside a ±1,2 dinucleotide position may be used to update a PVS1 decision tree and hence the applicable PVS1 code for a ±1,2 dinucleotide variant.

> **Source note:** rows 3 and 4 differ only in "region" vs "motif" wording between the ±1,2-dinucleotide and outside-dinucleotide positions ("within same splice donor/acceptor **region**" in row 4 vs "**motif**" in row 6). Transcribed verbatim; the source referenced by the VCEP ("see methods") is not distributed with this package.

---

### Appendix C — SVI Recommendation for De Novo Criteria (PS2 & PM6) - Version 1.1 (transcribed from `PS2_PM6.pdf`)

**Header:** ClinGen Sequence Variant Interpretation Recommendation for de novo Criteria (PS2/PM6) - Version 1.1. Working Group Page: https://clinicalgenome.org/working-groups/sequence-variant-interpretation/. Date Approved: March 18, 2018, updated May 5, 2021. Changes from v1: Clarified that confirmed/assumed is with regards to parental relationships and not de novo status.

This is the general ClinGen SVI document, distributed unmodified. The three parameters are: confirmed vs. assumed parental relationships status; phenotypic consistency; number of *de novo* observations. Each proband with a *de novo* variant is awarded a point value from Table 1; the combined point value of all *de novo* occurrences is compared to Table 2. If the parents have not been tested for parentage or for the variant, no points should be awarded.

#### Table 1. Points* awarded per *de novo* occurrence

| Phenotypic consistency | *de novo* with confirmed parental relationships | *de novo* with unconfirmed parental relationships |
|---|---|---|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity** | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

\*Note that these points are *not* equivalent to the points used to classify a variant per the Tavtigian et al 2020 "Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines"
\*\*Maximum allowable value of 1 may contribute to overall score

#### Table 2. Recommendation for determining the appropriate ACMG/AMP evidence strength level for *de novo* occurrence(s)

| Supporting (PS2_Supporting or PM6_Supporting) | Moderate (PS2_Moderate or PM6) | Strong (PS2 or PM6_Strong) | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |
|---|---|---|---|
| 0.5 | 1 | 2 | 4 |

#### Worked examples and additional considerations (verbatim, condensed)

For all uses of *de novo* criteria, the phenotype in the patient must be consistent with the gene/disease association as recommended in the ACMG/AMP guidelines. When the patient's phenotype is consistent with the gene/disease association but not highly specific, the SVI recommends decreasing the points awarded. Examples given: a *SIK1* case awarded 1 point → PS2_Moderate; three such cases combining to 3 points → PS2 (Strong, reaching 2 but not 4); an *ASH1L* case awarded 0.5 points → PS2_Supporting; two such cases combining to 1 point → PS2_Moderate; a *NIPBL* case with a non-consistent phenotype awarded zero points → no *de novo* criteria applied.

Additional considerations based on inheritance (verbatim):
- **Conditions with X-linked inheritance:** if the variant occurs *de novo* in an unaffected carrier mother, and family history is consistent - i.e., she has no affected brothers/other male relatives apart from her affected son(s) – *de novo* criteria may be applied despite the fact that she is unaffected.
- **Autosomal recessive conditions:** for a *de novo* occurrence in a gene associated with a condition inherited in an autosomal recessive pattern without an additional pathogenic/likely pathogenic variant identified, the strength of evidence should be decreased by one level.
- **Mosaicism:** for cases with apparent germline mosaicism (multiple affected siblings with both parents negative for the variant), parental relationships must be confirmed in order for *de novo* criteria to apply.

> **Note:** the specification's own PS2/PM6 sections restate none of these values; they say only "Use ClinGen SVI recommendations for *de novo* criteria (see instructions below)". This appendix is the distributed instruction sheet, so the 2 / 1 / 0.5 / 0.25 point matrix and the 0.5 / 1 / 2 / 4 strength ladder **are source-backed for FOXN1** by virtue of being in the VCEP's own distributed supplementary file. They are ClinGen SVI general values, not FOXN1-specific values.

---

### Appendix D — Affected Observations Scoring Guide (PS4 / PM3) (transcribed from `PS4_PM3.pdf`)

Single page, single table. Used by both PS4 (heterozygous probands) and PM3 (homozygous / compound heterozygous probands).

| Phenotype Consistency | Heterozygous Probands (PS4) | PM3: VBC is confirmed in trans with a P/LP variant | PM3: VBC is assumed in trans with a P/LP variant | PM3: VBC is confirmed in trans with a VUS | PM3: VBC is homozygous |
|---|---|---|---|---|---|
| Phenotype specific with gene (meets PP4) and all relevant genes for disorder tested (SCID gene panel or exome/genome sequencing), with no other variant of interest | +1 point | +2 point | +1.5 point | +1.0 point | +1.0 point |
| Phenotype specific with gene (meets PP4) but not all relevant genes for disorder tested, and/or more than one variant of interest | +0.5 point | +1 point | +0.75 point | +0.5 point | +0.5 point |
| Phenotype consistent with gene (has at least one core feature, see PP4) and all relevant genes for disorder tested (SCID gene panel or exome/genome sequencing), with no other variant of interest | +0.5 point | +0.5 point | +0.5 point | +0.5 point | +0.5 point |
| Phenotype consistent with gene (has at least one core feature, see PP4) but not all relevant genes for disorder tested, and/or more than one variant of interest | +0.25 point | +0.25 point | +0.25 point | +0.25 point | +0.25 point |
| Phenotype not consistent with gene | +0 point | +0 point | +0 point | +0 point | +0 point |

\*VBC variant being curated

> **Source wording flags (verbatim, uncorrected):** the units read "+2 point", "+1.5 point", "+0 point" (singular "point" throughout). The header row reads "Phenotype specific **with** gene" rather than "for gene". The asterisk footnote defines VBC but the asterisk is not attached to any cell in the table.

---

### Appendix E — PS3 Approved Assays (transcribed from `PS3.xlsx`)

Two worksheets.

#### Worksheet 1: `LuciferaseAssay` (21 rows × 5 columns)

The sheet is laid out with attributes as rows and one column per study. Transposed here for readability.

| Attribute | Study 1 | Study 2 | Study 3 | Study 4 |
|---|---|---|---|---|
| **PMID** | mansucript in press | 31566583 | 33464451 | 34860543 |
| **DOI / link** | https://www.sciencedirect.com/science/article/pii/S0091674923008588 | 10.1172/JCI127565 | 10.1007/s10875-021-00967-y | 10.1126/sciadv.abj9247 |
| **Author** | Nicolai van Oers (VCEP member) | Du | Giardino | Rota |
| **Year** | *(blank)* | 2019 | 2021 | 2021 |
| **Assay (general description)** | luciferase reporter construct cotransfected into heterologous cells together with expression vectors containing Foxn1 WT or mutants | The Psmb11 luciferase reporter construct (0.5 μg) was cotransfected into HEK 293T cells (2.5 × 10⁵ cells/well) together with pCMV-FLAG (0.5 μg) expression vectors containing Foxn1 WT or mutants, using Fugene 6 Reagent (Promega). A separate construct containing β-gal (0.1 μg) was included in the transfections to normalize each well for transfection efficiency. | A luciferase reporter gene pGL4.10 (Luc2, Promega) was cloned downstream of a wild-type β5t promoter (β5t-luc) or a mutated β5t promoter with a mutated FOXN1 binding site (β5t-mut-luc), with β5t being a known FOXN1 target. Each condition was transfected with a luciferase reporter plasmid (β5t-luc or β5t-mut-luc), a Renilla control plasmid (pRL Promega), and a FOXN1 construct of interest in a ratio | 4D6 cells were cotransfected with a renilla control plasmid (pRL Promega) and a luciferase reporter plasmid (pGL4.10[Luc2], Promega) under the control of a minimal wild-type Psmb11 promoter (designated β5t-luc) or a β5t promoter with a mutated FOXN1-binding sites (β5t-mut-luc) plus a FOXN1 construct of interest in a ratio of 1:10:10. |
| **Material used** | cell lines | HEK 293T cells; variants introduced by site-directed mutagenesis | 4D6 cells; variants introduced by site-directed mutagenesis | 4D6 cells; variants introduced by site-directed mutagenesis |
| **Readout type** | Quantitative | Quantitative | Quantitative | Quantitative |
| **Readout description** | luciferase activity relative to WT | Forty-eight hours after transfection, the cells were harvested and the luciferase activity measured using a luciferase assay kit (Promega). Luciferase activity was normalized to β-gal activity, which was used as an internal control. | Twenty-four hours post-transfection, cell lysates were prepared following the manufacturer's protocol (Promega Dual Luciferase reporter assay system) using 80 μl/well of PLB lysis buffer provided by the kit. Luciferase readings were performed at a Promega Glo Max luminometer. Reporter activity was corrected by calculating the ratio of luciferase/Renilla for each well. The activity of luciferase wa[s] *(cell text truncated in source cell)* | Luciferease activity was measured 24 hours later using the Dual-Lucifearase Assay kit |
| **Biological replicates (met/not met)** | met | triplicate samples | *(blank)* | *(blank)* |
| **Technical replicates (met/not met); description** | met | 3 independent transfections | Each transfection was performed in triplicate | *(blank)* |
| **Basic positive control (met/not met); description** | met | WT | WT | *(blank)* |
| **Basic negative control (met/not met); description** | met | Vector | β5t-mut-luc | *(blank)* |
| **Validation controls P/LP (#)** | 10 | *(blank)* | *(blank)* | *(blank)* |
| **Validation controls B/LB (#)** | 5 | *(blank)* | *(blank)* | *(blank)* |
| **Statistical analysis** | t test | 1-way ANOVA | unpaired t tests | two-tailed unpaired t test |
| **Threshold for normal readout** | >75% | >75% | >75% | >75% |
| **Threshold for abnormal readout** | <50% | <50% | <50% | <50% |
| **Approved assay (y/n)** | Y | y | y | y |
| **Proposed strength** | PS3_Moderate; BS3 not applied | PS3_Supporting; BS3 not applied | PS3_Supporting; BS3 not applied | PS3_Supporting; BS3 not applied |

Comparators: normal readout threshold **strict** (`>75%`); abnormal readout threshold **strict** (`<50%`). The 50–75% band is not assigned a call in this sheet.

> **Source typo flags (verbatim):** "mansucript in press" (PMID cell, study 1); "Luciferease activity ... Dual-Lucifearase Assay kit" (study 4); "a β5t promoter with a mutated FOXN1-binding **sites**" (study 4).

> **Note:** the specification text attributes PS3_Moderate to PMID 37419334, whereas the worksheet's PS3_Moderate study is recorded as "mansucript in press" with a ScienceDirect link. These are consistent in role but the worksheet has not been updated with the now-published PMID.

#### Worksheet 2: `unpublished data` — luciferase reporter results (lookup table)

This is a **variant-level lookup table**, not a rule. It lists luciferase reporter activity as a fraction of wild-type (%WT expressed as a decimal, e.g. 0.92 = 92% of WT). It supports application of the PS3 thresholds above; it does not itself define a criterion. Apply the `LuciferaseAssay` thresholds (abnormal `<50%`, normal `>75%`) to these values.

| Protein Sequence Change | DNA Sequence | Luciferase Reporter Assays (%WT) |
|---|---|---|
| P430S | 1288C>T | 0.92 |
| R69C | 205C>T | 0.91 |
| A121V | 362C>T | 0.89 |
| G238D | 713G>A | 1.05 |
| A555V | 1664C>T | 0.75 |
| E169K | 505G.A | 0.78 |
| P230R | 689C>G | 1.03 |
| P242S | 724C>T | 0.85 |
| V294I | *(blank)* | 0.18 |
| R320W | 958C>T | 0.02 |
| H321N | 961C>A | 0.05 |
| L325P | 974T>C | 0.015 |
| C328R | 982T>C | 0.57 |
| K331A/N334A/K335A | *(blank)* | 0.012 |
| S339D | 1015_1016TC>GA | 0.83 |
| P350L | 1049C>T | 0.88 |
| E359K | 1075G>A | 1.12 |
| G523R | 1567G>A | 0.84 |
| G543E | 1628G>A | 1.07 |
| P401del2aa | 1201_1206 | 0.58 |
| W363Cdel5aa | 1089_1103del15 | 0.49 |
| E303Sfs247 | 907_907delG | 0.012 |
| T313fsX169 | 933_936dupACCC | 0.009 |
| 331KVENK to AVEAA | *(blank)* | 0.0115 |
| P401Afs144 | 1201_1216del16 | 0.014 |
| A401Sfs | *(blank)* | 0.023 |
| P432fs118 | 1293delC | 0.004 |
| Y455CfsX94 | 1364-1367del | 0.016 |
| H457Pfs93 | 1370delA | 0.006 |
| P465Rfs82 | 1392_1401del10 | 0.014 |
| P473HfsX77 | 1418delC | 0.015 |
| Q489RfsX60 | 1465delC | 0.05 |
| D528fs | *(blank)* | 0.12 |
| L529Wfs21 | 1584delC | 0.125 |
| Y617Cfs157 | 1850_1854del5 | 0.32 |
| Tyr637X | 1911C>A | 0.72 |

**Legend text present in the sheet (cells F28 and F29, verbatim):**
- "Dark/Medium Blue= benign validation controls"
- "Dark Red = pathogenic validation controls"

> **Source flag — legend not recoverable.** The legend is keyed to cell colour. Inspection of the workbook's style records shows the colouring is applied as *font* colour, and the only non-black colours present in the sheet are three blues (#00B0F0, #0070C0, #2E74B5). **No red font or fill colour exists anywhere in the worksheet.** The "Dark Red = pathogenic validation controls" mapping therefore cannot be reconstructed from the distributed file, and the blue shades cannot be reliably split into "dark" vs "medium" for the benign controls. The `LuciferaseAssay` sheet states 10 P/LP and 5 B/LB validation controls for this assay; those assignments are **not identifiable** from the distributed workbook. This has not been inferred.

> **Source typo flags (verbatim):** "505G.A" (period rather than `>`); "907_907delG" (single-base range); "1364-1367del" (hyphen rather than underscore); "P401del2aa" and "W363Cdel5aa" use a non-HGVS shorthand. Protein nomenclature is legacy 1-letter/mixed style throughout and is not HGVS p. notation.

---

### Appendix F — FOXN1 Corrections (transcribed from `FOXN1 Corrections.docx`)

Full document content, verbatim:

> **FOXN1**
>
> **PM1**
>
> **Original ACMG Summary**
>
> Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
>
> Caveat: Variant must not meet BS1, BS2, or BA1 criteria.
>
> **VCEP Specifications:**
>
> **Moderate Specification:**
>
> Applicable for variants in the DNA binding forkhead domain (amino acids 270-367), which is a well-established functional domain (Newman et al., 2020; PMID: 31914405) of FOXN1 with low tolerance for benign variation.
>
> Caveat: Variant must not meet BS1, BS2, or BA1 criteria.
>
> **Modification Type:**
>
> Gene-specific

**Is this amendment reflected in the specification's own tables? No — and it is contradicted by them.**

| Point | Corrections.docx | v2.3 specification tables |
|---|---|---|
| Caveat wording | "Variant must not meet BS1, **BS2**, or BA1 criteria" | "Caveat: Variant must not meet **BS1 or BA1** criteria" |
| Where the caveat appears | Twice — under Original ACMG Summary **and** under the Moderate Specification | Once — under "VCEP Specifications" only; removed from the Moderate strength row |

Both differences are precisely the two edits the v2.3 release notes describe as having been made ("Removed Caveat rule from Moderate strength"; "Removed the word 'BS2' from caveat text since it's 'not applicable' for this gene"). The Corrections document therefore predates v2.3 and is **stale**, not an erratum that overrides the tables. Additionally, citing BS2 in a PM1 caveat is internally incoherent for this gene, since BS2 is declared Not Applicable ("Does not apply due to reduced penetrance").

**Operative rule: the v2.3 specification table.** The PM1 caveat is "Variant must not meet BS1 or BA1 criteria", stated once, at the VCEP Specifications level.

---

## Internal Inconsistencies and Source Gaps

Recorded rather than reconciled, per source-fidelity requirements.

1. **`FOXN1 Corrections.docx` contradicts the v2.3 PM1 table** on both the BS2 mention and the duplicated caveat placement. See Appendix F. The spec table is operative; the correction sheet is stale.
2. **PM6 has no Very Strong row** in the specification, yet `PM6_VeryStrong` is a defined outcome in the distributed SVI table (Appendix C) and `PM6_Strong` appears in the Rules for Combining Criteria "Strong" code list. Whether PM6 can reach Very Strong for FOXN1 is not stated. Not specified by this VCEP.
3. **PVS1 has no Supporting strength row** in the specification's strength table, but `PVS1_Supp` is a terminal outcome of the Initiation Codon branch of the distributed flowchart (Appendix A), and `PVS1_Supporting` appears as a baseline code in the PS1 splicing table (Appendix B).
4. **PVS1 flowchart footnote markers a, b, d are undefined** anywhere in the distributed package (Appendix A).
5. **PP4 T-cell-count branch leaves 0.05x10^9/L exactly unassigned** (`<0.05` vs `>0.05`).
6. **PS3 worksheet color legend is unrecoverable** — the legend references a red category that does not exist in the file (Appendix E).
7. **PS3 Moderate study identification differs** between the specification (PMID: 37419334) and the worksheet ("mansucript in press", ScienceDirect link) (Appendix E).
8. **BS4 Strong** restates the generic ACMG caveat and supplies no VCEP-specific threshold or rule.
9. **PS3 assay bands 50–75%** are not assigned a call by the approved-assay worksheet.
10. **No Tavtigian-style point-based classification system** is present anywhere in this package. Classification uses the Richards et al., 2015 combining rules transcribed above.

---

## Version History

| Version | Date | Notes |
|---|---|---|
| 2.3 | 6/1/2026 | PM1 update: Removed Caveat rule from Moderate strength, but kept in VCEP specification. (It was previously listed in two places which was confusing.) Removed the word "BS2" from caveat text since it's 'not applicable' for this gene. Now reads "Caveat: Variant must not meet BS1 or BA1 criteria." |

Only the v2.3 release notes are carried in the distributed specification; earlier release notes are not included in this package.

---

*This document was compiled from the ClinGen VCEP specification and its distributed supplementary files. For the most current version, please refer to the ClinGen website.*
