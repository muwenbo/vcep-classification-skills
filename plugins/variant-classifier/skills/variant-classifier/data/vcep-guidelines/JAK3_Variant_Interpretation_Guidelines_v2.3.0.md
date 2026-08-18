# ClinGen Severe Combined Immunodeficiency Disease VCEP Variant Interpretation Guidelines for JAK3

**Version:** 2.3
**Released:** 6/1/2026
**Affiliation:** Severe Combined Immunodeficiency Disease VCEP
**Type:** Richards et.al., 2015 - Combining rules
**DOI:** 10.5281/zenodo.21434489
**Rights Holder:** The Clinical Genome Resource (ClinGen)
**Source basis:** ClinGen Criteria Specification Registry record GN121 (`ClinGen_ACMG_Specifications_JAK3_v2.3.pdf`) plus the nine supplementary files distributed with it. Content below is transcribed from those files only.

**Release Notes (as published for v2.3):**
> Uploaded JAK3 Corrections file
> - Added caveat to PM1 "Caveat: Variant must not meet BS1, BS2, or BA1 criteria."

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | JAK3 (HGNC:6193) |
| **HGNC Name** | Janus kinase 3 |
| **Transcript** | NM_000215.4 |
| **Disease** | T-B+ severe combined immunodeficiency due to JAK3 deficiency (MONDO:0010938) |
| **Inheritance** | Autosomal recessive inheritance |
| **Keywords** | human biology genomics variant, variant classification, clingen, disease standards, JAK3, NM_000215.4, Autosomal recessive inheritance, T-B+ severe combined immunodeficiency due to JAK3 deficiency |

---

## Source Inventory

Every file distributed with GN121 was opened and read. None failed to open.

| # | File | Type | Status |
|---|------|------|--------|
| 1 | `ClinGen_ACMG_Specifications_JAK3_v2.3.pdf` (20 pp.) | Main specification | Read in full |
| 2 | `PVS1.pdf` (1 p.) | PVS1 flowchart | Read; transcribed (Appendix A) |
| 3 | `PS2_PM6.pdf` (2 pp.) | SVI de novo recommendation v1.1 | Read; transcribed (Appendix B) |
| 4 | `PM3 Criterion.pdf` (2 pp.) | SVI in trans recommendation v1.0, Table 1 updated Oct 17 2025 | Read; transcribed (Appendix C) |
| 5 | `PM3 Minor Amendments 12.12.2025.docx` | Amendment / SVI correspondence | Read incl. embedded PNG; transcribed (Appendix D) |
| 6 | `PP1.pdf` (2 pp.) | Oza et al. Tables 4a / 4b | Read; transcribed (Appendix E) |
| 7 | `PP4 - JAK3.pdf` (1 p.) | PP4 points table, "2025 Updates" | Read; transcribed (Appendix F) |
| 8 | `SCID VCEP PS3_BS3 Funcational Evidence (JAK3).xlsx` | Functional assay workbook, 2 sheets | Read in full; transcribed (Appendix G) |
| 9 | `JAK3 Corrections 1.6.26.docx` | Erratum #2 | Read; transcribed (Appendix H) |
| 10 | `JAK3 Corrections 5.29.2026.docx` | Erratum #3 | Read; transcribed (Appendix I) |

Filename typo preserved verbatim: **"Funcational"** (for "Functional") in file 8.

### Amendment / correction files — order and reconciliation

The specification ships **three** amendment documents. In chronological order:

| Order | Document | Subject | Reflected in the v2.3 criteria tables? |
|-------|----------|---------|----------------------------------------|
| 1 | PM3 Minor Amendments **12.12.2025** | PM3 Table 1 wording ("Proband" → "Proband-Family", "no max" on homozygous rows, consanguinity footnote, identity-by-descent footnote) | **Yes, indirectly.** The main spec's PM3 section only points to the attached PM3 criterion document; the attached `PM3 Criterion.pdf` Table 1 already carries all four amended elements. |
| 2 | JAK3 Corrections **1.6.26** | PS3, BS2, PP4 | **Partly — see conflict below.** BS2 and PP4 match the v2.3 tables exactly. PS3 does **not**. |
| 3 | JAK3 Corrections **5.29.2026** | PM1 caveat | **Yes.** The v2.3 PM1 section carries "Caveat: variant must not meet BS1, BS2, or BA1 criteria," and the release notes name this change. |

**Documented conflict (erratum vs. tables).** `JAK3 Corrections 1.6.26.docx` states under PS3 Supporting:

> "At least one previously observed proband with the JAK3 variant meeting PP4 is required to apply PS3 at any strength on the basis of a cellular model/in vitro study."

This sentence is **absent from the PS3 section of the v2.3 specification tables**, which list only the assay statement and the approved assay instance. The requirement is therefore transcribed here in Appendix H but is **not** reproduced as if it were part of the operative PS3 table. Curators should note the discrepancy; this guideline does not reconcile it.

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
Caveats (as printed in the specification):
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:** See attached PVS1 flowchart (transcribed in **Appendix A**).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)). *Modification Type: General recommendation, Gene-specific* |
| **Strong** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification: For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 24, or variants in the last 50 nucleotides of the penultimate exon after c.3157, codon 1053, in exon 23), at least one pathogenic variant **must be** present downstream in order to apply PVS1_Strong. *Modification Type: General recommendation, Gene-specific* |
| **Moderate** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification: For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 24, or variants in the last 50 nucleotides of the penultimate exon after c.3157, codon 1053, in exon 23), when at least one pathogenic variant is **not** present downstream downgrade to PVS1_Moderate. *Modification Type: General recommendation* |
| **Supporting** | Not listed as a separate strength row in the specification. PVS1_Supp does appear as an outcome in the attached flowchart (Initiation Codon branch, no pathogenic variant upstream of closest potential in-frame start codon). |

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

| Strength | Criteria |
|----------|----------|
| **Strong** | It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T. Applicable if the previously established variant is classified as **pathogenic** by SCID VCEP specifications for *JAK3*. *Modification Type: Gene-specific* |
| **Moderate** | It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be likely pathogenic, can use PS1 for c.105+1G>T. Applicable if the previously established variant is classified as **likely pathogenic** by SCID VCEP specifications for *JAK3*. *Modification Type: Gene-specific, Strength* |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** The following guidelines should be used when determining the phenotypic consistency of each proband:
- "Phenotype highly specific for gene" proband must meet at least PP4_Moderate criteria;
- "Phenotype consistent with gene but not highly specific" proband must meet PP4 criteria;
- "Phenotype consistent with gene but not highly specific and high genetic heterogeneity": proband has been asserted to have a SCID phenotype but does not meet PP4 criteria;
- Reduce points per proband by half if the phase is unconfirmed.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |
| **Strong** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |
| **Moderate** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |
| **Supporting** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |

The referenced SVI *de novo* instructions are distributed with this specification as `PS2_PM6.pdf` and are transcribed in **Appendix B**, including the SVI per-proband point table and the point-to-strength table. Those tables come from the distributed SVI document, not from a JAK3-specific table.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

| Strength | Criteria |
|----------|----------|
| **Strong** | PS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and recapitulating the JAK3-SCID phenotype. Animal models will be reviewed on a case-by-case basis by the VCEP to determine the appropriate strength level. *Modification Type: Gene-specific* |
| **Moderate** | Not specified by VCEP (no PS3_Moderate row is present). |
| **Supporting** | PS3_Supporting can be applied based on an abnormal result in an *in vitro* kinase activity assay. Approved assay instance: Roberts et al., 2004 (PMID: 14615376). *Modification Type: Gene-specific, Strength* |

**Additional requirement stated only in the `JAK3 Corrections 1.6.26` erratum, not in the v2.3 PS3 table:** "At least one previously observed proband with the JAK3 variant meeting PP4 is required to apply PS3 at any strength on the basis of a cellular model/in vitro study." See Appendix H and the conflict note above.

#### Approved Assay Instances

See **Appendix G** (functional evidence workbook). One assay is marked approved (`y`) — the in vitro kinase assay (JAK3 autophosphorylation), Roberts et al. 2004, proposed strength PS3_Supporting. The JAK3-γc binding assay from the same publication is marked **not** approved (`n`) with no proposed strength.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. (Notes 1 and 2 as in Richards et al., 2015.)

**VCEP Specifications:** **Not Applicable.** No comment text is given.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** Caveat: variant must not meet BS1, BS2, or BA1 criteria. *(Added in v2.3 per the release notes and `JAK3 Corrections 5.29.2026`.)*

| Strength | Criteria |
|----------|----------|
| **Moderate** | Defined to include missense alterations of two JH2 domain residues: R651W and C759R (PMID: 11668610). *Modification Type: Gene-specific* |

No other strength level is specified for PM1.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

| Strength | Criteria |
|----------|----------|
| **Supporting** | gnomAD popmax filtering allele frequency **< 0.000115** (**strict less-than**, as printed). An additional requirement is that **no homozygotes** have been observed in gnomAD. *Modification Type: Gene-specific* |

PM2 is specified at Supporting only.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Use ClinGen SVI adapted recommendations for *in trans* criterion (see PM3 criterion attached below) with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for *JAK3*.

> Caveat: All variants should be sufficiently rare (meet PM2 specification). The applicability of PM3 to suspected founder variants with allele frequencies exceeding the PM2 threshold will be evaluated on a case-by-case basis by the VCEP.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI adapted recommendations for *in trans* criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for *JAK3*. *Modification Type: General recommendation, Strength* |
| **Strong** | (identical wording) *Modification Type: General recommendation, Strength* |
| **Moderate** | (identical wording) *Modification Type: General recommendation, Strength* |
| **Supporting** | (identical wording) *Modification Type: General recommendation, Strength* |

The point system referenced by these rows is in the distributed `PM3 Criterion.pdf` and is transcribed in **Appendix C**; the December 2025 amendments to that table are in **Appendix D**.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Criteria |
|----------|----------|
| **Moderate** | When applied to deletion variants, the deleted region must contain a known **pathogenic** or **likely pathogenic** variant that is not predicted/observed to alter splicing. *Modification Type: Gene-specific* |
| **Supporting** | When applied to deletion variants, the deleted region must contain a known **VUS** variant that is not predicted/observed to alter splicing. *Modification Type: Gene-specific, Strength* |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications (for nonsense variants):**

- **PM5_Strong** — PM5 may be applied at a Strong level of evidence for any nonsense variant with 4+ points from informative variants (see point table below). PM5_Strong should be downgraded to PM5_Moderate if PVS1 is applied at any strength.
- **PM5_Moderate** — PM5 may also be applied at a Moderate level of evidence for any nonsense variant with 2+ points from informative variants (see point table below). PM5_Moderate may not be combined with PVS1_VeryStrong (should be downgraded to PM5_Supporting if PVS1_VeryStrong is applied).
- **PM5_Supporting** — Also applicable to a nonsense variant with 1 point from an informative variant (see point table). Informative variants must also be classified by these rule specifications.

#### PM5 nonsense-variant point table (verbatim)

| Type of variant under assessment (VUA); Informative variant | Score |
|---|---|
| Nonsense variant predicted to lead to NMD; P/LP variant in the exon of DNA change predicted to lead to NMD | +1pt |
| Nonsense variant predicted to lead to NMD; B/LB variant in the exon predicted to lead to NMD | -2pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD; P/LP variant resulting in a PTC in the same exon but downstream of VUA | +1pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD; B/LB variant resulting in PTC in the same exon but upstream of the VUA | -2pt |

NMD = nonsense-mediated decay; PTC = premature termination codon.

**Note (verbatim):** The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet "+1 pathogenic variant downstream" on the PVS1 flowchart. If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA. The VUA must be sufficiently rare, meet PM2_Supporting, to apply this point system. If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic without use of PM5 and without use of only PVS1 plus PM2.

#### Strength rows as printed

| Strength | Criteria |
|----------|----------|
| **Strong** | PM5 may be applied at a Strong level of evidence for any nonsense variant with 4+ points from informative variants (see point table). PM5_Strong should be downgraded to PM5_Moderate if PVS1 is applied at any strength. *Modification Type: General recommendation, Strength* |
| **Moderate** | Applicable at default strength (PM5) if previously established variant is classified as pathogenic or at reduced strength of PM5_Supporting if previously established variant is classified as likely pathogenic. PM5 may also be applied at a Moderate level of evidence for any nonsense variant with 2+ points from informative variants. PM5_Moderate may not be combined with PVS1_VeryStrong (should be downgraded to PM5_Supporting if PVS1_VeryStrong is applied). *Modification Type: General recommendation, Strength* |
| **Supporting** | Applicable at default strength (PM5) if previously established variant is classified as pathogenic or at reduced strength of PM5_Supporting if previously established variant is classified as likely pathogenic. Also applicable to a nonsense variant with 1 point from an informative variant (see point table). Informative variants must also be classified by these rule specifications. *Modification Type: General recommendation, Strength* |

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** The following guidelines should be used when determining the phenotypic consistency of each proband:
- "Phenotype highly specific for gene" proband must meet at least PP4_Moderate criteria;
- "Phenotype consistent with gene but not highly specific" proband must meet PP4 criteria;
- "Phenotype consistent with gene but not highly specific and high genetic heterogeneity": proband has been asserted to have a SCID phenotype but does not meet PP4 criteria;
- Reduce points per proband by half if the phase is unconfirmed.

| Strength | Criteria |
|----------|----------|
| **Strong** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |
| **Moderate** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |
| **Supporting** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification Type: General recommendation, Gene-specific* |

No PM6_VeryStrong row is listed for JAK3 (unlike PS2, which does list Very Strong). See **Appendix B**.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386) with the additional specification that unaffected individuals contributing to the calculated LOD score **(Attached document: PP1 specifications)** must be heterozygous carriers of one of the variants observed in the affected individuals (i.e. do not count wild-type/wild-type individuals).

| Strength | Criteria |
|----------|----------|
| **Strong** | Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations. *Modification Type: General recommendation* |
| **Moderate** | (identical wording) *Modification Type: General recommendation* |
| **Supporting** | (identical wording) *Modification Type: General recommendation* |

Thresholds are in the attached PP1 document, transcribed in **Appendix E**.

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable.**
Comment: The gnomAD v2.1.1 missense Z score for JAK3 (Z = 2.81) suggests this gene is not constrained for missense variation. Both benign and pathogenic missense variants are present in JAK3.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

| Strength | Criteria |
|----------|----------|
| **Supporting** | Only applicable to synonymous or intronic variants predicted to impact splicing by SpliceAI with a delta score **greater than or equal to 0.2** (**inclusive**). **Do not apply to missense variants.** *Modification Type: General recommendation* |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** PP4 applicability and strength is determined by the total points accumulated by a single affected individual according to the table below and the following total point ranges:

| Total points | Outcome |
|---|---|
| **<1 Point** (strict less-than) | PP4 not met |
| **1 - <2 Points** (lower bound inclusive, upper bound strict) | PP4 |
| **2 - <6 Points** (lower bound inclusive, upper bound strict) | PP4_Moderate |
| **≥6 Points** (inclusive) | PP4_Strong |

#### Evidence Description (Points)

| Evidence Description | Points |
|---|---|
| Diagnostic criteria met for SCID (Criteria 1 and 3 or Criterion 4 by itself) or Leaky SCID/Omenn syndrome (excluding Criterion 2)¹ | 0.5 |
| SCID gene panel or exome/genome sequencing conducted (only applicable if genetic testing did not provide an alternative genetic explanation for SCID/Leaky SCID/Omenn syndrome phenotype) | 1 |
| Family history of SCID (only applicable if SCID gene panel or exome/genome sequencing was conducted on proband and did not provide an alternative genetic explanation for phenotype) | 0.5 |
| Reduced constitutive or IL-2, IL-7, or IL-15-induced JAK3 tyrosine phosphorylation in patient cells as established by the laboratory AND pathogenic or likely pathogenic variants in IL2RG, STAT5A, STAT5B, IL2RA, IL2RB, IL7R, and IL15RA have been excluded  PMIDs: 8676091, 9354668, 10075926, 14615376, 19889552, 38598033 | 3 |
| Reduced constitutive or IL-2, IL-7, or IL-15-induced JAK3 tyrosine phosphorylation in patient cells as established by the laboratory AND pathogenic or likely pathogenic variants in IL2RG, STAT5A, STAT5B, IL2RA, IL2RB, IL7R, and IL15RA have **NOT** been excluded  PMIDs: 8676091, 9354668, 10075926, 14615376, 19889552, 38598033 | 1 |
| Reduced constitutive or IL-2, IL-7, or IL-15-induced phosphorylation of STAT5 in patient-derived T or B cells as established by the laboratory AND pathogenic or likely pathogenic variants in IL2RG, STAT5A, STAT5B, IL2RA, IL2RB, IL7R, and IL15RA have been excluded PMIDs: 8676091, 9354668, 10075926, 14615376, 19889552, 38598033 | 3 |
| Reduced constitutive or IL-2, IL-7, or IL-15-induced phosphorylation of STAT5 in patient-derived T or B cells as established by the laboratory AND pathogenic or likely pathogenic variants in IL2RG, STAT5A, STAT5B, IL2RA, IL2RB, IL7R, and IL15RA have **NOT** been excluded PMIDs: 8676091, 9354668, 10075926, 14615376, 19889552, 38598033 | 1 |
| SCID phenotype corrected by JAK3 gene therapy **WITHOUT** CNV testing performed² | 4.5 |
| SCID phenotype corrected by JAK3 gene therapy **WITH** CNV testing performed² | 6 |
| T-B+NK- lymphocyte subset profile* (*See notes*) | 0.5 |

¹ The diagnostic criteria should follow the PIDTC 2022 specification, summarized *here* (hyperlink in source; URL not rendered in the distributed PDF).
² CNV (Copy number variation) testing is required if PP4_Strong cannot be reached without points from gene therapy in order to certify that the variant in question is causative for the phenotype, and not one CNV event corrected by gene therapy and not previously identified.
\* **Notes:** 1) If NK cells are not noted or are present, criteria may still be applied if SCID gene panel or exome/genome sequencing has ruled out alternative causes; 2) If maternal T cells are present, the T lymphocyte profile is still considered to be T- (autologous T cells are absent).

"Find attached the PP4 table." — see **Appendix F**.

| Strength | Criteria |
|----------|----------|
| **Strong** | A patient score of ≥ 6 points¹ (inclusive). ¹CNV testing is required if PP4_Strong cannot be reached without points from gene therapy… *Modification Type: Disease-specific, Gene-specific* |
| **Moderate** | A patient score of 2-<6 points (see instructions below). *Modification Type: Disease-specific, Gene-specific* |
| **Supporting** | A patient score of 1-<2 points (see instructions below). *Modification Type: Disease-specific, Gene-specific* |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable.** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PubMed: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:** The maximum credible population allele frequency threshold was determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:
- Prevalence: 1:5,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.05 (based on the contribution of *JAK3* variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 5.2%, rounded to 5%)
- Penetrance: 50%

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | gnomAD popmax filtering allele frequency **> 0.00447** (**strict greater-than**). *Modification Type: Gene-specific* |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:** gnomAD popmax filtering allele frequency **> 0.00100**¹ (**strict greater-than**).
The maximum credible population allele frequency threshold was determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:
- Prevalence: 1:50,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.05 (based on the contribution of *JAK3* variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 5.2%, rounded to 5%)
- Penetrance: 100%

¹ Consider also bottleneck populations.

| Strength | Criteria |
|----------|----------|
| **Strong** | gnomAD popmax filtering allele frequency **> 0.00100**¹ (**strict**). ¹Consider also bottleneck populations. *Modification Type: Gene-specific* |

> Note: BA1 and BS1 use different prevalence (1:5,000 vs 1:50,000) and penetrance (50% vs 100%) inputs, as printed.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

| Strength | Criteria |
|----------|----------|
| **Strong** | BS2_Strong: Can be applied at Strong level if observed in **at least 3 homozygotes** (inclusive). *Modification Type: Strength* |
| **Supporting** | Only to be used when the variant is observed in the homozygous state in a healthy adult. BS2_Supporting: Can be applied at Supporting level if observed in **at least 1 homozygote** (inclusive). *Modification Type: Strength* |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** **Not Applicable.**
Comment: There is not a well-established functional study which can rule out all damaging effects on protein function.

> Note: the functional-evidence workbook distributed with this specification is titled "PS3_BS3", but BS3 is Not Applicable and the workbook proposes no BS3 strength for either assay.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

| Strength | Criteria |
|----------|----------|
| **Strong** | Can be applied without additional specifications. *Modification Type: General recommendation, None* |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | Does not apply. JAK3 missense variants are a known mechanism of disease. |
| **BP2** | Not Applicable | (no comment given) |
| **BP3** | Not Applicable | Does not apply. |
| **BP4** | Not Applicable | (no comment given) |
| **BP5** | Not Applicable | (no comment given) |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PubMed: 29543229) |
| **BP7** | **Supporting (applicable)** | Applicable to both synonymous variants and deep intronic variants affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions. The variant should be predicted not to impact splicing by at least two out of three *in silico* tools (freely available tools include GeneSplicer, MaxEntScan, NNSplice, SpliceAI, Splicing Sequences Finder (SSF), and varSEAK). Given the potential for poor conservation of genes related to T cell and B cell development among vertebrates, nucleotide conservation is not required in order to apply BP7. *Modification Type: Disease-specific* |

> Source wording preserved: BP7 says "at least two out of three *in silico* tools" while then listing six tools.

---

## Rules for Combining Criteria

Transcribed verbatim from the "Rules for Combining Criteria" section of the v2.3 specification (Richards et al., 2015 combining rules).

### Pathogenic

| # | Rule |
|---|------|
| 1 | 1 Very Strong *(PVS1, PS2_Very Strong, PM3_Very Strong)* **AND** ≥ 1 Strong *(PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong)* |
| 2 | 1 Very Strong **AND** ≥ 2 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate)* |
| 3 | 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting *(PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)* |
| 4 | 1 Very Strong **AND** ≥ 2 Supporting |
| 5 | ≥ 2 Strong *(PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong)* |
| 6 | 1 Strong **AND** ≥ 3 Moderate |
| 7 | 1 Strong **AND** 2 Moderate **AND** ≥ 2 Supporting |
| 8 | 1 Strong **AND** 1 Moderate **AND** ≥ 4 Supporting |

### Likely Pathogenic

| # | Rule |
|---|------|
| 1 | 1 Very Strong *(PVS1, PS2_Very Strong, PM3_Very Strong)* **AND** 1 Moderate |
| 2 | 1 Strong **AND** 1 Moderate |
| 3 | 1 Strong **AND** ≥ 2 Supporting |
| 4 | ≥ 3 Moderate |
| 5 | 2 Moderate **AND** ≥ 2 Supporting |
| 6 | 1 Moderate **AND** ≥ 4 Supporting |
| 7 | 1 Strong **AND** 2 Moderate |
| 8 | 1 Very Strong **AND** 1 Supporting |

*(Rule 7 of the Likely Pathogenic list, "1 Strong AND 2 Moderate", is a subset of Pathogenic rule 6 "1 Strong AND ≥ 3 Moderate" only at ≥3 Moderate; transcribed as printed.)*

### Benign

| # | Rule |
|---|------|
| 1 | ≥ 2 Strong *(BS1, BS2, BS4)* |
| 2 | 1 Stand Alone *(BA1)* |

### Likely Benign

| # | Rule |
|---|------|
| 1 | ≥ 2 Supporting *(BS2_Supporting, BP7)* |
| 2 | 1 Strong *(BS1, BS2, BS4)* |

---

## Appendices

### Appendix A — PVS1 flowchart (`PVS1.pdf`, "Specified PVS1 flowchart")

JAK3-specific NMD boundary used throughout the flowchart (highlighted in the source): premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon — **c.3157 (codon 1053) in exon 23**.

**Nonsense or Frameshift**
| Path | Outcome |
|---|---|
| Predicted to undergo NMD ᵇ → Exon is present in biologically-relevant transcript(s) | PVS1 |
| Predicted to undergo NMD ᵇ → Exon is absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD ᵇ → Truncated/altered region is critical to protein function | PVS1_Strong |
| Not predicted to undergo NMD ᵇ → Role of region unknown → LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD ᵇ → Role unknown → LoF not frequent & exon present → removes >10% of protein → 1+ pathogenic variant present downstream | PVS1_Strong |
| … → removes >10% of protein → No known downstream pathogenic variants | PVS1_Moderate |
| … → Variant removes <10% of protein | PVS1_Moderate |

**GT--AG 1,2 splice sites ᵃ**
| Path | Outcome |
|---|---|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD ᵇ → Exon present in biologically-relevant transcript(s) | PVS1 |
| … → Exon absent from biologically-relevant transcript(s) | N/A |
| Disrupts reading frame and is **NOT** predicted to undergo NMD ᵇ → Truncated/altered region is critical to protein function | PVS1_Strong |
| … → Role of region unknown → LoF frequent and/or exon absent | N/A |
| … → Role unknown → LoF not frequent & exon present → removes >10% → 1+ pathogenic variant present downstream | PVS1_Strong |
| … → removes >10% → No known downstream pathogenic variants | PVS1_Moderate |
| … → Variant removes <10% of protein | PVS1_Moderate |
| Exon skipping or use of a cryptic splice site **preserves** reading frame → Role of region unknown → LoF frequent and/or exon absent | N/A |
| … preserves frame → LoF not frequent & exon present → removes >10% → 1+ pathogenic variant present **within deleted region** | PVS1_Strong |
| … → removes >10% → No known pathogenic variants within deleted region | PVS1_Moderate |
| … → Variant removes <10% of protein | PVS1_Moderate |
| … preserves frame → Truncated/altered region is critical to protein function | PVS1_Strong |

**Deletion (single exon to full gene)**
| Path | Outcome |
|---|---|
| Full gene deletion | PVS1 ᵈ |
| Single to multi exon deletion – disrupts reading frame and is predicted to undergo NMD ᵇ → Exon present in biologically-relevant transcript(s) | PVS1 |
| … → Exon absent from biologically-relevant transcript(s) | N/A |
| Single to multi exon deletion – disrupts reading frame and is **NOT** predicted to undergo NMD ᵇ, **or** preserves reading frame → Truncated/altered region critical to protein function | PVS1_Strong |
| … → Role of region unknown → LoF frequent in general population and/or exon absent | N/A |
| … → LoF not frequent & exon present → removes >10% → 1+ pathogenic variant present within deleted region | PVS1_Strong |
| … → removes >10% → No known pathogenic variants within deleted region | PVS1_Moderate |
| … → Variant removes <10% of protein | PVS1_Moderate |

**Duplication (≥1 exon in size and must be completely contained within gene)**
| Path | Outcome |
|---|---|
| Proven in tandem → Reading frame disrupted and NMD predicted to occur | PVS1 |
| Proven / Presumed in tandem → No or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem → Reading frame presumed disrupted and NMD predicted to occur | PVS1_Strong |
| Proven not in tandem | N/A |

**Initiation Codon**
| Path | Outcome |
|---|---|
| No known alternative start codon in other transcripts → ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon | PVS1_Moderate |
| No known alternative start codon in other transcripts → No pathogenic variant(s) upstream of closest potential in-frame start codon | PVS1_Supp |
| Different functional transcript uses alternative start codon | N/A |

> **Unreadable/missing content flagged:** the flowchart carries superscript footnote markers **a**, **b** and **d**, but the distributed one-page PDF contains **no footnote legend** defining them (no text for a/b/c/d is present in the file). The meaning of footnotes a, b and d is therefore not specified in the distributed package.

---

### Appendix B — SVI *de novo* recommendation (`PS2_PM6.pdf`)

Header, verbatim: "ClinGen Sequence Variant Interpretation Recommendation for de novo Criteria (PS2/PM6) - Version 1.1. Working Group Page: https://clinicalgenome.org/working-groups/sequence-variant-interpretation/. Date Approved: March 18, 2018, updated May 5, 2021. Changes from v1: Clarified that confirmed/assumed is with regards to parental relationships and not de novo status."

The SVI proposes a point-based system based on three parameters: confirmed vs assumed parental relationships; phenotypic consistency; number of *de novo* observations. Per-proband points are summed and compared to Table 2. "If the parents have not been tested for parentage or for the variant, no points should be awarded."

**Table 1. Points\* awarded per *de novo* occurrence**

| Phenotypic consistency | *de novo* with confirmed parental relationships | *de novo* with unconfirmed parental relationships |
|---|---|---|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity\*\* | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

\* Note that these points are *not* equivalent to the points used to classify a variant per the Tavtigian et al 2020 "Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines"
\*\* Maximum allowable value of 1 may contribute to overall score

**Table 2. Recommendation for determining the appropriate ACMG/AMP evidence strength level for *de novo* occurrence(s)**

| Supporting (PS2_Supporting or PM6_Supporting) | Moderate (PS2_Moderate or PM6) | Strong (PS2 or PM6_Strong) | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |
|---|---|---|---|
| 0.5 | 1 | 2 | 4 |

**Additional considerations for applying *de novo* criteria based on inheritance (verbatim):**
- Conditions with X-linked inheritance: if the variant occurs *de novo* in an unaffected carrier mother, and family history is consistent - i.e., she has no affected brothers/other male relatives apart from her affected son(s) – *de novo* criteria may be applied despite the fact that she is unaffected.
- **Autosomal recessive conditions: for a *de novo* occurrence in a gene associated with a condition inherited in an autosomal recessive pattern without an additional pathogenic/likely pathogenic variant identified, the strength of evidence should be decreased by one level.** *(JAK3-SCID is autosomal recessive, so this clause is directly relevant.)*
- Mosaicism: for cases with apparent germline mosaicism (multiple affected siblings with both parents negative for the variant), parental relationships must be confirmed in order for *de novo* criteria to apply.

The document also gives worked SIK1 / ASH1L / NIPBL examples illustrating point summation; these are illustrative and gene-non-specific.

---

### Appendix C — SVI *in trans* recommendation (`PM3 Criterion.pdf`)

Header, verbatim: "ClinGen Sequence Variant Interpretation Recommendation for in trans Criterion (PM3) - Version 1.0. Date Approved: May 2, 2019; Table 1 updated October 17, 2025." (Registry label: "October 2025 Version, Minor Updates".)

**SVI revision to PM3:** For recessive disorders, detected in *trans* with a pathogenic **or likely pathogenic** variant **in an affected patient**.

**Table 1. Points awarded per in *trans* proband**

| Classification/Zygosity of other variant | Points per Proband-Family\* — Confirmed in *trans* | Points per Proband-Family\* — Phase unknown |
|---|---|---|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence, Non-consanguineous\*\* *(no max)* | 1.0 | 1.0 |
| Homozygous occurrence, Consanguineous\*\* *(no max)* | 0.5 | 0.5 |
| Uncertain significance variant *(max point 0.5)* | 0.25 | 0 |

\* Multiple probands from separate nuclear families that are later found to have identity-by-descent should only be counted once.
\*\* When consanguinity is not known or reported: if family IS NOT from a bottlenecked population (as defined by gnomAD), assume non-consanguinity; otherwise, assume consanguinity. If genetic ancestry of the family cannot be determined, assume consanguinity.

**Table 2. Recommendation for determining the appropriate evidence strength level for PM3**

| PM3_Supporting | PM3 | PM3_Strong | PM3_VeryStrong |
|---|---|---|---|
| 0.5 | 1.0 | 2.0 | 4.0 |

**Considerations (verbatim):**
- **Allele Frequency** – Application of PM3 is contingent on the allele frequency of the variant being assessed and the variant presumably on the other allele both being sufficiently rare (meets PM2 threshold). This contingency is to avoid incorrect application of PM3 to high frequency variants that are likely to occur in *trans* with P/LP variants based on frequency.
- **Phasing** – If the phase cannot be determined, it is recommended that at least two different LP/P variants (depending on classifications) are needed to equal the weight of one LP/P co-occurrence confirmed in *trans*. In confirmation of phasing, if only one parent is tested and found to carry one allele, variants can be counted as in *trans* (PAH c.601C>T / c.734T>C worked example given).
- **Classification** – Probands should be weighted less when the variant on the other allele is of uncertain significance and rare (meets PM2); however, weight may vary by gene size as larger genes are more likely to have a second variant by chance (default 0.25 points). If the variant on the other allele is classified as P or LP, weighting depends on phasing, with P/LP being weighted equally if confirmed in trans and different point values per proband if phasing is unknown (0.5 points and 0.25 points, respectively). To avoid circularity, in all instances (phasing confirmed or unknown), the classification of the variant on the other allele should not use evidence from the variant being interrogated.
- **Homozygous occurrences** – For homozygous occurrences, the default weight is dropped to 0.5 points, as a rare homozygous occurrence may be due to consanguinity. **A recommended max of 1.0 points of all homozygous cases is suggested to prevent overclassification of homozygous occurrences in the absence of additional data.**

> **Internal contradiction, flagged, not reconciled:** the "Homozygous occurrences" bullet retains the SVI default "max of 1.0 points of all homozygous cases", while Table 1 (as amended December 2025, see Appendix D) explicitly marks both homozygous rows **"(no max)"**. The amendment document shows the SCID VCEP deliberately requested removal of the homozygous max; the narrative bullet appears not to have been updated to match.

---

### Appendix D — PM3 Minor Amendments 12.12.2025

This document is a record of SVI comments and the SCID VCEP's responses regarding PM3 Table 1. Transcribed in full.

**Footnotes added to the Table:**
> \* Multiple probands from separate nuclear families that are later found to have identity-by-descent should only be counted once.
>
> \*\* When consanguinity is not known or reported: if family IS NOT from a bottlenecked population (as defined by gnomAD), assume non-consanguinity; otherwise, assume consanguinity.  If genetic ancestry of the family cannot be determined, assume consanguinity.

**SVI Comments and VCEP responses (verbatim):**

| SVI comment | SCID VCEP response |
|---|---|
| "Prefer N/A to repeating the 1.0 and 0.5" | "The SCID VCEP deliberated this point.  Our geneticists pointed out that apparent homozygous variants could result from hemizygosity, which may be undetected if the parents are not sequenced (i.e., "Phase unknown").  Because of the likelihood that authors may not bother to sequence the parents in homozygous situations, especially in older publications, the VCEP experts preferred to leave the numbers in place." |
| "Update "max point 0.5 per family" to "max point 0.5" as in original specs. Please replace "max point 0.5 per family" from the Homozygous Consanguineous and indicate "no max". Rationale: "per proband" is a rule for the whole table in general (per the table title); Multiple cases per family will inherently be counted as PP1 instead of multiple PM3s" | "The SCID VCEP agreed and made the changes to the table.  To minimize confusion for biocurators and experts as much as possible between proper application of PM3 vs. PP1 (which we have definitely observed, even in sustained curations), we changed "Proband" to "Proband-Family"." |
| "What to do if you don't know about consanguinity" | "The VCEP decided to use gnomAD definitions to specify assumption of non-consanguinity for families from non-bottlenecked populations and assumption of consanguinity otherwise.  A footnote was added to the Table." |
| "If the VCEP wishes, they can provide an asterisk footnote that supports the notion that "multiple probands from separate nuclear families that are later found to have identity-by-descent should only be counted once."" | "We added this footnote to the Table." |

**Amended Table 1 as reproduced in the amendment document** (identical to the table now in `PM3 Criterion.pdf`):

| Classification/Zygosity of other variant | Confirmed in trans | Phase unknown |
|---|---|---|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence — Non-consanguineous\*\* (no max) | 1.0 | 1.0 |
| Homozygous occurrence — Consanguineous\*\* (no max) | 0.5 | 0.5 |
| Uncertain significance variant (max point 0.5) | 0.25 | 0 |

**Embedded image (word/media/image1.png)** — the PM3 point-to-strength bar, identical to Table 2 of `PM3 Criterion.pdf`:

| PM3_Supporting | PM3 | PM3_Strong | PM3_VeryStrong |
|---|---|---|---|
| 0.5 | 1.0 | 2.0 | 4.0 |

> Date oddity, flagged: the amendment document is dated **12.12.2025** but `PM3 Criterion.pdf` states its Table 1 was "updated October 17, 2025" while already containing all of the December amendments.

---

### Appendix E — PP1 co-segregation thresholds (`PP1.pdf`)

Two tables reproduced from Oza et al. (*Hum Mutat*; the PP1 SVI reference cited by the VCEP is PMID: 30311386).

**Table 4a: Recommendations for PP1 (segregation evidence) — General Recommendations**

| | Supporting | Moderate | Strong |
|---|---|---|---|
| Likelihood | 4:1 | 16:1 | 32:1 |
| LOD Score | 0.6 | 1.2 | 1.5 |
| Autosomal dominant threshold | 2 affected segregations | 4 affected segregations | 5 affected segregations |
| Autosomal recessive threshold | See Table 4b | See Table 4b | See Table 4b |

*JAK3-SCID is autosomal recessive, so the Table 4b lookup applies.*

**Table 4b: Recommendations for autosomal recessive segregation evidence (PP1)** — General Recommendations (Phenocopy not an issue). Rows = affected segregations (0–10); columns = unaffected recessive segregations (0–10). Each cell is the LOD score. This is a **lookup table**: find the cell for the family's counts, then compare the LOD to the Table 4a thresholds (0.6 / 1.2 / 1.5).

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

**Table 4b notes (verbatim):** "Affected segregations are counted in rows and unaffected segregations in columns. Affected segregations are affected family members in whom biallelic compound heterozygous or homozygous variants segregates. Unaffected segregations are defined as unaffected family members, typically siblings, who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants identified in the proband, or a heterozygous carrier for a single variant. Unaffected, carrier parents do NOT count as unaffected segregations. There may be scenarios where individuals other than siblings could be counted as segregations, such as in families where one parent is affected with the autosomal recessive disorder, in large families with multiple branches, or in consanguineous families."
"Each cell shows the LOD score of each combination of affected and unaffected segregations. LOD scores were calculated using a simplified LOD score formula, as described in Strande et al., 2017."

**JAK3 VCEP addition (from the main specification):** unaffected individuals contributing to the calculated LOD score must be heterozygous carriers of one of the variants observed in the affected individuals (i.e. do not count wild-type/wild-type individuals).

> **Conflict, flagged, not reconciled:** the Oza Table 4b note permits unaffected segregations that are "either wild-type for both variants … or a heterozygous carrier for a single variant", whereas the JAK3 VCEP specification explicitly excludes wild-type/wild-type individuals. The VCEP statement is the gene-specific override.

---

### Appendix F — PP4 attached table (`PP4 - JAK3.pdf`, "2025 Updates")

The attached one-page PP4 table reproduces the point ranges and evidence rows given in the PP4 section above. Differences observed between the attachment and the v2.3 specification body, transcribed rather than reconciled:

1. In the attachment, the two **JAK3 tyrosine phosphorylation** rows (3 pt and 1 pt) carry **no PMID list**; the specification body appends "PMIDs: 8676091, 9354668, 10075926, 14615376, 19889552, 38598033" to all four phosphorylation rows. The two **STAT5** rows carry the PMIDs in both documents.
2. Footnote numbering is **swapped** between the two documents. In the attachment, footnote 1 is the CNV note and footnote 2 is the PIDTC note; in the specification body, footnote 1 is the PIDTC note and footnote 2 is the CNV note. The footnote *markers* in the attachment's point ranges list ("≥6 points: PP4_Strong¹") and evidence rows are keyed to the attachment's own numbering.
3. The attachment's CNV footnote reads "…and not identified previously"; the specification body reads "…and not previously identified". Same meaning, different word order.
4. Both documents render the PIDTC reference as a hyperlinked word "here"; the target URL is not visible in either distributed PDF.

All point values (0.5 / 1 / 0.5 / 3 / 1 / 3 / 1 / 4.5 / 6 / 0.5) and the four point ranges are **identical** in both documents.

---

### Appendix G — PS3/BS3 functional evidence workbook (`SCID VCEP PS3_BS3 Funcational Evidence (JAK3).xlsx`)

Two sheets. Both transcribed in full below (the workbook is small; no rows were omitted).

**Sheet 1: "General Class of Assay Summary"**

| Gene | General Class of Assay | PMIDs |
|---|---|---|
| JAK3 | `In vitro kinase assay (JAK3 autophosphorylation),+a+1wb +n i qww$-q ` | PMID: 14615376 |
| (blank) | JAK3-γc binding assay | PMID: 14615376 |

> **Source corruption preserved verbatim and flagged:** cell B2 contains the trailing garbage string `,+a+1wb +n i qww$-q ` appended to "In vitro kinase assay (JAK3 autophosphorylation)". This appears to be an accidental keystroke artifact in the distributed workbook; the same assay name appears clean in Sheet 2 cell B6.

**Sheet 2: "JAK3 Assay Instance Details"** (transposed layout — attributes in column A, one assay instance per subsequent column)

| Attribute | Assay instance 1 | Assay instance 2 |
|---|---|---|
| PMID | 14615376 | 14615376 |
| Gene | JAK3 | JAK3 |
| DOI / link | 10.1182/blood-2003-06-2104 | 10.1182/blood-2003-06-2104 |
| Author | Roberts...Buckley | Roberts...Buckley |
| Year | 2004 | 2004 |
| General Class of Assay | In vitro kinase assay (JAK3 autophosphorylation) | JAK3-γc binding assay |
| Assay (General Description) | Clarified whole cell lysates from JAK3-negative COS-7 cells transiently transfected with wild type or variant JAK3 cDNA expression vectors were immunoprecipitated with a JAK3 C-terminus antibody, incubated with [γ-32P]ATP for 1 min or 5 min, and analyzed on an SDS-PAGE gel to assess JAK3 phosphorylation | Clarified whole cell lysates from JAK3-negative COS-7 cells transiently transfected with Tac-γc and wild type or variant JAK3 cDNA expression vectors were immunoprecipitated with an anti-Tac antibody and immunoblotted with anti-JAK3 antibody to assess JAK3-γc binding |
| Material used (patient cells, engineered variants, cell lines, animal model, etc. | JAK3-negative COS-7 cells transiently transfected with wild type or variant JAK3 cDNA expression vectors | JAK3-negative COS-7 cells transiently transfected with Tac-γc and wild type or variant JAK3 cDNA expression vectors |
| Readout type (qualitative/quantitative) | Semi-quantitative | Semi-quantitative |
| Readout description | Presence/intensity of band corresponding to phosphorylated JAK3 | Presence/intensity of band corresponding to γc-coprecipitated JAK3 |
| Biological replicates (met/not met) | Not reported | Not reported |
| Technical replicates (met/not met); description | Not reported | Not reported |
| Basic positive control (met/not met); description | Wild type JAK3-transfected cells | Wild type JAK3-transfected cells |
| Basic negative control (met/not met); description | Vector-only transfected cells; JAK3 p.Lys855Ala (artificial catalytically inactive JAK3 variant) | Cells transfected with Tac-γc cDNA vector only (no exogenous JAK3 expression) |
| Validation controls P/LP (#) | 0 | 0 |
| Validation controls B/LB (#) | 0 | 0 |
| Statistical analysis (general description) | Not reported | Not reported |
| Threshold for normal readout | Wild type-like level of phosphorylated JAK3 | Wild type-like level of γc-coprecipitated JAK3 |
| Threshold for abnormal readout | Absence/reduced level of phosphorylated JAK3 | Absence/reduced level of γc-coprecipitated JAK3 |
| **Approved assay (y/n)** | **y** | **n** |
| **Proposed strength** | **PS3_Supporting** | *(blank)* |
| Variant(s) Tested | c.266_268del (p.Ala58del), c.602C>A (p.Glu169Asp), c.1860G>A (p.Gly589Ser) | c.266_268del (p.Ala58del), c.602C>A (p.Glu169Asp), c.1860G>A (p.Gly589Ser) |
| Notes | *(blank)* | *(blank)* |

The workbook contains no embedded images, comments, or additional sheets. Sheet header instructions referenced by the erratum ("Please follow the instructions in the sheet") are not present as separate text beyond the column headers above.

> **Apparent source errors, flagged, not corrected:** the "Variant(s) Tested" HGVS pairs do not internally agree. `c.602C>A` is in codon 201 and a C>A there cannot produce p.Glu169Asp; `c.1860G>A` is in codon 620 and cannot produce p.Gly589Ser (p.Gly589Ser would be c.1765G>A). `c.266_268del (p.Ala58del)` is also internally inconsistent (c.266_268 spans codons 89–90). Transcribed as printed.

---

### Appendix H — JAK3 Corrections 1.6.26

Erratum #2 of three. Covers PS3, BS2 and PP4. Transcribed below.

**PS3** — "SVI Recommended Resources: Functional assay sheet. Please follow the instructions in the sheet."
- *Strong Specification:* PS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and recapitulating the JAK3-SCID phenotype. Animal models will be reviewed on a case-by-case basis by the VCEP to determine the appropriate strength level. *Modification Type: Gene-specific*
- *Supporting Specification:* PS3_Supporting can be applied based on an abnormal result in an *in vitro* kinase activity assay. Approved assay instance: Roberts et al., 2004 (PMID: 14615376). **"At least one previously observed proband with the JAK3 variant meeting PP4 is required to apply PS3 at any strength on the basis of a cellular model/in vitro study."** *Modification Type: Gene-specific; Strength*

  → **This bolded sentence does not appear in the PS3 section of the v2.3 specification tables.** Status: erratum content not reflected in the spec's own tables.

**BS2** — Strong: BS2_Strong can be applied at Strong level if observed in at least 3 homozygotes. Supporting: only to be used when the variant is observed in the homozygous state in a healthy adult; BS2_Supporting can be applied at Supporting level if observed in at least 1 homozygote. *Modification Type: Strength.*
  → **Matches the v2.3 BS2 tables exactly.**

**PP4** — The erratum reproduces the complete PP4 block (point ranges, all ten evidence rows with points, footnotes 1/2 and the \*Notes, and the Strong/Moderate/Supporting rows) exactly as it appears in the v2.3 specification, including "Find attached the PP4 table."
  → **Matches the v2.3 PP4 tables exactly**, and uses the same footnote numbering as the specification body (PIDTC = 1, CNV = 2), i.e. the erratum agrees with the spec and the `PP4 - JAK3.pdf` attachment is the outlier.

The document contains no images.

---

### Appendix I — JAK3 Corrections 5.29.2026

Erratum #3 of three, and the most recent. Covers PM1 only. Transcribed in full:

> **JAK3**
> **PM1**
> *Original ACMG Summary:* Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.
> *VCEP Specifications:* Caveat: variant must not meet BS1, BS2, or BA1 criteria.
> *Moderate Specification:* Defined to include missense alterations of two JH2 domain residues: R651W and C759R (PMID: 11668610).
> *Modification Type:* Gene-specific

→ **Fully reflected in the v2.3 PM1 section**, and named in the v2.3 release notes ("Added caveat to PM1"). Note the release-note text capitalises "Variant" while the criteria table prints "variant"; wording is otherwise identical.

The document contains no images.

---

## Version History

| Version | Released | Notes (as published) |
|---|---|---|
| 2.3 | 6/1/2026 | Uploaded JAK3 Corrections file; Added caveat to PM1 "Caveat: Variant must not meet BS1, BS2, or BA1 criteria." |
| 2.2 | — | Not present in the local registry; version skipped locally (v2.1.0 → v2.3). Upstream release notes for v2.2 are not included in the distributed package. |
| Earlier | — | Release notes for versions prior to 2.3 are not included in the distributed package. |

---

## Statement of Coverage

Criteria **specified** by this VCEP: PVS1, PS1, PS2, PS3, PM1, PM2, PM3, PM4, PM5, PM6, PP1, PP3, PP4, BA1, BS1, BS2, BS4, BP7.
Criteria explicitly marked **Not Applicable**: PS4, PP2, PP5, BS3, BP1, BP2, BP3, BP4, BP5, BP6.
Criteria with a strength level **not specified**: PVS1_Supporting (no strength row; appears only as a flowchart outcome), PS3_Moderate, PM1 at any level other than Moderate, PM2 at any level other than Supporting, PM6_VeryStrong, PP3 at any level other than Supporting.

No point matrix, strength ladder, or combining rule appears in this document that is not present in the distributed source files.

---

*This document was compiled from the ClinGen VCEP specification (GN121, JAK3 v2.3) and its distributed supplementary files. For the most current version, please refer to the ClinGen website.*
