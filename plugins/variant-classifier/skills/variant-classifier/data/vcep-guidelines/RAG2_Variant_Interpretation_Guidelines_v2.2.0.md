# ClinGen Severe Combined Immunodeficiency Disease VCEP Variant Interpretation Guidelines for RAG2

**Version:** 2.2
**Released:** 6/1/2026
**Affiliation:** Severe Combined Immunodeficiency Disease VCEP
**Type:** Richards et.al., 2015 - Combining rules
**DOI:** 10.5281/zenodo.21434510
**Source basis:** ClinGen Criteria Specification Registry entry GN124, "ClinGen Severe Combined Immunodeficiency Disease Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for RAG2 Version 2.2", plus the eight supplementary files distributed with it (see [Appendices](#appendices) for the full inventory).

> **Scope note.** Everything below is transcribed from the RAG2 v2.2 specification package. Where the VCEP delegates to external guidance (e.g. ClinGen SVI recommendations) the delegation is reproduced as written, together with the SVI document the VCEP actually distributed. Where the VCEP says nothing, this document says **"Not specified by VCEP"** rather than supplying generic ACMG/AMP content.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | RAG2 (HGNC:9832) |
| **HGNC Name** | recombination activating 2 |
| **Transcript** | NM_000536.4 (MANE Select) |
| **Disease** | recombinase activating gene 2 deficiency (MONDO:0000573) |
| **Inheritance** | Autosomal recessive inheritance |

**Keywords (as registered):** human biology genomics variant variant classification clingen disease standards RAG2 NM_000536.4 Autosomal recessive inheritance recombinase activating gene 2 deficiency

**Rights holder:** The Clinical Genome Resource (ClinGen)
**Research group:** Severe Combined Immunodeficiency Disease VCEP

---

## Release Notes for Version 2.2 (verbatim)

> Edited Rules for Combining Criteria to reflect standard combinations plus (A) 1 very strong + 1 supporting = Likely Pathogenic and (B) 1 Strong Benign = Likely Benign.
>
> Refreshed and saved Rules for Combining Criteria.
>
> Uploaded two files to address minor PM3 changes:
>
> 1. "PM3 Criterion: October 2025 Version, Minor Updates"
> 2. "PM3: svi recommendations: October 2025 Group Responses to Minor Updates"
>
> Uploaded RAG2 corrections
>
> - Changes to PS3
> - Changes to PM1
> - Edited PP4 criteria.
> - Added BS2_Strong strength
> - Added text to BS2_Supporting

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
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Frequency Threshold Summary](#frequency-threshold-summary)
5. [Appendices](#appendices)
6. [Source Issues, Typos and Internal Inconsistencies](#source-issues-typos-and-internal-inconsistencies)
7. [Version History](#version-history)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats: Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7). Use caution interpreting LOF variants at the extreme 3' end of a gene. Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact. Use caution in the presence of multiple transcripts.

**VCEP Specifications:**

- Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with two modifications:
  - Given that the *RAG2* protein is encoded by a single exon (based on MANE Select transcript NM_000536.4) and nonsense-mediated decay is not predicted for nonsense or frameshift variants, PVS1 cannot be applied at the default strength to RAG2 variants (indicated by the red boxes in attached flow chart), except in the case of a full gene deletion or removing/altering critical domain (PHD domain **and** core domain)(indicated by the purple boxes in attached flow chart).
- PVS1 can be applied to variants not predicted to undergo nonsense-mediated decay but removing/altering the critical PHD domain (spanning amino acids 414-487) and core domain (amino acids 1-383) based on recommendations from Walker et. al., preprint (see attached flow chart).
- Strength modification for variants predicted to remove >10% of the protein (see attached flow chart).
- For variants not predicted to undergo nonsense-mediated decay, at least one pathogenic variant must be present downstream in order to apply PVS1_Strong.
- The PHD domain (spanning amino acids 414-487) is defined as a region critical to protein function (PMID: 15964836).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with two specifications: (1) Given that the *RAG2* protein is encoded by a single exon (based on MANE Select transcript NM_000536.4) and nonsense-mediated decay is not predicted for nonsense or frameshift variants, PVS1 cannot be applied at the default strength to RAG2 variants (indicated by the red boxes in the Flowchart), **except** in the case of full gene deletion **or** removing/altering critical domain: the PHD domain and core domain (indicated by the purple boxes in the Flowchart). (2) PVS1 can be applied to variants not predicted to undergo nonsense-mediated decay when removing/altering the critical PHD domain (spanning amino acids 414-487) and core domain (amino acids 1-383) based on recommendations from Walker et al., preprint. *(Modification Type: General recommendation, Gene-specific)* |
| **Strong** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification: For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein, at least one pathogenic variant **must be** present downstream in order to apply PVS1_Strong. *(Modification Type: General recommendation, Gene-specific)* |
| **Moderate** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification: For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein, when at least one pathogenic variant is **not** present downstream, downgrade to PVS1_Moderate. *(Modification Type: General recommendation)* |
| **Supporting** | Not specified as a standalone strength row in the specification. (PVS1_Supp appears only as an outcome of the Initiation Codon branch of the RAG2 PVS1 flowchart - see [Appendix A](#appendix-a---rag2-pvs1-decision-flowchart-file-pvs1pdf).) |

The gene-specific decision tree is transcribed in full in [Appendix A](#appendix-a---rag2-pvs1-decision-flowchart-file-pvs1pdf).

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T. Applicable if the previously established variant is classified as **pathogenic** by SCID VCEP specifications for *RAG2*. *(Modification Type: Gene-specific)* |
| **Moderate** | It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be likely pathogenic, can use PS1 for c.105+1G>T. Applicable if the previously established variant is classified as **likely pathogenic** by SCID VCEP specifications for *RAG2*. *(Modification Type: Gene-specific, Strength)* |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

The following guidelines should be used when determining the phenotypic consistency of each proband:

- "Phenotype highly specific for gene" proband must meet at least PP4_Moderate criteria;
- "Phenotype consistent with gene but not highly specific" proband must meet PP4 criteria;
- "Phenotype consistent with gene but not highly specific and high genetic heterogeneity": proband has been asserted to have a SCID phenotype but does not meet PP4 criteria;
- Reduce points per proband by half if the phase is unconfirmed.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *(Modification Type: General recommendation, Gene-specific)* |
| **Strong** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *(Modification Type: General recommendation, Gene-specific)* |
| **Moderate** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *(Modification Type: General recommendation, Gene-specific)* |
| **Supporting** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *(Modification Type: General recommendation, Gene-specific)* |

The VCEP does **not** publish its own PS2/PM6 point matrix. It maps the SVI phenotypic-consistency tiers onto RAG2 PP4 thresholds (above) and defers all point values and strength thresholds to the SVI *de novo* recommendation distributed with the package, transcribed in [Appendix B](#appendix-b---svi-recommendation-for-de-novo-criteria-ps2--pm6-version-11-file-ps2_pm6pdf).

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | PS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and recapitulating the RAG2-SCID phenotype. *(Modification Type: Gene-specific)* |
| **Moderate** | Strength of evidence from cellular models/*in vitro* studies is dependent upon abnormal result in a V(D)J recombination assay: **PS3_Moderate: <25% of wild-type activity in Tirosh et al., 2019 (PMID: 29772310)** *(Modification Type: Gene-specific, Strength)* |
| **Supporting** | Strength of evidence from cellular models/*in vitro* studies is dependent upon abnormal result in a V(D)J recombination assay: **PS3_Supporting: 25-60% of wild-type activity in Tirosh et al., 2019 (PMID: 29772310) OR Reduced activity compared to wild type in Couëdel et al., 2010 (PMID: 20234091)** *(Modification Type: Gene-specific, Strength)* |

**Additional requirement stated only in the "RAG2 Corrections 1.6.26" erratum (NOT present in the v2.2 specification tables above):**

> At least one previously observed proband with the expressed RAG2 variant meeting PP4 is required to apply PS3 at any strength.

The erratum places this sentence in both the Moderate and the Supporting specification blocks. The v2.2 registry tables reproduced above do not contain it. See [Source Issues](#source-issues-typos-and-internal-inconsistencies).

#### Approved Assay Instances

Approved/not-approved status, assay design, controls and thresholds are transcribed in [Appendix E](#appendix-e---scid-vcep-ps3bs3-functional-evidence-workbook-file-scid-vcep-ps3_bs3xlsx).

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance. Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** **Not Applicable.** (No comment provided by the VCEP.)

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** Caveat: variant must not meet BS1, BS2, or BA1 criteria.

| Strength | Criteria |
|----------|----------|
| **Moderate** | Strength is dependent upon the location of the variant within specific functional domains (PMID: 26996199): **PM1_Moderate: missense variant located in the PHD domain (amino acids 414-487);** Caveat: variant must not meet BS1, BS2, or BA1 criteria. *(Modification Type: Gene-specific)* |
| **Supporting** | Strength is dependent upon the location of the variant within specific functional domains (PMID: 26996199): **PM1_Supporting: missense variant located in the core domain (amino acids 1-383);** Caveat: variant must not meet BS1, BS2, or BA1 criteria. *(Modification Type: Gene-specific)* |

The "RAG2 Corrections 1.6.26" erratum reproduces this PM1 text identically; the erratum is fully reflected in the v2.2 tables.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | gnomAD popmax filtering allele frequency **<0.0000588** (strict less-than). An additional requirement is that **no homozygotes** have been observed in gnomAD. *(Modification Type: Gene-specific)* |

No Moderate (default) strength is offered; PM2 is available at Supporting only.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

Use ClinGen SVI adapted recommendations for *in trans* criterion (see PM3 Criterion attached below) with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for *RAG2*.

Caveat: All variants should be sufficiently rare (meet PM2 specification). The applicability of PM3 to suspected founder variants with allele frequencies exceeding the PM2 threshold will be evaluated on a case-by-case basis by the VCEP.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI adapted recommendations for *in trans* criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for *RAG2*. *(Modification Type: General recommendation, Strength)* |
| **Strong** | Same text as above. *(Modification Type: General recommendation, Strength)* |
| **Moderate** | Same text as above. *(Modification Type: General recommendation, Strength)* |
| **Supporting** | Same text as above. *(Modification Type: General recommendation, Strength)* |

The point system referenced is the SVI PM3 recommendation (Table 1 updated 17 October 2025) distributed with this package - transcribed in [Appendix C](#appendix-c---svi-recommendation-for-in-trans-criterion-pm3-version-10-file-pm3-criterionpdf). The VCEP's own commentary on the October 2025 amendments is in [Appendix D](#appendix-d---pm3-minor-amendments-scid-vcep-responses-file-pm3-minor-amendmentsdocx).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | When applied to deletion variants, the deleted region must contain a known **pathogenic** or **likely pathogenic** variant that is not predicted/observed to alter splicing. *(Modification Type: Gene-specific)* |
| **Supporting** | When applied to deletion variants, the deleted region must contain a known **VUS** variant that is not predicted/observed to alter splicing. *(Modification Type: Gene-specific, Strength)* |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

For nonsense variants:

**PM5_Strong** - PM5 may be applied at a Strong level of evidence for any nonsense variant with 4+ points from informative variants (see below point table). PM5_Strong should be downgraded to PM5_Moderate if PVS1 is applied at any strength.

**PM5_Moderate** - PM5 may also be applied at a Moderate level of evidence for any nonsense variant with 2+ points from informative variants (see below point table). PM5_Moderate may not be combined with PVS1_VeryStrong (should be downgraded to PM5_Supporting if PVS1_VeryStrong is applied).

**PM5_Supporting** - Also applicable to a nonsense variant with 1 point from an informative variant (see point table). Informative variants must also be classified by these rule specifications.

#### PM5 nonsense point table (source-defined)

| Type of variant under assessment (VUA) | Informative variant | Score |
|---|---|---|
| Nonsense variant predicted to lead to NMD | P/LP variant in the exon of DNA change predicted to lead to NMD | +1pt |
| Nonsense variant predicted to lead to NMD | B/LB variant in the exon predicted to lead to NMD | -2pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | P/LP variant resulting in a PTC in the same exon but downstream of VUA | +1pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | B/LB variant resulting in PTC in the same exon but upstream of the VUA | -2pt |

NMD = nonsense-mediated decay; PTC premature termination codon *(source punctuation preserved - no colon or "=" after "PTC")*.

**Note (verbatim, repeated by the VCEP under each strength):** The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet "+1 pathogenic variant downstream" on the PVS1 flowchart. If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA. The VUA must be sufficiently rare, meet PM2_Supporting, to apply this point system. If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic without use of PM5 and without use of only PVS1 plus PM2.

| Strength | Criteria |
|----------|----------|
| **Strong** | PM5 may be applied at a Strong level of evidence for any nonsense variant with 4+ points from informative variants. PM5_Strong should be downgraded to PM5_Moderate if PVS1 is applied at any strength. *(Modification Type: General recommendation, Strength)* |
| **Moderate** | Applicable at default strength (PM5) if previously established variant is classified as pathogenic or at reduced strength of PM5_Supporting if previously established variant is classified as likely pathogenic. PM5 may also be applied at a Moderate level of evidence for any nonsense variant with 2+ points from informative variants. PM5_Moderate may not be combined with PVS1_VeryStrong (should be downgraded to PM5_Supporting if PVS1_VeryStrong is applied). *(Modification Type: General recommendation, Strength)* |
| **Supporting** | Applicable at default strength (PM5) if previously established variant is classified as pathogenic or at reduced strength of PM5_Supporting if previously established variant is classified as likely pathogenic. Also applicable to a nonsense variant with 1 point from an informative variant (see point table). Informative variants must also be classified by these rule specifications. *(Modification Type: General recommendation, Strength)* |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

The following guidelines should be used when determining the phenotypic consistency of each proband:

- "Phenotype highly specific for gene" proband must meet at least PP4_Moderate criteria;
- "Phenotype consistent with gene but not highly specific" proband must meet PP4 criteria;
- "Phenotype consistent with gene but not highly specific and high genetic heterogeneity": proband has been asserted to have a SCID phenotype but does not meet PP4 criteria;
- Reduce points per proband by half if the phase is unconfirmed.

| Strength | Criteria |
|----------|----------|
| **Strong** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *(Modification Type: General recommendation, Gene-specific)* |
| **Moderate** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *(Modification Type: General recommendation, Gene-specific)* |
| **Supporting** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *(Modification Type: General recommendation, Gene-specific)* |

PM6 has no Very Strong row in the RAG2 v2.2 specification (PS2 does). See [Appendix B](#appendix-b---svi-recommendation-for-de-novo-criteria-ps2--pm6-version-11-file-ps2_pm6pdf) for the SVI point system the VCEP defers to.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386) with the additional specification that unaffected individuals contributing to the calculated LOD score **(Attached document: PP1 specifications)** must be heterozygous carriers of one of the variants observed in the affected individuals (i.e. do not count wild-type/wild-type, individuals).

*Source punctuation preserved: the stray comma in "wild-type/wild-type, individuals" is as written.*

| Strength | Criteria |
|----------|----------|
| **Strong** | Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations. *(Modification Type: General recommendation)* |
| **Moderate** | Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations. *(Modification Type: General recommendation)* |
| **Supporting** | Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations. *(Modification Type: General recommendation)* |

LOD-score thresholds and the autosomal-recessive segregation lookup table are transcribed in [Appendix F](#appendix-f---pp1-segregation-recommendations-oza-et-al-tables-4a-and-4b-file-pp1pdf). RAG2 is autosomal recessive, so Table 4b governs.

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable.** Comment: "Does not apply. The gnomAD v2.1.1 missense Z score for RAG2 (Z = 0.2) suggests this gene is not constrained for missense variation. Both benign and pathogenic missense variants are present in RAG2."

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Only applicable to synonymous or intronic variants predicted to impact splicing by SpliceAI with a delta score **greater than or equal to 0.2** (inclusive). **Do not apply to missense variants.** *(Modification Type: General recommendation)* |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

PP4 applicability and strength is determined by the total points accumulated by a single affected individual according to the table below and the following total point ranges:

| Total points | Outcome |
|---|---|
| **<1 Point** (strict) | PP4 not met |
| **1 - <2 Points** (lower bound inclusive, upper bound strict) | PP4 |
| **≥2 - <4 Points** (lower bound inclusive, upper bound strict) | PP4_Moderate |
| **≥4 Points** (inclusive) | PP4_Strong<sup>1</sup> |

#### PP4 evidence point table

| Evidence Description | Points |
|---|---|
| Diagnostic criteria met for SCID (Criteria 1 and 3 or Criterion 4 by itself) or Leaky SCID/Omenn syndrome (excluding Criterion 2)<sup>1</sup> | 0.5 |
| SCID gene panel or exome/genome sequencing conducted (only applicable if genetic testing did not provide an alternative genetic explanation for SCID/Leaky SCID/Omenn syndrome phenotype) | 1 |
| Family history of SCID (only applicable if SCID gene panel or exome/genome sequencing was conducted on proband and did not provide an alternative genetic explanation for phenotype) | 0.5 |
| Decreased presence of TCRVα7.2 (<2%) in CD3+ T lymphocytes and/or mucosa-associated invariant T-cells demonstrated by flow cytometry AND pathogenic or likely pathogenic variants in RAG1 and DCLRE1C have been excluded PMID: 39792639 | 1.5 |
| Decreased presence of TCRVα7.2 (<2%) in CD3+ T lymphocytes and/or mucosa-associated invariant T-cells demonstrated by flow cytometry AND pathogenic or likely pathogenic variants in RAG1 and DCLRE1C have **NOT** been excluded PMID: 39792639 | 0.5 |
| Increased presence of 9G4+ (>10%), 9G4int (>5%) or 9G4hi (>5%) cells in CD19+ B cells demonstrated by flow cytometry AND pathogenic or likely pathogenic variants in RAG1 have been excluded PMID: 39792639 | 1 |
| Increased presence of 9G4+ (>10%), 9G4int (>5%) or 9G4hi (>5%) cells in CD19+ B cells demonstrated by flow cytometry AND pathogenic or likely pathogenic variants in RAG1 have **NOT** been excluded PMID: 39792639 | 0.5 |
| SCID phenotype corrected by RAG2 gene therapy | 4 |
| T-B-NK+ lymphocyte subset profile* (See notes) | 0.5 |

<sup>1</sup> The diagnostic criteria should follow the PIDTC 2022 specification, summarized [here] (hyperlink in source; target URL not exposed in the distributed PDF text).

*Notes: 1) If NK cells are not noted or are present, criteria may still be applied if SCID gene panel or exome/genome sequencing has ruled out alternative causes; 2) If maternal T cells are present, the T lymphocyte profile is still considered to be T- (autologous T cells are absent).

All flow-cytometry comparators above are **strict** (`<2%`, `>10%`, `>5%`).

| Strength | Criteria |
|----------|----------|
| **Strong** | A patient score of ≥ 4 points. *(Modification Type: Disease-specific, Gene-specific)* |
| **Moderate** | A patient score of ≥2-<4 points (see instructions below). *(Modification Type: Disease-specific, Gene-specific)* |
| **Supporting** | A patient score of 1-<2 points (see instructions below). *(Modification Type: Disease-specific, Gene-specific)* |

**Additional requirement stated only in the "RAG2 Corrections 1.6.26" erratum (NOT present in the v2.2 specification tables or in the distributed PP4 table PDF):**

> **Strong** - A patient score of ≥ 4 points<sup>1</sup>.
> <sup>1</sup>CNV (Copy number variation) testing is required to consider PP4_Strong in order to certify that the variant in question is the causative for the phenotype and not one CNV event corrected by gene therapy and not identified previously (see instructions below).

This resolves the dangling superscript "1" on "≥4 points: PP4_Strong<sup>1</sup>" that appears in both the registry entry and the PP4 PDF without a matching footnote. See [Source Issues](#source-issues-typos-and-internal-inconsistencies).

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable.** "This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee." (PubMed: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:**

Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:

- Prevalence: 1:5,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.19 (based on the contribution of *RAG2* variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 19.2% rounded to 19%)
- Penetrance: 50%

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | gnomAD popmax filtering allele frequency **>0.00872** (strict greater-than). *(Modification Type: Gene-specific)* |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

gnomAD popmax filtering allele frequency **>0.00195**<sup>1</sup>

Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:

- Prevalence: 1:50,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.19 (based on the contribution of *RAG2* variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 19.2% rounded to 19%)
- Penetrance: 100%

<sup>1</sup> Consider also bottleneck populations.

| Strength | Criteria |
|----------|----------|
| **Strong** | gnomAD popmax filtering allele frequency **>0.00195**<sup>1</sup> (strict greater-than). <sup>1</sup> Consider also bottleneck populations. *(Modification Type: Gene-specific)* |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | BS2_Strong: Can be applied at Strong level if observed in **at least 3 homozygotes** (inclusive). *(Modification Type: Strength)* |
| **Supporting** | Only to be used when the variant is observed in the homozygous state in a healthy adult. BS2_Supporting: Can be applied at Supporting level if observed in **at least 1 homozygote** (inclusive). *(Modification Type: Strength)* |

The "RAG2 Corrections 1.6.26" erratum reproduces this BS2 text identically; the erratum is fully reflected in the v2.2 tables.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** **Not Applicable.** Comment: "There is not a well-established functional study which can rule out all damaging effects on protein function."

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Can be applied without additional specifications. *(Modification Type: General recommendation, None)* |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | "Does not apply." |
| **BP2** | Not Applicable | No comment provided. |
| **BP3** | Not Applicable | "Does not apply." |
| **BP4** | Not Applicable | No comment provided. |
| **BP5** | Not Applicable | No comment provided. |
| **BP6** | Not Applicable | "This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee." (PubMed: 29543229) |
| **BP7** | **Applicable - Supporting** | Applicable to both synonymous variants and deep intronic variants affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions. The variant should be predicted not to impact splicing by at least two out of three *in silico* tools (freely available tools include GeneSplicer, MaxEntScan, NNSplice, SpliceAI, Splicing Sequences Finder (SSF), and varSEAK). Given the potential for poor conservation of genes related to T cell and B cell development among vertebrates, nucleotide conservation is **not required** in order to apply BP7. *(Modification Type: General recommendation)* |

*Source note preserved: BP7 says "at least two out of three in silico tools" but then lists six tools.*

---

## Rules for Combining Criteria

Transcribed verbatim from the v2.2 registry entry. Parenthesised lists are the criterion codes the VCEP assigns to each strength tier.

### Pathogenic

| # | Rule |
|---|---|
| 1 | **1 Very Strong** (PVS1, PS2_Very Strong, PM3_Very Strong) **AND ≥ 1 Strong** (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong) |
| 2 | **1 Very Strong** (PVS1, PS2_Very Strong, PM3_Very Strong) **AND ≥ 2 Moderate** (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate) |
| 3 | **1 Very Strong** (PVS1, PS2_Very Strong, PM3_Very Strong) **AND 1 Moderate** (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate) **AND 1 Supporting** (PS2_Supporting, PS3_Supporting, PM1_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
| 4 | **1 Very Strong** (PVS1, PS2_Very Strong, PM3_Very Strong) **AND ≥ 2 Supporting** (PS2_Supporting, PS3_Supporting, PM1_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
| 5 | **≥ 2 Strong** (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong) |
| 6 | **1 Strong** (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong) **AND ≥ 3 Moderate** (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate) |
| 7 | **1 Strong AND 2 Moderate AND ≥ 2 Supporting** (same code lists as above) |
| 8 | **1 Strong AND 1 Moderate AND ≥ 4 Supporting** (same code lists as above) |

### Likely Pathogenic

| # | Rule |
|---|---|
| 1 | **1 Very Strong** (PVS1, PS2_Very Strong, PM3_Very Strong) **AND 1 Moderate** (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate) |
| 2 | **1 Strong** (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong) **AND 1 Moderate** (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate) |
| 3 | **1 Strong AND ≥ 2 Supporting** (PS2_Supporting, PS3_Supporting, PM1_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
| 4 | **≥ 3 Moderate** (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate) |
| 5 | **2 Moderate AND ≥ 2 Supporting** |
| 6 | **1 Moderate AND ≥ 4 Supporting** |
| 7 | **1 Strong AND 2 Moderate** |
| 8 | **1 Very Strong** (PVS1, PS2_Very Strong, PM3_Very Strong) **AND 1 Supporting** (PS2_Supporting, PS3_Supporting, PM1_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |

*(Rule 8 is change (A) announced in the v2.2 release notes.)*

### Benign

| # | Rule |
|---|---|
| 1 | **≥ 2 Strong** (BS1, BS2, BS4) |
| 2 | **1 Stand Alone** (BA1) |

### Likely Benign

| # | Rule |
|---|---|
| 1 | **≥ 2 Supporting** (BS2_Supporting, BP7) |
| 2 | **1 Strong** (BS1, BS2, BS4) |

*(Rule 2 is change (B) announced in the v2.2 release notes.)*

Note: the Likely Pathogenic table as published contains a duplicate-in-substance pair (rule 2 "1 Strong AND 1 Moderate" and rule 7 "1 Strong AND 2 Moderate"); both are reproduced as printed.

---

## Frequency Threshold Summary

| Criterion | Metric | Threshold | Comparator | Additional requirement |
|---|---|---|---|---|
| **BA1** (Stand Alone) | gnomAD popmax filtering allele frequency | 0.00872 | **> (strict)** | Derived from Whiffin/Ware: prevalence 1:5,000; allelic het. 1; genetic het. 0.19; penetrance 50% |
| **BS1** (Strong) | gnomAD popmax filtering allele frequency | 0.00195 | **> (strict)** | Consider also bottleneck populations. Derived from Whiffin/Ware: prevalence 1:50,000; allelic het. 1; genetic het. 0.19; penetrance 100% |
| **PM2** (Supporting) | gnomAD popmax filtering allele frequency | 0.0000588 | **< (strict)** | **No homozygotes** observed in gnomAD |
| **BS2** (Strong) | homozygote count in healthy adults | 3 | **≥ (inclusive, "at least 3")** | - |
| **BS2** (Supporting) | homozygote count in healthy adults | 1 | **≥ (inclusive, "at least 1")** | Homozygous state in a healthy adult |
| **PP3** (Supporting) | SpliceAI delta score | 0.2 | **≥ (inclusive)** | Synonymous or intronic variants only; do not apply to missense |
| **PS3_Moderate** | % wild-type V(D)J activity (Tirosh 2019) | 25% | **< (strict)** | - |
| **PS3_Supporting** | % wild-type V(D)J activity (Tirosh 2019) | 25-60% | range as printed (bounds not qualified in source) | OR reduced activity vs wild type in Couëdel 2010 |
| **PVS1** | proportion of protein removed | 10% | **>** for the strength-modification branch; **<** for the downgrade branch (source uses `<10%`, not `≤10%`) | - |
| **PP4** | TCRVα7.2 in CD3+ T lymphocytes | 2% | **< (strict)** | - |
| **PP4** | 9G4+ cells in CD19+ B cells | 10% | **> (strict)** | - |
| **PP4** | 9G4int / 9G4hi cells in CD19+ B cells | 5% | **> (strict)** | Both subsets carry the same 5% threshold in the source |

---

## Appendices

### Supplementary file inventory (9 files distributed; all 9 opened and read)

| # | File | Type | Opened? | Transcribed in |
|---|---|---|---|---|
| 1 | ClinGen_ACMG_Specifications_RAG2_v2.2.pdf (20 pp) | PDF | Yes | Main body of this document |
| 2 | PVS1.pdf ("Specified PVS1 flowchart", 1 p) | PDF | Yes | Appendix A |
| 3 | PS2_PM6.pdf ("SVI recommendations for de novo criteria", 2 pp) | PDF | Yes | Appendix B |
| 4 | PM3 Criterion.pdf ("October 2025 Version, Minor Updates", 2 pp) | PDF | Yes | Appendix C |
| 5 | PM3 Minor Amendments.docx | DOCX (25 paragraphs, 1 table, 1 embedded PNG) | Yes | Appendix D |
| 6 | SCID VCEP PS3_BS3.xlsx ("Functional Evidence (RAG2)") | XLSX (3 sheets) | Yes | Appendix E |
| 7 | PP1.pdf ("PP1 specifications", 2 pp) | PDF | Yes | Appendix F |
| 8 | PP4 - RAG2.pdf ("2025 updates", 1 p) | PDF | Yes | Appendix G |
| 9 | RAG2 Corrections 1.6.26.docx | DOCX (63 paragraphs, 1 table, no images) | Yes | Appendix H |

`GN124_data.json` is download metadata, not source material, and is excluded.

---

### Appendix A - RAG2 PVS1 decision flowchart (file: PVS1.pdf)

Single-page gene-specific adaptation of the SVI PVS1 decision tree. Colour legend as used by the VCEP: **red-X boxes** = default-strength PVS1 outcome that RAG2 *cannot* use (single-exon gene, NMD not predicted); **magenta/purple boxes** = PVS1 outcomes reached via the critical-domain branch; **yellow boxes** = the RAG2 critical-domain decision node; **orange-outlined group** = the LoF-frequency / percent-of-protein sub-tree.

The recurring yellow decision node reads, in all five places it appears:

> Truncated/altered region is critical to protein function - The PHD domain (spanning amino acids 414-487) and core domain (amino acids 1-383) are defined as a region critical to protein function.

**Branch 1 - Nonsense or Frameshift**

| Path | Outcome |
|---|---|
| Predicted to undergo NMD <sup>b</sup> → Exon is present in biologically-relevant transcript(s) | PVS1 — **marked with red X (not usable for RAG2)** |
| Predicted to undergo NMD <sup>b</sup> → Exon is absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD <sup>b</sup> → Truncated/altered region is critical to protein function (yellow node) | **PVS1** (magenta) |
| Not predicted to undergo NMD → Role of region unknown → LoF variants in this exon are frequent in the general population and/or exon absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD → Role unknown → LoF not frequent and exon present → Variant removes >10% of protein → 1+ pathogenic variant present downstream | **PVS1** (magenta) — *see inconsistency note below* |
| … → Variant removes >10% of protein → No known downstream pathogenic variants | PVS1_Moderate |
| … → Variant removes <10% of protein | PVS1_Moderate |

**Branch 2 - GT--AG 1,2 splice sites <sup>a</sup>**

| Path | Outcome |
|---|---|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD <sup>b</sup> → Exon present in biologically-relevant transcript(s) | PVS1 — **red X (not usable for RAG2)** |
| … → Exon absent from biologically-relevant transcript(s) | N/A |
| Exon skipping/cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD <sup>b</sup> → critical-to-function node (yellow) | **PVS1** (magenta) |
| … → Role unknown → LoF frequent and/or exon absent | N/A |
| … → Role unknown → LoF not frequent and exon present → removes >10% → 1+ pathogenic variant present downstream | PVS1_Strong |
| … → removes >10% → No known downstream pathogenic variants | PVS1_Moderate |
| … → removes <10% of protein | PVS1_Moderate |
| Exon skipping or use of a cryptic splice site preserves reading frame → critical-to-function node (yellow) | **PVS1** (magenta) |
| … → Role unknown → LoF frequent and/or exon absent | N/A |
| … → Role unknown → LoF not frequent and exon present → removes >10% → 1+ pathogenic variant present within deleted region | PVS1_Strong |
| … → removes >10% → No known pathogenic variants within deleted region | PVS1_Moderate |
| … → removes <10% of protein | PVS1_Moderate |

**Branch 3 - Deletion (single exon to full gene)**

| Path | Outcome |
|---|---|
| Full gene deletion | PVS1 <sup>d</sup> |
| Single to multi exon deletion - disrupts reading frame and is predicted to undergo NMD <sup>b</sup> → Exon present in biologically-relevant transcript(s) | PVS1 — **red X (not usable for RAG2)** |
| … → Exon absent from biologically-relevant transcript(s) | N/A |
| Single to multi exon deletion - disrupts reading frame and is NOT predicted to undergo NMD <sup>b</sup> → critical-to-function node (yellow) | **PVS1** (magenta) |
| … → Role unknown → LoF frequent and/or exon absent | N/A |
| … → Role unknown → LoF not frequent and exon present → removes >10% → 1+ pathogenic variant present within deleted region | PVS1_Strong |
| … → removes >10% → No known pathogenic variants within deleted region | PVS1_Moderate |
| … → removes <10% of protein | PVS1_Moderate |
| Single to multi exon deletion - preserves reading frame → critical-to-function node (yellow) | **PVS1** (magenta) |

**Branch 4 - Duplication (≥1 exon in size and must be completely contained within gene)**

| Path | Outcome |
|---|---|
| Proven in tandem → Reading frame disrupted and NMD predicted to occur | PVS1 — **red X (not usable for RAG2)** |
| Proven in tandem → No or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem → Reading frame presumed disrupted and NMD predicted to occur | PVS1_Strong |
| Proven not in tandem | N/A |

**Branch 5 - Initiation Codon**

| Path | Outcome |
|---|---|
| No known alternative start codon in other transcripts → ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon | PVS1_Moderate |
| No known alternative start codon in other transcripts → No pathogenic variant(s) upstream of closest potential in-frame start codon | PVS1_Supp |
| Different functional transcript uses alternative start codon | N/A |

**Unreadable/absent content:** the flowchart carries superscript footnote markers **a**, **b** and **d**, but the distributed one-page PDF contains **no footnote legend** defining them. Their definitions are not recoverable from the package and are not supplied here.

---

### Appendix B - SVI Recommendation for de novo Criteria (PS2 & PM6) Version 1.1 (file: PS2_PM6.pdf)

*ClinGen Sequence Variant Interpretation Working Group. Date Approved: March 18, 2018, updated May 5, 2021. Changes from v1: Clarified that confirmed/assumed is with regards to parental relationships and not de novo status.*

This is the general SVI document; it is **not** a RAG2-specific point matrix. The SCID VCEP distributes it unmodified and adds only the phenotypic-consistency mapping shown under [PS2](#ps2---de-novo-confirmed) / [PM6](#pm6---de-novo-assumed).

**Table 1. Points* awarded per de novo occurrence**

| Phenotypic consistency | de novo with confirmed parental relationships | de novo with unconfirmed parental relationships |
|---|---|---|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity** | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

\* Note that these points are *not* equivalent to the points used to classify a variant per the Tavtigian et al 2020 "Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines"
\*\* Maximum allowable value of 1 may contribute to overall score

**Table 2. Recommendation for determining the appropriate ACMG/AMP evidence strength level for de novo occurrence(s)**

| Supporting (PS2_Supporting or PM6_Supporting) | Moderate (PS2_Moderate or PM6) | Strong (PS2 or PM6_Strong) | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |
|---|---|---|---|
| 0.5 | 1 | 2 | 4 |

**Additional considerations for applying de novo criteria based on inheritance (verbatim):**

- Conditions with X-linked inheritance: if the variant occurs *de novo* in an unaffected carrier mother, and family history is consistent - i.e., she has no affected brothers/other male relatives apart from her affected son(s) - *de novo* criteria may be applied despite the fact that she is unaffected.
- **Autosomal recessive conditions: for a de novo occurrence in a gene associated with a condition inherited in an autosomal recessive pattern without an additional pathogenic/likely pathogenic variant identified, the strength of evidence should be decreased by one level.** *(directly relevant - RAG2 is autosomal recessive)*
- Mosaicism: for cases with apparent germline mosaicism (multiple affected siblings with both parents negative for the variant), parental relationships must be confirmed in order for *de novo* criteria to apply.

Worked examples in the source (SIK1, ASH1L, NIPBL) are illustrative only and are not reproduced.

---

### Appendix C - SVI Recommendation for in trans Criterion (PM3) Version 1.0 (file: PM3 Criterion.pdf)

*ClinGen Sequence Variant Interpretation Working Group. Date Approved: May 2, 2019; **Table 1 updated October 17, 2025**.*

**SVI revision to PM3:** For recessive disorders, detected in trans with a pathogenic *or likely pathogenic* variant *in an affected patient*.

**Table 1. Points awarded per in trans proband** (October 2025 version, as adopted by the SCID VCEP)

| Classification/Zygosity of other variant | Confirmed in trans | Phase unknown |
|---|---|---|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence, Non-consanguineous** *(no max)* | 1.0 | 1.0 |
| Homozygous occurrence, Consanguineous** *(no max)* | 0.5 | 0.5 |
| Uncertain significance variant *(max point 0.5)* | 0.25 | 0 |

Column header in the October 2025 version: **"Points per Proband-Family*"** (changed from "Points per Proband").

\* Multiple probands from separate nuclear families that are later found to have identity-by-descent should only be counted once.
\*\* When consanguinity is not known or reported: if family IS NOT from a bottlenecked population (as defined by gnomAD), assume non-consanguinity; otherwise, assume consanguinity. If genetic ancestry of the family cannot be determined, assume consanguinity.

**Table 2. Recommendation for determining the appropriate evidence strength level for PM3**

| PM3_Supporting | PM3 | PM3_Strong | PM3_VeryStrong |
|---|---|---|---|
| 0.5 | 1.0 | 2.0 | 4.0 |

**Considerations (verbatim):**

- **Allele Frequency** - Application of PM3 is contingent on the allele frequency of the variant being assessed and the variant presumably on the other allele both being sufficiently rare (meets PM2 threshold). This contingency is to avoid incorrect application of PM3 to high frequency variants that are likely to occur in trans with P/LP variants based on frequency.
- **Phasing** - If the phase cannot be determined, it is recommended that at least two different LP/P variants (depending on classifications) are needed to equal the weight of one LP/P co-occurrence confirmed in trans.
  - In confirmation of phasing, if only one parent is tested and found to carry one allele, variants can be counted as in trans. (PAH c.601C>T / c.734T>C example given in source.)
- **Classification** - Probands should be weighted less when the variant on the other allele is of uncertain significance and rare (meets PM2); however, weight may vary by gene size as larger genes are more likely to have a second variant by chance (default 0.25 points). If the variant on the other allele is classified as P or LP, weighting depends on phasing (see *Phasing* above), with P/LP being weighted equally if confirmed in trans and different point values per proband if phasing is unknown (0.5 points and 0.25 points, respectively). To avoid circularity, in all instances (phasing confirmed or unknown), the classification of the variant on the other allele should not use evidence from the variant being interrogated.
- **Homozygous occurrences** - For homozygous occurrences, the default weight is dropped to 0.5 points, as a rare homozygous occurrence may be due to consanguinity. **A recommended max of 1.0 points of all homozygous cases is suggested** to prevent overclassification of homozygous occurrences in the absence of additional data. *(This sentence conflicts with the "(no max)" annotations in the updated Table 1 - see [Source Issues](#source-issues-typos-and-internal-inconsistencies).)*

---

### Appendix D - "PM3 Minor Amendments" - SCID VCEP responses (file: PM3 Minor Amendments.docx)

This file is the VCEP's point-by-point response to the SVI's October 2025 minor updates. It is a rationale document; the operative table it carries is identical to Appendix C Table 1, and its single embedded image (`word/media/image1.png`) is a picture of Appendix C Table 2 (PM3_Supporting 0.5 / PM3 1.0 / PM3_Strong 2.0 / PM3_VeryStrong 4.0). **Both are reflected in the spec's own PM3 sources.**

Verbatim content:

**Footnotes carried on the table:**
- \* Multiple probands from separate nuclear families that are later found to have identity-by-descent should only be counted once.
- \*\* When consanguinity is not known or reported: if family IS NOT from a bottlenecked population (as defined by gnomAD), assume non-consanguinity; otherwise, assume consanguinity. If genetic ancestry of the family cannot be determined, assume consanguinity.

**SVI Comments (with SCID VCEP responses):**

1. *SVI:* "Prefer N/A to repeating the 1.0 and 0.5"
   *VCEP:* "The SCID VCEP deliberated this point. Our geneticists pointed out that apparent homozygous variants could result from hemizygosity, which may be undetected if the parents are not sequenced (i.e., 'Phase unknown'). Because of the likelihood that authors may not bother to sequence the parents in homozygous situations, especially in older publications, the VCEP experts preferred to leave the numbers in place."
2. *SVI:* "Update 'max point 0.5 per family' to 'max point 0.5' as in original specs. Please replace 'max point 0.5 per family' from the Homozygous Consanguineous and indicate 'no max'. Rationale: 'per proband' is a rule for the whole table in general (per the table title); Multiple cases per family will inherently be counted as PP1 instead of multiple PM3s."
   *VCEP:* "The SCID VCEP agreed and made the changes to the table. To minimize confusion for biocurators and experts as much as possible between proper application of PM3 vs. PP1 (which we have definitely observed, even in sustained curations), we changed 'Proband' to 'Proband-Family'."
3. *SVI:* "What to do if you don't know about consanguinity"
   *VCEP:* "The VCEP decided to use gnomAD definitions to specify assumption of non-consanguinity for families from non-bottlenecked populations and assumption of consanguinity otherwise. A footnote was added to the Table."
4. *SVI:* "If the VCEP wishes, they can provide an asterisk footnote that supports the notion that 'multiple probands from separate nuclear families that are later found to have identity-by-descent should only be counted once.'"
   *VCEP:* "We added this footnote to the Table."

**Reflected in the spec's own tables?** **Yes.** Every change described here is present in the distributed PM3 Criterion.pdf (Table 1 updated October 17, 2025). The RAG2 registry entry itself carries no PM3 point table of its own, so there is nothing in the registry entry for this erratum to contradict.

---

### Appendix E - SCID VCEP PS3/BS3 Functional Evidence workbook (file: SCID VCEP PS3_BS3.xlsx)

Three sheets. **Sheet 3 is a variant-level lookup table**, not a rule set - use it to look up individual variants, not to derive criteria.

#### Sheet 1: "General Class of Assay Summary"

| Gene | General Class of Assay | PMIDs |
|---|---|---|
| RAG2 | V(D)J recombination assay+ | PMID: 20234091, PMID: 29772310 |
| | Cellular localization assay | PMID: 20234091 |
| | Histone interaction assay | PMID: 20234091 |

*The trailing "+" on "V(D)J recombination assay+" is as printed in the source; no legend for it appears in the workbook.*

#### Sheet 2: "RAG2 Assay Instance Details" (4 assay instances, transposed - rows are attributes)

| Attribute | Instance 1 | Instance 2 | Instance 3 | Instance 4 |
|---|---|---|---|---|
| PMID | 20234091 | 20234091 | 20234091 | 29772310 |
| Gene | RAG2 | RAG2 | RAG2 | RAG2 |
| DOI / link | 10.1172/JCI41305 | 10.1172/JCI41305 | 10.1172/JCI41305 | 10.1016/j.jaci.2018.04.027 |
| Author | Couëdel...Cortes | Couëdel...Cortes | Couëdel...Cortes | Tirosh...Lee |
| Year | 2010 | 2010 | 2010 | 2019 |
| General Class of Assay | V(D)J recombination | Cellular localization | Histone interaction | V(D)J recombination |
| Assay (General Description) | Retrovirally transduced pro-B cells expressing wild type or variant Rag2 proteins were harvested 8-12 days post-transduction for genomic DNA extraction, and PCR amplification of endogenous Ig rearrangement sequences. The PCR products were analyzed by Southern blot to examine IgH D-to-J and V-to-DJ rearrangements and IgL Vκ-to-Jκ rearrangement | The cellular localization of wild type and variant Rag2 in retrovirally transduced pro-B cell lines and transfected 293T cells was determined by Western blotting analysis of fractionated cytoplasmic and nuclear extracts | Anti-Flag coimmunoprecipitations were performed on whole cell extracts from retrovirally transduced pro-B cells and 293T cells expressing wild type or variant Rag2 proteins and analyzed for the presence of acetylated histone H3 and histone H4 via Western blotting | Murine Rag2-/- Abl pro-B cells were transduced with a retroviral vector containing wild type, mock, or variant human RAG2 cDNA, blocked in the G0/G1 cell cycle phases for 96 hours, and harvested for analysis by flow cytometry |
| Material used | Murine Rag2–/– pro-B cell line retrovirally transduced to express FNT-tagged wild type or variant Rag2 | Murine Rag2–/– pro-B cell line retrovirally transduced to express FNT-tagged wild type or variant Rag2; 293T cells transfected to express FNT-tagged wild type or variant Rag2 | Murine Rag2–/– pro-B cell line retrovirally transduced to express FNT-tagged wild type or variant Rag2; 293T cells transfected to express FNT-tagged wild type or variant Rag2 | Murine Rag2-/- Abl pro-B cells with a stable single integration of the pMX-INV GFP cassette flanked by two coding recombination signal sequences |
| Readout type | Semi-quantitative | Semi-quantitative | Semi-quantitative | Quantitative |
| Readout description | Presence/intensity of Southern blot bands corresponding to different recombination patterns | Presence/intensity of band corresponding to Rag2 protein localized in cytoplasm or nucleus | Presence/intensity of band corresponding to Rag2-coimmunoprecipitated acetylated histone H3 and histone H4 | GFP expression as a readout of recombination activity (reported as a percentage of the recombination activity of wild type RAG1) |
| Biological replicates (met/not met) | None (not met) | 2 (Murine Rag2–/– pro-B cell line and 293T cells) | 2 (Murine Rag2–/– pro-B cell line and 293T cells) | None (not met) |
| Technical replicates | 2 | Not reported | Not reported | 3 |
| Basic positive control | PCR products from genomic DNA isolated from cells expressing wild type Rag2 or the Rag2 core domain (thought to be essential for recombination) | Fractions from cells expressing wild type Rag2 protein | Coimmunoprecipitates from cells expressing wild type Rag2 protein and cells expressing Rag2 C-terminus (including the PHD domain thought to be involved in histone interaction) | Wild type RAG2 cDNA-transduced cells |
| Basic negative control | PCR products from genomic DNA isolated from nontransduced cells, mock-transduced cells, FLAG-tag only-transduced cells (empty vector), and cells expressing the Rag2 C-terminus (lacking the core domain thought to be essential for recombination) | Not reported | Coimmunoprecipitates from cells expressing the core region of Rag2 protein (aa 1-387; lacking the PHD domain thought to be involved in histone interaction); Coimmunoprecipitates from cells expressing FLAG tag only (empty vector; no exogenous Rag2 expression) | Mock-transduced cells |
| Validation controls P/LP (#) | 0 | 0 | 0 | 0 |
| Validation controls B/LB (#) | 0 | 0 | 0 | 0 |
| Statistical analysis | Not reported | Not reported | Not reported | Mann-Whitney test |
| Threshold for normal readout | Wild type-like pattern/intensity of recombination products indicative of intact recombination activity | Wild type-like pattern of nuclear localization | Wild type-like pattern of interactions with AcH3 and histone H4 | Wild type-like recombination activity (numeric threshold not reported) |
| Threshold for abnormal readout | Altered pattern/intensity of recombination products indicative of a defect in recombination activity | Altered localization pattern (increased presence of protein in cytoplasm, reduced presence of protein in nucleus) | Disrupted pattern (reduction) of interactions with AcH3 and histone H4 | Reduced recombination activity (numeric threshold not reported) |
| **Approved assay (y/n)** | **y** | **n** | **n** | **y** |
| **Proposed strength** | **PS3_Supporting** | (blank) | (blank) | **PS3_Moderate** |
| Variant(s) Tested | c.1247G>T (p.Trp416Leu), c.1338C>G (p.Cys446Trp), c.1357T>A (p.Trp453Arg), c.1421A>G (p.Asn474Ser), c.1433G>A (p.Cys478Tyr), c.1442A>C (p.His481Pro) | same six variants | same six variants | 41 variants (see Table II in publication) |
| Notes | (blank) | Use of 293T cells helped overcome limitations of studying variants with inappropriate subcellular localization and/or decreased protein stability in the pro-B cell line | Use of 293T cells helped overcome limitations of studying variants with inappropriate subcellular localization and/or decreased protein stability in the pro-B cell line | Could likely assemble a sufficient number of validation controls based on existing information (case reports, allele frequency, etc.) to use this assay at a moderate level (or possibly strong) if the experts feel it is appropriate. |

**Operative rule from this sheet:** only two of the four assay instances are approved - Couëdel et al., 2010 V(D)J recombination (PS3_Supporting) and Tirosh et al., 2019 V(D)J recombination (PS3_Moderate). The cellular-localization and histone-interaction assays are **not approved**. No BS3 strength is proposed for any instance, consistent with BS3 being Not Applicable in the specification.

#### Sheet 3: "RAG2 Tirosh et al., 2019 Valida" - validation control lookup

Structure: one row per validation-control variant. Columns: Variant (Nucleotide Change) | Variant (Protein Change) | Overall Classification | ACMG/AMP Codes Applied | Mean V(D)J Recombination Activity Level in Tirosh et al., 2019 | Tirosh et al., 2019 V(D)J Recombination Assay Result Interpretation (according to VCEP-established thresholds) | Validation Control | Notes.

This is a **lookup table of the 11 variants the VCEP used to validate the Tirosh assay**; it is not itself a criterion rule. Full contents:

| Nucleotide | Protein | Overall Classification | ACMG/AMP Codes Applied | Mean V(D)J activity (%) | Interpretation | Validation Control |
|---|---|---|---|---|---|---|
| c.46C>T | p.Gln16Ter | Likely Pathogenic | PVS1_Strong, PM3, PM2_Supporting | 1.7 | Abnormal | Known Pathogenic |
| c.104G>C | p.Gly35Ala | Likely Pathogenic | PM5, PP4, PM1_Supporting, PM2_Supporting, PM3_Supporting | 22.1 | Abnormal | Known Pathogenic |
| c.379A>T | p.Lys127Ter | Likely Pathogenic | PVS1_Strong, PM3, PM2_Supporting | 0.1 | Abnormal | Known Pathogenic |
| c.644C>T | p.Thr215Ile | Benign | BA1 | 67.2 | Normal | Known Benign |
| c.686G>A | p.Arg229Gln | Pathogenic | PM3_VeryStrong, PP1, PM1_Supporting, PM2_Supporting, PM5_Supporting | 8.9 | Abnormal | Known Pathogenic |
| c.921G>A | p.Trp307Ter | Likely Pathogenic | PVS1_Strong, PM3, PM2_Supporting | 0.2 | Abnormal | Known Pathogenic |
| c.1158C>A | p.Phe386Leu | Benign | BA1 | 109.1 | Normal | Known Benign |
| c.1219G>T | p.Glu407Ter | Likely Pathogenic | PVS1_Strong, PM2_Supporting, PM3_Supporting | 2.9 | Abnormal | Known Pathogenic |
| c.1357T>A | p.Trp453Arg | Likely Pathogenic | PM1, PM3, PP4, PM2_Supporting | 0.6 | Abnormal | Known Pathogenic |
| c.1433G>A | p.Cys478Tyr | Likely Pathogenic | PM1, PP1, PP4, PM2_Supporting, PM3_Supporting | 0.2 | Abnormal | Known Pathogenic |
| c.1504A>G | p.Met502Val | Benign | BA1 | 99.6 | Normal | Known Benign |

Note repeated on the three nonsense rows c.46C>T, c.379A>T and c.1219G>T: "RAG2 is encoded by a single exon, mitigating concerns about the ability of cDNA expression experiments to model the behavior of variants subject to nonsense mediated decay."

---

### Appendix F - PP1 segregation recommendations (Oza et al. Tables 4a and 4b) (file: PP1.pdf)

Reprint of Tables 4a and 4b from Oza et al. (Hum Mutat; PMID: 30311386). This is the general recommendation the VCEP defers to; the VCEP adds only the "unaffected individuals must be heterozygous carriers" specification given under [PP1](#pp1---co-segregation).

**Table 4a: Recommendations for PP1 (segregation evidence) - General Recommendations**

| | Supporting | Moderate | Strong |
|---|---|---|---|
| Likelihood | 4:1 | 16:1 | 32:1 |
| LOD Score | 0.6 | 1.2 | 1.5 |
| Autosomal dominant threshold | 2 affected segregations | 4 affected segregations | 5 affected segregations |
| Autosomal recessive threshold | See Table 4b | See Table 4b | See Table4b |

*Typo preserved: the Strong cell reads "See Table4b" (missing space).*

**Table 4b: Recommendations for autosomal recessive segregation evidence (PP1)** - General Recommendations (Phenocopy not an issue). **This is a LOD-score lookup table**: affected segregations in rows, unaffected recessive segregations in columns; each cell is the LOD score for that combination. Compare the cell value to the Table 4a LOD thresholds (0.6 Supporting / 1.2 Moderate / 1.5 Strong).

| Affected \ Unaffected | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **0** | 0 | 0.12 | 0.25 | 0.37 | 0.5 | 0.62 | 0.75 | 0.87 | 1 | 1.12 | 1.25 |
| **1** | 0.6 | 0.73 | 0.85 | 0.98 | 1.1 | 1.23 | 1.35 | 1.48 | 1.6 | 1.73 | 1.85 |
| **2** | 1.2 | 1.33 | 1.45 | 1.58 | 1.7 | 1.83 | 1.95 | 2.08 | 2.2 | 2.33 | 2.45 |
| **3** | 1.81 | 1.93 | 2.06 | 2.18 | 2.31 | 2.43 | 2.56 | 2.68 | 2.81 | 2.93 | 3.06 |
| **4** | 2.41 | 2.53 | 2.66 | 2.78 | 2.91 | 3.03 | 3.16 | 3.28 | 3.41 | 3.53 | 3.66 |
| **5** | 3.01 | 3.14 | 3.26 | 3.39 | 3.51 | 3.63 | 3.76 | 3.88 | 4.01 | 4.13 | 4.26 |
| **6** | 3.61 | 3.74 | 3.86 | 3.99 | 4.11 | 4.24 | 4.36 | 4.49 | 4.61 | 4.74 | 4.86 |
| **7** | 4.21 | 4.34 | 4.46 | 4.59 | 4.71 | 4.84 | 4.96 | 5.09 | 5.21 | 5.34 | 5.46 |
| **8** | 4.82 | 4.94 | 5.07 | 5.19 | 5.32 | 5.44 | 5.57 | 5.69 | 5.82 | 5.94 | 6.07 |
| **9** | 5.42 | 5.54 | 5.67 | 5.79 | 5.92 | 6.04 | 6.17 | 6.29 | 6.42 | 6.54 | 6.67 |
| **10** | 6.02 | 6.15 | 6.27 | 6.4 | 6.52 | 6.65 | 6.77 | 6.9 | 7.02 | 7.15 | 7.27 |

Legend (verbatim): "Affected segregations are counted in rows and unaffected segregations in columns. Affected segregations are affected family members in whom biallelic compound heterozygous or homozygous variants segregates. Unaffected segregations are defined as unaffected family members, typically siblings, who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants identified in the proband, or a heterozygous carrier for a single variant. Unaffected, carrier parents DO NOT count as unaffected segregations. There may be scenarios where individuals other than siblings could be counted as segregations, such as in families where one parent is affected with the autosomal recessive disorder, in large families with multiple branches, or in consanguineous families. Each cell shows the LOD score of each combination of affected and unaffected segregations. LOD scores were calculated using a simplified LOD score formula, as described in Strande et al., 2017."

---

### Appendix G - PP4 table, 2025 updates (file: PP4 - RAG2.pdf)

Single-page standalone rendering of the PP4 criterion. Its content is **identical** to the PP4 section of the v2.2 registry entry (point ranges, all nine evidence rows and point values, footnote 1 and the *Notes). It is fully reflected in the spec's own tables and adds nothing beyond them. It likewise carries the dangling superscript on "≥4 points: PP4_Strong<sup>1</sup>" with no matching CNV footnote.

---

### Appendix H - "RAG2 Corrections 1.6.26" (file: RAG2 Corrections 1.6.26.docx)

Erratum covering four criteria. **Transcribed in full below, with a per-criterion statement of whether it is reflected in the spec's own tables.**

#### H.1 PS3 — **PARTIALLY reflected; the erratum adds a requirement the spec tables do not contain**

Header material: "SVI Recommended Resources - Functional assay sheet. Please follow the instructions in the sheet."

- **Strong Specification:** "PS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and recapitulating the RAG2-SCID phenotype." *(Modification Type: Gene-specific)* — **matches** the v2.2 table.
- **Moderate Specification:** "Strength of evidence from cellular models/in vitro studies is dependent upon abnormal result in a V(D)J recombination assay: PS3_Moderate: <25% of wild-type activity in Tirosh et al., 2019 (PMID: 29772310). **At least one previously observed proband with the expressed RAG2 variant meeting PP4 is required to apply PS3 at any strength.**" *(Modification Type: Gene-specific; Strength)* — the first sentence matches the v2.2 table; **the bolded sentence is absent from the v2.2 table.**
- **Supporting Specification:** "Strength of evidence from cellular models/in vitro studies is dependent upon abnormal result in a V(D)J recombination assay: PS3_Supporting: 25-60% of wild-type activity in Tirosh et al., 2019 (PMID: 29772310) OR Reduced activity compared to wild type in Couëdel et al., 2010 (PMID: 20234091). **At least one previously observed proband with the expressed RAG2 variant meeting PP4 is required to apply PS3 at any strength.**" *(Modification Type: Gene-specific; Strength)* — same situation.

Note the erratum's own wording is self-inconsistent in placement: the requirement says it applies "at any strength" but is printed only under Moderate and Supporting, not under Strong.

#### H.2 PM1 — **fully reflected**

Erratum text is word-for-word identical to the v2.2 PM1 Moderate and Supporting rows and to the PM1 caveat (see [PM1](#pm1---mutational-hot-spot)).

#### H.3 BS2 — **fully reflected**

Erratum text is word-for-word identical to the v2.2 BS2 Strong and Supporting rows (see [BS2](#bs2---observed-in-healthy-adult)).

#### H.4 PP4 — **PARTIALLY reflected; the erratum adds a footnote the spec tables do not contain**

The erratum's PP4 point ranges, nine-row evidence table, footnote 1 (PIDTC 2022) and *Notes are identical to the v2.2 registry entry and to Appendix G. The Moderate and Supporting rows are identical.

The **Strong** row differs:

| Source | Strong text |
|---|---|
| v2.2 registry entry and PP4 - RAG2.pdf | "A patient score of ≥ 4 points." |
| RAG2 Corrections 1.6.26.docx | "A patient score of ≥ 4 points<sup>1</sup>. <sup>1</sup>CNV (Copy number variation) testing is required to consider PP4_Strong in order to certify that the variant in question is the causative for the phenotype and not one CNV event corrected by gene therapy and not identified previously (see instructions below)." |

The erratum therefore supplies the missing definition for the otherwise dangling "1" superscript that both the registry entry and the PP4 PDF print on "≥4 points: PP4_Strong<sup>1</sup>".

---

## Source Issues, Typos and Internal Inconsistencies

Recorded, not corrected. Curators should treat these as open questions for the VCEP.

1. **PS3 erratum vs. spec tables (substantive).** "RAG2 Corrections 1.6.26.docx" requires "at least one previously observed proband with the expressed RAG2 variant meeting PP4 … to apply PS3 at any strength". This gating requirement appears in **neither** the v2.2 registry entry nor the PS3/BS3 workbook. A curator applying only the registry entry would apply PS3 without it.
2. **PS3 erratum internal placement.** The same sentence is stated to apply "at any strength" but is printed only under the Moderate and Supporting blocks, not under Strong (animal model).
3. **PP4 erratum vs. spec tables (substantive).** The CNV-testing prerequisite for PP4_Strong exists only in the erratum. Both the registry entry and PP4 - RAG2.pdf print "PP4_Strong<sup>1</sup>" with a footnote marker whose only defined footnote on that page is the unrelated PIDTC-2022 note — a dangling reference that the erratum resolves.
4. **PVS1 flowchart vs. PVS1 spec text (substantive).** The specification's PVS1_Strong row says that for variants not predicted to undergo NMD but removing >10% of protein with at least one pathogenic variant downstream, **PVS1_Strong** applies. In the flowchart, the analogous endpoint in the **splice-site** and **deletion** branches is indeed PVS1_Strong, but in the **Nonsense or Frameshift** branch the same endpoint is drawn as **PVS1** (full Very Strong, magenta box). The two documents disagree for nonsense/frameshift variants.
5. **PVS1 flowchart footnotes missing.** Superscript markers **a**, **b** and **d** appear on the flowchart with no legend anywhere in the one-page PDF. Their meanings cannot be recovered from the distributed package.
6. **PVS1 colour terminology.** The specification text refers to "red boxes" and "purple boxes"; the flowchart actually uses red-X annotations on pink boxes and magenta boxes respectively. Same intent, different vocabulary.
7. **PM3 SVI document internal conflict.** Table 1 (October 2025) annotates both homozygous rows "(no max)", but the unchanged "Homozygous occurrences" consideration on page 2 still states "A recommended max of 1.0 points of all homozygous cases is suggested". This is a conflict inside the SVI document itself, carried into the RAG2 package unresolved. The VCEP's "PM3 Minor Amendments" response confirms the "(no max)" change was deliberate.
8. **PS2/PM6 "phase" wording.** The VCEP writes "Reduce points per proband by half if the phase is unconfirmed" under both PS2 and PM6. The SVI *de novo* framework halves points for **unconfirmed parental relationships**, not for unconfirmed phase; "phase" is the PM3 concept. The numeric effect matches SVI Table 1 column 2 (2→1, 1→0.5, 0.5→0.25), so the intent appears to be "parental relationships", but the word used is "phase".
9. **PM5 nonsense point table vs. RAG2 biology.** The point table's first two rows are conditioned on the VUA being "predicted to lead to NMD" and on informative variants "in the exon" — but the specification states RAG2 is a **single-exon** gene for which NMD is **not** predicted. Those two rows appear to be inapplicable to RAG2 as written; the VCEP does not say so.
10. **PM6 has no Very Strong row** while PS2 does, even though the SVI Table 2 the VCEP defers to defines PM6_VeryStrong.
11. **BP7 tool count.** "predicted not to impact splicing by at least two out of three *in silico* tools" is followed by a list of **six** tools.
12. **PP1 typo.** Table 4a Strong cell reads "See Table4b" (missing space). The VCEP PP1 specification text contains a stray comma: "do not count wild-type/wild-type, individuals".
13. **PM5 legend punctuation.** "NMD = nonsense-mediated decay; PTC premature termination codon" — the second definition is missing its "=" or colon.
14. **PP4 9G4 thresholds.** "9G4int (>5%) or 9G4hi (>5%)" assigns the same 5% cutoff to both subsets; whether this is intended or a copy error is not stated.
15. **BA1 vs BS1 parameter asymmetry.** BA1 uses prevalence 1:5,000 with 50% penetrance; BS1 uses 1:50,000 with 100% penetrance. Both are as printed; the VCEP gives no rationale for the differing prevalence assumptions.
16. **Workbook "V(D)J recombination assay+"** carries a trailing "+" with no legend in the workbook.
17. **Likely Pathogenic combining rules** list both "1 Strong AND 1 Moderate" (rule 2) and "1 Strong AND 2 Moderate" (rule 7); rule 7 is subsumed by rule 2 as printed.

---

## Criteria Status Summary

| Applicable (specified) | Not Applicable (explicitly) | Not specified by VCEP |
|---|---|---|
| PVS1, PS1, PS2, PS3, PM1, PM2, PM3, PM4, PM5, PM6, PP1, PP3, PP4, BA1, BS1, BS2, BS4, BP7 | PS4, PP2, PP5, BS3, BP1, BP2, BP3, BP4, BP5, BP6 | PVS1_Supporting as a registry strength row (appears only in the flowchart's Initiation Codon branch); PM6_VeryStrong |

---

## Version History

Only the v2.2 release notes are distributed with this package. Earlier version history is not included in the downloaded files and is therefore not reproduced here.

| Version | Released | Notes |
|---|---|---|
| 2.2 | 6/1/2026 | Edited Rules for Combining Criteria to reflect standard combinations plus (A) 1 very strong + 1 supporting = Likely Pathogenic and (B) 1 Strong Benign = Likely Benign. Refreshed and saved Rules for Combining Criteria. Uploaded two files to address minor PM3 changes: "PM3 Criterion: October 2025 Version, Minor Updates" and "PM3: svi recommendations: October 2025 Group Responses to Minor Updates". Uploaded RAG2 corrections: changes to PS3; changes to PM1; edited PP4 criteria; added BS2_Strong strength; added text to BS2_Supporting. |

Both announced combining-rule changes were verified present in the v2.2 tables: (A) Likely Pathogenic rule 8 (1 Very Strong + 1 Supporting); (B) Likely Benign rule 2 (1 Strong: BS1, BS2, BS4).

---

*This document was compiled from the ClinGen VCEP specification GN124 (RAG2 v2.2) and all nine distributed files. For the most current version, please refer to the ClinGen website.*
