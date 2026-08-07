# ClinGen Severe Combined Immunodeficiency Disease VCEP Variant Interpretation Guidelines for IL7R

**Version:** 2.2
**Released:** 5/15/2026
**Affiliation:** Severe Combined Immunodeficiency Disease VCEP
**Source basis:** Richards et al., 2015 - Combining rules
**DOI:** 10.5281/zenodo.21434466
**ClinGen Criteria Specification Registry ID:** GN119

**Release Notes (verbatim from the specification):**

> Edited Rules for Combining Criteria to reflect standard combinations plus (A) 1 very strong + 1 supporting = Likely Pathogenic and (B) 1 Strong Benign = Likely Benign.
>
> Rules for Combining Criteria refreshed and saved.
>
> Uploaded two files to address minor PM3 changes:
>
> 1. "PM3 Criterion: October 2025 Version, Minor Updates"
> 2. "PM3: svi recommendations: October 2025 Group Responses to Minor Updates"
>
> Uploaded IL7R corrections which includes PM1 and PS3 codes.
>
> - Made edits to PS3 text
> - Made updates to subscript text for PP4 criteria.
> - Added BS2_Strong strength
>   - Edited text for BS2_Supporting

**Rights Holder:** The Clinical Genome Resource (ClinGen)

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | IL7R (HGNC:6024) |
| **HGNC Name** | interleukin 7 receptor |
| **Transcript** | NM_002185.5 |
| **Disease** | immunodeficiency 104 (MONDO:0012163) |
| **Inheritance** | Autosomal recessive inheritance |

**Keywords (as listed by the VCEP):** human biology genomics variant variant classification clingen disease standards IL7R NM_002185.5 Autosomal recessive inheritance immunodeficiency 104

---

## Source Files Used

All eight distributed files were opened and transcribed. None failed to open.

| File | Type | Status |
|------|------|--------|
| `ClinGen_ACMG_Specifications_IL7R_v2.2.pdf` | Main specification (20 pages) | Transcribed |
| `PM3 Criterion.pdf` ("PM3 Criterion: October 2025 Version, Minor Updates") | SVI PM3 recommendation v1.0, Table 1 updated 17 Oct 2025 (2 pages) | Transcribed |
| `PM3 Minor Amendments 12.12.2025.docx` ("PM3: svi recommendations: October 2025 Group Responses to Minor Updates") | SVI comments + VCEP responses + revised Table 1 | Transcribed |
| `PP4 - IL7R.pdf` ("PP4 - IL7R: 2025 Updates") | PP4 point table (1 page) | Transcribed |
| `PP1.pdf` ("PP1: PP1 specifications") | Oza et al. Tables 4a/4b (2 pages) | Transcribed |
| `PS2_PM6.pdf` ("PS2_PM6: SVI recommendations for de novo criteria") | SVI de novo recommendation v1.1 (2 pages) | Transcribed |
| `PVS1.pdf` ("PVS1: Specified PVS1 flowchart for IL7R gene") | Gene-specific PVS1 decision tree (1 page) | Transcribed |
| `SCID VCEP PS3_BS3 Functional Evidence (IL7R).xlsx` | 2 worksheets | Transcribed |

`GN119_data.json` is download metadata and is not source material.

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

**VCEP Specifications:** See attached PVS1 flowchart. (Reproduced in [Appendix A](#appendix-a--pvs1-decision-flowchart-il7r-specific).)

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)). *Modification type: General recommendation, Gene-specific* |
| **Strong** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with two specifications: (1) For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 8, or variants in the last 50 nucleotides of the penultimate exon after c.826, codon 276, in exon 7), at least one pathogenic variant **must be** present downstream in order to apply PVS1_Strong. (2) PVS1_Strong can be applied to variants predicted to undergo nonsense-mediated decay but causing truncation of the transmembrane domain (which begins at amino acid 240) or any distal region (i.e. cytoplasmatic domain). *Modification type: General recommendation, Gene-specific* |
| **Moderate** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification: For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 8, or variants in the last 50 nucleotides of the penultimate exon after c.826, codon 276, in exon 7), when at least one pathogenic variant is **not** present downstream downgrade to PVS1_Moderate. *Modification type: General recommendation* |
| **Supporting** | No PVS1_Supporting row is defined in the specification's strength table. The attached flowchart does assign **PVS1_Supp** to one terminal branch (Initiation Codon, no known alternative start codon in other transcripts, no pathogenic variant(s) upstream of closest potential in-frame start codon). |

> **Source note (typo preserved):** the Strong row reads "cytoplasmatic domain"; the flowchart reads "cytoplasmic domain".

> **Apparent internal inconsistency:** the Strong row states PVS1_Strong applies to variants **predicted to undergo** NMD that truncate the transmembrane domain or distal region. In the flowchart, the "Truncated/altered region is critical to protein function – causes truncation of the transmembrane domain (which begins at amino acid 240) or any distal region (i.e. cytoplasmic domain)" → PVS1_Strong branches all sit under the **NOT predicted to undergo NMD** (or reading-frame-preserving) arms; variants predicted to undergo NMD in a biologically-relevant exon go to full PVS1. Transcribed as written in both sources; not reconciled here.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T. Applicable if the previously established variant is classified as **pathogenic** by SCID VCEP specifications for *IL7R*. *Modification type: Gene-specific* |
| **Moderate** | It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be likely pathogenic, can use PS1 for c.105+1G>T. Applicable if the previously established variant is classified as **likely pathogenic** by SCID VCEP specifications for *IL7R*. *Modification type: Gene-specific, Strength* |

> **Source note:** the Moderate row's example sentence ends without a period and reuses the PS1 label rather than PS1_Moderate; transcribed verbatim.

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
| **Very Strong** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification type: General recommendation, Gene-specific* |
| **Strong** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification type: General recommendation, Gene-specific* |
| **Moderate** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification type: General recommendation, Gene-specific* |
| **Supporting** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification type: General recommendation, Gene-specific* |

The referenced SVI *de novo* recommendation is distributed with this specification as `PS2_PM6.pdf` and is reproduced in full in [Appendix D](#appendix-d--svi-recommendation-for-de-novo-criteria-ps2--pm6-version-11). Its point table and strength ladder are therefore source-backed for this VCEP.

> **Apparent VCEP wording error:** the bullet "Reduce points per proband by half if the phase is unconfirmed" uses "phase" where the SVI *de novo* framework distinguishes **confirmed vs. unconfirmed parental relationships** (phase is a PM3 concept). Note also that the SVI Table 1 already encodes the halving as its second column (2→1, 1→0.5, 0.5→0.25), so applying the VCEP bullet on top of Table 1 would halve twice. Transcribed as written; not reconciled here.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

| Strength | Criteria |
|----------|----------|
| **Strong** | PS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and recapitulating the IL7R-SCID phenotype. Animal models will be reviewed on a case-by-case basis by the VCEP to determine the appropriate strength level. *Modification type: Gene-specific* |
| **Moderate** | Not specified by VCEP (no PS3_Moderate row appears in the specification). |
| **Supporting** | PS3_Supporting can be applied based on an abnormal result in **at least one** approved *in vitro* assay (IL-7-induced Jak3 phosphorylation assay, IL-7 binding assay, IL-7-induced STAT5 DNA binding/transcriptional induction). *Modification type: Gene-specific, Strength* |

#### Approved Assay Instances (as listed in the main specification)

| General class of assay | Reference |
|---|---|
| IL-7-induced Jak3 phosphorylation assay | Roifman et al., 2000 (PMID: 11023514) |
| IL-7 binding assay | Puel et al., 1998 (PMID: 9843216) |
| IL-7-induced STAT5 DNA binding/transcriptional induction | Puel et al., 1998 (PMID: 9843216) |

The full assay-instance dossier from `SCID VCEP PS3_BS3 Functional Evidence (IL7R).xlsx` is reproduced in [Appendix F](#appendix-f--ps3bs3-functional-evidence-workbook-il7r).

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance. Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** **Not Applicable.** (No comment provided by the VCEP.)

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** Caveat: variant must not meet BS1, BS2, BA1 criteria

| Strength | Criteria |
|----------|----------|
| **Strong** | Caveat: variant must not meet BS1, BS2, BA1 criteria *Modification type: Gene-specific* |
| **Moderate** | Caveat: variant must not meet BS1, BS2, BA1 criteria *Modification type: Gene-specific* |
| **Supporting** | Caveat: variant must not meet BS1, BS2, BA1 criteria *Modification type: Gene-specific* |

> **Apparent VCEP error / incomplete entry:** every PM1 row in the v2.2 specification contains only the caveat text. The specification defines **no** hot spot, domain, or residue set, and gives no basis for choosing among PM1_Strong, PM1_Moderate and PM1_Supporting. The v2.2 release notes state "Uploaded IL7R corrections which includes PM1 and PS3 codes", but no PM1 substance appears in the published record or in any distributed supplementary file. **The operative PM1 rule is therefore not specified by this VCEP**; no content has been supplied here to fill the gap. PM1 at Strong, Moderate and Supporting does appear in the Rules for Combining Criteria.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | gnomAD popmax filtering allele frequency **<0.00004129** (strict less-than). An additional requirement is that **no homozygotes** have been observed in gnomAD. *Modification type: Gene-specific* |

**Comparator:** strict (`<`). Not inclusive.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Use ClinGen SVI adapted recommendations for *in trans* criterion (see PM3 criterion attached below) with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for *IL7R*.

Caveat: All variants should be sufficiently rare (meet PM2 specification). The applicability of PM3 to suspected founder variants with allele frequencies exceeding the PM2 threshold will be evaluated on a case-by-case basis by the VCEP.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI adapted recommendations for *in trans* criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for *IL7R*. *Modification type: General recommendation, Strength* |
| **Strong** | (same text as Very Strong) *Modification type: General recommendation, Strength* |
| **Moderate** | (same text as Very Strong) *Modification type: General recommendation, Strength* |
| **Supporting** | (same text as Very Strong) *Modification type: General recommendation, Strength* |

#### PM3 Point System (from the distributed `PM3 Criterion.pdf`, Table 1 updated October 17, 2025)

**Table 1. Points awarded per in trans proband**

| Classification/Zygosity of other variant | Points per Proband-Family\* — Confirmed in *trans* | Points per Proband-Family\* — Phase unknown |
|---|---|---|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence — Non-consanguineous\*\* *(no max)* | 1.0 | 1.0 |
| Homozygous occurrence — Consanguineous\*\* *(no max)* | 0.5 | 0.5 |
| Uncertain significance variant *(max point 0.5)* | 0.25 | 0 |

\*Multiple probands from separate nuclear families that are later found to have identity-by-descent should only be counted once.

\*\*When consanguinity is not known or reported: if family IS NOT from a bottlenecked population (as defined by gnomAD), assume non-consanguinity; otherwise, assume consanguinity. If genetic ancestry of the family cannot be determined, assume consanguinity.

**Table 2. Recommendation for determining the appropriate evidence strength level for PM3**

| PM3_Supporting | PM3 | PM3_Strong | PM3_VeryStrong |
|---|---|---|---|
| 0.5 | 1.0 | 2.0 | 4.0 |

Thresholds are stated as bare point values in the source; the source's own worked example applies PM3_Strong at exactly 2.0 points, i.e. the thresholds behave as inclusive (`>=`).

**SVI revision to the criterion definition:** For recessive disorders, detected in trans with a pathogenic *or likely pathogenic* variant *in an affected patient*.

Full considerations text and the 12.12.2025 amendment record are in [Appendix C](#appendix-c--svi-recommendation-for-in-trans-criterion-pm3-version-10) and [Appendix G](#appendix-g--pm3-minor-amendments-12122025).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Criteria |
|----------|----------|
| **Moderate** | When applied to deletion variants, the deleted region must contain a known **pathogenic** or **likely pathogenic** variant that is not predicted/observed to alter splicing. *Modification type: Gene-specific* |
| **Supporting** | When applied to deletion variants, the deleted region must contain a known **VUS** variant that is not predicted/observed to alter splicing. *Modification type: Gene-specific, Strength* |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** For nonsense variants:

- **PM5_Strong** — PM5 may be applied at a Strong level of evidence for any nonsense variant with 4+ points from informative variants (see below point table). PM5_Strong should be downgraded to PM5_Moderate if PVS1 is applied at any strength.
- **PM5_Moderate** — PM5 may also be applied at a Moderate level of evidence for any nonsense variant with 2+ points from informative variants (see below point table). PM5_Moderate may not be combined with PVS1_VeryStrong (should be downgraded to PM5_Supporting if PVS1_VeryStrong is applied).
- **PM5_Supporting** — Also applicable to a nonsense variant with 1 point from an informative variant (see point table). Informative variants must also be classified by these rule specifications.

Additionally, at the Moderate and Supporting rows the specification states: "Applicable at default strength (PM5) if previously established variant is classified as pathogenic or at reduced strength of PM5_Supporting if previously established variant is classified as likely pathogenic."

#### PM5 Point Table — Type of variant under assessment (VUA); Informative variant; Score

| Type of variant under assessment (VUA) | Informative variant | Score |
|---|---|---|
| Nonsense variant predicted to lead to NMD | P/LP variant in the exon of DNA change predicted to lead to NMD | +1 pt |
| Nonsense variant predicted to lead to NMD | B/LB variant in the exon predicted to lead to NMD | -2 pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | P/LP variant resulting in a PTC in the same exon but downstream of VUA | +1 pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | B/LB variant resulting in PTC in the same exon but upstream of the VUA | -2 pt |

NMD = nonsense-mediated decay; PTC = premature termination codon

**Note (verbatim):** The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet "+1 pathogenic variant downstream" on the PVS1 flowchart. If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA. The VUA must be sufficiently rare, meet PM2_Supporting, to apply this point system. If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic without use of PM5 and without use of only PVS1 plus PM2.

**Point thresholds:** stated as "4+", "2+" and "1" point — i.e. inclusive (`>=`).

*Modification type: General recommendation, Strength (Strong, Moderate); Gene-specific, Strength (Supporting)*

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
| **Very Strong** | Not listed as a separate row in the specification for PM6 (the specification lists Strong, Moderate and Supporting). PM6_VeryStrong does appear in the referenced SVI *de novo* Table 2. |
| **Strong** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification type: General recommendation, Gene-specific* |
| **Moderate** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification type: General recommendation, Gene-specific* |
| **Supporting** | Use ClinGen SVI recommendations for *de novo* criteria (see instructions below). *Modification type: General recommendation, Gene-specific* |

See [Appendix D](#appendix-d--svi-recommendation-for-de-novo-criteria-ps2--pm6-version-11). Note in particular the SVI consideration for autosomal recessive conditions, which applies to *IL7R*: "for a *de novo* occurrence in a gene associated with a condition inherited in an autosomal recessive pattern without an additional pathogenic/likely pathogenic variant identified, the strength of evidence should be decreased by one level."

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386) with the additional specification that unaffected individuals contributing to the calculated LOD score **(Attached document: PP1 specifications)** must be heterozygous carriers of one of the variants observed in the affected individuals (i.e. do not count wild-type/wild-type, individuals).

| Strength | Criteria |
|----------|----------|
| **Strong** | Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations. *Modification type: General recommendation* |
| **Moderate** | Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations. *Modification type: General recommendation* |
| **Supporting** | Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations. *Modification type: General recommendation* |

The attached PP1 tables (Oza et al., Tables 4a and 4b) are reproduced in [Appendix E](#appendix-e--pp1-segregation-tables-oza-et-al-tables-4a-and-4b). *IL7R* is autosomal recessive, so **Table 4b** is the operative lookup.

> **Source note (typo preserved):** "(i.e. do not count wild-type/wild-type, individuals)" — stray comma before "individuals".

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable.** Comment: "Does not apply. The gnomAD v2.1.1 missense Z score for IL7R (Z = -1.29) suggests this gene is not constrained for missense variation. Both benign and pathogenic missense variants are present in IL7R."

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

| Strength | Criteria |
|----------|----------|
| **Supporting** | Only applicable to synonymous or intronic variants predicted to impact splicing by SpliceAI with a delta score **greater than or equal to 0.2** (inclusive, `>=`). **Do not apply to missense variants.** *Modification type: General recommendation* |

**Comparator:** inclusive (`>=` 0.2).

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** PP4 applicability and strength is determined by the total points accumulated by a single affected individual according to the table below and the following total point ranges:

| Total points | Outcome |
|---|---|
| <1 point | PP4 not met |
| 1 - <2 points | PP4 |
| 2 - <6 points | PP4_Moderate |
| ≥6 points | PP4_Strong<sup>1</sup> |

**Comparators:** lower bounds inclusive (`>=`), upper bounds strict (`<`); PP4_Strong at `>= 6` (inclusive).

#### Evidence Description (Points)

| Evidence Description | Points |
|---|---|
| Diagnostic criteria met for SCID (Criteria 1 and 3 or Criterion 4 by itself) or Leaky SCID/Omenn syndrome (excluding Criterion 2)<sup>2</sup> | 0.5 |
| SCID gene panel or exome/genome sequencing conducted (only applicable if genetic testing did not provide an alternative genetic explanation for SCID/Leaky SCID/Omenn syndrome phenotype) | 1 |
| Family history of SCID (only applicable if SCID gene panel or exome/genome sequencing was conducted on proband and did not provide an alternative genetic explanation for phenotype) | 0.5 |
| Absent CD127 expression (demonstrated by RT-PCR, Western blot, flow cytometry PMID: 9843216, 11023514, 17827065 | 4.5 |
| Reduced CD127 expression (demonstrated by RT-PCR, or Western blot) as established by the laboratory PMID: 9843216, 11023514, 17827065 | 3 |
| Reduced CD127 expression (demonstrated by flow cytometry) as established by the laboratory AND pathogenic or likely pathogenic variants in IL2RG have been excluded; OR reduced IL-7-induced phosphorylation of STAT5 in patient-derived T-cells as established by the laboratory AND pathogenic or likely pathogenic variants in IL2RG, JAK3, STAT5A, and STAT5B have been excluded PMID: 38587703 | 3 |
| Reduced CD127 expression (demonstrated by flow cytometry) as established by the laboratory AND pathogenic or likely pathogenic variants in IL2RG have **NOT** been excluded; OR reduced IL-7-induced phosphorylation of STAT5 in patient-derived T-cells as established by the laboratory AND pathogenic or likely pathogenic variants in IL2RG, JAK3, STAT5A, and STAT5B have **NOT** been excluded | 1 |
| SCID phenotype corrected by IL7R gene therapy **WITHOUT** CNV testing performed | 4.5 |
| SCID phenotype corrected by IL7R gene therapy **WITH** CNV testing performed | 6 |
| T-B+NK+ lymphocyte subset profile\* (See notes) | 0.25 |

**Footnotes:**

<sup>1</sup> (main specification wording) CNV (Copy number variation) testing is required if PP4_Strong cannot be reached without points from gene therapy in order to certify that the variant in question is causative for the phenotype, and not one CNV event corrected by gene therapy and not previously identified.

<sup>2</sup> The diagnostic criteria should follow the PIDTC 2022 specification, summarized [here].

\***Notes:** 1) If NK cells are not noted or are present, criteria may still be applied if SCID gene panel or exome/genome sequencing has ruled out alternative causes; 2) If maternal T cells are present, the T lymphocyte profile is still considered to be T- (autologous T cells are absent).

> **Source note (typo preserved):** the "Absent CD127 expression" row has an unclosed parenthesis — "(demonstrated by RT-PCR, Western blot, flow cytometry PMID: ..." — in both the main specification and the attached PP4 PDF.

> **Discrepancy between the main specification and `PP4 - IL7R.pdf`:** the attached PDF's footnote 1 reads "CNV (Copy number variation) testing is **required to consider PP4_Strong** in order to certify that the variant in question is the causative for the phenotype, and not one CNV event corrected by gene therapy and not identified previously." The main specification narrows this to "required **if PP4_Strong cannot be reached without points from gene therapy**". The two are not equivalent. The superscript numbering is also swapped between the two documents (PDF: 1 = CNV, 2 = PIDTC on the diagnostic-criteria row; main spec text: 1 = PIDTC, 2 = CNV, while the Strong strength row again uses 1 = CNV). The v2.2 release note "Made updates to subscript text for PP4 criteria" appears to refer to this change; the conflict is not resolved in the distributed package.

| Strength | Criteria |
|---|---|
| **Strong** | A patient score of ≥ 6 points. *Modification type: Disease-specific, Gene-specific* |
| **Moderate** | A patient score of 2-<6 points (see instructions below). *Modification type: Disease-specific, Gene-specific* |
| **Supporting** | A patient score of 1-<2 points (see instructions below). *Modification type: Disease-specific, Gene-specific* |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable.** "This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee." (PubMed: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:** Maximum credible population allele frequency threshold is determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:

- Prevalence: 1:5,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.08 (based on the contribution of *IL7R* variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 7.6%, rounded to 8%)
- Penetrance: 50%

| Strength | Criteria |
|---|---|
| **Stand Alone** | gnomAD popmax filtering allele frequency **>0.00566** (strict greater-than). *Modification type: Gene-specific* |

**Comparator:** strict (`>`). Not inclusive.

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:** gnomAD popmax filtering allele frequency **>0.00126**<sup>1</sup>

Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:

- Prevalence: 1:50,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.08 (based on the contribution of *IL7R* variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 7.6%, rounded to 8%)
- Penetrance: 100%

<sup>1</sup> Consider also bottleneck populations.

| Strength | Criteria |
|---|---|
| **Strong** | gnomAD popmax filtering allele frequency **>0.00126**. Consider also bottleneck populations. *Modification type: Gene-specific* |

**Comparator:** strict (`>`). Not inclusive.

> **Source note:** BA1 uses prevalence 1:5,000 with 50% penetrance, BS1 uses 1:50,000 with 100% penetrance. Both are transcribed as written.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

| Strength | Criteria |
|---|---|
| **Strong** | BS2_Strong: Can be applied at Strong level if observed in at least 3 homozygotes. *Modification type: Strength* |
| **Supporting** | Only to be used when the variant is observed in the homozygous state in a healthy adult. BS2_Supporting: Can be applied at Supporting level if observed in at least 1 homozygote. *Modification type: Strength* |

**Comparators:** "at least 3" and "at least 1" — inclusive (`>=`).

*(BS2_Strong was newly added in v2.2 and BS2_Supporting text was edited, per the release notes.)*

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** **Not Applicable.** Comment: "There is not a well-established functional study which can rule out all damaging effects on protein function."

> Note: the distributed functional-evidence workbook is titled "SCID VCEP PS3_BS3 Functional Evidence (IL7R)", but every approved assay instance in it carries a proposed strength of PS3_Supporting only; no BS3 strength is proposed anywhere in the workbook, consistent with BS3 being Not Applicable.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

| Strength | Criteria |
|---|---|
| **Strong** | Can be applied without additional specifications. *Modification type: None* |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | "Does not apply. IL7R missense variants are a known mechanism of disease." |
| **BP2** | Not Applicable | No comment provided by the VCEP. |
| **BP3** | Not Applicable | "Does not apply." |
| **BP4** | Not Applicable | No comment provided by the VCEP. |
| **BP5** | Not Applicable | No comment provided by the VCEP. |
| **BP6** | Not Applicable | "This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee." (PubMed: 29543229) |
| **BP7** | **Supporting** | Applicable to both synonymous variants and deep intronic variants affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions. The variant should be predicted not to impact splicing by at least two out of three *in silico* tools (freely available tools include GeneSplicer, MaxEntScan, NNSplice, SpliceAI, Splicing Sequences Finder (SSF), and varSEAK). Given the potential for poor conservation of genes related to T cell and B cell development among vertebrates, nucleotide conservation is not required in order to apply BP7. *Modification type: Disease-specific* |

> **Source note:** BP7 says "at least two out of three *in silico* tools" but then lists six freely available tools. Transcribed as written.

---

## Rules for Combining Criteria

Transcribed verbatim from the "Rules for Combining Criteria" section of the v2.2 specification. Parenthetical lists are the specification's own enumerations of which coded criteria count at that strength.

### Pathogenic

| Rule |
|---|
| 1 Very Strong *(PVS1, PS2_Very Strong, PM3_Very Strong)* **AND** ≥ 1 Strong *(PVS1_Strong, PS1, PS2, PS3, PM1_Strong, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong)* |
| 1 Very Strong *(PVS1, PS2_Very Strong, PM3_Very Strong)* **AND** ≥ 2 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate)* |
| 1 Very Strong *(PVS1, PS2_Very Strong, PM3_Very Strong)* **AND** 1 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate)* **AND** 1 Supporting *(PS2_Supporting, PS3_Supporting, PM1_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)* |
| 1 Very Strong *(PVS1, PS2_Very Strong, PM3_Very Strong)* **AND** ≥ 2 Supporting *(PS2_Supporting, PS3_Supporting, PM1_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)* |
| ≥ 2 Strong *(PVS1_Strong, PS1, PS2, PS3, PM1_Strong, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong)* |
| 1 Strong *(PVS1_Strong, PS1, PS2, PS3, PM1_Strong, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong)* **AND** ≥ 3 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate)* |
| 1 Strong **AND** 2 Moderate **AND** ≥ 2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** ≥ 4 Supporting |

### Likely Pathogenic

| Rule |
|---|
| 1 Very Strong *(PVS1, PS2_Very Strong, PM3_Very Strong)* **AND** 1 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate)* |
| 1 Strong *(PVS1_Strong, PS1, PS2, PS3, PM1_Strong, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong)* **AND** 1 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate)* |
| 1 Strong **AND** ≥ 2 Supporting *(PS2_Supporting, PS3_Supporting, PM1_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)* |
| ≥ 3 Moderate *(PVS1_Moderate, PS1_Moderate, PS2_Moderate, PM1, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate)* |
| 2 Moderate **AND** ≥ 2 Supporting |
| 1 Moderate **AND** ≥ 4 Supporting |
| 1 Strong **AND** 2 Moderate |
| 1 Very Strong *(PVS1, PS2_Very Strong, PM3_Very Strong)* **AND** 1 Supporting *(PS2_Supporting, PS3_Supporting, PM1_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4)* |

### Benign

| Rule |
|---|
| ≥ 2 Strong *(BS1, BS2, BS4)* |
| 1 Stand Alone *(BA1)* |

### Likely Benign

| Rule |
|---|
| ≥ 2 Supporting *(BS2_Supporting, BP7)* |
| 1 Strong *(BS1, BS2, BS4)* |

> **Note:** The v2.2 release notes describe the additions as "(A) 1 very strong + 1 supporting = Likely Pathogenic and (B) 1 Strong Benign = Likely Benign", both of which appear above.
>
> **Note:** The Pathogenic list includes a "1 Strong AND 2 Moderate AND ≥ 2 Supporting" rule and the Likely Pathogenic list includes a "1 Strong AND 2 Moderate" rule; the specification lists both as published. No rule is given for Uncertain Significance — by the source's structure, anything not meeting a listed combination is Uncertain Significance, but the specification does not state this explicitly.

---

## Appendices

### Appendix A — PVS1 Decision Flowchart (IL7R-specific)

Transcribed from `PVS1.pdf` (1 page; "PVS1: Specified PVS1 flowchart for IL7R gene"). Gene-specific anchors used throughout: NMD boundary at **c.826 (codon 276) in exon 7**; last exon is **exon 8**; the transmembrane domain **begins at amino acid 240**.

**Nonsense or Frameshift**

| Path | Outcome |
|---|---|
| Predicted to undergo NMD<sup>b</sup> → Exon is present in biologically-relevant transcript(s) | **PVS1** |
| Predicted to undergo NMD<sup>b</sup> → Exon is absent from biologically-relevant transcript(s) | **N/A** |
| Not predicted to undergo NMD<sup>b</sup> (i.e. premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon [c.826 (codon 276) in exon 7]) → Truncated/altered region is critical to protein function – causes truncation of the transmembrane domain (which begins at amino acid 240) or any distal region (i.e. cytoplasmic domain) | **PVS1_Strong** |
| Not predicted to undergo NMD → Role of region in protein function is unknown → LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) | **N/A** |
| Not predicted to undergo NMD → Role unknown → LoF not frequent and exon present → Variant removes >10% of protein → 1+ pathogenic variant present downstream | **PVS1_Strong** |
| Not predicted to undergo NMD → Role unknown → LoF not frequent and exon present → Variant removes >10% of protein → No known downstream pathogenic variants | **PVS1_Moderate** |
| Not predicted to undergo NMD → Role unknown → LoF not frequent and exon present → Variant removes <10% of protein | **PVS1_Moderate** |

**GT--AG 1,2 splice sites<sup>a</sup>**

| Path | Outcome |
|---|---|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD<sup>b</sup> → Exon is present in biologically-relevant transcript(s) | **PVS1** |
| …→ Exon is absent from biologically-relevant transcript(s) | **N/A** |
| Exon skipping or cryptic splice site disrupts reading frame and is **NOT** predicted to undergo NMD<sup>b</sup> (i.e. premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon [c.826 (codon 276) in exon 7]) → Truncated/altered region is critical to protein function (transmembrane domain from aa 240 or any distal region) | **PVS1_Strong** |
| …→ Role of region unknown → LoF frequent in general population and/or exon absent from biologically-relevant transcript(s) | **N/A** |
| …→ Role unknown → LoF not frequent and exon present → removes >10% of protein → 1+ pathogenic variant present downstream | **PVS1_Strong** |
| …→ Role unknown → LoF not frequent and exon present → removes >10% of protein → No known downstream pathogenic variants | **PVS1_Moderate** |
| …→ Role unknown → LoF not frequent and exon present → removes <10% of protein | **PVS1_Moderate** |
| Exon skipping or use of a cryptic splice site preserves reading frame → Truncated/altered region critical to protein function (transmembrane domain from aa 240 or any distal region) | **PVS1_Strong** |
| Exon skipping/cryptic splice site preserves reading frame → Role unknown → LoF frequent and/or exon absent | **N/A** |
| …→ Role unknown → LoF not frequent and exon present → removes >10% of protein → 1+ pathogenic variant present within deleted region | **PVS1_Strong** |
| …→ Role unknown → LoF not frequent and exon present → removes >10% of protein → No known pathogenic variants within deleted region | **PVS1_Moderate** |
| …→ Role unknown → LoF not frequent and exon present → removes <10% of protein | **PVS1_Moderate** |

**Deletion (single exon to full gene)**

| Path | Outcome |
|---|---|
| Full gene deletion | **PVS1**<sup>d</sup> |
| Single to multi exon deletion – disrupts reading frame and is predicted to undergo NMD<sup>b</sup> → Exon present in biologically-relevant transcript(s) | **PVS1** |
| …→ Exon absent from biologically-relevant transcript(s) | **N/A** |
| Single to multi exon deletion – disrupts reading frame and is **NOT** predicted to undergo NMD<sup>b</sup> (i.e. premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon [c.826 (codon 276) in exon 7]) → Truncated/altered region critical to protein function (transmembrane domain from aa 240 or any distal region) | **PVS1_Strong** |
| …→ Role unknown → LoF frequent and/or exon absent | **N/A** |
| …→ Role unknown → LoF not frequent and exon present → removes >10% of protein → 1+ pathogenic variant present within deleted region | **PVS1_Strong** |
| …→ Role unknown → LoF not frequent and exon present → removes >10% of protein → No known pathogenic variants within deleted region | **PVS1_Moderate** |
| …→ Role unknown → LoF not frequent and exon present → removes <10% of protein | **PVS1_Moderate** |
| Single to multi exon deletion – preserves reading frame → Truncated/altered region critical to protein function (transmembrane domain from aa 240 or any distal region) | **PVS1_Strong** |

**Duplication (≥1 exon in size and must be completely contained within gene)**

| Path | Outcome |
|---|---|
| Proven in tandem → Reading frame disrupted and NMD predicted to occur | **PVS1** |
| Presumed in tandem → No or unknown impact on reading frame and NMD | **N/A** |
| Presumed in tandem → Reading frame presumed disrupted and NMD predicted to occur | **PVS1_Strong** |
| Proven not in tandem | **N/A** |

**Initiation Codon**

| Path | Outcome |
|---|---|
| No known alternative start codon in other transcripts → ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon | **PVS1_Moderate** |
| No known alternative start codon in other transcripts → No pathogenic variant(s) upstream of closest potential in-frame start codon | **PVS1_Supp** |
| Different functional transcript uses alternative start codon | **N/A** |

> **Gap in the source:** the flowchart carries footnote markers **a**, **b** and **d**, but the distributed one-page PDF contains **no footnote legend**; the definitions of a, b and d are not present in any distributed file. Not specified by this VCEP in the distributed package.

---

### Appendix B — PM3 Point System

See the [PM3 section](#pm3---in-trans-with-pathogenic) above for Table 1 and Table 2, and [Appendix C](#appendix-c--svi-recommendation-for-in-trans-criterion-pm3-version-10) for the full source text.

---

### Appendix C — SVI Recommendation for in trans Criterion (PM3) - Version 1.0

Transcribed from `PM3 Criterion.pdf`. Header: "ClinGen Sequence Variant Interpretation Recommendation for in *trans* Criterion (PM3) - Version 1.0; Working Group Page: https://clinicalgenome.org/working-groups/sequence-variant-interpretation/; **Date Approved: May 2, 2019; Table 1 updated October 17, 2025**".

**Body text (verbatim):**

> The Sequence Variant Interpretation (SVI) Working Group proposes a point-based system to determine the strength of in *trans* observations (ACMG/AMP criterion PM3) based upon variant phasing and classification of the variant occurring on the other allele. Additionally, SVI recommends a revision to the criterion definition to indicate this evidence should only be applied if the individual is affected:
>
> SVI revision to PM3: For recessive disorders, detected in *trans* with a pathogenic ***or likely pathogenic*** variant *in an affected patient*
>
> To determine the appropriate strength level to apply for in *trans* occurrence(s), each proband is awarded a point value based upon phasing of the two variants in question (confirmed in *trans* versus unknown) and classification of the variant on the other allele (Table 1). The combined point value of all proband occurrences is then summed and compared to Table 2 to determine the applicable evidence strength level. For example, if assessing *PAH* variant NM_000277.3:c.1208C>T (p.Ala403Val) and the variant was confirmed in *trans* with Likely pathogenic variant c.1301C>A (p.Ala434Asp) in one proband (1.0 points; Table 1) and confirmed in *trans* with Pathogenic variant c.331C>T (p.Arg111Ter) in another proband (1.0 points, Table 1), then PM3 at the Strong strength level (PM3_Strong) is applicable (2.0 points total; Table 2).

**Table 1 and Table 2:** reproduced in the [PM3 section](#pm3---in-trans-with-pathogenic) above.

**Considerations (verbatim):**

> - **Allele Frequency** - Application of PM3 is contingent on the allele frequency of the variant being assessed and the variant presumably on the other allele both being sufficiently rare (meets PM2 threshold). This contingency is to avoid incorrect application of PM3 to high frequency variants that are likely to occur in *trans* with P/LP variants based on frequency.
> - **Phasing** - If the phase cannot be determined, it is recommended that at least two different LP/P variants (depending on classifications) are needed to equal the weight of one LP/P co-occurrence confirmed in *trans*.
>   - In confirmation of phasing, if only one parent is tested and found to carry one allele, variants can be counted as in *trans*. For example, assessing PAH variant c.601C>T (p.His201Tyr) and variant was identified in PKU proband who also carries known pathogenic variant c.734T>C (p.Val245Ala). Only the mother is available for testing and the mother only carries c.734T>C (p.Val245Ala) variant, then variants can be considered in *trans*.
> - **Classification** – Probands should be weighted less when the variant on the other allele is of uncertain significance and rare (meets PM2); however, weight may vary by gene size as larger genes are more likely to have a second variant by chance (default 0.25 points). If the variant on the other allele is classified as P or LP, weighting depends on phasing (see *Phasing* above), with P/LP being weighted equally if confirmed in trans and different point values per proband if phasing is unknown (0.5 points and 0.25 points, respectively). To avoid circularity, in all instances (phasing confirmed or unknown), the classification of the variant on the other allele should not use evidence from the variant being interrogated.
> - **Homozygous occurrences** – For homozygous occurrences, the default weight is dropped to 0.5 points, as a rare homozygous occurrence may be due to consanguinity. A recommended max of 1.0 points of all homozygous cases is suggested to prevent overclassification of homozygous occurrences in the absence of additional data.

> **Internal inconsistency inside `PM3 Criterion.pdf` itself:** the updated Table 1 marks both homozygous-occurrence rows "*(no max)*", while the unrevised "Homozygous occurrences" bullet under Considerations still states "A recommended max of 1.0 points of all homozygous cases is suggested". The October 2025 Table 1 update was evidently not carried through to the Considerations text. Both are transcribed; not reconciled here.

---

### Appendix D — SVI Recommendation for de novo Criteria (PS2 & PM6) - Version 1.1

Transcribed from `PS2_PM6.pdf`. Header: "Date Approved: March 18, 2018, updated May 5, 2021. Changes from v1: Clarified that confirmed/assumed is with regards to parental relationships and not de novo status."

Three parameters determine strength: confirmed vs. assumed parental relationships status; phenotypic consistency; number of *de novo* observations.

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

Thresholds are stated as bare point values; the source's worked examples apply the Strong level at exactly 2 points, i.e. inclusive (`>=`).

**Worked examples and additional considerations (verbatim):**

> For all uses of *de novo* criteria, the phenotype in the patient must be consistent with the gene/disease association as recommended in the ACMG/AMP guidelines. When the patient's phenotype is consistent with the gene/disease association but not highly specific, we recommend decreasing the points awarded. For example:
>
> - A patient with early infantile epileptic encephalopathy and a *de novo SIK1* variant with confirmed parental relationships is awarded 1 point … If this patient is the only *de novo* occurrence for the variant, then a Moderate strength level (PS2_Moderate) is applied.
>   - If two additional unrelated patients with early infantile epileptic encephalopathy and a *de novo SIK1* variant with confirmed parental relationships are identified, then the combined point value is 3 … a Strong strength level (PS2) is applied as the points reach the Strong threshold (2 points) but not the VeryStrong threshold (4 points).
> - A patient with nonsyndromic intellectual disability and a *de novo ASH1L* variant is awarded 0.5 points … then a Supporting strength level (PS2_Supporting) is applied.
>   - If a second patient … is identified, then the combined point value is 1 … a Moderate strength level (PS2_Moderate) is applied.
> - A patient with developmental delay but no other features of Cornelia de Lange syndrome and a *de novo NIPBL* variant with unconfirmed parental relationships is awarded zero points as this phenotype is not consistent with the gene/disease association. If this patient was the only *de novo* occurrence for the variant, then no *de novo* criteria are applied.
>
> Additional considerations for applying *de novo* criteria based on inheritance:
>
> - **Conditions with X-linked inheritance:** if the variant occurs *de novo* in an unaffected carrier mother, and family history is consistent - i.e., she has no affected brothers/other male relatives apart from her affected son(s) – *de novo* criteria may be applied despite the fact that she is unaffected.
> - **Autosomal recessive conditions:** for a *de novo* occurrence in a gene associated with a condition inherited in an autosomal recessive pattern without an additional pathogenic/likely pathogenic variant identified, the strength of evidence should be decreased by one level.
> - **Mosaicism:** for cases with apparent germline mosaicism (multiple affected siblings with both parents negative for the variant), parental relationships must be confirmed in order for *de novo* criteria to apply.

Note: the first bullet of the *IL7R* PS2/PM6 VCEP text maps the SVI phenotypic-consistency tiers onto SCID PP4 strengths (highly specific = PP4_Moderate or above; consistent but not highly specific = PP4 met; consistent but not highly specific with high genetic heterogeneity = asserted SCID phenotype not meeting PP4).

---

### Appendix E — PP1 Segregation Tables (Oza et al., Tables 4a and 4b)

Transcribed from `PP1.pdf` (Oza et al., *Hum Mutat*, author manuscript pages 35–36; PMID: 30311386).

**Table 4a: Recommendations for PP1 (segregation evidence) — General Recommendations**

| | Supporting | Moderate | Strong |
|---|---|---|---|
| Likelihood | 4:1 | 16:1 | 32:1 |
| LOD Score | 0.6 | 1.2 | 1.5 |
| Autosomal dominant threshold | 2 affected segregations | 4 affected segregations | 5 affected segregations |
| Autosomal recessive threshold | See Table 4b | See Table 4b | See Table 4b |

**Table 4b: Recommendations for autosomal recessive segregation evidence (PP1)** — General Recommendations (Phenocopy not an issue). **This is the operative table for *IL7R*.** This is a lookup table: rows = affected segregations (0–10), columns = unaffected recessive segregations (0–10); each cell is the LOD score for that combination. Compare the looked-up LOD against the Table 4a LOD thresholds (0.6 / 1.2 / 1.5).

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

**Table 4b legend (verbatim):**

> Affected segregations are counted in rows and unaffected segregations in columns. Affected segregations are affected family members in whom biallelic compound heterozygous or homozygous variants segregates. Unaffected segregations are defined as unaffected family members, typically siblings, who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants identified in the proband, or a heterozygous carrier for a single variant. Unaffected, carrier parents DO NOT count as unaffected segregations. There may be scenarios where individuals other than siblings could be counted as segregations, such as in families where one parent is affected with the autosomal recessive disorder, in large families with multiple branches, or in consanguineous families.
>
> Each cell shows the LOD score of each combination of affected and unaffected segregations. LOD scores were calculated using a simplified LOD score formula, as described in Strande et al., 2017.

**VCEP overlay:** unaffected individuals contributing to the calculated LOD score must be heterozygous carriers of one of the variants observed in the affected individuals (i.e. do not count wild-type/wild-type individuals).

> **Note:** the Oza Table 4b legend permits unaffected segregations to be "either wild-type for both variants identified in the proband, or a heterozygous carrier for a single variant", whereas the *IL7R* VCEP overlay excludes wild-type/wild-type individuals. The VCEP overlay is the operative rule for *IL7R*.

---

### Appendix F — PS3/BS3 Functional Evidence Workbook (IL7R)

Transcribed from `SCID VCEP PS3_BS3 Functional Evidence (IL7R).xlsx` (2 worksheets). This workbook is an assay-instance dossier, not a variant-level lookup — it contains four assay instances and no per-variant classification table.

**Sheet 1: "General Class of Assay Summary"** (3 rows × 3 columns)

| Gene | General Class of Assay | PMIDs |
|---|---|---|
| IL7R | IL-7-induced Jak-3/STAT5 phosphorylation assay+ | PMID: 11023514 |
| | IL-7 binding assay | PMID: 11023514, PMID: 9843216 |
| | IL-7-induced STAT5 DNA binding/transcription assay | PMID: 9843216 |

> **Source note:** "IL-7-induced Jak-3/STAT5 phosphorylation assay+" carries a trailing "+" with no corresponding footnote anywhere in the workbook.
>
> **Inconsistency:** this summary sheet lists PMID 11023514 among the "IL-7 binding assay" references, but the instance-detail sheet attributes the IL-7 binding assay only to PMID 9843216 (Puel 1998); PMID 11023514 (Roifman 2000) is recorded there as the Jak-3 phosphorylation assay only. The main specification's approved-assay list follows the instance-detail sheet.

**Sheet 2: "IL7R Assay Instance Details"** (25 rows × 5 columns; the sheet is transposed — attributes in rows, one column per assay instance)

| Attribute | Instance 1 | Instance 2 | Instance 3 | Instance 4 |
|---|---|---|---|---|
| PMID | 11023514 | 9843216 | 9843216 | 9843216 |
| Gene | IL7R | IL7R | IL7R | IL7R |
| DOI / link | 10.1182/blood.V96.8.2803 | 10.1038/3877 | 10.1038/3877 | 10.1038/3877 |
| Author | Roifman…Sharfe | Puel…Leonard | Puel…Leonard | Puel…Leonard |
| Year | 2000 | 1998 | 1998 | 1998 |
| General Class of Assay | IL-7-induced Jak-3 phosphorylation assay | IL-7 binding assay | IL-7-induced Stat5 DNA-binding activity | IL-7-induced Stat5 transcription activity |
| Assay (General Description) | COS-7 cells were transfected with expression vectors encoding γc, Jak3, and either wild type or variant IL-7Rα, incubated in the presence or absence of IL-7 for 10 minutes, lysed, and immunoprecipitated with anti-Jak3 antibody and subsequently blotted with either anti-phosphotyrosine or anti-Jak3 antibodies | 293T cells were transfected with expression vectors encoding γc and either wild type or variant IL-7Rα and incubated with 125I-labelled IL-7 followed by increasing amounts of unlabelled ligand to analyze displacement kinetics | Stat5 DNA binding was evaluated by electrophoretic mobility shift assay in 293T cells transfected with expression vectors encoding γc, Jak3, Stat5a, Stat5b and either wild type or variant IL-7Rα and stimulated with varying concentrations of IL-7 for 30 seconds | Transcription from a Stat5-responsive reporter construct was evaluated by luciferase activity in 293T cells transfected with expression vectors encoding γc, Jak3, Stat5a, Stat5b, β-casein-luciferase reporter, and either wild type or variant IL-7Rα and stimulated with varying concentrations of IL-7 for 30 seconds |
| Material used | COS-7 cells transfected with wild type and variant IL7R cDNA constructs | 293T cells transfected with wild type and variant IL7R and wild type γc cDNA constructs | 293T cells transfected with wild type and variant IL7R and wild type γc, Jak3, Stat5a, and Stat5b cDNA constructs | 293T cells transfected with wild type and variant IL7R and wild type γc, Jak3, Stat5a, Stat5b, and β-casein-luciferase reporter cDNA constructs |
| Readout type | Semi-quantitative | Quantitative | Semi-quantitative | Quantitative |
| Readout description | Presence/intensity of band corresponding to Jak3 tyrosine phosphorylation | Ratio of specific binding to concentration of free radioligand at varying ligand concentrations | Presence/intensity of band corresponding to DNA-bound Stat5 | Relative luciferase activity (corresponding to Stat5-induced transcription) |
| Biological replicates | Not reported | Not reported | Not reported | Not reported |
| Technical replicates | Not reported | Not reported | Not reported | Not reported |
| Basic positive control | COS-7 cells expressing wild type IL-7Rα | 293T cells expressing wild type IL-7Rα | 293T cells expressing wild type IL-7Rα | 293T cells expressing wild type IL-7Rα |
| Basic negative control | Untransfected COS-7 cells | 293T cells expressing empty vector | 293T cells expressing empty vector | 293T cells expressing empty vector |
| Validation controls P/LP (#) | 0 | 0 | 0 | 0 |
| Validation controls B/LB (#) | 0 | 0 | 0 | 0 |
| Statistical analysis | Not reported | Not reported | Not reported | Not reported |
| Threshold for normal readout | Wild type-like level of phosphorylated Jak3 | Wild type-like levels of IL7 binding | Wild type-like levels of Stat5 DNA binding | Wild type-like levels of Stat5-induced transcription |
| Threshold for abnormal readout | Reduced level of phosphorylated Jak3 | Reduced IL7 binding | Reduced Stat5 DNA binding | Reduced Stat5-induced transcription |
| **Approved assay (y/n)** | **y** | **y** | **y** | **y** |
| **Proposed strength** | **PS3_Supporting** | **PS3_Supporting** | **PS3_Supporting** | **PS3_Supporting** |
| Variant(s) Tested | *(blank)* | c.197T>C (p.Ile66Thr) and c.412G>A (p.Val138Ile) (in cis) | c.197T>C (p.Ile66Thr) and c.412G>A (p.Val138Ile) (in cis) | c.197T>C (p.Ile66Thr) and c.412G>A (p.Val138Ile) (in cis) |
| Notes | *(blank)* | The variants tested in this assay were observed in homozygosity in the proband and tested in cis in the cDNA constructs, preventing analysis of the independent effects of each variant on protein function. Additionally, both tested variants were asserted by the authors to be benign ("polymorphisms") on the basis of allele frequency, which is supported by gnomAD allele frequencies. | *(same note as Instance 2)* | *(same note as Instance 2)* |

> **Notes on the workbook:** (1) All four instances have zero P/LP and zero B/LB validation controls and no reported replicates or statistical analysis, which is consistent with the maximum proposed strength being PS3_Supporting. (2) The workbook lists four instances; the main specification's approved-assay list collapses instances 3 and 4 into a single entry, "IL-7-induced STAT5 DNA binding/transcriptional induction". (3) No BS3 strength is proposed for any instance despite the workbook title.

---

### Appendix G — PM3 Minor Amendments 12.12.2025

Transcribed in full from `PM3 Minor Amendments 12.12.2025.docx` ("PM3: svi recommendations: October 2025 Group Responses to Minor Updates"). Formatting is the source's; SVI comments and SCID VCEP responses are interleaved.

**Footnotes proposed for the table:**

> \* Multiple probands from separate nuclear families that are later found to have identity-by-descent should only be counted once.
>
> \*\* When consanguinity is not known or reported: if family IS NOT from a bottlenecked population (as defined by gnomAD), assume non-consanguinity; otherwise, assume consanguinity.  If genetic ancestry of the family cannot be determined, assume consanguinity.

**SVI Comments (verbatim, with SCID VCEP responses):**

> **Prefer N/A to repeating the 1.0 and 0.5**
>
> The SCID VCEP deliberated this point.  Our geneticists pointed out that apparent homozygous variants could result from hemizygosity, which may be undetected if the parents are not sequenced (i.e., "Phase unknown").  Because of the likelihood that authors may not bother to sequence the parents in homozygous situations, especially in older publications, the VCEP experts preferred to leave the numbers in place.
>
> **Update "max point 0.5 per family" to "max point 0.5" as in original specs**
>
> Please replace "max point 0.5 per family" from the Homozygous Consanguineous and indicate "no max". Rationale:
>
> - "per proband" is a rule for the whole table in general (per the table title)
> - Multiple cases per family will inherently be counted as PP1 instead of multiple PM3s
>
> - The SCID VCEP agreed and made the changes to the table.  To minimize confusion for biocurators and experts as much as possible between proper application of PM3 vs. PP1 (which we have definitely observed, even in sustained curations), we changed "Proband" to "Proband-Family".
>
> **What to do if you don't know about consanguinity**
>
> The VCEP decided to use gnomAD definitions to specify assumption of non-consanguinity for families from non-bottlenecked populations and assumption of consanguinity otherwise.  A footnote was added to the Table.
>
> If the VCEP wishes, they can provide an asterisk footnote that supports the notion that "multiple probands from separate nuclear families that are later found to have identity-by-descent should only be counted once."
>
> We added this footnote to the Table.

**Revised Table included in the amendment document (verbatim):**

| Classification/Zygosity of other variant | Points per Proband-Family\* — Confirmed in trans | Points per Proband-Family\* — Phase unknown |
|---|---|---|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence — Non-consanguineous\*\* *(no max)* | 1.0 | 1.0 |
| Homozygous occurrence — Consanguineous\*\* *(no max)* | 0.5 | 0.5 |
| Uncertain significance variant *(max point 0.5)* | 0.25 | 0 |

#### Is the amendment reflected in the spec's own tables?

**Yes.** The amended table in `PM3 Minor Amendments 12.12.2025.docx` is **identical** to Table 1 as published in the distributed `PM3 Criterion.pdf` (whose header reads "Table 1 updated October 17, 2025"): both use the "Points per Proband-Family\*" column header, both mark the two homozygous rows "(no max)", both keep "(max point 0.5)" on the VUS row, and both carry the two footnotes. Every change requested by SVI and accepted by the VCEP is present in the operative table. **This is not an erratum contradicting the tables.**

Two residual caveats:

1. The amendment's editorial trail is internally muddled — the heading says 'Update "max point 0.5 per family" to "max point 0.5" as in original specs' while the body immediately below asks to 'replace "max point 0.5 per family" from the Homozygous Consanguineous and indicate "no max"'. The implemented outcome is "no max" on both homozygous rows and "max point 0.5" on the VUS row. Transcribed as written.
2. The one place the amendment did **not** propagate is the **Considerations** prose in `PM3 Criterion.pdf`, which still says "A recommended max of 1.0 points of all homozygous cases is suggested" — contradicting the "(no max)" in the updated Table 1. See [Appendix C](#appendix-c--svi-recommendation-for-in-trans-criterion-pm3-version-10).

The main *IL7R* specification body does not restate the PM3 point table; it delegates to the attached PM3 criterion document, so there is no third copy that could disagree.

---

## Criteria Not Specified by This VCEP

The following are explicitly **Not Applicable** per the specification: PS4, PP2, PP5, BS3, BP1, BP2, BP3, BP4, BP5, BP6.

The following are **not specified** (as distinct from not applicable):

- **PM1** — strength rows contain only a caveat; no hot spot or domain is defined anywhere in the package.
- **PS3_Moderate** — no Moderate row is published.
- **PVS1_Supporting** — no strength-table row; appears only as one flowchart terminus (PVS1_Supp).
- **PM6_VeryStrong** — no strength-table row; appears in the referenced SVI Table 2.
- **PVS1 flowchart footnotes a, b, d** — markers present, legend absent from the distributed package.
- **Uncertain Significance** — no explicit rule in the Rules for Combining Criteria.

---

## Version History

| Version | Released | Notes |
|---|---|---|
| 2.2 | 5/15/2026 | Edited Rules for Combining Criteria to reflect standard combinations plus (A) 1 very strong + 1 supporting = Likely Pathogenic and (B) 1 Strong Benign = Likely Benign. Rules for Combining Criteria refreshed and saved. Uploaded two files to address minor PM3 changes: "PM3 Criterion: October 2025 Version, Minor Updates" and "PM3: svi recommendations: October 2025 Group Responses to Minor Updates". Uploaded IL7R corrections which includes PM1 and PS3 codes: made edits to PS3 text; made updates to subscript text for PP4 criteria; added BS2_Strong strength; edited text for BS2_Supporting. |

Earlier version history is not distributed with the v2.2 package.

---

*This document was compiled from the ClinGen VCEP specification and its distributed supplementary files. Content that the VCEP delegates to external guidance without reproducing it is marked as such rather than filled in. For the most current version, please refer to the ClinGen website.*
