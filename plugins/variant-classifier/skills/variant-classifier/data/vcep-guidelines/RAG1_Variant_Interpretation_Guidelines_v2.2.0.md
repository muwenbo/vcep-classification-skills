# ClinGen Severe Combined Immunodeficiency Disease VCEP Variant Interpretation Guidelines for RAG1

**Version:** 2.2
**Released:** 5/15/2026
**Affiliation:** Severe Combined Immunodeficiency Disease VCEP
**Type:** Richards et.al., 2015 - Combining rules
**DOI:** 10.5281/zenodo.21434500
**Source basis:** ClinGen Severe Combined Immunodeficiency Disease Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for RAG1 Version 2.2 (ClinGen Criteria Specification Registry, GN123), plus the supplementary files distributed with that specification.

**Release Notes (verbatim from the specification):**

> Edited Rules for Combining Criteria to reflect standard combinations plus (A) 1 very strong + 1 supporting = Likely Pathogenic and (B) 1 Strong Benign = Likely Benign.
>
> Refreshed and saved Rules for Combining Criteria.
>
> Uploaded two files to address minor PM3 changes:
>
> 1. "PM3 Criterion: October 2025 Version, Minor Updates"
> 2. "PM3: svi recommendations: October 2025 Group Responses to Minor Updates"
>
> Uploaded RAG1 Corrections 1.6.26 file
>
> - Made changes regarding PP4 criteria.
> - PS3_Moderate specification edit
> - Added caveat to PM1
> - Added BS2_Strong strength
> - Added BS2_Supporting requirement to have minimum of 1 homozygote.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | RAG1 (HGNC:9831) |
| **HGNC Name** | recombination activating 1 |
| **Transcript** | NM_000448.3 |
| **Disease** | recombinase activating gene 1 deficiency (MONDO:0000572) |
| **Inheritance** | Autosomal recessive inheritance |
| **Keywords** | human biology genomics variant variant classification clingen disease standards RAG1 NM_000448.3 Autosomal recessive inheritance recombinase activating gene 1 deficiency |
| **Rights Holder** | The Clinical Genome Resource (ClinGen) |

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
2. [Benign Criteria](#benign-criteria)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)
5. [Source Notes, Typos and Internal Inconsistencies](#source-notes-typos-and-internal-inconsistencies)

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

- Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with two modifications:
  - Given that the *RAG1* protein is encoded by a single exon (based on MANE Select transcript NM_000448.3) and nonsense-mediated decay is not predicted for nonsense or frameshift variants, PVS1 cannot be applied at the default strength to RAG1 variants (indicated by the red boxes in attached PVS1 flowchart.), except in the case of a full gene deletion or removing/altering critical domain (NBD domain, DDBD domain and core domain)(indicated by the purple boxes in attached PVS1 flowchart.):
  - PVS1 can be applied to variants not predicted to undergo nonsense-mediated decay but removing/altering the critical NBD domain (aa 394-460), DDBD domain (aa 461-517), and core domain (aa 387-1011) based on recommendations from Walker et. al., preprint (See attached PVS1 flowchart.)
  - Strength modification for variants predicted to remove >10% of the protein (See attached PVS1 flowchart.).
  - For variants not predicted to undergo nonsense-mediated decay, at least one pathogenic variant must be present downstream in order to apply PVS1_Strong (See attached PVS1 flowchart.).
  - The NBD domain (aa 394-460), DDBD domain (aa 461-517) and core domain (aa 387-1011) are defined as a region critical to protein function. (PMID: 26996199).

> **Source note:** the lead-in says "two modifications" but five bullets follow. Transcribed as written.

#### Strength Levels

| Strength | Criteria (verbatim) |
|----------|---------------------|
| **Very Strong** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with two specifications: (a) Given that the *RAG1* protein is encoded by a single exon (based on MANE Select transcript NM_000448.3) and nonsense-mediated decay is not predicted for nonsense or frameshift variants, PVS1 cannot be applied at the default strength to RAG1 variants (indicated by the red boxes in the Flowchart attached), **except** in the case of full gene deletion **or** removing/altering critical domain for the protein (NBD domain, DDBD domain, and core domain, indicated by the purple in the Flowchart). (b) PVS1 can be applied to variants not predicted to undergo nonsense-mediated decay when removing/altering the critical NBD domain (aa 394-460), DDBD domain (aa 461-517), and core domain (aa 387-1011) based on recommendations from Walker et al., preprint. *Modification Type: General recommendation, Gene-specific* |
| **Strong** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification: For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein, at least one pathogenic variant **must be** present downstream in order to apply PVS1_Strong. *Modification Type: General recommendation, Gene-specific* |
| **Moderate** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification: For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein, when at least one pathogenic variant is **not** present downstream, downgrade to PVS1_Moderate. *Modification Type: General recommendation* |
| **Supporting** | Not specified as a separate row in the specification. PVS1_Supp appears only in the attached PVS1 flowchart (Initiation Codon branch — see [Appendix A](#appendix-a---rag1-specified-pvs1-flowchart)). |

See [Appendix A](#appendix-a---rag1-specified-pvs1-flowchart) for the full gene-specified PVS1 decision tree.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria (verbatim) |
|----------|---------------------|
| **Strong** | It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T. Applicable if the previously established variant is classified as **pathogenic** by SCID VCEP specifications for *RAG1*. *Modification Type: Gene-specific* |
| **Moderate** | It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be likely pathogenic, can use PS1 for c.105+1G>T. Applicable if the previously established variant is classified as **likely pathogenic** by SCID VCEP specifications for *RAG1*. *Modification Type: Gene-specific, Strength* |

SpliceAI comparator: "equal to or greater than" the known pathogenic variant (inclusive). No numeric delta threshold is given for PS1.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

The following guidelines should be used when determining the phenotypic consistency of each proband:

- "Phenotype highly specific for gene" proband must meet at least PP4_Moderate criteria;
- "Phenotype consistent with gene but not highly specific" proband must meet PP4 criteria;
- "Phenotype consistent with gene but not highly specific and high genetic heterogeneity": proband has been asserted to have a SCID phenotype but does not meet PP4 criteria;
- Reduce points per proband by half if the phase is unconfirmed.

**Strength rows (all four identical in the specification):**

| Strength | Criteria (verbatim) |
|----------|---------------------|
| **Very Strong** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |
| **Strong** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |
| **Moderate** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |
| **Supporting** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |

The referenced SVI *de novo* point system is distributed with this specification as `PS2_PM6.pdf` and is transcribed in full in [Appendix B](#appendix-b---svi-recommendation-for-de-novo-criteria-ps2--pm6-version-11). The VCEP itself defines no separate point matrix; it maps its own phenotypic-consistency categories onto the SVI Table 1 rows.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria (verbatim) |
|----------|---------------------|
| **Strong** | PS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and recapitulating the RAG1-SCID phenotype. *Modification Type: Gene-specific* |
| **Moderate** | The strength of evidence from cellular models/*in vitro* studies is dependent upon the abnormal result in a V(D)J recombination assay: PS3_Moderate: <25% of wild-type activity in Lee et al., 2014 (PMID: 24290284); *Modification Type: Gene-specific* |
| **Supporting** | The strength of evidence from cellular models/*in vitro* studies is dependent upon the abnormal result in a V(D)J recombination assay: PS3_Supporting: 25-60% of wild-type activity in Lee et al., 2014 (PMID: 24290284) **OR** Reduced activity compared to wild type in Corneo et al., 2001 (PMID: 11313270); *Modification Type: Gene-specific, Strength* |

**Comparators:** PS3_Moderate uses a strict `<` (less than 25% of wild-type activity). PS3_Supporting is written as an inclusive range "25-60%"; the specification does not state whether the endpoints are inclusive beyond the plain reading of the range.

> **No proband/PP4 precondition on PS3.** The RAG1 package states no requirement that a previously observed proband meeting PP4 exist before PS3 may be applied. (Sibling SCID VCEP specifications ship such a gate in a separate "Corrections" file; RAG1 ships no Corrections file and no equivalent text appears in any of its nine distributed files.) Applying such a gate to RAG1 would be **not specified by this VCEP**.

#### Approved Assay Instances

See [Appendix C](#appendix-c---ps3bs3-functional-evidence-scid-vcep-ps3_bs3xlsx) for the full transcription of the distributed functional-evidence workbook (approved assays, assay-instance detail, and the Lee et al., 2014 validation-control set).

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance. Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** **Not Applicable.** (No comment provided by the VCEP.)

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** Caveat: variant must not meet BS1, BS2, or BA1 criteria.

| Strength | Criteria (verbatim) |
|----------|---------------------|
| **Moderate** | Strength is dependent upon the location of the variant within specific functional domains (PMID: 26996199): PM1_Moderate: missense variant located in the **NBD domain** (amino acids 394-460) and **DDBD domain** (amino acids 461-517). Caveat: variant must not meet BS1, BS2, or BA1 criteria. *Modification Type: Gene-specific* |
| **Supporting** | Strength is dependent upon the location of the variant within specific functional domains (PMID: 26996199): PM1_Supporting: missense variant located elsewhere in the **core domain** (amino acids 387-1011). Caveat: variant must not meet BS1, BS2, or BA1 criteria. *Modification Type: Gene-specific* |

Domain boundaries are inclusive amino-acid ranges as written.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

| Strength | Criteria (verbatim) |
|----------|---------------------|
| **Supporting** | gnomAD popmax filtering allele frequency **<0.000102**. An additional requirement is that **no homozygotes** have been observed in gnomAD. *Modification Type: Gene-specific* |

**Comparator:** strict less-than (`<`) 0.000102. Only a Supporting row is defined.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

Use ClinGen SVI adapted recommendations for *in trans* criterion (see PM3 criterion attached below) with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for *RAG1*.

Caveat: All variants should be sufficiently rare (meet PM2 specification). The applicability of PM3 to suspected founder variants with allele frequencies exceeding the PM2 threshold will be evaluated on a case-by-case basis by the VCEP.

| Strength | Criteria (verbatim) |
|----------|---------------------|
| **Very Strong** | Use ClinGen SVI adapted recommendations for *in trans* criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for *RAG1*. *Modification Type: General recommendation, Strength* |
| **Strong** | (identical text) *Modification Type: General recommendation, Strength* |
| **Moderate** | (identical text) *Modification Type: General recommendation, Strength* |
| **Supporting** | (identical text) *Modification Type: General recommendation, Strength* |

The main specification body contains **no PM3 point table of its own**. The operative point system is the attached SVI PM3 document (Version 1.0, Table 1 updated October 17, 2025), transcribed in [Appendix D](#appendix-d---svi-recommendation-for-in-trans-criterion-pm3-version-10-table-1-updated-17-october-2025). Three PM3 supplementary files are distributed; the two .docx files ("PM3: svi recommendations: October 2025 Group Responses to Minor Updates" and "PM3 Minor Amendments 12.12.2025") have identical content and are transcribed once in [Appendix E](#appendix-e---pm3-svi-recommendations--pm3-minor-amendments-two-files-identical-content). All three agree on every value.

**Operative PM3 points for RAG1** (SVI Table 1 as updated, per attached documents; the VCEP adds only the requirement that the co-occurring variant be classified by SCID VCEP RAG1 specifications, plus the PM2-rarity caveat):

| Classification/Zygosity of other variant | Confirmed in *trans* | Phase unknown |
|---|---|---|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence — Non-consanguineous *(no max)* | 1.0 | 1.0 |
| Homozygous occurrence — Consanguineous *(no max)* | 0.5 | 0.5 |
| Uncertain significance variant *(max point 0.5)* | 0.25 | 0 |

Points-to-strength (SVI Table 2): PM3_Supporting 0.5 | PM3 1.0 | PM3_Strong 2.0 | PM3_VeryStrong 4.0.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria (verbatim) |
|----------|---------------------|
| **Moderate** | When applied to deletion variants, the deleted region must contain a known **pathogenic** or **likely pathogenic** variant that is not predicted/observed to alter splicing. *Modification Type: Gene-specific* |
| **Supporting** | When applied to deletion variants, the deleted region must contain a known **VUS** variant that is not predicted/observed to alter splicing. *Modification Type: Gene-specific, Strength* |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

For nonsense variants:

**PM5_Strong** — PM5 may be applied at a Strong level of evidence for any nonsense variant with 4+ points from informative variants (see below point table). PM5_Strong should be downgraded to PM5_Moderate if PVS1 is applied at any strength.

**PM5_Moderate** — PM5 may also be applied at a Moderate level of evidence for any nonsense variant with 2+ points from informative variants (see below point table). PM5_Moderate may not be combined with PVS1_VeryStrong (should be downgraded to PM5_Supporting if PVS1_VeryStrong is applied).

**PM5_Supporting** — Also applicable to a nonsense variant with 1 point from an informative variant (see point table). Informative variants must also be classified by these rule specifications.

#### PM5 nonsense point table (verbatim, 4 rows)

| Type of variant under assessment (VUA) | Informative variant | Score |
|---|---|---|
| Nonsense variant predicted to lead to NMD | P/LP variant in the exon of DNA change predicted to lead to NMD | +1pt |
| Nonsense variant predicted to lead to NMD | B/LB variant in the exon predicted to lead to NMD | -2pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | P/LP variant resulting in a PTC in the same exon but downstream of VUA | +1pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | B/LB variant resulting in PTC in the same exon but upstream of the VUA | -2pt |

NMD = nonsense-mediated decay; PTC premature termination codon

**Note:** The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet "+1 pathogenic variant downstream" on the PVS1 flowchart. If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA. The VUA must be sufficiently rare, meet PM2_Supporting, to apply this point system. If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic without use of PM5 and without use of only PVS1 plus PM2.

**Point thresholds** are written as "4+", "2+" and "1" point — i.e. inclusive at the stated value.

**Missense (default) application**, stated in the Moderate and Supporting rows: "Applicable at default strength (PM5) if previously established variant is classified as pathogenic or at reduced strength of PM5_Supporting if previously established variant is classified as likely pathogenic."

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

The following guidelines should be used when determining the phenotypic consistency of each proband:

- "Phenotype highly specific for gene" proband must meet at least PP4_Moderate criteria;
- "Phenotype consistent with gene but not highly specific" proband must meet PP4 criteria;
- "Phenotype consistent with gene but not highly specific and high genetic heterogeneity": proband has been asserted to have a SCID phenotype but does not meet PP4 criteria;
- Reduce points per proband by half if the phase is unconfirmed.

| Strength | Criteria (verbatim) |
|----------|---------------------|
| **Strong** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |
| **Moderate** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |
| **Supporting** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |

No Very Strong row is defined for PM6 in this specification. See [Appendix B](#appendix-b---svi-recommendation-for-de-novo-criteria-ps2--pm6-version-11).

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386) with the additional specification that unaffected individuals contributing to the calculated LOD score **(Attached document: PP1 specifications)** must be heterozygous carriers of one of the variants observed in the affected individuals (i.e. do not count wild-type/wild-type, individuals).

| Strength | Criteria (verbatim) |
|----------|---------------------|
| **Strong** | Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations. *Modification Type: General recommendation* |
| **Moderate** | (identical text) *Modification Type: General recommendation* |
| **Supporting** | (identical text) *Modification Type: General recommendation* |

The numeric thresholds live in the attached PP1 document (Oza et al., Tables 4a and 4b), transcribed in [Appendix F](#appendix-f---pp1-segregation-thresholds-oza-et-al-tables-4a-and-4b).

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable.**
Comments: Does not apply. The gnomAD v2.1.1 missense Z score for RAG1 (Z = 0.58) suggests this gene is not constrained for missense variation. Both benign and pathogenic missense variants are present in RAG1.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria (verbatim) |
|----------|---------------------|
| **Supporting** | Only applicable to synonymous or intronic variants predicted to impact splicing by SpliceAI with a delta score greater than or equal to 0.2. **Do not apply to missense variants.** *Modification Type: General recommendation* |

**Comparator:** inclusive (`>=`) — "greater than or equal to 0.2".

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

PP4 applicability and strength is determined by the total points accumulated by a single affected individual according to the table below and the following total point ranges:

- <1 Point: PP4 not met
- 1 - <2 Points: PP4
- ≥2 - <4 Points: PP4_Moderate
- ≥4 Points: PP4_Strong

**Comparators:** lower bounds inclusive (`1`, `≥2`, `≥4`); upper bounds strict (`<2`, `<4`); "not met" is strict `<1`.

#### PP4 evidence point table (verbatim)

| Evidence Description | Points |
|---|---|
| Diagnostic criteria met for SCID (Criteria 1 and 3 or Criterion 4 by itself) or Leaky SCID/Omenn syndrome (excluding Criterion 2)¹ | 0.5 |
| SCID gene panel or exome/genome sequencing conducted (only applicable if genetic testing did not provide an alternative genetic explanation for SCID/Leaky SCID/Omenn syndrome phenotype) | 1 |
| Family history of SCID (only applicable if SCID gene panel or exome/genome sequencing was conducted on proband and did not provide an alternative genetic explanation for phenotype) | 0.5 |
| Decreased presence of TCRVα7.2 (<2%) in CD3+ T lymphocytes and/or mucosa-associated invariant T-cells demonstrated by flow cytometry AND pathogenic or likely pathogenic variants in RAG2 and DCLRE1C have been excluded PMID: 39792639 | 1.5 |
| Decreased presence of TCRVα7.2 (<2%) in CD3+ T lymphocytes and/or mucosa-associated invariant T-cells demonstrated by flow cytometry AND pathogenic or likely pathogenic variants in RAG2 and DCLRE1C have **NOT** been excluded PMID: 39792639 | 0.5 |
| Increased presence of 9G4+ (>10%), 9G4int (>5%) or 9G4hi (>5%) cells in CD19+ B cells demonstrated by flow cytometry AND pathogenic or likely pathogenic variants in RAG2 have been excluded PMID: 39792639 | 1 |
| Increased presence of 9G4+ (>10%), 9G4int (>5%) or 9G4hi (>5%) cells in CD19+ B cells demonstrated by flow cytometry AND pathogenic or likely pathogenic variants in RAG2 have **NOT** been excluded PMID: 39792639 | 0.5 |
| SCID phenotype corrected by RAG1 gene therapy | 4 |
| T-B-NK+ lymphocyte subset profile* (See notes) | 0.5 |

¹ The diagnostic criteria should follow the PIDTC 2022 specification, summarized [here] (hyperlink in source; target URL not rendered in the distributed PDF).

*Notes: 1) If NK cells are not noted or are present, criteria may still be applied if SCID gene panel or exome/genome sequencing has ruled out alternative causes; 2) If maternal T cells are present, the T lymphocyte profile is still considered to be T- (autologous T cells are absent).

**Flow-cytometry comparators within the table are strict:** TCRVα7.2 `<2%`; 9G4+ `>10%`; 9G4int `>5%`; 9G4hi `>5%`.

| Strength | Criteria (verbatim) |
|----------|---------------------|
| **Strong** | A patient score of ≥ 4 points. *Modification Type: Disease-specific, Gene-specific* |
| **Moderate** | A patient score of ≥2-<4 points (see instructions below). *Modification Type: Disease-specific, Gene-specific* |
| **Supporting** | A patient score of 1-<2 points (see instructions below). *Modification Type: Disease-specific, Gene-specific* |

The attached `PP4 - RAG1.pdf` ("2025 updates") reproduces exactly the same ranges and the same nine-row point table; the two are consistent.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable.** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:** Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:

- Prevalence: 1:5,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.19 (based on the contribution of *RAG1* variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 19.2% rounded to 19%)
- Penetrance: 50%

| Strength | Criteria (verbatim) |
|----------|---------------------|
| **Stand Alone** | gnomAD popmax filtering allele frequency >0.00872. *Modification Type: Gene-specific* |

**Comparator:** strict greater-than (`>`) 0.00872.

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:** gnomAD popmax filtering allele frequency >0.00195¹

Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:

- Prevalence: 1:50,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.19 (based on the contribution of *RAG1* variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 19.2% rounded to 19%)
- Penetrance: 100%

¹ Consider also bottleneck populations.

| Strength | Criteria (verbatim) |
|----------|---------------------|
| **Strong** | gnomAD popmax filtering allele frequency >0.00195¹ (¹ Consider also bottleneck populations.) *Modification Type: Gene-specific* |

**Comparator:** strict greater-than (`>`) 0.00195.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

| Strength | Criteria (verbatim) |
|----------|---------------------|
| **Strong** | BS2_Strong: Can be applied at Strong level if observed in at least 3 homozygotes. *Modification Type: Strength* |
| **Supporting** | Only to be used when the variant is observed in the homozygous state in a healthy adult. BS2_Supporting: Can be applied at Supporting level if observed in at least 1 homozygote. *Modification Type: Strength* |

**Comparators:** "at least 3" and "at least 1" — inclusive (`>=`).

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** **Not Applicable.**
Comments: There is not a well-established functional study which can rule out all damaging effects on protein function.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

| Strength | Criteria (verbatim) |
|----------|---------------------|
| **Strong** | Can be applied without additional specifications. *Modification Type: None* |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment (verbatim) |
|-----------|--------|---------|
| **BP1** | Not Applicable | Does not apply. |
| **BP2** | Not Applicable | (no comment provided) |
| **BP3** | Not Applicable | Does not apply. |
| **BP4** | Not Applicable | (no comment provided) |
| **BP5** | Not Applicable | (no comment provided) |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229) |
| **BP7** | **Specified (Supporting)** | Applicable to both synonymous variants and deep intronic variants affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions. The variant should be predicted not to impact splicing by at least two out of three *in silico* tools (freely available tools include GeneSplicer, MaxEntScan, NNSplice, SpliceAI, Splicing Sequences Finder (SSF), and varSEAK). Given the potential for poor conservation of genes related to T cell and B cell development among vertebrates, nucleotide conservation is **not required** in order to apply BP7. *Modification Type: General recommendation* |

BP7 positional comparator: "at or beyond the +7 (donor) and -21 (acceptor) positions" — inclusive of +7 and -21.

> **Source note:** BP7 requires agreement of "at least two out of three *in silico* tools" but then lists six named tools. Transcribed as written.

---

## Rules for Combining Criteria

Transcribed verbatim from the specification (v2.2 "Rules for Combining Criteria" section). Code lists in parentheses are the source's own enumerations of which codes count at that strength.

### Pathogenic

1. **1 Very Strong** (PVS1, PS2_Very Strong, PM3_Very Strong) **AND ≥ 1 Strong** (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong)
2. **1 Very Strong** (PVS1, PS2_Very Strong, PM3_Very Strong) **AND ≥ 2 Moderate** (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate)
3. **1 Very Strong AND 1 Moderate AND 1 Supporting** (Supporting list: PS2_Supporting, PS3_Supporting, PM1_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)
4. **1 Very Strong AND ≥ 2 Supporting**
5. **≥ 2 Strong** (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong)
6. **1 Strong AND ≥ 3 Moderate**
7. **1 Strong AND 2 Moderate AND ≥ 2 Supporting**
8. **1 Strong AND 1 Moderate AND ≥ 4 Supporting**

### Likely Pathogenic

1. **1 Very Strong AND 1 Moderate**
2. **1 Strong AND 1 Moderate**
3. **1 Strong AND ≥ 2 Supporting**
4. **≥ 3 Moderate**
5. **2 Moderate AND ≥ 2 Supporting**
6. **1 Moderate AND ≥ 4 Supporting**
7. **1 Strong AND 2 Moderate**
8. **1 Very Strong AND 1 Supporting**

### Benign

1. **≥ 2 Strong** (BS1, BS2, BS4)
2. **1 Stand Alone** (BA1)

### Likely Benign

1. **≥ 2 Supporting** (BS2_Supporting, BP7)
2. **1 Strong** (BS1, BS2, BS4)

**Strength-tier membership as enumerated by the source:**

| Tier | Codes |
|---|---|
| Very Strong | PVS1, PS2_Very Strong, PM3_Very Strong |
| Strong | PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong |
| Moderate | PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate |
| Supporting | PS2_Supporting, PS3_Supporting, PM1_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4 |
| Benign Strong | BS1, BS2, BS4 |
| Benign Supporting | BS2_Supporting, BP7 |
| Stand Alone | BA1 |

---

## Appendices

All appendices below are transcriptions of files distributed with the RAG1 v2.2 specification. Nothing here is supplied from outside the VCEP package.

### Appendix A - RAG1-specified PVS1 flowchart

Source: `PVS1.pdf` ("PVS1: Specified PVS1 flowchart"), 1 page, a single decision-tree image. Transcribed below. Colour semantics per the main specification: **red X** = PVS1 at default (Very Strong) strength *cannot* be applied to RAG1; **magenta/purple** = PVS1 at default strength *can* be applied (critical-domain or full-gene-deletion route); orange boxes = the >10%-of-protein / downstream-pathogenic-variant sub-tree.

The gene-specific yellow annotation, which appears at five points in the flowchart, reads: *"Truncated/altered region is critical to protein function - The NBD domain (aa 394-460), DDBD domain (aa 461-517) and core domain (aa 387-1011) are defined as a region critical to protein function."*

**Branch 1 — Nonsense or Frameshift**
- Predicted to undergo NMD ᵇ → Exon is present in biologically-relevant transcript(s) → **PVS1 (struck out — not applicable to RAG1)**
- Predicted to undergo NMD ᵇ → Exon is absent from biologically-relevant transcript(s) → **N/A**
- Not predicted to undergo NMD ᵇ → Truncated/altered region is critical to protein function (yellow annotation) → **PVS1**
- Not predicted to undergo NMD ᵇ → Role of region in protein function is unknown →
  - LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) → **N/A**
  - LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) →
    - Variant removes >10% of protein → 1+ pathogenic variant present downstream → **PVS1_Strong**
    - Variant removes >10% of protein → No known downstream pathogenic variants → **PVS1_Moderate**
    - Variant removes <10% of protein → **PVS1_Moderate**

**Branch 2 — GT--AG 1,2 splice sites ᵃ**
- Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD ᵇ → Exon is present in biologically-relevant transcript(s) → **PVS1 (struck out)**; Exon is absent → **N/A**
- Exon skipping or use of a cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD ᵇ →
  - Truncated/altered region is critical to protein function (yellow annotation) → **PVS1**
  - Role of region unknown → LoF frequent and/or exon absent → **N/A**
  - Role of region unknown → LoF not frequent and exon present →
    - removes >10% of protein → 1+ pathogenic variant present downstream → **PVS1_Strong**
    - removes >10% of protein → No known downstream pathogenic variants → **PVS1_Moderate**
    - removes <10% of protein → **PVS1_Moderate**
- Exon skipping or use of a cryptic splice site preserves reading frame →
  - Role of region unknown → LoF frequent and/or exon absent → **N/A**
  - Role of region unknown → LoF not frequent and exon present →
    - removes >10% of protein → 1+ pathogenic variant present within deleted region → **PVS1**
    - removes >10% of protein → No known pathogenic variants within deleted region → **PVS1_Moderate**
    - removes <10% of protein → **PVS1_Moderate**
  - Truncated/altered region is critical to protein function (yellow annotation) → **PVS1**

**Branch 3 — Deletion (single exon to full gene)**
- Full gene deletion → **PVS1 ᵈ**
- Single to multi exon deletion — disrupts reading frame and is predicted to undergo NMD ᵇ → Exon present → **PVS1 (struck out)**; Exon absent → **N/A**
- Single to multi exon deletion — disrupts reading frame and is NOT predicted to undergo NMD ᵇ →
  - Truncated/altered region critical (yellow annotation) → **PVS1**
  - Role unknown → LoF frequent and/or exon absent → **N/A**
  - Role unknown → LoF not frequent and exon present →
    - removes >10% of protein → 1+ pathogenic variant present within deleted region → **PVS1_Strong**
    - removes >10% of protein → No known pathogenic variants within deleted region → **PVS1_Moderate**
    - removes <10% of protein → **PVS1_Moderate**
- Single to multi exon deletion — preserves reading frame → (same "role of region unknown" sub-tree as above)
  - Truncated/altered region critical (yellow annotation) → **PVS1**

**Branch 4 — Duplication (≥1 exon in size and must be completely contained within gene)**
- Proven in tandem → Reading frame disrupted and NMD predicted to occur → **PVS1 (struck out)**
- Proven in tandem / Presumed in tandem → No or unknown impact on reading frame and NMD → **N/A**
- Presumed in tandem → Reading frame presumed disrupted and NMD predicted to occur → **PVS1_Strong**
- Proven not in tandem → **N/A**

**Branch 5 — Initiation Codon**
- No known alternative start codon in other transcripts → ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1_Moderate**
- No known alternative start codon in other transcripts → No pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1_Supp**
- Different functional transcript uses alternative start codon → **N/A**

> Footnote markers ᵃ, ᵇ, ᵈ appear on the flowchart but **no footnote text is printed anywhere in the distributed one-page PDF**. Not specified by this VCEP in the distributed file; the markers derive from the Tayoun et al., 2018 SVI PVS1 decision tree (PMID: 30192042).

---

### Appendix B - SVI Recommendation for de novo Criteria (PS2 & PM6), Version 1.1

Source: `PS2_PM6.pdf` — "ClinGen Sequence Variant Interpretation Recommendation for de novo Criteria (PS2/PM6) - Version 1.1", Working Group Page: https://clinicalgenome.org/working-groups/sequence-variant-interpretation/, Date Approved: March 18, 2018, updated May 5, 2021. Changes from v1: Clarified that confirmed/assumed is with regards to parental relationships and not de novo status.

The SVI Working Group proposes a point-based system to determine the strength of *de novo* evidence (PS2 and PM6) based upon three parameters: confirmed parental relationships versus assumed parental relationships status; phenotypic consistency; number of *de novo* observations.

To determine the appropriate strength level to apply for *de novo* occurrence(s), each proband with a *de novo* variant is awarded a point value based upon phenotypic consistency and confirmed or assumed parental relationships (Table 1). The combined point value of all *de novo* occurrences is then compared to Table 2 to determine the applicable evidence strength level. For example, if a *NIPBL* variant was *de novo* in one patient with Cornelia de Lange syndrome, with confirmed parental relationships (2 points; Table 1) and *de novo* in two additional unrelated patients with Cornelia de Lange syndrome with unconfirmed parental relationships (1 + 1 points; Table 1), then VeryStrong evidence level is applied (PS2_VeryStrong) based on combined point value of 4 (Table 2).

**Table 1. Points\* awarded per *de novo* occurrence**

| Phenotypic consistency | *de novo* with confirmed parental relationships | *de novo* with unconfirmed parental relationships |
|---|---|---|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity\*\* | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

\*Note that these points are *not* equivalent to the points used to classify a variant per the Tavtigian et al 2020 "Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines"
\*\*Maximum allowable value of 1 may contribute to overall score

**Table 2. Recommendation for determining the appropriate ACMG/AMP evidence strength level for *de novo* occurrence(s)**

| Supporting (PS2_Supporting or PM6_Supporting) | Moderate (PS2_Moderate or PM6) | Strong (PS2 or PM6_Strong) | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |
|---|---|---|---|
| 0.5 | 1 | 2 | 4 |

**Worked examples and additional considerations (verbatim summary):**

For all uses of *de novo* criteria, the phenotype in the patient must be consistent with the gene/disease association as recommended in the ACMG/AMP guidelines. When the patient's phenotype is consistent with the gene/disease association but not highly specific, we recommend decreasing the points awarded. For example:

- A patient with early infantile epileptic encephalopathy and a *de novo* SIK1 variant with confirmed parental relationships is awarded 1 point. If this patient is the only *de novo* occurrence for the variant, then a Moderate strength level (PS2_Moderate) is applied.
  - If two additional unrelated patients with early infantile epileptic encephalopathy and a *de novo* SIK1 variant with confirmed parental relationships are identified, then the combined point value is 3. For these combined occurrences, a Strong strength level (PS2) is applied as the points reach the Strong threshold (2 points) but not the VeryStrong threshold (4 points).
- A patient with nonsyndromic intellectual disability and a *de novo* ASH1L variant is awarded 0.5 points. If this patient is the only *de novo* occurrence for the variant, then a Supporting strength level (PS2_Supporting) is applied.
  - If a second patient with nonsyndromic intellectual disability and a *de novo* ASH1L variant with confirmed parental relationships is identified, then the combined point value is 1. For these combined occurrences, a Moderate strength level (PS2_Moderate) is applied.
- A patient with developmental delay but no other features of Cornelia de Lange syndrome and a *de novo* NIPBL variant with unconfirmed parental relationships is awarded zero points as this phenotype is not consistent with the gene/disease association. If this patient was the only *de novo* occurrence for the variant, then no *de novo* criteria are applied.

Additional considerations for applying *de novo* criteria based on inheritance:

- **Conditions with X-linked inheritance:** if the variant occurs *de novo* in an unaffected carrier mother, and family history is consistent - i.e., she has no affected brothers/other male relatives apart from her affected son(s) - *de novo* criteria may be applied despite the fact that she is unaffected.
- **Autosomal recessive conditions:** for a *de novo* occurrence in a gene associated with a condition inherited in an autosomal recessive pattern without an additional pathogenic/likely pathogenic variant identified, the strength of evidence should be decreased by one level. *(RAG1 is autosomal recessive, so this consideration applies.)*
- **Mosaicism:** for cases with apparent germline mosaicism (multiple affected siblings with both parents negative for the variant), parental relationships must be confirmed in order for *de novo* criteria to apply.

**Threshold comparators:** Table 2 values are stated as bare point values; the worked example clarifies that a tier is reached when points "reach the ... threshold", i.e. inclusive (`>=`).

---

### Appendix C - PS3/BS3 Functional Evidence (`SCID VCEP PS3_BS3.xlsx`)

Workbook distributed as "SCID VCEP PS3_BS3: Functional Evidence (RAG1)". Three worksheets, all readable.

#### C.1 Sheet "General Class of Assay Summary"

| Gene | General Class of Assay | PMIDs |
|---|---|---|
| RAG1 | V(D)J recombination assay | PMID: 11313270, PMID: 24290284 |

#### C.2 Sheet "RAG1 Assay Instance Details"

Two approved assay instances, transposed here from the source's column-per-instance layout.

| Field | Instance 1 | Instance 2 |
|---|---|---|
| PMID | 11313270 | 24290284 |
| Gene | RAG1 | RAG1 |
| DOI / link | 10.1182/blood.v97.9.2772 | 10.1016/j.jaci.2013.10.007 |
| Author | Corneo...de Villartay | Lee...Notarangelo |
| Year | 2001 | 2014 |
| General Class of Assay | V(D)J recombination assay | V(D)J recombination assay |
| Assay (General Description) | SV40-transformed fibroblasts were electroporated with wild type or variant RAG1 cDNA constructs and extrachromosomal V(D)J recombination substrates. The extrachromosomal substrates were recovered, transformed in E. coli, and plated on X-Gal plates to determine recombination frequency via blue/white screening | Murine Rag1-/- Abl pro-B cells were transduced with a retroviral vector containing wild type, mock, or variant human RAG1 cDNA, blocked in the G0/G1 cell cycle phases for 96 hours, and harvested for analysis by flow cytometry |
| Material used | SV40-transformed fibroblasts electroporated with wild type or variant RAG1 cDNA constructs and extrachromosomal V(D)J recombination substrates | Murine Rag1-/- Abl pro-B cells with a stable single integration of the pMX-INV GFP cassette flanked by two coding recombination signal sequences |
| Readout type | Quantitative | Quantitative |
| Readout description | Number of blue colonies as a read out for recombination frequency | GFP expression as a readout of recombination activity (reported as a percentage of the recombination activity of wild type RAG1) |
| Biological replicates (met/not met) | Not reported | None (not met) |
| Technical replicates (met/not met); description | Not reported | **`2022-03-05 00:00:00`** — see source note below |
| Basic positive control | Cells expressing wild type RAG1 | Wild type RAG1 cDNA-transduced cells |
| Basic negative control | Not reported | Empty vector-transduced cells |
| Validation controls P/LP (#) | 0 | 0 (none reported by authors as known pathogenic variants) |
| Validation controls B/LB (#) | 0 | 3 (described as "known polymorphisms": G99S, H249R, and K820R) |
| Statistical analysis | Not reported | Mann-Whitney U test |
| Threshold for normal readout | Recombination frequency similar to wild type RAG1 (numeric threshold not reported) | Wild type-like recombination activity (numeric threshold not reported) |
| Threshold for abnormal readout | Reduced recombination frequency (numeric threshold not reported) | Reduced recombination activity (numeric threshold not reported) |
| Approved assay (y/n) | y | y |
| **Proposed strength** | **PS3_Supporting** | **PS3_Moderate** |
| Variant(s) Tested | c.256_257del (p.Lys86fs), c.999T>A (p.Tyr333Ter), c.1210C>T (p.Arg404Trp), c.1421G>A (p.Arg474His), c.1871G>A (p.Arg624His), p.Thr173fsTer27 (nucleotide change not reported), c.2158G>T (p.Gly720Cys), c.2194C>T (p.Leu732Phe), p.Ser875fs (nucleotide change not reported), c.2918G>A (p.Arg973His), c.2974A>G (p.Lys992Glu) | 79 variants (see Table E1 in publication and R plot of data below) |
| Notes | (blank) | Curated a set of 11 known pathogenic and known benign validation controls in order to use evidence from this assay instance at PS3_Moderate. All known pathogenic and known benign controls were correctly classified as abnormal and normal, respectively, by this instance of the V(D)J recombination assay. See supplemental table for classifications of these validation controls. |

> **Source note (apparent spreadsheet error):** the "Technical replicates" cell for Lee et al., 2014 (cell `C14`) is stored as the Excel date serial `2022-03-05 00:00:00` with number format `m\-d`, i.e. it renders on screen as **`3-5`**. This is a text entry auto-converted to a date by Excel; the intended text cannot be recovered from the file. Not inferred here.

#### C.3 Sheet "RAG1 Lee et al., 2014 Validatio[n Controls]"

Full transcription (11 validation controls). Column "Mean V(D)J Recombination Activity Level in Lee et al., 2014" is a percentage of wild type.

| Variant (Nucleotide) | Variant (Protein) | Overall Classification | ACMG/AMP Codes Applied | Mean Activity | Assay Result Interpretation (per VCEP-established thresholds) | Validation Control | Notes |
|---|---|---|---|---|---|---|---|
| c.256_257del | p.Lys86fs | Pathogenic | PM3_Strong, PVS1_Strong, PP1, PP4, PM2_Supporting | 2.7 | Abnormal | Known Pathogenic | RAG1 is encoded by a single exon, mitigating concerns about the ability of cDNA expression experiments to model the behavior of variants subject to nonsense mediated decay. |
| c.295G>A | p.G99S | Benign | BA1 | 113.2 | Normal | Known Benign | |
| c.322C>T | p.R108X | Pathogenic | PM3_Strong, PVS1_Strong, PP4, PM2_Supporting | 1.8 | Abnormal | Known Pathogenic | RAG1 is encoded by a single exon, mitigating concerns about the ability of cDNA expression experiments to model the behavior of variants subject to nonsense mediated decay. |
| c.746A>G | p.H249R | Benign | BA1 | 112.2 | Normal | Known Benign | |
| c.1186C>T | p.R396C | Pathogenic | PM3_Strong, PM1, PM5, PP1, PP4, PM2_Supporting | 0.6 | Abnormal | Known Pathogenic | |
| c.1331C>T | p.A444V | Pathogenic | PM3_VeryStrong, PM1, PP4, PM2_Supporting | 1.4 | Abnormal | Known Pathogenic | |
| c.1303A>G | p.M435V | Pathogenic | PM3_VeryStrong, PM1, PP4, PM2_Supporting | 23.6 | Abnormal | Known Pathogenic | |
| c.1346G>A | p.R449K | Benign | BA1 | 92.1 | Normal | Known Benign | |
| c.1682G>A | p.R561H | Pathogenic | PM3_VeryStrong, PM5, PP4, PM1_Supporting, PM2_Supporting | 2 | Abnormal | Known Pathogenic | |
| c.2210G>A | p.R737H | Pathogenic | PM3_VeryStrong, PP1, PP4, PM1_Supporting, PM2_Supporting | 0.2 | Abnormal | Known Pathogenic | |
| c.2459A>G | p.K820R | Benign | BA1 | 117.9 | Normal | Known Benign | |

This is a **lookup/validation dataset**, not a rule: it documents the controls used to justify PS3_Moderate for the Lee et al., 2014 assay instance. It is not a list of pre-classified variants for general use.

#### C.4 Embedded figure

The workbook embeds one image (`xl/media/image1.png`, anchored below the assay-instance table): an R bar plot titled on its axes "Mean Recombination Activity (% of wild type RAG1)" (y) vs "RAG1 Variant" (x), with error bars, showing all 79 variants from Lee et al., 2014 ranked from lowest to highest activity. The lowest-activity variants shown include p.C730F, p.E722K, p.E965X, p.L411P, p.I732P, p.M458SfsX34, p.P786L, p.R410Q, p.R410W; the highest include p.G99S, p.K820R, p.H612R, p.R474C. This is a **graphical lookup** of per-variant activity values; individual bar heights are not numerically labelled in the image and are not transcribed here.

---

### Appendix D - SVI Recommendation for in trans Criterion (PM3), Version 1.0 (Table 1 updated 17 October 2025)

Source: `PM3 Criterion.pdf` — "ClinGen Sequence Variant Interpretation Recommendation for in trans Criterion (PM3) - Version 1.0", Working Group Page: https://clinicalgenome.org/working-groups/sequence-variant-interpretation/, Date Approved: May 2, 2019; Table 1 updated October 17, 2025.

The SVI Working Group proposes a point-based system to determine the strength of *in trans* observations (PM3) based upon variant phasing and classification of the variant occurring on the other allele. Additionally, SVI recommends a revision to the criterion definition to indicate this evidence should only be applied if the individual is affected:

> **SVI revision to PM3:** For recessive disorders, detected in *trans* with a pathogenic **or likely pathogenic** variant **in an affected patient**

To determine the appropriate strength level to apply for in *trans* occurrence(s), each proband is awarded a point value based upon phasing of the two variants in question (confirmed in *trans* versus unknown) and classification of the variant on the other allele (Table 1). The combined point value of all proband occurrences is then summed and compared to Table 2 to determine the applicable evidence strength level. For example, if assessing *PAH* variant NM_000277.3:c.1208C>T (p.Ala403Val) and the variant was confirmed in *trans* with Likely pathogenic variant c.1301C>A (p.Ala434Asp) in one proband (1.0 points; Table 1) and confirmed in *trans* with Pathogenic variant c.331C>T (p.Arg111Ter) in another proband (1.0 points, Table 1), then PM3 at the Strong strength level (PM3_Strong) is applicable (2.0 points total; Table 2).

**Table 1. Points awarded per in *trans* proband**

| Classification/Zygosity of other variant | Confirmed in *trans* | Phase unknown |
|---|---|---|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence — Non-consanguineous\*\* *(no max)* | 1.0 | 1.0 |
| Homozygous occurrence — Consanguineous\*\* *(no max)* | 0.5 | 0.5 |
| Uncertain significance variant *(max point 0.5)* | 0.25 | 0 |

Column header in the updated table: **"Points per Proband-Family\*"**.

\*Multiple probands from separate nuclear families that are later found to have identity-by-descent should only be counted once.
\*\*When consanguinity is not known or reported: if family IS NOT from a bottlenecked population (as defined by gnomAD), assume non-consanguinity; otherwise, assume consanguinity. If genetic ancestry of the family cannot be determined, assume consanguinity.

**Table 2. Recommendation for determining the appropriate evidence strength level for PM3**

| PM3_Supporting | PM3 | PM3_Strong | PM3_VeryStrong |
|---|---|---|---|
| 0.5 | 1.0 | 2.0 | 4.0 |

**Considerations (verbatim):**

- **Allele Frequency** - Application of PM3 is contingent on the allele frequency of the variant being assessed and the variant presumably on the other allele both being sufficiently rare (meets PM2 threshold). This contingency is to avoid incorrect application of PM3 to high frequency variants that are likely to occur in *trans* with P/LP variants based on frequency.
- **Phasing** - If the phase cannot be determined, it is recommended that at least two different LP/P variants (depending on classifications) are needed to equal the weight of one LP/P co-occurrence confirmed in *trans*.
  - In confirmation of phasing, if only one parent is tested and found to carry one allele, variants can be counted as in *trans*. For example, assessing PAH variant c.601C>T (p.His201Tyr) and variant was identified in PKU proband who also carries known pathogenic variant c.734T>C (p.Val245Ala). Only the mother is available for testing and the mother only carries c.734T>C (p.Val245Ala) variant, then variants can be considered in *trans*.
- **Classification** - Probands should be weighted less when the variant on the other allele is of uncertain significance and rare (meets PM2); however, weight may vary by gene size as larger genes are more likely to have a second variant by chance (default 0.25 points). If the variant on the other allele is classified as P or LP, weighting depends on phasing (see *Phasing* above), with P/LP being weighted equally if confirmed in trans and different point values per proband if phasing is unknown (0.5 points and 0.25 points, respectively). To avoid circularity, in all instances (phasing confirmed or unknown), the classification of the variant on the other allele should not use evidence from the variant being interrogated.
- **Homozygous occurrences** - For homozygous occurrences, the default weight is dropped to 0.5 points, as a rare homozygous occurrence may be due to consanguinity. A recommended max of 1.0 points of all homozygous cases is suggested to prevent overclassification of homozygous occurrences in the absence of additional data.

> **Source notes on this file:** (1) The distributed PDF carries a "Wondershare PDFelement" trial watermark across both pages. (2) The "Considerations — Homozygous occurrences" paragraph still recommends "a max of 1.0 points of all homozygous cases", while Table 1 as updated marks both homozygous rows "*(no max)*". This is an internal contradiction within the distributed SVI document; both statements are transcribed as written and neither has been reconciled here.

---

### Appendix E - PM3 SVI recommendations / PM3 Minor Amendments (two files, identical content)

Sources: **`PM3.docx`** — advertised in the specification's Files & Images list as *"PM3: svi recommendations: October 2025 Group Responses to Minor Updates"* — and **`PM3 Minor Amendments 12.12.2025.docx`**, advertised with an **empty description** in the Files & Images list.

**These two .docx files have identical readable content.** Verified: identical table (6 rows x 3 columns), identical footnotes, identical SVI comment/VCEP response text, and a byte-identical embedded image (`word/media/image1.png`, MD5 `3ca0922f9a23860943c1915291c9ebbc`). They differ only in packaging metadata and Word run-splitting: `PM3.docx` was created 2025-10-10 and last modified 2025-10-10 by "Chinn, Ivan Kingyue" (revision 10); `PM3 Minor Amendments 12.12.2025.docx` was created 2025-11-11, last modified 2025-12-12 by "Sulit, Monica Corpuz" (revision 1). Neither file carries an internal title, heading, or letterhead — the titles above exist only in the ClinGen Files & Images list, not inside the documents. Neither file contains tracked changes (`w:ins`/`w:del`) or comments. The single transcription below therefore serves for both.

Each document is the amended PM3 Table 1, followed by the embedded PM3 Table 2 image, followed by SVI comments and the SCID VCEP's responses to each.

**Amended table as it appears in both documents:**

| Classification/Zygosity of other variant | Points per Proband-Family\* — Confirmed in trans | Points per Proband-Family\* — Phase unknown |
|---|---|---|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence — Non-consanguineous\*\* *(no max)* | 1.0 | 1.0 |
| Homozygous occurrence — Consanguineous\*\* *(no max)* | 0.5 | 0.5 |
| Uncertain significance variant *(max point 0.5)* | 0.25 | 0 |

\* Multiple probands from separate nuclear families that are later found to have identity-by-descent should only be counted once.
\*\* When consanguinity is not known or reported: if family IS NOT from a bottlenecked population (as defined by gnomAD), assume non-consanguinity; otherwise, assume consanguinity. If genetic ancestry of the family cannot be determined, assume consanguinity.

**SVI Comments and VCEP responses (verbatim):**

1. *SVI:* "Prefer N/A to repeating the 1.0 and 0.5"
   *VCEP:* "The SCID VCEP deliberated this point. Our geneticists pointed out that apparent homozygous variants could result from hemizygosity, which may be undetected if the parents are not sequenced (i.e., "Phase unknown"). Because of the likelihood that authors may not bother to sequence the parents in homozygous situations, especially in older publications, the VCEP experts preferred to leave the numbers in place."
2. *SVI:* "Update "max point 0.5 per family" to "max point 0.5" as in original specs. Please replace "max point 0.5 per family" from the Homozygous Consanguineous and indicate "no max". Rationale: "per proband" is a rule for the whole table in general (per the table title); Multiple cases per family will inherently be counted as PP1 instead of multiple PM3s"
   *VCEP:* "The SCID VCEP agreed and made the changes to the table. To minimize confusion for biocurators and experts as much as possible between proper application of PM3 vs. PP1 (which we have definitely observed, even in sustained curations), we changed "Proband" to "Proband-Family"."
3. *SVI:* "What to do if you don't know about consanguinity"
   *VCEP:* "The VCEP decided to use gnomAD definitions to specify assumption of non-consanguinity for families from non-bottlenecked populations and assumption of consanguinity otherwise. A footnote was added to the Table."
4. *SVI:* "If the VCEP wishes, they can provide an asterisk footnote that supports the notion that "multiple probands from separate nuclear families that are later found to have identity-by-descent should only be counted once.""
   *VCEP:* "We added this footnote to the Table."

**Embedded image** (`word/media/image1.png`, positioned after the two table footnotes and before "SVI Comments:") : PM3 Table 2, unchanged — a four-cell colour-coded strip reading **PM3_Supporting 0.5 | PM3 1.0 | PM3_Strong 2.0 | PM3_VeryStrong 4.0**.

> **Do these documents agree with `PM3 Criterion.pdf` Table 1?** **Yes.** The table in both .docx files is equivalent to Table 1 in `PM3 Criterion.pdf` (whose header states "Table 1 updated October 17, 2025"): same "Points per Proband-Family\*" spanning header, same four data rows and eight values, same "(no max)" annotations on both homozygous rows, same "(max point 0.5)" annotation on the uncertain-significance row, and both footnotes word-for-word. The embedded Table 2 image is identical in content to Table 2 in the PDF. **No value, threshold, or footnote differs among the three PM3 files.**
>
> **Do `PM3.docx` and `PM3 Minor Amendments 12.12.2025.docx` agree with each other?** **Yes — they are the same document.** See the header of this appendix.
>
> **The main RAG1 specification PDF contains no PM3 point table of its own**, so there is no table in the main document for these amendments to contradict — the main spec only points to the attached PM3 criterion document. The only residual inconsistency is *within* the SVI PM3 PDF itself (Table 1 "no max" vs. the Considerations paragraph's "recommended max of 1.0 points of all homozygous cases"), noted in Appendix D; the .docx files reproduce only Table 1 and so do not carry that contradiction.

---

### Appendix F - PP1 segregation thresholds (Oza et al., Tables 4a and 4b)

Source: `PP1.pdf` — two pages excerpted from the Oza et al. author manuscript (*Hum Mutat*, available in PMC 2019 November 01), pages 35-36. This is the document referenced by the VCEP as "Attached document: PP1 specifications" and corresponds to PMID: 30311386.

**Table 4a: Recommendations for PP1 (segregation evidence)**

| | Supporting | Moderate | Strong |
|---|---|---|---|
| Likelihood | 4:1 | 16:1 | 32:1 |
| LOD Score | 0.6 | 1.2 | 1.5 |
| Autosomal dominant threshold | 2 affected segregations | 4 affected segregations | 5 affected segregations |
| Autosomal recessive threshold | See Table 4b | See Table 4b | See Table 4b |

*RAG1 is autosomal recessive, so Table 4b is the operative lookup.*

**Table 4b: Recommendations for autosomal recessive segregation evidence (PP1)**

LOD scores by number of affected segregations (rows) × unaffected recessive segregations (columns), "General Recommendations (Phenocopy not an issue)".

| Affected ↓ / Unaffected → | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
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

Cells in Table 4b are colour-coded green/orange/red in the source, corresponding to the Supporting (≥0.6) / Moderate (≥1.2) / Strong (≥1.5) LOD bands of Table 4a.

**Table 4b footnotes (verbatim):** Affected segregations are counted in rows and unaffected segregations in columns. Affected segregations are affected family members in whom biallelic compound heterozygous or homozygous variants segregates. Unaffected segregations are defined as unaffected family members, typically siblings, who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants identified in the proband, or a heterozygous carrier for a single variant. Unaffected, carrier parents do NOT count as unaffected segregations. There may be scenarios where individuals other than siblings could be counted as segregations, such as in families where one parent is affected with the autosomal recessive disorder, in large families with multiple branches, or in consanguineous families.

Each cell shows the LOD score of each combination of affected and unaffected segregations. LOD scores were calculated using a simplified LOD score formula, as described in Strande et al., 2017.

**RAG1-specific addition (from the main specification):** unaffected individuals contributing to the calculated LOD score must be heterozygous carriers of one of the variants observed in the affected individuals (i.e. do not count wild-type/wild-type individuals). Note that this is *narrower* than the Oza et al. footnote, which permits counting individuals who are "either wild-type for both variants identified in the proband, or a heterozygous carrier for a single variant"; the VCEP's specification is the operative rule for RAG1.

---

## Source Notes, Typos and Internal Inconsistencies

Transcribed as found; nothing below has been silently corrected.

1. **"with two modifications" followed by five bullets** — PVS1 VCEP Specifications block. The Very Strong row says "with two specifications" and lists two.
2. **PS2/PM6 "Reduce points per proband by half if the phase is unconfirmed."** — "phase" is the PM3 concept; for *de novo* criteria the SVI parameter is *confirmed vs. unconfirmed parental relationships*. Read literally against SVI Table 1, halving is exactly what the "unconfirmed parental relationships" column does. Likely a wording slip by the VCEP; transcribed verbatim.
3. **PM5 section header says "For nonsense variants:"** but the Moderate and Supporting strength rows also carry the classic missense PM5 guidance ("Applicable at default strength (PM5) if previously established variant is classified as pathogenic..."). The Strong row carries no missense provision.
4. **PS1 rows contain no base statement** — both the Strong and Moderate rows begin "It can also be applied for splice variants ...", with no preceding "It can be applied..." sentence anywhere in the specification.
5. **BP7 requires "at least two out of three *in silico* tools"** but then names six tools.
6. **BS3 is Not Applicable**, yet the functional-evidence workbook distributed with the spec is named "SCID VCEP PS3_BS3". It contains PS3 evidence only.
7. **Assay workbook date corruption**: "Technical replicates" for Lee et al., 2014 is stored as the date `2022-03-05` and displays as `3-5` (see Appendix C.2).
8. **Validation-control count**: the assay-instance sheet records "Validation controls B/LB (#) = 3 (described as 'known polymorphisms': G99S, H249R, and K820R)", but the validation sheet lists **four** Known Benign controls (adds c.1346G>A p.R449K). The "3" appears to describe what the *authors* reported; the VCEP curated 11 controls in total (7 Known Pathogenic + 4 Known Benign), consistent with the Notes cell.
9. **PM3 Criterion PDF internal contradiction**: Table 1 marks homozygous rows "(no max)" while the Considerations text still recommends "a max of 1.0 points of all homozygous cases". See Appendix D.
10. **PM3 Criterion PDF carries a "Wondershare PDFelement" trial watermark** on both pages.
11. **PVS1 flowchart footnote markers ᵃ, ᵇ, ᵈ have no printed footnote text** in the distributed one-page PDF.
12. **PP4 footnote marker ¹ is attached both to the first evidence row and to "≥4 Points: PP4_Strong"** in the attached PP4 document, but only one footnote text is given (the PIDTC 2022 diagnostic-criteria note).
13. **Release notes reference a "RAG1 Corrections 1.6.26 file" that is neither advertised nor shipped.** The v2.2 release notes state "Uploaded RAG1 Corrections 1.6.26 file", followed by five bullets (PP4 changes, PS3_Moderate edit, PM1 caveat, BS2_Strong, BS2_Supporting 1-homozygote requirement). The specification's own **Files & Images list does not contain any Corrections item** — it lists exactly eight supplementary entries (PP4 - RAG1, PM3 Criterion, PVS1, SCID VCEP PS3_BS3, PS2_PM6, PM3: svi recommendations, PP1, PM3 Minor Amendments 12.12.2025), all nine files (with the main PDF) present in this download. So the file is mentioned only in prose, is not offered for download, and was not distributed. Four of the five changes it is said to carry (PP4, PM1 caveat, BS2_Strong, BS2_Supporting minimum-1-homozygote) **are** visible in the v2.2 criteria tables. The fifth, the "PS3_Moderate specification edit", is **not** identifiable: the PS3_Moderate threshold text (`<25%` of wild-type activity) is unchanged from the prior version, so the Corrections document's own wording is both unavailable and unreconstructable. **In particular, the PS3 gate that sibling SCID VCEP specifications (ADA, DCLRE1C, JAK3, RAG2) carry in their Corrections files — "at least one previously observed proband meeting PP4 is required to apply PS3 at any strength" — does not appear anywhere in the RAG1 package.** A full-text search of all nine RAG1 source files for that sentence and its components returns nothing: RAG1's PS3 rows state only the animal-model (Strong), <25% (Moderate) and 25-60%/Corneo (Supporting) conditions, with no PP4 precondition. **A PP4 gate on PS3 is therefore Not specified by this VCEP for RAG1 and must not be applied by analogy to the sibling specs.**
14. **All nine advertised files were downloaded and read for this revision.** An earlier generation of this guideline recorded "PM3: svi recommendations: October 2025 Group Responses to Minor Updates" as missing because a downloader filename collision dropped it. It is present here as `PM3.docx` and is fully transcribed in Appendix E. Its content proved to be identical to `PM3 Minor Amendments 12.12.2025.docx`.
15. **The release notes undercount the PM3 uploads.** They say "Uploaded **two** files to address minor PM3 changes" and name "PM3 Criterion..." and "PM3: svi recommendations...". The Files & Images list actually carries **three** PM3 items, the third being "PM3 Minor Amendments 12.12.2025", whose Files & Images **description is empty** (the entry reads "PM3 Minor Amendments 12.12.2025:" with nothing after the colon). That third file duplicates the second.
16. **BA1 and BS1 use different Whiffin/Ware parameters** (BA1: prevalence 1:5,000, penetrance 50%; BS1: prevalence 1:50,000, penetrance 100%). Both are stated by the VCEP; this parameter split is intentional in ClinGen practice (BA1 uses the more permissive assumptions) and is recorded here only for completeness.
17. **Rules for Combining Criteria — subset relationships.** The Likely Pathogenic list contains "1 Strong AND 2 Moderate", while the Pathogenic list contains "1 Strong AND 2 Moderate AND ≥ 2 Supporting". As written, a variant meeting the P combination also meets an LP combination; the higher classification governs per standard ACMG/AMP practice. The specification does not state a tie-break rule.

### Frequency and numeric comparator summary

| Criterion | Threshold | Comparator |
|---|---|---|
| BA1 (Stand Alone) | gnomAD popmax filtering AF 0.00872 | strict `>` |
| BS1 (Strong) | gnomAD popmax filtering AF 0.00195 | strict `>` |
| PM2 (Supporting) | gnomAD popmax filtering AF 0.000102 | strict `<`; plus **zero** homozygotes in gnomAD |
| BS2 (Strong) | 3 homozygotes | inclusive ("at least 3") |
| BS2 (Supporting) | 1 homozygote | inclusive ("at least 1") |
| PS3 (Moderate) | 25% of wild-type V(D)J activity | strict `<` |
| PS3 (Supporting) | 25-60% of wild-type V(D)J activity | range as written (endpoints not further qualified) |
| PP3 (Supporting) | SpliceAI delta 0.2 | inclusive `>=` ("greater than or equal to") |
| PP4 not met | 1 point | strict `<` |
| PP4 (Supporting) | 1 to 2 points | lower inclusive, upper strict (`1 - <2`) |
| PP4 (Moderate) | 2 to 4 points | lower inclusive, upper strict (`≥2 - <4`) |
| PP4 (Strong) | 4 points | inclusive `≥` |
| PP4 table: TCRVα7.2 | 2% in CD3+ T lymphocytes | strict `<` |
| PP4 table: 9G4+ / 9G4int / 9G4hi | 10% / 5% / 5% in CD19+ B cells | strict `>` |
| PM5 (Strong / Moderate / Supporting) | 4+ / 2+ / 1 informative-variant points | inclusive at the stated value |
| PVS1 strength modification | 10% of protein removed | strict `>` (and `<` on the opposite branch); the flowchart has no branch for exactly 10% |
| PM3 (SVI Table 2) | 0.5 / 1.0 / 2.0 / 4.0 points | inclusive (points "reach the threshold") |
| PP1 (Oza Table 4a) | LOD 0.6 / 1.2 / 1.5 | inclusive |
| BP7 intronic window | +7 (donor), -21 (acceptor) | inclusive ("at or beyond") |

---

## Version History

| Version | Released | Notes |
|---|---|---|
| 2.2 | 5/15/2026 | Edited Rules for Combining Criteria to reflect standard combinations plus (A) 1 very strong + 1 supporting = Likely Pathogenic and (B) 1 Strong Benign = Likely Benign. Refreshed and saved Rules for Combining Criteria. Uploaded two files to address minor PM3 changes: "PM3 Criterion: October 2025 Version, Minor Updates" and "PM3: svi recommendations: October 2025 Group Responses to Minor Updates". Uploaded RAG1 Corrections 1.6.26 file: changes regarding PP4 criteria; PS3_Moderate specification edit; added caveat to PM1; added BS2_Strong strength; added BS2_Supporting requirement to have minimum of 1 homozygote. |

Earlier version history is not included in the distributed v2.2 specification.

---

## Distributed Files Inventory

| File (as advertised) | Local file | Opened | Transcribed in |
|---|---|---|---|
| ClinGen ACMG Specifications RAG1 v2.2 | `ClinGen_ACMG_Specifications_RAG1_v2.2.pdf` (20 pp.) | Yes | Body of this document |
| PM3 Minor Amendments 12.12.2025 *(no description given in Files & Images)* | `PM3 Minor Amendments 12.12.2025.docx` (1 table, 1 embedded PNG) | Yes (incl. embedded PNG) | Appendix E |
| PP4 - RAG1: 2025 updates | `PP4 - RAG1.pdf` (1 p.) | Yes | PP4 section |
| PM3 Criterion: October 2025 Version, Minor Updates | `PM3 Criterion.pdf` (2 pp.) | Yes | Appendix D |
| PVS1: Specified PVS1 flowchart | `PVS1.pdf` (1 p.) | Yes | Appendix A |
| SCID VCEP PS3_BS3: Functional Evidence (RAG1) | `SCID VCEP PS3_BS3.xlsx` (3 sheets + 1 embedded PNG) | Yes | Appendix C |
| PS2_PM6: SVI recommendations for de novo criteria | `PS2_PM6.pdf` (2 pp.) | Yes | Appendix B |
| PM3: svi recommendations: October 2025 Group Responses to Minor Updates | `PM3.docx` (1 table, 1 embedded PNG) | Yes (incl. embedded PNG) | Appendix E |
| PP1: PP1 specifications | `PP1.pdf` (2 pp.) | Yes | Appendix F |
| *(RAG1 Corrections 1.6.26 — named in release-note prose only)* | **not advertised in Files & Images; not distributed** | n/a | See source note 13 |

**9 of 9 advertised files downloaded, opened and transcribed.** Verification method per file: 20-page and 1-2 page PDFs read page-by-page as rendered images plus a `pypdf` text extraction cross-check; `.docx` files read with `python-docx` (body paragraphs, tables, headers/footers, core properties) with their `word/media/` payloads extracted and viewed; `.xlsx` read with `openpyxl` across all three worksheets with the embedded chart image extracted and viewed.

---

*This document was compiled from the ClinGen VCEP specification and its distributed supplementary files. Content the VCEP did not specify is marked "Not Applicable" or "Not specified"; no external ACMG/AMP or SVI content has been introduced beyond the SVI documents the VCEP itself distributed. For the most current version, please refer to the ClinGen website.*
