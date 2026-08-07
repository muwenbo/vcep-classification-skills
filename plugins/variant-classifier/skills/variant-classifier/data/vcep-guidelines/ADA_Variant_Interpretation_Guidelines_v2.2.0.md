# ClinGen Severe Combined Immunodeficiency Disease VCEP Variant Interpretation Guidelines for ADA

**Version:** 2.2
**Released:** 7/17/2026
**Affiliation:** Severe Combined Immunodeficiency Disease VCEP
**Registry ID:** GN114
**DOI:** 10.5281/zenodo.21434426
**Type (as stated by VCEP):** Richards et.al., 2015 - Combining rules
**Source basis:** ClinGen Criteria Specification Registry record "Rules for ADA", plus the six supplementary files distributed with it (PS2_PM6, ADA Corrections 1.6.26, PP4 - ADA, PP1, PVS1, PM3 Criterion). Everything below is transcribed from those files; nothing has been supplied from generic ACMG/AMP or SVI material that the VCEP did not distribute.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | ADA (HGNC:186) |
| **HGNC Name** | adenosine deaminase |
| **Transcript** | NM_000022.4 |
| **Disease** | severe combined immunodeficiency, autosomal recessive, T cell-negative, B cell-negative, NK cell-negative, due to adenosine deaminase deficiency (MONDO:0007064) |
| **Inheritance** | Autosomal recessive inheritance |
| **Rights Holder** | The Clinical Genome Resource (ClinGen) |

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
2. [Benign Criteria](#benign-criteria)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)
5. [Source Conflicts and Transcription Notes](#source-conflicts-and-transcription-notes)
6. [Version History](#version-history)

---

## Quick Reference: Frequency Thresholds and Comparators

Comparator inclusivity is recorded exactly as written in the source.

| Criterion | Threshold (gnomAD popmax filtering allele frequency) | Comparator | Inclusive/Strict |
|-----------|------------------------------------------------------|------------|------------------|
| **BA1** (Stand Alone) | 0.00721 | `>` | **Strict** (greater than) |
| **BS1** (Strong) | 0.00161 | `>` | **Strict** (greater than) |
| **PM2** (Supporting) | 0.0001742 | `<` | **Strict** (less than); plus no homozygotes observed in gnomAD |

Enzyme-activity thresholds (PS3 / former BS3), transcribed with their comparators:

| Item | Threshold | Comparator |
|------|-----------|------------|
| PS3_Moderate | 0.05% of wild-type activity (group I) | `≤` **inclusive** |
| PS3_Supporting | 0.06-0.6% of wild-type activity (groups II and III) | closed range, **inclusive** at both ends as written |
| BS3_Supporting (**withdrawn in v2.2 — BS3 is Not Applicable**) | 4.8% of wild-type activity (based on group IV) | `≥` inclusive (written "> = 4.8%" in the BS3 comment) |

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease. Caveats: • Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7). • Use caution interpreting LOF variants at the extreme 3' end of a gene. • Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact. • Use caution in the presence of multiple transcripts.

**VCEP Specifications:** See attached PVS1 flowchart (transcribed in [Appendix A](#appendix-a---ada-specified-pvs1-flowchart)).

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)). *Modification Type: General recommendation, Gene-specific* |
| **Strong** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification: For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 12, or variants in the last 50 nucleotides of the penultimate exon after c.1028, codon 343, in exon 11), at least one pathogenic variant must be present downstream in order to apply PVS1_Strong. *Modification Type: General recommendation, Gene-specific* |
| **Moderate** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification: For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 12, or variants in the last 50 nucleotides of the penultimate exon after c.1028, codon 343, in exon 11), when at least one pathogenic variant is not present downstream downgrade to PVS1_Moderate. *Modification Type: General recommendation* |
| **Supporting** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)). *Modification Type: Gene-specific, Strength* |

> **Gene-specific NMD boundary:** the ADA flowchart defines "not predicted to undergo NMD" as a premature stop codon in the last exon **or** in the last 50 nucleotides of the penultimate exon, i.e. after **c.1028 (codon 343) in exon 11**. The last exon of NM_000022.4 is **exon 12**.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T. Applicable if the previously established variant is classified as **pathogenic** by SCID VCEP specifications for ADA. *Modification Type: Gene-specific* |
| **Moderate** | It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be likely pathogenic, can use PS1 for c.105+1G>T. Applicable if the previously established variant is classified as **likely pathogenic** by SCID VCEP specifications for ADA. *Modification Type: Gene-specific, Strength* |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

The following guidelines should be used when determining the phenotypic consistency of each proband:

- "Phenotype highly specific for gene" proband must meet at least **PP4_Moderate** criteria;
- "Phenotype consistent with gene but not highly specific" proband must meet **PP4** criteria;
- "Phenotype consistent with gene but not highly specific and high genetic heterogeneity": proband has been asserted to have a SCID phenotype but does not meet PP4 criteria;
- Reduce points per proband by half if the phase is unconfirmed.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI recommendations for de novo criteria (see [Appendix B](#appendix-b---clingen-svi-recommendation-for-de-novo-criteria-ps2--pm6-version-11)). *Modification Type: General recommendation, Gene-specific* |
| **Strong** | Use ClinGen SVI recommendations for de novo criteria (see Appendix B). *Modification Type: General recommendation, Gene-specific* |
| **Moderate** | Use ClinGen SVI recommendations for de novo criteria (see Appendix B). *Modification Type: General recommendation, Gene-specific* |
| **Supporting** | Use ClinGen SVI recommendations for de novo criteria (see Appendix B). *Modification Type: General recommendation, Gene-specific* |

The point system referenced here is the SVI PS2/PM6 v1.1 system, distributed by this VCEP as `PS2_PM6.pdf` and transcribed verbatim in [Appendix B](#appendix-b---clingen-svi-recommendation-for-de-novo-criteria-ps2--pm6-version-11).

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | PS3 may potentially be applied at the default strength level of Strong for evidence from an animal model expressing the variant of interest and recapitulating the ADA-SCID phenotype. *Modification Type: Gene-specific* |
| **Moderate** | The strength of evidence from cellular models/in vitro studies is dependent upon the level of expressed ADA enzyme activity based on levels defined in Arredondo-Vega et al., 1998 (PMID: 9758612): **PS3_Moderate: ≤0.05% of wild-type activity (group I)**. *Modification Type: Gene-specific* |
| **Supporting** | The strength of evidence from cellular models/in vitro studies is dependent upon the level of expressed ADA enzyme activity based on levels defined in Arredondo-Vega et al., 1998 (PMID: 9758612): **PS3_Supporting: 0.06-0.6% of wild-type activity (groups II and III)**. *Modification Type: Gene-specific, Strength* |

#### Approved Assay Instances

**Not distributed with this specification.** The v2.2 release notes state "Uploaded SCID VCEP PS3 Functional Evidence (ADA) 6.2.26", and the `ADA Corrections 1.6.26.docx` file states under PS3: *"SVI Recommended Resources — Functional assay sheet. Please follow the instructions in the sheet."* **No functional assay sheet is present in the distributed file set for GN114** (see [Source Conflicts and Transcription Notes](#source-conflicts-and-transcription-notes)). No assay instance list can be reproduced here.

#### Proband requirement — removed in v2.2

The v2.2 release notes state: *"Removed PS3 text regarding having at least one proband as a requirement to apply PS3. Included reasoning for removing."* The specification's own PS3 Strong/Moderate/Supporting entries contain **no** proband requirement. The `ADA Corrections 1.6.26.docx` erratum file, however, still carries the sentence *"At least one previously observed proband with the expressed ADA variant meeting PP4 is required to apply PS3 at any strength on the basis of a cellular model/in vitro study."* under both Moderate and Supporting. **The operative rule is the specification tables: there is no proband requirement in v2.2.** This is flagged as an unreconciled conflict, not silently corrected.

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
| **Strong** | Caveat: variant must not meet BS1, BS2, or BA1 criteria. *Modification Type: Gene-specific* |
| **Moderate** | Caveat: variant must not meet BS1, BS2, or BA1 criteria. *Modification Type: Gene-specific* |
| **Supporting** | Caveat: variant must not meet BS1, BS2, or BA1 criteria. *Modification Type: Gene-specific* |

> **Gap flagged:** the specification enables PM1 at Strong, Moderate and Supporting but the only text supplied at every strength is the BS1/BS2/BA1 caveat. **No hot spot, no functional domain, no residue list, and no rule for choosing among the three strengths is given by this VCEP**, and no supplementary file addresses PM1. Nothing has been inferred here.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | gnomAD popmax filtering allele frequency **< 0.0001742** (strict less-than). An additional requirement is that **no homozygotes have been observed in gnomAD**. *Modification Type: Gene-specific* |

PM2 is specified at Supporting only.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:**

Use ClinGen SVI adapted recommendations for in trans criterion (see PM3 Criterion attached below, transcribed in [Appendix C](#appendix-c---clingen-svi-recommendation-for-in-trans-criterion-pm3-version-10-table-1-updated-october-17-2025)) with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for ADA.

Caveat: All variants should be sufficiently rare (meet PM2 specification). The applicability of PM3 to suspected founder variants with allele frequencies exceeding the PM2 threshold will be evaluated on a case-by-case basis by the VCEP.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI adapted recommendations for in trans criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for ADA. *Modification Type: General recommendation, Strength* |
| **Strong** | (identical text) *Modification Type: General recommendation, Strength* |
| **Moderate** | (identical text) *Modification Type: General recommendation, Strength* |
| **Supporting** | (identical text) *Modification Type: General recommendation, Strength* |

The point system is the SVI PM3 v1.0 system (Table 1 updated October 17, 2025), distributed as `PM3 Criterion.pdf` and transcribed in [Appendix C](#appendix-c---clingen-svi-recommendation-for-in-trans-criterion-pm3-version-10-table-1-updated-october-17-2025).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | When applied to deletion variants, the deleted region must contain a known pathogenic or likely pathogenic variant that is not predicted/observed to alter splicing. *Modification Type: Gene-specific* |
| **Supporting** | When applied to deletion variants, the deleted region must contain a known VUS variant that is not predicted/observed to alter splicing. *Modification Type: Gene-specific, Strength* |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

For nonsense variants:

- **PM5_Strong** — PM5 may be applied at a Strong level of evidence for any nonsense variant with **4+ points** from informative variants (see below point table). PM5_Strong should be downgraded to PM5_Moderate if PVS1 is applied at any strength.
- **PM5_Moderate** — PM5 may also be applied at a Moderate level of evidence for any nonsense variant with **2+ points** from informative variants (see below point table). PM5_Moderate may not be combined with PVS1_VeryStrong (should be downgraded to PM5_Supporting if PVS1_VeryStrong is applied).
- **PM5_Supporting** — Also applicable to a nonsense variant with **1 point** from an informative variant (see point table). Informative variants must also be classified by these rule specifications.

For missense variants (stated in the Moderate and Supporting entries): Applicable at default strength (PM5) if previously established variant is classified as pathogenic, or at reduced strength of PM5_Supporting if previously established variant is classified as likely pathogenic.

#### PM5 nonsense point table (VCEP-specified)

| Type of variant under assessment (VUA) | Informative variant | Score |
|---|---|---|
| Nonsense variant predicted to lead to NMD | P/LP variant in the exon of DNA change predicted to lead to NMD | **+1 pt** |
| Nonsense variant predicted to lead to NMD | B/LB variant in the exon predicted to lead to NMD | **-2 pt** |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | P/LP variant resulting in a PTC in the same exon but **downstream** of VUA | **+1 pt** |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | B/LB variant resulting in PTC in the same exon but **upstream** of the VUA | **-2 pt** |

NMD = nonsense-mediated decay; PTC premature termination codon *(source text reads "PTC premature termination codon" — the colon/equals sign is missing in the source; transcribed verbatim)*

**Notes (repeated at every strength in the source):** The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet "+1 pathogenic variant downstream" on the PVS1 flowchart. If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA. The VUA must be sufficiently rare, meet PM2_Supporting, to apply this point system. If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic without use of PM5 and without use of only PVS1 plus PM2.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

The following guidelines should be used when determining the phenotypic consistency of each proband:

- "Phenotype highly specific for gene" proband must meet at least **PP4_Moderate** criteria;
- "Phenotype consistent with gene but not highly specific" proband must meet **PP4** criteria;
- "Phenotype consistent with gene but not highly specific and high genetic heterogeneity": proband has been asserted to have a SCID phenotype but does not meet PP4 criteria;
- Reduce points per proband by half if the phase is unconfirmed.

| Strength | Criteria |
|----------|----------|
| **Strong** | Use ClinGen SVI recommendations for de novo criteria (see [Appendix B](#appendix-b---clingen-svi-recommendation-for-de-novo-criteria-ps2--pm6-version-11)). *Modification Type: General recommendation, Gene-specific* |
| **Moderate** | Use ClinGen SVI recommendations for de novo criteria (see Appendix B). *Modification Type: General recommendation, Gene-specific* |
| **Supporting** | Use ClinGen SVI recommendations for de novo criteria (see Appendix B). *Modification Type: General recommendation, Gene-specific* |

> Note: the specification lists **no Very Strong entry for PM6** (PS2 does have one), even though PM6_VeryStrong appears in the SVI table in Appendix B. Transcribed as found.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386) with the additional specification that unaffected individuals contributing to the calculated LOD score (Attached document: PP1 specifications, transcribed in [Appendix D](#appendix-d---pp1-segregation-thresholds-oza-et-al-tables-4a-and-4b)) must be heterozygous carriers of one of the variants observed in the affected individuals (i.e. do not count wild-type/wild-type, individuals).

*(Source typo preserved: "wild-type/wild-type, individuals" — stray comma.)*

| Strength | Criteria |
|----------|----------|
| **Strong** | Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations. *Modification Type: General recommendation* |
| **Moderate** | Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations. *Modification Type: General recommendation* |
| **Supporting** | Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations. *Modification Type: General recommendation* |

Thresholds are in [Appendix D](#appendix-d---pp1-segregation-thresholds-oza-et-al-tables-4a-and-4b). ADA is autosomal recessive, so **Table 4b** applies.

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable.**

*Comments:* Does not apply. The gnomAD v2.1.1 missense Z score for ADA (Z = 0.12) suggests this gene is not constrained for missense variation. Both benign and pathogenic missense variants are present in ADA.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Only applicable to synonymous or intronic variants predicted to impact splicing by SpliceAI with a delta score **greater than or equal to 0.2** (`≥`, inclusive). **Do not apply to missense variants.** *Modification Type: General recommendation* |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

PP4 applicability and strength is determined by the total points accumulated by a **single affected individual** according to the table below and the following total point ranges:

| Total points | Outcome |
|---|---|
| **<1 point** | PP4 not met |
| **1 - <2 points** | PP4 (Supporting) |
| **2 - <6 points** | PP4_Moderate |
| **≥6 points** | PP4_Strong <sup>1</sup> |

*(Comparators as written: lower bounds inclusive, upper bounds strict; ≥6 inclusive.)*

#### PP4 point table

| Evidence Description | Points |
|---|---|
| Diagnostic criteria met for SCID (Criteria 1 and 3 or Criterion 4 by itself) or Leaky SCID/Omenn syndrome (excluding Criterion 2) <sup>1</sup> | 0.5 |
| SCID gene panel or exome/genome sequencing conducted (only applicable if genetic testing did not provide an alternative genetic explanation for SCID/Leaky SCID/Omenn syndrome phenotype) | 1 |
| Family history of SCID (only applicable if SCID gene panel or exome/genome sequencing was conducted on proband and did not provide an alternative genetic explanation for phenotype) | 0.5 |
| Reduced ADA enzyme activity in patient cells (<1-2% of normal ADA catalytic activity) AND/OR increased dAdo nucleotides (dATP or dAXP) in pretreatment or non-transfused erythrocytes above the reference range. PMIDs 20301656 and 39182630 | 5 |
| ADA-SCID phenotype corrected by exogenous ADA supplementation **WITHOUT** CNV testing performed <sup>2</sup> | 4.5 |
| ADA-SCID phenotype corrected by exogenous ADA supplementation **WITH** CNV testing performed <sup>2</sup> | 6 |
| ADA-SCID phenotype corrected by ADA gene therapy **WITHOUT** CNV testing performed <sup>2</sup> | 4.5 |
| ADA-SCID phenotype corrected by ADA gene therapy **WITH** CNV testing performed <sup>2</sup> | 6 |
| T-B-NK- lymphocyte subset profile* (See notes) | 0.5 |

<sup>1</sup> The diagnostic criteria should follow the PIDTC 2022 specification, summarized here. *(The specification says "summarized here" but distributes no PIDTC summary document; see Source Conflicts.)*

<sup>2</sup> CNV (Copy number variation) testing is required if PP4_Strong cannot be reached without points from exogenous ADA supplementation or gene therapy in order to certify that the variant in question is causative for the phenotype, and not one CNV event corrected by gene therapy or enzyme replacement and not previously identified.

*Notes: 1) If NK cells are not noted or are present, criteria may still be applied if SCID gene panel or exome/genome sequencing has ruled out alternative causes; 2) If maternal T cells are present, the T lymphocyte profile is still considered to be T- (autologous T cells are absent).*

| Strength | Criteria |
|----------|----------|
| **Strong** | A patient score of **≥ 6 points**. CNV testing is required if PP4_Strong cannot be reached without points from exogenous ADA supplementation or gene therapy (see footnote 2). *Modification Type: Disease-specific, Gene-specific* |
| **Moderate** | A patient score of **2 - <6 points**. *Modification Type: Disease-specific, Gene-specific* |
| **Supporting** | A patient score of **1 - <2 points**. *Modification Type: Disease-specific, Gene-specific* |

> **Stale attachment warning:** the distributed `PP4 - ADA.pdf` ("Table Updates") carries an **older** CNV footnote — *"CNV testing is required to consider PP4_Strong in order to certify that the variant in question is the causative for the phenotype, and not one CNV event corrected by gene therapy and not identified previously."* The specification body and the `ADA Corrections 1.6.26` erratum both carry the newer wording reproduced above. The newer wording is operative.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable.** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. PubMed: 29543229.

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:**

Maximum credible population allele frequency threshold is determined using the Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:

- Prevalence: 1:5,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.13 (based on the contribution of ADA variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 12.8%, rounded to 13%)
- Penetrance: 50%

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | gnomAD popmax filtering allele frequency **> 0.00721** (strict greater-than). *Modification Type: Gene-specific* |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

gnomAD popmax filtering allele frequency **> 0.00161** (strict greater-than).

Maximum credible population allele frequency threshold determined using the Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:

- Prevalence: 1:50,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.13 (based on the contribution of ADA variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 12.8%, rounded to 13%)
- Penetrance: 100%

<sup>1</sup> Consider also bottleneck populations.

| Strength | Criteria |
|----------|----------|
| **Strong** | gnomAD popmax filtering allele frequency > 0.00161. <sup>1</sup> Consider also bottleneck populations. *Modification Type: Gene-specific* |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | **BS2_Strong:** Can be applied at Strong level if observed in **at least 3 homozygotes**. *Modification Type: Gene-specific* |
| **Supporting** | Only to be used when the variant is observed in the homozygous state in a healthy adult. **BS2_Supporting:** Can be applied at Supporting level if observed in **at least 1 homozygote**. *Modification Type: Gene-specific* |

*(Both thresholds are "at least" — inclusive.)*

New in v2.2: the homozygote counts and the BS2_Strong level were added via the `ADA Corrections 1.6.26` erratum, and both are reflected in the specification tables.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** **Not Applicable** (changed to Not Applicable in v2.2).

*Comments (verbatim):* There is not a well-established functional study which can rule out all damaging effects on protein function. Use of BS3 for ADA was discussed in Dec 19, 2025 meeting and is justified by: - Current BS3_Supporting: Expressed ADA enzyme activity > = 4.8% of wild-type activity (based on group IV) -Change to Not applicable - does not apply - More publications have come out since the 1 paper in 1998. Dr. Hershfield published new data in 2024: Group IV now goes all of the way up to 94.9% of wild-type (Table 2). - How many variants have we applied this to so far? 3 total but only 1 published so far (1 Provisional; 1 In Progress) - would not change classification - Approved by experts/geneticists, 12.19.2025

> The `ADA Corrections 1.6.26` erratum is headed "BS3 Change to Not Applicable" but then still reproduces a **Supporting** entry (`BS3_Supporting: Expressed ADA enzyme activity ≥4.8% of wild-type activity (based on group IV)`). The specification table is the operative source: **BS3 is Not Applicable in v2.2** and the 4.8% threshold is retained only as historical context inside the justification comment.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Can be applied without additional specifications. *Modification Type: None* |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | Does not apply. |
| **BP2** | Not Applicable | (No comment provided.) |
| **BP3** | Not Applicable | Does not apply. |
| **BP4** | Not Applicable | (No comment provided.) |
| **BP5** | Not Applicable | (No comment provided.) |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. PubMed: 29543229. |
| **BP7** | **Supporting** | Applicable to both synonymous variants and deep intronic variants affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions. The variant should be predicted not to impact splicing by at least two out of three in silico tools (freely available tools include GeneSplicer, MaxEntScan, NNSplice, SpliceAI, Splicing Sequences Finder (SSF), and varSEAK). Given the potential for poor conservation of genes related to T cell and B cell development among vertebrates, nucleotide conservation is not required in order to apply BP7. *Modification Type: General recommendation* |

*(BP7 source oddity preserved: "at least two out of three in silico tools" is followed by a list of six tools.)*

---

## Rules for Combining Criteria

Transcribed verbatim from the specification (Richards et al., 2015 combining-rules framework as modified by this VCEP).

### Pathogenic

- 1 Very Strong (PVS1, PS2_Very Strong, PM3_Very Strong) **AND** ≥ 1 Strong (PVS1_Strong, PS1, PS2, PS3, PM1_Strong, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong)
- 1 Very Strong **AND** ≥ 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate)
- 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting (PVS1_Supporting, PS2_Supporting, PS3_Supporting, PM1_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)
- 1 Very Strong **AND** ≥ 2 Supporting
- ≥ 2 Strong
- 1 Strong **AND** ≥ 3 Moderate
- 1 Strong **AND** 2 Moderate **AND** ≥ 2 Supporting
- 1 Strong **AND** 1 Moderate **AND** ≥ 4 Supporting

### Likely Pathogenic

- 1 Very Strong **AND** 1 Moderate
- 1 Strong **AND** 1 Moderate
- 1 Strong **AND** ≥ 2 Supporting
- ≥ 3 Moderate
- 2 Moderate **AND** ≥ 2 Supporting
- 1 Moderate **AND** ≥ 4 Supporting
- 1 Strong **AND** 2 Moderate
- **1 Very Strong AND 1 Supporting** *(added in v2.2)*

### Benign

- ≥ 2 Strong (BS1, BS2, BS4)
- 1 Stand Alone (BA1)

### Likely Benign

- ≥ 2 Supporting (BS2_Supporting, BP7)
- **1 Strong (BS1, BS2, BS4)** *(added in v2.2)*

### Evidence-strength membership lists (as given in the source)

| Strength bucket | Codes |
|---|---|
| **Very Strong** | PVS1, PS2_Very Strong, PM3_Very Strong |
| **Strong (pathogenic)** | PVS1_Strong, PS1, PS2, PS3, PM1_Strong, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong |
| **Moderate** | PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate |
| **Supporting (pathogenic)** | PVS1_Supporting, PS2_Supporting, PS3_Supporting, PM1_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4 |
| **Stand Alone** | BA1 |
| **Strong (benign)** | BS1, BS2, BS4 |
| **Supporting (benign)** | BS2_Supporting, BP7 |

> Note: the pathogenic-Strong membership list includes **PM6_Strong** and the Moderate list includes **PM6**, but the specification's PM6 section defines Strong / Moderate / Supporting only (no PM6_VeryStrong), while the Very Strong bucket lists only PVS1, PS2_Very Strong and PM3_Very Strong. Transcribed as found.

---

## Appendices

### Appendix A - ADA-specified PVS1 flowchart

Source: `PVS1.pdf`, "Specified PVS1 flowchart for ADA gene" (1 page, vector flowchart; transcribed from the extracted text into decision paths below). The chart follows the ClinGen SVI PVS1 structure (Tayoun et al., 2018) with **one ADA-specific insertion**: the NMD boundary is defined as *"premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon [c.1028 (codon 343) in exon 11]"*.

Footnote markers `a`, `b`, `d` appear on the chart but their footnote text is not present in the distributed file.

**Branch 1 — Nonsense or Frameshift**

- Predicted to undergo NMD <sup>b</sup>
  - Exon is present in biologically-relevant transcript(s) → **PVS1**
  - Exon is absent from biologically-relevant transcript(s) → **N/A**
- Not predicted to undergo NMD <sup>b</sup> (i.e. premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon [c.1028 (codon 343) in exon 11])
  - Truncated/altered region is critical to protein function → **PVS1_Strong**
  - Role of region in protein function is unknown
    - LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) → **N/A**
    - LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s)
      - Variant removes >10% of protein
        - 1+ pathogenic variant present downstream → **PVS1_Strong**
        - No known downstream pathogenic variants → **PVS1_Moderate**
      - Variant removes <10% of protein → **PVS1_Moderate**

**Branch 2 — GT--AG ±1,2 splice sites <sup>a</sup>**

- Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD <sup>b</sup>
  - Exon is present in biologically-relevant transcript(s) → **PVS1**
  - Exon is absent from biologically-relevant transcript(s) → **N/A**
- Exon skipping or use of a cryptic splice site disrupts reading frame and is **NOT** predicted to undergo NMD <sup>b</sup> (i.e. premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon [c.1028 (codon 343) in exon 11])
  - Truncated/altered region is critical to protein function → **PVS1_Strong**
  - Role of region in protein function is unknown
    - LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) → **N/A**
    - LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s)
      - Variant removes >10% of protein
        - 1+ pathogenic variant present downstream → **PVS1_Strong**
        - No known downstream pathogenic variants → **PVS1_Moderate**
      - Variant removes <10% of protein → **PVS1_Moderate**
- Exon skipping or use of a cryptic splice site preserves reading frame → routed to the "role of region" evaluation above (**PVS1_Strong** if truncated/altered region is critical to protein function; otherwise **N/A** or **PVS1_Strong / PVS1_Moderate** per the >10% / <10% branch)

**Branch 3 — Deletion (single exon to full gene)**

- Full gene deletion → **PVS1** <sup>d</sup>
- Single to multi exon deletion — disrupts reading frame and is predicted to undergo NMD <sup>b</sup>
  - Exon is present in biologically-relevant transcript(s) → **PVS1**
  - Exon is absent from biologically-relevant transcript(s) → **N/A**
- Single to multi exon deletion — disrupts reading frame and is **NOT** predicted to undergo NMD <sup>b</sup> (i.e. premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon [c.1028 (codon 343) in exon 11])
  - Truncated/altered region is critical to protein function → **PVS1_Strong**
  - Role of region in protein function is unknown
    - LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) → **N/A**
    - LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s)
      - Variant removes >10% of protein
        - 1+ pathogenic variant present within deleted region → **PVS1_Strong**
        - No known pathogenic variants within deleted region → **PVS1_Moderate**
      - Variant removes <10% of protein → **PVS1_Moderate**
- Single to multi exon deletion — preserves reading frame → same "role of region" evaluation, with **1+ pathogenic variant present within deleted region → PVS1_Moderate** / **No known pathogenic variants within deleted region → PVS1_Moderate**

**Branch 4 — Duplication (≥1 exon in size and must be completely contained within gene)**

- Proven in tandem
  - Reading frame disrupted and NMD predicted to occur → **PVS1**
  - No or unknown impact on reading frame and NMD → **N/A**
- Presumed in tandem
  - Reading frame presumed disrupted and NMD predicted to occur → **PVS1_Strong**
- Proven not in tandem → **N/A**

**Branch 5 — Initiation Codon**

- Different functional transcript uses alternative start codon → **N/A**
- No known alternative start codon in other transcripts
  - ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1_Moderate**
  - No pathogenic variant(s) upstream of closest potential in-frame start codon → **PVS1_Supp**

> Transcription caveat: `PVS1.pdf` is a single-page graphical flowchart. The connector geometry for the duplication and "preserves reading frame" sub-branches is not fully recoverable from the text layer; the branch structure above is reconstructed from the SVI PVS1 layout that the chart follows. Where a routing is ambiguous it is stated as such rather than guessed. Consult the original PDF for the authoritative graphic.

---

### Appendix B - ClinGen SVI Recommendation for de novo Criteria (PS2 & PM6), Version 1.1

Source: `PS2_PM6.pdf`, 2 pages. Date approved March 18, 2018, updated May 5, 2021. Changes from v1: clarified that confirmed/assumed is with regards to parental relationships and not de novo status.

The SVI proposes a point-based system based upon three parameters: confirmed vs assumed parental relationships status; phenotypic consistency; number of de novo observations. Each proband with a de novo variant is awarded a point value from Table 1; the combined point value is compared to Table 2. **If the parents have not been tested for parentage or for the variant, no points should be awarded.**

**Table 1. Points\* awarded per de novo occurrence**

| Phenotypic consistency | de novo with **confirmed** parental relationships | de novo with **unconfirmed** parental relationships |
|---|---|---|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity** | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

\* Note that these points are not equivalent to the points used to classify a variant per the Tavtigian et al 2020 "Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines"
\*\* Maximum allowable value of 1 may contribute to overall score

**Table 2. Recommendation for determining the appropriate ACMG/AMP evidence strength level for de novo occurrence(s)**

| Supporting (PS2_Supporting or PM6_Supporting) | Moderate (PS2_Moderate or PM6) | Strong (PS2 or PM6_Strong) | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |
|---|---|---|---|
| 0.5 | 1 | 2 | 4 |

**Additional considerations for applying de novo criteria based on inheritance (verbatim):**

- **Conditions with X-linked inheritance:** if the variant occurs de novo in an unaffected carrier mother, and family history is consistent - i.e., she has no affected brothers/other male relatives apart from her affected son(s) – de novo criteria may be applied despite the fact that she is unaffected.
- **Autosomal recessive conditions:** for a de novo occurrence in a gene associated with a condition inherited in an autosomal recessive pattern without an additional pathogenic/likely pathogenic variant identified, **the strength of evidence should be decreased by one level.** *(ADA is autosomal recessive — this applies.)*
- **Mosaicism:** for cases with apparent germline mosaicism (multiple affected siblings with both parents negative for the variant), parental relationships must be confirmed in order for de novo criteria to apply.

For all uses of de novo criteria, the phenotype in the patient must be consistent with the gene/disease association as recommended in the ACMG/AMP guidelines. When the patient's phenotype is consistent with the gene/disease association but not highly specific, SVI recommends decreasing the points awarded. (The source gives worked examples using NIPBL, SIK1 and ASH1L; these are illustrative and not ADA-specific.)

---

### Appendix C - ClinGen SVI Recommendation for in trans Criterion (PM3), Version 1.0 (Table 1 updated October 17, 2025)

Source: `PM3 Criterion.pdf`, 2 pages. Date approved May 2, 2019; Table 1 updated October 17, 2025. Table 2 is embedded as an image in the PDF and was read from that image.

**SVI revision to PM3:** For recessive disorders, detected in trans with a pathogenic or likely pathogenic variant **in an affected patient**.

**Table 1. Points awarded per in trans proband**

| Classification/Zygosity of other variant | Confirmed in trans | Phase unknown |
|---|---|---|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence, Non-consanguineous** (no max) | 1.0 | 1.0 |
| Homozygous occurrence, Consanguineous** (no max) | 0.5 | 0.5 |
| Uncertain significance variant (max point 0.5) | 0.25 | 0 |

\* Multiple probands from separate nuclear families that are later found to have identity-by-descent should only be counted once.
\*\* When consanguinity is not known or reported: if family IS NOT from a bottlenecked population (as defined by gnomAD), assume non-consanguinity; otherwise, assume consanguinity. If genetic ancestry of the family cannot be determined, assume consanguinity.

**Table 2. Recommendation for determining the appropriate evidence strength level for PM3**

| PM3_Supporting | PM3 | PM3_Strong | PM3_VeryStrong |
|---|---|---|---|
| 0.5 | 1.0 | 2.0 | 4.0 |

**Considerations (verbatim):**

- **Allele Frequency** — Application of PM3 is contingent on the allele frequency of the variant being assessed and the variant presumably on the other allele both being sufficiently rare (meets PM2 threshold). This contingency is to avoid incorrect application of PM3 to high frequency variants that are likely to occur in trans with P/LP variants based on frequency.
- **Phasing** — If the phase cannot be determined, it is recommended that at least two different LP/P variants (depending on classifications) are needed to equal the weight of one LP/P co-occurrence confirmed in trans. In confirmation of phasing, if only one parent is tested and found to carry one allele, variants can be counted as in trans.
- **Classification** — Probands should be weighted less when the variant on the other allele is of uncertain significance and rare (meets PM2); however, weight may vary by gene size as larger genes are more likely to have a second variant by chance (default 0.25 points). If the variant on the other allele is classified as P or LP, weighting depends on phasing, with P/LP being weighted equally if confirmed in trans and different point values per proband if phasing is unknown (0.5 points and 0.25 points, respectively). To avoid circularity, in all instances (phasing confirmed or unknown), the classification of the variant on the other allele should not use evidence from the variant being interrogated.
- **Homozygous occurrences** — For homozygous occurrences, the default weight is dropped to 0.5 points, as a rare homozygous occurrence may be due to consanguinity. A recommended max of 1.0 points of all homozygous cases is suggested to prevent overclassification of homozygous occurrences in the absence of additional data.

> Internal inconsistency in the SVI source: Table 1 labels both homozygous rows "(no max)", while the Considerations text states "a recommended max of 1.0 points of all homozygous cases is suggested". Transcribed as found; not reconciled.

---

### Appendix D - PP1 segregation thresholds (Oza et al., Tables 4a and 4b)

Source: `PP1.pdf`, 2 pages — reprint pages 35-36 of Oza et al. (Hum Mutat; PMID: 30311386).

**Table 4a: Recommendations for PP1 (segregation evidence) — General Recommendations**

| | Supporting | Moderate | Strong |
|---|---|---|---|
| Likelihood | 4:1 | 16:1 | 32:1 |
| LOD Score | 0.6 | 1.2 | 1.5 |
| Autosomal dominant threshold | 2 affected segregations | 4 affected segregations | 5 affected segregations |
| Autosomal recessive threshold | See Table 4b | See Table 4b | See Table4b |

*(Source typo preserved in the last cell: "See Table4b", missing space.)*

**Table 4b: Recommendations for autosomal recessive segregation evidence (PP1) — General Recommendations (Phenocopy not an issue)**

This is a **lookup table**: find the row for the number of affected segregations and the column for the number of unaffected recessive segregations; the cell is the LOD score, which is then compared against the Table 4a LOD thresholds (0.6 Supporting / 1.2 Moderate / 1.5 Strong).

| Affected ↓ \ Unaffected → | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
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

**Table 4b legend (verbatim):** Affected segregations are counted in rows and unaffected segregations in columns. Affected segregations are affected family members in whom biallelic compound heterozygous or homozygous variants segregates. Unaffected segregations are defined as unaffected family members, typically siblings, who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants identified in the proband, or a heterozygous carrier for a single variant. Unaffected, carrier parents DO NOT count as unaffected segregations. There may be scenarios where individuals other than siblings could be counted as segregations, such as in families where one parent is affected with the autosomal recessive disorder, in large families with multiple branches, or in consanguineous families. Each cell shows the LOD score of each combination of affected and unaffected segregations. LOD scores were calculated using a simplified LOD score formula, as described in Strande et al., 2017.

**ADA-specific overlay (from the specification body):** unaffected individuals contributing to the calculated LOD score must be heterozygous carriers of one of the variants observed in the affected individuals (i.e. do not count wild-type/wild-type individuals). *Note this ADA restriction is narrower than the Oza legend, which permits counting unaffected individuals who are wild-type for both variants.* Both are transcribed; the ADA specification governs for ADA.

---

### Appendix E - ADA Corrections 1.6.26 (erratum file), transcribed in full

Source: `ADA Corrections 1.6.26.docx` (referenced by the specification as "ADA Corrections 1.6.26", and in the release notes as "ADA corrections 1.6.26_MS_Updated 5.29.26"). Document title: **"Criteria & Strength Specifications for ADA"**. It covers four criteria only: PS3, BS2, BS3, PP4.

**PS3** — "SVI Recommended Resources: Functional assay sheet. Please follow the instructions in the sheet."

- *Strong Specification:* PS3 may potentially be applied at the default strength level of Strong for evidence from an animal model expressing the variant of interest and recapitulating the ADA-SCID phenotype. Modification Type: Gene-specific
- *Moderate Specification:* The strength of evidence from cellular models/in vitro studies is dependent upon the level of expressed ADA enzyme activity based on levels defined in Arredondo-Vega et al., 1998 (PMID: 9758612): PS3_Moderate: ≤0.05% of wild-type activity (group I). **"At least one previously observed proband with the expressed ADA variant meeting PP4 is required to apply PS3 at any strength on the basis of a cellular model/in vitro study."** Modification Type: Gene-specific
- *Supporting Specification:* ... PS3_Supporting: 0.06-0.6% of wild-type activity (groups II and III). **"At least one previously observed proband with the expressed ADA variant meeting PP4 is required to apply PS3 at any strength on the basis of a cellular model/in vitro study."** Modification Type: Gene-specific; Strength

**BS2**

- *Supporting Specification:* Only to be used when the variant is observed in the homozygous state in a healthy adult. BS2_Supporting: Can be applied at Supporting level if observed in at least 1 homozygote. Modification Type: Gene-specific
- *Strong Specification:* BS2_Strong: Can be applied at Strong level if observed in at least 3 homozygotes. Modification Type: Gene-Specific *(source capitalises "Specific" here and not elsewhere; preserved)*

**BS3 — "Change to Not Applicable."**

- *Supporting:* The strength of evidence from cellular models/in vitro studies is dependent upon the level of expressed ADA enzyme activity based on levels defined in Arredondo-Vega et al., 1998 (PMID: 9758612): BS3_Supporting: Expressed ADA enzyme activity ≥4.8% of wild-type activity (based on group IV). Modification Type: Gene-specific

**PP4** — the erratum reproduces the full PP4 point table and strength ranges. Its content matches the specification body reproduced in the PP4 section above, including the **revised** footnote 2 on CNV testing and the footnote 1 pointer to the PIDTC 2022 specification. It ends with "Find attached the PP4 table."

---

## Source Conflicts and Transcription Notes

Every conflict below is reported, not resolved. Where an operative rule must be identified, the specification's own criteria tables are treated as authoritative over the erratum attachment, and this is stated each time.

1. **PS3 proband requirement — erratum contradicts the specification tables.** The v2.2 release notes explicitly say the proband requirement was *removed*, and the specification's PS3 entries contain no such requirement. The `ADA Corrections 1.6.26.docx` erratum still contains it twice. **Operative: no proband requirement.** This is the same failure mode previously seen with the InSiGHT MMR erratum: the erratum file was not re-cut when the rule changed.

2. **BS3 — erratum internally inconsistent.** The erratum is headed "BS3 Change to Not Applicable" but then reproduces a live BS3_Supporting rule at ≥4.8% of wild-type activity. **Operative: BS3 is Not Applicable** per the specification table and the recorded 12.19.2025 expert approval.

3. **PS3 functional assay sheet is missing from the distribution.** The release notes claim "Uploaded SCID VCEP PS3 Functional Evidence (ADA) 6.2.26" and the erratum instructs the curator to "follow the instructions in the sheet", but **no such file is present** among the seven distributed files (`GN114_data.json` lists the complete expected set and does not include it). The approved-assay list therefore cannot be reproduced. Not inferred.

4. **`PP4 - ADA.pdf` is stale relative to the specification.** Its CNV footnote reads "CNV testing is required **to consider** PP4_Strong ... and not one CNV event corrected by gene therapy and not identified previously", whereas the specification and erratum read "required **if PP4_Strong cannot be reached without points from exogenous ADA supplementation or gene therapy** ... corrected by gene therapy **or enzyme replacement** and not previously identified." The footnote numbering is also swapped between the two documents (PDF: 1 = CNV, 2 = PIDTC; specification: 1 = PIDTC, 2 = CNV). **Operative: the specification wording.**

5. **PP4 footnote 1 points to a PIDTC 2022 summary that is not distributed.** The text says "The diagnostic criteria should follow the PIDTC 2022 specification, summarized here", with "here" being a hyperlink whose target is not recoverable from the PDF text layer and whose content is not included in the file set. The SCID diagnostic criteria numbering ("Criteria 1 and 3", "Criterion 4", "excluding Criterion 2") is therefore **not defined anywhere in this package**. Not filled in.

6. **PM1 has no substantive specification.** PM1 is enabled at Strong, Moderate and Supporting but the only text at every level is "Caveat: variant must not meet BS1, BS2, or BA1 criteria." No hot spot, domain, residue set, or strength-selection rule is given, and no supplementary file covers PM1.

7. **PM6 has no Very Strong entry** in the specification, yet PM6_VeryStrong appears in the SVI Table 2 that the specification adopts by reference. Also, the combining-rules Very Strong bucket lists only PVS1, PS2_Very Strong and PM3_Very Strong.

8. **PS2/PM6 "Reduce points per proband by half if the phase is unconfirmed."** For de novo criteria the SVI parameter is *parental relationship* confirmation, not phase; and the SVI Table 1 already encodes the halving in its "unconfirmed parental relationships" column. As written this is either a wording error or a double reduction. Transcribed verbatim, not reconciled.

9. **PP1: ADA overlay vs Oza legend.** The ADA specification requires unaffected contributors to be heterozygous carriers, excluding wild-type/wild-type individuals; the Oza Table 4b legend explicitly permits "either wild-type for both variants ... or a heterozygous carrier for a single variant". Both transcribed; the ADA restriction governs for ADA.

10. **SVI PM3 Table 1 vs Considerations:** homozygous rows are marked "(no max)" while the Considerations text recommends a 1.0-point maximum across all homozygous cases.

11. **BP7 "at least two out of three in silico tools"** is followed by a list of six named tools.

12. **Source typos preserved:** "See Table4b" (PP1 Table 4a); "wild-type/wild-type, individuals" (PP1 spec text); "PTC premature termination codon" (PM5 legend, missing colon); "> = 4.8%" (BS3 comment); "Criterion2" and "the variant in question is **the** causative for the phenotype" (`PP4 - ADA.pdf`); "Gene-Specific" vs "Gene-specific" inconsistency (erratum BS2); "Type: Richards et.al., 2015" (missing space after "et").

13. **PDF text-layer artifacts (not source errors):** the combining-criteria section of the specification PDF contains a garbled repeated fragment (`_ pp g _ pp g ...`) at the page 19/20 boundary, and footnote superscripts render as stray digits `1`/`2` on separate lines in the PP4 and BS1 sections. `PM3 Criterion.pdf` and `PP4 - ADA.pdf` carry a "Wondershare PDFelement" watermark image on every page.

14. **Files that could not be read: none.** All seven distributed files opened and were transcribed. `PM3 Criterion.pdf` Table 2 exists only as an embedded raster image; it was extracted and read visually. `PVS1.pdf` is a vector flowchart whose text layer is recoverable but whose connector geometry is only partially recoverable — this is stated in Appendix A rather than guessed at.

---

## Source File Inventory

| File | Type | Opened | Transcribed where |
|---|---|---|---|
| `ClinGen_ACMG_Specifications_ADA_v2.2.pdf` | PDF, 20 pp | Yes | Whole document |
| `PS2_PM6.pdf` | PDF, 2 pp | Yes | Appendix B (complete) |
| `PM3 Criterion.pdf` | PDF, 2 pp + 1 embedded table image | Yes | Appendix C (complete, incl. image-only Table 2) |
| `PP1.pdf` | PDF, 2 pp | Yes | Appendix D (complete, both tables) |
| `PVS1.pdf` | PDF, 1 p, vector flowchart | Yes | Appendix A (text complete; geometry partially reconstructed, caveated) |
| `PP4 - ADA.pdf` | PDF, 1 p (+3 watermark images) | Yes | PP4 section + conflict #4 |
| `ADA Corrections 1.6.26.docx` | DOCX, 55 paragraphs + 1 table | Yes | Appendix E (complete) |
| `GN114_data.json` | Metadata | Yes | Not part of the guideline (per skill instructions) |

---

## Version History

**Version 2.2** — Released 7/17/2026. Release notes as published by the VCEP:

- Edited Rules for Combining Criteria to reflect standard combinations plus (A) 1 very strong + 1 supporting = Likely Pathogenic and (B) 1 Strong Benign = Likely Benign.
- Removed ADA Amendments 12.12.25
- Uploaded ADA corrections 1.6.26_MS_Updated 5.29.26
  1. Removed PS3 text regarding having at least one proband as a requirement to apply PS3. Included reasoning for removing.
  2. Edits to footnotes for PP4
  3. Added number of homozygotes needed to apply certain strengths for BS2.
  4. Added BS2_Strong strength
  5. Changed BS3 to Not Applicable. Added text to justify why it's not applicable.
- Uploaded SCID VCEP PS3 Functional Evidence (ADA) 6.2.26
- Removed BS3 from original document since it is not applicable.
- Removed original PS3 document that included BS3 and replaced with the above document.

*(Trailing whitespace after item 4 preserved in the source; "it's" for "its" in item 5 preserved.)*

---

*This document was compiled from the ClinGen VCEP specification and its distributed supplementary files. For the most current version, please refer to the ClinGen website.*
