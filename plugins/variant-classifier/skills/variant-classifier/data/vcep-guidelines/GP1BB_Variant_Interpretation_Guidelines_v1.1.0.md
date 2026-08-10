# ClinGen Platelet Disorders VCEP Variant Interpretation Guidelines for GP1BB

**Version:** 1.1.0
**Released:** 9/29/2025
**Affiliation:** Platelet Disorders VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines
**DOI:** 10.5281/zenodo.21433998

---

## Gene Information

| Attribute | Value |
|---|---|
| **Gene** | GP1BB (HGNC:4440) |
| **HGNC Name** | glycoprotein Ib platelet subunit beta |
| **Transcript** | NM_000407.5 |
| **Disease** | Bernard-Soulier syndrome (MONDO:0009276) |
| **Inheritance** | Autosomal recessive inheritance |

## Source-integrity notices

- `Instructions for PS2_PM6 code use.docx` assigns PS2 and PM6 labels at all four strengths. The core specification makes PM6 not applicable and says to use PS2 instead. It also gives PS2 only at Very Strong, Strong, and Moderate strengths, while the attachment includes PS2_Supporting. This conflict is unresolved; no precedence is inferred.
- The PVS1 slide uses markers `(a)` through `(d)` and red X symbols but supplies no definitions or legend, including in the notes. The affected branches are transcribed below but remain unresolved.
- The combining-rules images use superscripts `a` and `b`, but the DOCX supplies no footnote definitions. They are preserved without inferred definitions.
- The hidden `Mufti` worksheet contains sparse VWF material and no approved-assay designation. It is not used as GP1BB functional evidence.

---

## Pathogenic Criteria

### PVS1 — Null Variant

Use the GP1BB-modified decision tree for Very Strong, Strong, Moderate, and Supporting evidence.

#### Nonsense or frameshift

- Predicted to undergo NMD `(b)`:
  - the distributed slide states: `GP1BB coding sequence begins in the last 50 nucleotides of the penultimate exon (1 of 2) which is not considered subject to NMD`;
  - exon present in biologically relevant transcript(s) → **PVS1** (red X shown at/near this outcome);
  - exon absent from biologically relevant transcript(s) → **N/A** (red X shown at/near this outcome).
- Not predicted to undergo NMD `(b)`:
  - critical region `(c)` / transmembrane region amino acids 148–173 → **PVS1_Strong**;
  - role unknown and exon frequent/absent from biologically relevant transcript(s) → **N/A**;
  - role unknown and exon not frequent/present → truncation removes `>10%` (before p.186) → **PVS1_Strong**;
  - role unknown and exon not frequent/present → truncation removes `<10%` (at/after p.186) → **PVS1_Moderate**.

Terminal-most PTV annotation: `NM_000407.5:c.448del (Ala150Argfs*43)`, ClinVar 627075 (`Likely Pathogenic, 1 star`).

#### GT--AG 1,2 splice sites `(a)`

- Disrupts reading frame and predicted to undergo NMD `(b)`:
  - exon present → **PVS1** (red X shown at/near this outcome);
  - exon absent → **N/A** (red X shown at/near this outcome).
- Disrupts reading frame and is not predicted to undergo NMD `(b)`:
  - critical region `(c)` / transmembrane region → **PVS1_Strong**;
  - role unknown and exon frequent/absent → **N/A**;
  - role unknown and exon not frequent/present → `>10%` (`truncation before p.186 or deletion of >20 amino acids`) → **PVS1_Strong**;
  - role unknown and exon not frequent/present → `<10%` (`truncation at/after p.186 or deletion of <21 amino acids`) → **PVS1_Moderate**.
- Preserves reading frame:
  - critical region `(c)` / transmembrane region → **PVS1_Strong**;
  - role unknown → use the same exon-frequency and `>10%` / `<10%` split above.

#### Deletion

- Full-gene deletion → **PVS1** `(d)`.
- Disrupts reading frame and predicted to undergo NMD `(b)`:
  - exon present → **PVS1** (red X shown at/near this outcome);
  - exon absent → **N/A** (red X shown at/near this outcome).
- Disrupts reading frame and is not predicted to undergo NMD `(b)`:
  - critical region `(c)` / transmembrane region → **PVS1_Strong**;
  - role unknown and exon frequent/absent → **N/A**;
  - role unknown and exon not frequent/present → `>10%` or deletion of `>20` amino acids → **PVS1_Strong**;
  - role unknown and exon not frequent/present → `<10%` or deletion of `<21` amino acids → **PVS1_Moderate**.
- Preserves reading frame: critical region → **PVS1_Strong**; otherwise use the same role-unknown size split.

#### Duplication(≥1 exon in size and must be completely contained within gene)

- Proven in tandem:
  - reading frame disrupted and NMD predicted → **PVS1**;
  - no or unknown impact on reading frame → **N/A**.
- Presumed in tandem:
  - reading frame presumed disrupted and NMD predicted → **PVS1_Strong**;
  - no or unknown impact on reading frame → **N/A**.
- Proven not in tandem → **N/A**.

#### Initiation codon

- Different functional transcript uses alternative start codon → **N/A**.
- No known alternative start codon in other transcripts:
  - `≥1 pathogenic variant(s) upstream of closest potential in-frame start codon` → **PVS1**;
  - `No pathogenic variant(s) upstream of closest potential in-frame start codon` → **PVS1_Supp** (red X shown at/near this outcome).

Source annotation: `GP1BB does not have another potential in-frame start codon`.

The slide's `(a)`–`(d)` markers and red X symbols have no supplied definitions. Raw OOXML also leaves some connector endpoints unbound, so the rendered arrow routing controls this transcription; no missing meaning is inferred.

### PS1 — Same amino-acid change

| Strength | Criteria |
|---|---|
| **Strong** | Use as originally specified, but the comparison variant must reach a pathogenic classification using `the these rule specifications` [sic] in order to apply code. |
| **Moderate** | Use as originally specified, but the comparison variant must reach a likely pathogenic classification using `the these rule specifications` [sic] in order to apply code. |

### PS2 — De novo

Only applicable when the proband has a known pathogenic or likely pathogenic variant according to the BSS rule specifications along with the de novo variant. Use the phenotype consistency `Phenotype highly specific for gene` only when all three genes (`GP1BA`, `GP1BB` and `GP9`) have been sequenced. When only one or two have been sequenced, use `Phenotype consistent with gene but not highly specific`.

#### Table 1. Points awarded per de novo occurrence

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

#### Table 2. Recommendation for determining the appropriate ACMG/AMP evidence strength level for de novo occurrence(s)

The attachment prints bare point values:

| Strength | Criterion label(s) | Points |
|---|---|---:|
| Supporting | PS2_Supporting or PM6_Supporting | 0.5 |
| Moderate | PS2_Moderate or PM6 | 1 |
| Strong | PS2 or PM6_Strong | 2 |
| Very Strong | PS2_VeryStrong or PM6_VeryStrong | 4 |

The core specification provides PS2 only at total 1 (Moderate), 2 (Strong), and 4 (Very Strong), makes PM6 not applicable, and says to use PS2 for de novo cases. The attachment's Supporting and PM6 labels are retained above to disclose the unresolved source conflict. No precedence is inferred.

### PS3 — Functional studies

| Strength | Criteria |
|---|---|
| **Strong** | In a transgenic animal model, must demonstrate minimal to no function. |
| **Supporting** | Functional assays measuring quantity of GP1ba and/or GPIX expression on cell surface measured by flow cytometry. See the approved GP1BB assays below. |

#### Approved GP1BB assays in `PS3_Supporting Functional Assays.xlsx`

| PMID | Year | First author | Source assay summary |
|---:|---:|---|---|
| 10216092 | 1999 | Dermot Kenny; also PMID 12529755 from the same research group | Transient transfection of mutant GPIbb with wild-type GPIba and GPIX into 293T cells; quantity of GP1ba expression on the cell surface by flow cytometry. |
| 10928480 | 2000 | Shinji Kunishima; also PMIDs 12447957 and 16978236 from the same research group | 293T cells transiently cotransfected with wild-type or mutant GPIb with wild-type GPIb and GPIX; quantity of GP1ba and GPIX expression on the cell surface by flow cytometry. |
| 12958615 | 2003 | Consuelo González-Manchón | CHO cells transiently cotransfected with normal GPIba and GPIX cDNAs and normal or mutant GPIbβ cDNAs; quantity of GP1ba and GPIX expression on the cell surface by flow cytometry. |
| 16409472 | 2006 | C. STRASSEL; also PMID 12693941 from the same research group | CHO cells expressing the GPIbaand GPIX subunits, further transfected with wild-type (bWT) ormutant (bmut) GPIbb; quantity of GP1b-IX expression on the cell surface by flow cytometry. |

Each is marked `y`, proposes `PS3_supporting`, and uses the exact threshold `when there is absent or near absent expression, >75% reduction`. The exact abnormal-readout wording is `Sigificantly decreased from WT` [sic]. Source gene/protein typography and defects are preserved where quoted.

The workbook also contains approved GPIX and GPIBA assays for the related panel genes. Its hidden `Mufti` sheet contains no approved assay or proposed strength and includes VWF material; it is not promoted into GP1BB criteria.

### PS4 — Prevalence in affected

Before scoring a heterozygote: the variant must meet PM2_supporting; there must be an assumed unrelated biallelic BSS proband meeting PP4; a family proband is counted in PM3 or PS4 but not both; and additional family members are considered under PP1, not PS4.

| Evidence from a heterozygous individual | Points |
|---|---:|
| Significantly reduced surface expression of GP1b measured by flow cytometry | 0.5 |
| Giant platelets (MPD `>7` microns) **or** macrothrombocytopenia (MPV `>12` fL **and** platelet count `<150x10^9/L`) | 0.25 |

| Strength | Total |
|---|---|
| **Moderate** | `2+ points` |
| **Supporting** | `1-1.75` |

### PM1 — Critical cysteine residues

Apply at Moderate strength when cysteine residues 93, 95, 118, 141, or 147 are altered. The source states that these disulfide bonds are critical for interaction with GPIX (PMID 12036872) and receptor binding to von Willebrand factor (PMID 18647229), and that no known benign variants occur at these residues.

### PM2 — Population frequency

**Supporting:** gnomAD MAF less than or equal to `0.00006517`.

### PM3 — In-trans evidence

An in-trans VUS under the BSS specifications must meet PM2_supporting. An in-trans pathogenic or likely pathogenic variant need not meet PM2_supporting, but cannot meet BS1 or BA1.

#### Table 1. Points awarded per in trans proband

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

#### Table 2. Recommendation for determining the appropriate evidence strength level for PM3

The attachment prints bare point values:

| PM3_Supporting | PM3 | PM3_Strong | PM3_VeryStrong |
|---:|---:|---:|---:|
| 0.5 | 1.0 | 2.0 | 4.0 |

The core prints the source-supplied link at each applicable strength:

| Strength | Core `22q11.2` exception |
|---|---|
| **Very Strong** | A `22q11.2` deletion in trans (`https://www.ncbi.nlm.nih.gov/books/NBK1523/`) may be scored automatically as 1 point when confirmed to include `GP1BB`. |
| **Strong** | A `22q11.2` deletion in trans (`https://www.ncbi.nlm.nih.gov/books/NBK1523/`) may be scored automatically as 1 point when confirmed to include `GP1BB`. |
| **Moderate** | A `22q11.2` deletion in trans (`https://www.ncbi.nlm.nih.gov/books/NBK1523/`) may be scored automatically as 1 point when confirmed to include `GP1BB`. |
| **Supporting** | The core does not state this exception. |

### PM4 — Protein-length changes

**Moderate:** use with no specification.

### PM5 — Novel missense at the same residue

| Strength | Criteria |
|---|---|
| **Moderate** | Comparison variant must reach pathogenic using these rule specifications. |
| **Supporting** | Comparison variant must reach likely pathogenic using these rule specifications. |

### PM6 — Assumed de novo

**Not Applicable.** `Use PS2 for de novo cases in lieu of this rule code.` See the unresolved attachment conflict under PS2.

### PP1 — Co-segregation

There must be a biallelic BSS proband meeting PP4 before points are awarded. Heterozygotes used for PP1 cannot also be used for PS4.

| Evidence | Points |
|---|---:|
| Proband | 0 |
| BSS-affected relative with the same biallelic variants as the proband | 1 |
| Heterozygous relative with significantly reduced surface GP1b by flow cytometry | 0.5 |
| Heterozygous relative with giant platelets (MPD `>7` microns) **or** macrothrombocytopenia (MPV `>12` fL **and** platelets `<150x10^9/L`) | 0.25 |

Only one parent of a homozygous proband in a consanguineous pedigree is scored.

| Strength | Total segregation score |
|---|---|
| **Supporting** | `1-1.75 points` |
| **Moderate** | `2-2.75 points` |
| **Strong** | `3+ points` |

### PP2 — Missense in constrained gene

**Not Applicable.** The source says BSS is rare and GP1BB is not constrained for missense variation in gnomAD.

### PP3 — Computational evidence

| Strength | Criteria |
|---|---|
| **Moderate** | REVEL `≥0.773`. |
| **Supporting** | REVEL `≥0.644 (to <0.773)` **or** SpliceAI greater than or equal to `0.5`. |

PP3 may be used only once in an evaluation.

### PP4 — Phenotype specificity

| Strength | Criteria |
|---|---|
| **Moderate** | Both: (1) absent ristocetin aggregation with all other agonists present **or** flow cytometry/Western blot less than `10%` GPIba expression; **and** (2) full sequencing of `GP1BA`, `GP1BB`, and `GP9` plus deletion/duplication analysis. |
| **Supporting** | Absent ristocetin aggregation with all other agonists present **or** flow cytometry/Western blot less than `10%` GPIba expression. |

### PP5 — Reputable source

**Not Applicable.** The ClinGen Sequence Variant Interpretation VCEP Review Committee recommends not using this criterion (PMID 29543229).

---

## Benign Criteria

### BA1 — Population frequency

**Stand Alone:** gnomAD MAF greater than or equal to `0.001` (or 0.1%).

### BS1 — Population frequency

**Strong:** gnomAD MAF greater than or equal to `0.0005` but less than `0.001`.

### BS2 — Unaffected homozygotes

**Strong:** use with one or more homozygotes who are unaffected, proven with `aggregometry OR flow cytometry AND normal platelet count AND normal platelet size`. The source's operator scope is retained exactly.

### BS3 — Functional studies showing no damaging effect

| Strength | Criteria |
|---|---|
| **Strong** | Normal aggregometry in a transgenic mouse model. |
| **Supporting** | In a heterologous cell line, both normal expression and normal protein function compared with wildtype. |

### BS4 — Lack of segregation

**Strong:** variant not tracking in an affected family member.

### BP1–BP7

| Criterion | Status | Specification |
|---|---|---|
| **BP1** | Not Applicable | Truncating variants do not predominate and missense variants are a known cause of disease. |
| **BP2** | Supporting | Use as written for recessive variants; the variant must be observed in cis with a pathogenic variant. |
| **BP3** | Supporting | Use with no specification. |
| **BP4** | Supporting | Missense: REVEL less than or equal to `0.290` **and** SpliceAI `0`. Synonymous or intronic: SpliceAI `0`. Determine the REVEL and SpliceAI cutoff before applying; do not use if PP3 applies. |
| **BP5** | Not Applicable | An individual can be a carrier of an unrelated pathogenic variant for a recessive disorder. |
| **BP6** | Not Applicable | The ClinGen Sequence Variant Interpretation VCEP Review Committee recommends not using this criterion (PMID 29543229). |
| **BP7** | Supporting | SpliceAI `score = 0.2 or less` and PhyloP `score = 1.5 or less`. Can be used for intronic variants and in combination with BP4. |

---

## Rules for Combining Criteria

### Richards et al. qualitative combinations

| Classification | Criteria combinations |
|---|---|
| **Pathogenic** | 1 Very Strong AND ≥1 Strong; 1 Very Strong AND ≥2 Moderate; 1 Very Strong AND 1 Moderate AND 1 Supporting; 1 Very Strong AND ≥2 Supporting; ≥2 Strong; 1 Strong AND ≥3 Moderate; 1 Strong AND 2 Moderate AND ≥2 Supporting; 1 Strong AND 1 Moderate AND ≥4 Supporting |
| **Likely Pathogenic** | 1 Very Strong AND 1 Moderate; 1 Strong AND 1 Moderate; 1 Strong AND ≥2 Supporting; ≥3 Moderate; 2 Moderate AND ≥2 Supporting; 1 Moderate AND ≥4 Supporting; 1 Strong AND 2 Moderate |
| **Benign** | ≥2 Strong; 1 Stand Alone |
| **Likely Benign** | 1 Strong AND 1 Supporting; ≥2 Supporting |

### GP1BA, GP1BB, GP9 Rules for Combining Codes with Conflicting Criteria

When both benign and pathogenic criteria apply, the attachment says not to assign an automatic VUS. It recommends the Tavtigian et al. 2020 point system (PMID 32720330).

#### TABLE 2 Point values for ACMG/AMP strength of evidence categories

| Evidence strength | Pathogenic point scale | Benign point scale |
|---|---:|---:|
| Indeterminate | 0 | 0ᵃ |
| Supporting | 1 | -1 |
| Moderate | 2 | -2ᵇ |
| Strong | 4 | -4 |
| Very strong | 8 | -8ᵇ |

#### TABLE 3 Point-based variant classification categories

| Category | Point ranges |
|---|---:|
| Pathogenic | `≥10` |
| Likely Pathogenic | `6 to 9ᵃ` |
| Uncertain | `0 to 5` |
| Likely Benign | `-1 to -6ᵃ` |
| Benign | `≤ -7` |

The source does not supply definitions for superscripts `a` or `b`; none are inferred here.

---

## References

The core specification supplies one formal reference:

1. Savoia A, Pastore A, et al. Clinical and genetic aspects of Bernard-Soulier syndrome: searching for genotype/phenotype correlations. *Haematologica*. 2011;96(3):417–423. PMID 21173099. DOI 10.3324/haematol.2010.032631.

Other PMIDs above are identifiers printed in the criterion text or supplements; descriptions have not been expanded beyond the distributed package.

---

## Version History

| Version | Date | Notes |
|---|---|---|
| 1.1.0 | 9/29/2025 | `The BP4 rule was corrected to include less than “or equal to”.` |
| 1.0.0 | Initial | Initial release. |

### Document corrections — 2026-08-10

Source-first remediation verified against all six distributed files: `ClinGen_ACMG_Specifications_GP1BB_v1.1.pdf`, `Guidance for Combining Pathogenic and Benign Rule Codes.docx`, `Instructions for PM3 code use.docx`, `Instructions for PS2_PM6 code use.docx`, `PS3_Supporting Functional Assays.xlsx`, and `PVS1 flowchart for GP1BB gene.pptx`.

- Replaced the incomplete, partly inferred PVS1 prose with the rendered GP1BB slide topology, retaining the distributed GP1BB NMD sentence, literal `Duplication(≥1 exon in size and must be completely contained within gene)`, `≥1 pathogenic variant(s) upstream of closest potential in-frame start codon`, `PVS1_Supp`, exact `GT--AG`, `>10%`, `<10%`, `>20`, and `<21` comparators, and undefined markers/red X symbols. Removed two invented critical-region routes from the predicted-NMD branches.
- Restored source typos and forms that had been normalized, including `the these rule specifications`, `Sigificantly decreased from WT`, and the PM3 footnote's `classified as a variants`.
- Replaced the source-contradicting PM3 per-proband expansion with the exact two embedded tables and restored the source-supplied `https://www.ncbi.nlm.nih.gov/books/NBK1523/` link at each core strength that states the `22q11.2` exception.
- Restored the de novo attachment's exact titles, two-level `Points per Proband` framing, bare point cells, labels, and footnote while explicitly preserving its conflict with core PM6 and PS2 strength rules.
- Restored the full conflicting-criteria point tables, including Indeterminate, benign Moderate/Very strong values, exact point ranges, and unresolved superscripts.
- Removed unsupported control requirements, generic/inferred summaries, and unsourced associated-gene appendix fields. Restored same-research-group PMID metadata for the three GPIBB assay records that supply it. No plausible local-only gene-specific content remains, so no package-warning banner is required.

---

*This remediation reflects the distributed package exactly where possible and leaves source contradictions or omissions unresolved. No web research was used.*
