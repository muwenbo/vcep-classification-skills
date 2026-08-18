# ClinGen Platelet Disorders Expert Panel Variant Interpretation Guidelines for GP1BA

- **Version:** 1.1.0
- **Released:** 9/29/2025
- **Affiliation:** Platelet Disorders VCEP
- **Based on:** Richards et al., 2015 ACMG/AMP Guidelines
- **Gene:** GP1BA (HGNC:4439)
- **HGNC name:** glycoprotein Ib platelet subunit alpha
- **Transcript:** NM_000173.7
- **Disease:** Bernard-Soulier syndrome (MONDO:0009276)
- **Inheritance:** Autosomal recessive inheritance
- **Specification DOI:** 10.5281/zenodo.21433981

---

## Source note

This transcription integrates the core specification with its five distributed attachments. Source contradictions, undefined superscripts, typographic errors, comparator forms, and decision-tree topology are retained and flagged rather than silently resolved.

## Pathogenic criteria

### PVS1 — Null variant

**Original ACMG summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**

- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3′ end of a gene.
- Use caution with splice variants predicted to cause exon skipping while leaving the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP specification:** See the GP1BA modified decision tree. At Very Strong, Strong, Moderate, and Supporting strengths, use the GP1BA modified decision tree as per SVI WG.

#### Distributed GP1BA decision tree

The source slide states that GP1BA has a single coding exon which is not considered subject to NMD. It nevertheless prints NMD paths; red X marks visibly sit beside the PVS1/N/A terminal pair for the NMD path in each of the nonsense/frameshift, GT--AG 1,2 splice-site, and deletion sections. Superscripts `a`, `b`, `c`, and `d` are printed but not defined in the slide or its notes.

##### Nonsense or Frameshift

- Predicted to undergo NMD^b:
  - exon present in biologically-relevant transcript(s) → PVS1 [red X beside terminal pair];
  - exon absent from biologically-relevant transcript(s) → N/A [red X beside terminal pair].
- Not predicted to undergo NMD^b:
  - truncated/altered region is critical to protein function^c; the transmembrane domain (amino acids 532-553) is considered critical → PVS1_Strong;
  - role of region unknown → LoF variants in this exon are frequent in the general population and/or exon is absent from biologically-relevant transcript(s) → N/A;
  - role of region unknown → LoF variants are not frequent and exon is present → variant removes `>10%` of protein (truncation before p.588) → PVS1_Strong;
  - same preceding path → variant removes `<10%` of protein (truncation at/after p.588) → PVS1_Moderate.

The slide annotates the terminal most PTV as `NM_000173.7:c.1846_1852del (p.Asn616Valfs*5)`, ClinVar 1703858 (Pathogenic, 1 star).

##### GT--AG 1,2 splice sites^a

- Exon skipping or use of a cryptic splice site disrupts the reading frame and is predicted to undergo NMD^b:
  - exon present → PVS1 [red X beside terminal pair];
  - exon absent → N/A [red X beside terminal pair].
- Exon skipping or use of a cryptic splice site disrupts the reading frame and is **NOT** predicted to undergo NMD^b → follow the critical/unknown-region paths below.
- Exon skipping or use of a cryptic splice site preserves the reading frame → follow the critical/unknown-region paths below.
- Truncated/altered region is critical^c; the transmembrane domain (amino acids 532-553) is considered critical → PVS1_Strong.
- Role unknown → LoF frequent and/or exon absent → N/A.
- Role unknown → LoF not frequent and exon present:
  - variant removes `>10%` (truncation before p.588 or deletion of `>65 amino acids`) → PVS1_Strong;
  - variant removes `<10%` (truncation at/after p.588 or deletion of `<66 amino acids`) → PVS1_Moderate.

##### Deletion (Single exon to full gene)

- Full gene deletion → PVS1^d.
- Single-to-multi-exon deletion disrupts the reading frame and is predicted to undergo NMD^b:
  - exon present → PVS1 [red X beside terminal pair];
  - exon absent → N/A [red X beside terminal pair].
- Single-to-multi-exon deletion disrupts the reading frame and is **NOT** predicted to undergo NMD^b → follow the critical/unknown-region paths below.
- Single-to-multi-exon deletion preserves the reading frame → follow the critical/unknown-region paths below.
- Truncated/altered region is critical^c; the transmembrane domain (amino acids 532-553) is considered critical → PVS1_Strong.
- Role unknown → LoF frequent and/or exon absent → N/A.
- Role unknown → LoF not frequent and exon present:
  - variant removes `>10%` (`deletion of >65 amino acids`) → PVS1_Strong;
  - variant removes `<10%` (`deletion of <66 amino acids`) → PVS1_Moderate.

##### Duplication

The duplication is `≥1 exon in size and must be completely contained within gene`.

- Proven in tandem → reading frame disrupted and NMD predicted to occur → PVS1.
- Proven in tandem → no or unknown impact on reading frame and NMD → N/A.
- Presumed in tandem → reading frame presumed disrupted and NMD predicted to occur → PVS1_Strong.
- Presumed in tandem → no or unknown impact on reading frame and NMD → N/A.
- Proven not in tandem → N/A.

##### Initiation Codon

- No known alternative start codon in other transcripts → `≥1 pathogenic variant(s)` upstream of the closest potential in-frame start codon at Met68 → PVS1_Moderate.
- No known alternative start codon in other transcripts → no pathogenic variant(s) upstream of the closest potential in-frame start codon at Met68 → PVS1_Supp.
- Different functional transcript uses alternative start codon → N/A.

> **Source issue:** The tree prints no exact-10% path. Its paired cutoffs are `>65 amino acids` and `<66 amino acids`; no inferred interval has been added. The red-X meaning and superscripts `a`–`d` are not defined in the distributed slide or notes.

### PS1 — Same amino acid change

**Original ACMG summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

| Strength | VCEP specification |
|---|---|
| Strong | Use as originally specified, but the comparison variant must reach a pathogenic classification using these rule specifications. |
| Moderate | Use as originally specified, but the comparison variant must reach a likely pathogenic classification using these rule specifications. |

### PS2 — De novo

**Original ACMG summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

PS2 is only applicable when the proband has a known pathogenic or likely pathogenic variant according to the BSS rule specifications along with the de novo variant. Only use “highly specific phenotype” scoring if GP1BA, GP1BB, and GP9 were all sequenced; otherwise use “consistent but not highly specific” scoring.

**Table 1. Points awarded per de novo occurrence**

<table>
  <thead>
    <tr><th rowspan="2">Phenotypic consistency</th><th colspan="2">Points per Proband</th></tr>
    <tr><th>Confirmed de novo</th><th>Assumed de novo</th></tr>
  </thead>
  <tbody>
    <tr><td>Phenotype highly specific for gene</td><td>2</td><td>1</td></tr>
    <tr><td>Phenotype consistent with gene but not highly specific</td><td>1</td><td>0.5</td></tr>
    <tr><td>Phenotype consistent with gene but not highly specific and high genetic heterogeneity*</td><td>0.5</td><td>0.25</td></tr>
    <tr><td>Phenotype not consistent with gene</td><td>0</td><td>0</td></tr>
  </tbody>
</table>

`*Maximum allowable value of 1 may contribute to overall score`

**Table 2. Recommendation for determining the appropriate ACMG/AMP evidence strength level for de novo occurrence(s)**

| Evidence strength | Total points |
|---|---:|
| Supporting (`PS2_Supporting or PM6_Supporting`) | 0.5 |
| Moderate (`PS2_Moderate or PM6`) | 1 |
| Strong (`PS2 or PM6_Strong`) | 2 |
| Very Strong (`PS2_VeryStrong or PM6_VeryStrong`) | 4 |

> **Source conflict:** The core specification says PM6 is Not Applicable and directs de novo cases to PS2, while this distributed scoring attachment retains PM6 labels at all four strengths. Neither statement has been discarded.

### PS3 — Functional studies

**Original ACMG summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

| Strength | VCEP specification |
|---|---|
| Strong | In a transgenic animal model, must demonstrate minimal to no function. |
| Supporting | Functional assays measuring quantity of GP1ba expression on the cell surface by flow-cytometry analysis of GPIb and GPIX when there is absent or near absent expression, `>75% reduction`. |

#### Source-derived assay summary

The following summary is transcribed from the distributed `GPIBA` sheet rather than a separately distributed prose table. All six columns are marked approved (`y`) and `PS3_supporting`; the normal threshold is `Equivalent to WT`, the abnormal threshold is `Sigificantly decreased from WT` [sic], and the proposed application is `when there is absent or near absent expression, >75% reduction`.

| PMID | First-author/source note | Flow-cytometry readout |
|---|---|---|
| 7579348 | `ChaoyangLi` [sic] | Quantity of GP1ba expression on the cell surface. |
| 9326229 | Dermot Kenny; also PMIDs 9639514 and 10887115 from the same group | Quantity of GP1ba expression on the cell surface. |
| 11054083 | Vahid Afshar-Kharghan; also PMID 9326230 from the same group | Quantity of GP1ba expression on the cell surface. |
| 10928479 | Philippe Ulsemer | Quantity of GP1ba expression on the cell surface. |
| 11776304 | Consuelo González-Manchón | Quantity of GP1ba expression on the cell surface. |
| 17083647 | N. Rosenberg | Analysis of GPIb and GPIX. |

> **Workbook provenance and source issue:** The workbook contains visible `GPIX` (93 populated cells), visible `GPIBA` (108), visible `GPIBB` (77), and hidden `Mufti` (27), for 305 populated cells total. `GPIX` and `GPIBB` are sibling-gene assay sheets. Hidden `Mufti` contains VWF-related text and a DOI/link not aligned with a GP1BA assay. These non-GPIBA records are disclosed but not converted into GP1BA criteria.

### PS4 — Prevalence in affected individuals

Individuals heterozygous for Bernard-Soulier syndrome variants are considered informative due to measurable quantitative abnormalities relevant to the disease (PMID 25370924).

All caveats apply:

1. The variant must meet PM2_supporting.
2. There must be an assumed unrelated biallelic BSS patient meeting PP4 before heterozygotes are considered.
3. A single family proband may be included in PM3 (biallelic) or PS4 (monoallelic), not both.
4. Additional relatives are excluded from PS4 but may be considered for PP1.

| Evidence | Points |
|---|---:|
| Significantly reduced surface expression of GP1b measured by flow cytometry | 0.5pt |
| Giant platelets (`MPD >7 microns`) or macrothrombocytopenia (`MPV >12 fL` and platelet count `<150x10^9/L`) | 0.25pt |

| Strength | Score |
|---|---:|
| Moderate | `2+ points` |
| Supporting | `1-1.75` |

### PM1 — Mutational hot spot/critical domain

**Moderate:** Disulfide bonds in GPIb are critical to interaction with GPIX (PMID 12036872) and receptor binding to von Willebrand factor (PMID 18647229). Apply when cysteine residue 20, 33, 225, 227, 264, 280, 526, or 527 is altered; the source reports no known benign variants at these residues.

### PM2 — Absent from controls

**Supporting:** gnomAD MAF of **less than or equal to 0.0001114**.

### PM3 — In trans with pathogenic variant

An in-trans VUS classified under the GP1BA specifications must meet PM2_supporting. An in-trans pathogenic/likely pathogenic variant classified under these specifications need not meet PM2_supporting but cannot meet BS1 or BA1. Both variants must be classified under these specifications.

**Table 1. Points awarded per in trans proband**

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

¹ In trans variants classified as a variants [sic] of uncertain significance, as per the Bernard Soulier syndrome (BSS) rule specifications, must meet PM2_supporting to be scored. Conversely, in trans variants that meet a pathogenic or likely pathogenic classification using the BSS rule specifications do not have to meet PM2_supporting criteria; however, they cannot meet BS1 or BA1 criteria; P – Pathogenic; LP – Likely pathogenic

**Table 2. Recommendation for determining the appropriate evidence strength level for PM3**

| Evidence strength | Total points |
|---|---:|
| PM3_Supporting | 0.5 |
| PM3 | 1.0 |
| PM3_Strong | 2.0 |
| PM3_VeryStrong | 4.0 |

### PM4 — Protein length changes

**Moderate:** Use with no specification.

### PM5 — Novel missense change at the same residue

| Strength | VCEP specification |
|---|---|
| Moderate | Use as originally specified, but the comparison variant must reach a pathogenic classification “using the these rule specifications” [sic]. |
| Supporting | Use as originally specified, but the comparison variant must reach a likely pathogenic classification “using the these rule specifications” [sic]. |

### PM6 — Assumed de novo

**Not Applicable.** Use PS2 for de novo cases in lieu of this rule code.

See the PS2 section for the unresolved conflict with PM6 labels in the distributed scoring attachment.

### PP1 — Co-segregation

A biallelic BSS patient meeting PP4 is required before segregation points are awarded. Heterozygotes used for PP1 cannot be applied to PS4.

| Evidence | Points |
|---|---:|
| Proband (should be accounted for in PP4 or PS4) | 0pt |
| BSS-affected relative with the same biallelic variant(s) as the proband | 1pt |
| Heterozygous relative with significantly reduced GP1b surface expression by flow cytometry | 0.5pt |
| Heterozygous relative with giant platelets (`MPD >7 microns`) or macrothrombocytopenia (`MPV >12 fL` and platelet count `<150x10^9/L`) | 0.25pt |

Only one parent of a homozygous proband in a consanguineous pedigree may be scored.

| Strength | Total segregation score |
|---|---:|
| Strong | `3+ points` |
| Moderate | `2-2.75 points` |
| Supporting | `1-1.75 points` |

### PP2 — Missense in constrained gene

**Not Applicable.** This rule does not apply because BSS is rare and GP1BA is not constrained for missense variation in gnomAD.

### PP3 — Computational evidence

| Strength | VCEP specification |
|---|---|
| Moderate | REVEL `≥0.773` (PMID 36413997). |
| Supporting | REVEL `≥0.644 (to <0.773)` (PMID 36413997), OR suggested splicing effect using SpliceAI **greater than or equal to 0.5**. |

### PP4 — Phenotype specificity

| Strength | VCEP specification |
|---|---|
| Moderate | Must meet both: (1) absent ristocetin aggregation with aggregation present for all other agonists, OR flow cytometry/Western blot **less than 10%** expression of GPIba; and (2) full sequencing of GP1BA, GP1BB, and GP9 plus deletion/duplication analysis. |
| Supporting | Absent ristocetin aggregation with aggregation present for all other agonists, OR flow cytometry/Western blot **less than 10%** expression of GPIba. |

### PP5 — Reputable source

**Not Applicable.** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID 29543229).

## Benign criteria

### BA1 — Allele frequency

**Stand Alone:** gnomAD MAF of **greater than or equal to 0.001 (or 0.1%)**.

### BS1 — Frequency greater than expected

**Strong:** gnomAD MAF **greater than or equal to 0.0005 but less than 0.001**.

### BS2 — Unaffected homozygote

**Strong:** One or more unaffected homozygotes proven with aggregometry OR flow cytometry AND normal platelet count AND normal platelet size.

### BS3 — Functional studies showing no damaging effect

| Strength | VCEP specification |
|---|---|
| Strong | Normal aggregometry in a transgenic mouse model. |
| Supporting | In a heterologous cell line, BOTH normal expression and normal protein function compared with wildtype. |

### BS4 — Lack of segregation

**Strong:** Variant not tracking in an affected family member.

### BP1 — Missense in a truncating-variant gene

**Not Applicable.** Truncating variants do not predominate and missense variants are a known cause of disease.

### BP2 — Observed in cis

**Supporting:** For recessive variants, use only when observed in cis with a pathogenic variant.

### BP3 — In-frame variant in repetitive region

**Supporting:** Use with no specification.

### BP4 — Computational evidence suggesting no impact

Determine the REVEL and Splice AI cutoff before applying this code; do not use if PP3 is met.

**Supporting:** For a missense variant, REVEL **less than or equal to 0.290** AND SpliceAI score zero; OR, for a synonymous or intronic variant, SpliceAI score zero.

### BP5 — Alternate molecular basis

**Not Applicable.** Do not use because an individual can be a carrier of an unrelated pathogenic variant for a recessive disorder.

### BP6 — Reputable benign source

**Not Applicable.** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID 29543229).

### BP7 — Synonymous/intronic evidence

**Supporting:** Use SpliceAI to rule out a possible splicing defect (`score = 0.2 or less`) AND reference PhyloP (`score = 1.5 or less`) to assess conservation. May be used for intronic variants and in combination with BP4.

## Rules for combining criteria

### Richards et al. combinations printed in the core

#### Pathogenic

- 1 Very Strong AND ≥1 Strong
- 1 Very Strong AND ≥2 Moderate
- 1 Very Strong AND 1 Moderate AND 1 Supporting
- 1 Very Strong AND ≥2 Supporting
- ≥2 Strong
- 1 Strong AND ≥3 Moderate
- 1 Strong AND 2 Moderate AND ≥2 Supporting
- 1 Strong AND 1 Moderate AND ≥4 Supporting

#### Likely Pathogenic

- 1 Very Strong AND 1 Moderate
- 1 Strong AND 1 Moderate
- 1 Strong AND ≥2 Supporting
- ≥3 Moderate
- 2 Moderate AND ≥2 Supporting
- 1 Moderate AND ≥4 Supporting
- 1 Strong AND 2 Moderate

#### Benign

- ≥2 Strong
- 1 Stand Alone

#### Likely Benign

- 1 Strong AND 1 Supporting
- ≥2 Supporting

### Distributed conflicting-evidence rules

If pathogenic and benign evidence coexist, do not automatically classify the variant as VUS. Apply the Tavtigian et al. 2020 point system (PMID 32720330).

| Strength | Pathogenic points | Benign points |
|---|---:|---:|
| Indeterminate | 0 | 0^a |
| Supporting | 1 | -1 |
| Moderate | 2 | -2^b |
| Strong | 4 | -4 |
| Very strong | 8 | -8^b |

| Classification | Total points |
|---|---:|
| Pathogenic | `≥10` |
| Likely Pathogenic | `6 to 9^a` |
| Uncertain | `0 to 5` |
| Likely Benign | `-1 to -6^a` |
| Benign | `≤ -7` |

> **Source issue:** Superscripts `a` and `b` are printed in the embedded table images, but the distributed DOCX contains no substantive definitions for them.

## Source-derived editorial summaries

The following concise summaries reorganize values already printed in the distributed sources; they are not separately distributed VCEP tables.

### Population-frequency values

| Criterion | Source wording | Strength |
|---|---|---|
| BA1 | greater than or equal to 0.001 (or 0.1%) | Stand Alone |
| BS1 | greater than or equal to 0.0005 but less than 0.001 | Strong |
| PM2 | less than or equal to 0.0001114 | Supporting |

### Computational-predictor values

| Criterion | Source wording |
|---|---|
| PP3_Moderate | REVEL `≥0.773` |
| PP3_Supporting | REVEL `≥0.644 (to <0.773)`, OR SpliceAI greater than or equal to 0.5 |
| BP4 | REVEL less than or equal to 0.290 AND SpliceAI zero for missense; SpliceAI zero for synonymous/intronic |
| BP7 | SpliceAI `score = 0.2 or less` AND PhyloP `score = 1.5 or less` |

### Critical residues/domain

- PM1 cysteines: 20, 33, 225, 227, 264, 280, 526, 527.
- PVS1 transmembrane domain: amino acids 532-553.

## References supplied by the sources

- Savoia A, Pastore A et al. *Clinical and genetic aspects of Bernard-Soulier syndrome: searching for genotype/phenotype correlations.* Haematologica. 2011;96(3):417-423. DOI 10.3324/haematol.2010.032631. PMID 21173099.
- Additional PMIDs explicitly cited in the core or attachments: 12036872, 18647229, 25370924, 29543229, 32720330, and 36413997.
- GPIBA assay-sheet PMIDs: 7579348, 9326229, 9639514, 10887115, 11054083, 9326230, 10928479, 11776304, and 17083647.

## Document corrections history

| Date | Correction |
|---|---|
| 2026-08-10 | Reconciled this transcription against all six distributed artifacts: `ClinGen_ACMG_Specifications_GP1BA_v1.1.pdf`, `Guidance for Combining Pathogenic and Benign Rule Codes.docx`, `Instructions for PM3 code use.docx`, `Instructions for PS2_PM6 code use.docx`, `PS3_Supporting Functional Assays.xlsx`, and `PVS1 flowchart for GP1BA gene.pptx`. Restored the complete PVS1 topology and correct initiation-codon outcomes; restored the exact PS2/PM6 and PM3 table titles, two-level header framing, row labels, cells, and PM3 footnote; replaced normalized comparators with source forms; restored printed typos and undefined superscripts; replaced the rewritten conflicting-evidence point table with the distributed table; removed unsupported assay-control requirements and unsupported homozygous PM3 categories; labeled source-derived editorial summaries; documented workbook sheet visibility, exact populated-cell counts, and the hidden `Mufti` disposition; and documented unresolved package conflicts without resolving them. |

## Version history

| Version | Date | Notes |
|---|---|---|
| 1.1.0 | 9/29/2025 | The BP4 rule was corrected to include less than “or equal to”. |
| 1.0.0 | Initial release | Original specifications. |
