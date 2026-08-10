# ClinGen Epilepsy Sodium Channel Expert Panel Variant Interpretation Guidelines for SCN1B

**Version:** 2.0.0

**Released:** 1/7/2025

**Affiliation:** Epilepsy Sodium Channel VCEP

**DOI:** 10.5281/zenodo.21433959

**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

**Release Notes:** Release contains updates to transcript information and exon numbering.

> **Operative combining framework:** The core specification directs users to disregard its printed “Rules for Combining Criteria” and use the distributed `Combining Rules.pdf` points-based framework instead. The core literally calls the attachment “Combing Rules”; that is a source typo.

> **Unresolved transcript contradiction:** The core PDF and its keywords name `NM_001037.4`, while `PVS1 Decision Tree.pptx` and the SCN1B sheet of `PVS1 exon numbering.xlsx` name `NM_001037.5`. The release note says transcript information was updated but does not reconcile the versions. Preserve both readings.

---

## Gene information

| Attribute | Value |
|---|---|
| Gene | SCN1B (HGNC:10586) |
| HGNC name | sodium voltage-gated channel beta subunit 1 |
| Core-PDF transcript | NM_001037.4 |
| PVS1 slide/workbook transcript | NM_001037.5 |
| Disease | Generalized epilepsy with febrile seizures plus (MONDO:0018214), autosomal dominant |
| Disease | Developmental and epileptic encephalopathy (MONDO:0100062), autosomal recessive |

---

## Pathogenic criteria

### PVS1 - Null variant

**Original ACMG summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single- or multi-exon deletion) in a gene where loss of function is a known disease mechanism.

**Original caveats retained by the source:** use caution at the extreme 3' end, with predicted exon skipping that leaves the remainder of the protein intact, and in the presence of multiple transcripts.

**SCN1B parameters from the core and distributed decision tree:**

- Most terminal codon expected to undergo NMD: p.Thr204.
- For splice sites, do not combine PVS1 with PP3.
- A full-gene deletion warrants a pathogenic classification.
- The slide's biologically relevant transcript is `NM_001037.5` (MANE Select).
- A truncated/altered region is “critical to protein function” when non-truncating variants classified Pathogenic under these criteria are present.
- All exons are out of frame.

The last three definitions were verified in the PPTX speaker notes, not inferred from the visible slide.

> **Unresolved full-gene-deletion conflict:** The core says a full-gene deletion warrants a Pathogenic classification; the decision tree assigns PVS1; and `Combining Rules.pdf` assigns Pathogenic Very Strong 8 points while its 6-9-point band is Likely Pathogenic. Report all three readings without reconciling them.

#### Unresolved size-branch inconsistency

> The rendered source slide visibly places `Variant removes >10% of protein` and `>=200 aa` in the same Strong branch box, and `<10% of protein` and `<200 aa` in the same Moderate branch box. It supplies no AND/OR word between each pair. For the short SCN1B protein this is internally problematic, but it must not be repaired or reinterpreted. The percent comparisons are strict: exactly 10% is assigned to neither branch. The absolute comparisons are inclusive `>=200 aa` versus strict `<200 aa`.

#### Decision-tree topology

The flowchart uses the following common late-truncation/frame-preserving decision block:

| Condition | Next condition | Source outcome |
|---|---|---|
| Truncated/altered region is critical to protein function | — | PVS1_Strong |
| Role of region in protein function is unknown | LoF variants in the exon are frequent in the general population and/or the exon is absent from biologically relevant transcript(s) | N/A |
| Role unknown | LoF variants are not frequent and the exon is present -> box containing both `>10% of protein` and `>=200 aa` | PVS1_Strong |
| Role unknown | LoF variants are not frequent and the exon is present -> box containing both `<10% of protein` and `<200 aa` | PVS1_Moderate |

Entry paths into that block:

| Variant class | Entry condition | Source outcome or next block |
|---|---|---|
| Nonsense or frameshift | Predicted NMD; stop codon 5' of p.Thr204; exon present in biologically relevant transcript `NM_001037.5` | PVS1 |
| Nonsense or frameshift | Not predicted NMD; stop codon 3' of p.Thr204 | Common block above |
| `GT--AG` 1,2 splice site | Exon skipping or cryptic splice site disrupts reading frame; predicted NMD; stop codon 5' of p.Thr204; exon present in `NM_001037.5` | PVS1 |
| `GT--AG` 1,2 splice site | Disrupts reading frame; not predicted NMD; stop codon 3' of p.Thr204 | Common block above |
| `GT--AG` 1,2 splice site | Preserves reading frame | Common block above |
| Single-to-multi-exon deletion | Disrupts reading frame; predicted NMD; stop codon 5' of p.Thr204; exon present in `NM_001037.5` | PVS1 |
| Single-to-multi-exon deletion | Disrupts reading frame; not predicted NMD; stop codon 3' of p.Thr204 | Common block above |
| Single-to-multi-exon deletion | Preserves reading frame | Common block above |
| Full-gene deletion | — | PVS1 |

The slide literally labels the splice class `GT--AG 1,2 splice sites (if applied, PP3 not to be used in combination)`.

Duplication paths (`>=1` exon and completely contained within the gene):

| Tandem status | Reading-frame/NMD condition | Source outcome |
|---|---|---|
| Proven in tandem | Reading frame disrupted and NMD predicted | PVS1 |
| Proven in tandem | `No or unknown impact on reading frame and NMD` | N/A |
| Presumed in tandem | Reading frame presumed disrupted and NMD predicted | PVS1_Strong |
| Presumed in tandem | `No or unknown impact on reading frame and NMD` | N/A |
| Proven not in tandem | — | N/A |

The quoted N/A condition is the slide's incomplete literal wording.

Initiation-codon paths:

| Condition | Source outcome |
|---|---|
| Different functional transcript uses an alternative start codon | N/A |
| No known alternative start codon in other transcripts and `>=1` Pathogenic variant upstream of the closest potential in-frame start codon | PVS1_Moderate |
| No known alternative start codon in other transcripts and no Pathogenic variant upstream of the closest potential in-frame start codon | `PVS1_Supp` |

`PVS1_Supp` is the slide's literal abbreviated outcome label.

#### SCN1B exon numbering

Source: SCN1B sheet of `PVS1 exon numbering.xlsx`, headed `NM_001037.5`.

| Physical exon | Coding exon | Start | Stop | Frame |
|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 0 | OUT |
| 2 | 2 | 1 | 0 | OUT |
| 3 | 3 | 0 | 1 | OUT |
| 4 | 4 | 1 | 2 | OUT |
| 5 | 5 | 2 | -1 | OUT |
| 6 | - | untranslated |  |  |

The exon-5 stop value is the literal numeric `-1`; the source does not explain or normalize it.

### PS1 - Same amino-acid change

**Original ACMG summary:** Same amino-acid change as a previously established Pathogenic variant regardless of nucleotide change; beware of changes that affect splicing rather than the amino-acid/protein level.

| Strength | Missense rule |
|---|---|
| Strong | Same amino-acid change as a previously established Pathogenic variant, regardless of nucleotide change. |
| Moderate | Same amino-acid change as a previously established Likely Pathogenic variant, regardless of nucleotide change. |
| Supporting | No separate missense rule is specified; splice-event strength follows the matrix below. |

#### PS1 for variants with the same predicted splicing event

Source: `PS1_Variants impacting splicing.pdf`, Table 2 from Walker et al. (2023), PMID 37352859. Apply PS1 with PP3 or PVS1 as specified; do not replace this matrix with a simple P-versus-LP rule.

| VUA position and baseline code | Comparison-variant position relative to VUA | P comparison | LP comparison |
|---|---|---|---|
| Outside splice donor/acceptor `+/- 1,2`; PP3 | Same nucleotide | PS1 | PS1_Moderate |
| Outside splice donor/acceptor `+/- 1,2`; PP3 | Within the same splice donor/acceptor motif, including `+/- 1,2` | PS1_Moderate | PS1_Supporting |
| At splice donor/acceptor `+/- 1,2`; PVS1 | Within the same splice donor/acceptor `+/- 1,2` | PS1_Supporting | N/A |
| At splice donor/acceptor `+/- 1,2`; PVS1 | Within the same splice donor/acceptor region but outside `+/- 1,2` | PS1_Supporting | PS1_Supporting |
| At splice donor/acceptor `+/- 1,2`; PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | Within the same splice donor/acceptor `+/- 1,2` | PS1 | N/A |
| At splice donor/acceptor `+/- 1,2`; PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | Within the same splice donor/acceptor motif but outside `+/- 1,2` | PS1_Moderate | PS1_Supporting |

### PS2 - De novo, confirmed

Both maternity and paternity must be confirmed. Paternity alone is insufficient; egg donation, surrogate motherhood, embryo-transfer error, etc. can cause non-maternity.

Each unrelated proband receives phenotype-specific points:

| Phenotype | Points |
|---|---:|
| Genetic epilepsy with febrile seizures plus | 1 |
| Other epilepsy type or syndrome, with or without associated neurodevelopmental features | 0.5 |

The source prints four exact totals:

| Exact total | Strength |
|---:|---|
| 4 | PS2_VeryStrong |
| 2 | PS2_Strong |
| 1 | PS2_Moderate |
| 0.5 | PS2_Supporting |

> The VCEP does not state `>=` operators or define intermediate totals. Do not infer ranges.

### PS3 - Functional studies

| Strength | Criteria; any one is sufficient |
|---|---|
| Strong | Mouse knock-in model displays spontaneous seizures. |
| Moderate | Heterologous expression with voltage clamping shows a statistically significant difference from wild type in at least one parameter; mouse knock-in displays induced seizures; or zebrafish knock-in displays spontaneous seizures evidenced by hyperexcitability through electrophysiology or calcium-imaging-based studies. |
| Supporting | Zebrafish knock-in displays induced seizures evidenced by hyperexcitability through electrophysiology or calcium-imaging-based studies. |

### PS4 - Prevalence in affected individuals

The original source note uses strict `>5.0` for case-control RR or OR and requires that its confidence interval not include 1.0. For multiple unrelated patients with a consistent phenotype, use the same phenotype points as PS2.

| Total points | Strength |
|---:|---|
| `16+` | PS4_VeryStrong |
| 4-15.5, inclusive | PS4_Strong |
| 2-3.5, inclusive | PS4_Moderate |
| 1-1.5, inclusive | PS4_Supporting |

The core literally says “Present in in multiple unrelated patients”; the duplicated “in” is a source typo.

### PM1 - Mutational hot spot

**Not Applicable.** The core says too few pathogenic SCN1B variants have been reported to calculate mutational hotspots and that SCN1B does not belong to a gene family for PER use.

### PM2 - Absent from controls

Apply PM2_Supporting for one or fewer alleles when at least 10,000 alleles were assessed in population databases such as gnomAD. Population data for indels may be poorly called by next-generation sequencing.

### PM3 - In trans with a pathogenic variant

For the recessive disorder, score each occurrence by phase and classification of the other variant:

| Other variant / occurrence | Confirmed in trans | Phase unknown |
|---|---:|---:|
| Pathogenic | 1 | 0.5 |
| Likely Pathogenic | 1 | 0.25 |
| Homozygous occurrence (maximum total 1.0) | source says 0.5 | Not specified |
| VUS | 0.25 | 0 |

The source literally places “Confirmed in trans: 0.5 points” under homozygous occurrence; it does not give a separate phase-unknown homozygous value.

| Exact total | Strength |
|---:|---|
| 4.0 | PM3_VeryStrong |
| 2.0 | PM3_Strong |
| 1.0 | PM3_Moderate |
| 0.5 | PM3_Supporting |

The source does not state `>=` operators or intermediate ranges.

### PM4 - Protein-length change

Apply PM4_Moderate, unchanged from ACMG, for an in-frame deletion/insertion in a non-repeat region or a stop-loss variant.

### PM5 - Different missense change at the same site

| Strength | Criteria |
|---|---|
| Strong | `>=2` known Pathogenic variants at the same site as the novel change. |
| Moderate | Novel missense change at a residue where a different missense change was determined Pathogenic. |
| Supporting | Novel missense change at a residue where a different missense change was determined Likely Pathogenic. |

Beware of changes that affect splicing. The Strong source cell literally says “This should say greater than or equal to 2 known pathogenic variants at same site as novel change”; its editorial wording is a source defect, while `>=2` is explicit.

### PM6 - De novo, assumed

Each unrelated proband receives:

| Phenotype | Points |
|---|---:|
| Genetic epilepsy with febrile seizures plus | 0.5 |
| Other epilepsy type or syndrome, with or without associated neurodevelopmental features | 0.25 |

The source prints four exact totals:

| Exact total | Strength |
|---:|---|
| 4 | PM6_VeryStrong |
| 2 | PM6_Strong |
| 1 | PM6_Moderate |
| 0.5 | PM6_Supporting |

> The VCEP does not state `>=` operators or define intermediate totals. The Very Strong value is printed inside the Strong block. The package also does not state that PS2 and PM6 points may be pooled.

### PP1 - Co-segregation

| Strength | Autosomal dominant | Autosomal recessive |
|---|---:|---:|
| Strong | `>=7` independent meioses | `>=3` affected segregations |
| Moderate | 5-6 independent meioses | 2 affected segregations |
| Supporting | 3-4 independent meioses | 1 affected segregation |

### PP2 - Missense in a constrained gene

**Not Applicable.** Benign missense variants are common.

### PP3 - Computational evidence

Follow ClinGen recommendations (PMID 36413997) using REVEL. PP3 may be applied at Supporting or Moderate and is capped at Moderate. PP3+PM1 may reach no higher than Strong, although PM1 is Not Applicable for SCN1B. For splice-site variants where PVS1 is applied, do not combine PP3.

> The package supplies no numeric REVEL thresholds. Obtain them from the cited external recommendation; do not invent local cutoffs.

### PP4 - Phenotype specificity

**Not Applicable.** Phenotype specificity is incorporated into PS2, PM6, and PS4.

### PP5 - Reputable source

**Not Applicable.** The ClinGen SVI VCEP Review Committee recommends against this criterion (PMID 29543229).

---

## Benign criteria

### BA1 - Stand-alone frequency

Apply BA1 when allele frequency is strictly `>0.3%` in gnomAD or another large population database, with `>=5` alleles when at least 10,000 alleles were assessed.

### BS1 - Frequency greater than expected

Apply BS1_Strong when allele frequency is strictly `>0.01%` in gnomAD or another large population database, with `>=5` alleles when at least 10,000 alleles were assessed.

### BS2 - Observed in a healthy adult

Apply BS2_Strong when observed in a healthy adult individual. The VCEP supplies no further qualification beyond the original ACMG summary.

### BS3 - Functional studies showing no effect

**Not Applicable.** Values indicating no effect on channel function have not been sufficiently characterized. Normal heterologous electrophysiology cannot exclude non-electrophysiological neuronal defects such as mis-localization. Absence of an epilepsy phenotype in an animal model is also insufficient, and other behavioral comorbidities may still support pathogenicity. The expert panel may reassess this later.

### BS4 - Lack of segregation

**Not Applicable** because of reduced penetrance, variable expressivity, and phenocopies.

### BP1-BP7

| Criterion | Status | Source rule |
|---|---|---|
| BP1 | Not Applicable | The core literally says “Missense variants are common cause of disease.” |
| BP2 | Supporting | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder, or in cis with a pathogenic variant in any inheritance pattern. |
| BP3 | Supporting | In-frame deletion/insertion in a repetitive region without known function. |
| BP4 | Supporting or Moderate | Follow PMID 36413997 using REVEL. The package supplies no numeric thresholds. |
| BP5 | Supporting | Variant found in a case with an alternate molecular basis for disease. |
| BP6 | Not Applicable | Not for use per the ClinGen SVI VCEP Review Committee (PMID 29543229). |
| BP7 | Supporting | Synonymous variant predicted to have no effect on the splice consensus sequence and not create a new splice site, with a nucleotide that is not highly conserved. |

---

## Operative rules for combining criteria

Source: `Combining Rules.pdf`, which literally says “Tavtigan et al, 2018” in conjunction with “forthcoming points-based guidance.” No version or citation for that forthcoming guidance is supplied.

### Points per criterion

| Criterion strength | Points |
|---|---:|
| Pathogenic - Very Strong | 8 |
| Pathogenic - Strong | 4 |
| Pathogenic - Moderate | 2 |
| Pathogenic - Supporting | 1 |
| Benign - Supporting | -1 |
| Benign - Strong | -4 |

### Classification by total

| Total points | Classification | Posterior probability |
|---:|---|---:|
| `>=10` | Pathogenic | `>=0.99` |
| 6-9, inclusive | Likely Pathogenic | `>=0.9` to `<0.99` |
| 0-5, inclusive | VUS | `>=0.10` to `<0.9` |
| -6 to -1, inclusive | Likely Benign | source prints `>=0.001, <0.1` |
| -7 and below | Benign | `<0.001` |

Additional caveats:

- PP3+PM1 combined can reach no higher than Strong; PM1 is Not Applicable for SCN1B.
- When PM5_Strong is reached, do not combine PM1 with PM5.

The traditional combination table still printed in the core PDF is intentionally not reproduced as an operative alternative because the core explicitly directs users to disregard it.

---

## Supplement inspection notes

`PVS1 exon numbering.xlsx` also contains SCN1A, SCN2A, SCN3A, and SCN8A sheets. Those sheets corroborate panel conventions but must not be substituted for the SCN1B table above.

`PVS1 Decision Tree.pptx` contains 80 shapes and 77 connectors. Three connector bindings are incomplete in raw OOXML, although the rendered endpoints visibly establish the intended branches. The branch transcription above follows the rendered topology and the exact slide text/notes.

---

## Source files

- `ClinGen_ACMG_Specifications_SCN1B_v2.0.pdf`
- `PVS1 Decision Tree.pptx`
- `PVS1 exon numbering.xlsx`
- `PS1_Variants impacting splicing.pdf`
- `Combining Rules.pdf`

## Version history

| Version | Date | Notes |
|---|---|---|
| 2.0.0 | 1/7/2025 | Updates to transcript information and exon numbering; points-based combining system incorporated. |

### Document corrections - 2026-08-10

Same-version documentation remediation; the ClinGen specification version remains 2.0.0.

- Verified all criteria, release metadata, DOI, core transcript `.4`, exact comparators, source typos, and instruction to disregard the traditional combination grid against `ClinGen_ACMG_Specifications_SCN1B_v2.0.pdf`.
- Restored the complete rendered topology and all three speaker-note definitions from `PVS1 Decision Tree.pptx`; corrected reversed initiation-codon outcomes, missing N/A branches, and the unsupported direct mapping of an unknown region to Moderate; preserved the exact `>10%`/`>=200 aa` and `<10%`/`<200 aa` box pairings without supplying an AND/OR relation; recorded the exact-10% gap, incomplete connector bindings, and the unresolved core/tree/points conflict for full-gene deletion.
- Recorded the core `.4` versus supplement `.5` transcript contradiction and restored the complete SCN1B exon table, including literal exon-5 stop `-1`, from `PVS1 exon numbering.xlsx` after inspecting all five workbook sheets.
- Restored the exact six-row splice-event matrix from `PS1_Variants impacting splicing.pdf`; removed broad P-versus-LP splice shortcuts that contradicted its position/baseline-dependent outcomes.
- Restored the operative points, classification intervals, posterior probabilities, and caveats from `Combining Rules.pdf`; removed the explicitly superseded traditional combination grid.
- Replaced inferred `>=` PS2/PM6 ladders with the core's exact bare totals, removed unsupported interpolations, corrected the unsupported homozygous phase-unknown PM3 cell, and marked undistributed numeric REVEL thresholds as unavailable.
- Preserved or explicitly flagged source wording defects rather than silently repairing them.
