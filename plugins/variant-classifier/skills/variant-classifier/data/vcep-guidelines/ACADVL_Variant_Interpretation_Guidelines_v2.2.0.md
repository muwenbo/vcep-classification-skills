# ClinGen ACADVL VCEP Variant Interpretation Guidelines for ACADVL

**Version:** 2.2
**Released:** 7/20/2026
**Affiliation:** ACADVL VCEP
**Source basis:** "Type: Richards et.al., 2015 - Combining rules" (as stated on the specification cover page)
**DOI:** 10.5281/zenodo.21457671
**Registry ID:** GN021

**Description (verbatim from the specification):**
> ACADVL Specifications version 2.0. The VCEP reviewed all the codes and updated wording.
> ACADVL Specifications version 2.0.1. The VCEP updated the wording for PP3 and BP4 to only include reference to the Splice AI tool. 6/11/26 the VCEP added that PVS1 + PM2 (supporting) = Likely Pathogenic

**Release Notes (verbatim from the specification):**
> Version 2.0.1 - the ACADVL VCEP reviewed the PP3 and BP4 codes' wording and updated the reference to only include the Splice AI tool.
>
> 6/11/26 the VCEP added that PVS1 + PM2 (supporting) = Likely Pathogenic
>
> 7/14/26 the VCEP re-added that PVS1 + PM2 (supporting) = LP; No pilot classifications changed due to this added rule.

**General Comments field (verbatim):** `Version 2.0`

> **Note on provenance.** Everything below is transcribed from the ClinGen GN021 v2.2 specification PDF and the eight supplementary files distributed with it. Where the VCEP delegates to external guidance or is silent, that is stated explicitly rather than filled in. Source typos and internal contradictions are preserved verbatim and flagged in [Appendix H](#appendix-h---source-typos-internal-inconsistencies-and-apparent-vcep-errors).

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | ACADVL (HGNC:92) |
| **HGNC Name** | acyl-CoA dehydrogenase very long chain |
| **Transcript** | NM_000018.4 |
| **Disease** | very long chain acyl-CoA dehydrogenase deficiency (MONDO:0008723) |
| **Inheritance** | Autosomal recessive inheritance |

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
   - [BA1 - Allele Frequency](#ba1---allele-frequency)
   - [BS1 - Frequency Greater Than Expected](#bs1---frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (No Effect)](#bs3---functional-studies-no-effect)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP1-BP7 - Benign Supporting](#bp1-bp7---benign-supporting)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Criterion Interaction / Mutual Exclusivity Rules](#criterion-interaction--mutual-exclusivity-rules)
5. [Frequency Threshold Comparator Summary](#frequency-threshold-comparator-summary)
6. [Appendices](#appendices)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**Modification type:** Disease-specific (levels Very Strong, Strong, Moderate; the Supporting level is labelled "Disease specific" without the hyphen)

**VCEP Specifications:**

> **Transcription note:** In the source specification the *identical* block of text below is repeated verbatim under all four strength headings (Very Strong, Strong, Moderate, Supporting). The specification does **not** give strength-differentiating text in the criterion body; the strength assignment comes entirely from the ACADVL PVS1 decision tree (Appendix A). See [Appendix H, item 4](#appendix-h---source-typos-internal-inconsistencies-and-apparent-vcep-errors).

Loss of function is a known mechanism for VLCAD Deficiency. The specifications below are based on published guidance for assigning strength of evidence for PVS1 (Abou Tayoun et al., (2018) PMID: 30192042). There are multiple transcripts for ACADVL. The major isoform, NM_000018.4, encodes a 655 amino acid precursor protein that contains a 40 amino acid N-terminal target sequence that is removed during uptake (Aoyama et al., (1995) PMID: 7668252). In a joint project between NCBI and EMBL-EBI (MANE), NM_000018.4 was designated as the most relevant transcript. Nonsense or Frameshift:

- Use caution when interpreting LOF variants at the 3' end of the gene.
- NMD is not predicted if the variant is in the last exon (exon 20) or in the last 50 nucleotides of the penultimate exon (exon 19).
- Canonical Splice Site (+1, +2, -1, -2): All donor/acceptor sites follow the GT/AG rule, except for the donor splice site of intron 8, which begins with GC. PVS1 should not be applied for variants in the splice donor site of intron 8 since the impact of GC donor splice sites is not well understood. For +1 or +2 GT donor splice site variants, the exon immediately 5' of the variant is predicted to be skipped. For -1 or -2 AG acceptor splice site variants, the exon immediately 3' of the variants is predicted to be skipped.
- Initiation codon: The next in-frame methionine is at position 6 (on transcript NM_000018). However, the first 40 amino acids comprise the leader sequence in the precursor peptide and are important for proper localization of the protein (Aoyama et al., (1995) PMID: 7668252). Therefore, initiator codon variants will meet PVS1_Strong.
- Well-established _in vitro_ or _in vivo_ functional studies supportive of a damaging effect _as measured by effect on mRNA transcript profile (mRNA assay only)._ Apply as PVS1 (RNA) at appropriate strength.
- See ACADVL PVS1 decision tree; cannot be combined with PM1

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Assigned via the ACADVL PVS1 decision tree ([Appendix A](#appendix-a---acadvl-pvs1-decision-tree)); shown in the tree simply as "PVS1". |
| **Strong** | Assigned via the decision tree ("PVS1_Strong"); also the fixed strength for initiator-codon variants. |
| **Moderate** | Assigned via the decision tree ("PVS1_Moderate"). |
| **Supporting** | A Supporting level exists in the specification (with the same boilerplate text), but **no PVS1_Supporting outcome appears anywhere in the ACADVL PVS1 decision tree**. The VCEP does not state when PVS1_Supporting applies. Not specified by VCEP. |

**PVS1 (RNA):** The specification states that mRNA-assay evidence is applied "as PVS1 (RNA) at appropriate strength." The specification does **not** define which strength corresponds to which RNA result, and no RNA-specific PVS1 decision tree was distributed with this package. **Not specified by this VCEP.**

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**Modification type:** Gene-specific (all three levels)

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established **pathogenic** variant classified using the ACADVL specifications without application of PS1, regardless of nucleotide change **OR** same amino acid change as **≥2 previously established likely pathogenic** variants classified using the ACADVL specifications without application of PS1, regardless of nucleotide change.<br>*Caveat (from ACMG/AMP guidelines):* Assess the possibility that the variant may act directly through the DNA change (e.g. through splicing disruption as assessed by at least computational analysis) instead of through the amino acid change.<br>**Splicing route:** Same predicted impact on splicing as previously classified variant (Refer to Table 2 in Walker et al., (2023) PMID: 37352859). |
| **Moderate** | PS1_Moderate: Same amino acid change as a previously established **likely pathogenic** variant classified using the ACADVL specifications without application of PS1, regardless of nucleotide change.<br>*Same ACMG/AMP caveat as above.*<br>**Splicing route:** Same predicted impact on splicing as previously classified variant (Refer to Table 2 in Walker et al., (2023) PMID: 37352859). |
| **Supporting** | Same predicted impact on splicing as previously classified variant (Refer to Table 2 in Walker et al., (2023) PMID: 37352859). *(Splicing route only — no protein-level Supporting rule is given.)* |

**PS1 for splice variants (all three strengths, verbatim):**
> PS1 can be applied at varying strengths for splice variants, in conjunction with either PP3 or PVS1. PS1 strength depends on location of the variant under assessment (within or outside the +/- 1,2 dinucleotide positions) and the location of the previously classified variant (within or outside the +/- 1,2 dinucleotide position). Specific combinations are outlined in Table 2 in Walker, et al., (2023) PMID: 37352859.

> **Gap flag.** Table 2 of Walker et al. (2023) is **not reproduced** in the specification and was **not distributed** as a supplementary file. The strength-by-position combinations are **not specified by this VCEP; consult the referenced external guidance** (Walker et al., 2023, PMID: 37352859, Table 2).

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** **Not Applicable.** PS2 is designated "Not Applicable" by the ACADVL VCEP. No comment text accompanies the designation.

> **No PS2/PM6 point system exists in this specification.** The specification and all eight supplementary files contain no de novo point table, no proband-count table, and no 0.5/1/2/4 strength ladder for PS2 or PM6.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**Modification type:** Disease-specific (all four levels)

**Common text applied at every strength:**
- Functional evidence from non-patient derived material with only a single variant best reflects the variant-level data. **Apply patient-derived evidence in PP4.**
- Apply criteria at the level determined by validation parameters (see PS3 BS3 flowchart, [Appendix D](#appendix-d---ps3--bs3-evaluation-flowchart)).
- Enzyme activity assays, total protein production, protein stability, dimer formation and transcript production are valid assays to consider for PS3.

| Strength | Additional criteria specific to that level |
|----------|--------------------------------------------|
| **Very Strong** | "OddsPath analysis sufficient for very strong application." |
| **Strong** | No level-specific text beyond the common text; assign per the PS3/BS3 flowchart. |
| **Moderate** | No level-specific text beyond the common text; assign per the PS3/BS3 flowchart. |
| **Supporting** | "If an enzyme activity assay has **>20% activity** it cannot be weighted above PS3_supporting regardless of flowchart results." (strict `>`) |

#### Approved Assay Instances

See [Appendix E](#appendix-e---ps3-functional-assay-evaluation-spreadsheet) for the complete transcription of the distributed "PS3 functional assay.xlsx" workbook, which records, per publication, whether the assay instance is approved (y/n) and the proposed strength.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** **Not Applicable.** PS4 is designated "Not Applicable" by the ACADVL VCEP. No comment text accompanies the designation.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**Modification type:** Disease-specific

**VCEP Specifications (Moderate only — no other strength is defined):**

> See table PM1, curators may seek approval from the expert panel for identifying additional hotspots or critical regions as discovered in literature searches for inclusion.

Regions listed **in the main specification PDF** (Moderate):

| Protein location | Functional evidence | References |
|---|---|---|
| p.1-40 | mitochondrial signal peptide | PMIDs: 18227065\*, 20060901 |
| p.214-223 | nucleotide/substrate binding | PMIDs: 18227065\*, 20060901 |
| p.249-251 | nucleotide/substrate binding | PMIDs: 18227065\*, 20060901 |
| p.R326 | CpG dinucleotide | PMID: 9973285 |
| p.381-382 | FAD binding and salt-bridge interaction | PMID: 20060901 |
| p.R429 | CpG dinucleotide | PMID: 9973285 |
| p.E441 | Adjacent to FAD binding, on dimer formation loop | PMIDs: 20060901 |
| p.R459 | dimerization | PMID: 14517516 |
| p.481-516 | membrane binding | PMIDs: 18227065\*, 20060901 |
| p.562 | nucleotide/substrate binding | PMIDs: 18227065\*, 20060901 |

\* protein is described in mature protein nomenclature without signal peptide; add 40 amino acids to reach HGVS nomenclature

> **Discrepancy flag.** The distributed **PM1 table_updated.xlsx** contains one additional region, **p.460-466 (nucleotide/substrate binding, PMIDs: 18227065\*, 20060901)**, which is **absent** from the list embedded in the main specification PDF. The full spreadsheet is transcribed in [Appendix B](#appendix-b---pm1-table-pm1-table_updatedxlsx). The VCEP does not state which list supersedes.

**Mutual exclusivity:** PM1 cannot be combined with PVS1 ("See ACADVL PVS1 decision tree; cannot be combined with PM1"), and cannot be applied with PM5 (see PM5).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**Modification type:** Disease-specific

**VCEP Specifications (Supporting only):**

> Variants with a highest population minor allele frequency (MAF) **<0.001 (0.1%)** in any continental population with **>2000 alleles** in gnomAD will meet PM2_supporting.

- **Comparator:** MAF threshold is **strict** (`<`, not `<=`). The allele-count qualifier is also **strict** (`>2000 alleles`).
- Calculated using the Prevalence of 1:100,000, Allelic Contribution of 0.2, Genetic Contribution of 1, and Penetrance of 0.75 to allow for mild VLCADD that may develop in adulthood. This was multiplied by 1.5 to account for mildly pathogenic variants being present in carriers within the population databases.
- It is acceptable for an ACADVL variant to be present in controls because VLCAD deficiency is a recessive condition. It is also possible for homozygous ACADVL variants to be present in population databases due to later onset of the condition. If homozygous variants are present, the number should be noted and discussed with an expert.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**Modification type:** Disease-specific (all four levels)

**Common text applied at every strength (verbatim):**
- Details of the cDNA change must be used to describe any variants used as evidence for PM3. If the variant is described only as an amino acid change, this is not sufficient. **Probands must also meet PP4 criteria to be counted.**
- If more than one case has the same genotype and the variants are not confirmed in trans, then only one case should be used for assigning points to avoid overcounting evidence if the variants are actually in cis and hence inherited together in multiple individuals or potentially counting the same case twice. If the variants are confirmed to be in trans, more than one individual with the same genotype can be counted as long as the reports do not represent the same case.
- These variant interpretation guidelines should be used to determine the classification of the "other variant" in order to determine the appropriate number of points to assign.
- For a variant to be "confirmed in trans" in a compound heterozygous patient, parental testing, or another appropriate molecular method (such as cloning each allele separately followed by sequencing), must have been performed. Otherwise, the phase of the variants is unknown. **Parental testing is not required for homozygous cases.**
- See PM3 table.

#### PM3 Point System (from the main specification and the distributed "PM3 table.pdf")

**Points per proband:**

| Classification/Zygosity of other variant | Confirmed in trans | Phase unknown |
|---|---|---|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P)<br>0.25 (LP) |
| Homozygous occurrence<br>(Max points = 1.0) | 0.5 | N/A |

**PM3 Point Table (thresholds as stated in the main specification):**

| Strength | Point range (main specification) | Point value (PM3 table.pdf) |
|---|---|---|
| **PM3_Supporting** | PM3 score ≥ 0.5 < 1.0 | 0.5 points |
| **PM3 (Moderate)** | PM3 score ≥ 1.0 < 2.0 | 1.0 points |
| **PM3_Strong** | PM3 score ≥ 2.0 < 4.0 | 2.0 points |
| **PM3_VeryStrong** | PM3 score ≥ 4.0 | 4.0 points |

- **Comparators:** lower bounds are **inclusive** (`≥`); upper bounds are **strict** (`<`).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**Modification type:** Disease-specific

| Strength | Criteria |
|----------|----------|
| **Moderate** | "Follow recommendations as outlined in ACMG/AMP guidelines and/or Sequence Variant Interpretation working group." — **Not specified by this VCEP; consult the referenced external guidance** (ACMG/AMP guidelines; ClinGen Sequence Variant Interpretation working group). |
| **Supporting** | Not specified by VCEP (no Supporting level is defined for PM4). |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**Modification type:** Disease-specific (all three levels)

**Common note applied at every strength (verbatim):**
> See PM5 table. Note: Cannot be applied with PM1, apply criteria with the highest strength. If both are applicable at the same strength, apply PM5 as it is amino acid specific.

**Point assignment (from the distributed "PM5 table.xlsx"):**
> Each additional variant at the same codon: **LP = 0.5, P = 1.0** (As classified by the ACADVL VCEP)

| Strength | Points (PM5 table.xlsx) | Illustrative examples given in the main specification |
|---|---|---|
| **PM5_Strong** | ≥2.0 | *(No example given in the main specification.)* |
| **PM5_Moderate** | ≥1.0 and <2.0 | "Two likely pathogenic variants at the same codon"; "One pathogenic variant at the same codon" |
| **PM5_Supporting** | 0.5 | "One likely pathogenic variant at the same codon" |

- **Comparators:** PM5_Strong lower bound **inclusive** (`≥2.0`); PM5_Moderate is **inclusive** at the lower bound and **strict** at the upper bound (`≥1.0 and <2.0`); PM5_Supporting is stated as an exact value (`0.5`), not a range.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**Modification type:** No change

| Strength | Criteria |
|----------|----------|
| **Moderate** | "Assumed de novo, but without confirmation of paternity and maternity." (unchanged from ACMG/AMP) |

> No PM6 point system, proband-count table, or strength ladder appears anywhere in this specification or its supplementary files. Any strength other than Moderate is **not specified by VCEP**.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**Modification type:** Disease-specific (all three levels)

**Common text applied at every strength (verbatim):**
> See PP1 table. Probands are NOT counted toward segregation. Likewise, carrier parents DO NOT count as unaffected segregations. Affected segregations = # affected individuals in the family with the variants - 1. Affected segregations are defined as affected family members (typically siblings) who harbor the variant in question and a second variant on the remaining allele. Unaffected segregations are defined as unaffected family members, typically siblings, who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants identified in the proband, or a heterozygous carrier for a single variant. There may be scenarios where individuals other than siblings could be counted as segregations, such as in families where one parent is affected with the autosomal recessive disorder, in large families with multiple branches, or in consanguineous families.

#### LOD score thresholds (main specification, verbatim)

| Strength | Likelihood | LOD score threshold |
|---|---|---|
| **Strong** | 32:1 Likelihood | A LOD score **≥ 1.50** |
| **Moderate** | 16:1 Likelihood | A LOD score **< 1.50 ≥ 1.20** |
| **Supporting** | 4:1 Likelihood | An LOD score **< 1.20 ≥ 0.60** |

- **Comparators:** lower bounds **inclusive** (`≥`); upper bounds **strict** (`<`).

The distributed **PP1 tables.pdf** contains the general recommendation table and the affected × unaffected segregation LOD grid — both fully transcribed in [Appendix C](#appendix-c---pp1-segregation-tables).

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** **Not Applicable.**
**Comment (verbatim):** "This rule does not apply as there are benign and pathogenic missense variants in ACADVL."

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**Modification type:** Disease-specific

**VCEP Specifications (Supporting only):**
- Missense changes with a **REVEL scores >0.75** will meet PP3 *(source wording "scores" preserved; comparator is **strict** `>`)*
- For in-frame deletions and insertions, use **Mutation Taster**. *(No score threshold is given for Mutation Taster — **not specified by VCEP**.)*
- For non-canonical splice site variants, use **Splice AI**. Based on data from Jaganathan et al., (2019) PMID: 30661751, Houdayer et al., (2012) PMID: 22505045 and Tang et al., (2016) PMID: 27313609 and Walker et al., (2023) PMID: 37352859, PP3 can be applied if there is, a SpliceAI "high score" (**Δ Score ≥ 0.5** "confidently predicted splice variants") (**exclude any results with Δ Score ≤ 0.2** from consideration of pathogenicity, **<0.2** are not "predicted to alter splicing").
- For SpliceAI's cryptic splice-site rules, the creation of a new splice-site with **Δ Score ≥ 0.5** may be enough to produce a large proportion of aberrant transcripts.
- If a new splice site is predicted to be generated, this rule can be applied if the newly generated splice site is significantly stronger than the wild type site (**Δ Score ≥ 0.5** using SpliceAI).
- **Do not apply this rule for canonical splice site changes meeting PVS1.**

- **Comparators:** REVEL `>0.75` **strict**; SpliceAI application `≥ 0.5` **inclusive**; SpliceAI exclusion `≤ 0.2` **inclusive**. The parenthetical then says `<0.2` (strict) are not "predicted to alter splicing" — see [Appendix H, item 9](#appendix-h---source-typos-internal-inconsistencies-and-apparent-vcep-errors).
- The specification does not state how variants with Δ Score >0.2 and <0.5 are treated. **Not specified by VCEP.**

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**Modification type:** Disease-specific

**Common text applied at both strengths (verbatim):**
> Abnormal tests that are consistent with VLCAD deficiency include deficient VLCAD enzyme activity in patient cells (leukocytes, fibroblasts, liver, heart, or skeletal muscle, or amniocytes), abnormal C14:1 acylcarnitine values from newborn screening (NBS), and abnormal acylcarnitine values from follow-up plasma analysis.

| Strength | Points |
|----------|--------|
| **Moderate** | 2 points (See PP4 Table) |
| **Supporting** | 1 point (See PP4 Table) |

#### PP4 Points Table (from "PP4 points table.xlsx")

| Description of evidence | Points |
|---|---|
| VLCAD enzyme activity (ꞵ-Oxidation Flux) **≤20% of normal** | 2 |
| VLCAD enzyme activity (ꞵ-Oxidation Flux) **21-27% of normal** | 1 |
| Assertion of reduced VLCAD activity without specific levels | 1 |
| NBS C14:1 Levels from **0.8 - 0.99 μM** | 1 (a) |
| Assertion of abnormal NBS "consistent with VLCADD" without specific levels | 0.5 |
| Follow-Up Plasma Acylcarnitine analysis "consistent with VLCADD" without specific levels | 0.5 (b) |

Footnotes (verbatim):
- **(a)** In order to reach PP4_Moderate using NBS data, C14:1 Levels must be **≥ 1.0 μM**
- **(b)** If NBS C14:1 Levels are **≥ 1.0 μM**, this can be upweighted to 1 pt

**PP4 Point Table:**

| Strength | Points |
|---|---|
| **PP4** | 1.0 points |
| **PP4_Moderate** | 2.0 points |

- **Comparators:** enzyme activity `≤20%` **inclusive**; the `21-27%` band is stated as an inclusive integer range; NBS `0.8 - 0.99 μM` is an inclusive range; footnote thresholds `≥ 1.0 μM` **inclusive**.
- **Gap flag:** the enzyme-activity rows leave **>27% of normal** and the interval **>20% to <21%** unaddressed, and the NBS rows leave **<0.8 μM** unaddressed. **Not specified by VCEP.** See [Appendix H, item 10](#appendix-h---source-typos-internal-inconsistencies-and-apparent-vcep-errors).

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable.** "This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee." (PubMed: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Modification type:** Disease-specific

**VCEP Specifications (Stand Alone):**
> Variants with a highest population minor allele frequency (MAF) **≥0.007 (0.7%)** in any continental population with **>2000 alleles** in gnomAD will meet BA1.
> Calculated using the Prevalence of 1:30,000, Allelic Contribution of 1, Genetic Contribution of 1, and Penetrance of 0.75 to allow for mild VLCADD that may develop in adulthood.

- **Comparators:** MAF threshold **inclusive** (`≥0.007`). Allele-count qualifier **strict** (`>2000 alleles`).

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**Modification type:** Disease-specific

**VCEP Specifications (Strong):**
> Variants with a highest population minor allele frequency (MAF) **≥0.0035 (0.35%)** in any continental population with **>2000 alleles** in gnomAD will meet BS1.
> Calculated using the Prevalence of 1:30,000, Allelic Contribution of 0.5, Genetic Contribution of 1, and Penetrance of 0.75 to allow for mild VLCAD that may develop in adulthood.

- **Comparators:** MAF threshold **inclusive** (`≥0.0035`). Allele-count qualifier **strict** (`>2000 alleles`).

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** **Not Applicable.** No comment text accompanies the designation.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**Modification type:** Disease-specific (Strong, Moderate, Supporting)

**VCEP Specifications — identical text at all three strengths (verbatim, typo preserved):**
> Enzyme activity assays, total protein production, protein stability, dimer formation and transcript production are valid assays to consider for **PS3**. Apply criteria at the level determined by validation parameters (see PS3 BS3 flowchart).

> **Typo flag.** The BS3 entry says "valid assays to consider for **PS3**" — the criterion under discussion is BS3. Transcribed verbatim; see [Appendix H, item 5](#appendix-h---source-typos-internal-inconsistencies-and-apparent-vcep-errors).

Strength is assigned by the PS3/BS3 evaluation flowchart ([Appendix D](#appendix-d---ps3--bs3-evaluation-flowchart)). No BS3 Stand-Alone or Very Strong level is defined; the flowchart's top BS3 outcome is "Max BS3" (i.e. Strong).

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**Modification type:** No change

| Strength | Criteria |
|----------|----------|
| **Strong** | "Follow recommendations as outlined in ACMG/AMP guidelines and/or Sequence Variant Interpretation working group" — **Not specified by this VCEP; consult the referenced external guidance.** |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | "This rule does not apply. There are known pathogenic missense variants in ACADVL." |
| **BP2** | Supporting (Modification type: **No change**) | "Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder; or observed in cis with a pathogenic variant in any inheritance pattern." |
| **BP3** | Not Applicable | "There are no known repetitive regions without known function in ACADVL." |
| **BP4** | Supporting (Modification type: **Disease-specific**) | See detail below. |
| **BP5** | Not Applicable | "An individual could be a carrier of a pathogenic variant in ACADVL and have another disorder." |
| **BP6** | Not Applicable | "This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee." (PubMed: 29543229) |
| **BP7** | **Strong** (Disease-specific) and **Supporting** (Gene-specific) | See detail below. |

#### BP4 detail (Supporting)

- Missense changes with a **REVEL score <0.5** will meet BP4. *(strict `<`)*
- For in-frame deletions and insertions, use **Mutation Taster**. *(No threshold given — **not specified by VCEP**.)*
- For non-canonical splice site variants, use **Splice AI**. Based on data from Jaganathan et al., 2019 (PMID: 30661751), Houdayer et al., 2012 (PMID: 22505045), Tang et al., 2016 (PMID: 27313609), and Walker et al., (2023) PMID: 37352859, BP4 can be applied if there is a **Δ Score ≤ 0.1**. *(inclusive `≤`)*
- **Do not apply this rule if there is evidence for creation of a cryptic splice site.**
- **Can be used with BP7 code.**

> **Gap flag:** REVEL scores in the interval `≥0.5` to `≤0.75` meet neither PP3 nor BP4; the specification does not state how they are treated. **Not specified by VCEP.**

#### BP7 detail

| Strength | Criteria |
|---|---|
| **Strong** (Disease-specific) | "BP7_Strong (RNA) in vitro evidence of no splicing impact for intronic or synonymous variants irrespective of position and predicted impact on splicing." |
| **Supporting** (Gene-specific) | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.<br>Can be used for intronic variants that fall outside the minimal splice region (**≥+7 or ≤-21**) — both comparators **inclusive**.<br>Can be used with BP4 code. |

---

## Rules for Combining Criteria

Transcribed verbatim from the "Rules for Combining Criteria" section of the specification (Type: Richards et al., 2015 - Combining rules).

**Pathogenic**
- 1 Very Strong AND ≥ 1 Strong
- 1 Very Strong AND ≥ 2 Moderate
- 1 Very Strong AND 1 Moderate AND 1 Supporting
- 1 Very Strong AND ≥ 2 Supporting
- ≥ 2 Strong
- 1 Strong AND ≥ 3 Moderate
- 1 Strong AND 2 Moderate AND ≥ 2 Supporting
- 1 Strong AND 1 Moderate AND ≥ 4 Supporting

**Likely Pathogenic**
- 1 Very Strong AND 1 Moderate
- 1 Strong AND 1 Moderate
- 1 Strong AND ≥ 2 Supporting
- ≥ 3 Moderate
- 2 Moderate AND ≥ 2 Supporting
- 1 Moderate AND ≥ 4 Supporting
- 1 Strong AND 2 Moderate
- **1 Very Strong (PVS1) AND 1 Supporting (PM2_Supporting)** ← added in this version cycle (see Release Notes)

**Benign**
- ≥ 2 Strong
- 1 Stand Alone

**Likely Benign**
- 1 Strong AND 1 Supporting
- ≥ 2 Supporting

> **Note.** The specification provides no point-based (Tavtigian-style) classification scheme; combination is by the Richards et al. 2015 rule set above only. There is no rule listed for Uncertain Significance — anything not meeting the above is, by the Richards et al. framework, VUS, but the specification itself does not state this.

---

## Criterion Interaction / Mutual Exclusivity Rules

Collected from the criterion entries and supplementary files (all are explicit source statements):

| Rule | Source |
|---|---|
| PVS1 **cannot be combined with PM1** | PVS1 entry, all strengths |
| PM5 **cannot be applied with PM1**; apply the criterion with the highest strength; if both apply at the same strength, apply PM5 because it is amino acid specific | PM5 entry, all strengths |
| PP3 **must not be applied** for canonical splice site changes meeting PVS1 | PP3 entry |
| BP4 **must not be applied** if there is evidence for creation of a cryptic splice site | BP4 entry |
| BP4 **can be used with** BP7 | BP4 and BP7 entries |
| PM3 probands **must also meet PP4 criteria** to be counted | PM3 entry, all strengths |
| Patient-derived functional evidence is applied under **PP4**, not PS3 | PS3 entry, all strengths |
| PS1 for splice variants is applied **in conjunction with either PP3 or PVS1** | PS1 entry, all strengths |
| Enzyme activity assay with **>20% activity** caps PS3 at Supporting regardless of flowchart result | PS3 Supporting |

---

## Frequency Threshold Comparator Summary

| Criterion | Threshold | Comparator | Population/qualifier | Qualifier comparator |
|---|---|---|---|---|
| **BA1** (Stand Alone) | MAF 0.007 (0.7%) | **≥ (inclusive)** | any continental population, gnomAD | **> 2000 alleles (strict)** |
| **BS1** (Strong) | MAF 0.0035 (0.35%) | **≥ (inclusive)** | any continental population, gnomAD | **> 2000 alleles (strict)** |
| **PM2** (Supporting) | MAF 0.001 (0.1%) | **< (strict)** | any continental population, gnomAD | **> 2000 alleles (strict)** |

Non-frequency numeric comparators, for completeness:

| Criterion | Threshold | Comparator |
|---|---|---|
| PP3 (missense) | REVEL 0.75 | **> (strict)** |
| BP4 (missense) | REVEL 0.5 | **< (strict)** |
| PP3 (splice) | SpliceAI Δ 0.5 | **≥ (inclusive)** |
| PP3 (splice, exclusion) | SpliceAI Δ 0.2 | **≤ (inclusive)** |
| BP4 (splice) | SpliceAI Δ 0.1 | **≤ (inclusive)** |
| BP7 (intronic window) | +7 / −21 | **≥ / ≤ (both inclusive)** |
| PS3 cap | enzyme activity 20% | **> (strict)** |
| PP4 | enzyme activity 20% of normal | **≤ (inclusive)** |
| PP4 (NBS footnotes) | C14:1 1.0 μM | **≥ (inclusive)** |
| PP1 | LOD 1.50 / 1.20 / 0.60 | lower bounds **≥ (inclusive)**, upper bounds **< (strict)** |
| PM3 | 0.5 / 1.0 / 2.0 / 4.0 points | lower bounds **≥ (inclusive)**, upper bounds **< (strict)** |
| PM5 | 1.0 / 2.0 points | lower bounds **≥ (inclusive)**, upper bound **< (strict)** |

---

## Appendices

Eight supplementary files were distributed with GN021 v2.2. All eight opened successfully and are transcribed below.

| # | File | Type | Transcribed in |
|---|---|---|---|
| 1 | PVS1 decision tree.pdf (2 pages) | PDF, vector figure + table | [Appendix A](#appendix-a---acadvl-pvs1-decision-tree) |
| 2 | PM1 table_updated.xlsx | Excel | [Appendix B](#appendix-b---pm1-table-pm1-table_updatedxlsx) |
| 3 | PP1 tables.pdf (1 page) | PDF, raster images | [Appendix C](#appendix-c---pp1-segregation-tables) |
| 4 | PS3 and BS3 flowchart.pdf (1 page) | PDF, raster image | [Appendix D](#appendix-d---ps3--bs3-evaluation-flowchart) |
| 5 | PS3 functional assay.xlsx (5 sheets) | Excel | [Appendix E](#appendix-e---ps3-functional-assay-evaluation-spreadsheet) |
| 6 | PM3 table.pdf (1 page) | PDF | transcribed inline under [PM3](#pm3---in-trans-with-pathogenic) |
| 7 | PM5 table.xlsx | Excel | transcribed inline under [PM5](#pm5---novel-missense-at-same-residue) |
| 8 | PP4 points table.xlsx | Excel | transcribed inline under [PP4](#pp4---phenotype-specificity) |

---

### Appendix A - ACADVL PVS1 decision tree

Source: `PVS1 decision tree.pdf`, 2 pages. Page 1 is the decision tree; page 2 is the exon-level lookup table.

#### A.1 Decision tree (page 1)

**Branch: Nonsense or Frameshift**

| Condition | Sub-condition | Further condition | Outcome |
|---|---|---|---|
| Predicted to undergo NMD (Termination pre-c.1778) | Exon is present in biologically-relevant transcript (NM_000018.4) | — | **PVS1** |
| Predicted to undergo NMD (Termination pre-c.1778) | Exon is absent from biologically-relevant transcript (NM_000018.4) | — | **N/A** |
| Not predicted to undergo NMD (termination at c.1778 or after) → Role of region in protein function is unknown | Exon is absent from biologically-relevant transcript (NM_000018.4) | — | **N/A** |
| Not predicted to undergo NMD (termination at c.1778 or after) → Role of region in protein function is unknown | Exon is present in biologically-relevant transcript (NM_000018.4) | Variant removes <10% of protein | **PVS1_Moderate** |

**Branch: GT--AG 1,2 splice sites** <sup>a</sup>

| Condition | Sub-condition | Further condition | Outcome |
|---|---|---|---|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD | Exon is present in biologically-relevant transcript (NM_000018.4) | — | **PVS1** |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD | Exon is absent from biologically-relevant transcript (NM_000018.4) | — | **N/A** |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is **NOT** predicted to undergo NMD (Exon 20) → Role of region in protein function is unknown | Exon is absent from biologically-relevant transcript (NM_000018.4) | — | **N/A** |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is **NOT** predicted to undergo NMD (Exon 20) → Role of region in protein function is unknown | Exon is present in biologically-relevant transcript (NM_000018.4) | Variant removes <10% of protein | **PVS1_Moderate** |
| Exon skipping or use of a cryptic splice site preserves reading frame (Exons 3, 6, 9, 11-14) → Role of region in protein function is unknown | Exon is absent from biologically-relevant transcript (NM_000018.4) | — | **N/A** |
| Exon skipping or use of a cryptic splice site preserves reading frame (Exons 3, 6, 9, 11-14) → Role of region in protein function is unknown | LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript | Variant removes <10% of protein | **PVS1_Moderate** |
| Exon skipping or use of a cryptic splice site preserves reading frame (Exons 3, 6, 9, 11-14) | Truncated/altered region is critical to protein function (Exons 13-14) | — | **PVS1_Strong** |

**Branch: Deletion (Single exon to full gene)**

| Condition | Sub-condition | Further condition | Outcome |
|---|---|---|---|
| Full gene deletion | — | — | **PVS1** |
| Single to multi exon deletion – Disrupts reading frame and is predicted to undergo NMD <sup>b</sup> | Exon is present in biologically-relevant transcript (NM_000018.4) | — | **PVS1** |
| Single to multi exon deletion – Disrupts reading frame and is predicted to undergo NMD <sup>b</sup> | Exon is absent from biologically-relevant transcript (NM_000018.4) | — | **N/A** |
| Single to multi exon deletion – Disrupts reading frame and is **NOT** predicted to undergo NMD <sup>b</sup> | Truncated/altered region is critical to protein function (**Exons 1-2, 8, 10, 13-15, 18**) | — | **PVS1_Strong** |
| Single to multi exon deletion – Disrupts reading frame and is **NOT** predicted to undergo NMD <sup>b</sup> → Role of region in protein function is unknown | Exon is absent from biologically-relevant transcript (NM_000018.4) | — | **N/A** |
| Single to multi exon deletion – Disrupts reading frame and is **NOT** predicted to undergo NMD <sup>b</sup> → Role of region in protein function is unknown | Exon is present in biologically-relevant transcript (NM_000018.4) | Variant removes **>10%** of protein | **PVS1_Strong** |
| Single to multi exon deletion – Preserves reading frame → Role of region in protein function is unknown | Exon is present in biologically-relevant transcript (NM_000018.4) | Variant removes **<10%** of protein | **PVS1_Moderate** |
| Single to multi exon deletion – Preserves reading frame | Truncated/altered region is critical to protein function (**Exons 1-2, 10, 13-15, 18**) | — | **PVS1_Strong** |

> In the figure, the "Role of region in protein function is unknown" node is shared between the "Disrupts reading frame and is NOT predicted to undergo NMD" and "Preserves reading frame" deletion branches, and the ">10% of protein" / "<10% of protein" leaves both hang off it. The row assignment above follows the drawn arrows. Note that the "critical to protein function" exon lists differ between the two branches (exon 8 present in one, absent in the other) — see [Appendix H, item 7](#appendix-h---source-typos-internal-inconsistencies-and-apparent-vcep-errors).

**Branch: Duplication (≥1 exon in size and must be completely contained within gene)**

| Condition | Sub-condition | Outcome |
|---|---|---|
| Proven in tandem | Reading frame disrupted and NMD predicted to occur | **PVS1** |
| Proven in tandem / Presumed in tandem | No or unknown impact on reading frame and NMD | **N/A** |
| Presumed in tandem | Reading frame presumed disrupted and NMD predicted to occur | **PVS1_Strong** |
| Proven not in tandem | — | **N/A** |

**Branch: Initiation Codon**

| Condition | Sub-condition | Outcome |
|---|---|---|
| Is present in (NM_000018.4); no known alternative start codon in other transcripts | Next in frame methionine at codon 6, but the first 40 amino acids comprise the leader sequence and are required for proper protein localization (Aoyamaa T et al., PMID: 7668252) | **PVS1_Strong** |

> **Missing footnotes.** The figure carries footnote markers **a** (on "GT--AG 1,2 splice sites") and **b** (on the two "Single to multi exon deletion – Disrupts reading frame…" boxes). **No footnote text for a or b appears anywhere in the 2-page PDF or in the main specification.** Their content is unknown and is **not reproduced here**.

#### A.2 Exon-level lookup table (page 2)

This is a per-exon lookup: given the exon predicted to be skipped, read off the PVS1 strength.

| Exon | First coding nt | Last coding nt | Exon length (nts) | Exon in frame or out | PVS1 Strength for skipping | Rationale |
|---|---|---|---|---|---|---|
| 1 | 1 | 62 | 62 | Out of frame | PVS1 | Fs, PTC, NMD |
| 2 | 63 | 138 | 76 | Out of frame | PVS1 | Fs, PTC, NMD |
| 3 | 139 | 204 | 66 | In frame | PVS1_Moderate | 33 amino acids, ~3.4% of total |
| 4 | 205 | 277 | 73 | Out of frame | PVS1 | Fs, PTC, NMD |
| 5 | 278 | 342 | 65 | Out of frame | PVS1 | Fs, PTC, NMD |
| 6 | 343 | 477 | 135 | In frame | PVS1_Moderate | 45 amino acids, ~6.9% of total |
| 7 | 478 | 622 | 145 | Out of frame | PVS1 | Fs, PTC, NMD |
| 8 | 623 | 752 | 130 | Out of frame | PVS1 | Fs, PTC, NMD |
| 9 | 753 | 878 | 126 | In frame | PVS1_Moderate | 42 amino acids, ~6.4% of total |
| 10 | 879 | 1077 | 199 | Out of frame | PVS1 | Fs, PTC, NMD |
| 11 | 1078 | 1182 | 105 | In frame | PVS1_Moderate | 35 amino acids, ~5.3% of total |
| 12 | 1183 | 1269 | 87 | In frame | PVS1_Moderate | 29 amino acids, ~4.4% of total |
| 13 | 1270 | 1332 | 63 | In frame | PVS1_Moderate | 21 amino acids, ~3.2% of total |
| 14 | 1333 | 1434 | 102 | In frame | PVS1_Moderate | 34 amino acids, 5.2% of total |
| 15 | 1435 | 1532 | 98 | Out of frame | PVS1 | Fs, PTC, NMD |
| 16 | 1533 | 1605 | 73 | Out of frame | PVS1 | Fs, PTC, NMD |
| 17 | 1606 | 1678 | 73 | Out of frame | PVS1 | Fs, PTC, NMD |
| 18 | 1679 | 1751 | 73 | Out of frame | PVS1 | Fs, PTC, NMD |
| 19 | 1752 | 1827 | 76 | Out of frame | PVS1 | Fs, PTC, NMD |
| 20 | 1828 | 1968 | 141 | In frame | PVS1_Moderate | **7 amino acids, ~7.2% of total** |

Abbreviations (verbatim): Fs=frameshift, PTC=premature termination codon, NMD=nonsense mediated decay, nt=nucleotide, nts=nucleotides

> Exon 20's rationale reads "7 amino acids, ~7.2% of total" — see [Appendix H, item 6](#appendix-h---source-typos-internal-inconsistencies-and-apparent-vcep-errors).

---

### Appendix B - PM1 table ("PM1 table_updated.xlsx")

Complete transcription of Sheet1 (the workbook contains one sheet and no embedded images).

| Protein location | Functional Evidence | References |
|---|---|---|
| p.1-40 | Mitochondrial signal peptide | PMIDs: 18227065\*, 20060901 |
| p.214-223 | Nucleotide/substrate binding | PMIDs: 18227065\*, 20060901 |
| p.249-251 | Nucleotide/substrate binding | PMIDs: 18227065\*, 20060901 |
| p.R326 | CpG dinucleotide | PMID: 9973285 |
| p.381-382 | FAD binding and salt-bridge interaction | PMID: 20060901 |
| p.R429 | CpG dinucleotide | PMID: 9973285 |
| p.E441 | Adjacent to FAD binding, on dimer formation loop | PMID: 20060901 |
| p.R459 | Dimerization | PMID: 14517516 |
| **p.460-466** | **Nucleotide/substrate binding** | **PMIDs: 18227065\*, 20060901** |
| p.481-516 | Membrane binding | PMIDs: 18227065\*, 20060901 |
| p.562 | Nucleotide/substrate binding | PMIDs: 18227065\*, 20060901 |

Footnote (merged cell A13:C13, verbatim): "\*protein described in mature protein nomenclature without signal peptide, add 40 amino acids to reach HGVS numbering"

Rows shown in **bold** are present in the spreadsheet but absent from the list in the main specification PDF.

---

### Appendix C - PP1 segregation tables

Source: `PP1 tables.pdf`, 1 page. The page is a fragment of the *Version 1* ACADVL specification document (header: "ClinGen ACADVL Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines Version 1 … Date Approved: November 8, 2021"). Both tables are raster images with no text layer; transcribed from the rendered page.

#### C.1 General recommendation table

|  | **General Recommendations (Phenocopy not an issue)** | | |
|---|---|---|---|
|  | **Supporting** | **Moderate** | **Strong** |
| **Likelihood** | 4:1 | 16:1 | 32:1 |
| **LOD Score** | 0.6 | 1.2 | 1.5 |
| **Autosomal dominant threshold** | 2 affected segregations | 4 affected segregations | 5 affected segregations |
| **Autosomal recessive threshold** | See Table 2 | See Table 2 | See Table 2 |

> ACADVL is autosomal recessive, so the "Autosomal recessive threshold" row applies and directs the user to Table 2 (the LOD grid, C.2). The autosomal dominant row is reproduced only for completeness.

#### C.2 Table 2 — LOD score grid (General Recommendations, Phenocopy not an issue)

Rows = **Affected segregations** (0-10); columns = **Unaffected segregations** (0-10). Cell values are LOD scores. **This is a lookup table:** compute affected and unaffected segregation counts per the PP1 definitions, read the LOD score, then apply the PP1 strength thresholds (Supporting ≥0.60, Moderate ≥1.20, Strong ≥1.50).

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

**Colour coding in the source image** (green = Supporting, orange = Moderate, pink/red = Strong). The shaded cells are:
- **Green (Supporting)**: row 0 columns 5-9 (0.62, 0.75, 0.87, 1, 1.12); row 1 columns 0-4 (0.6, 0.73, 0.85, 0.98, 1.1).
- **Orange (Moderate)**: row 0 column 10 (1.25); row 1 columns 5-7 (1.23, 1.35, 1.48); row 2 columns 0-2 (1.2, 1.33, 1.45).
- **Pink (Strong)**: row 1 columns 8-10 (1.6, 1.73, 1.85); row 2 columns 3-10 (1.58 onward); all of rows 3-10.
- Row 0 columns 0-4 (0-0.5) are unshaded — below the Supporting threshold.

> The shading is consistent with the stated LOD thresholds except that the value 1.48 (row 1, unaffected 7) is shaded orange/Moderate although 1.48 < 1.50, which is correct, and 1.58 (row 2, unaffected 3) is pink/Strong although the Moderate band is <1.50 — also correct. No shading/threshold conflict was found.

---

### Appendix D - PS3 / BS3 evaluation flowchart

Source: `PS3 and BS3 flowchart.pdf`, 1 page. Same *Version 1* document header and "Date Approved: November 8, 2021" footer as the PP1 file. The flowchart is a raster image with no text layer; transcribed from the rendered page. It is the ClinGen SVI functional-evidence framework (Brnich et al.) as adopted by this VCEP.

**Step 1 — Define the disease mechanism**

**Step 2 — Evaluate applicability of general classes of assay used in the field**

| Question | Answer | Result |
|---|---|---|
| Does the general class of assay model pathogenesis/disease mechanism? | NO | **Do not use PS3/BS3** |
| Does the general class of assay model pathogenesis/disease mechanism? | YES | → Step 3 |

**Step 3 — Evaluate validity of specific instances of assays**

| Question | Answer | Next |
|---|---|---|
| Were basic controls included? (Normal/Negative/Wild type; Abnormal/Positive/Null) **AND** were multiple replicates used? | YES | → "Were variant controls used?" |
| Were basic controls included? … AND were multiple replicates used? | NO | → "Has the class of assay been…?" |
| Has the class of assay been: broadly accepted historically / previously validated **OR** provided as a kit with defined performance metrics, but where controls/replicates are not documented for the specific instance of the assay? | NO | **Do not use PS3/BS3** |
| Has the class of assay been … ? | YES | **Max PS3_supporting / Max BS3_supporting** |
| Were variant controls used?\* (Known pathogenic; Known benign) <br>\*Or were variants tested that reach P/LP or B/LB without PS3/BS3 criteria? | NO | **Max PS3_supporting / Max BS3_supporting** |
| Were variant controls used?\* | YES | → Step 4 |

**Step 4 — Apply evidence to individual variant interpretation**

| Question | Answer | Result |
|---|---|---|
| Are the statistical analyses sufficient to estimate or calculate OddsPath? | YES | Correlate the strength of evidence to the calculated OddsPath (Table 1) → **Max PS3_very_strong / Max BS3** |
| Are the statistical analyses sufficient to estimate or calculate OddsPath? | NO | → "How many total benign/pathogenic variant controls were used?" |
| How many total benign/pathogenic variant controls were used? | 10 or less in total | **Max PS3_supporting / Max BS3_supporting** |
| How many total benign/pathogenic variant controls were used? | At least 11 in total | **Max PS3_moderate / Max BS3_moderate** |

> **"Table 1" (the OddsPath-to-strength correlation) is referenced by the flowchart but is not reproduced in the flowchart PDF, in the main specification, or in any other distributed supplementary file.** The OddsPath-to-strength mapping is **not specified by this VCEP; consult the referenced external guidance** (ClinGen SVI functional evidence recommendations, https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-019-0690-2, as cited in the PS3 functional assay workbook).

---

### Appendix E - PS3 functional assay evaluation spreadsheet

Source: `PS3 functional assay.xlsx`, 5 sheets, no embedded images. This is the SVI functional-assay documentation template. It is a **per-publication lookup**: each column is one "specific instance" (a publication) of a general assay class (one sheet per class); read down a column to see whether that instance is an approved assay and at what strength.

#### E.1 Sheet "Instructions" (verbatim)

> In December 2019, ClinGen published recommendations for application of the functional evidence PS3/BS3 criterion using the ACMG/AMP sequence variant interpretation framework (https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-019-0690-2). This guidance should be incorporated into ClinGen VCEP specifications.
>
> The SVI functional assay evaluation group has put together this spreadsheet to assist you in presenting your work on PS3/BS3. This spreadsheet attempts to document the steps of the validation requirements that were outlined in the SVI paper on this topic (https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-019-0690-2). This spreadsheet is meant to give your VCEP a way to document the general functional assays that are used in your field, and to evaluate specific instances of those assays.
>
> Basic instructions:
> Fill out one spreadsheet per gene.
> Each tab should be used for a "general class of assay" (e.g. "Cellular growth assay" or "Radioligand binding assay" etc.) and each column should represent one "specific instance" (typically a publication) that uses that type of assay.
> You can use multiple columns to document specific examples of assays that do meet your VCEPs criteria for inclusion (and at what strength) as well as those that you evaluated but do not meet your threshold for PS3/BS3. This will also help the SVI to compare the rigor of the controls that were used in each specific instance and the degree of clinical validation (the "known" controls that were evaluated in the assay).

#### E.2 Row legend (identical across the four assay sheets)

PMID · DOI / link · Author · Year · Assay (general description) · Material used (patient cells, engineered variants, cell lines, animal model, etc.) · Readout type (qualitative/quantitative) · Readout description · Biological replicates (met/not met) · Technical replicates (met/not met); description · Basic positive control (met/not met); description · Basic negative control (met/not met); description · Validation controls P/LP (#) · Validation controls B/LB (#) · Statistical analysis (general description) · Threshold for normal readout · Threshold for abnormal readout · **Approved assay (y/n)** · **Proposed strength**

#### E.3 Sheet "Enzyme activity" — approval summary

| PMID | Author | Year | Assay | Material | Approved assay (y/n) | Proposed strength |
|---|---|---|---|---|---|---|
| 30194637 | Hesse | 2018 | Palmitoyl-CoA oxidation | Patient fibroblasts and lymphocytes | **N** | Assay performed in patient cells, count under PP4 |
| 8554073 | Souri | 1996 | Palmitoyl-CoA oxidation | Transfected and selected (with G418) CHO cells | **Y** | Supporting |
| 17374501 | Goetzman (Vockley lab) | 2007 | Enzyme activity C16-CoA | Bacterial expression/purification | **Y** | Supporting |
| 33986768 | Remec | 2021 | *(blank)* | Patient lymphocytes | **N** | Assay performed in patient cells, count under PP4 |
| 11914034 | Takusa | 2002 | Palmitoyl-CoA oxidation | SV40 transformed VLCAD null fibroblasts transfected with plasmid | **Y** | Supporting |
| 23480858 | Schiff (Vockley lab) | 2013 | Fatty acid oxidation | Bacterial expression/pufication (figure 3) | **N** (only western blot for fig 3, other assays in patient fibroblasts) | Other assays performed in patient cells, count under PP4 |
| 9461620 | Souri | 1998 | Palmitoyl-CoA oxidation | Baculovirus expression system | **Y** | Supporting |
| 10790204 | Watanabe | 2000 | Palmitoyl-CoA oxidation | SV40 transformed VLCAD null fibroblasts transfected with plasmid | **Y** (only for fig. 4, other assays in patient cells) | Supporting |
| 20060901 | Gobin-Limballe | 2010 | Palmitoyl-CoA oxidation | Patient fibroblasts | **N** | Assay performed in patient cells, count under PP4 |
| 35218577 | D'Annibale | 2022 | Palmitoyl-CoA oxidation | VLCAD null HEK293 and VLCAD null fibroblasts transfected | **Y** | Supporting |
| 33150772 | Chen | 2020 | Palmitoyl-CoA oxidation | HEK293 transfection | **Y** | supporting |

Validation-parameter detail for the same columns (in column order above):

| Row | 30194637 | 8554073 | 17374501 | 33986768 | 11914034 | 23480858 | 9461620 | 10790204 | 20060901 | 35218577 | 33150772 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Readout type | Quantitative | Quantitative | Quantitative | Quantitative | Quantitative | Quantitative | Quantitative | Quantitative | Quantitative | Quantitative | Quantitative |
| Readout description | Residual activity is the % of the mean of healthy controls | Read out is in mU/mg | Read out is mU/mg | Read out is umol/L | Read out is nmol/min/mg | Read out is % of WT | Read out is units/mg | Read out is nmol/min/mg | nmol 3H FA/h/mg | Average activity | Relative FAO compared to Control |
| Biological replicates | not met | met; expression, pulse-chase, gel filtration (for dimers) | not met | not met | met; western blotting | met; western blotting | not met | met; western blotting | met; western blotting | met; western blotting | met; FAO, dimer formation |
| Technical replicates | met; triplicate | met; triplicate | met; triplicate | unclear | met; triplicate | not met, appears to be one | unclear | unclear | met; triplicate repeated 2-3 times | met; triplicate | met; triplicate |
| Basic positive control | not met | met; VLCAD transfected | met; WT expression | not met | met; WT expression | met; WT expression | met; WT expression | met; WT expression | met; WT expression | met; WT expression | WT ACADVL |
| Basic negative control | met; unaffected individuals | met; transfected with empty plasmid | not met | not met | met; mock transfection | not met | not met | met; mock transfection | not met | met; ACADVL null | Mock control |
| Validation controls P/LP (#) | 0 | 0 | 2 (R429W, R573W) | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| Validation controls B/LB (#) | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Statistical analysis | not done | standard deviation | standard deviation | unclear | standard deviation | not done | not done | unclear | unclear | standard deviation | standard deviation |
| Threshold for normal readout | 12.2+/-1.6 mU/mg | 11.2+/-.29 mU/mg | 200 mU/mg | not clear | 100% (normalized for WT) | 100% (normalized for WT) | not done | not done | not done | not done | not done |
| Threshold for abnormal readout | 20% activity | No threshold set | No threshold set | Not clear | No threshold set | No threshold set | not done | not done | not done | not done | not done |

> Note the columns for 23480858 and 11914034 are in the sheet order shown; the "Assay (general description)" cell for PMID 33986768 (Remec 2021) is **blank** in the source.

#### E.4 Sheet "Protein reduction by western"

| PMID | Author | Year | Assay | Material | Approved assay (y/n) | Proposed strength |
|---|---|---|---|---|---|---|
| 35218577 | D'Annibale | 2022 | Western blot, total protein production | VLCAD null HEK293 and VLCAD null fibroblasts transfected | **Y** | Supporting |
| 11914034 | Takusa | 2002 | Western blot | SV40 transformed VLCAD null fibroblasts transfected with plasmid | **Y** | Supporting |
| 23480858 | Schiff (Vockley lab) | 2013 | Western blot | Bacterial expression/pufication (figure 3) | **Y** (only for fig 3, other assays in patient fibroblasts) | Supporting |
| 10790204 | Watanabe | 2000 | Western blot | SV40 transformed VLCAD null fibroblasts transfected with plasmid | **Y** (only for fig. 4, other assays in patient cells) | Supporting |
| 20060901 | Gobin-Limballe | 2010 | Western blot | Patient fibroblasts | **N** | Assay performed in patient cells, count under PP4 |
| 35218577 *(duplicate column)* | D'Annibale | 2022 | Western blot | VLCAD null HEK293 and VLCAD null fibroblasts transfected | **Y** | Supporting |

| Row | 35218577 | 11914034 | 23480858 | 10790204 | 20060901 | 35218577 (dup) |
|---|---|---|---|---|---|---|
| Readout type | Quantitative | Qualitative | Qualitative | Qualitative | Qualitative | Quantitative |
| Readout description | Relative expression | Relative expression | Relative expression | Relative expression | Relative Expression | Relative expression |
| Biological replicates | met; enzyme activity | met; Palmitoyl-CoA oxidation | met; fatty acid oxidation | met; Palmitoyl-CoA oxidation | met; Palmitoyl-CoA oxidation | met; Palmitoyl-CoA oxidation |
| Technical replicates | not met | not met | not met | not met | not met | not met |
| Basic positive control | met; WT expression | met; WT expression | met; WT expression | met; "normal" expression | met; control expression | met; WT expression |
| Basic negative control | met; ACADVL null | met; mock transfection | not met | met; mock transfection | not met | met; ACADVL null |
| Validation controls P/LP (#) | 1 | 0 | 0 | 0 | 0 | 1 |
| Validation controls B/LB (#) | 0 | 0 | 0 | 0 | 0 | 0 |
| Statistical analysis | standard deviation | none | none | none | none | standard deviation |
| Threshold for normal readout | not done | not done | not done | not done | not done | not done |
| Threshold for abnormal readout | not done | not done | not done | not done | not done | not done |

#### E.5 Sheet "dimer formation"

| Field | Value |
|---|---|
| PMID | 33150772 |
| DOI / link | DOI: 10.1631/jzus.B2000339 |
| Author / Year | Chen, 2020 |
| Assay | dimer formation |
| Material used | HEK293 transfection |
| Readout type | Quantitative |
| Readout description | Relative dimer formation compared to Control |
| Biological replicates | met; FAO |
| Technical replicates | Not met |
| Basic positive control | WT ACADVL |
| Basic negative control | Mock control |
| Validation controls P/LP (#) | 1 |
| Validation controls B/LB (#) | 0 |
| Statistical analysis | standard deviation |
| Threshold for normal readout | not done |
| Threshold for abnormal readout | not done |
| **Approved assay (y/n)** | **Y** |
| **Proposed strength** | supporting |

#### E.6 Sheet "Protein stability"

| Field | Value |
|---|---|
| PMID | 8554073 |
| DOI / link | https://pmc.ncbi.nlm.nih.gov/articles/PMC1914938/ |
| Author / Year | Souri, 1996 |
| Assay | pulse chase |
| Material used | transfected CHO cells |
| Readout type | qualitative |
| Readout description | Stabilitu versus variant *(typo in source)* |
| Biological replicates | Met, mRNA expression, western |
| Technical replicates | not met |
| Basic positive control | Normal |
| Basic negative control | Not met |
| Validation controls P/LP (#) | 0 |
| Validation controls B/LB (#) | 0 |
| Statistical analysis | None |
| Threshold for normal readout | None |
| Threshold for abnormal readout | None |
| **Approved assay (y/n)** | **Y** |
| **Proposed strength** | Supporting |

DOI/link values for the Enzyme activity sheet, in column order: 10.1007/s10545-018-0245-5 · https://pmc.ncbi.nlm.nih.gov/articles/PMC1914938/ · 10.1016/j.ymgme.2007.01.013 · 10.3389/fgene.2021.648493 · 10.1006/mgme.2002.3297 · 10.1016/j.ymgme.2013.02.002 · 10.1074/jbc.273.7.4227 · 10.1002/(SICI)1098-1004(200005)15:5<430::AID-HUMU4>3.0.CO;2-1 · 10.1016/j.bbadis.2010.01.001 · 10.1002/jimd.12492 · 10.1631/jzus.B2000339

> **Coverage note:** the spec lists five valid assay types for PS3/BS3 (enzyme activity, total protein production, protein stability, dimer formation, **transcript production**). The workbook contains sheets for the first four only; **no sheet documents transcript-production assays.**

---

### Appendix F - Criteria explicitly designated "Not Applicable"

PS2, PS4, PP2, PP5, BS2, BP1, BP3, BP5, BP6.

Of these, PS2, PS4 and BS2 carry **no explanatory comment** in the specification.

### Appendix G - Criteria/strengths not specified by this VCEP

| Item | Status |
|---|---|
| PVS1_Supporting trigger conditions | Not specified by VCEP (level exists, no rule) |
| PVS1 (RNA) strength assignment | Not specified by VCEP |
| PVS1 decision tree footnotes **a** and **b** | Absent from the distributed file — content unknown |
| PS1 splice strength combinations | Not specified by this VCEP; consult Walker et al. 2023 (PMID: 37352859) Table 2 |
| PS3/BS3 OddsPath-to-strength "Table 1" | Not specified by this VCEP; consult ClinGen SVI functional evidence recommendations |
| PM4 (Moderate) detail; PM4 Supporting | Delegated to ACMG/AMP and SVI working group / not specified |
| PM6 strengths other than Moderate | Not specified by VCEP |
| BS4 detail | Delegated to ACMG/AMP and SVI working group |
| Mutation Taster thresholds (PP3, BP4) | Not specified by VCEP |
| REVEL interval ≥0.5 to ≤0.75 | Not specified by VCEP |
| SpliceAI Δ interval >0.2 to <0.5 | Not specified by VCEP |
| PP4: enzyme activity >27%, interval >20-<21%, NBS C14:1 <0.8 μM | Not specified by VCEP |
| PS2/PM6 point matrix | **Does not exist in this specification** |
| Point-based (Tavtigian) classification scheme | **Does not exist in this specification** — combining is by the Richards et al. 2015 rules only |

---

### Appendix H - Source typos, internal inconsistencies, and apparent VCEP errors

All items below are transcribed as they appear in the source; nothing has been silently corrected.

1. **Version metadata is stale.** The document is Version 2.2 (Released 7/20/2026), but the *Description* field describes only versions "2.0" and "2.0.1", and the *General Comments* field reads "Version 2.0". No description text for versions 2.1 or 2.2 is given other than the release notes.
2. **Release-note duplication/contradiction.** The Description says "6/11/26 the VCEP added that PVS1 + PM2 (supporting) = Likely Pathogenic"; the Release Notes repeat this and then state "7/14/26 the VCEP **re-added** that PVS1 + PM2 (supporting) = LP". The intervening removal is not documented.
3. **PM1 region list mismatch.** `PM1 table_updated.xlsx` includes **p.460-466 (nucleotide/substrate binding)**; the main specification PDF's PM1 list omits it. Also, the main PDF writes "PMIDs: 20060901" (plural, one PMID) for p.E441 where the spreadsheet writes "PMID: 20060901"; and the main PDF footnote says "HGVS nomenclature" where the spreadsheet says "HGVS numbering".
4. **PVS1 criterion text is identical at all four strengths.** The Very Strong, Strong, Moderate and Supporting entries carry byte-identical boilerplate; only the decision tree differentiates strength. In addition, the Supporting entry's Modification Type reads "Disease specific" (no hyphen) where the other three read "Disease-specific".
5. **BS3 text refers to PS3.** All three BS3 strength entries read "…are valid assays to consider for **PS3**." — apparently a copy/paste from the PS3 entry.
6. **PVS1 exon table, exon 20.** Rationale reads "**7 amino acids**, ~7.2% of total". 7.2% of the 655-amino-acid precursor is ~47 amino acids, and exon 20's 141 coding nt correspond to 47 codons; "7" appears to be a truncation of "47". Transcribed verbatim. Exon 14's rationale also omits the "~" used on every other in-frame row ("5.2% of total").
7. **PVS1 deletion branch, differing critical-exon lists.** For "Disrupts reading frame and is NOT predicted to undergo NMD" the critical exons are listed as **1-2, 8, 10, 13-15, 18**; for "Preserves reading frame" they are **1-2, 10, 13-15, 18** (exon 8 dropped). The specification does not explain the difference.
8. **PVS1 tree footnote markers a and b have no footnote text** anywhere in the 2-page PDF. Their content cannot be recovered from this package.
9. **PP3 SpliceAI exclusion comparator is stated twice with different operators.** "exclude any results with Δ Score **≤ 0.2**" followed immediately by "**<0.2** are not 'predicted to alter splicing'". The two statements disagree at exactly Δ = 0.2.
10. **PP4 table has uncovered ranges.** The enzyme-activity rows cover ≤20% and 21-27%, leaving >20 to <21% and >27% unaddressed; the NBS rows cover 0.8-0.99 μM and (via footnotes) ≥1.0 μM, leaving <0.8 μM unaddressed. Also, footnote (a) states the ≥1.0 μM requirement for PP4_Moderate but **no table row assigns 2 points to NBS C14:1 ≥1.0 μM** — the 2-point NBS rule exists only in the footnote.
11. **PVS1 tree author name typo:** "Aoyamaa T et al., PMID: 7668252" in the decision tree vs. "Aoyama et al., (1995) PMID: 7668252" in the main specification.
12. **PVS1 initiation-codon transcript inconsistency:** the criterion text says "The next in-frame methionine is at position 6 (on transcript **NM_000018**)" — without a version suffix — while the rest of the specification uses NM_000018.4.
13. **PP1 and PS3/BS3 supplementary files are Version 1 fragments.** Both `PP1 tables.pdf` and `PS3 and BS3 flowchart.pdf` carry the header "…Variant Interpretation Guidelines **Version 1**" and footer "Date Approved: **November 8, 2021**" / "ClinGen_ACADVL_ACMG_Specifications_v1". They have not been re-versioned for v2.2. `PP1 tables.pdf` also includes a stray trailing fragment of the v1 document (the words "consanguineous families." and an unrelated greyed-out PP2 heading) around the tables.
14. **PS3 functional assay workbook.** The "Protein reduction by western" sheet contains **two identical columns for PMID 35218577 (D'Annibale 2022)** — a duplicated column. The "Enzyme activity" sheet has a **blank** "Assay (general description)" cell for PMID 33986768 (Remec 2021). Typos in the workbook: "Bacterial expression/**pufication**" (twice), "**Stabilitu** versus variant". No sheet exists for **transcript production**, although the specification names it as a valid PS3/BS3 assay type.
15. **PP3 wording:** "Missense changes with a REVEL **scores** >0.75 will meet PP3" (singular/plural disagreement) and "PP3 can be applied if there is, a SpliceAI 'high score'" (stray comma).
16. **PM3 homozygous row.** The PM3 table assigns 0.5 points to a homozygous occurrence under the "Confirmed in trans" column (with "Phase unknown" = N/A), while the criterion text states "Parental testing is not required for homozygous cases" — i.e. homozygous cases are always scored in the "confirmed in trans" column by construction. Not an error, but the column heading is potentially confusing.
17. **PM5_Strong has no worked example.** The main specification gives illustrative examples for PM5_Moderate and PM5_Supporting only; the ≥2.0-point Strong tier is defined solely in `PM5 table.xlsx`.

---

## Version History

| Version | Date | Notes |
|---|---|---|
| 1 | November 8, 2021 (Date Approved) | Original ACADVL VCEP specification (referenced by the PP1 and PS3/BS3 supplementary files, which are still v1 documents) |
| 2.0 | — | "The VCEP reviewed all the codes and updated wording." |
| 2.0.1 | — | "The VCEP updated the wording for PP3 and BP4 to only include reference to the Splice AI tool." |
| — | 6/11/2026 | "the VCEP added that PVS1 + PM2 (supporting) = Likely Pathogenic" |
| — | 7/14/2026 | "the VCEP re-added that PVS1 + PM2 (supporting) = LP; No pilot classifications changed due to this added rule." |
| **2.2** | **7/20/2026** | Current version. DOI 10.5281/zenodo.21457671. |

The specification's own metadata does not describe a version 2.1 release.

---

*This document was compiled from the ClinGen VCEP specification (GN021, ACADVL v2.2) and its eight distributed supplementary files. For the most current version, please refer to the ClinGen website.*
