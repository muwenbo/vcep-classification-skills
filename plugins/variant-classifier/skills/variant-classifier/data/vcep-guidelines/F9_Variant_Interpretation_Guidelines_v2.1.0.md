# ClinGen Coagulation Factor Deficiency VCEP Variant Interpretation Guidelines for F9

**Version:** 2.1 (registry label; the spec's own Release Notes text refers to "v2.1.0" — see [Version History](#version-history))
**Released:** 4/16/2026
**Affiliation:** Coagulation Factor Deficiency VCEP
**Specification type (as stated by VCEP):** Tavtigian et.al., 2020 - Bayesian adaptation of Richards et.al., 2015
**Description (as stated by VCEP):** Rule specifications for hemophilia B.
**DOI:** 10.5281/zenodo.21433987
**ClinGen VCEP ID:** GN080

**Source basis:** This document was compiled only from the ClinGen criteria specification PDF
`ClinGen_ACMG_Specifications_F9_v2.1.pdf` and the five supplementary files distributed with it
(see [Appendix E](#appendix-e--source-file-inventory)). Nothing outside that package has been added.
Where the VCEP defers to external guidance without reproducing it, that is stated explicitly rather than filled in.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | F9 (HGNC:3551) |
| **HGNC Name** | coagulation factor IX |
| **Transcript** | NM_000133.4 |
| **Disease** | hemophilia B (MONDO:0010604) |
| **Inheritance** | X-linked inheritance |

**General Comments (verbatim from spec):** "When pathogenic and benign rule codes are applied, see guidance
below for the point counting variant classification system rather than defer to classification of variant of
uncertain significance."

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
2. [Benign Criteria](#benign-criteria)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)
   - [Appendix A — PVS1 Decision Tree](#appendix-a--pvs1-decision-tree)
   - [Appendix B — De Novo (PS2/PM6) Point Guidance](#appendix-b--de-novo-ps2pm6-point-guidance)
   - [Appendix C — Approved Functional Assays (PS3/BS3)](#appendix-c--approved-functional-assays-ps3bs3)
   - [Appendix D — Pilot Study Results (F9)](#appendix-d--pilot-study-results-f9)
   - [Appendix E — Source File Inventory](#appendix-e--source-file-inventory)
   - [Appendix F — Source Typos, Gaps and Internal Inconsistencies](#appendix-f--source-typos-gaps-and-internal-inconsistencies)
5. [Version History](#version-history)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation
codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specifications (verbatim):** "Apply the ClinGen Coagulation Factor Deficiency VCEP/SVI decision tree to
determine use and strength of the PVS1 rule. PVS1 (RNA): assays demonstrating a variant leads to aberrant
splicing profile that can be used in the PVS1 decision tree as described in Walker et al. (PMID: 36865205)
that was added to the v1 CFD-VCEP PVS1 flowchart. If using PVS1(RNA), do not apply PP3."

#### Strength Levels

| Strength | Criteria | Default Point Value | Modification Type |
|----------|----------|---------------------|-------------------|
| **Very Strong** | Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree. | 8 | Gene-specific |
| **Strong** | Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree. | 4 | Gene-specific |
| **Moderate** | Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree. | 2 | Gene-specific |
| **Supporting** | Per Coagulation Factor Deficiency VCEP/SVI PVS1 decision tree. | 1 | Gene-specific |

The decision tree itself is transcribed in [Appendix A](#appendix-a--pvs1-decision-tree). Note that the
distributed decision tree assigns only PVS1, PVS1_Strong, PVS1_Supp, BP7_Strong and N/A outcomes; it does
not contain any PVS1_Moderate endpoint even though the spec defines a Moderate point value.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of
nucleotide change.

**VCEP Specifications:** No separate VCEP preamble; specifications are given per strength level.

| Strength | Criteria (verbatim) | Default Point Value | Modification Type |
|----------|---------------------|---------------------|-------------------|
| **Strong** | "This evidence code can be applied when there is 1 pathogenic variant or 2 likely pathogenic variants at the same residue based on F9 gene rule specifications from the Coagulation Factor Deficiency VCEP and where in silico predictors do not suggest a splicing defect. OR When two or more variants are share the same predicted splicing effect and one comparison splicing variant reaches a pathogenic classification or 2 comparison variants reach a likely pathogenic classification using the Coagulation Factor Deficiency VCEP specifications modified from Walker, et al 2023 (PMID: 37352859)." *[sic: "are share"]* | 4 | General recommendation |
| **Moderate** | "This evidence code can be applied when there is 1 likely pathogenic variants at the same residue based on F9 gene rule specifications from the Coagulation Factor Deficiency VCEP and where in silico predictors do not suggest a splicing defect. OR When the comparison variant shares the same predicted splicing effect and the comparison splicing variant reaches a likely pathogenic classification using the Coagulation Factor Deficiency VCEP specifications based on Walker, et al 2023 (PMID: 37352859)." *[sic: "1 likely pathogenic variants"]* | 2 | General recommendation |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and
no family history.

**VCEP Specifications (verbatim):** "Use ClinGen's de novo modified point system for a highly specific
phenotype (see guidance below). Combine all assumed and confirmed de novo cases for this code and use at the
appropriate strength based on amount of points for all probands. Probands must meet the PS4 phenotype criteria
to apply this code."

| Strength | Criteria (verbatim) | Default Point Value | Modification Type |
|----------|---------------------|---------------------|-------------------|
| **Very Strong** | "Use the SVI recommendations for de novo cases; 4 points. Use de novo guidance below to determine point value." | 8 | Disease-specific |
| **Strong** | "Use the SVI recommendations for de novo cases; 2 points. Use de novo guidance below to determine point value." | 4 | Disease-specific |
| **Moderate** | "Use the SVI recommendations for de novo cases; 1 point. Use de novo guidance below to determine point value." | 2 | Disease-specific |
| **Supporting** | "Use the SVI recommendations for de novo cases; 0.5 point. Use de novo guidance below to determine point value." | 1 | Disease-specific |

> **Two different point scales are in play here and must not be confused.** The "4 / 2 / 1 / 0.5 points" figures
> are *de novo evidence points* accumulated across probands (Appendix B, Table 2). The "Default Point Value"
> column is the *Tavtigian classification point value* contributed by the resulting code strength.

The de novo point system is distributed with this specification and is transcribed in
[Appendix B](#appendix-b--de-novo-ps2pm6-point-guidance). PM6 is folded into PS2 (see [PM6](#pm6---de-novo-assumed)).

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging
effect on the gene or gene product.

**VCEP Specifications (verbatim):** "See functional study spreadsheet."

| Strength | Criteria | Default Point Value | Modification Type |
|----------|----------|---------------------|-------------------|
| **Very Strong** | Not specified by VCEP (no such level defined) | — | — |
| **Strong** | Not specified by VCEP (no such level defined) | — | — |
| **Moderate** | Not specified by VCEP (no such level defined) | — | — |
| **Supporting** | "Abnormal factor IX activity level (<40 IU/dL or 40%) in a cell line and/or mouse model. --OR-- Abnormal factor IX activity level (<40 IU/dL or 40%) studied in an animal model setting other than mouse (i.e. – bovine factor IX activity levels compared to factor X levels). --OR-- Absent or significantly reduced factor IX antigen level compared to wildtype using conformation-specific reporter assay in cell lines." | 1 | Disease-specific |

**Comparator:** the factor IX activity threshold is **strict** (`< 40 IU/dL or 40%`); a value of exactly 40%
does not meet PS3.

In v2.1 all assays were downgraded to supporting weight (see Release Notes). Approved assay instances are in
[Appendix C](#appendix-c--approved-functional-assays-ps3bs3).

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased
compared to the prevalence in controls.

**VCEP Specifications (verbatim):**

> "Hemophilia B phenotype requirements:
> -Abnormal factor IX activity levels in the severe, moderate or mild range (< 40% factor IX activity level)
> are sufficient to confer a diagnosis.
> - It is reasonable to expect that genomic data from individuals with hemophilia B could be used in population
> databases. Therefore, we decided to implement use of a ratio of hemizygotes found to harbor a variant of
> interest by the total number of alleles in XY individuals in that population database (# of hemizygotes with
> variant of interest/total # of alleles from XY individuals sequenced in the database) as a criteria for using
> the PS4 code. The PS4 code is only applicable to variants with a ratio lower than or equal to 1.26 x 10-5.
> This ratio was set by using the most frequently seen pathogenic variant, F9 c.316G>A, p.Gly106Ser, in gnomAD
> that was studied in the Coagulation Factor Deficiency VCEP pilot F9 study."

**Comparators:**
- Phenotype: factor IX activity `< 40%` — **strict**.
- Population gate: hemizygote ratio `<= 1.26 x 10^-5` — **inclusive** ("lower than or equal to").

| Strength | Criteria (verbatim) | Default Point Value | Modification Type |
|----------|---------------------|---------------------|-------------------|
| **Very Strong** | "≥8 probands meet criteria described below" | 8 | Disease-specific |
| **Strong** | "4-7 probands meet criteria described below" | 4 | Disease-specific |
| **Moderate** | "2-3 probands meet criteria described below" | 2 | Disease-specific |
| **Supporting** | "1 proband meets criteria described below" | 1 | Disease-specific |

A proband counted toward PP4 cannot also be counted toward PS4 (see [PP4](#pp4---phenotype-specificity)).

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional
domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications (verbatim):** "The combined weight of codes PM1 and PM5 applied for a single variant can
only equal strong."

| Strength | Criteria (verbatim) | Default Point Value | Modification Type |
|----------|---------------------|---------------------|-------------------|
| **Strong** | "This code can be used for variants affecting any of the 3 catalytic residues (H267, D315 or S411) and 2 activation residues (R191-A192 and R226-V227) in the F9 gene (PMID: 12554099)." | 4 | Gene-specific |
| **Moderate** | "This code should be applied when the variant is within exons 3, 4 or 5." | 2 | Gene-specific |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome
Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications (verbatim):** "none"

| Strength | Criteria (verbatim) | Default Point Value | Modification Type |
|----------|---------------------|---------------------|-------------------|
| **Supporting** | "Variant must be absent in males in population databases, such as gnomAD." | 1 | Disease-specific |

**Comparator:** absolute absence in males (zero hemizygous observations); no numeric frequency cutoff is given.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Status: Not Applicable.** VCEP comment (verbatim): "Not applicable for the F9 gene."

No PM3 point system is defined by this VCEP.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region
or stop-loss variants.

**VCEP Specifications:** The "VCEP Specifications" field in the source contains only a single period
character (`.`) — i.e. no specification text. See [Appendix F](#appendix-f--source-typos-gaps-and-internal-inconsistencies).

| Strength | Criteria (verbatim) | Default Point Value | Modification Type |
|----------|---------------------|---------------------|-------------------|
| **Moderate** | "Use code with no specification." | 2 | None |
| **Supporting** | Not specified by VCEP (no such level defined) | — | — |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change
determined to be pathogenic has been seen before.

**VCEP Specifications (verbatim):** "The combined weight of codes PM1 and PM5 applied for a single variant can
only equal strong."

| Strength | Criteria (verbatim) | Default Point Value | Modification Type |
|----------|---------------------|---------------------|-------------------|
| **Moderate** | "This evidence code can be applied when there is 1 pathogenic variant or 2 likely pathogenic variants at the same residue based on F9 rule specification from the Coagulation Factor Deficiency VCEP and where in silico predictors do not suggest a splicing defect." | 2 | Gene-specific |
| **Supporting** | "This evidence code can be applied when there is 1 likely pathogenic variant at the same residue based on F9 rule specifications Coagulation Factor Deficiency VCEP and where in silico predictors do not suggest a splicing defect. A "highly suspicious" VUS is defined as a variant that is 1 supporting code away from reaching a likely pathogenic classification." | 1 | Gene-specific |

> The "highly suspicious VUS" definition appears in the PM5_Supporting text but the term "highly suspicious"
> is never used in any criterion in this specification. Transcribed as written; flagged in Appendix F.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**Status: Not Applicable (as a standalone code).** VCEP comment (verbatim): "This rule code is combined with
PS2. Please combined assumed de novo cases with confirmed de novo cases and apply PS2 at the appropriate
weight." *[sic: "Please combined"]*

Assumed de novo observations are scored using the "Assumed de novo" column of
[Appendix B, Table 1](#appendix-b--de-novo-ps2pm6-point-guidance) and contribute to PS2.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene
definitively known to cause the disease.

**VCEP Specifications (verbatim):** "Base strength of rule code on number of meioses across one or more families."

| Strength | Criteria (verbatim) | Default Point Value | Modification Type |
|----------|---------------------|---------------------|-------------------|
| **Strong** | "This code is applicable when there ≥4 meioses across ≥2 families." *[sic: missing "are"]* | 4 | Disease-specific |
| **Moderate** | "This code is applicable when there are at least 3 meioses across one or more families." | 2 | Disease-specific |
| **Supporting** | "This code is applicable when there 2 meioses in one family OR 1 meiosis between 2 affected siblings." *[sic: missing "are"]* | 1 | Disease-specific |

**Comparators:** Strong `>= 4` meioses across `>= 2` families (inclusive); Moderate "at least 3" (inclusive);
Supporting exactly 2 meioses in one family, or 1 meiosis between 2 affected siblings.

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and
where missense variants are a common mechanism of disease.

**Status: Not Applicable.** VCEP comment (verbatim): "Not applicable for F9."

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or
gene product (conservation, evolutionary, splicing impact, etc.).

**VCEP Specifications (verbatim):** "Do not apply PP3 for variants that meet criteria for a PVS1_RNA rule code."

| Strength | Criteria (verbatim) | Default Point Value | Modification Type |
|----------|---------------------|---------------------|-------------------|
| **Supporting** | "Code can be applied for variants where the REVEL score is greater than or equal to 0.6 or a SpliceAI score of greater than or equal to 0.2." | 1 | Gene-specific |

**Comparators:** REVEL `>= 0.6` — **inclusive**; SpliceAI `>= 0.2` — **inclusive**. The two are combined with OR.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single
genetic etiology.

**VCEP Specifications (verbatim):**

> "Hemophilia B phenotype requirements:
> -Abnormal factor IX activity levels in the severe, moderate or mild range (< 40% factor IX activity level)
> are sufficient to confer a diagnosis.
> -A proband must have had full gene sequencing and deletion/duplication analysis to apply this code.
> -A proband used for this code cannot be applied towards the PS4 count."

| Strength | Criteria (verbatim) | Default Point Value | Modification Type |
|----------|---------------------|---------------------|-------------------|
| **Moderate** | "Proband must meet hemophilia B phenotype criteria AND have full gene sequencing and deletion/duplication analysis." | 2 | Disease-specific |

**Comparator:** factor IX activity `< 40%` — **strict**.

No PP4 proband-count point system is defined by this VCEP.

---

### PP5 - Reputable Source

**Status: Not Applicable.** Verbatim: "This criterion is not for use as recommended by the ClinGen Sequence
Variant Interpretation VCEP Review Committee. PubMed : 29543229"

---

## Benign Criteria

### BA1 - Allele Frequency

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome
Aggregation Consortium.

**VCEP Specifications (verbatim):** "99.99% CI; subpopulation must have a minimum of five variant alleles
present. Males and females are included for this code."

| Strength | Criteria (verbatim) | Default Point Value | Modification Type |
|----------|---------------------|---------------------|-------------------|
| **Stand Alone** | "MAF cutoff of greater than or equal to 0.0000556 (or 0.00556%)." | Not Applicable | Gene-specific |

**Comparator:** MAF `>= 0.0000556` (5.56 x 10^-5) — **inclusive**. Requires 99.99% CI and a minimum of five
variant alleles in the subpopulation.

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications (verbatim):** "99.99% CI; subpopulation must have a minimum of five variant alleles
present. Males and females are included for this code."

| Strength | Criteria (verbatim) | Default Point Value | Modification Type |
|----------|---------------------|---------------------|-------------------|
| **Strong** | "MAF cutoff of greater than or equal to 0.00000556 (or 0.000556%)." | -4 | Gene-specific |

**Comparator:** MAF `>= 0.00000556` (5.56 x 10^-6) — **inclusive**. This is exactly one tenth of the BA1
cutoff. Requires 99.99% CI and a minimum of five variant alleles in the subpopulation.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant
(heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications (verbatim):** "none"

| Strength | Criteria (verbatim) | Default Point Value | Modification Type |
|----------|---------------------|---------------------|-------------------|
| **Strong** | "This evidence code can be used when a F9 variant is observed in a male with a normal factor IX activity level (at least >40% IU or as defined by laboratory cut off)." | -4 | Disease-specific |

**Comparator:** the source writes "at least >40% IU", which mixes an inclusive phrase ("at least") with a
strict operator (">"). The operative written operator is **strict `> 40%`**, and the criterion permits a
laboratory-defined cutoff instead. Flagged in Appendix F. (The Release Notes state "BS2- fixed typo" for v2.1.)

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on
protein function or splicing.

**VCEP Specifications (verbatim):** "none"

| Strength | Criteria (verbatim) | Default Point Value | Modification Type |
|----------|---------------------|---------------------|-------------------|
| **Strong** | "This code can be used for F9 gene variants studied in a cell line or mouse model setting that confer a normal factor IX activity AND normal factor IX antigen levels OR normal Western Blot." | -4 | Disease-specific |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications (verbatim):** "none"

| Strength | Criteria (verbatim) | Default Point Value | Modification Type |
|----------|---------------------|---------------------|-------------------|
| **Strong** | "This evidence code can be used when a F9 variant is observed in a male with a family history of hemophilia B and has a normal factor IX activity level." | -4 | Disease-specific |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment (verbatim) |
|-----------|--------|--------------------|
| **BP1** | Not Applicable | "Not applicable for F9 gene." |
| **BP2** | Not Applicable | "Not being used at this time. There are reports of males with hemophilia having two suspicious pathogenic variants." |
| **BP3** | Not Applicable | "Not applicable for F9 gene." |
| **BP4** | Specified — Supporting (-1, Gene-specific) | VCEP Specifications: "none". Supporting: "This code can be applied for variants reaching a REVEL score of 0.3 or below AND a Splice AI score of less than or equal to 0.1." |
| **BP5** | Not Applicable | "This rule code is not recommended for use at this time. There is no known alternate cause of isolated factor IX deficiency." |
| **BP6** | Not Applicable | "This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. PubMed : 29543229" |
| **BP7** | Specified — Strong (-4) and Supporting (-1) | See below. |

#### BP4 comparators

REVEL `<= 0.3` ("0.3 or below") — **inclusive**; SpliceAI `<= 0.1` — **inclusive**. The two are combined with AND.

#### BP7

**VCEP Specifications (verbatim):** "This code can also be used for non-canonical intronic variants. The use of
BP7 with BP4 is allowed, as appropriate, to classify variants meeting both criteria as likely benign."

| Strength | Criteria (verbatim) | Default Point Value | Modification Type |
|----------|---------------------|---------------------|-------------------|
| **Strong** | "Applicable for variants that have no observable splicing impact with RNA sequencing and/or minigene assay and a SpliceAI score of less than or equal to 0.1." | -4 | General recommendation |
| **Supporting** | "Splicing prediction score of less than or equal to 0.1 is required. Conservation should be assess using PhyloP (cutoff less than 0.1) and PhastCons (cutoff less than 0.5)." *[sic: "should be assess"]* | -1 | Gene-specific |

**BP7 comparators:** SpliceAI `<= 0.1` — **inclusive** (both Strong and Supporting); PhyloP `< 0.1` —
**strict**; PhastCons `< 0.5` — **strict**.

---

## Rules for Combining Criteria

This VCEP does specify combining rules, in two places: the point-range table printed in the specification PDF,
and the distributed supplementary document *Rule Guidance for Combining Pathogenic and Benign Codes*.

### From the specification PDF — "Point Based Variant Classification Categories" (verbatim)

| Category | Point Ranges |
|----------|--------------|
| Pathogenic | 10 |
| Likely Pathogenic | 6-9 |
| Uncertain Significance | 0-5 |
| Likely Benign | -6 - -1 |
| Benign | -7 |

The PDF's "Additional Notes" field for this table is empty.

> The PDF table drops the open-ended operators. The distributed supplement (Tavtigian Table 3, reproduced
> below) supplies them: Pathogenic is `>= 10` and Benign is `<= -7`. Use the supplement's form.

### From the supplementary document (verbatim)

> "F9 Rules for Combining Codes with Conflicting Criteria
>
> For F9 variants where criteria codes for benign and pathogenic evidence apply, these variants are not
> subjected to an automatic variant of uncertain significance (VUS) classification. Instead, we recommend
> application of the rule combination point system described by Tavtigian, et al. 2020 (PMID: 32720330).
>
> Use the Tavtigian, et al. Table 2 below to determine how many points that each evidence code is worth and sum
> those point values:
>
> Then, use the Tavtigian, et al. Table 3 below to determine which variant classification corresponds to the
> summed point value."

**Tavtigian et al. TABLE 2 — Point values for ACMG/AMP strength of evidence categories** (transcribed from the
image embedded in the supplement):

| Evidence Strength | Pathogenic | Benign |
|-------------------|-----------|--------|
| Indeterminate | 0 | 0 (a) |
| Supporting | 1 | -1 |
| Moderate | 2 | -2 (b) |
| Strong | 4 | -4 |
| Very strong | 8 | -8 (b) |

**Tavtigian et al. TABLE 3 — Point-based variant classification categories** (transcribed from the image
embedded in the supplement):

| Category | Point ranges |
|----------|--------------|
| Pathogenic | ≥10 |
| Likely Pathogenic | 6 to 9 (a) |
| Uncertain | 0 to 5 |
| Likely Benign | −1 to −6 (a) |
| Benign | ≤ −7 |

Footnote markers (a) and (b) appear in the reproduced Tavtigian tables, but the supplement reproduces only the
table images — **the footnote texts are not included in the distributed file**. Not specified by this VCEP;
consult Tavtigian et al. 2020 (PMID: 32720330) for the footnotes.

### Additional combination constraints stated elsewhere in the spec

- The combined weight of PM1 and PM5 applied to a single variant can only equal Strong.
- If PVS1(RNA) is applied, PP3 cannot be applied.
- A proband used for PP4 cannot also be counted toward PS4.
- Assumed de novo observations are combined with confirmed de novo observations under PS2; PM6 is not applied
  separately.
- BP7 may be used together with BP4.

No other rules for combining criteria are specified by this VCEP.

---

## Appendices

### Appendix A — PVS1 Decision Tree

Transcribed from the distributed `PVS1 Decision Tree.pptx` (2 slides). Red text in the original is the
F9-specific annotation; it is reproduced inline below.

#### Slide 1 — Sequence/CNV branches

**Nonsense or Frameshift**

| Predicted NMD status | F9-specific boundary | Next test | Outcome |
|---|---|---|---|
| Predicted to undergo NMD | Nonsense up to c.788; Frameshift -1/+2 up to c.730; Frameshift +1/-2 up to c.773 | Exon is present in biologically-relevant transcript(s) | **PVS1** |
| Not predicted to undergo NMD | Nonsense from c.789; Frameshift -1/+2 from c.731; Frameshift +1/-2 from c.774 | Truncated/altered region is critical to protein function — "Several patients with severe hemophilia B reported in the EAHAD database warranting PVS1 - https://f9-db.eahad.org/advance_search_results.php" | **PVS1** |

**GT--AG 1,2 splice sites** (footnote marker "a" in original)

| Branch | F9-specific exons | Next test | Outcome |
|---|---|---|---|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD | Exons 2, 3, 6 | Exon is present in biologically-relevant transcript(s) | **PVS1** |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is **NOT** predicted to undergo NMD | Exon 7 | Truncated/altered region is critical to protein function — several patients with severe hemophilia B in EAHAD warranting PVS1 | **PVS1** |
| Exon skipping or use of a cryptic splice site preserves reading frame | Exons 1, 4, 5 | Truncated/altered region is critical to protein function — "Exons 1 deletion removes signal peptide, exons 4 and 5 encode critical protein domains and variants in all these exons have been seen in patients with severe HB" | **PVS1_Strong** |

**Deletion (single exon to full gene)**

| Branch | Next test | Outcome |
|---|---|---|
| Full gene deletion | (direct) | **PVS1** (footnote marker "d") |
| Single to multi exon deletion – disrupts reading frame and is predicted to undergo NMD (footnote marker "b") | Exon is present in biologically-relevant transcript(s) | **PVS1** |
| Single to multi exon deletion – disrupts reading frame and is **NOT** predicted to undergo NMD (footnote marker "b") | Truncated/altered region is critical to protein function — several patients with severe hemophilia B in EAHAD warranting PVS1 | **PVS1_Strong** |
| Single to multi exon deletion – preserves reading frame | Truncated/altered region is critical to protein function — "Exons 1 deletion removes signal peptide, exons 4 and 5 encode critical protein domains and variants in all these exons have been seen in patients with severe HB" | **PVS1_Strong** |

**Duplication** (≥1 exon in size and must be completely contained within gene)

| Branch | Next test | Outcome |
|---|---|---|
| Proven in tandem | Reading frame disrupted and NMD predicted to occur | **PVS1** |
| Proven in tandem / Presumed in tandem | No or unknown impact on reading frame and NMD | **N/A** |
| Presumed in tandem | Reading frame presumed disrupted and NMD predicted to occur (Exons 1, 4, 5) | **PVS1_Strong** |
| Proven not in tandem | (direct) | **N/A** |

**Initiation Codon**

| Branch | Next test | Outcome |
|---|---|---|
| No known alternative start codon in other transcripts | "No pathogenic variant(s) upstream of closest potential in-frame start codon - in-frame ATGs at codon 6 (c.16; kozak: -3A; +4A), 8 (c.22; kozak: -3A; +4G), (from CCDS); variants at codons 3 and 7 in EAHAD and ClinVar, but with benign or CONF interpretations" | **PVS1_Supp** |

**Slide 1 speaker notes (verbatim):**
> "F9
> Last nonsense variant, c.1369A>T, is near C terminal and leads to severe hemophilia. Most nonsense variants
> in exon 8 result in severe HB (show EAHAD F9 to show all nonsense variants.) Upgrade to PVS1 from strong
> Exon 1 deletion results in severe disease in patients, and removes prepropeptide. Upgrade to PVS1 from strong
> The upgrade to PVS1 may be applicable to other coag factors, at least serine proteases.
> EAHAD – exon 5-8 (severity not specified), 1-6 duplications result in severe disease"

#### Slide 2 — RNA splicing data branch

| Branch | Next test | Outcome |
|---|---|---|
| No variant-specific observed impact for silent/intronic alterations | SpliceAI delta score ≤ 0.1 | **BP7_Strong** |
| Variant-specific impact shown by assay compared to control (for all coding and non-coding variants) | Complete loss of protein (no evidence of normal spliced mRNA) | **PVS1\*** |
| Variant-specific impact shown by assay compared to control (for all coding and non-coding variants) | Near complete loss of protein (some evidence of normal spiced mRNA) *[sic: "spiced"]* | **PVS1_Strong\*** |

\* "When PVS1 is applied using RNA splicing data, PP3 cannot be applied."

**Comparator:** SpliceAI delta score `<= 0.1` — **inclusive**.

**Slide 2 speaker notes (verbatim — note these describe F8, not F9):**
> "F8
> aDownstream of c.6852: 3 variants get to LP or P without PVS1 based on VCEP rules and 2 ClinVar missense
> variants are classified P and therefore warrant use of PVS1 at the strong level.
> bExons 8 and 14, contain all the PM1_Strong residues
> cNext in-frame start codon at 32 (c.96; kozak: -3G; +4G); at least 4 P/LP variants in ClinVar upstream of c.96"

> **Flag:** the flowchart's footnote markers (a, b, d) are defined nowhere for F9. The only footnote
> definitions shipped in the file are the F8 ones above (a, b, c), which refer to F8 coordinates (c.6852,
> exons 8 and 14, codon 32) and cannot be applied to F9. Marker "d" has no definition anywhere in the file.
> The F9 footnote definitions are effectively missing from the distributed source — do not substitute the F8 text.

---

### Appendix B — De Novo (PS2/PM6) Point Guidance

Transcribed from the distributed `Guidance for Combined De Novo Rule Code (PS2_PM6).docx`.

**Document body text (verbatim, in full):**
> "ClinGen SVI Recommendations for Applying de novo Evidence
>
> Use the phenotype consistency "Phenotype highly specific for gene" (1st option) for hemophilia A and B."

The remainder of the document is a single embedded image reproducing the SVI tables. Transcribed:

**Table 1. Points awarded per de novo occurrence**

| Phenotypic consistency | Points per proband — Confirmed de novo | Points per proband — Assumed de novo |
|---|---|---|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity\* | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

\* "Maximum allowable value of 1 may contribute to overall score"

**Table 2. Recommendation for determining the appropriate ACMG/AMP evidence strength level for de novo occurrence(s)**

| Evidence strength | Code label | Total de novo points |
|---|---|---|
| Supporting | PS2_Supporting or PM6_Supporting | 0.5 |
| Moderate | PS2_Moderate or PM6 | 1 |
| Strong | PS2 or PM6_Strong | 2 |
| Very Strong | PS2_VeryStrong or PM6_VeryStrong | 4 |

**How this VCEP applies it:** always use the first row of Table 1 ("Phenotype highly specific for gene") for
hemophilia A and B — i.e. 2 points per confirmed de novo proband and 1 point per assumed de novo proband.
Sum across all probands (confirmed and assumed combined) and read the strength from Table 2. Probands must
meet the PS4 phenotype criteria. The resulting code is always reported as PS2 at the appropriate strength;
PM6 is not used separately by this VCEP.

The source does not state how to handle totals that fall between the Table 2 tiers (e.g. 3 points).
Not specified by this VCEP.

---

### Appendix C — Approved Functional Assays (PS3/BS3)

Transcribed from the distributed `F9 Functional Assays.xlsx`. The workbook has three worksheets:
`Example` (a blank-form template populated with dummy data), `ELISA` (the one real assay record), and
`Sheet2` (empty).

**`Example` worksheet — this is a TEMPLATE, not an approved F9 assay.** It carries placeholder values
(PMID "1234567", DOI "doi:abcd/123", Author "Jones", Year 1985, a HeLa/XYZ-gene survival assay). It is
reproduced here only to document the field structure the VCEP uses to evaluate assays:

PMID; DOI / link; Author; Year; Assay (general description); Material used (patient cells, engineered
variants, cell lines, animal model, etc.); Readout type (qualitative/quantitative); Readout description;
Biological replicates (met/not met); Technical replicates (met/not met), description; Basic positive control
(met/not met), description; Basic negative control (met/not met), description; Validation controls P/LP (#);
Validation controls B/LB (#); Statistical analysis (general description); Threshold for normal readout;
Threshold for abnormal readout; Approved assay (y/n); Proposed strength.

**`ELISA` worksheet — the only approved assay record in the file:**

| Field | Value (verbatim) |
|---|---|
| PMID | 32766856 |
| DOI / link | 10.1182/bloodadvances.2020002520 |
| Author | Gao |
| Year | 2020 |
| Assay (general description) | "Cell-based reporter assay that measures secreted conformation-specific reporter levels and secreted total reporter levels, which corresponds to the FIX protein levels in patients. Protein levels evaluated by ELISA." |
| Material used | HEK293T cells |
| Readout type | quantitative (0-100%) |
| Readout description | FIX-PC quantified by ELISA |
| Biological replicates | met; triplicates |
| Technical replicates | not met |
| Basic positive control | met; WT |
| Basic negative control | not met |
| Validation controls P/LP (#) | "28 variants - to evaluate pathogenicity" |
| Validation controls B/LB (#) | *(blank)* |
| Statistical analysis | none |
| Threshold for normal readout | "Similar to WT (results presented as % of WT)" |
| Threshold for abnormal readout | "Lesser than WT" |
| **Approved assay (y/n)** | **y** |
| **Proposed strength** | **Supporting** |

No BS3-specific assay approvals are listed in this workbook. BS3 is defined only in the specification PDF
(cell line or mouse model, normal factor IX activity AND normal antigen levels OR normal Western Blot).

---

### Appendix D — Pilot Study Results (F9)

Transcribed from the distributed `Pilot Study Results for F8 and F9.xlsx`. The workbook has two worksheets:
`F8 Variants` (39 variants, out of scope for this F9 guideline) and `F9 Variants` (39 variants, below).

**This is a variant-level lookup table, not a rule.** It records how the VCEP classified specific variants
during its pilot. It does not define, extend, or override any criterion above. Use it as a worked-example
reference only; a variant absent from it is not thereby unclassifiable.

**Column structure:** Variant Information | ClinVar/CA ID | ClinVar Classification | ClinVar Star |
VCEP Submitter Classification | Coag EP | Applied Codes | Evidence Summary.

The eighth column, **Evidence Summary**, holds a free-text paragraph per variant (typically 3-8 sentences
citing REVEL scores, gnomAD hemizygote counts, proband counts, meioses and PMIDs, ending in the sentence
"ACMG/AMP criteria applied, as specified by the Coagulation Factor Deficiency Variant Curation Expert Panel
for F9: <codes>"). Those paragraphs are not reproduced here; consult the source workbook for them.

| Variant Information | ClinVar/CA ID | ClinVar Class. | Star | VCEP Submitter Class. | Coag EP | Applied Codes |
|---|---|---|---|---|---|---|
| NM_000133.4(F9):c.1095A>G (p.Ser365=) | 368002 | Benign/Lbenign | 2 | Benign | Benign | BA1, BP4, BP7 |
| NM_000133.3(F9):c.580A>G (p.Thr194Ala) | 10588 | Benign | 2 | Benign | Benign | BA1, BP4 |
| NM_000133.3(F9):c.108C>T (p.Asn36=) | 367998 | Benign/Lbenign | 2 | Benign | Benign | BA1, BP4, BP7 |
| NM_000133.3(F9):c.391+7A>G | 367999 | Benign | 2 | Benign | Benign | BA1 |
| NM_000133.4(F9):c.8G>A (p.Arg3His) | 695909 | Benign/Lbenign | 2 | Likely benign | Benign | BA1 |
| NM_000133.4(F9):c.712T>G (p.Phe238Val) | 1166447 | Pathogenic/Benign | 1 | Likely benign | Benign | BA1 |
| NM_000133.4:c.88+75A>G | CA336128584 | n/a | n/a | Likely benign | Benign | BA1, BP4 |
| NM_000133.4(F9):c.471T>C (p.Cys157=) | 798429 | Likely benign | 1 | Likely benign | VUS | PM2_Supporting, BP4 |
| NM_000133.4(F9):c.60A>G (p.Leu20=) | 701352 | Likely benign/VUS | 1 | Likely benign | Benign | BA1, BP4 and BP7 |
| NM_000133.4(F9):c.19A>T (p.Ile7Phe) | 367997 | Benign/Likely benign | 2 | Likely benign/VUS | Benign | BA1, BS2 |
| NM_000133.4(F9):c.59T>C (p.Leu20Ser) | CA414434363 | n/a | n/a | VUS | Likely pathogenic | PS4, PP3, PM2_Supporting |
| NM_000133.4(F9):c.520G>A (p.Val174Met) | 811516 | Likely pathogenic | 1 | VUS | Likely pathogenic | PM1, PS4_Moderate, PP3, PM2_Supporting |
| NM_000133.4(F9):c.51C>T (p.Ile17=) | 697610 | Benign | 1 | VUS | Benign | BA1 |
| NM_000133.4(F9):c.637A>T (p.Asn213Tyr) | 391981 | VUS | 1 | VUS | VUS | PM2_Supporting |
| NM_000133.3(F9):c.*1110del | 368016 | VUS | 1 | VUS | VUS | PM2_Supporting |
| NM_000133.4(F9):c.155T>C (p.Leu52Ser) | CA414435714 | n/a | n/a | VUS | Likely pathogenic | PM1, PS4_Moderate, PP3, PM2_Supporting |
| NM_000133.4(F9):c.952C>T (p.Leu318Phe) | CA414444915 | n/a | n/a | VUS | Likely pathogenic | PS4, PP3, PM2_Supporting, PM5_Supporting |
| NM_000133.4(F9):c.1235G>A (p.Gly412Glu) | CA414446709 | n/a | n/a | VUS | Pathogenic | PS4_Very Strong, PM1, PP3, PM2_Supporting |
| NM_000133.4(F9):c.86C>T (p.Thr29Ile) | CA414434494 | n/a | n/a | VUS | Likely pathogenic | PS4, PP3, PM2_Supporting |
| NM_000133.4(F9):c.138G>C (p.Arg46Ser) | CA414435594 | n/a | n/a | Likely pathogenic | VUS | PS4_Moderate, PP3, PM2_Supporting, PS3_Supporting |
| NM_000133.3(F9):c.1324G>A (p.Gly442Arg) | 10624 | Pathogenic | 0 | Likely pathogenic | Likely pathogenic | PS4, PP3, PM2_Supporting, PM5_Supporting |
| NM_000133.4(F9):c.277G>A (p.Asp93Asn) | 994410 | Pathogenic | 1 | Likely pathogenic | Likely pathogenic | PS4, PM1, PP3, PM2_Supporting |
| NM_000133.4(F9):c.420A>T (p.Arg140Ser) | CA414438886 | n/a | n/a | Likely pathogenic | Likely pathogenic | PS4_Moderate, PM1, PS3_Supporting, PM2_Supporting |
| NM_000133.3(F9):c.316G>A (p.Gly106Ser) | 10579 | Pathogenic | 2 | Pathogenic/Lpath | Pathogenic | PS4_Very strong, PM1, PP3 |
| NM_000133.4(F9):c.969_975del (p.Pro324CysfsTer2) | CA658820951 | n/a | n/a | Likely pathogenic | Likely pathogenic | PVS1_Strong, PS4_Supporting, PM2_Supporting |
| NM_000133.4(F9):c.1025C>T (p.Thr342Met) | 10607 | Pathogenic/LPath | 2 | Likely pathogenic | Pathogenic | PS4_Very strong, PP3, PM2_Supporting |
| NM_000133.4(F9):c.802T>A (p.Cys268Ser) | 627143 | Likely pathogenic | 1 | Likely pathogenic | VUS | PS4_Moderate, PM2_Supporting, PP3 |
| NM_000133.4(F9):c.88+1G>A | 627155 | Likely pathogenic | 1 | Likely pathogenic | Likely pathogenic | PVS1_Strong, PS4_Supporting, PM2_Supporting |
| NM_000133.4(F9):c.1345C>T (p.Arg449Trp) | 626990 | Pathogenic/LPath/VUS | 1 | Likely pathogenic | VUS | None |
| NM_000133.4(F9):c.835G>A (p.Ala279Thr) | 216926 | Pathogenic/LPath | 2 | Pathogenic/Lpath | Pathogenic | PS4_Very Strong, PM1, PP3, PM2_Supporting |
| NM_000133.3(F9):c.88G>C (p.Val30Leu) | 627400 | Pathogenic | 1 | Likely pathogenic | VUS | PP3, PS4_Supporting, PM2_Supporting |
| NM_000133.4(F9):c.223C>T (p.Arg75Ter) | 10572 | Pathogenic | 2 | Pathogenic | Pathogenic | PVS1, PS4_Very strong, PM2_Supporting |
| NM_000133.4(F9):c.1303T>G (p.Cys435Gly) | CA414447216 | n/a | n/a | Pathogenic | VUS | PS4_Moderate, PP3, PM2_Supporting, PM5_Supporting |
| NM_000133.4(F9):c.720G>A (p.Trp240Ter) | 811503 | Pathogenic | 1 | Pathogenic | Pathogenic | PVS1, PS4_Very strong, PM2_Supporting |
| NM_000133.4(F9):c.224G>A (p.Arg75Gln) | 10573 | Pathogenic/LPath | 2 | Pathogenic | Likely pathogenic | PS4_Very strong, PP3 |
| NM_000133.4(F9):c.572G>A (p.Arg191His) | 10585 | Pathogenic | 2 | Pathogenic | Pathogenic | PS4_Very Strong, PM1_Strong, PP3 |
| NM_000133.4(F9):c.407T>C (p.Ile136Thr) | 627177 | Pathogenic | 1 | Pathogenic | Likely pathogenic | PS4, PM1, PP3, PM2_Supporting |
| NM_000133.4(F9):c.519A>C (p.Ala173=) | 993386 | VUS | 1 | Pathogenic | Likely pathogenic | PS4, PM1, PP3, PM2_Supporting |
| NM_000133.3(F9):c.880C>T (p.Arg294Ter) | 10587 | Pathogenic | 2 | Pathogenic | Pathogenic | PS4_VeryStrong, PVS1_Strong, PM2_Supporting |

The spec describes this file as: "Pilot study results for the F8 and F9 rule specifications. Use the tab at the
bottom of the spreadsheet to toggle between results for hemophilia A and B."

> Note: the pilot results predate v2.1 and were produced under earlier rule versions. Several rows use
> PS3_Supporting, and several rows apply codes at strengths the current text would need re-derivation to
> confirm. They are transcribed as-is.

---

### Appendix E — Source File Inventory

| File | Type | Opened | Transcribed into this document |
|---|---|---|---|
| `ClinGen_ACMG_Specifications_F9_v2.1.pdf` | PDF (main spec) | Yes | Yes — in full (all criteria, point table, header metadata) |
| `PVS1 Decision Tree.pptx` | PowerPoint, 2 slides | Yes | Yes — Appendix A, both slides plus speaker notes |
| `Guidance for Combined De Novo Rule Code (PS2_PM6).docx` | Word + 1 embedded PNG | Yes | Yes — Appendix B, body text and both tables from the embedded image |
| `Rule Guidance for Combining Pathogenic and Benign Codes.docx` | Word + 2 embedded PNGs | Yes | Yes — Rules for Combining Criteria, body text and both Tavtigian tables from the embedded images |
| `F9 Functional Assays.xlsx` | Excel, 3 sheets | Yes | Yes — Appendix C, all populated cells |
| `Pilot Study Results for F8 and F9.xlsx` | Excel, 2 sheets | Yes | F9 sheet fully transcribed (Appendix D) except the free-text Evidence Summary column; F8 sheet intentionally omitted (different gene) |

`GN080_data.json` is download metadata, not source content, and is excluded per the skill workflow.

**Nothing in the distributed package failed to open.** No content is marked as unreadable.

---

### Appendix F — Source Typos, Gaps and Internal Inconsistencies

Transcribed verbatim above; recorded here so downstream users do not mistake them for transcription errors.

**Typos preserved verbatim**

1. PS1_Strong: "When two or more variants **are share** the same predicted splicing effect".
2. PS1_Moderate: "there is **1 likely pathogenic variants**" (singular/plural mismatch).
3. PM6 comment: "Please **combined** assumed de novo cases with confirmed de novo cases".
4. PP1_Strong: "This code is applicable when **there ≥4 meioses**" (missing "are").
5. PP1_Supporting: "when **there 2 meioses** in one family" (missing "are").
6. BP7_Supporting: "Conservation should be **assess** using PhyloP".
7. PVS1 decision tree slide 2: "some evidence of normal **spiced** mRNA".
8. Release note "v2.1.0 corrects the PVS1 Decision Tree file" while every other field in the document,
   including the title, states version "2.1".

**Gaps — where the source is silent (nothing has been filled in)**

9. PM4 "VCEP Specifications" contains only a stray period (`.`). PM4 is applied "with no specification".
10. The Tavtigian Table 2/Table 3 footnote markers (a), (b) appear in the reproduced images but their
    footnote texts are not distributed. Consult Tavtigian et al. 2020 (PMID: 32720330).
11. The PVS1 decision tree carries footnote markers a, b and d on the F9 slide, but the only footnote
    definitions shipped are the F8 ones (a, b, c) in the slide-2 speaker notes; marker "d" is defined nowhere.
    The F9 footnote definitions are absent from the source.
12. Appendix B Table 2 gives strength tiers only at exactly 0.5, 1, 2 and 4 de novo points. Handling of
    intermediate totals (e.g. 3 points) is not specified by this VCEP.
13. PS3 defines only a Supporting level; Moderate/Strong/Very Strong levels for PS3 are not defined.
    PM4 defines only Moderate. PP4 defines only Moderate. PM2 defines only Supporting. PP3 and BP4 define
    only Supporting.

**Internal inconsistencies / apparent VCEP errors**

14. The PDF's own "Point Based Variant Classification Categories" table prints bare values ("Pathogenic 10",
    "Benign -7") where the distributed supplement's Tavtigian Table 3 has open-ended operators (≥10, ≤ −7).
    Read literally, the PDF table leaves 10+ and −8 and below unclassified. The supplement's form is correct.
15. The PVS1 decision tree never yields PVS1_Moderate, yet the spec defines a PVS1 Moderate strength with a
    default point value of 2. Nothing in the package explains when Moderate would be reached.
16. The PM5_Supporting text defines a "'highly suspicious' VUS" but that term is used nowhere else in the
    specification, so the definition is orphaned.
17. BS2_Strong's threshold is written "at least >40% IU", combining an inclusive phrase with a strict operator.
    The Release Notes claim "BS2- fixed typo" for v2.1; a phrasing ambiguity nonetheless remains.
18. PVS1 cites "Walker et al. (PMID: 36865205)" for RNA recommendations while PS1 cites "Walker, et al 2023
    (PMID: 37352859)". Two different PMIDs are attributed to Walker et al. within the same document; both are
    transcribed as printed.
19. The "F9 Functional Assays" workbook's `Example` sheet contains dummy data (PMID 1234567, "Jones", 1985)
    marked "Approved assay: y" and "Proposed strength: PS3_Supporting; BS3 not applied". This is a template
    row shipped in the released file, not a real F9 assay, and must not be treated as an approved assay.
20. PS3 was downgraded to Supporting only (max +1) in v2.1, while BS3 remains Strong (−4). The asymmetry is
    deliberate on its face but is not explained in the package.
21. The PVS1 decision tree's slide-2 speaker notes describe F8 (c.6852, exons 8 and 14, in-frame start codon
    at 32), i.e. content from the sibling F8 specification left in the F9 file. The v2.1 Release Notes state
    "v2.1.0 corrects the PVS1 Decision Tree file" — this residue apparently survived that correction.
22. The Gao 2020 ELISA assay record lists "Technical replicates: not met", "Basic negative control: not met",
    "Validation controls B/LB: (blank)" and "Statistical analysis: none", yet is marked approved. Consistent
    with the v2.1 downgrade of all assays to Supporting weight.

---

## Version History

**v2.1 — Released 4/16/2026** (DOI 10.5281/zenodo.21433987). Release Notes, verbatim from the specification:

> "v2.1.0 corrects the PVS1 Decision Tree file.
>
> Edits post SVI review
>
> PVS1 - Updated to include RNA recommendations based on Walker, et al paper.
>
> PP3/BP4/BP7 - Updated SpliceAI cut off based on Walker, et al paper.
>
> PS4 - changed requirement that only 3 hemizygotes could be present in gnomAD in order to apply code. This was
> changed as a result of the increased number of individuals in gnomAD v4.1. Now using a ratio to avoid needing
> to update regularly in the future.
>
> BS2- fixed typo
>
> PS1 - added splicing option from Walker, et al.
>
> PS3 - downgraded all assays to supporting weight"

Earlier version history is not included in the distributed v2.1 package.

---

*This document was compiled from the ClinGen VCEP specification (GN080, F9 v2.1) and the five supplementary
files distributed with it. For the most current version, please refer to the ClinGen website.*
