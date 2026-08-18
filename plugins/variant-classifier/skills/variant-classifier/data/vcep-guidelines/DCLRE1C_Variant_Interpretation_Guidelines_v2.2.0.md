# ClinGen Severe Combined Immunodeficiency Disease VCEP Variant Interpretation Guidelines for DCLRE1C

**Version:** 2.2
**Released:** 6/1/2026
**Affiliation:** Severe Combined Immunodeficiency Disease VCEP
**Source basis:** Richards et al., 2015 - Combining rules
**DOI:** 10.5281/zenodo.21434447
**Registry ID:** GN116

**Release Notes (verbatim from the specification):**
- Edited Rules for Combining Criteria to reflect standard combinations plus (A) 1 very strong + 1 supporting = Likely Pathogenic and (B) 1 Strong Benign = Likely Benign.
- Refreshed and saved Rules for Combining Criteria.
- Uploaded two files to address minor PM3 changes:
  1. "PM3 Criterion: October 2025 Version, Minor Updates"
  2. "PM3: svi recommendations: October 2025 Group Responses to Minor Updates"
- Made changes to PP4 criteria.
- Uploaded DCLRE1C corrections which includes PS3 codes edits.
- Removed request for update of caveat on PM1 criteria. This was made in error and should not have been added.
- BS2 criteria was changed for DCLRE1C similar to ADA which enumerates the homozygotes needed to reach supporting (n=1) and strong (n=3).
- Uploaded DCLREIC Corrections 1.6.26 file with changes listed above.

> Source typo flagged: the last release note reads "DCLREIC Corrections 1.6.26" (gene symbol misspelled as DCLREIC); the distributed file is named "DCLRE1C Corrections 1.6.26.docx". Transcribed verbatim.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | DCLRE1C (HGNC:17642) |
| **HGNC Name** | DNA cross-link repair 1C |
| **Transcript** | NM_001033855.3 |
| **Disease** | severe combined immunodeficiency due to DCLRE1C deficiency (MONDO:0011225) |
| **Inheritance** | Autosomal recessive inheritance |

**Keywords (as listed by the VCEP):** human biology genomics variant variant classification clingen disease standards DCLRE1C NM_001033855.3 Autosomal recessive inheritance severe combined immunodeficiency due to DCLRE1C deficiency

**Rights Holder:** The Clinical Genome Resource (ClinGen)

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
2. [Benign Criteria](#benign-criteria)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)
5. [Source File Inventory](#source-file-inventory)
6. [Version History](#version-history)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:** See attached PVS1 flowchart (transcribed in [Appendix A](#appendix-a---dclre1c-pvs1-flowchart-file-pvs1pdf)).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)).<br>*Modification Type: General recommendation, Gene-specific* |
| **Strong** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification:<br>• For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 14, or variants in the last 50 nucleotides of the penultimate exon after c.1106, codon 369, in exon 13), at least one pathogenic variant **must be** present downstream in order to apply PVS1_Strong.<br>*Note: Exons 1-3 and exons 1-4 have been reported as a hot spot for deletion variants as a result of homologous recombination of the wild-type DCLRE1C gene with a DCLRE1C pseudogene (PMID: 19953608).*<br>*Modification Type: General recommendation, Gene-specific* |
| **Moderate** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification:<br>• For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 14, or variants in the last 50 nucleotides of the penultimate exon after c.1106, codon 369, in exon 13), when at least one pathogenic variant is **not** present downstream downgrade to PVS1_Moderate.<br>*Note: Exons 1-3 and exons 1-4 have been reported as a hot spot for deletion variants as a result of homologous recombination of the wild-type DCLRE1C gene with a DCLRE1C pseudogene (PMID: 19953608).*<br>*Modification Type: General recommendation* |
| **Supporting** | Not listed as a separate strength row in the specification. PVS1_Supp does appear as an outcome within the attached PVS1 flowchart (Initiation Codon branch, no pathogenic variant upstream of closest potential in-frame start codon). See [Appendix A](#appendix-a---dclre1c-pvs1-flowchart-file-pvs1pdf). |

> Note on the >10% threshold: the specification writes "removing >10% of protein" (strict greater-than); the flowchart writes "Variant removes >10% of protein" versus "Variant removes <10% of protein", leaving exactly 10% unassigned in both documents. Transcribed as written.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T.<br>Applicable if the previously established variant is classified as **pathogenic** by SCID VCEP specifications for *DCLRE1C*.<br>*Modification Type: Gene-specific* |
| **Moderate** | It can also be applied for splice variants at the same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tool SpliceAI). - Example: c.105+1G>C is known to be likely pathogenic, can use PS1 for c.105+1G>T<br>Applicable if the previously established variant is classified as **likely pathogenic** by SCID VCEP specifications for *DCLRE1C*.<br>*Modification Type: Gene-specific, Strength* |

Comparator note: SpliceAI impact must be "equal to or greater than" the known pathogenic variant — inclusive.

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

The referenced SVI *de novo* recommendation (PS2/PM6 v1.1) is distributed with this specification and transcribed in full in [Appendix B](#appendix-b---svi-recommendation-for-de-novo-criteria-ps2--pm6-version-11-file-ps2_pm6pdf). It contains the point matrix (2 / 1 / 0.5 / 0.25 per proband) and the 0.5 / 1 / 2 / 4 strength ladder.

> The VCEP's own text does not restate the SVI point values; it maps the SVI phenotypic-consistency tiers onto its PP4 criterion (above) and adds the "reduce points per proband by half if the phase is unconfirmed" instruction.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | PS3 may potentially be applied at the default strength level of Strong for evidence from an animal model expressing the variant of interest and recapitulating the DCLRE1C-SCID phenotype. Animal models will be reviewed on a case-by-case basis by the VCEP to determine the appropriate strength level.<br>*Modification Type: Gene-specific* |
| **Moderate** | The strength of evidence from cellular models/*in vitro* studies is dependent upon abnormal results in *in vitro* DNA repair activity and V(D)J recombination assays:<br>• **PS3_Moderate:** Abnormal result in **both** an *in vitro* DNA repair activity assay AND an *in vitro* V(D)J recombination assay (defined as <25% of wild-type activity for both assays).<br>*Modification Type: Gene-specific* |
| **Supporting** | The strength of evidence from cellular models/*in vitro* studies is dependent upon abnormal results in *in vitro* DNA repair activity and V(D)J recombination assays:<br>• **PS3_Supporting:** Abnormal result in an *in vitro* V(D)J recombination assay (same threshold, <25% of wild-type activity).<br>*Modification Type: Gene-specific, Strength* |

**Threshold comparator:** abnormal is defined as **<25%** of wild-type activity — strict less-than.

**Additional requirement (from the DCLRE1C Corrections 1.6.26 file, stated under both Moderate and Supporting):** At least one previously observed proband with the DCLRE1C variant meeting PP4 is required to apply PS3 at any strength on the basis of a cellular model/in vitro study.

> This proband requirement appears in the corrections document but is **not** present in the PS3 rows of the v2.2 specification's own criteria table. See [Changelog / Errata](#appendix-e---erratum-cross-check).

#### Approved Assay Instances

**DNA repair activity assay**
- Felgentreff et al., 2015 (PMID: 25917813)

**V(D)J recombination assay**
- Pannicke et al., 2004 (PMID: 15071507)
- Ege et al., 2005 (PMID: 15731174)
- Felgentreff et al., 2015 (PMID: 25917813)
- Volk et al., 2015 (PMID: 26476407)

Full assay-instance evidence table: see [Appendix D](#appendix-d---scid-vcep-ps3bs3-functional-evidence-dclre1c-file-scid-vcep-ps3_bs3-functional-evidence-dclre1cxlsx).

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** **Not Applicable.** (No further comment given by the VCEP.)

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** **Not Applicable.**

**Comments:** Does not apply. No known missense variation hot spots in the DCLRE1C gene have been described. See PVS1 for the note about a known hotspot for DCLRE1C deletion variants. Note: Exons 1-3 and exons 1-4 have been reported as a hot spot for deletion variants as a result of homologous recombination of the wild-type DCLRE1C gene with a DCLRE1C pseudogene (PMID: 19953608).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | gnomAD popmax filtering allele frequency **<0.00003266** (strict less-than).<br>• An additional requirement is that **no homozygotes** have been observed in gnomAD.<br>*Modification Type: Gene-specific* |

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Use ClinGen SVI adapted recommendations for *in trans* criterion (see PM3 criterion attached below) with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for *DCLRE1C*.

**Caveat:** All variants should be sufficiently rare (meet PM2 specification). The applicability of PM3 to suspected founder variants with allele frequencies exceeding the PM2 threshold will be evaluated on a case-by-case basis by the VCEP.

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI adapted recommendations for *in trans* criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for *DCLRE1C*. *Modification Type: General recommendation, Strength* |
| **Strong** | (same text as Very Strong) *Modification Type: General recommendation, Strength* |
| **Moderate** | (same text as Very Strong) *Modification Type: General recommendation, Strength* |
| **Supporting** | (same text as Very Strong) *Modification Type: General recommendation, Strength* |

The attached SVI PM3 recommendation (v1.0, Table 1 updated October 17, 2025) is transcribed in full in [Appendix C](#appendix-c---svi-recommendation-for-in-trans-criterion-pm3-version-10-file-pm3pdf), including the per-proband point table and the strength ladder (0.5 / 1.0 / 2.0 / 4.0).

The VCEP's deliberation over the October 2025 PM3 amendments is transcribed in [Appendix C2](#appendix-c2---pm3-minor-amendments-file-pm3-minor-amendmentsdocx).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | When applied to deletion variants, the deleted region must contain a known **pathogenic** or **likely pathogenic** variant that is not predicted/observed to alter splicing.<br>*Modification Type: Gene-specific* |
| **Supporting** | When applied to deletion variants, the deleted region must contain a known **VUS** variant that is not predicted/observed to alter splicing.<br>*Modification Type: Gene-specific, Strength* |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications (as given in the VCEP Specifications cell):**

For nonsense variants:

**PM5_Strong**
- PM5 may be applied at a Strong level of evidence for any nonsense variant with 4+ points from informative variants (see below point table). PM5_Strong should be downgraded to PM5_Moderate if PVS1 is applied at any strength.

**PM5_Moderate**
- PM5 may also be applied at a Moderate level of evidence for any nonsense variant with 2+ points from informative variants (see below point table). PM5_Moderate may not be combined with PVS1_VeryStrong (should be downgraded to PM5_Supporting if PVS1_VeryStrong is applied).

**PM5_Supporting**
- Also applicable to a nonsense variant with 1 point from an informative variant (see point table). Informative variants must also be classified by these rule specifications.

#### PM5 Point Table (Type of variant under assessment (VUA); Informative variant; Score)

| Type of variant under assessment (VUA) | Informative variant | Score |
|---|---|---|
| Nonsense variant predicted to lead to NMD | P/LP variant in the exon of DNA change predicted to lead to NMD | +1 pt |
| Nonsense variant predicted to lead to NMD | B/LB variant in the exon predicted to lead to NMD | -2 pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | P/LP variant resulting in a PTC in the same exon but downstream of VUA | +1 pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | B/LB variant resulting in PTC in the same exon but upstream of the VUA | -2 pt |

NMD = nonsense-mediated decay; PTC premature termination codon *(source typo: "PTC premature termination codon" — missing "=" — transcribed verbatim)*

**Note (verbatim):** The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet "+1 pathogenic variant downstream" on the PVS1 flowchart. If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA. The VUA must be sufficiently rare, meet PM2_Supporting, to apply this point system. If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic without use of PM5 and without use of only PVS1 plus PM2

#### Strength rows

| Strength | Criteria |
|----------|----------|
| **Strong** | PM5 may be applied at a Strong level of evidence for any nonsense variant with 4+ points from informative variants (see point table above). PM5_Strong should be downgraded to PM5_Moderate if PVS1 is applied at any strength. *(Notes as above.)* *Modification Type: General recommendation, Strength* |
| **Moderate** | Applicable at default strength (PM5) if previously established variant is classified as pathogenic or at reduced strength of PM5_Supporting if previously established variant is classified as likely pathogenic.<br>PM5 may also be applied at a Moderate level of evidence for any nonsense variant with 2+ points from informative variants (see point table above). PM5_Moderate may not be combined with PVS1_VeryStrong (should be downgraded to PM5_Supporting if PVS1_VeryStrong is applied). *(Notes as above.)* *Modification Type: General recommendation, Strength* |
| **Supporting** | Applicable at default strength (PM5) if previously established variant is classified as pathogenic or at reduced strength of PM5_Supporting if previously established variant is classified as likely pathogenic. Also applicable to a nonsense variant with 1 point from an informative variant (see point table). Informative variants must also be classified by these rule specifications. *(Notes as above.)* *Modification Type: General recommendation, Strength* |

> Internal inconsistency flagged: the Moderate and Supporting rows both open with the sentence "Applicable at default strength (PM5) if previously established variant is classified as pathogenic or at reduced strength of PM5_Supporting if previously established variant is classified as likely pathogenic." The same sentence therefore appears under two different strength headings. Transcribed as written; not reconciled.

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

PM6 has no Very Strong row in the specification (PS2 does). See [Appendix B](#appendix-b---svi-recommendation-for-de-novo-criteria-ps2--pm6-version-11-file-ps2_pm6pdf) for the SVI ladder, which does define PM6_VeryStrong at 4 points.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386) with the additional specification that unaffected individuals contributing to the calculated LOD score **(Attached document: PP1 specifications)** must be heterozygous carriers of one of the variants observed in the affected individuals (i.e. do not count wild-type/wild-type, individuals).

| Strength | Criteria |
|----------|----------|
| **Strong** | Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations. *Modification Type: General recommendation* |
| **Moderate** | Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations. *Modification Type: General recommendation* |
| **Supporting** | Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations. *Modification Type: General recommendation* |

The attached PP1 tables (Oza et al., Tables 4a and 4b) are transcribed in [Appendix F](#appendix-f---pp1-segregation-tables-file-pp1pdf). DCLRE1C is autosomal recessive, so Table 4b applies.

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable.**

**Comments:** Does not apply. The gnomAD v2.1.1 missense Z score for DCLRE1C (Z = -0.68) suggests this gene is not constrained for missense variation. Both benign and pathogenic missense variants are present in DCLRE1C.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | • Only applicable to synonymous or intronic variants predicted to impact splicing by SpliceAI with a delta score **greater than or equal to 0.2** (inclusive).<br>• **Do not apply to missense variants.**<br>*Modification Type: General recommendation* |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** PP4 applicability and strength is determined by the total points accumulated by a single affected individual according to the table below and the following total point ranges:

| Total points | Outcome |
|---|---|
| **<1 Point** (strict less-than) | PP4 not met |
| **1 - <2 Points** (lower bound inclusive, upper bound strict) | PP4 |
| **2 - <6 Points** (lower bound inclusive, upper bound strict) | PP4_Moderate |
| **≥6 Points** (inclusive) | PP4_Strong<sup>1</sup> |

#### PP4 Evidence Point Table

| Evidence Description | Points |
|---|---|
| Diagnostic criteria met for SCID (Criteria 1 and 3 or Criterion 4 by itself) or Leaky SCID/Omenn syndrome (excluding Criterion 2)<sup>1</sup> | 0.5 |
| SCID gene panel or exome/genome sequencing conducted (only applicable if genetic testing did not provide an alternative genetic explanation for SCID/Leaky SCID/Omenn syndrome phenotype) | 1 |
| Family history of SCID (only applicable if SCID gene panel or exome/genome sequencing was conducted on proband and did not provide an alternative genetic explanation for phenotype) | 0.5 |
| Navajo or Apache descent | 0.25 |
| Increased cellular radiosensitivity as determined by >1 log of decreased proliferation or survival OR impaired gH2AX correction compared to wild-type controls AND pathogenic or likely pathogenic variants in PRKDC, NHEJ1, and LIG4 have been excluded. PMIDs: 11336668, 26476407, 27611239, 25917813 | 4.5 |
| Increased cellular radiosensitivity as determined by >1 log of decreased proliferation or survival OR impaired gH2AX correction compared to wild-type controls AND pathogenic or likely pathogenic variants in PRKDC, NHEJ1, and LIG4 have **NOT** been excluded. PMIDs: 11336668, 26476407, 27611239, 25917813 | 0.5 |
| Decreased V(D)J recombination as established by the laboratory AND pathogenic or likely pathogenic variants in RAG1, RAG2, PRKDC, NHEJ1, LIG4, and NUDCD3 have been excluded. PMIDs: 11336668, 15071507, 25917813, and 29906526 | 4.5 |
| Decreased V(D)J recombination as established by the laboratory AND pathogenic or likely pathogenic variants in RAG1, RAG2, PRKDC, NHEJ1, LIG4, and NUDCD3 have **NOT** been excluded. PMIDs: 11336668, 15071507, 25917813, and 29906526 | 1 |
| Vector-based complementation corrected increased cellular radiosensitivity (as determined by >1 log of decreased proliferation or survival OR impaired gH2AX correction compared to wild-type controls) and/or decreased V(D)J recombination (as established by the laboratory) and/or led to in vitro restoration of hematopoietic stem cell maturation into T cells | 5 |
| SCID phenotype corrected by DCLRE1C gene therapy **WITHOUT** CNV testing performed<sup>2</sup> | 4.5 |
| SCID phenotype corrected by DCLRE1C gene therapy **WITH** CNV testing performed<sup>2</sup> | 6 |
| T-B-NK+ lymphocyte subset profile* (See notes) | 0.5 |

<sup>1</sup> The diagnostic criteria should follow the PIDTC 2022 specification, summarized [here] (link target given in the source as a hyperlink; the URL itself is not printed in the distributed PDF).

<sup>2</sup> CNV (Copy number variation) testing is required if PP4_Strong cannot be reached without points from gene therapy in order to certify that the variant in question is causative for the phenotype, and not one CNV event corrected by gene therapy and not previously identified.

\*Notes: 1) If NK cells are not noted or are present, criteria may still be applied if SCID gene panel or exome/genome sequencing has ruled out alternative causes; 2) If maternal T cells are present, the T lymphocyte profile is still considered to be T- (autologous T cells are absent).

#### Strength rows

| Strength | Criteria |
|----------|----------|
| **Strong** | A patient score of ≥ 6 points<sup>1</sup>. (<sup>1</sup>CNV testing is required if PP4_Strong cannot be reached without points from gene therapy…) *Modification Type: Disease-specific, Gene-specific* |
| **Moderate** | A patient score of 2-<6 points. *Modification Type: Disease-specific, Gene-specific* |
| **Supporting** | A patient score of 1-<2 points. *Modification Type: Disease-specific, Gene-specific* |

> The standalone "PP4 - DCLRE1C.pdf" (labelled "2025 Updates" in the registry) contains an earlier revision of this table. Differences are listed in [Appendix E](#appendix-e---erratum-cross-check).

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable.** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:** Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:
- Prevalence: 1:5,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.03 (based on the contribution of *DCLRE1C* variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 3.2%, rounded to 3%)
- Penetrance: 50%

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | gnomAD popmax filtering allele frequency **>0.00346** (strict greater-than). *Modification Type: Gene-specific* |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:** gnomAD popmax filtering allele frequency **>0.00078**<sup>1</sup> (strict greater-than).

Maximum credible population allele frequency threshold is determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:
- Prevalence: 1:50,000
- Allelic heterogeneity: 1
- Genetic heterogeneity: 0.03 (based on the contribution of *DCLRE1C* variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 3.2%, rounded to 3%)
- Penetrance: 100%

<sup>1</sup> Consider also bottleneck populations.

| Strength | Criteria |
|----------|----------|
| **Strong** | gnomAD popmax filtering allele frequency >0.00078 (Consider also bottleneck populations). *Modification Type: Gene-specific* |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | BS2_Strong: Can be applied at Strong level if observed in at least 3 homozygotes (i.e. ≥3, inclusive). *Modification Type: Disease-specific, Gene-specific* |
| **Supporting** | Only to be used when the variant is observed in the homozygous state in a healthy adult.<br>BS2_Supporting: Can be applied at Supporting level if observed in at least 1 homozygote (i.e. ≥1, inclusive). *Modification Type: Disease-specific, Gene-specific* |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** **Not Applicable.**

**Comments:** There is not a well-established functional study which can rule out all damaging effects on protein function.

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
| **BP1** | Not Applicable | Does not apply. DCLRE1C missense variants are a known mechanism of disease. |
| **BP2** | Not Applicable | No comment given. |
| **BP3** | Not Applicable | Does not apply. |
| **BP4** | Not Applicable | No comment given. |
| **BP5** | Not Applicable | No comment given. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP7** | **Specified — Supporting** | • Applicable to both synonymous variants and deep intronic variants affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions.<br>• The variant should be predicted not to impact splicing by at least two out of three *in silico* tools (freely available tools include GeneSplicer, MaxEntScan, NNSplice, SpliceAI, Splicing Sequences Database (SSF), and varSEAK).<br>• Given the potential for poor conservation of genes related to T cell and B cell development among vertebrates, nucleotide conservation is **not required** in order to apply BP7.<br>*Modification Type: General recommendation* |

> Source inconsistency flagged: BP7 requires agreement of "at least two out of three *in silico* tools" but then lists six tools. Transcribed verbatim; not reconciled.
> Positional comparators for BP7 are inclusive: "at or beyond the +7 (donor) and -21 (acceptor) positions."

---

## Rules for Combining Criteria

Transcribed verbatim from the "Rules for Combining Criteria" section of the v2.2 specification. Parenthetical lists are the criterion codes the VCEP assigns to each strength bucket.

### Pathogenic

| # | Combination |
|---|---|
| 1 | **1 Very Strong** (PVS1, PS2_Very Strong, PM3_Very Strong) **AND ≥ 1 Strong** (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong) |
| 2 | **1 Very Strong** (PVS1, PS2_Very Strong, PM3_Very Strong) **AND ≥ 2 Moderate** (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate) |
| 3 | **1 Very Strong** (PVS1, PS2_Very Strong, PM3_Very Strong) **AND 1 Moderate** (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate) **AND 1 Supporting** (PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
| 4 | **1 Very Strong** (PVS1, PS2_Very Strong, PM3_Very Strong) **AND ≥ 2 Supporting** (PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
| 5 | **≥ 2 Strong** (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong) |
| 6 | **1 Strong** (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong) **AND ≥ 3 Moderate** (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate) |
| 7 | **1 Strong** **AND 2 Moderate** **AND ≥ 2 Supporting** |
| 8 | **1 Strong** **AND 1 Moderate** **AND ≥ 4 Supporting** |

### Likely Pathogenic

| # | Combination |
|---|---|
| 1 | **1 Very Strong** (PVS1, PS2_Very Strong, PM3_Very Strong) **AND 1 Moderate** (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate) |
| 2 | **1 Strong** (PVS1_Strong, PS1, PS2, PS3, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong) **AND 1 Moderate** (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate) |
| 3 | **1 Strong AND ≥ 2 Supporting** (PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
| 4 | **≥ 3 Moderate** (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS3_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate) |
| 5 | **2 Moderate AND ≥ 2 Supporting** |
| 6 | **1 Moderate AND ≥ 4 Supporting** |
| 7 | **1 Strong AND 2 Moderate** |
| 8 | **1 Very Strong** (PVS1, PS2_Very Strong, PM3_Very Strong) **AND 1 Supporting** (PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |

> Note: Likely Pathogenic rows 2 and 7 overlap with each other (1 Strong + 1 Moderate; 1 Strong + 2 Moderate). Transcribed as listed.

### Benign

| # | Combination |
|---|---|
| 1 | **≥ 2 Strong** (BS1, BS2, BS4) |
| 2 | **1 Stand Alone** (BA1) |

### Likely Benign

| # | Combination |
|---|---|
| 1 | **≥ 2 Supporting** (BS2_Supporting, BP7) |
| 2 | **1 Strong** (BS1, BS2, BS4) |

> No Tavtigian-style points-based classification system is specified by this VCEP. The specification type is stated as "Richards et al., 2015 - Combining rules".

---

## Appendices

### Appendix A - DCLRE1C PVS1 flowchart (file: PVS1.pdf)

Registry label: "PVS1: Specified PVS1 flowchart for DCLRE1C gene". One-page decision tree. Transcribed below as branch → condition → outcome.

**Branch: Nonsense or Frameshift**

| Condition | Sub-condition | Outcome |
|---|---|---|
| Predicted to undergo NMD <sup>b</sup> | Exon is present in biologically-relevant transcript(s) | PVS1 |
| Predicted to undergo NMD <sup>b</sup> | Exon is absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD <sup>b</sup> (i.e. premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon [c.1106 (codon 369) in exon 13]) | Truncated/altered region is critical to protein function | PVS1_Strong |
| " (role of region in protein function is unknown) | LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) | N/A |
| " (role unknown) | LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) → Variant removes >10% of protein → 1+ pathogenic variant present downstream | PVS1_Strong |
| " (role unknown) | … → Variant removes >10% of protein → No known downstream pathogenic variants | PVS1_Moderate |
| " (role unknown) | … → Variant removes <10% of protein | PVS1_Moderate |

**Branch: GT--AG 1,2 splice sites <sup>a</sup>**

| Condition | Sub-condition | Outcome |
|---|---|---|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD <sup>b</sup> | Exon is present in biologically-relevant transcript(s) | PVS1 |
| " | Exon is absent from biologically-relevant transcript(s) | N/A |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is **NOT** predicted to undergo NMD <sup>b</sup> (i.e. premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon [c.1106 (codon 369) in exon 13]) | Truncated/altered region is critical to protein function | PVS1_Strong |
| " (role unknown) | LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) | N/A |
| " (role unknown) | LoF not frequent and exon present → removes >10% of protein → 1+ pathogenic variant present downstream | PVS1_Strong |
| " (role unknown) | … → removes >10% of protein → No known downstream pathogenic variants | PVS1_Moderate |
| " (role unknown) | … → Variant removes <10% of protein | PVS1_Moderate |
| Exon skipping or use of a cryptic splice site preserves reading frame | Truncated/altered region is critical to protein function | PVS1_Strong |
| " (role unknown) | LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) | N/A |
| " (role unknown) | LoF not frequent and exon present → removes >10% of protein → 1+ pathogenic variant present within deleted region | PVS1_Strong |
| " (role unknown) | … → removes >10% of protein → No known pathogenic variants within deleted region | PVS1_Moderate |
| " (role unknown) | … → Variant removes <10% of protein | PVS1_Moderate |

**Branch: Deletion (Single exon to full gene)**

| Condition | Sub-condition | Outcome |
|---|---|---|
| Full gene deletion | — | PVS1 <sup>d</sup> |
| Single to multi exon deletion – Disrupts reading frame and is predicted to undergo NMD <sup>b</sup> | Exon is present in biologically-relevant transcript(s) | PVS1 |
| " | Exon is absent from biologically-relevant transcript(s) | N/A |
| Single to multi exon deletion – Disrupts reading frame and is **NOT** predicted to undergo NMD <sup>b</sup> (i.e. premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon [c.1106 (codon 369) in exon 13]) — and — Single to multi exon deletion – Preserves reading frame | Truncated/altered region is critical to protein function | PVS1_Strong |
| " (role unknown) | LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) | N/A |
| " (role unknown) | LoF not frequent and exon present → removes >10% of protein → 1+ pathogenic variant present within deleted region | PVS1_Strong |
| " (role unknown) | … → removes >10% of protein → No known pathogenic variants within deleted region | PVS1_Moderate |
| " (role unknown) | … → Variant removes <10% of protein | PVS1_Moderate |

**Branch: Duplication (≥1 exon in size and must be completely contained within gene)**

| Condition | Outcome |
|---|---|
| Proven in tandem → Reading frame disrupted and NMD predicted to occur | PVS1 |
| Proven in tandem → No or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem → Reading frame presumed disrupted and NMD predicted to occur | PVS1_Strong |
| Proven not in tandem | N/A |

**Branch: Initiation Codon**

| Condition | Outcome |
|---|---|
| No known alternative start codon in other transcripts → ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon | PVS1_Moderate |
| No known alternative start codon in other transcripts → No pathogenic variant(s) upstream of closest potential in-frame start codon | PVS1_Supp |
| Different functional transcript uses alternative start codon | N/A |

> **Missing content flagged:** The flowchart uses footnote markers **a**, **b**, and **d**, but the distributed one-page PDF contains no footnote legend defining them. Their definitions are **not specified in the distributed file**; do not infer them.

---

### Appendix B - SVI Recommendation for de novo Criteria (PS2 & PM6), Version 1.1 (file: PS2_PM6.pdf)

Working Group Page: https://clinicalgenome.org/working-groups/sequence-variant-interpretation/
Date Approved: March 18, 2018, updated May 5, 2021
Changes from v1: Clarified that confirmed/assumed is with regards to parental relationships and not de novo status

The SVI Working Group proposes a point-based system to determine the strength of de novo evidence (ACMG/AMP criteria codes PS2 and PM6) based upon three parameters:
- confirmed parental relationships versus assumed parental relationships status
- phenotypic consistency
- number of de novo observations

Each proband with a de novo variant is awarded a point value based upon phenotypic consistency and confirmed or assumed parental relationships (Table 1). The combined point value of all de novo occurrences is then compared to Table 2. If the parents have not been tested for parentage or for the variant, no points should be awarded.

**Table 1. Points* awarded per de novo occurrence**

| Phenotypic consistency | de novo with confirmed parental relationships | de novo with unconfirmed parental relationships |
|---|---|---|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity** | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

\*Note that these points are *not* equivalent to the points used to classify a variant per the Tavtigian et al 2020 "Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines"
\*\*Maximum allowable value of 1 may contribute to overall score

**Table 2. Recommendation for determining the appropriate ACMG/AMP evidence strength level for de novo occurrence(s)**

| Supporting (PS2_Supporting or PM6_Supporting) | Moderate (PS2_Moderate or PM6) | Strong (PS2 or PM6_Strong) | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |
|---|---|---|---|
| 0.5 | 1 | 2 | 4 |

**Additional considerations for applying de novo criteria based on inheritance (verbatim):**
- Conditions with X-linked inheritance: if the variant occurs de novo in an unaffected carrier mother, and family history is consistent - i.e., she has no affected brothers/other male relatives apart from her affected son(s) – de novo criteria may be applied despite the fact that she is unaffected.
- **Autosomal recessive conditions: for a de novo occurrence in a gene associated with a condition inherited in an autosomal recessive pattern without an additional pathogenic/likely pathogenic variant identified, the strength of evidence should be decreased by one level.** (Directly relevant to DCLRE1C.)
- Mosaicism: for cases with apparent germline mosaicism (multiple affected siblings with both parents negative for the variant), parental relationships must be confirmed in order for de novo criteria to apply.

The document also contains worked examples using NIPBL, SIK1 and ASH1L variants; these are illustrative and gene-agnostic.

---

### Appendix C - SVI Recommendation for in trans Criterion (PM3), Version 1.0 (file: PM3.pdf)

Working Group Page: https://clinicalgenome.org/working-groups/sequence-variant-interpretation/
Date Approved: May 2, 2019; **Table 1 updated October 17, 2025**

**SVI revision to PM3 (verbatim):** For recessive disorders, detected in trans with a pathogenic *or likely pathogenic* variant *in an affected patient*.

**Table 1. Points awarded per in trans proband**

| Classification/Zygosity of other variant | Confirmed in trans | Phase unknown |
|---|---|---|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence — Non-consanguineous** *(no max)* | 1.0 | 1.0 |
| Homozygous occurrence — Consanguineous** *(no max)* | 0.5 | 0.5 |
| Uncertain significance variant *(max point 0.5)* | 0.25 | 0 |

Column header in source: "Points per Proband-Family*".

\*Multiple probands from separate nuclear families that are later found to have identity-by-descent should only be counted once.
\*\*When consanguinity is not known or reported: if family IS NOT from a bottlenecked population (as defined by gnomAD), assume non-consanguinity; otherwise, assume consanguinity. If genetic ancestry of the family cannot be determined, assume consanguinity.

**Table 2. Recommendation for determining the appropriate evidence strength level for PM3**

| PM3_Supporting | PM3 | PM3_Strong | PM3_VeryStrong |
|---|---|---|---|
| 0.5 | 1.0 | 2.0 | 4.0 |

**Considerations (verbatim):**
- **Allele Frequency** - Application of PM3 is contingent on the allele frequency of the variant being assessed and the variant presumably on the other allele both being sufficiently rare (meets PM2 threshold). This contingency is to avoid incorrect application of PM3 to high frequency variants that are likely to occur in trans with P/LP variants based on frequency.
- **Phasing** - If the phase cannot be determined, it is recommended that at least two different LP/P variants (depending on classifications) are needed to equal the weight of one LP/P co-occurrence confirmed in trans.
  - In confirmation of phasing, if only one parent is tested and found to carry one allele, variants can be counted as in trans. (Worked PAH example given.)
- **Classification** – Probands should be weighted less when the variant on the other allele is of uncertain significance and rare (meets PM2); however, weight may vary by gene size as larger genes are more likely to have a second variant by chance (default 0.25 points). If the variant on the other allele is classified as P or LP, weighting depends on phasing (see Phasing above), with P/LP being weighted equally if confirmed in trans and different point values per proband if phasing is unknown (0.5 points and 0.25 points, respectively). To avoid circularity, in all instances (phasing confirmed or unknown), the classification of the variant on the other allele should not use evidence from the variant being interrogated.
- **Homozygous occurrences** – For homozygous occurrences, the default weight is dropped to 0.5 points, as a rare homozygous occurrence may be due to consanguinity. A recommended max of 1.0 points of all homozygous cases is suggested to prevent overclassification of homozygous occurrences in the absence of additional data.

> **Internal contradiction flagged (within PM3.pdf itself):** Table 1 marks both homozygous rows *"(no max)"*, while the "Homozygous occurrences" consideration paragraph on page 2 still states "A recommended max of 1.0 points of all homozygous cases is suggested." The October 2025 Table 1 update was evidently not propagated to the narrative Considerations text. Transcribed both; not reconciled.
> Additionally, the Classification paragraph gives the VUS default as 0.25 points, whereas Table 1 gives 0.25 (confirmed in trans) / 0 (phase unknown) with a max of 0.5.

---

### Appendix C2 - PM3 Minor Amendments (file: PM3 Minor Amendments.docx)

This file records the SVI's proposed October 2025 minor updates to PM3 Table 1 and the SCID VCEP's responses. Transcribed in full.

**Footnotes as amended:**
- \* Multiple probands from separate nuclear families that are later found to have identity-by-descent should only be counted once.
- \*\* When consanguinity is not known or reported: if family IS NOT from a bottlenecked population (as defined by gnomAD), assume non-consanguinity; otherwise, assume consanguinity. If genetic ancestry of the family cannot be determined, assume consanguinity.

**SVI Comments and SCID VCEP responses (verbatim):**

| SVI comment | SCID VCEP response |
|---|---|
| Prefer N/A to repeating the 1.0 and 0.5 | The SCID VCEP deliberated this point. Our geneticists pointed out that apparent homozygous variants could result from hemizygosity, which may be undetected if the parents are not sequenced (i.e., "Phase unknown"). Because of the likelihood that authors may not bother to sequence the parents in homozygous situations, especially in older publications, the VCEP experts preferred to leave the numbers in place. |
| Update "max point 0.5 per family" to "max point 0.5" as in original specs.<br>Please replace "max point 0.5 per family" from the Homozygous Consanguineous and indicate "no max". Rationale: "per proband" is a rule for the whole table in general (per the table title); Multiple cases per family will inherently be counted as PP1 instead of multiple PM3s | The SCID VCEP agreed and made the changes to the table. To minimize confusion for biocurators and experts as much as possible between proper application of PM3 vs. PP1 (which we have definitely observed, even in sustained curations), we changed "Proband" to "Proband-Family". |
| What to do if you don't know about consanguinity | The VCEP decided to use gnomAD definitions to specify assumption of non-consanguinity for families from non-bottlenecked populations and assumption of consanguinity otherwise. A footnote was added to the Table. |
| If the VCEP wishes, they can provide an asterisk footnote that supports the notion that "multiple probands from separate nuclear families that are later found to have identity-by-descent should only be counted once." | We added this footnote to the Table. |

**Amended Table 1 as it appears in this document:**

| Classification/Zygosity of other variant | Points per Proband-Family* — Confirmed in trans | Points per Proband-Family* — Phase unknown |
|---|---|---|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence — Non-consanguineous** (no max) | 1.0 | 1.0 |
| Homozygous occurrence — Consanguineous** (no max) | 0.5 | 0.5 |
| Uncertain significance variant (max point 0.5) | 0.25 | 0 |

**Embedded image (word/media/image1.png), transcribed:** a copy of PM3 Table 2 —

| PM3_Supporting | PM3 | PM3_Strong | PM3_VeryStrong |
|---|---|---|---|
| 0.5 | 1.0 | 2.0 | 4.0 |

**Amendment status: REFLECTED.** Every amendment agreed to in this document ("Proband" → "Proband-Family"; consanguineous homozygous row changed from "max point 0.5 per family" to "no max"; the gnomAD consanguinity-assumption footnote; the identity-by-descent footnote) appears in the distributed PM3.pdf Table 1 (marked "Table 1 updated October 17, 2025"). The one caveat is the un-updated narrative paragraph on page 2 of PM3.pdf noted in Appendix C.

---

### Appendix D - SCID VCEP PS3_BS3 Functional Evidence (DCLRE1C) (file: SCID VCEP PS3_BS3 Functional Evidence (DCLRE1C).xlsx)

Two worksheets. This is an **assay-instance lookup**, not a variant-level classification table: it catalogues each published assay instance and whether the VCEP approved it. The rules that consume it are the PS3 specifications above.

**Worksheet 1 — "General Class of Assay Summary"** (full transcription; 5 populated rows)

| Gene | General Class of Assay | PMIDs |
|---|---|---|
| DCLRE1C | V(D)J recombination assay | PMID: 26476407, PMID: 15731174, PMID: 25917813, PMID: 15071507, PMID: 19349461 |
| | DNA cleavage assay** | PMID: 15731174, PMID: 24500713, PMID: 15071507, PMID: 19349461 |
| | DNA-PKcs assay (binding and/or phosphorylation) | PMID: 15731174, PMID: 15071507, PMID: 19349461 |
| | DNA repair activity assay$++ | PMID: 25917813 |

> **Flagged:** the markers `**`, `$` and `++` appear on assay-class names in this sheet, but the worksheet contains **no legend defining them**. Their meaning is not specified in the distributed file.

**Worksheet 2 — "DCLRE1C Assay Instance Details"** — column-oriented (attributes in column A, one assay instance per column B..O; 14 instances). Structure and legend:

Row labels (attributes captured for each instance): PMID; Gene; DOI / link; Author; Year; General Class of Assay; Assay (General Description); Material used (patient cells, engineered variants, cell lines, animal model, etc.); Readout type (qualitative/quantitative); Readout description; Biological replicates (met/not met); Technical replicates (met/not met); description; Basic positive control (met/not met); description; Basic negative control (met/not met); description; Validation controls P/LP (#); Validation controls B/LB (#); Statistical analysis (general description); Threshold for normal readout; Threshold for abnormal readout; **Approved assay (y/n)**; **Proposed strength**; Variant(s) Tested; Notes.

**Approval summary (the operative lookup):**

| # | PMID | Author, Year | General Class of Assay | Approved assay (y/n) | Proposed strength |
|---|---|---|---|---|---|
| 1 | 26476407 | Volk…Grimbacher, 2015 | V(D)J recombination | y | PS3_Supporting |
| 2 | 15731174 | Ege…Pannicke, 2005 | V(D)J recombination | y | PS3_Supporting |
| 3 | 25917813 | Felgentreff…Notarangelo, 2015 | V(D)J recombination | y | PS3_Supporting |
| 4 | 15071507 | Pannicke…Schwarz, 2004 | V(D)J recombination | y | PS3_Supporting |
| 5 | 19349461 | Huang…Sekiguchi, 2009 | V(D)J recombination (murine Artemis-P70 model) | n | (blank) |
| 6 | 15731174 | Ege…Pannicke, 2005 | DNA cleavage assay | n | (blank) |
| 7 | 24500713 | Li…Lieber, 2014 | DNA cleavage assay | n | (blank) |
| 8 | 15071507 | Pannicke…Schwarz, 2004 | DNA cleavage assay | n | (blank) |
| 9 | 19349461 | Huang…Sekiguchi, 2009 | DNA cleavage assay | n | (blank) |
| 10 | 15731174 | Ege…Pannicke, 2005 | DNA-PKcs assay (phosphorylation) | n | "Should this be approved at any level of strength? Uncertain relationship to disease mechanism…" |
| 11 | 15071507 | Pannicke…Schwarz, 2004 | DNA-PKcs assay (phosphorylation) | n | "Should this be approved at any level of strength? Uncertain relationship to disease mechanism…" |
| 12 | 19349461 | Huang…Sekiguchi, 2009 | DNA-PKcs assay (binding) | n | "Should this be approved at any level of strength? … possible evidence for PVS1 …" |
| 13 | 19349461 | Huang…Sekiguchi, 2009 | DNA-PKcs assay (phosphorylation) | n | "Should this be approved at any level of strength? … possible evidence for PVS1 …" |
| 14 | 25917813 | Felgentreff…Notarangelo, 2015 | DNA repair activity assay | y | PS3_Supporting |

> **Note / apparent discrepancy:** every approved instance in this workbook carries a "Proposed strength" of **PS3_Supporting**, including the DNA repair activity assay. The v2.2 specification, by contrast, assigns **PS3_Moderate** when *both* a DNA repair activity assay and a V(D)J recombination assay are abnormal, and PS3_Supporting for V(D)J recombination alone. The workbook column is labelled "Proposed" and predates/underlies the criterion text; both are transcribed as found.

> **Note:** the workbook's own "Threshold for normal/abnormal readout" rows record "numeric threshold not reported" for the V(D)J and DNA repair assays. The **<25% of wild-type activity** threshold comes from the VCEP's PS3 criterion text, not from the source publications.

**Validation controls:** every instance records 0 P/LP and 0 B/LB validation controls.

**Notes field (populated instances only):**
- Volk 2015 (V(D)J recombination): "Relatively little information about methods/validation reported for this assay in the publication"
- Ege 2005 (DNA cleavage): "Concerns about presence of host cell 5' exonucleases present in previous experiments that used HEK293T expression system rather than baculovirus expression system"
- Ege 2005 (DNA-PKcs phosphorylation): "Has loss of DNA-PKcs-attributed ARTEMIS phosphorylation been observed for any missense DCLRE1C variants?"

The "Variant(s) Tested" row lists the specific variants assayed in each instance (the Felgentreff 2015 columns list 41 variants). That row is a per-publication lookup and is not reproduced in full here; consult the workbook when confirming whether a specific variant was assayed.

---

### Appendix E - Erratum cross-check

Two erratum/amendment files ship with v2.2. Both were transcribed. Their status against the specification's own criteria tables:

#### E1. "PM3 Minor Amendments.docx" — **REFLECTED**

Every change agreed by the VCEP in this document is present in the distributed PM3.pdf Table 1 (which is stamped "Table 1 updated October 17, 2025"). No contradiction with the specification's PM3 rows, which simply point to the SVI document. Residual issue: PM3.pdf's page-2 narrative still says homozygous cases have "a recommended max of 1.0 points", contradicting the "(no max)" now in its own Table 1 — a defect inside the SVI document, not a VCEP/erratum conflict.

#### E2. "DCLRE1C Corrections 1.6.26.docx" — **PARTIALLY REFLECTED**

| Item in the corrections file | Present in the v2.2 spec tables? |
|---|---|
| PS3_Strong — animal model text | **Yes**, verbatim. |
| PS3_Moderate — abnormal in **both** DNA repair activity AND V(D)J recombination, <25% of wild-type | **Yes**, verbatim. |
| PS3_Supporting — abnormal V(D)J recombination alone, <25% of wild-type | **Yes**, verbatim. |
| PS3 approved assay instance lists | **Yes**, identical in both. |
| **PS3 gating requirement: "At least one previously observed proband with the DCLRE1C variant meeting PP4 is required to apply PS3 at any strength on the basis of a cellular model/in vitro study."** | **NO.** This sentence appears twice in the corrections file (under Moderate and under Supporting) but is **absent** from the PS3 rows of the v2.2 specification PDF. The release notes state "Uploaded DCLRE1C corrections which includes PS3 codes edits", so the corrections file is the operative statement of intent; the requirement appears simply not to have been carried into the criteria table. **This is an unreconciled discrepancy — the VCEP should be consulted before applying or ignoring the gate.** |
| BS2_Strong ≥3 homozygotes; BS2_Supporting ≥1 homozygote | **Yes**, verbatim, and matches release note. |
| PP4 point table and 4-tier point ranges | **Yes**, matches the spec's PP4 table row for row and point for point. |
| PP4 footnote: "CNV testing is required if PP4_Strong cannot be reached without points from gene therapy…" | **Yes**, matches the spec. Note this is the **newer** wording. |

#### E3. Stale supplementary file: "PP4 - DCLRE1C.pdf" (registry label "2025 Updates")

This standalone PP4 PDF is an **earlier** revision than the PP4 content in both the v2.2 spec and the corrections file. Differences:

| | PP4 - DCLRE1C.pdf | v2.2 spec + Corrections 1.6.26 |
|---|---|---|
| Footnote 1 | "CNV testing is required **to consider PP4_Strong** in order to certify that the variant in question is **the causative** for the phenotype, and not one CNV event corrected by gene therapy and not **identified previously**." | "CNV testing is required **if PP4_Strong cannot be reached without points from gene therapy** in order to certify that the variant in question is **causative** for the phenotype, and not one CNV event corrected by gene therapy and not **previously identified**." |
| V(D)J rows | Both the "have been excluded" and the "have **NOT**been excluded" rows carry an inline **"(4.5 pt)"** in the description text, while the Points column reads 4.5 and **1** respectively — the "(4.5 pt)" on the NOT-excluded row **contradicts** its own Points cell of 1. | Inline point annotations agree with the row values (4.5 pt and 1 pt). |
| Typo | "have NOTbeen excluded" (missing space) — appears in both V(D)J NOT rows. | Corrected to "have NOT been excluded". |

**Operative version: the v2.2 specification table (equivalently, the Corrections 1.6.26 file).** The standalone PP4 PDF should be treated as superseded. Its footnote-1 wording is materially different: it appears to require CNV testing for *any* PP4_Strong, whereas the operative wording requires it only when gene-therapy points are needed to reach PP4_Strong.

#### E4. Release-note item with no corresponding table change

The release notes state: "Removed request for update of caveat on PM1 criteria. This was made in error and should not have been added." The PM1 row in v2.2 is Not Applicable with the pseudogene/deletion-hotspot comment; there is no residual caveat request. Consistent.

---

### Appendix F - PP1 segregation tables (file: PP1.pdf)

Reproduced from Oza et al. (Hum Mutat; PMID: 30311386), pages 35–36.

**Table 4a: Recommendations for PP1 (segregation evidence) — General Recommendations**

| | Supporting | Moderate | Strong |
|---|---|---|---|
| Likelihood | 4:1 | 16:1 | 32:1 |
| LOD Score | 0.6 | 1.2 | 1.5 |
| Autosomal dominant threshold | 2 affected segregations | 4 affected segregations | 5 affected segregations |
| Autosomal recessive threshold | See Table 4b | See Table 4b | See Table 4b |

**Table 4b: Recommendations for autosomal recessive segregation evidence (PP1) — General Recommendations (Phenocopy not an issue)**

Rows = affected segregations; columns = unaffected recessive segregations. Cell value = LOD score.

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

**Table 4b legend (verbatim):** Affected segregations are counted in rows and unaffected segregations in columns. Affected segregations are affected family members in whom biallelic compound heterozygous or homozygous variants segregates. Unaffected segregations are defined as unaffected family members, typically siblings, who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants identified in the proband, or a heterozygous carrier for a single variant. Unaffected, carrier parents DO NOT count as unaffected segregations. There may be scenarios where individuals other than siblings could be counted as segregations, such as in families where one parent is affected with the autosomal recessive disorder, in large families with multiple branches, or in consanguineous families.

Each cell shows the LOD score of each combination of affected and unaffected segregations. LOD scores were calculated using a simplified LOD score formula, as described in Strande et al., 2017.

> **DCLRE1C-specific overlay (from the spec's PP1 VCEP Specifications cell):** unaffected individuals contributing to the calculated LOD score must be heterozygous carriers of one of the variants observed in the affected individuals — i.e. do **not** count wild-type/wild-type individuals. This is narrower than Table 4b's own legend, which admits wild-type-for-both individuals as unaffected segregations. Where they conflict, the VCEP specification governs for DCLRE1C. Flagged as a deliberate VCEP narrowing, not an error.

> Comparator note: the LOD thresholds in Table 4a (0.6 / 1.2 / 1.5) are stated as bare values; neither Oza et al. nor the VCEP states whether they are inclusive. **Not specified.**

---

## Source File Inventory

All nine distributed files were opened and transcribed. None failed to open.

| File | Type | Opened | Transcribed in |
|---|---|---|---|
| ClinGen_ACMG_Specifications_DCLRE1C_v2.2.pdf | PDF, 20 pp | Yes | Body + Rules for Combining Criteria |
| PVS1.pdf | PDF, 1 p (flowchart) | Yes | Appendix A |
| PP1.pdf | PDF, 2 pp | Yes | Appendix F |
| PM3.pdf | PDF, 2 pp | Yes | Appendix C |
| PS2_PM6.pdf | PDF, 2 pp | Yes | Appendix B |
| PP4 - DCLRE1C.pdf | PDF, 1 p | Yes | Appendix E3 (superseded revision) |
| PM3 Minor Amendments.docx | DOCX (+1 embedded PNG) | Yes, incl. embedded image | Appendix C2 |
| DCLRE1C Corrections 1.6.26.docx | DOCX | Yes | PS3 / BS2 / PP4 body + Appendix E2 |
| SCID VCEP PS3_BS3 Functional Evidence (DCLRE1C).xlsx | XLSX, 2 sheets | Yes | Appendix D |

(`GN116_data.json` is download metadata, not source material.)

**Content referenced by the sources but not distributed:**
- PVS1 flowchart footnotes **a**, **b**, **d** — markers used, legend absent from the file.
- Footnote markers `**`, `$`, `++` in the xlsx assay-class summary — no legend in the workbook.
- The PIDTC 2022 diagnostic-criteria summary, linked as "here" in PP4 — the URL is not printed in the distributed PDFs.
- Tayoun et al., 2018 (PMID: 30192042) PVS1 recommendations, referenced by PVS1 strength rows but not distributed beyond the gene-specific flowchart.

---

## Version History

| Version | Released | Notes |
|---|---|---|
| 2.2 | 6/1/2026 | Current. Release notes reproduced at the top of this document. |

Earlier version history is not stated in the distributed v2.2 package. **Not specified by this VCEP.**

---

*This document was compiled from the ClinGen VCEP specification and its distributed supplementary files. Content the VCEP did not specify is marked as such rather than filled in from generic ACMG/AMP or SVI defaults. For the most current version, please refer to the ClinGen website.*
