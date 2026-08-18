# ClinGen Severe Combined Immunodeficiency Disease VCEP Variant Interpretation Guidelines for RMRP

**Version:** 1.3
**Released:** 5/1/2026
**Affiliation:** Severe Combined Immunodeficiency Disease VCEP
**Source basis:** Richards et.al., 2015 - Combining rules
**DOI:** 10.5281/zenodo.21434137
**ClinGen VCEP ID:** GN088

**Release Notes (verbatim from source):**
> Edited Rules for Combining Criteria to reflect standard combinations plus (A) 1 very strong + 1 supporting = Likely Pathogenic and (B) 1 Strong Benign = Likely Benign.

**Keywords (verbatim):** human biology genomics variant variant classification clingen disease standards RMRP NR_003051.3 Autosomal recessive inheritance cartilage-hair hypoplasia

**Source basis for this document:** the ClinGen specification PDF `ClinGen_ACMG_Specifications_RMRP_v1.3.pdf` plus the five files distributed with it (`PS2_PM6.pdf`, `PM3.pdf`, `PP1.pdf`, `PS3_BS3.xlsx`, `VCEP Comments.docx`). All five were opened and transcribed. Nothing in this document is supplied from generic ACMG/AMP or SVI content that is not present in that package.

---

## Important Note on Gene Biology

**RMRP encodes a non-coding RNA** (RNA component of mitochondrial RNA processing endoribonuclease; transcript NR_003051.3). There is no protein product. The VCEP has consequently marked several protein-centric ACMG/AMP criteria **Not Applicable** (PVS1, PM5, PP2, BP1, BP3, BP7 among them) and has **redefined** others in nucleotide/RNA terms rather than amino-acid terms:

- **PS1** is redefined at the *nucleotide* level (a different nucleotide change at the same nucleotide position), despite the criterion's original amino-acid wording.
- **PM1** is redefined as a promoter-region rule (TATA box to transcription start site).
- **PM4**, whose original wording concerns protein length, is redefined as insertions/duplications that increase the *distance between the TATA box and the transcription start site*.
- **PP3** is redefined around RNA secondary-structure prediction (RNAsnp), not protein missense predictors.

Coordinates throughout are given in `n.` (non-coding transcript) numbering.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | RMRP (HGNC:10031) |
| **HGNC Name** | RNA component of mitochondrial RNA processing endoribonuclease |
| **Transcript** | NR_003051.3 |
| **Disease** | cartilage-hair hypoplasia (MONDO:0009595) |
| **Inheritance** | Autosomal recessive inheritance |

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
2. [Benign Criteria](#benign-criteria)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)
5. [Source Issues and Flags](#source-issues-and-flags)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specification:** **Not Applicable.** Comments: "Does not apply."

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specification — Downgraded to PS1_Supporting.**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Downgraded to PS1_Supporting. Applicable if a different nucleotide change at the same nucleotide position has been previously classified as pathogenic or likely pathogenic. Cannot be applied if a different nucleotide change at the same position has been previously classified as benign or likely benign. Previously established variants must be classified by SCID VCEP specifications for RMRP. |
| **Strong** | Not specified by VCEP (PS1 is downgraded to Supporting). |
| **Moderate** | Not specified by VCEP. |

**Modification Type:** Gene-specific, Strength

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications (verbatim):**

> The following guidelines should be used when determining the phenotypic consistency of each proband:
>
> - "Phenotype highly specific for gene" proband must meet PP4_Moderate criteria;
> - "Phenotype consistent with gene but not highly specific" proband must meet PP4 criteria;
> - "Phenotype consistent with gene but not highly specific and high genetic heterogeneity": proband has been asserted to have a Cartilage-hair hypoplasia (CHH) phenotype but does not meet PP4 criteria;
> - Reduce points per proband by half if the phase is unconfirmed.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Very Strong** | Use ClinGen SVI recommendations for de novo criteria (see [Appendix A](#appendix-a--svi-recommendation-for-de-novo-criteria-ps2--pm6-version-11)). | Disease-specific, Strength |
| **Strong** | Use ClinGen SVI recommendations for de novo criteria (see Appendix A). | Disease-specific, Strength |
| **Moderate** | Use ClinGen SVI recommendations for de novo criteria (see Appendix A). | Disease-specific, Strength |
| **Supporting** | Use ClinGen SVI recommendations for de novo criteria (see Appendix A). | Disease-specific, Strength |

The point system referenced here is **distributed with this specification** as `PS2_PM6.pdf` and is transcribed in full in [Appendix A](#appendix-a--svi-recommendation-for-de-novo-criteria-ps2--pm6-version-11).

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications (verbatim):** "PS3 may be applied when RT/PCR or RNA evidence indicates variant results in absent expression."

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | PS3 may potentially be applied at the default strength level of strong for evidence from an animal model expressing the variant of interest and recapitulating the Cartilage-hair hypoplasia (CHH) phenotype. Animal models will be reviewed on a case-by-case basis by the VCEP to determine the appropriate strength level. | Gene-specific |
| **Moderate** | Not specified by VCEP. | — |
| **Supporting** | PS3_Supporting can be applied based on an abnormal result in at least one approved in vitro assay. | Disease-specific, Strength |

#### Approved Assay Instances (verbatim from specification PDF)

- **Endonucleolytic cleavage activity assay** (mRNA cleavage activity **smaller than 0.9** — strict `<`)
  - Thiel et al., 2005 (PMID: 16252239)
  - Thiel et al., 2007 (PMID: 17701897)) **OR**
- **Luciferase reporter assay**
  - Hermanns et al., 2005 (PMID: 16254002)) (luciferase activity **higher than 7** — strict `>`)

*(The doubled closing parentheses above are present in the source and are preserved verbatim.)*

Full assay-instance detail from the distributed `PS3_BS3.xlsx` is transcribed in [Appendix D](#appendix-d--ps3bs3-functional-evidence-ps3_bs3xlsx).

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specification:** **Not Applicable.** Comments: "Does not apply."

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specification — applied at Strong (PM1_Strong):**

> Defined to include insertions/duplications between the TATA box (spanning n.-32 to n.-24) and the transcription start site (n.4). Caveat: All variants should be sufficiently rare - variant does not have to meet PM2 specification criteria but variant should not meet BS1/BA1 criteria (unless a suspected founder variant). The applicability of PM1 to suspected founder variants exceeding the BS1/BA1 threshold will be evaluated on a case-by-case basis by the VCEP.

**Modification Type:** Gene-specific

The distributed `VCEP Comments.docx` ("Updates to PM1 10/23/25") documents the origin of this caveat wording; it is transcribed in [Appendix E](#appendix-e--vcep-comments-updates-to-pm1-102325).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification — Downgraded to PM2_Supporting:**

| Strength | Criteria |
|----------|----------|
| **Supporting** | Absent in population databases (or at extremely low frequency if recessive). Downgraded to PM2_Supporting. **gnomAD popmax filtering allele frequency <0.0000447** |

**Comparator:** strict less-than (`<`). The threshold value **0.0000447** is not met by a variant whose popmax FAF equals exactly 0.0000447.

Additional text: "The applicability of PM2 to suspected founder variants with allele frequencies exceeding the PM2 threshold will be evaluated on a case-by-case basis by the VCEP."

**Modification Type:** Disease-specific, Strength

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications (verbatim):**

> Caveat: All variants should be sufficiently rare - variant does not have to meet PM2 specification criteria but variant should not meet BS1/BA1 criteria (unless a suspected founder variant). The applicability of PM3 to suspected founder variants exceeding the BS1/BA1 threshold will be evaluated on a case-by-case basis by the VCEP.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Very Strong** | Use ClinGen SVI recommendations for in trans criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for RMRP. | General recommendation, Strength |
| **Strong** | Use ClinGen SVI recommendations for in trans criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for RMRP. | General recommendation, Strength |
| **Moderate** | Use ClinGen SVI recommendations for in trans criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for RMRP. | General recommendation |
| **Supporting** | Use ClinGen SVI recommendations for in trans criterion with the additional requirement that the co-occurring variant must be classified using the SCID VCEP specifications for RMRP. | General recommendation, Strength |

The referenced SVI point system is **distributed with this specification** as `PM3.pdf` and is transcribed in full in [Appendix B](#appendix-b--svi-recommendation-for-in-trans-criterion-pm3-version-10).

**Note on an internal tension:** the SVI PM3 document states that all variants should be sufficiently rare and specifically "meet PM2 specification"; the RMRP VCEP overrides this with its own caveat above ("does not have to meet PM2 specification criteria but variant should not meet BS1/BA1 criteria"). The VCEP caveat is the operative rule for RMRP.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Defined to include insertions/duplications of 6 or more nucleotides increasing the distance between the TATA box (spanning n.-32 to n.-24) and the transcription start site (n.4). | Gene-specific |
| **Supporting** | Not specified by VCEP. | — |

**Comparator:** "6 or more nucleotides" — inclusive (`>=6`).

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**VCEP Specification:** **Not Applicable.** Comments: "Does not apply."

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications (verbatim — identical wording to PS2):**

> The following guidelines should be used when determining the phenotypic consistency of each proband:
>
> - "Phenotype highly specific for gene" proband must meet PP4_Moderate criteria;
> - "Phenotype consistent with gene but not highly specific" proband must meet PP4 criteria;
> - "Phenotype consistent with gene but not highly specific and high genetic heterogeneity": proband has been asserted to have a Cartilage-hair hypoplasia (CHH) phenotype but does not meet PP4 criteria;
> - Reduce points per proband by half if the phase is unconfirmed.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Very Strong** | Not listed by the VCEP for PM6 (only Strong, Moderate, Supporting are enumerated). |  — |
| **Strong** | Use ClinGen SVI recommendations for de novo criteria (see Appendix A). | Disease-specific, Strength |
| **Moderate** | Use ClinGen SVI recommendations for de novo criteria (see Appendix A). | Disease-specific, Strength |
| **Supporting** | Use ClinGen SVI recommendations for de novo criteria (see Appendix A). | Disease-specific, Strength |

See [Appendix A](#appendix-a--svi-recommendation-for-de-novo-criteria-ps2--pm6-version-11) for the distributed point system.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications (verbatim):**

> Use ClinGen SVI recommendations for co-segregation criterion (PMID: 30311386) with the additional specification that unaffected individuals contributing to the calculated LOD score (Attached document: PP1 specifications) must be heterozygous carriers of one of the variants observed in the affected individuals (i.e. do not count wild-type/wild-type, individuals).

*(The stray comma in "wild-type/wild-type, individuals" is present in the source.)*

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations. | General recommendation, Strength |
| **Moderate** | Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations. | General recommendation, Strength |
| **Supporting** | Use recommendations for co-segregation criterion from PMID: 30311386, with strength dependent on number of affected segregations. | General recommendation, Strength |

The LOD-score tables (Oza et al. Tables 4a and 4b) are **distributed with this specification** as `PP1.pdf` and are transcribed in full in [Appendix C](#appendix-c--pp1-segregation-lod-score-tables-oza-et-al-pmid-30311386).

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specification:** **Not Applicable.** Comments: "Does not apply."

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**VCEP Specification — Supporting only:**

> Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc).
>
> - Use RNAsnp to access SNP effects on local RNA secondary structure (https://rth.dk/resources/rnasnp/)
> - Use only for Single Nucleotide Polymorphism inside the gene (do not use for promoter sequence)
>   - Parameters utilized:
>     - Input sequence: FASTA (Ensembl NR__003051.3)
>     - Insert SNP details
>     - Mode: 1
>     - Folding window: 100 nt
>     - Measure: "Distance" option
>     - Minimum length of the sequence interval: 50
>     - Cut-off the base pair probabilities: 0.01
>
> The p-value threshold significance should be considered 0.1 according to Sabarinathan et al., 2013. PMID: 23315997. If the value is less than 0.1, apply PP3 as a supporting level of evidence.

**Comparator:** "If the value is **less than** 0.1" — strict (`<`).

**Source typos preserved:** "Ensembl NR__003051.3" (double underscore; the transcript elsewhere is NR_003051.3), and "access" where "assess" appears to be intended.

**Modification Type:** Gene-specific, Strength

BP4 (the benign counterpart) is Not Applicable for this gene — see Benign Criteria.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** PP4 applicability and strength is determined by the **total points accumulated by a single affected individual** according to the list below and the following total point ranges:

| Total points | Outcome |
|---|---|
| **<1 point** (strict) | PP4 not met |
| **1-<2 points** (lower bound inclusive, upper bound strict) | PP4 (Supporting) |
| **≥2 points** (inclusive) | PP4_Moderate |

#### PP4 Point Assignment (verbatim item list and values)

| Feature | Points |
|---|---|
| Diagnostic criteria for SCID/Leaky SCID/Omenn syndrome met¹ | 1 pt |
| SCID gene panel or exome/genome sequencing conducted (only applicable if genetic testing did not provide an alternative genetic explanation for SCID/Leaky SCID/Omenn syndrome phenotype) | 0.5 pt |
| Family history of SCID | 0.5 pt |
| Family history of CHH | 1 pt |
| Metaphyseal dysplasia (disproportionate short stature + radiographic evidence) | 1 pt |
| Skeletal dysplasia gene panel or WES/WGS conducted with no alternative genetic diagnosis | 1 pt |
| Hypotrichosis | 0.5 pt |
| Macrocytic, hypoplastic anemia | 0.25 pt |
| Hirschsprung disease or congenital megacolon | 0.25 pt |
| T-cell lymphopenia* (see notes) | 0.5 pt |
| 3-fold or more reduction of mutant RMRP RNA (or cDNA) expression in peripheral blood mononuclear cells | 2 pts |

¹ "The diagnostic criteria should follow the PIDTC 2022 specification, summarized here." — the word "here" is a hyperlink in the source PDF to an external Google Doc (`https://docs.google.com/document/d/1Ag2g8DhdxkFyX62Tw-4-kUBcULZvDQtXC0j3ol9kxiM/edit`). **That document is not distributed with the specification package and was not retrieved; its contents are therefore not reproduced here.**

**\*Notes (verbatim):**
1. If maternal T cells are present, the T lymphocyte profile is still considered to be T- (autologous T cells are absent).
2. Allocate 0.25 points for T-cell lymphopenia only in cases where the SCID diagnostic criteria are not applied. It is important to note that if the SCID diagnostic criteria were applied, the points for the T-B+NK+ lymphocyte subset profile cannot be considered.

> **Flagged internal inconsistency:** the point list assigns T-cell lymphopenia **0.5 pt**, while Note 2 instructs allocating **0.25 points** for T-cell lymphopenia. The source is not reconciled; both values are transcribed as written.

**"3-fold or more"** is inclusive (`>=3-fold`).

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | A patient score of ≥2 points. | Disease-specific, Gene-specific, Strength |
| **Supporting** | A patient score of 1-<2 points. | Disease-specific, Gene-specific |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specification:** **Not Applicable.** "This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee." (PubMed: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification — Stand Alone:**

> Common in population databases.
> **gnomAD popmax filtering allele frequency >0.00400**
> Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:
> - Prevalence: 1:5,000
> - Allelic heterogeneity: 1
> - Genetic heterogeneity: 0.04 (based on the contribution of RMRP variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 3.6%, rounded to 4%)
> - Penetrance: 50%
>
> Use caution when applying BA1 based on allele frequencies derived from gnomAD exome sequencing given the reduced coverage of certain regions of RMRP. Ensure at least 20X read depth for allele frequencies derived from exome sequencing.

**Comparator:** strict greater-than (`>`) 0.00400. Note that this is well below the ACMG default 5%.
**Read depth:** "at least 20X" — inclusive (`>=20X`).

**Modification Type:** Disease-specific

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification — Strong:**

> Allele frequency is greater than expected for disorder.
> **gnomAD popmax filtering allele frequency >0.00089**
> Maximum credible population allele frequency threshold determined using Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/) and the following parameters:
> - Prevalence: 1:50,000
> - Allelic heterogeneity: 1
> - Genetic heterogeneity: 0.04 (based on the contribution of RMRP variants to total SCID in the PIDTC 6901 cohort reported in Dvorak et al., 2019 (PMID: 30193840, Table 1): 3.6%, rounded to 4%)
> - Penetrance: 100%
>
> Use caution when applying BS1 based on allele frequencies derived from gnomAD exome sequencing given the reduced coverage of certain regions of RMRP. Ensure at least 20X read depth for allele frequencies derived from exome sequencing.

**Comparator:** strict greater-than (`>`) 0.00089.

**Modification Type:** Disease-specific

#### Frequency threshold summary

| Criterion | Threshold (gnomAD popmax filtering AF) | Comparator |
|---|---|---|
| **BA1** (Stand Alone) | 0.00400 | strict `>` |
| **BS1** (Strong) | 0.00089 | strict `>` |
| **PM2_Supporting** | 0.0000447 | strict `<` |

*Values between 0.0000447 and 0.00089 inclusive of the endpoints satisfy neither PM2_Supporting nor BS1; the source leaves this intermediate band with no frequency code, which is the expected behaviour of a strict-comparator design.*

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

| Strength | Criteria | Comparator | Modification Type |
|----------|----------|-----------|-------------------|
| **Strong** | BS2_Strong: Observed in >=3 (3 or more) homozygotes in gnomAD. | inclusive (`>=3`) | Gene-specific, Strength |
| **Supporting** | BS2_Supporting: Can be applied at Supporting level of evidence if observed at least 2 homozygotes in gnomAD. | inclusive (`>=2`) | Gene-specific, Strength |

> **Flagged:** as literally written the two tiers overlap — "at least 2 homozygotes" is also satisfied at 3 or more. The source does not state an upper bound for the Supporting tier. Transcribed as written; the evident intent is 2 homozygotes = Supporting, ≥3 = Strong, but the specification does not say so.

*Source grammar preserved: "if observed at least 2 homozygotes" (missing "in").*

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specification:** **Not Applicable.** Comments: "Does not apply."

> Note: the distributed functional-evidence file is named `PS3_BS3.xlsx` and titled "RMRP Functional Evidence", but BS3 is Not Applicable in this specification. The file contains only PS3-directed content ("Proposed strength: PS3_Supporting" for all three assay instances); no BS3 thresholds appear in it.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specification — Strong:**

> Can be applied without additional specifications. To apply the BS4 criteria, it is sufficient to have one affected family member without the segregation of the variant.

**Modification Type:** None

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | "Does not apply." |
| **BP2** | Not Applicable | "Does not apply." |
| **BP3** | Not Applicable | "Does not apply." |
| **BP4** | Not Applicable | "Does not apply." |
| **BP5** | Not Applicable | "Does not apply." |
| **BP6** | Not Applicable | "This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee." (PubMed: 29543229) |
| **BP7** | Not Applicable | "Does not apply." |

---

## Rules for Combining Criteria

Transcribed verbatim from the specification PDF. Type: **Richards et.al., 2015 - Combining rules**. (These were the section revised in v1.3 per the release notes.)

### Pathogenic

1. 1 Very Strong (PS2_Very Strong, PM3_Very Strong) AND ≥ 1 Strong (PS2, PS3, PM1_Strong, PM3_Strong, PM6_Strong, PP1_Strong)
2. 1 Very Strong (PS2_Very Strong, PM3_Very Strong) AND ≥ 2 Moderate (PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate)
3. 1 Very Strong (PS2_Very Strong, PM3_Very Strong) AND 1 Moderate (PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate) AND 1 Supporting (PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3, PP4)
4. 1 Very Strong (PS2_Very Strong, PM3_Very Strong) AND ≥ 2 Supporting (PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3, PP4)
5. ≥ 2 Strong (PS2, PS3, PM1_Strong, PM3_Strong, PM6_Strong, PP1_Strong)
6. 1 Strong (PS2, PS3, PM1_Strong, PM3_Strong, PM6_Strong, PP1_Strong) AND ≥ 3 Moderate (PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate)
7. 1 Strong (PS2, PS3, PM1_Strong, PM3_Strong, PM6_Strong, PP1_Strong) AND 2 Moderate (PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate) AND ≥ 2 Supporting (PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3, PP4)
8. 1 Strong (PS2, PS3, PM1_Strong, PM3_Strong, PM6_Strong, PP1_Strong) AND 1 Moderate (PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate) AND ≥ 4 Supporting (PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3, PP4)

### Likely Pathogenic

1. 1 Very Strong (PS2_Very Strong, PM3_Very Strong) AND 1 Moderate (PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate)
2. 1 Strong (PS2, PS3, PM1_Strong, PM3_Strong, PM6_Strong, PP1_Strong) AND 1 Moderate (PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate)
3. 1 Strong (PS2, PS3, PM1_Strong, PM3_Strong, PM6_Strong, PP1_Strong) AND ≥ 2 Supporting (PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3, PP4)
4. ≥ 3 Moderate (PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate)
5. 2 Moderate (PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate) AND ≥ 2 Supporting (PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3, PP4)
6. 1 Moderate (PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate) AND ≥ 4 Supporting (PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3, PP4)
7. **1 Very Strong (PS2_Very Strong, PM3_Very Strong) AND 1 Supporting** (PS1_Supporting, PS2_Supporting, PS3_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3, PP4)  — *addition (A) in v1.3*
8. 1 Strong (PS2, PS3, PM1_Strong, PM3_Strong, PM6_Strong, PP1_Strong) AND 2 Moderate (PS2_Moderate, PM3, PM4, PM6, PP1_Moderate, PP4_Moderate)

### Benign

1. ≥ 2 Strong (BS1, BS2, BS4)
2. 1 Stand Alone (BA1)

### Likely Benign

1. ≥ 2 Supporting (BS2_Supporting)
2. **1 Strong (BS1, BS2, BS4)** — *addition (B) in v1.3*

### Notes on the combining rules as written

- The evidence-code rosters above are exactly as printed. Note that **PM1_Strong** appears in the "Strong" roster but PM1 has no Moderate tier in this specification; **PM3** (unqualified) appears in the Moderate roster and **PM3_Supporting/PM3_Strong/PM3_Very Strong** in their respective rosters; **PM6** (unqualified) is listed as Moderate.
- **PM6_Very Strong is not listed anywhere** in the combining rules, consistent with the PM6 criterion section, which enumerates only Strong/Moderate/Supporting.
- **PS4, PVS1, PM5, PP2, PP5, BS3, BP1-BP7** do not appear in any roster, consistent with their Not Applicable status.
- **BP-level benign supporting codes are absent entirely**; the only Supporting-level benign code in use is BS2_Supporting.
- The specification does **not** provide a Tavtigian-style points-based classification scheme; it uses the Richards et al. 2015 combining-rule framework only.

---

## Appendices

All appendices below are transcribed from files distributed with this specification. Nothing here is supplied from outside the download package.

### Appendix A — SVI Recommendation for de novo Criteria (PS2 & PM6), Version 1.1

*Source: `PS2_PM6.pdf`, listed in the specification as "PS2_PM6: SVI recommendations for de novo criteria". Working Group page: https://clinicalgenome.org/working-groups/sequence-variant-interpretation/ · Date Approved: March 18, 2018, updated May 5, 2021 · Changes from v1: Clarified that confirmed/assumed is with regards to parental relationships and not de novo status.*

The SVI Working Group proposes a point-based system to determine the strength of de novo evidence (PS2 and PM6) based upon three parameters:
- confirmed parental relationships versus assumed parental relationships status
- phenotypic consistency
- number of de novo observations

Each proband with a de novo variant is awarded a point value based upon phenotypic consistency and confirmed or assumed parental relationships (Table 1). The combined point value of all de novo occurrences is then compared to Table 2 to determine the applicable evidence strength level. **If the parents have not been tested for parentage or for the variant, no points should be awarded.**

#### Table 1. Points* awarded per de novo occurrence

| Phenotypic consistency | de novo with confirmed parental relationships | de novo with unconfirmed parental relationships |
|---|---|---|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity** | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

\* Note that these points are not equivalent to the points used to classify a variant per the Tavtigian et al 2020 "Fitting a naturally scaled point system to the ACMG/AMP variant classification guidelines"
\*\* Maximum allowable value of 1 may contribute to overall score

#### Table 2. Appropriate ACMG/AMP evidence strength level for de novo occurrence(s)

| Supporting (PS2_Supporting or PM6_Supporting) | Moderate (PS2_Moderate or PM6) | Strong (PS2 or PM6_Strong) | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |
|---|---|---|---|
| 0.5 | 1 | 2 | 4 |

*(Comparators are not stated explicitly in the source; the worked examples treat the tabulated values as thresholds reached — e.g. "the points reach the Strong threshold (2 points) but not the VeryStrong threshold (4 points)", implying inclusive `>=` at each tier.)*

#### Additional considerations for applying de novo criteria based on inheritance (verbatim)

- **Conditions with X-linked inheritance:** if the variant occurs de novo in an unaffected carrier mother, and family history is consistent - i.e., she has no affected brothers/other male relatives apart from her affected son(s) – de novo criteria may be applied despite the fact that she is unaffected.
- **Autosomal recessive conditions:** for a de novo occurrence in a gene associated with a condition inherited in an autosomal recessive pattern without an additional pathogenic/likely pathogenic variant identified, **the strength of evidence should be decreased by one level.** *(RMRP-relevant: cartilage-hair hypoplasia is autosomal recessive.)*
- **Mosaicism:** for cases with apparent germline mosaicism (multiple affected siblings with both parents negative for the variant), parental relationships must be confirmed in order for de novo criteria to apply.

*The document also gives worked examples (NIPBL/Cornelia de Lange, SIK1/early infantile epileptic encephalopathy, ASH1L/nonsyndromic intellectual disability, PAH). These are illustrative only and are not RMRP-specific.*

> **Note on Table 2 vs. Table 1 in the RMRP context:** the RMRP VCEP additionally instructs "Reduce points per proband by half if the phase is unconfirmed" (PS2/PM6 sections). This RMRP-specific instruction refers to *phase*, whereas SVI Table 1 columns refer to *parental relationships*; the specification does not reconcile the two. Both are transcribed as written.

---

### Appendix B — SVI Recommendation for in trans Criterion (PM3), Version 1.0

*Source: `PM3.pdf`, listed in the specification as "PM3: SVI recommendations for pm3 criterion". Working Group page: https://clinicalgenome.org/working-groups/sequence-variant-interpretation/ · Date Approved: May 2, 2019.*

**SVI revision to the criterion definition:** "For recessive disorders, detected in *trans* with a pathogenic **or likely pathogenic** variant **in an affected patient**."

Each proband is awarded a point value based upon phasing of the two variants (confirmed in trans versus unknown) and classification of the variant on the other allele (Table 1). The combined point value of all proband occurrences is summed and compared to Table 2.

#### Table 1. Points awarded per in trans proband

| Classification/Zygosity of other variant¹ | Confirmed in trans | Phase unknown |
|---|---|---|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (max point 1.0) | 0.5 | N/A |
| Uncertain significance variant (max point 0.5) | 0.25 | 0.0 |

¹ All variants should be sufficiently rare (meet PM2 specification); P - Pathogenic; LP - Likely pathogenic
*(For RMRP the VCEP replaces this PM2 rarity requirement with its own BS1/BA1-based caveat — see the PM3 section above.)*

#### Table 2. Appropriate evidence strength level for PM3

| PM3_Supporting | PM3 | PM3_Strong | PM3_VeryStrong |
|---|---|---|---|
| 0.5 | 1.0 | 2.0 | 4.0 |

#### Considerations (verbatim, condensed to the operative statements)

- **Allele Frequency** — Application of PM3 is contingent on the allele frequency of the variant being assessed and the variant presumably on the other allele both being sufficiently rare (meets PM2 threshold). This contingency is to avoid incorrect application of PM3 to high frequency variants that are likely to occur in trans with P/LP variants based on frequency.
- **Phasing** — If the phase cannot be determined, it is recommended that at least two different LP/P variants (depending on classifications) are needed to equal the weight of one LP/P co-occurrence confirmed in trans. In confirmation of phasing, if only one parent is tested and found to carry one allele, variants can be counted as in trans.
- **Classification** — Probands should be weighted less when the variant on the other allele is of uncertain significance and rare (meets PM2); however, weight may vary by gene size as larger genes are more likely to have a second variant by chance (default 0.25 points). To avoid circularity, in all instances (phasing confirmed or unknown), the classification of the variant on the other allele should not use evidence from the variant being interrogated.
- **Homozygous occurrences** — For homozygous occurrences, the default weight is dropped to 0.5 points, as a rare homozygous occurrence may be due to consanguinity. A recommended max of 1.0 points of all homozygous cases is suggested to prevent overclassification of homozygous occurrences in the absence of additional data.

*The RMRP VCEP adds: the co-occurring variant must be classified using the SCID VCEP specifications for RMRP.*

---

### Appendix C — PP1 Segregation LOD Score Tables (Oza et al., PMID: 30311386)

*Source: `PP1.pdf`, listed in the specification as "PP1: Specifications". The PDF is an excerpt of Oza et al., Hum Mutat (author manuscript), pages 35-36, Tables 4a and 4b.*

#### Table 4a. Recommendations for PP1 (segregation evidence) — General Recommendations

| | Supporting | Moderate | Strong |
|---|---|---|---|
| **Likelihood** | 4:1 | 16:1 | 32:1 |
| **LOD Score** | 0.6 | 1.2 | 1.5 |
| **Autosomal dominant threshold** | 2 affected segregations | 4 affected segregations | 5 affected segregations |
| **Autosomal recessive threshold** | See Table 4b | See Table 4b | See Table4b |

*(Source typo preserved: "See Table4b" in the Strong column.)*
**RMRP is autosomal recessive, so Table 4b governs; the autosomal dominant row does not apply.**

#### Table 4b. Recommendations for autosomal recessive segregation evidence (PP1)

General Recommendations (Phenocopy not an issue). **This is a lookup table:** rows = number of affected segregations (0-10), columns = number of unaffected recessive segregations (0-10); each cell is the LOD score for that combination. Compare the looked-up LOD score against the LOD thresholds in Table 4a (0.6 Supporting / 1.2 Moderate / 1.5 Strong).

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

**Table legend (verbatim):** Affected segregations are counted in rows and unaffected segregations in columns. Affected segregations are affected family members in whom biallelic compound heterozygous or homozygous variants segregates. Unaffected segregations are defined as unaffected family members, typically siblings, who are at risk to inherit the two variants identified in the proband. These individuals should be either wild-type for both variants identified in the proband, or a heterozygous carrier for a single variant. Unaffected, carrier parents DO NOT count as unaffected segregations. There may be scenarios where individuals other than siblings could be counted as segregations, such as in families where one parent is affected with the autosomal recessive disorder, in large families with multiple branches, or in consanguineous families. Each cell shows the LOD score of each combination of affected and unaffected segregations. LOD scores were calculated using a simplified LOD score formula, as described in Strande et al., 2017.

**RMRP VCEP overlay:** unaffected individuals contributing to the calculated LOD score "must be heterozygous carriers of one of the variants observed in the affected individuals (i.e. do not count wild-type/wild-type, individuals)." **This narrows the Oza legend**, which permits counting unaffected individuals who are wild-type for both variants. Where the two conflict, the VCEP specification governs for RMRP.

---

### Appendix D — PS3/BS3 Functional Evidence (`PS3_BS3.xlsx`)

*Source: `PS3_BS3.xlsx`, listed in the specification as "PS3_BS3: RMRP Functional Evidence". Two worksheets, both transcribed in full below. No embedded images. Despite the filename, no BS3 content is present.*

#### Sheet 1 — "General Class of Assay Summary"

| Gene | General Class of Assay | PMIDs |
|---|---|---|
| RMRP | Endonucleolytic cleavage activity assay | PMID: 16252239, PMID: 17701897 |
| | Luciferase reporter assay | PMID: 16254002 |

#### Sheet 2 — "RMRP Assay Instance Details"

| Field | Instance 1 | Instance 2 | Instance 3 |
|---|---|---|---|
| **PMID** | 16252239 | 17701897 | 16254002 |
| **Gene** | RMRP | RMRP | RMRP |
| **DOI / link** | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1271388/ | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1950841/ | https://academic.oup.com/hmg/article/14/23/3723/559481?login=false |
| **Author** | Thiel...Rauch | Thiel...Rauch | Hermanns...Lee |
| **Year** | 2005 | 2007 | 2005 |
| **General Class of Assay** | Endonucleolytic cleavage activity | Endonucleolytic cleavage activity | Luciferase reporter assay |
| **Assay (General Description)** | RNA and DNA extracted from normal human fibroblasts 12 h, 36 h, 48 h, and 60 h post-transient transfection with wild type or variant RMRP expression constructs were used as template for quantitative real-time PCR evaluation of RMRP, CCNA2, CCNB2, 5.8S rRNA, and ITS-1-bound 5.8S rRNA expression levels | RNA and DNA extracted from normal human fibroblasts transiently transfected with wild type or variant RMRP expression constructs were used as template for quantitative real-time PCR evaluation of RMRP, CCNB2, 5.8S rRNA, and ITS-1-bound 5.8S rRNA expression levels | Expression plasmids containing wild type and variant RMRP promoter sequences upstream of an shRNA against luciferase were transfected in cos7 cells in combination with a luciferase expression plasmid. |
| **Material used** | Normal human fibroblasts transiently transfected with wild type or variant RMRP expression constructs | Normal human fibroblasts transiently transfected with wild type or variant RMRP expression constructs | cos7 cells transfected with a luciferase-targeted shRNA under the control of wild type or variant RMRP promoters |
| **Readout type** | Quantitative | Quantitative | Quantitative |
| **Readout description** | Cyclin levels (based on CCNA2 and CCNB2 mRNA levels); rRNA cleavage activity normalized to wild type (ratio of levels of cleaved to uncleaved 5.8S rRNA) | mRNA cleavage activity normalized to wild type (inverse relative increase of CCNB2 mRNA level); rRNA cleavage activity normalized to wild type (ratio of levels of cleaved to uncleaved 5.8S rRNA) | Relative luciferase activity (promoter strength correlates with the degree of shRNA-mediated downregulation of luciferase expression) |
| **Biological replicates** | 3 | Not reported | Not reported |
| **Technical replicates** | 4 | Not reported | 2 |
| **Basic positive control** | Cells transfected with wild type RMRP | Cells transfected with wild type RMRP | Cells transfected with luciferase shRNA under the control of the wild type RMRP promoter (two versions of the promoter sequence tested: -352 bp upstream of the transcription start site and -841 bp upstream of the transcription start site) or under the control of the U6 promoter |
| **Basic negative control** | Cells transfected with empty vector | Not reported | Cells transfected with a U6 promoter without a luciferase shRNA and with the luciferase shRNA without a promoter sequence |
| **Validation controls P/LP (#)** | 0 | 0 | 0 |
| **Validation controls B/LB (#)** | 0 | 0 | 0 |
| **Statistical analysis** | Not reported | Not reported | P values reported, but details of statistical analyses not included |
| **Threshold for normal readout** | Wild type-like level of cyclins and rRNA cleavage activity | Wild type-like level of mRNA and rRNA cleavage activity | Wild type-like level of luciferase activity |
| **Threshold for abnormal readout** | Reduced level of cyclins and/or rRNA cleavage activity (mRNA cleavage activity smaller than 0.9) | Reduced level of mRNA and/or rRNA cleavage activity (mRNA cleavage activity smaller than 0.9) | Increased level of luciferase activity (Luciferase activity higher than 7) |
| **Approved assay (y/n)** | y | y | y |
| **Proposed strength** | PS3_Supporting | PS3_Supporting | PS3_Supporting |
| **Proposed strength (modified)** | NA | NA | NA |
| **Variant(s) Tested** | +14G→A, +90_91AG→GC, ins111_112ACGTAGACATTCCT, +254C→G, and +70A→G | g.111_112insACTGTAGACATTCCT, g.90_91AG→GC e g.254C→G, g.63C→T, g.70A→G, g.96_97dupTG, g.126C→T, g.146G→A, g.4C→T, g.220T→C, g.248C→T e g.261C→T) and g.195C→T, | 89C>G, 124C>T, 70A>G, -23-14dup; and 180G>A |
| **Notes** | NA | NA | NA |

**Abnormal-readout comparators:** "mRNA cleavage activity **smaller than** 0.9" — strict `<`. "Luciferase activity **higher than** 7" — strict `>`.

**Source-fidelity flags for this file:**
- The insertion allele is written inconsistently between the two instance columns: `ins111_112ACGTAGACATTCCT` (instance 1) vs `g.111_112insACTGTAGACATTCCT` (instance 2) — the inserted sequences differ (ACGTAGACATTCCT vs ACTGTAGACATTCCT). Transcribed as written; not reconciled.
- Instance 2's variant list contains "e" (Italian/Portuguese for "and") twice, an unbalanced closing parenthesis, and a trailing comma. Preserved verbatim.
- Variant nomenclature mixes `+`, `g.`, and bare-number styles and is not HGVS-conformant against NR_003051.3. Preserved verbatim.

---

### Appendix E — VCEP Comments: "Updates to PM1 10/23/25"

*Source: `VCEP Comments.docx`, listed in the specification as "VCEP Comments: Updates to PM1 10/23/25". Transcribed in full.*

> **PM1 Update Notes - RMRP**
>
> Currently, PM1 says: "Defined to include insertions/duplications between the TATA box (spanning n.-32 to n.-24) and the transcription start site (n.4). Caveat: variant must also meet PM2."
>
> However, we have come across this variant, which should meet PM1 but cannot because its AF is a little higher than PM2 but not close to BS1 or BA1: https://curation.clinicalgenome.org/variant-central/adaa60fb-2f9f-45de-97e9-b7509bdad377/interpretation/1ce71cec-8393-41c0-8a81-8514d688ef19/
>
> This variant is able to meet PM3 because PM3 says: "Caveat: All variants should be sufficiently rare - variant does not have to meet PM2 specification criteria but variant should not meet BS1/BA1 criteria (unless a suspected founder variant). The applicability of PM3 to suspected founder variants exceeding the BS1/BA1 threshold will be evaluated on a case-by-case basis by the VCEP."
>
> We would like to amend PM1 to say the same thing as PM3, that is:
>
> "Defined to include insertions/duplications between the TATA box (spanning n.-32 to n.-24) and the transcription start site (n.4). Caveat: All variants should be sufficiently rare - variant does not have to meet PM2 specification criteria but variant should not meet BS1/BA1 criteria (unless a suspected founder variant). The applicability of PM1 to suspected founder variants exceeding the BS1/BA1 threshold will be evaluated on a case-by-case basis by the VCEP."
>
> The SCID VCEP discussed this modification on 9/26/2025 and approved with consensus.

**Status:** the amended wording proposed in this document **is** the PM1 wording present in the v1.3 specification PDF, so the amendment has been incorporated. The v1.3 release notes mention only the Rules for Combining Criteria change, so this PM1 amendment was presumably applied in an earlier release; the package does not state which.

---

### Appendix F — Files & Images distributed with the specification

Reproduced verbatim from the final page of the specification PDF:

| Label | Description | Local file | Transcribed |
|---|---|---|---|
| PS2_PM6 | SVI recommendations for de novo criteria | `PS2_PM6.pdf` | Yes — Appendix A |
| VCEP Comments | Updates to PM1 10/23/25 | `VCEP Comments.docx` | Yes — Appendix E |
| PS3_BS3 | RMRP Functional Evidence | `PS3_BS3.xlsx` | Yes — Appendix D |
| PM3 | SVI recommendations for pm3 criterion | `PM3.pdf` | Yes — Appendix B |
| PP1 | Specifications | `PP1.pdf` | Yes — Appendix C |

*(The label "SVI recommendations for pm3 criterion" uses lowercase "pm3" in the source; preserved.)*

**External references cited but NOT distributed** (not retrieved, contents not reproduced):
- PIDTC 2022 diagnostic criteria summary — Google Doc link from the PP4 footnote.
- Oza et al. full text (PMID: 30311386) — only Tables 4a/4b excerpt distributed.
- Sabarinathan et al., 2013 (PMID: 23315997) — cited for the PP3 p-value threshold.
- Dvorak et al., 2019 (PMID: 30193840) — cited for the genetic heterogeneity parameter.
- Richards et al., 2015; SVI VCEP Review Committee (PubMed: 29543229).
- RNAsnp web tool (https://rth.dk/resources/rnasnp/); Whiffin/Ware calculator (https://www.cardiodb.org/allelefrequencyapp/).

---

## Source Issues and Flags

Consolidated list of typos, inconsistencies and apparent VCEP errors found in the v1.3 package. All are transcribed as written above and are **not** silently corrected.

| # | Location | Issue |
|---|---|---|
| 1 | PP4 point list vs. Note 2 | T-cell lymphopenia is listed at **0.5 pt** in the table but Note 2 says allocate **0.25 points**. Unreconciled contradiction. |
| 2 | BS2 | BS2_Strong is ">=3 (3 or more) homozygotes"; BS2_Supporting is "at least 2 homozygotes" — the tiers overlap at 3+; no upper bound stated for Supporting. |
| 3 | PP3 | "Ensembl NR__003051.3" — double underscore (transcript is NR_003051.3). Also "access SNP effects" where "assess" appears intended. |
| 4 | PS3 approved assays | Doubled closing parentheses: "(PMID: 17701897))" and "(PMID: 16254002))". |
| 5 | PP1 VCEP text | "do not count wild-type/wild-type, individuals" — stray comma. Also the VCEP requirement that unaffected contributors be heterozygous carriers **conflicts with** the Oza Table 4b legend, which permits counting unaffecteds who are wild-type for both variants. |
| 6 | PP1 Table 4a (source) | "See Table4b" (missing space) in the Strong column. |
| 7 | PS3_BS3.xlsx | Inserted-sequence discrepancy between instance columns: `ACGTAGACATTCCT` vs `ACTGTAGACATTCCT`. |
| 8 | PS3_BS3.xlsx | Instance 2 variant list contains "e" (non-English "and") twice, an unbalanced `)`, and a trailing comma; nomenclature is non-HGVS. |
| 9 | PS3_BS3.xlsx filename/title | Named "PS3_BS3" and "RMRP Functional Evidence" but BS3 is Not Applicable and no BS3 content is present. |
| 10 | PM3 (VCEP) vs PM3.pdf (SVI) | SVI PM3 requires variants to meet PM2; the RMRP VCEP explicitly waives this in favour of a BS1/BA1 ceiling. Operative rule = VCEP. |
| 11 | PS2/PM6 vs PS2_PM6.pdf | The VCEP instructs "Reduce points per proband by half if the phase is unconfirmed", but SVI Table 1 halves points based on **parental relationships**, not phase. Terminology mismatch, unreconciled. |
| 12 | PM6 | PM6 has no Very Strong tier in the criterion section and PM6_Very Strong appears nowhere in the combining rules, although SVI Table 2 defines PM6_VeryStrong at 4 points. The VCEP appears to deliberately cap PM6 at Strong, but does not say so. |
| 13 | PM1 / PM4 | Both refer to "the transcription start site (n.4)". Transcribed as written. |
| 14 | PS1 / PM4 headings | Criterion titles retain protein-centric ACMG wording ("Same amino acid change", "Protein length changes") while the VCEP text redefines them at the nucleotide level for this non-coding gene. |
| 15 | Release notes vs. package | v1.3 release notes cite only the Rules-for-Combining-Criteria edit, yet the distributed `VCEP Comments.docx` (PM1 amendment, approved 9/26/2025, dated 10/23/25) is bundled with this release. The package does not state in which version the PM1 amendment landed. |

**Explicitly not specified by this VCEP** (do not substitute generic guidance): PS1_Strong / PS1_Moderate, PS3_Moderate, PM4_Supporting, PM6_Very Strong, and any Tavtigian-style points-based classification scheme. Where the specification says "Use ClinGen SVI recommendations", the applicable SVI documents are the ones distributed with the package and reproduced in Appendices A-C; nothing beyond them is supplied.

---

## Version History

| Version | Released | Notes (verbatim from source where available) |
|---|---|---|
| **1.3** | 5/1/2026 | Edited Rules for Combining Criteria to reflect standard combinations plus (A) 1 very strong + 1 supporting = Likely Pathogenic and (B) 1 Strong Benign = Likely Benign. |

*Earlier version history is not included in the v1.3 specification package and is therefore not reproduced here.*

---

*This document was compiled from the ClinGen VCEP specification `ClinGen_ACMG_Specifications_RMRP_v1.3.pdf` and its five distributed supplementary files, all of which were opened and transcribed. For the most current version, please refer to the ClinGen website (https://cspec.genome.network/cspec/ui/svi/).*
