# ClinGen Epilepsy Sodium Channel Expert Panel Variant Interpretation Guidelines for SCN1A

**Version:** 2.0.0

**Released:** 1/7/2025

**Affiliation:** Epilepsy Sodium Channel VCEP

**DOI:** 10.5281/zenodo.21433911

**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

**Release Notes:** Release contains updates to exon numbering and revised PM1 table.

> **Operative combining framework:** This VCEP directs users to disregard the “Rules for Combining Criteria” printed in the core specification and use the distributed `Combining Rules.pdf` points-based framework instead.

> **Source-package limitation:** The core specification repeatedly says that a “PVS1 Decision Tree” is included, but no such file is present in the distributed package or its metadata. Do not substitute a generic SVI/Tayoun decision tree. The package supports the full-gene-deletion statement and the exon-numbering table below, but it does not support operational PVS1 branch assignments for other variant types.

---

## Gene information

| Attribute | Value |
|---|---|
| Gene | SCN1A (HGNC:10585) |
| HGNC name | sodium voltage-gated channel alpha subunit 1 |
| Core-PDF transcript | NM_001165963.3 |
| Exon-workbook transcript | NM_001165963.4 |
| Disease | Dravet syndrome (MONDO:0100135), autosomal dominant |
|  | Generalized epilepsy with febrile seizures plus (MONDO:0018214), autosomal dominant |
|  | Developmental and epileptic encephalopathy (MONDO:0100062), autosomal dominant |

> **Unresolved source contradiction:** The core PDF names `NM_001165963.3`, while the SCN1A sheet of `PVS1 exon numbering.xlsx` names `NM_001165963.4`. The release note says exon numbering was updated, but the package does not reconcile the transcript versions. Preserve both readings when interpreting the document.

### Clinical criteria for Dravet syndrome

The source attributes these criteria to Li et al. (2021), PMID 34338318. Dravet syndrome requires the listed major features and at least three minor criteria.

**Major features**

- Fever-sensitive seizures
- Hemiclonic or tonic-clonic seizures
- Status epilepticus

**Minor criteria (at least 3)**

- Normal development before seizure onset
- Seizure onset `<=12m`
- Developmental impairment by age 5y
- Intellectual disability

---

## Pathogenic criteria

### PVS1 - Null variant

**Original ACMG summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single- or multi-exon deletion) in a gene where loss of function is a known disease mechanism.

**Original caveats retained by the source:** use caution at the extreme 3' end, with predicted exon skipping that leaves the remainder of the protein intact, and in the presence of multiple transcripts.

**VCEP specification:** A full-gene deletion warrants a pathogenic classification. For PVS1 Very Strong, Strong, Moderate, and Supporting, the core says to follow Tayoun et al. (2018) using an included “PVS1 Decision Tree.” That decision tree is not distributed, so these other PVS1 paths cannot be operationalized from this package.

#### SCN1A exon numbering

Source: SCN1A sheet of `PVS1 exon numbering.xlsx`, headed `NM_001165963.4`.

| Physical exon | Coding exon | Start | Stop | Frame |
|---:|---:|---:|---:|---|
| 1 | - | untranslated |  |  |
| 2 | - | untranslated |  |  |
| 3 | - | untranslated |  |  |
| 4 | 1 | 0 | 0 | IN |
| 5 | 2 | 0 | 2 | OUT |
| 6 | 3 | 2 | 2 | IN |
| 7 | 4 | 2 | 2 | IN |
| 8 | 5 | 2 | 1 | OUT |
| 9 | 6 | 1 | 1 | IN |
| 10 | 7 | 1 | 2 | OUT |
| 11 | 8 | 2 | 0 | OUT |
| 12 | 9 | 0 | 0 | IN |
| 13 | 10 | 0 | 0 | IN |
| 14 | 11 | 0 | 0 | IN |
| 15 | 12 | 0 | 1 | OUT |
| 16 | 13 | 1 | 0 | OUT |
| 17 | 14 | 0 | 0 | IN |
| 18 | 15 | 0 | 0 | IN |
| 19 | 16 | 0 | 0 | IN |
| 20 | 17 | 0 | 1 | OUT |
| 21 | 18 | 1 | 0 | OUT |
| 22 | 19 | 0 | 0 | IN |
| 23 | 20 | 0 | 0 | IN |
| 24 | 21 | 0 | 0 | IN |
| 25 | 22 | 0 | 0 | IN |
| 26 | 23 | 0 | 0 | IN |
| 27 | 24 | 0 | 0 | IN |
| 28 | 25 | 0 | 1 | OUT |
| 29 | 26 | 1 | `X ` | OUT |

The final stop cell is literally `X ` with a trailing space. The workbook does not map these exon/frame data to PVS1 strengths.

### PS1 - Same amino-acid change

**Original ACMG summary:** Same amino-acid change as a previously established pathogenic variant regardless of nucleotide change. Beware of changes that affect splicing rather than the amino-acid/protein level.

The source says the neurodevelopmental sodium-channel paralogs SCN1A, SCN2A, SCN3A, and SCN8A share >77% sequence identity (PMID 33531663). Their voltage-sensor and pore domains are largely preserved; excluding terminal regions and cytoplasmic loops raises homology to >90% (PMIDs 33531663 and 16382098). Pathogenic and Likely Pathogenic paralogous variants may therefore be considered.

| Strength | Missense rule |
|---|---|
| Strong | Same amino-acid change as a previously established Pathogenic variant, regardless of nucleotide change; **or** `>1` identical amino-acid change in a paralogous SCN1A/SCN2A/SCN3A/SCN8A gene previously established as Pathogenic or Likely Pathogenic. |
| Moderate | Same amino-acid change as a previously established Likely Pathogenic variant, regardless of nucleotide change. |
| Supporting | A single identical amino-acid change in a paralogous SCN1A/SCN2A/SCN3A/SCN8A gene previously established as Pathogenic or Likely Pathogenic. |

Use the exact position alignment in `Paralogous Gene Table.xlsx`; the workbook supplies position correspondence only, not variant classifications or amino-acid identities.

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

**Original ACMG summary:** De novo with both maternity and paternity confirmed in a patient with the disease and no family history.

Confirmation of paternity alone is insufficient; egg donation, surrogate motherhood, embryo-transfer error, etc. can contribute to non-maternity.

Each unrelated proband receives phenotype-specific points:

| Phenotype | Points |
|---|---:|
| Dravet syndrome meeting the criteria above | 2 |
| Genetic epilepsy with febrile seizures plus | 1 |
| Developmental and epileptic encephalopathy | 1 |
| Hemiplegic migraine | 0.5 |
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

**Original ACMG summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. The core also retains the original note that the most well-established studies are validated, reproducible, and robust in a clinical diagnostic laboratory setting.

If a variant reaches different strengths across measurements or publications, use the highest available strength, capped at Strong.

| Strength | Criteria; any one is sufficient |
|---|---|
| Strong | Peak current `<=72.7%` of wild type; persistent current `>=135%` of wild type; absolute activation shift at least 2.2 mV; absolute inactivation shift at least 4.1 mV; or mouse knock-in with spontaneous seizures. |
| Moderate | Peak current `<=80.6%` of wild type; persistent current `>=125%` of wild type; absolute activation shift at least 2.1 mV; absolute inactivation shift at least 3.0 mV; mouse knock-in with induced seizures; or zebrafish knock-in with spontaneous seizures evidenced by hyperexcitability through electrophysiology or calcium-imaging studies. |
| Supporting | Zebrafish knock-in with induced seizures evidenced by hyperexcitability through electrophysiology or calcium-imaging studies. |

The current and voltage-shift thresholds overlap by design; apply the highest satisfied strength.

### PS4 - Prevalence in affected individuals

For multiple unrelated patients with a consistent phenotype, use the same phenotype point values as PS2.

| Total points | Strength |
|---:|---|
| `16+` | PS4_VeryStrong |
| 4-15.5, inclusive | PS4_Strong |
| 2-3.5, inclusive | PS4_Moderate |
| 1-1.5, inclusive | PS4_Supporting |

The source notation is `16+`; it does not print a comparison operator, so it is not rewritten as `>=16`.

The core literally says “Present in in multiple unrelated patients”; the duplicated “in” is a source typo.

### PM1 - Pathogenic Enriched Region

**Original ACMG summary:** Located in a mutational hot spot and/or critical, well-established functional domain without benign variation.

The VCEP defines Pathogenic Enriched Regions as regions enriched for pathogenic ClinVar/HGMD variants across gene families and lacking gnomAD variation (Pérez-Palma 2020, PMID 31871067; Lal et al. 2020, PMID 32183904). Apply PM1_Moderate to a variant within an attached-table PER.

The attached `PM1 Table.xlsx` enumerates every residue. Its consecutive rows compress exactly to these inclusive ranges:

| PER | SCN1A | SCN2A | SCN3A | SCN8A |
|---:|---:|---:|---:|---:|
| 1 | 212-230 | 213-231 | 212-230 | 216-234 |
| 2 | 247-255 | 248-256 | 247-255 | 251-259 |
| 3 | 411-424 | 413-426 | 412-425 | 399-412 |
| 4 | 859-867 | 850-858 | 851-859 | 844-852 |
| 5 | 879-887 | 870-878 | 871-879 | 864-872 |
| 6 | 889-902 | 880-893 | 881-894 | 874-887 |
| 7 | 904-912 | 895-903 | 896-904 | 889-897 |
| 8 | 931-939 | 922-930 | 923-931 | 916-924 |
| 9 | 979-997 | 970-988 | 971-989 | 964-982 |
| 10 | 1321-1364 | 1311-1354 | 1309-1352 | 1301-1344 |
| 11 | 1468-1476 | 1458-1466 | 1453-1461 | 1449-1457 |
| 12 | 1478-1491 | 1468-1481 | 1463-1476 | 1459-1472 |
| 13 | 1493-1511 | 1483-1501 | 1478-1496 | 1474-1492 |
| 14 | 1631-1649 | 1621-1639 | 1616-1634 | 1612-1630 |
| 15 | 1656-1674 | 1646-1664 | 1641-1659 | 1637-1655 |
| 16 | 1771-1784 | 1761-1774 | 1756-1769 | 1751-1764 |

PP3+PM1 combined can reach no higher than Strong.

### PM2 - Absent from controls

Apply PM2_Supporting for one or fewer alleles when at least 10,000 alleles were assessed in population databases such as gnomAD. Population data for indels may be poorly called by next-generation sequencing.

### PM3 - In trans with a pathogenic variant

**Not Applicable.** SCN1A is associated with autosomal dominant inheritance.

### PM4 - Protein-length change

Apply PM4_Moderate, unchanged from ACMG, for an in-frame deletion/insertion in a non-repeat region or a stop-loss variant.

### PM5 - Different missense change at the same residue

The same paralog rationale and mapping limitation described under PS1 applies. Beware of variants that affect splicing.

| Strength | Criteria |
|---|---|
| Strong | `>=2` known pathogenic variants at the same site as the novel change, within the same gene. |
| Moderate | Novel missense change at a residue in the same gene where a different missense variant was determined Pathogenic. |
| Supporting | Novel missense change at a residue where a different missense change was determined Likely Pathogenic; **or** `>1` non-identical amino-acid change in paralogous SCN1A/SCN2A/SCN3A/SCN8A genes where a different missense change was determined Pathogenic or Likely Pathogenic. |

If PM5_Strong is reached and the variant lies in a PM1 region, do not add PM1.

The core literally misspells “neurodevelopmental” as “neurodevelomental” in its PS1/PM5 paralog discussion and includes the malformed phrase “amino acid sequence similarly” in PM5. These are source wording defects; the operative transcription above preserves their evident meaning without silently treating the literal text as valid terminology.

### PM6 - De novo, assumed

**Original ACMG summary:** Assumed de novo without confirmation of maternity and paternity.

Each unrelated proband receives:

| Phenotype | Points |
|---|---:|
| Dravet syndrome meeting the criteria above | 1 |
| Genetic epilepsy with febrile seizures plus | 0.5 |
| Developmental and epileptic encephalopathy | 0.5 |
| Hemiplegic migraine | 0.25 |
| Other epilepsy type or syndrome, with or without associated neurodevelopmental features | 0.25 |

The source prints four exact totals:

| Exact total | Strength |
|---:|---|
| 4 | PM6_VeryStrong |
| 2 | PM6_Strong |
| 1 | PM6_Moderate |
| 0.5 | PM6_Supporting |

> The VCEP does not state `>=` operators or define intermediate totals. Do not infer ranges. The source literally prints “Dravet*: 1 points”; that grammatical error is preserved here as a source note. The package also does not state that PS2 and PM6 totals may be pooled together.

### PP1 - Co-segregation

| Independent meioses | Strength |
|---:|---|
| `>=7` | PP1_Strong |
| 5-6, inclusive | PP1_Moderate |
| 3-4, inclusive | PP1_Supporting |

### PP2 - Missense in a constrained gene

**Not Applicable.** The source says benign missense variants are common.

### PP3 - Computational evidence

Follow ClinGen recommendations (PMID 36413997) using REVEL. PP3 may be applied at Supporting or Moderate, is capped at Moderate, and PP3+PM1 may reach no higher than Strong.

> The package supplies no numeric REVEL thresholds. Obtain them from the cited external recommendation; do not invent local cutoffs.

The PP3_Supporting block in the core repeats “with the following stipulations” twice; this is a source typo.

### PP4 - Phenotype specificity

**Not Applicable.** Phenotype specificity is incorporated into PS2, PM6, and PS4.

### PP5 - Reputable source

**Not Applicable.** The ClinGen SVI VCEP Review Committee recommends against using this criterion (PMID 29543229).

---

## Benign criteria

### BA1 - Stand-alone frequency

Apply BA1 when allele frequency is strictly `>0.02%` in gnomAD or another large population database, with `>=5` alleles when at least 10,000 alleles were assessed.

### BS1 - Frequency greater than expected

Apply BS1_Strong when allele frequency is strictly `>0.0004%` in gnomAD or another large population database, with `>=5` alleles when at least 10,000 alleles were assessed.

### BS2 - Observed in a healthy adult

Apply BS2_Strong when observed in a healthy adult individual. The VCEP supplies no further qualification beyond the original ACMG summary.

### BS3 - Functional studies showing no effect

**Not Applicable.** Values indicating no effect on channel function have not been sufficiently characterized. Normal heterologous electrophysiology cannot exclude non-electrophysiological neuronal defects such as mis-localization. Absence of an epilepsy phenotype in an animal model is also insufficient, and other behavioral comorbidities may still support pathogenicity. The expert panel may reassess this later.

### BS4 - Lack of segregation

**Not Applicable** because of reduced penetrance, variable expressivity, and phenocopies.

### BP1-BP7

| Criterion | Status | Source rule |
|---|---|---|
| BP1 | Not Applicable | Missense variants are a common disease mechanism. |
| BP2 | Supporting | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder, or in cis with a pathogenic variant in any inheritance pattern. |
| BP3 | Supporting | In-frame deletion/insertion in a repetitive region without known function. |
| BP4 | Supporting or Moderate | Follow PMID 36413997 using REVEL. The package supplies no numeric thresholds. |
| BP5 | Supporting | Variant found in a case with an alternate molecular basis for disease. |
| BP6 | Not Applicable | Not for use per the ClinGen SVI VCEP Review Committee (PMID 29543229). |
| BP7 | Supporting | Synonymous variant predicted to have no effect on the splice consensus sequence and not create a new splice site, with a nucleotide that is not highly conserved. |

---

## Operative rules for combining criteria

Source: `Combining Rules.pdf`, based on “Tavtigan [sic] et al, 2018” in conjunction with “forthcoming points-based guidance.” No version or citation for that forthcoming guidance is supplied.

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

- PP3+PM1 combined can reach no higher than Strong.
- When PM5_Strong is reached, do not combine PM1 with PM5.

The traditional combination table still printed in the core PDF is intentionally not reproduced as an operative alternative because the core explicitly directs users to disregard it.

---

## Supplement interpretation notes

### Paralogous position mapping

`Paralogous Gene Table.xlsx` contains 2,044 alignment rows under four columns. It does not contain amino-acid identities, transcript accessions, variant classifications, or provenance. Each gene column contains every integer residue number exactly once and literal `NA` alignment gaps:

| Gene | Residues represented | `NA` cells |
|---|---:|---:|
| SCN1A | 1-2009 | 35 |
| SCN2A | 1-2005 | 39 |
| SCN3A | 1-2000 | 44 |
| SCN8A | 1-1980 | 64 |

Use its exact row alignment for cross-gene translation. A constant offset is unsafe because gap locations change across the alignment. The workbook declares the OOXML dimension `A1:IV2045`, but its actual populated/data range is only `A1:D2045`; columns E:IV contain no data. The oversized declared dimension makes PDF/print exports unreadably compressed. This is a workbook-layout defect, not missing data.

The mapping is losslessly reconstructable from the following worksheet-row gaps (row 1 is the header): start each gene at residue 1 on row 2, increment by one on every non-`NA` row, and retain `NA` on the listed rows.

| Gene | Worksheet rows containing `NA` |
|---|---|
| SCN1A | 41-44, 49, 300, 475-478, 491-493, 532, 594-595, 637-641, 746, 1091, 1189, 1431, 2024-2033 |
| SCN2A | 41-44, 475-478, 480, 524, 532, 594-595, 637-641, 685, 693-703, 746, 1109-1110, 1171, 1431, 2008, 2024-2026 |
| SCN3A | 41-44, 49, 475-480, 594-595, 637-641, 693-703, 746, 1069, 1078-1081, 1171, 1425-1427, 1431, 2008, 2024-2026 |
| SCN8A | 49, 288-304, 493, 553-554, 560-561, 685-686, 693-704, 1067-1068, 1111-1112, 1124, 1171, 1189, 1762, 1960-1977, 2008 |

### PVS1 workbook scope

`PVS1 exon numbering.xlsx` also contains SCN2A, SCN3A, SCN8A, and SCN1B sheets. Those sheets corroborate panel conventions but must not be substituted for the SCN1A table above.

---

## Source files

- `ClinGen_ACMG_Specifications_SCN1A_v2.0.pdf`
- `PS1_Variants impacting splicing.pdf`
- `PM1 Table.xlsx`
- `Combining Rules.pdf`
- `PVS1 exon numbering.xlsx`
- `Paralogous Gene Table.xlsx`
- Package manifest: `GN067_data.json`

## Version history

| Version | Date | Notes |
|---|---|---|
| 2.0.0 | 1/7/2025 | Updates to exon numbering and revised PM1 table; points-based combining system incorporated. |

### Document corrections - 2026-08-10

Same-version documentation remediation; the ClinGen specification version remains 2.0.0.

- Verified the complete criteria transcription, release metadata, DOI, transcript `.3`, source wording including the PS4 `16+` notation, and explicit instruction to disregard the traditional combination table against `ClinGen_ACMG_Specifications_SCN1A_v2.0.pdf`.
- Recorded that the core-claimed “PVS1 Decision Tree” is absent from the distributed package and removed any implication that its branch rules are locally available; verified package completeness and the advertised file list against `GN067_data.json`.
- Restored the exact six-row splice-event matrix and its position/baseline qualifications from `PS1_Variants impacting splicing.pdf`; removed broad P-versus-LP summaries that contradicted the matrix.
- Verified all 249 PM1 data rows and retained their complete cross-gene ranges from `PM1 Table.xlsx`.
- Replaced inferred `>=` PS2/PM6 ladders with the core’s exact bare totals and removed the unsupported claim that PS2 and PM6 totals may be pooled.
- Marked the transcript `.3`/`.4` contradiction, restored the complete SCN1A exon table, and preserved the terminal `X ` cell from `PVS1 exon numbering.xlsx`.
- Verified every one of the 8,176 alignment cells in `Paralogous Gene Table.xlsx`; clarified that it is a position mapping rather than a variant or amino-acid-identity table and distinguished its erroneous declared dimension `A1:IV2045` from its actual populated/data range `A1:D2045`.
- Restored the operative point weights, literal classification-band wording including “-7 and below,” posterior probabilities, both caveats, and printed “Tavtigan [sic]” attribution from `Combining Rules.pdf`; removed the superseded traditional rule grid from operational presentation.
- Preserved or explicitly flagged source typos and unresolved omissions instead of silently correcting or reconciling them.
