# ClinGen Platelet Disorders Expert Panel Variant Interpretation Guidelines for GP9

**Version:** 1.1.0

**Released:** 9/29/2025

**Affiliation:** Platelet Disorders VCEP

**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

**DOI:** 10.5281/zenodo.21434005

**Release Notes:** The BP4 rule was corrected to include less than “or equal to”.

## Gene Information

| Attribute | Value |
|---|---|
| Gene | GP9 (HGNC:4444) |
| HGNC Name | glycoprotein IX platelet |
| Transcript | NM_000174.5 |
| Disease | Bernard-Soulier syndrome (MONDO:0009276) |
| Inheritance | Autosomal recessive inheritance |

## Source provenance

This transcription is controlled by the six files distributed with the GP9 v1.1 specification:

- `ClinGen_ACMG_Specifications_GP9_v1.1.pdf`
- `PVS1 flowchart for GP9 gene.pptx`
- `Guidance for Combining Pathogenic and Benign Rule Codes.docx`
- `Instructions for PS2_PM6 code use.docx`
- `Instructions for PM3 code use.docx`
- `PS3_Supporting Functional Assays.xlsx`

Supplement-derived tables below identify their controlling artifact. Source typos, exact comparison operators, and unresolved contradictions are preserved. No external guidance has been used to fill source gaps.

## Pathogenic Criteria

### PVS1 — Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specification:** For Very Strong, Strong, Moderate, and Supporting strengths, use the GP9 modified decision tree as per the SVI WG. See Appendix A for a source-derived transcription of `PVS1 flowchart for GP9 gene.pptx`.

### PS1 — Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val→Leu caused by either G>C or G>T in the same codon. Beware of changes that impact splicing rather than at the amino-acid/protein level.

| Strength | Specification | Modification Type |
|---|---|---|
| Strong | Use as originally specified, but the comparison variant must reach a pathogenic classification using the **the these** rule specifications in order to apply code. | General recommendation |
| Moderate | Use as originally specified, but the comparison variant must reach a likely pathogenic classification using the **the these** rule specifications in order to apply code. | General recommendation |

“The these” is preserved from the source.

### PS2 — De Novo

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Confirmation of paternity only is insufficient; egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

Only applicable when the proband has a known pathogenic or likely pathogenic variant according to the BSS rule specifications along with the de novo variant. Only use “highly specific phenotype” scoring if all three BSS genes were sequenced. Otherwise use “consistent but not highly specific” scoring.

| Strength | Source-stated total | Modification Type |
|---|---:|---|
| Very Strong | 4 points | Disease-specific |
| Strong | 2 points | Disease-specific |
| Moderate | 1 point | Disease-specific |
| Supporting | 0.5 point | Disease-specific |

See Appendix B for the attached SVI table. The core states that PM6 is Not Applicable for GP9 and directs use of PS2, while the attachment labels PM6 strengths. Both statements are preserved as an unresolved conflict; no precedence is inferred.

### PS3 — Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Functional studies validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

| Strength | Specification | Modification Type |
|---|---|---|
| Strong | In a transgenic animal model, must demonstrate minimal to no function. | Disease-specific |
| Supporting | Functional assays measuring quantity of GP9 expression on cell surface measured by flow cytometry analysis of GPIb and GPIX when there is absent or near absent expression, `>75%` reduction (see spreadsheet for more detail). | Disease-specific |

See Appendix D for a source-derived summary of the GP9-relevant `GPIX` worksheet in `PS3_Supporting Functional Assays.xlsx`.

### PS4 — Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared with controls. The core notes an RR or OR `>5.0` whose confidence interval excludes 1.0, and permits multiple unrelated affected observations with absence from controls as Moderate evidence for very rare variants when case-control studies may not reach statistical significance.

According to Bragadottir et al., individuals heterozygous for Bernard-Soulier syndrome variants are considered informative due to measurable, quantitative abnormalities relevant to the disease (PMID: 25370924).

All caveats apply:

1. The variant must be sufficiently rare, meeting PM2_supporting.
2. There must be an assumed unrelated biallelic BSS patient, meeting PP4, before heterozygotes are considered.
3. A single proband of a family can be included in either PM3 (biallelic proband) or PS4 (monoallelic proband), not both.
4. Any additional family members are not included in PS4; they may be considered for segregation in PP1.

| Evidence | Points |
|---|---:|
| Significantly reduced surface expression of GP1b measured by flow cytometry | 0.5 pt |
| **OR** giant platelets (`MPD >7 microns`) or macrothrombocytopenia (`MPV >12 fL` and platelet count `<150x10^9/L`) | 0.25 pt |

| Strength | Score | Modification Type |
|---|---|---|
| Moderate | `2+` points | Disease-specific |
| Supporting | `1-1.75` points | Disease-specific |

### PM1 — Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain without benign variation.

**Not Applicable.** Rule does not apply due to gene being polymorphic.

### PM2 — Absent from Controls

**Original ACMG Summary:** Absent from controls, or at extremely low frequency for a recessive disorder, in population databases. Population data for indels may be poorly called by next-generation sequencing.

| Strength | Specification | Modification Type |
|---|---|---|
| Supporting | gnomAD MAF of less than or equal to `0.0000329`. | Disease-specific, Gene-specific |

### PM3 — In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Testing of parents or offspring is required to determine phase.

In trans variants classified as a **variants** of uncertain significance, as per the GP9 rule specifications, must meet PM2_supporting to be scored. Conversely, in trans variants that meet a pathogenic or likely pathogenic classification using the GP9 rule specifications do not have to meet PM2_supporting; however, they cannot meet BS1 or BA1. “A variants” is preserved from the source.

Very Strong, Strong, Moderate, and Supporting use the proposed SVI point recommendations in Appendix C. Both variants must be classified using these rule specifications.

### PM4 — Protein Length Changes

**Original ACMG Summary:** Protein-length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Specification | Modification Type |
|---|---|---|
| Moderate | Use with no specification. | No change |

### PM5 — Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino-acid residue where a different missense change determined to be pathogenic has been seen before. Beware of changes that impact splicing rather than at the amino-acid/protein level.

| Strength | Specification | Modification Type |
|---|---|---|
| Moderate | Use as originally specified, but the comparison variant must reach a pathogenic classification using these rule specifications in order to apply code. | General recommendation |
| Supporting | Use as originally specified, but the comparison variant must reach a likely pathogenic classification using these rule specifications in order to apply code. | General recommendation |

### PM6 — De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**Not Applicable.** Use PS2 for de novo cases in lieu of this rule code.

The attached generic de novo table nevertheless labels PM6 strengths. Both source statements are preserved as an unresolved conflict; no precedence is inferred.

### PP1 — Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. May be used as stronger evidence with increasing segregation data.

For Bernard-Soulier syndrome, segregation is informative both for additional relatives with BSS and for heterozygous relatives with measurable, quantitative abnormalities relevant to the disease. There must be a biallelic BSS patient meeting PP4 before segregation points are awarded. Heterozygous relatives counted for PP1 must not be counted for PS4.

| Family member or evidence | Points |
|---|---:|
| Proband | 0; proband should be accounted for in PP4 or PS4 |
| BSS-affected relative with the same biallelic variant(s) identified in the proband | 1 pt |
| Relative heterozygous for the variant under assessment with significantly reduced GP1b surface expression by flow cytometry | 0.5 pt |
| **OR** relative heterozygous for the variant under assessment with giant platelets (`MPD >7 microns`) or macrothrombocytopenia (`MPV >12 fL` and platelet count `<150x10^9/L`) | 0.25 pt |

Only score one parent of a homozygous proband in a consanguineous pedigree.

| Strength | Total segregation score | Modification Type |
|---|---|---|
| Strong | `3+` points | Disease-specific |
| Moderate | `2-2.75` points | Disease-specific |
| Supporting | `1-1.75` points | Disease-specific |

### PP2 — Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene with a low rate of benign missense variation and where missense variants are a common disease mechanism.

**Not Applicable.** BSS is a rare disease and this gene is not constrained for missense variation (gnomAD).

### PP3 — Computational Evidence

**Original ACMG Summary:** Multiple computational lines support a deleterious effect on the gene or gene product. Correlated algorithms are not independent, and PP3 may be used only once per variant evaluation.

| Strength | Specification | Modification Type |
|---|---|---|
| Moderate | REVEL score `≥0.773`, based on Pejaver et al., 2022 (PMID: 36413997). | Gene-specific |
| Supporting | REVEL score `≥0.644` (to `<0.773`), based on Pejaver et al., 2022 (PMID: 36413997), **OR** suggested splicing **affect** using SpliceAI greater than or equal to `0.5`. | Gene-specific |

“Splicing affect” is preserved from the source.

### PP4 — Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

| Strength | Specification | Modification Type |
|---|---|---|
| Moderate | Must meet both: (1) proband with platelet aggregation absent for ristocetin and present for all other agonists **OR** flow cytometry or Western blot less than `10%` expression of GPIba; and (2) full sequencing of GP1BA, GP1BB, and GP9 plus deletion/duplication analysis. | Disease-specific |
| Supporting | Proband with platelet aggregation absent for ristocetin and present for all other agonists, **OR** flow cytometry or Western blot less than `10%` expression of GPIba. | Disease-specific |

### PP5 — Reputable Source

**Original ACMG Summary:** A reputable source reports the variant as pathogenic, but the evidence is unavailable for independent evaluation.

**Not Applicable.** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

## Benign Criteria

### BA1 — Allele Frequency Stand Alone

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

| Strength | Specification | Modification Type |
|---|---|---|
| Stand Alone | gnomAD MAF greater than or equal to `0.001` (or `0.1%`). | Gene-specific |

### BS1 — Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for the disorder.

| Strength | Specification | Modification Type |
|---|---|---|
| Strong | gnomAD MAF greater than or equal to `0.0007` but less than `0.001`. | Gene-specific |

### BS2 — Observed in a Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

| Strength | Specification | Modification Type |
|---|---|---|
| Strong | One or more homozygotes who are unaffected, proven with aggregometry **OR** flow cytometry **AND** normal platelet count **AND** normal platelet size. | Disease-specific |

### BS3 — Functional Studies Showing No Effect

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

| Strength | Specification | Modification Type |
|---|---|---|
| Strong | Must demonstrate normal aggregometry in a transgenic mouse model. | Disease-specific |
| Supporting | In a heterologous cell line, must demonstrate **both** normal expression and normal protein function as compared to wildtype. | Disease-specific |

### BS4 — Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected family members. The core cautions that phenocopies and more than one pathogenic variant can confound apparent lack of segregation.

| Strength | Specification | Modification Type |
|---|---|---|
| Strong | Variant not tracking in an affected family member. | Disease-specific |

### BP1–BP7 — Benign Supporting

| Criterion | Status | Specification | Modification Type |
|---|---|---|---|
| BP1 | Not Applicable | Rule does not apply as truncating variants do not predominate and missense variants are a known cause of disease. | N/A |
| BP2 | Supporting | Use as written for recessive variants (i.e. - variant must be observed in cis with a pathogenic variant). | Disease-specific |
| BP3 | Supporting | Use with no specification. | None |
| BP4 | Supporting | Missense: REVEL score is **less than or = to `0.290`** **AND** SpliceAI score is zero. **OR** synonymous/intronic: SpliceAI score is zero. Do not use if PP3 applies. | Gene-specific |
| BP5 | Not Applicable | Do not use because an individual can be a carrier of an unrelated pathogenic variant for a recessive disorder. | N/A |
| BP6 | Not Applicable | Not for use per the ClinGen SVI VCEP Review Committee (PMID: 29543229). | N/A |
| BP7 | Supporting | Use SpliceAI to rule out possible splicing defect (`score = 0.2 or less`) and reference PhyloP (`score = 1.5 or less`) to assess conservation. Can be used for intronic variants and along with BP4. | Gene-specific |

## Rules for Combining Criteria

These are the qualitative combinations printed in the core GP9 PDF.

### Pathogenic

- 1 Very Strong AND ≥1 Strong
- 1 Very Strong AND ≥2 Moderate
- 1 Very Strong AND 1 Moderate AND 1 Supporting
- 1 Very Strong AND ≥2 Supporting
- ≥2 Strong
- 1 Strong AND ≥3 Moderate
- 1 Strong AND 2 Moderate AND ≥2 Supporting
- 1 Strong AND 1 Moderate AND ≥4 Supporting

### Likely Pathogenic

- 1 Very Strong AND 1 Moderate
- 1 Strong AND 1 Moderate
- 1 Strong AND ≥2 Supporting
- ≥3 Moderate
- 2 Moderate AND ≥2 Supporting
- 1 Moderate AND ≥4 Supporting
- 1 Strong AND 2 Moderate

### Benign

- ≥2 Strong
- 1 Stand Alone

### Likely Benign

- 1 Strong AND 1 Supporting
- ≥2 Supporting

## Guidance for Combining Conflicting Criteria

The following tables transcribe `Guidance for Combining Pathogenic and Benign Rule Codes.docx`. They apply when both benign and pathogenic evidence codes apply; such variants are not automatically assigned VUS. The document directs use of Tavtigian et al. 2020 (PMID: 32720330).

### Table 2. Point values for ACMG/AMP strength of evidence categories

| Evidence Strength | Pathogenic | Benign |
|---|---:|---:|
| Indeterminate | 0 | 0ᵃ |
| Supporting | 1 | −1 |
| Moderate | 2 | −2ᵇ |
| Strong | 4 | −4 |
| Very strong | 8 | −8ᵇ |

### Table 3. Point-based variant classification categories

| Category | Point ranges |
|---|---|
| Pathogenic | `≥10` |
| Likely Pathogenic | `6 to 9`ᵃ |
| Uncertain | `0 to 5` |
| Likely Benign | `−1 to −6`ᵃ |
| Benign | `≤ −7` |

The source images display superscript `a` and `b` markers but the distributed DOCX supplies no definitions for them.

## Appendix A — Source-derived PVS1 flowchart transcription

**Controlling artifact:** `PVS1 flowchart for GP9 gene.pptx`. This prose/table appendix is an editorial transcription for accessibility; the slide's exact connectors and visual red-X marks control.

The slide states that GP9 has a single coding exon which is not considered subject to NMD. It nevertheless retains predicted-NMD branches connected to PVS1/N/A endpoints and visibly places red X marks through/beside those route sets. Both features are preserved here as an unresolved source contradiction.

**Shared decision labels:** critical region (`c`) is the transmembrane domain, aa 148–169. The terminal-most PTV is `NM_000174.5:c.450G>A (p.Trp150Ter)`, Xu et al., 2010, PMID 20497174. In unknown-role branches, frequent/absent from healthy population databases leads to N/A; not frequent/present continues to the displayed size thresholds.

### Nonsense or frameshift

| Route | Outcome |
|---|---|
| Predicted to undergo NMD (`b`); relevant exon present | PVS1, in the visually red-X-negated route set |
| Predicted to undergo NMD (`b`); relevant exon absent | N/A, in the visually red-X-negated route set |
| Not predicted to undergo NMD (`b`); transmembrane critical region | PVS1_Strong |
| Not predicted to undergo NMD; unknown role; frequent/absent | N/A |
| Not predicted to undergo NMD; unknown role; not frequent/present; truncation `>10%` before p.160 | PVS1_Strong |
| Not predicted to undergo NMD; unknown role; not frequent/present; truncation `<10%` at/after p.160 | PVS1_Moderate |

### GT--AG 1,2 splice sites (`a`)

| Route | Outcome |
|---|---|
| Reading frame disrupted; NMD predicted (`b`); relevant exon present | PVS1, in the visually red-X-negated route set |
| Reading frame disrupted; NMD predicted (`b`); relevant exon absent | N/A, in the visually red-X-negated route set |
| Reading frame disrupted; NMD not predicted (`b`); transmembrane critical region | PVS1_Strong |
| Reading frame preserved; transmembrane critical region | PVS1_Strong |
| Either non-NMD/preserved-frame route; unknown role; frequent/absent | N/A |
| Either non-NMD/preserved-frame route; unknown role; not frequent/present; truncation `>10%` before p.160 or deletion `>17 aa`, as displayed on the applicable branch | PVS1_Strong |
| Either non-NMD/preserved-frame route; unknown role; not frequent/present; truncation `<10%` at/after p.160 or deletion `<18 aa`, as displayed on the applicable branch | PVS1_Moderate |

### Single-exon through full-gene deletion

| Route | Outcome |
|---|---|
| Full-gene deletion | PVS1 (`d`) |
| Frame disrupted; NMD predicted (`b`); relevant exon present | PVS1, in the visually red-X-negated route set |
| Frame disrupted; NMD predicted (`b`); relevant exon absent | N/A, in the visually red-X-negated route set |
| Frame disrupted with NMD not predicted (`b`), or frame preserved; transmembrane critical region | PVS1_Strong |
| Either non-NMD/preserved-frame route; unknown role; frequent/absent | N/A |
| Either non-NMD/preserved-frame route; unknown role; not frequent/present; deletion `>17 aa` | PVS1_Strong |
| Either non-NMD/preserved-frame route; unknown role; not frequent/present; deletion `<18 aa` | PVS1_Moderate |

### Duplication(≥1 exon in size and must be completely contained within gene)

| Route | Outcome |
|---|---|
| Proven in tandem; frame disrupted and NMD predicted | PVS1 |
| Proven in tandem; no/unknown frame disruption or NMD | N/A |
| Presumed in tandem; frame presumed disrupted and NMD predicted | PVS1_Strong |
| Presumed in tandem; no/unknown frame disruption or NMD | N/A |
| Proven not in tandem | N/A |

### Initiation codon

| Route | Outcome |
|---|---|
| Different functional transcript uses an alternative start codon | N/A |
| No known alternative start; ≥1 pathogenic variant upstream of closest in-frame Met32: `NM_000174.5(GP9):c.70T>C (p.Cys24Arg)`, ClinVar 13533 (Pathogenic, 2 stars) | PVS1_Moderate |
| No known alternative start; no pathogenic variant upstream of Met32 | PVS1_Supp |

The slide supplies letter markers `a`–`d` at nodes but no marker definitions or separate reference list. Their meanings are not inferred.

## Appendix B — Source-derived de novo tables

**Controlling artifacts:** the GP9 core PDF and `Instructions for PS2_PM6 code use.docx`. These are accessibility transcriptions, not new scoring rules.

Use “Phenotype highly specific for gene” for BSS when all three genes (GP1BA, GP1BB, and GP9) have been sequenced. Use “Phenotype consistent with gene but not highly specific ” when only one or two genes have been sequenced; the trailing space in the source quotation is noted here but has no operational meaning.

### Table 1. Points awarded per de novo occurrence

The source groups “Confirmed de novo” and “Assumed de novo” under the header **Points per Proband**.

| Phenotypic consistency | Confirmed de novo | Assumed de novo |
|---|---:|---:|
| Phenotype highly specific for gene | 2 | 1 |
| Phenotype consistent with gene but not highly specific | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity* | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

`*Maximum allowable value of 1 may contribute to overall score`

### Table 2. Recommendation for determining the appropriate ACMG/AMP evidence strength level for de novo occurrence(s)

| Supporting (PS2_Supporting or PM6_Supporting) | Moderate (PS2_Moderate or PM6) | Strong (PS2 or PM6_Strong) | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |
|---:|---:|---:|---:|
| 0.5 | 1 | 2 | 4 |

These are bare source cells. The attachment supplies no `≥` ladder or pooling rule. The core makes PM6 Not Applicable and directs use of PS2, while this attachment explicitly labels PM6 strengths. The conflict is unresolved and no precedence is inferred.

## Appendix C — Source-derived PM3 tables

**Controlling artifacts:** the GP9 core PDF and `Instructions for PM3 code use.docx`. The attachment's general footnote and the GP9 core's partner-variant exception differ. The conflict is unresolved and no precedence is inferred.

### Table 1. Points awarded per in trans proband

<table>
  <thead>
    <tr><th rowspan="2">Classification/Zygosity of other variant¹</th><th colspan="2">Points per Proband</th></tr>
    <tr><th>Confirmed in trans</th><th>Phase unknown</th></tr>
  </thead>
  <tbody>
    <tr><td>Pathogenic or Likely pathogenic variant</td><td>1.0</td><td>0.5 (P)<br>0.25 (LP)</td></tr>
    <tr><td>Homozygous occurrence<br><em>(max point 1.0)</em></td><td>0.5</td><td>N/A</td></tr>
    <tr><td>Uncertain significance variant<br><em>(max point 0.5)</em></td><td>0.25</td><td>0.0</td></tr>
  </tbody>
</table>

`¹All variants should be sufficiently rare (meet PM2 specification); P - Pathogenic; LP - Likely pathogenic`

### Table 2. Recommendation for determining the appropriate evidence strength level for PM3

| PM3_Supporting | PM3 | PM3_Strong | PM3_VeryStrong |
|---:|---:|---:|---:|
| 0.5 | 1.0 | 2.0 | 4.0 |

These are bare source cells. The attachment supplies no `≥` ladder, no cross-proband pooling instruction, and no separate consanguinity-based homozygous values.

## Appendix D — Source-derived GP9 PS3 assay summary

**Controlling artifact:** the `GPIX` sheet of `PS3_Supporting Functional Assays.xlsx`. This editorial table selects the cells relevant to GP9; it is not a full workbook transcription. The workbook also contains visible sibling-gene sheets `GPIBA` and `GPIBB`, and a hidden, incomplete `Mufti` sheet containing unrelated VWF/FVIII material; those do not expand GP9 PS3.

| PMID / author / year as printed | Material and system | Proposed strength and threshold |
|---|---|---|
| PMID: 8608225 / Garunee Sae-Tung / 1996 | Asp21Gly and Asn45Ser (legacy nomenclature) GP IX generated by site directed mutagenesis on pDX; transfection into either CHO αβ cells or cotransfection with GP Ibα and GP lbβ into wild-type CHO cells | `PS3_supporting` when absent or near absent expression, `>75% reduction` |
| PMID: 10527407 / Keijiroh Suzuki / 1999 | Phe71Ser (legacy nomenclature) GP IX generated by site directed mutagenesis on pcDNA3.1; cotransfection with GP Ibα and GP lbβ into CHO-K1 cells | `PS3_supporting` when absent or near absent expression, `>75% reduction` |
| PMID: 10583255 / Shinji Kunishima / 2001 | Cys97Tyr and Cys73Tyr (legacy nomenclature) GP IX generated by site directed mutagenesis on pDX; cotransfection with GP Ibα and GP lbβ into CHO DUK- cells | `PS3_supporting` when absent or near absent expression, `>75% reduction` |
| PMID: 12100158 / François Lanza / 2002 | Leu7Pro (legacy nomenclature) GP IX generated by site directed mutagenesis on pDX; cotransfection with GP Ibα and GP lbβ into CHO K1- cells | `PS3_supporting` when absent or near absent expression, `>75% reduction` |
| `PMID: 8972003` / Masaaki Noda / 1996 | ` C73Y` (legacy nomenclature) GP IX generated by site directed mutagenesis cloned into pBK-EF; co-transfection into 293 cells with GP lbβ | `PS3_supporting` when absent or near absent expression, `>75% reduction` |

All five use a quantitative flow-cytometric cell-surface expression readout, wild-type GPIX as positive control, “Equivalent to WT” as normal, and “Sigificantly decreased from WT” as abnormal. The misspelling is preserved. Empty-vector negative controls are populated only for the first three columns. Biological-replicate information is populated only for Suzuki (“mean of seven separate experiments”) and Kunishima (“three independent transfection experiments”). Validation-control counts and statistical-analysis descriptions are not populated.

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.1.0 document corrections | 2026-08-10 | Source-first correction against all six distributed artifacts: `ClinGen_ACMG_Specifications_GP9_v1.1.pdf`; `PVS1 flowchart for GP9 gene.pptx`; `Guidance for Combining Pathogenic and Benign Rule Codes.docx`; `Instructions for PS2_PM6 code use.docx`; `Instructions for PM3 code use.docx`; and `PS3_Supporting Functional Assays.xlsx`. Replaced the inaccurate PVS1 summary with the slide's exact branch strengths, thresholds, literal `Duplication(≥1 exon in size and must be completely contained within gene)` scope, duplication/initiation topology, red-X/NMD contradiction, and marker limitations; restored complete PS2 and PM3 tables, exact two-level grouped header framing, printed phase-unknown cell forms, bare strength cells, footnotes, and the P-versus-LP distinction; removed invented PM3 consanguinity categories and generic conflicting-evidence point mappings; restored exact combining-table values and undefined superscripts; restored literal BP4/BP7 wording; preserved source contradictions without inferred precedence; preserved source typos and exact comparators; and labelled all supplement-derived appendices as editorial accessibility summaries controlled by their named artifacts. |
| 1.1.0 | 9/29/2025 | BP4 rule corrected to include less than “or equal to”. |
| 1.0.0 | Initial | Initial release. |
