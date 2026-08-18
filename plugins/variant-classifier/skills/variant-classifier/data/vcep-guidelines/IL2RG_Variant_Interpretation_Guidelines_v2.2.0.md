# ClinGen Severe Combined Immunodeficiency Disease VCEP Variant Interpretation Guidelines for IL2RG

**Version:** 2.2
**Released:** 6/1/2026
**Affiliation:** Severe Combined Immunodeficiency Disease VCEP
**Source basis:** "Type: Richards et.al., 2015 - Combining rules" (as stated by the VCEP)
**DOI:** 10.5281/zenodo.21434697
**ClinGen registry ID:** GN129
**Rights Holder:** The Clinical Genome Resource (ClinGen)
**Research Group:** Severe Combined Immunodeficiency Disease VCEP

**Release Notes (verbatim from the specification):**
> Edited Rules for Combining Criteria to reflect standard combinations plus (A) 1 very strong + 1 supporting = Likely Pathogenic and (B) 1 Strong Benign = Likely Benign.
> Refreshed and saved Rules for Combining Criteria.
> Updated:
> PM5_Strong
> PM5_Moderate
> PM5_Supporting
> Made changes to PP4 criteria.
> Uploaded IL2RG corrections which includes PM1 and PS3 codes.

---

## Source Inventory

Every file distributed with this specification was opened and transcribed. Nothing in this guideline comes from any other source.

| File | Type | Opened | Where transcribed |
|------|------|--------|-------------------|
| `ClinGen_ACMG_Specifications_IL2RG_v2.2.pdf` (19 pp.) | Main specification | Yes | Throughout |
| `PVS1.pdf` (1 p.) | IL2RG-specific PVS1 decision tree | Yes (text + page render) | Appendix A |
| `PS2_PM6.pdf` (2 pp.) | ClinGen SVI de novo recommendation v1.1 | Yes | Appendix B |
| `PP1.pdf` (2 pp.) | Oza et al. Tables 4a / 4b (segregation) | Yes | Appendix C |
| `PP4 - IL2RG.pdf` (1 p.) | IL2RG PP4 points table | Yes (text + page render) | Appendix D |
| `SCID VCEP PS3_BS3 Functional Evidence.xlsx` (1 sheet: "IL2RG Assay Instance Details") | PS3/BS3 assay instance detail | Yes (openpyxl) | Appendix E |
| `GN129_data.json` | Download metadata | Yes | Not guideline content (per skill instructions) |

The specification's own "Files & Images" page lists exactly these five supplementary items:

> PP4 - IL2RG: 2025 updates
> PVS1: Specified PVS1 flowchart for IL2RG gene
> PS2_PM6: SVI recommendations for de novo criteria
> PP1: PP1 specifications
> SCID VCEP PS3_BS3 Functional Evidence : IL2RG

No file failed to open. No content was unreadable.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | IL2RG (HGNC:6010) |
| **HGNC Name** | interleukin 2 receptor subunit gamma |
| **Transcript** | NM_000206.3 |
| **Disease** | T-B+ severe combined immunodeficiency due to gamma chain deficiency (MONDO:0010315) |
| **Inheritance** | X-linked inheritance |

**Inheritance note.** This is an X-linked specification. The consequences the VCEP draws from that are explicit and are reproduced where they occur: PM3 is **Not Applicable**; BS2 is defined in **hemizygotes**; PM2 adds a **no-hemizygotes** requirement; and PS2/PM6 add a rule for unaffected carrier females. Do not import in-trans / biallelic reasoning from autosomal-recessive SCID specifications.

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
2. [Benign Criteria](#benign-criteria)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)
5. [Internal Inconsistencies and Apparent Source Errors](#internal-inconsistencies-and-apparent-source-errors)
6. [Version History](#version-history)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats (as printed in the specification):**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:** "See attached PVS1 flowchart." The flowchart is transcribed in full in [Appendix A](#appendix-a-il2rg-pvs1-decision-tree).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification: PVS1 at default strength (Very Strong) can be applied to variants not predicted to undergo nonsense-mediated decay but truncating the transmembrane domain (which begins at amino acid 255) or any distal region (i.e. cytoplasmic domain) due to the lack of functionality of the protein expressed with this defect. *(Modification Type: Gene-specific, Strength)* |
| **Strong** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification: For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 8, or variants in the last 50 nucleotides of the penultimate exon after c.874, codon 292, in exon 7), at least one pathogenic variant must be present downstream in order to apply PVS1_Strong. *(Modification Type: Gene-specific, Strength)* |
| **Moderate** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)) with one specification: For variants not predicted to undergo nonsense-mediated decay but removing >10% of protein (i.e. variants in the last exon, exon 8, or variants in the last 50 nucleotides of the penultimate exon after c.874, codon 292, in exon 7), when at least one pathogenic variant is not present downstream downgrade to PVS1_Moderate. *(Modification Type: Gene-specific, Strength)* |
| **Supporting** | Use ClinGen SVI recommendations for loss of function criterion (Tayoun et al., 2018 (PMID: 30192042)). *(Modification Type: Gene-specific, Strength)* |

*The Moderate row is transcribed verbatim; the source sentence reads "...when at least one pathogenic variant is not present downstream downgrade to PVS1_Moderate" (no comma before "downgrade"), which is awkward but not a duplication.*

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

Same amino acid change as a previously established pathogenic variant regardless of nucleotide change OR splice variants at same nucleotide and with similar impact prediction as previously reported pathogenic variant (if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tools, ie SpliceAI).

- Can also use PS1 for splice variants located in the splice consensus sequence, at the same nucleotide position as a previously reported pathogenic variant.
  - Example: c.105+1G>C is known to be pathogenic, can use PS1 for c.105+1G>T
- Applicable at default strength (PS1) if previously established variant is classified as pathogenic or at reduced strength of PS1_Moderate if previously established variant is classified as likely pathogenic.
- Previously established variant must be classified by SCID VCEP specifications for IL2RG.

| Strength | Criteria |
|----------|----------|
| **Strong** | Strength modification depending upon classification of previously established variant (pathogenic vs. likely pathogenic). Previously established variant must be classified using the SCID VCEP specifications for IL2RG. *(Modification Type: General recommendation, Strength)* |
| **Moderate** | Strength modification depending upon classification of previously established variant (pathogenic vs. likely pathogenic). Previously established variant must be classified using the SCID VCEP specifications for IL2RG. *(Modification Type: General recommendation, Strength)* |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

The following guidelines should be used when determining the phenotypic consistency of each proband at https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf

- "Phenotype highly specific for gene": proband must meet at least PP4_Moderate criteria;
- "Phenotype consistent with gene but not highly specific": proband must meet PP4 criteria;
- "Phenotype consistent with gene but not highly specific and high genetic heterogeneity": proband has been asserted to have a SCID phenotype but does not meet PP4 criteria;
- Reduce points per proband by half if the phase is unconfirmed.
- **Unaffected carrier females must have an affected child and maternity and paternity must be confirmed.** *(X-linked-specific rule.)*

**Recommendation for determining the appropriate ACMG/AMP evidence strength level for de novo occurences** *(source spelling "occurences" preserved)*:

| Strength code | Points |
|---------------|--------|
| PS2_Supporting | 0.5 |
| PS2_Moderate | 1 |
| PS2_Strong | 2 |
| PS2_VeryStrong | 4 |

This total-point ladder **is present in the source specification** (page 4 of the main PDF) and corresponds to Table 2 of the distributed SVI de novo document ([Appendix B](#appendix-b-svi-de-novo-recommendation-ps2--pm6-version-11)).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Use ClinGen SVI recommendations for de novo criteria (https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf). Phenotypic consistency determined using points-based system defined in PP4. *(Modification Type: Disease-specific, Strength)* |
| **Strong** | Same text as above. *(Modification Type: Disease-specific, Strength)* |
| **Moderate** | Same text as above. *(Modification Type: Disease-specific, Strength)* |
| **Supporting** | Same text as above. *(Modification Type: Disease-specific, Strength)* |

**Per-proband point values** (Table 1 of the distributed SVI document, [Appendix B](#appendix-b-svi-de-novo-recommendation-ps2--pm6-version-11)) are supplied by that supplementary file, not authored by the VCEP; the VCEP supplies only the mapping of the three phenotypic-consistency tiers onto its own PP4 thresholds (above).

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

- PS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and recapitulating the IL2RG-SCID phenotype. Animal models will be reviewed on a case-by-case basis by the VCEP to determine the appropriate strength level.
- PS3_Supporting can be applied based on an abnormal result in at least one approved in vitro assay.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | PS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and recapitulating the IL2RG-SCID phenotype. *(Modification Type: Disease-specific, Strength)* |
| **Moderate** | Not specified by VCEP. |
| **Supporting** | Strength modification based on an abnormal result in at least one approved in vitro assay. *(Modification Type: Disease-specific, Strength)* |

#### Approved Assay Instances

Listed verbatim in the specification under both the VCEP Specifications block and the Supporting strength block:

| Assay class | Supporting publication(s) |
|-------------|---------------------------|
| Phosphorylation of JAK3 / Co-Immunoprecipitation with JAK3 | Sharfe et al., 1997 (PMID: 9399950); Kumaki et al., 1999 (PMID: 9933465); Arcas-García et al., 2020 (PMID: 31799703) |
| Cytokine binding | Sharfe et al., 1997 (PMID: 9399950); Kumaki et al., 1995 (PMID: 7632950) |
| Surface expression of the gamma chain | Kumaki et al., 1995 (PMID: 7632950) |
| Interaction profiling-BioID | Tuovinen et al., 2020 (PMID: 32072341) |

Assay-instance detail (materials, controls, readouts, thresholds, variants tested, and one **non-approved** assay) is in [Appendix E](#appendix-e-ps3bs3-functional-evidence-assay-instance-detail).

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls. Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance. Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**

When the variant has been detected in multiple affected unrelated individuals, count the number of probands, **excluding the proband used to satisfy the PP4 criteria**:

| Strength code | Probands |
|---------------|----------|
| PS4_Supporting | 1 proband |
| PS4_Moderate | 2 probands |
| PS4_Strong | 3 probands |
| PS4_VeryStrong | ≥4 probands (inclusive) |

**Caveats:**
- Variant must be sufficiently rare (meet PM2 specification);
- Proband must fulfill the diagnostic criteria for SCID as per the PIDTC 2022 guidelines.

#### Strength Levels as printed in the per-strength blocks

| Strength | Criteria (verbatim) |
|----------|---------------------|
| **Very Strong** | Sum of case scores >16 points (see instructions below) *(Modification Type: Gene-specific, Strength)* |
| **Strong** | Sum of case scores 4.5-16 points (see instructions below) *(Modification Type: Gene-specific, Strength)* |
| **Moderate** | Sum of case scores 2.5-4 points (see instructions below) *(Modification Type: Gene-specific, Strength)* |
| **Supporting** | Sum of case scores 1-2 points (see instructions below) *(Modification Type: Gene-specific, Strength)* |

> **Unresolved conflict — do not silently reconcile.** The PS4 VCEP Specifications block defines strength by a **proband count** (1 / 2 / 3 / ≥4). The four per-strength blocks instead define strength by a **"sum of case scores" point range** (1–2 / 2.5–4 / 4.5–16 / >16). The specification package contains **no case-score point table and no "instructions below"** for PS4; no supplementary file supplies one. The referenced scoring instructions are therefore **absent from this specification package**. See [Section 5](#internal-inconsistencies-and-apparent-source-errors).

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

**Upgraded to PM1_Strong.** Defined to include missense alterations of the following positions:

| Category | Positions (verbatim) |
|----------|----------------------|
| Affecting a conserved cysteine residue | Cys62, Cys72, Cys102, Cys115 |
| Affecting CpG dinucleotides | c.684C (Arg224), c.690C (Arg226), **c.691G (Arg691)**, c.868G (Arg285) (PMID: 7668284) |
| Affecting the WSxWS motif | Trp237, Ser238, Glu239, Trp240, Ser241 |
| Affecting a transmembrane domain residue by introducing a charged or polar residue (Asn, Asp, Arg, Cys, His, Glu, Gln, Lys, Ser, Thr, Tyr) | amino acids 263-283 |

**Caveats:**
- Variant must also meet PM2.
- Variant must not meet BS1, BS2, or BA1 criteria.

| Strength | Criteria |
|----------|----------|
| **Strong** | Defined to include IL2RG-specific hot spots and functional domains. Caveat: Variant must not meet BS1, BS2, or BA1 criteria. *(Modification Type: Gene-specific, Strength)* |

*Source values preserved verbatim. "c.691G (Arg691)" is transcribed exactly as printed and appears to be an error (see [Section 5](#internal-inconsistencies-and-apparent-source-errors)). The WSxWS residue list as printed is Trp-Ser-Glu-Trp-Ser, i.e. the "x" position is given as Glu239.*

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

**Downgraded to PM2_Supporting.**

| Parameter | Value | Comparator |
|-----------|-------|------------|
| gnomAD popmax filtering allele frequency | 0.000124 | **strict less-than (`<`)** — "gnomAD popmax filtering allele frequency <0.000124" |
| Hemizygote requirement | "Additional requirement that no hemizygotes have been observed in gnomAD." | zero hemizygotes |

| Strength | Criteria (verbatim from the per-strength block) |
|----------|--------------------------------------------------|
| **Supporting** | "Strength modification based on an abnormal result in at least one approved in vitro assay." *(Modification Type: Disease-specific, Strength)* |

> The PM2 Supporting block text is copied from PS3 and does not describe PM2. Transcribed verbatim and flagged in [Section 5](#internal-inconsistencies-and-apparent-source-errors); the operative PM2 rule is the frequency threshold plus hemizygote requirement above.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary (as printed twice in the source, once with lost word spacing):** "Forrecessivedisordersdetectedintranswithapathogenicvariant" / "For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase."

**VCEP Specifications:** **Not Applicable.** Comments: "Does not apply."

No PM3 point system exists in this specification. IL2RG is X-linked; the VCEP does not define in-trans or biallelic evidence for this gene. Any PM3 point table (e.g. the 0.5/1/2/4-per-occurrence tables used by autosomal-recessive SCID gene specifications) must **not** be applied here.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

When applied to deletion variants, the deleted region must contain a known pathogenic or likely pathogenic variant that is not predicted/observed to alter splicing in order to apply PM4 at the default strength, or contain a variant of uncertain significance not predicted/observed to alter splicing in order to apply PM4 at the reduced strength of PM4_Supporting.

| Strength | Criteria |
|----------|----------|
| **Moderate** | Additional requirement that deletion variants must contain a known pathogenic variant, likely pathogenic variant, or variant of uncertain significance that is not predicted/observed to alter splicing in order to apply PM4, with the strength of evidence dependent upon the classification of the variant contained within the deletion. *(Modification Type: General recommendation, Strength)* |
| **Supporting** | Identical text to the Moderate block. *(Modification Type: General recommendation, Strength)* |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications (nonsense-variant point system — updated in v2.2):**

- **PM5_Strong** — PM5 may be applied at a Strong level of evidence for any nonsense variant with **4+ points** from informative variants (see point table). PM5_Strong should be downgraded to PM5_Moderate if PVS1 is applied at any strength.
- **PM5_Moderate** — PM5 may also be applied at a Moderate level of evidence for any nonsense variant with **2+ points** from informative variants. PM5_Moderate may not be combined with PVS1_VeryStrong (should be downgraded to PM5_Supporting if PVS1_VeryStrong is applied).
- **PM5_Supporting** — Also applicable to a nonsense variant with **1 point** from an informative variant. Informative variants must also be classified by these rule specifications.

#### PM5 Point Table (verbatim)

| Type of variant under assessment (VUA) | Informative variant | Score |
|----------------------------------------|---------------------|-------|
| Nonsense variant predicted to lead to NMD | P/LP variant in the exon of DNA change predicted to lead to NMD | +1pt |
| Nonsense variant predicted to lead to NMD | B/LB variant in the exon predicted to lead to NMD | -2pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | P/LP variant resulting in a PTC in the same exon but downstream of VUA | +1pt |
| Nonsense variant, resulting in a PTC in the final exon, not predicted to lead to NMD | B/LB variant resulting in PTC in the same exon but upstream of the VUA | -2pt |

NMD = nonsense-mediated decay; PTC premature termination codon *(source omits "=" after PTC; preserved)*

**Notes (verbatim, repeated in every PM5 strength block):** The informative variant must be classified by the SCID VCEP specifications and may not be the same variant used to meet "+1 pathogenic variant downstream" on the PVS1 flowchart. If negative points are calculated, the curator should not apply PM5 and should reconsider if PVS1 is applicable for the VUA. The VUA must be sufficiently rare, meet PM2_Supporting, to apply this point system. If the informative variant is a frameshift or nonsense variant, it must reach classification as Pathogenic or Likely Pathogenic without use of PM5 and without use of only PVS1 plus PM2.

**Missense-variant PM5 (appears only in the Moderate and Supporting strength blocks):** "Applicable at default strength (PM5) if previously established variant is classified as pathogenic or at reduced strength of PM5_Supporting if previously established variant is classified as likely pathogenic."

*(Modification Type for all three PM5 blocks: General recommendation, Strength.)*

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

The following guidelines should be used when determining the phenotypic consistency of each proband at https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf

- "Phenotype highly specific for gene": proband must meet at least PP4_Moderate criteria;
- "Phenotype consistent with gene but not highly specific": proband must meet PP4 criteria;
- "Phenotype consistent with gene but not highly specific and high genetic heterogeneity": proband has been asserted to have a SCID phenotype but does not meet PP4 criteria;
- Reduce points per proband by half if the phase is unconfirmed.
- **Unaffected carrier females must have an affected child and maternity and paternity must be confirmed.** *(X-linked-specific rule.)*

**Recommendation for determining the appropriate ACMG/AMP evidence strength level for de novo occurences:**

| Strength code | Points |
|---------------|--------|
| PM6_Supporting | 0.5 |
| PM6_Moderate | 1 |
| PM6_Strong | 2 |
| PM6_VeryStrong | 4 |

This ladder **is present in the source specification** (page 11 of the main PDF).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | No separate Very Strong block is printed for PM6 in the specification, although PM6_VeryStrong = 4 points appears in the ladder above. Not specified further by VCEP. |
| **Strong** | Use ClinGen SVI recommendations for de novo criteria (link above). Phenotypic consistency determined using points-based system defined in PP4. *(Modification Type: Disease-specific, Strength)* |
| **Moderate** | Same text. *(Modification Type: Disease-specific, Strength)* |
| **Supporting** | Same text. *(Modification Type: Disease-specific, Strength)* |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386).

Recommendation for determining the appropriate evidence strength level for PP1:

| Strength code | Threshold |
|---------------|-----------|
| PP1 | 2 affected segregations (not including the proband) |
| PP1_Moderate | 4 affected segregations (not including the proband) |
| PP1_Strong | 5 affected segregations (not including the proband) |

| Strength | Criteria |
|----------|----------|
| **Strong** | Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386), with strength dependent on number of affected segregations (see list above). *(Modification Type: General recommendation, Strength)* |
| **Moderate** | Same text. *(Modification Type: General recommendation, Strength)* |
| **Supporting** | Same text. *(Modification Type: General recommendation, Strength)* |

The distributed `PP1.pdf` supplies Oza et al. Tables 4a and 4b — see [Appendix C](#appendix-c-pp1-segregation-tables-oza-et-al-tables-4a-and-4b). The VCEP's 2 / 4 / 5 thresholds match the **autosomal dominant** row of Table 4a. The VCEP does not state which Oza row it intends for an X-linked gene, and Table 4b (autosomal recessive) is distributed but never referenced by the VCEP text. See [Section 5](#internal-inconsistencies-and-apparent-source-errors).

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable.** Comments: "Does not apply. The gnomAD v2.1.1 missense Z score for IL2RG (Z = 1.49) suggests this gene is not constrained for missense variation. Both benign and pathogenic missense variants are present in IL2RG."

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Only applicable to synonymous or intronic variants predicted to impact splicing by SpliceAI with a delta score **greater than or equal to 0.2** (inclusive `≥`). **Do not apply to missense variants.** *(Modification Type: General recommendation)* |

No other strength level is specified for PP3.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

PP4 applicability and strength is determined by the total points accumulated by a **single affected individual** according to the table below and the following total point ranges:

| Total points | Outcome | Comparators |
|--------------|---------|-------------|
| <1 point | PP4 not met | strict `<` |
| 1 – <2.5 points | PP4 (Supporting) | inclusive lower bound, strict upper bound |
| 2.5 – <6 points | PP4_Moderate | inclusive lower bound, strict upper bound |
| ≥6 points | PP4_Strong | inclusive `≥` |

#### PP4 Evidence Point Table

*(Reproduced from the main specification; the distributed `PP4 - IL2RG.pdf` gives the same table — differences between the two renderings are flagged in [Section 5](#internal-inconsistencies-and-apparent-source-errors). Wording below follows the standalone PP4 supplement, which is the VCEP's own document for this criterion.)*

| Evidence Description | Points |
|----------------------|--------|
| Diagnostic criteria met for SCID (Criteria 1 and 3 or Criterion 4 by itself) or Leaky SCID/Omenn syndrome (excluding Criterion 2)<sup>2</sup> | 0.5 |
| SCID gene panel or exome/genome sequencing conducted (only applicable if genetic testing did not provide an alternative genetic explanation for SCID/Leaky SCID/Omenn syndrome phenotype) | 1 |
| Family history of SCID (only applicable if SCID gene panel or exome/genome sequencing was conducted on proband and did not provide an alternative genetic explanation for phenotype) | 0.5 |
| Absent CD132 expression (demonstrated by RT-PCR, Western blot, flow cytometry) | 4.5 |
| Reduced CD132 expression (demonstrated by RT-PCR, Western blot or flow cytometry) as established by the laboratory | 3 |
| Reduced IL-2-induced phosphorylation of JAK3 or STAT5 in patient-derived cells as established by the laboratory AND pathogenic or likely pathogenic variants in JAK3, STAT5A, STAT5B, IL2RA, and IL2RB **have been excluded** PMID: 10794431, 31799703, 32072341 | 3 |
| Reduced IL-2-induced phosphorylation of JAK3 or STAT5 in patient-derived cells as established by the laboratory AND pathogenic or likely pathogenic variants in JAK3, STAT5A, STAT5B, IL2RA, and IL2RB **have NOT been excluded** PMID: 10794431, 31799703, 32072341 | 1.5 |
| Reduced **IL-21**-induced phosphorylation of STAT3 in total lymphocytes or B cells as established by the laboratory AND pathogenic or likely pathogenic variants in JAK3, STAT3, and IL21R **have been excluded** PMID: 25042067, 32072341 | 3 |
| Reduced **IL-21**-induced phosphorylation of STAT3 in total lymphocytes or B cells as established by the laboratory AND pathogenic or likely pathogenic variants in JAK3, STAT3, and IL21R **have NOT been excluded** PMID: 25042067, 32072341 | 1.5 |
| SCID phenotype corrected by IL2RG gene therapy **WITHOUT** CNV testing performed | 4.5 |
| SCID phenotype corrected by IL2RG gene therapy **WITH** CNV testing performed | 6 |
| T-B+ lymphocyte subset profile* (See notes) | 0.5 |
| NK cells below the normal reference range or absent | 1 |

**Footnote 1 (PP4 supplement wording):** CNV (Copy number variation) testing is required to consider PP4_Strong in order to certify that the variant in question is the causative for the phenotype, and not one CNV event corrected by gene therapy and not identified previously. *(Source grammar "is the causative for the phenotype" preserved.)*

**Footnote 1 (main specification wording):** CNV (Copy number variation) testing is required **if PP4_Strong cannot be reached without points from gene therapy** in order to certify that the variant in question is causative for the phenotype, and not one CNV event corrected by gene therapy and not previously identified.

**Footnote 2:** The diagnostic criteria should follow the PIDTC 2022 specification, summarized [here] (hyperlink target not resolvable from the distributed PDF).

**Notes:** 1) If NK cells are not noted or are present, criteria may still be applied if SCID gene panel or exome/genome sequencing has ruled out alternative causes; 2) If maternal T cells are present, the T lymphocyte profile is still considered to be T- (autologous T cells are absent).

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Strong** | A patient score of ≥ 6 points. CNV testing is required if PP4_Strong cannot be reached without points from gene therapy in order to certify that the variant in question is causative for the phenotype, and not one CNV event corrected by gene therapy and not previously identified. *(Modification Type: Disease-specific, Gene-specific)* |
| **Moderate** | A patient score of ≥2.5-<6 points. *(Modification Type: Disease-specific, Strength)* |
| **Supporting** | A patient score of 1-<2.5 points. *(Modification Type: Disease-specific, Strength)* |

---

### PP5 - Reputable Source

**VCEP Specifications:** **Not Applicable.** "This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. PubMed: 29543229"

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:** Common in population databases.

| Parameter | Value | Comparator |
|-----------|-------|------------|
| gnomAD popmax filtering allele frequency | 0.01110 | **strict greater-than (`>`)** — "gnomAD popmax filtering allele frequency >0.01110" |

Maximum credible population allele frequency threshold determined using the Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:

| Parameter | Value |
|-----------|-------|
| Prevalence | 1:5,000 |
| Allelic heterogeneity | 1 |
| Genetic heterogeneity | 0.31 (based on the contribution of IL2RG variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 30.8%, rounded to 31%) |
| Penetrance | 50% |

| Strength | Criteria |
|----------|----------|
| **Stand Alone** | gnomAD popmax filtering allele frequency >0.01110. *(Modification Type: Disease-specific)* |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

| Parameter | Value | Comparator |
|-----------|-------|------------|
| gnomAD popmax filtering allele frequency | 0.00249 | **strict greater-than (`>`)** — "gnomAD popmax filtering allele frequency >0.00249" |

Maximum credible population allele frequency threshold determined using the Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:

| Parameter | Value |
|-----------|-------|
| Prevalence | 1:50,000 |
| Allelic heterogeneity | 1 |
| Genetic heterogeneity | 0.31 (based on the contribution of IL2RG variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 30.8%, rounded to 31%) |
| Penetrance | 100% |

Additional instruction: "Consider bottleneck populations."

| Strength | Criteria |
|----------|----------|
| **Strong** | gnomAD popmax filtering allele frequency >0.00249. Consider bottleneck populations. *(Modification Type: Disease-specific)* |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications (X-linked — hemizygote based):**

| Strength code | Rule | Comparator |
|---------------|------|------------|
| BS2_Strong | Observed in >=3 (3 or more) hemizygotes in gnomAD | **inclusive (`≥3`)**, stated both symbolically and in words |
| BS2_Supporting | Can be applied at Supporting level of evidence if observed at least 2 hemizygotes in gnomAD | **inclusive (`≥2`)** as printed ("at least 2") |

| Strength | Criteria |
|----------|----------|
| **Strong** | BS2_Strong: Observed in >=3 (3 or more) hemizygotes in gnomAD. *(Modification Type: Gene-specific, Strength)* |
| **Supporting** | BS2_Supporting: Can be applied at Supporting level of evidence if observed at least 2 hemizygotes in gnomAD. *(Modification Type: Gene-specific)* |

*As literally printed, the two bands overlap: a variant seen in ≥3 hemizygotes also satisfies "at least 2". The VCEP does not state that the Supporting band is exactly 2. Transcribed as printed; flagged in [Section 5](#internal-inconsistencies-and-apparent-source-errors).*

**Note on grammar:** the source reads "if observed at least 2 hemizygotes" (missing "in"). Preserved.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** **Not Applicable.** Comments: "Does not apply."

*Note: the distributed functional-evidence workbook is titled "SCID VCEP PS3_BS3 Functional Evidence" and the spec's file list labels it for IL2RG, yet BS3 is declared not applicable for IL2RG and the workbook's "Proposed strength" row lists only PS3_Supporting values. Flagged in [Section 5](#internal-inconsistencies-and-apparent-source-errors).*

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:** Can be applied without additional specifications.

| Strength | Criteria |
|----------|----------|
| **Strong** | Can be applied without additional specifications. *(Modification Type: None)* |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment (verbatim) |
|-----------|--------|--------------------|
| **BP1** | Not Applicable | "Does not apply. IL2RG missense variants are a known mechanism of disease." |
| **BP2** | Not Applicable | "Does not apply." |
| **BP3** | Not Applicable | "Does not apply." |
| **BP4** | Not Applicable | "Does not apply." |
| **BP5** | Not Applicable | "Does not apply." |
| **BP6** | Not Applicable | "This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. PubMed: 29543229" |
| **BP7** | **Specified (Supporting)** | See below. |

#### BP7 - Synonymous / Deep Intronic

**VCEP Specifications:**
- Applicable to both synonymous variants and deep intronic variants affecting nucleotides at or beyond the **+7 (donor)** and **−21 (acceptor)** positions (inclusive — "at or beyond").
- The variant should be predicted not to impact splicing by at least **two out of three** in silico tools (freely available tools include GeneSplicer, MaxEntScan, NNSplice, SpliceAI, Splicing Sequences Finder (SSF), and varSEAK).
- Given the potential for poor conservation of genes related to T cell and B cell development among vertebrates, nucleotide conservation is **not** required in order to apply BP7.

| Strength | Criteria |
|----------|----------|
| **Supporting** | Applicable to both synonymous variants and deep intronic variants affecting nucleotides at or beyond the +7 (donor) and -21 (acceptor) positions. Given the potential for poor conservation of genes related to T cell and B cell development among vertebrates, nucleotide conservation is not required in order to apply BP7. *(Modification Type: General recommendation, Gene-specific)* |

*Note: the "two out of three in silico tools" requirement appears only in the VCEP Specifications block and is absent from the Supporting strength block. The list offered as "three" tools names six. Both preserved as printed and flagged in [Section 5](#internal-inconsistencies-and-apparent-source-errors).*

---

## Rules for Combining Criteria

This section is transcribed verbatim from the "Rules for Combining Criteria" pages of the specification (pages 18–19). It is source content, not a template default.

### Pathogenic

| # | Combination |
|---|-------------|
| 1 | 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong) AND ≥ 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM1_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong) |
| 2 | 1 Very Strong AND ≥ 2 Moderate (PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate) |
| 3 | 1 Very Strong AND 1 Moderate AND 1 Supporting (PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4) |
| 4 | 1 Very Strong AND ≥ 2 Supporting |
| 5 | ≥ 2 Strong |
| 6 | 1 Strong AND ≥ 3 Moderate |
| 7 | 1 Strong AND 2 Moderate AND ≥ 2 Supporting |
| 8 | 1 Strong AND 1 Moderate AND ≥ 4 Supporting |

### Likely Pathogenic

| # | Combination |
|---|-------------|
| 1 | 1 Very Strong AND 1 Moderate |
| 2 | 1 Strong AND 1 Moderate |
| 3 | 1 Strong AND ≥ 2 Supporting |
| 4 | ≥ 3 Moderate |
| 5 | 2 Moderate AND ≥ 2 Supporting |
| 6 | 1 Moderate AND ≥ 4 Supporting |
| 7 | 1 Strong AND 2 Moderate |
| 8 | 1 Very Strong AND 1 Supporting |

### Benign

| # | Combination |
|---|-------------|
| 1 | ≥ 2 Strong (BS1, BS2, BS4) |
| 2 | 1 Stand Alone (BA1) |

### Likely Benign

| # | Combination |
|---|-------------|
| 1 | ≥ 2 Supporting (BS2_Supporting, BP7) |
| 2 | 1 Strong (BS1, BS2, BS4) |

### Evidence-code membership of each strength tier (as printed with every rule)

| Tier | Codes |
|------|-------|
| **Very Strong** | PVS1, PS2_Very Strong, PS4_Very Strong |
| **Strong** | PVS1_Strong, PS1, PS2, PS3, PS4, PM1_Strong, PM5_Strong, PM6_Strong, PP1_Strong, PP4_Strong |
| **Moderate** | PVS1_Moderate, PS1_Moderate, PS2_Moderate, PS4_Moderate, PM4, PM5, PM6, PP1_Moderate, PP4_Moderate |
| **Supporting** | PVS1_Supporting, PS2_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PM5_Supporting, PM6_Supporting, PP1, PP3, PP4 |
| **Benign Strong** | BS1, BS2, BS4 |
| **Benign Supporting** | BS2_Supporting, BP7 |
| **Stand Alone** | BA1 |

*Note: "Likely Pathogenic" rules 2 and 7 are both listed even though rule 2 (1 Strong + 1 Moderate) subsumes rule 7 (1 Strong + 2 Moderate). Preserved as printed. Note also that PM1 appears in the tier lists only as PM1_Strong, and PM6_VeryStrong does not appear in the Very Strong tier list even though the PM6 section defines a PM6_VeryStrong = 4 points level. Flagged in [Section 5](#internal-inconsistencies-and-apparent-source-errors).*

---

## Appendices

### Appendix A: IL2RG PVS1 Decision Tree

Transcribed from `PVS1.pdf` (single page, labeled "IL2RG"), read both as extracted text and as a rendered page image. The IL2RG-specific content (highlighted in the source) is: the **transmembrane domain begins at amino acid 255**, and the NMD boundary is the **last exon or the last 50 nucleotides of the penultimate exon [c.874 (codon 292) in exon 7]**.

#### Branch 1 — Nonsense or Frameshift

| Path | Outcome |
|------|---------|
| Predicted to undergo NMD <sup>b</sup> → Exon is present in biologically-relevant transcript(s) | **PVS1** |
| Predicted to undergo NMD <sup>b</sup> → Exon is absent from biologically-relevant transcript(s) | **N/A** |
| Not predicted to undergo NMD <sup>b</sup> (i.e. premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon [c.874 (codon 292) in exon 7]) → Truncated/altered region is critical to protein function – causes truncation of the transmembrane domain (which begins at amino acid 255) or any distal region (i.e. cytoplasmic domain) | **PVS1** |
| Not predicted to undergo NMD → Role of region in protein function is unknown → LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) | **N/A** |
| Not predicted to undergo NMD → Role unknown → LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) → Variant removes >10% of protein → 1+ pathogenic variant present downstream | **PVS1_Strong** |
| …same → Variant removes >10% of protein → No known downstream pathogenic variants | **PVS1_Moderate** |
| …same → Variant removes <10% of protein | **PVS1_Moderate** |

#### Branch 2 — GT--AG 1,2 splice sites <sup>a</sup>

| Path | Outcome |
|------|---------|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD <sup>b</sup> → Exon is present in biologically-relevant transcript(s) | **PVS1** |
| …→ Exon is absent from biologically-relevant transcript(s) | **N/A** |
| Exon skipping or cryptic splice site disrupts reading frame and is **NOT** predicted to undergo NMD <sup>b</sup> (i.e. premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon [c.874 (codon 292) in exon 7]) → Truncated/altered region is critical to protein function (truncation of the transmembrane domain beginning at aa 255, or any distal region) | **PVS1** |
| …→ Role of region unknown → LoF variants frequent in general population and/or exon absent from biologically-relevant transcript(s) | **N/A** |
| …→ Role unknown → LoF variants not frequent and exon present → removes >10% of protein → 1+ pathogenic variant present downstream | **PVS1_Strong** |
| …→ removes >10% of protein → No known downstream pathogenic variants | **PVS1_Moderate** |
| …→ removes <10% of protein | **PVS1_Moderate** |
| Exon skipping or use of a cryptic splice site **preserves reading frame** → Truncated/altered region is critical to protein function (transmembrane domain from aa 255 or distal) | **PVS1** |
| …preserves reading frame → Role unknown → LoF variants frequent and/or exon absent | **N/A** |
| …preserves reading frame → Role unknown → LoF not frequent and exon present → removes >10% of protein → 1+ pathogenic variant present within deleted region | **PVS1_Strong** |
| …→ removes >10% of protein → No known pathogenic variants within deleted region | **PVS1_Moderate** |
| …→ removes <10% of protein | **PVS1_Moderate** |

#### Branch 3 — Deletion (single exon to full gene)

| Path | Outcome |
|------|---------|
| Full gene deletion | **PVS1** <sup>d</sup> |
| Single to multi exon deletion – disrupts reading frame and is predicted to undergo NMD <sup>b</sup> → Exon is present in biologically-relevant transcript(s) | **PVS1** |
| …→ Exon is absent from biologically-relevant transcript(s) | **N/A** |
| Single to multi exon deletion – disrupts reading frame and is **NOT** predicted to undergo NMD <sup>b</sup> (i.e. premature stop codon in the last exon or the last 50 nucleotides of the penultimate exon [c.874 (codon 292) in exon 7]) → Truncated/altered region is critical to protein function (transmembrane domain from aa 255 or distal) | **PVS1** |
| …→ Role of region unknown → LoF variants frequent and/or exon absent | **N/A** |
| …→ Role unknown → LoF not frequent and exon present → removes >10% of protein → 1+ pathogenic variant present within deleted region | **PVS1_Strong** |
| …→ removes >10% of protein → No known pathogenic variants within deleted region | **PVS1_Moderate** |
| …→ removes <10% of protein | **PVS1_Moderate** |
| Single to multi exon deletion – **preserves reading frame** → Truncated/altered region is critical to protein function (transmembrane domain from aa 255 or distal) | **PVS1** |
| …preserves reading frame → Role unknown → (same three sub-outcomes as immediately above) | **N/A / PVS1_Strong / PVS1_Moderate / PVS1_Moderate** |

#### Branch 4 — Duplication (≥1 exon in size and must be completely contained within gene)

| Path | Outcome |
|------|---------|
| Proven in tandem → Reading frame disrupted and NMD predicted to occur | **PVS1** |
| Proven in tandem / Presumed in tandem → No or unknown impact on reading frame and NMD | **N/A** |
| Presumed in tandem → Reading frame presumed disrupted and NMD predicted to occur | **PVS1_Strong** |
| Proven not in tandem | **N/A** |

#### Branch 5 — Initiation Codon

| Path | Outcome |
|------|---------|
| No known alternative start codon in other transcripts → ≥1 pathogenic variant(s) upstream of closest potential in-frame start codon | **PVS1_Moderate** |
| No known alternative start codon in other transcripts → No pathogenic variant(s) upstream of closest potential in-frame start codon | **PVS1_Supp** |
| Different functional transcript uses alternative start codon | **N/A** |

**Footnote markers `a`, `b`, and `d` appear on the flowchart but no footnote legend is printed anywhere on the distributed page.** Their definitions are therefore not available in this specification package; they are not reproduced or guessed here.

---

### Appendix B: SVI De Novo Recommendation (PS2 / PM6), Version 1.1

Transcribed from `PS2_PM6.pdf`. This is a **ClinGen SVI Working Group** document distributed with the specification, dated "March 18, 2018, updated May 5, 2021". Changes from v1: "Clarified that confirmed/assumed is with regards to parental relationships and not de novo status."

The SVI proposes a point-based system based on three parameters: confirmed vs. assumed parental relationships; phenotypic consistency; number of de novo observations.

#### Table 1. Points* awarded per de novo occurrence

| Phenotypic consistency | de novo with confirmed parental relationships | de novo with unconfirmed parental relationships |
|---|---|---|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity** | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

\* Note that these points are not equivalent to the points used to classify a variant per the Tavtigian et al 2020 "Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines"
\*\* Maximum allowable value of 1 may contribute to overall score

#### Table 2. Recommendation for determining the appropriate ACMG/AMP evidence strength level for de novo occurrence(s)

| Supporting (PS2_Supporting or PM6_Supporting) | Moderate (PS2_Moderate or PM6) | Strong (PS2 or PM6_Strong) | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |
|---|---|---|---|
| 0.5 | 1 | 2 | 4 |

If the parents have not been tested for parentage or for the variant, no points should be awarded.

#### Additional considerations for applying de novo criteria based on inheritance (verbatim)

- **Conditions with X-linked inheritance:** if the variant occurs de novo in an unaffected carrier mother, and family history is consistent - i.e., she has no affected brothers/other male relatives apart from her affected son(s) – de novo criteria may be applied despite the fact that she is unaffected.
- **Autosomal recessive conditions:** for a de novo occurrence in a gene associated with a condition inherited in an autosomal recessive pattern without an additional pathogenic/likely pathogenic variant identified, the strength of evidence should be decreased by one level. *(Not applicable to IL2RG, which is X-linked.)*
- **Mosaicism:** for cases with apparent germline mosaicism (multiple affected siblings with both parents negative for the variant), parental relationships must be confirmed in order for de novo criteria to apply.

---

### Appendix C: PP1 Segregation Tables (Oza et al., Tables 4a and 4b)

Transcribed from `PP1.pdf`. Source header: "Oza et al., Hum Mutat. Author manuscript; available in PMC 2019 November 01."

#### Table 4a: Recommendations for PP1 (segregation evidence) — General Recommendations

| | Supporting | Moderate | Strong |
|---|---|---|---|
| **Likelihood** | 4:1 | 16:1 | 32:1 |
| **LOD Score** | 0.6 | 1.2 | 1.5 |
| **Autosomal dominant threshold** | 2 affected segregations | 4 affected segregations | 5 affected segregations |
| **Autosomal recessive threshold** | See Table 4b | See Table 4b | See Table 4b |

The VCEP's stated IL2RG thresholds (PP1 = 2, PP1_Moderate = 4, PP1_Strong = 5 affected segregations, not including the proband) correspond numerically to the autosomal dominant row.

#### Table 4b: Recommendations for autosomal recessive segregation evidence (PP1) — General Recommendations (Phenocopy not an issue)

LOD score by affected segregations (rows) × unaffected recessive segregations (columns):

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

Table 4b legend (verbatim): "Affected segregations are counted in rows and unaffected segregations in columns. Affected segregations are affected family members in whom biallelic compound heterozygous or homozygous variants segregates. Unaffected segregations are defined as unaffected family members, typically siblings, who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants identified in the proband, or a heterozygous carrier for a single variant. Unaffected, carrier parents DO NOT count as unaffected segregations. There may be scenarios where individuals other than siblings could be counted as segregations, such as in families where one parent is affected with the autosomal recessive disorder, in large families with multiple branches, or in consanguineous families. Each cell shows the LOD score of each combination of affected and unaffected segregations. LOD scores were calculated using a simplified LOD score formula, as described in Strande et al., 2017."

**Applicability note:** Table 4b is written for **autosomal recessive** biallelic segregation. IL2RG is X-linked and the VCEP's PP1 rule does not reference Table 4b. Table 4b is reproduced here only because it is part of the distributed file; the VCEP gives no instruction for using it with IL2RG.

---

### Appendix D: PP4 Points Table (standalone supplement)

The full contents of `PP4 - IL2RG.pdf` are transcribed inline in the [PP4 section](#pp4---phenotype-specificity) above, including both footnotes and the notes block. The supplement contains no content beyond that table, its point ranges, and its footnotes. The specification's file list describes this file as "PP4 - IL2RG: 2025 updates".

---

### Appendix E: PS3/BS3 Functional Evidence — Assay Instance Detail

Transcribed from `SCID VCEP PS3_BS3 Functional Evidence.xlsx`, sheet **"IL2RG Assay Instance Details"** (the workbook contains exactly one sheet). The sheet is laid out with attributes in column A and one **assay instance per column** (B–I). This is a **per-assay-instance lookup**, not a variant-level classification table; all eight instances are reproduced below in full because the sheet is small.

| Attribute | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|
| **PMID** | 24853770 | 9399950 | 9933465 | 31799703 | 9399950 | 7632950 | 7632950 | 32072341 |
| **Gene** | IL2RG | IL2RG | IL2RG | IL2RG | IL2RG | IL2RG | IL2RG | IL2RG |
| **DOI / link** | 10.1038/srep05043 | 10.1172/JCI119858 | 10.1046/j.1365-2249.1999.00792.x | 10.1111/cei.13405 | 10.1172/JCI119858 | pubmed.ncbi.nlm.nih.gov/7632950/ | pubmed.ncbi.nlm.nih.gov/7632950/ | 10.1007/s10875-020-00745-2 |
| **Author** | Matsubara...Asahara | Sharfe...Roifman | Kumaki, H D Ochs... Baumann | Arcas-García...Franco-Jarava | Sharfe...Roifman | Kumaki...Giri | Kumaki...Giri | Tuovinen... Seppänen |
| **Year** | 2014 | 1997 | 1999 | 2020 | 1997 | 1995 | 1995 | 2020 |
| **General Class of Assay** | IL-2-induced expression of downstream targets | IL-2-induced Jak-3 phosphorylation assay | JAK3 association by immunoprecipitation | JAK3 association by immunoprecipitation | Cytokine binding | Cytokine binding | Surface expression of the gamma chain | Interaction profiling-BioID |
| **Readout type** | Quantitative | Semi-quantitative | Semi-quantitative | Semi-quantitative | Semi-quantitative | Semi-quantitative | Semi-quantitative | Quantitative |
| **Readout description** | BCL2 expression normalized to β-actin and relative to non-stimulated cells | Presence/intensity of band corresponding to Jak3 tyrosine phosphorylation | Presence/intensity of band corresponding to Jak3 tyrosine phosphorylation | Presence/intensity of band corresponding to Jak3 tyrosine phosphorylation | Binding change/protein interaction compared to wild type IL2RG | Binding change/protein interaction compared to wild type IL2RG | Expression of the mutant chain by an IL-2 receptor monoclonal antibody stained in the cell surface. | Fold change in protein interaction compared to wild type IL2RG |
| **Biological replicates** | None (not met) | Not reported | Not reported | Not reported | Not reported | Not reported | Not reported | None (not met) |
| **Technical replicates** | 3 | Not reported | Not reported | Not reported | Not reported | Not reported | Not reported | 2 |
| **Basic positive control** | Control Jurkat cells (wild type IL2RG) | COS-7 cells expressing wild type IL-2Rγ | COS-1 cells expressing wild type IL-2Rγ and Beta Actin | COS-7 cells expressing wild type IL-2Rγ | control EBV cell lines | COS-7 cell expressing WT γ chain. | COS-7 cell expressing WT γ chain. | Wild type IL2RG-expressing cells |
| **Basic negative control** | Not reported | Untransfected COS-7 cells | Not reported | Not reported | Empty vector-transduced cells | Empty vector-transduced cells | Empty vector-transduced cells | Not reported |
| **Validation controls P/LP (#)** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Validation controls B/LB (#)** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **Statistical analysis** | Two-tailed Student's t-test | Not reported | Not reported | Not reported | Not reported | Not reported | Not reported | Student's t test |
| **Threshold for normal readout** | Wild type-like level of BCL2 expression (no numeric threshold given) | Wild type-like level of phosphorylated Jak3 | Wild type-like level of phosphorylated **Jak4** | Wild type-like level of phosphorylated **Jak5** | Wild type-like pattern of protein-protein interactions | Wild type-like pattern of protein-protein interactions = Binding and Internalization | The wild-type γ chain, which was clearly stained by TUGh4 on the transfected cells. | Wild type-like pattern of protein-protein interactions |
| **Threshold for abnormal readout** | Reduced level of BCL2 expression (no numeric threshold given) | Reduced level of phosphorylated Jak3 | Reduced level of phosphorylated Jak3 | Reduced level of phosphorylated Jak3 | Significantly altered pattern of binding indicative of affinity is reduced | Significantly altered pattern of binding indicative of affinity is reduced | The mutant chain could not be detected by an antihuman IL-2 receptor monoclonal antibody, TUGh4, on the cell surface of the transfected COS-7 cells. | Significantly altered pattern of protein-protein interactions indicative of mislocalization/inability to transport to cell surface |
| **Approved assay (y/n)** | **n** | y | y | y | y | y | y | y |
| **Proposed strength** | *(blank)* | PS3_Supporting | PS3_Supporting | PS3_Supporting | PS3_Supporting | PS3_Supporting | PS3_Supporting | PS3_Supporting |
| **Variant(s) Tested** | "del-2" and "del-3", deletions in the region containing the translational start codon | c.664C>T (p.Arg222Cys) | single nucleotide deletion at position 939 in the γc chain. The G deletion at 939 corresponds to the first base of exon 8, and results from g to a substitution at the last nucleotide of intron 7 | c.982C>T (p.Arg328Ter) | c.664C>T (p.Arg222Cys) | c.690C>T (p.Arg204Cys) | c.690C>T (p.Arg204Cys) | c.172C>T (p.Pro58Ser) |

**Full "Assay (General Description)" and "Material used" text** (row 8 and row 9), verbatim:

- **B (Matsubara 2014):** "Jurkat cells containing IL2RG variants generated by TALEN-mediated gene editing were stimulated with PMA and ionomycin in the presence of exogenous IL-2 and the expression of BCL2 (a downstream target of IL-2 signaling) was measured by qPCR 48 hours post-stimulation." Material: Jurkat cells containing IL2RG variants generated by TALEN-mediated gene editing.
- **C (Sharfe 1997):** "Expression vectors for a normal b+ γ, or b+ γR222C, and Jak3 were cotransfected into COS-7 cells and the level of Jak3 phosphorylation induced by low levels of IL-2 was examined by antiphosphotyrosine western blot of Jak3 immunoprecipitates. Lysate from each transfection was blotted with anti-Jak3 to ensure equal expression." Material: COS-7 cells transfected with wild type and variants generated by cDNA constructs.
- **D (Kumaki 1999):** "COS-1 cells were transfected with the wild-type γc chain, a truncated γc chain (γcΔ), the mutant γc chain obtained from the X-SCID patient or the vector control (409) and with Jak3. The transfected cells were lysed and immunoprecipitated with an anti-human γc chain MoAb, TUGh4, or isotype-matched control. (b) 10 microlitre aliquots of cell lysates from the transfected cells used in (a) were immunoblotted with Jak3 antiserum to compare the levels of Jak3 expression in the transfectants." Material: COS-1 transfected with a truncate form (γcΔ) from the patient and the wild-type γc chain. [Similar results were obtained using COS-7 cells (data not shown)].
- **E (Arcas-García 2020):** "Co-Immunoprecipitation of JAK3 with IL2RG R328X, Y325X and WT in COS-7 cells." Material: COs7 cells with variant generated with the GENEART Site-Directed Mutagenesis System (Invitrogen, Carlsbad, CA, USA) using the pEF6-IL2RGY325X-Myc construct as a template. *(Source spelling "COs7" preserved.)*
- **F (Sharfe 1997, cytokine binding):** "COS-7 cells were transfected with cDNA for an IL-2Rb chain in combination with either a normal IL-2Rg cDNA or cDNA for the patient IL-2Rg and binding of the IL-2 fluorokine analyzed." Material: COS-7 cells transfected with wild type and variants generated by cDNA constructs.
- **G (Kumaki 1995, cytokine binding):** "COS-7 cells were cotransfected with the empty expression vector, intact human IL-2 receptor γ chain cDNA (γ) or mutant γ chain cDNA of patient no. 1 (γ*), and the human IL-2 receptor β chain using the DEAE-dextran method. Results shown in pixel index: the ratio of total pixel counts of transfectants to cells transfected with the empty expression vector plus the β chain."
- **H (Kumaki 1995, surface expression):** "COS-7 cells transfected with an empty expression vector, pDC409, the intact γ chain cDNA, and the mutant γ chain cDNA of patient in pDC409. Shows surface expression of the γ chain in transfected COS7 cells. Intracellular distribution of the γ chain in COS7 cells. Cells were stained with TUGh4 or YOYO 1. YOYO-1 is for nucleic acid counterstaining." Material: COS7 transfected cells.
- **I (Tuovinen 2020):** "BioID proximity labeling was used to characterize interactions between wild type or variant IL2RG and other proteins known to be associated with the endoplasmic reticulum, ER-golgi, golgi, focal adhesion, cytosol, nucleus, or other cellular locations." Material: HEK293 cells inducibly expressing wild type or variant IL2RG.

The "Notes" row (A26) is present but **empty for all instances**. Rows A7, A12 and A22 are blank spacer rows. The sheet declares a range of A1:AF1000 but all populated cells fall within A1:I26.

**Important:** column B (Matsubara et al., 2014, PMID 24853770) is marked **"Approved assay: n"** with no proposed strength, and its assay class ("IL-2-induced expression of downstream targets") is **not** among the four approved classes listed in the PS3 section. It must not be used to apply PS3.

---

## Internal Inconsistencies and Apparent Source Errors

These are reported, not corrected. The operative source text is transcribed above in each case.

1. **PS4 defines strength two incompatible ways.** The VCEP Specifications block uses proband counts (1 / 2 / 3 / ≥4). The per-strength blocks use "sum of case scores" point ranges (1–2 / 2.5–4 / 4.5–16 / >16) and refer to "instructions below" that do not exist anywhere in the specification or its supplementary files. The point ranges also leave gaps (2–2.5, 4–4.5, and 16 falls in the Strong band while >16 is Very Strong). The case-score system is **absent from this specification package**.
2. **PM2's Supporting strength block contains PS3 text.** It reads "Strength modification based on an abnormal result in at least one approved in vitro assay", which is verbatim the PS3 Supporting text and has nothing to do with allele frequency.
3. **PM1 CpG position "c.691G (Arg691)".** IL2RG (NM_000206.3) does not have 691 codons; the adjacent entries are c.684C (Arg224), c.690C (Arg226), c.868G (Arg285). The protein position appears to be a transcription error for a codon in the low-230s. Preserved verbatim.
4. **PM1 codon numbering vs. the functional-evidence workbook.** PM1 lists c.690C as Arg226; the workbook lists c.690C>T as p.Arg204Cys (columns G and H). Also c.664C>T is p.Arg222Cys in the workbook while PM1 lists c.684C as Arg224. The two documents use inconsistent protein numbering for the same nucleotide positions.
5. **PP4: IL-2 vs IL-21 for the STAT3 rows.** The main specification PDF renders these four points as "Reduced **IL-2**-induced phosphorylation of STAT3"; the standalone `PP4 - IL2RG.pdf` reads "Reduced **IL-21**-induced phosphorylation of STAT3". The IL-21 wording (supplement) is biologically consistent with the STAT3/IL21R gene list and is used in the table above; the discrepancy is flagged rather than silently resolved.
6. **PP4 footnote 1 differs between documents.** Supplement: "CNV testing is required to consider PP4_Strong". Main spec / Strong strength block: "CNV testing is required **if PP4_Strong cannot be reached without points from gene therapy**". These are materially different requirements.
7. **PP4 footnote 2 hyperlink** ("summarized here") points to an external PIDTC 2022 summary that is not distributed with the specification and whose target is not recoverable from the PDF.
8. **BS2 bands overlap as printed.** BS2_Strong requires ≥3 hemizygotes; BS2_Supporting requires "at least 2". A variant with ≥3 hemizygotes literally satisfies both. The VCEP does not state that Supporting is exactly 2.
9. **BS3 is Not Applicable, yet a "PS3_BS3 Functional Evidence" workbook is distributed for IL2RG.** The workbook proposes only PS3_Supporting strengths and contains no BS3 assignments, so the two are reconcilable, but the file name implies BS3 use that the specification forbids.
10. **BP7's "two out of three in silico tools" requirement is missing from the Supporting strength block**, and the list of "three" tools names six (GeneSplicer, MaxEntScan, NNSplice, SpliceAI, SSF, varSEAK).
11. **PM6_VeryStrong is defined (4 points) but has no Very Strong strength block and does not appear in the Very Strong tier list** of the Rules for Combining Criteria (which lists only PVS1, PS2_Very Strong, PS4_Very Strong).
12. **PM1 appears in the combining rules only as PM1_Strong**, consistent with the upgrade, but the specification never defines a default-strength PM1, so PM1 at Moderate is not usable.
13. **Likely Pathogenic rules 2 and 7 are redundant** (1 Strong + 1 Moderate subsumes 1 Strong + 2 Moderate).
14. **PVS1 flowchart footnote markers a, b, d have no legend** anywhere in the distributed file.
15. **Functional-evidence workbook typos:** the "Threshold for normal readout" row reads "Wild type-like level of phosphorylated **Jak4**" (column D) and "**Jak5**" (column E), while the corresponding abnormal-readout cells both read "Jak3". Both are apparent typos for Jak3.
16. **PM5 point-table legend is incomplete:** "NMD = nonsense-mediated decay; PTC premature termination codon" — the "=" is missing after PTC. Preserved.
17. **PM3's Original ACMG Summary is rendered twice**, once with all inter-word spacing lost ("Forrecessivedisordersdetectedintranswithapathogenicvariant"). This is a source rendering defect.
18. **Spelling "occurences"** (for "occurrences") appears in the PS2 and PM6 headings of the main specification.
19. **PP1's Oza Table 4b is autosomal-recessive-specific and is distributed without any instruction for X-linked use.** The VCEP's numeric thresholds match Table 4a's autosomal dominant row; the specification never states which row applies to an X-linked gene.

---

## Criteria Status Summary

| Criterion | Status |
|-----------|--------|
| PVS1 | Specified (VeryStrong / Strong / Moderate / Supporting; IL2RG flowchart) |
| PS1 | Specified (Strong / Moderate) |
| PS2 | Specified (VeryStrong / Strong / Moderate / Supporting) |
| PS3 | Specified (Strong / Supporting; Moderate not specified) |
| PS4 | Specified but internally contradictory (see Section 5) |
| PM1 | Specified, upgraded to PM1_Strong only |
| PM2 | Specified, downgraded to PM2_Supporting only |
| PM3 | **Not Applicable** |
| PM4 | Specified (Moderate / Supporting) |
| PM5 | Specified (Strong / Moderate / Supporting; nonsense point system) |
| PM6 | Specified (Strong / Moderate / Supporting; VeryStrong point value defined without a block) |
| PP1 | Specified (Strong / Moderate / Supporting) |
| PP2 | **Not Applicable** |
| PP3 | Specified (Supporting only) |
| PP4 | Specified (Strong / Moderate / Supporting; points table) |
| PP5 | **Not Applicable** (SVI VCEP Review Committee recommendation) |
| BA1 | Specified (Stand Alone) |
| BS1 | Specified (Strong) |
| BS2 | Specified (Strong / Supporting; hemizygotes) |
| BS3 | **Not Applicable** |
| BS4 | Specified (Strong, no additional specifications) |
| BP1 | **Not Applicable** |
| BP2 | **Not Applicable** |
| BP3 | **Not Applicable** |
| BP4 | **Not Applicable** |
| BP5 | **Not Applicable** |
| BP6 | **Not Applicable** (SVI VCEP Review Committee recommendation) |
| BP7 | Specified (Supporting) |

---

## Version History

| Version | Released | Notes |
|---------|----------|-------|
| 2.2 | 6/1/2026 | Edited Rules for Combining Criteria to reflect standard combinations plus (A) 1 very strong + 1 supporting = Likely Pathogenic and (B) 1 Strong Benign = Likely Benign. Refreshed and saved Rules for Combining Criteria. Updated PM5_Strong, PM5_Moderate, PM5_Supporting. Made changes to PP4 criteria. Uploaded IL2RG corrections which includes PM1 and PS3 codes. |

Earlier version history is not printed in the v2.2 specification document.

---

*This document was compiled from the ClinGen VCEP specification (GN129, IL2RG v2.2) and its five distributed supplementary files. Nothing here was supplied from generic ACMG/AMP or SVI content that the VCEP package does not itself distribute. For the most current version, please refer to the ClinGen website.*
