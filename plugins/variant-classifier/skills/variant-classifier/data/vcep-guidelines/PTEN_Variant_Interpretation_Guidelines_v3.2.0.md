# ClinGen PTEN Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for PTEN

**Version:** 3.2
**Released:** 4/6/2026
**Affiliation:** PTEN VCEP
**Rights Holder:** The Clinical Genome Resource (ClinGen)
**Type (as stated by VCEP):** Richards et.al., 2015 - Combining rules
**Description (as stated by VCEP):** ACMG Classification Rules Specified for PTEN Variant Curation
**DOI:** 10.5281/zenodo.21421451
**Source basis:** ClinGen Criteria Specification Registry entry GN003, `ClinGen_ACMG_Specifications_PTEN_v3.2.pdf`, plus five distributed supplementary files (PVS1 decision tree, Rules for Combining Criteria, pediatric phenotype scoring table, Cleveland Clinic score table, BLOSUM matrix).

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | PTEN (HGNC:9588) |
| **HGNC Name** | phosphatase and tensin homolog |
| **Transcript** | NM_000314.8 |
| **Disease** | PTEN hamartoma tumor syndrome (MONDO:0017623) |
| **Inheritance** | Autosomal dominant inheritance |

**Keywords (as listed by VCEP):** human biology genomics variant variant classification clingen disease standards PTEN NM_000314.8 Autosomal dominant inheritance PTEN hamartoma tumor syndrome

**General Comments (verbatim from the specification):**

> Minor Changes: 1. Correct SpliceAI cutoff for BP4 rule 2. Correct the Rules for Combining Criteria 3. Add BLOSUM matrix, Cleveland Clinic core and Pediatric score tables 4. Added disease name, MOI and added underscores for some greater than symbols

*(Transcribed verbatim; "Cleveland Clinic core" appears in the source where "score" is presumably intended.)*

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PS4 - Prevalence in Affected / Phenotype Specificity](#ps4---prevalence-in-affected--phenotype-specificity)
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
3. [Frequency Threshold Summary](#frequency-threshold-summary)
4. [Rules for Combining Criteria](#rules-for-combining-criteria)
5. [Appendices](#appendices)
6. [References](#references)
7. [Version History](#version-history)

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.
Caveats:
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:**

> PTEN EP Specification: Follow SVI guidance, using PTEN-specific information. Per the PVS1 workflow guidance provided in Tayoun et al. 2018 (PMID 30192042), the following will apply:
>
> 1. **Nonsense, frameshift variants:**
>    - PVS1 applies to variants predicted to result in nonsense-mediated decay (NMD); the predicted NMD cutoff for PTEN occurs at c.1121 (p.D375).
>    - For nonsense or frameshift variants at the 3' end of the gene NOT predicted to result in nonsense-mediated decay, PVS1 may still be applied if the protein is disrupted at or 5' to c.1121 (NM_000314.6). Please see supplementary information in manuscript for evidence supporting this cutoff.
>    - PVS1_Moderate applies to variants resulting in protein truncation 3' of this cutoff.
> 2. **Splicing variants (+/- 1,2 intronic positions):** Only apply to the variants resulting NMD (please refer to decision tree) OR entire exon deletion:
>    - Exons 1,2,4,5,6 OR 7 deletions OR multi-exon deletion: PVS1 (Resulting frameshift)
>    - Exons 3,8 OR 9 deletions: PVS1_Strong (in-frame but truncated/altered region is critical to protein function).
> 3. **Deletion (Single/multi exon to full gene):** Please refer to decision tree.
> 4. **Duplication:** Please refer to decision tree.
> 5. **Initiation codon:** PVS1 applies to initiation codon variants.
>
> PTEN EP Commentary: No known alternative start codon in other transcripts. There are sufficient patients' data from literature and labs support the pathogenicity of initiation codon variants.

*Note on transcript: the PVS1 narrative cites `NM_000314.6` for the c.1121 cutoff, while the specification header and the PVS1 decision tree both use `NM_000314.8`. Transcribed as written — see changelog.*

#### Strength Levels

| Strength | Criteria (verbatim) | Modification Type |
|----------|---------------------|-------------------|
| **Very Strong** | Use PTEN PVS1 decision tree. | Disease-specific |
| **Strong** | Use PTEN PVS1 decision tree. | Disease-specific |
| **Moderate** | Use PTEN PVS1 decision tree. | Disease-specific |
| **Supporting** | Not specified by VCEP (no PVS1_Supporting level is defined). | — |

The decision tree itself is transcribed in [Appendix A](#appendix-a--pten-pvs1-decision-tree).

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
Example: Val->Leu caused by either G>C or G>T in the same codon.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

> PTEN EP Specification: PS1 will be applied as described and expanded to include a different nucleotide substitution for an intronic splice site variant if the predicted impact is equal to or greater than the known pathogenic variant per in silico splicing tools. Caution should be used when applying this criteria to exonic variants causing aberrant splicing.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change OR different variant at same nucleotide position as a pathogenic splicing variant, where in silico models predict impact equal to or greater than the known pathogenic variant. | Disease-specific |
| **Moderate** | Not specified by VCEP. | — |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:**

> PS2_Very Strong: Two or more occurrences of PS2 OR two or more occurrences of PM6 AND one occurrence of PS2.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Very Strong** | Two proven OR four assumed OR one proven + two assumed de novo observations in a patient with the disease and no family history. | Strength |
| **Strong** | De novo (both maternity and paternity confirmed) observation in a patient with the disease and no family history. | None |
| **Moderate** | Not specified by VCEP under PS2 (assumed de novo is handled under PM6). | — |
| **Supporting** | Not specified by VCEP. | — |

**No de novo point matrix is defined by this VCEP.** The specification defines de novo escalation only through the counting rules above and the parallel PM6 rules; it does not distribute points per observation and does not reference the SVI de novo point system.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:**

> PTEN EP Specification:
>
> PS3 may be applied to the following assays:
> - RNA, mini-gene, or other assay demonstrating an impact on splicing.
>
> **PS3_Moderate:**
> - Mighell et al. 2018 (PMID: 29706350): Massively parallel functional assay interrogating phosphatase activity.
>   - In the supplementary material (Table S2) search for the variant in columns A or B and make sure the variant in question is listed as TRUE under column I (high confidence). If not, do not use as evidence.
>   - Under column G, the cumulative score is listed. Apply PS3_moderate for all variants with scores ≤ -1.11.
>
> **PS3_Supporting:** Other studies demonstrating lipid phosphatase activity <50% of wild-type or abnormal in vitro cellular assay or transgenic model with phenotype different from wild-type that does not meet PS3_moderate. Examples of in vitro cellular assays to be considered for PS3_supporting evidence may include:
> - In vitro assay demonstrating >50% reduction in phosphatase activity compared to wild type control. Phosphatase assays for which criteria may be applied must include a catalytic dead control, such as p.C124S, as well as at least three biological replicates: Myers et al. 1998 (PMID: 9811831), Stambolic et al. 1998 (PMID: 9778245), Han et al. 2000 (PMID: 10866302), Rodriguez-Escudero et al. 2011 (PMID: 21828076), Costa et al. 2015 (PMID: 26504226), Malek et al. 2017 (PMID: 29056325).
> - Decreased PTEN or increased pAKT expression: Tan 2011 (PMID: 21194675), Spinelli 2015 (PMID: 25527629).
> - Disruption of protein cellular localization: Lobo et al. 2009 (PMID: 19457929), He et al. 2012 (PMID: 22962422), Gil et al. 2015 (PMID: 25875300)
> - Aberrant cellular phenotypes, including defective cell migration, proliferation, and invasion: Costa et al. 2015 (PMID: 26504226), Malek et al. 2017 (PMID: 29056325)

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. RNA, mini-gene, or other assay shows impact on splicing. | Disease-specific |
| **Moderate** | Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Phosphatase activity ≤ -1.11 per Mighell et al. 2018, PMID: 29706350. | Disease-specific |
| **Supporting** | Phosphatase activity <50% of wild-type or abnormal in vitro cellular assay or transgenic model with phenotype different from wild type that does not meet PS3_moderate. | Disease-specific, Strength |

#### Approved Assay Instances

| Assay / readout | PMID | Strength |
|-----------------|------|----------|
| RNA, mini-gene, or other splicing assay showing impact on splicing | — | PS3 (Strong) |
| Mighell et al. 2018 massively parallel phosphatase assay — Table S2 cumulative score (column G) **≤ -1.11**, with high-confidence flag TRUE in column I | 29706350 | PS3_Moderate |
| In vitro phosphatase assay, >50% reduction vs. wild type (requires catalytic-dead control e.g. p.C124S and ≥3 biological replicates) — Myers 1998 | 9811831 | PS3_Supporting |
| In vitro phosphatase assay — Stambolic 1998 | 9778245 | PS3_Supporting |
| In vitro phosphatase assay — Han 2000 | 10866302 | PS3_Supporting |
| In vitro phosphatase assay — Rodriguez-Escudero 2011 | 21828076 | PS3_Supporting |
| In vitro phosphatase assay / aberrant cellular phenotype — Costa 2015 | 26504226 | PS3_Supporting |
| In vitro phosphatase assay / aberrant cellular phenotype — Malek 2017 | 29056325 | PS3_Supporting |
| Decreased PTEN or increased pAKT expression — Tan 2011 | 21194675 | PS3_Supporting |
| Decreased PTEN or increased pAKT expression — Spinelli 2015 | 25527629 | PS3_Supporting |
| Disruption of protein cellular localization — Lobo 2009 | 19457929 | PS3_Supporting |
| Disruption of protein cellular localization — He 2012 | 22962422 | PS3_Supporting |
| Disruption of protein cellular localization — Gil 2015 | 25875300 | PS3_Supporting |

**Comparator note:** the Mighell threshold is **inclusive** (`≤ -1.11`).

---

### PS4 - Prevalence in Affected / Phenotype Specificity

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:**

> PTEN EP Commentary: This criterion is unlikely to be used in this manner for a condition as rare as PHTS. However, if sufficiently powered, a case-control study finding an odds ratio >2 for a PHTS component phenotype with p<0.05 and 95% confidence interval with lower limit >1.5, this criteria may be applied. However, this criterion may not be applied in combination with PP4.
>
> **Use 2:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.
>
> PTEN EP Specifications: This criterion may not be applied if BS1 applies. Phenotype specificity scores are added across independent probands and calculated as follows:
>
> **Adults:**
> - 1 point per proband with Cleveland Clinic (CC) score ≥ 30 (Tan 2011)
> - 0.5 points per proband with CC score of 25-29.
>
> **Children:**
> - 1 point per proband with pediatric phenotype score ≥ 5 (please see supplementary information in manuscript for scoring rubric).
> - 0.5 points per proband with pediatric phenotype score of 4, but autism/developmental delay/intellectual disability may not contribute to the score.
>
> PS4_Very Strong: Probands with specificity score ≥16.
> PS4: Probands with specificity score of 4-15.5.
> PS4_Moderate: Probands with specificity score of 2-3.5.
> PS4_Supporting: Proband(s) with specificity score of 1-1.5.

*Note: the specification labels the phenotype-specificity branch "Use 2" but no branch is explicitly labelled "Use 1"; the case-control commentary above it is the implied Use 1. Transcribed as written.*

#### Phenotype Specificity Score → Strength

| Strength | Specificity score | Modification Type |
|----------|-------------------|-------------------|
| **Very Strong** | ≥ 16 (inclusive) | Strength |
| **Strong (PS4)** | 4 – 15.5 (inclusive range) OR the prevalence of the variant in affected individuals is significantly increased compared with the prevalence in controls | Strength |
| **Moderate** | 2 – 3.5 (inclusive range) | Strength |
| **Supporting** | 1 – 1.5 (inclusive range); phenotype specific for disease with single genetic etiology | Disease-specific |

#### Per-proband point assignment

| Proband group | Condition | Points |
|---------------|-----------|--------|
| Adults | Cleveland Clinic score **≥ 30** (inclusive) | 1 |
| Adults | Cleveland Clinic score **25–29** (inclusive range) | 0.5 |
| Children | Pediatric phenotype score **≥ 5** (inclusive) | 1 |
| Children | Pediatric phenotype score **= 4**, with autism/DD/ID not contributing to the score | 0.5 |

Scoring rubrics are transcribed in [Appendix B](#appendix-b--cleveland-clinic-score-adults) and [Appendix C](#appendix-c--pten-phenotype-scoring-for-pediatric-patients).

**Interaction constraints stated by the VCEP:**
- PS4 may **not** be applied in combination with PP4 (PP4 is in any case Not Applicable for PTEN).
- PS4 may **not** be applied if BS1 applies.
- When PM6_Strong is applied for a single individual on the basis of phenotype specificity, that individual is **not** also counted towards PS4.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:**

> PTEN EP Specification: Defined to include residues in one of PTEN's catalytic motifs, which include the WPD loop (residues 90-94), P-loop (also described as phosphatase core, residues 123-130), and the TI-loop (residues 166-168) (NP_ 000305.3) (Lee 1999).

| Catalytic motif | Residues (NP_ 000305.3) |
|-----------------|-------------------------|
| WPD loop | 90–94 |
| P-loop (phosphatase core) | 123–130 |
| TI-loop | 166–168 |

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Located in a mutational hot spot and/or critical and well-established functional domain. Defined to include residues in catalytic motifs: 90-94, 123-130, 166-168 (NP_ 000305.3) | Disease-specific |

*Source note: the protein accession is written `NP_ 000305.3` with an internal space throughout the specification; the citation "(Lee 1999)" is not present in the specification's reference list.*

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.
Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:**

> PTEN EP Specification: Criteria may be applied if a variant is present at <0.00001 (0.001%) allele frequency in gnomAD or another large sequenced population. If multiple alleles are present within a subpopulation, allele frequency in that subpopulation must be <0.00002 (0.002%). Please see supplementary information in manuscript supporting application of PM2 for ultra-rare alleles.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | Absent in population. Databases present at <0.00001 (0.001%) allele frequency in gnomAD or another large sequenced population. If multiple alleles are present within any subpopulation, allele frequency in that subpopulation must be <0.00002 (0.002%). | Disease-specific |

**Comparator note:** both thresholds are **strict** (`<`). PM2 is applied only at Supporting strength (PM2_Supporting).

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** **Not Applicable.**

> Comments: This rule is not applicable to PTEN.

No PM3 point system is defined by this VCEP.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

> PTEN EP Specification: For in-frame insertions or deletions, criteria may apply only if the variant impacts at least one residue in one of the catalytic motifs specified in the PM1 criteria. Criteria will also apply for variants resulting in protein extension.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. Applies to in-frame insertions or deletions impacting at least one residue in a catalytic motif (see PM1), and variants causing protein extension. | Disease-specific |
| **Supporting** | Not specified by VCEP. | — |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
Example: Arg156His is pathogenic; now you observe Arg156Cys.
Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

> PTEN EP Specifications:
> - This rule may be applied when the known variant is likely pathogenic unless applying would lead to a higher (pathogenic) classification for the variant being assessed.
> - The variant in question need not be novel but must have a BLOSUM62 (Henikoff 1992) score equal to or less than the known variant.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate** | Missense change at an amino acid residue where a different missense change determined to be pathogenic or likely pathogenic has been seen before. In addition, variant being interrogated must have BLOSUM62 score equal to or less than the known variant. | Disease-specific |

**Comparator note:** the BLOSUM62 comparison is **inclusive** ("equal to or less than"). The BLOSUM62 matrix distributed with this specification is transcribed in [Appendix D](#appendix-d--blosum62-matrix).

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:**

> PM6_Very Strong: Four or more occurrences of PM6 OR two occurrences of PM6 AND one occurrence of PS2.
>
> PM6_Strong: Two occurrences of PM6 OR occurrence of PM6 for an individual with a highly specific phenotype (meets criteria to count towards PS4).
>
> Of note, when PM6_S is applied for a single individual with phenotype specificity, the individual will not be counted towards PS4 as well.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Very Strong** | Two proven OR four assumed OR one proven + two assumed de novo observations in a patient with the disease and no family history. | Strength |
| **Strong** | Two probands with presumed de novo occurrence (maternity/paternity not confirmed) with the disease and no family history. May also be used for a proband with presumed de novo occurrence for an individual with a highly specific phenotype (meets criteria to count towards PS4). | Strength |
| **Moderate** | Assumed de novo, but without confirmation of paternity and maternity, in proband with the disease and no family history. | None |

**No de novo point matrix is defined by this VCEP** — escalation is by the observation counts above only.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

> PTEN EP Specification:
> - PP1: Requires 3 or 4 meioses in order to apply.
> - PP1_Strong: At least 7 meioses required across at least two families.
> - PP1_Moderate: Requires 5 or 6 meioses in order to apply.

#### Segregation Thresholds

| Strength | Meioses | Additional requirement | Modification Type |
|----------|---------|------------------------|-------------------|
| **Strong** | ≥ 7 (inclusive) | Across at least two families | Strength |
| **Moderate** | 5 or 6 | — | Strength |
| **Supporting** | 3 or 4 | — | Disease-specific |

The VCEP specifies meiosis counts only; it does not specify an LOD-score or likelihood-ratio segregation model.

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** No PTEN-specific specification text is given. The criterion is retained at its default strength with Modification Type "None".

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease. | None |

The PP3 and BP4 commentary notes that PP3/BP4 strengths were downgraded to supporting **because** the VCEP also applies PP2 for missense variants.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:**

> PTEN EP Specification: To be applied to synonymous or intronic variants where SpliceAl and VarSeak in silico models predict a splicing impact (SpliceAl: scores 0.5-1 are consider evidence of pathogenic. VarSeak: Class 4 and 5 are consider evidence of pathogenic). May also be applied to missense variants with REVEL score > 0.7.
>
> PTEN EP Commentary: Per Bayesian adaptation of the ACMG/AMP variant interpretation framework (Tavtigian et al., 2018), odds of pathogenicity (OddsPath) were estimated for various numbers of previously classified controls. When REVEL scores > 0.7 were used as evidence of pathogenic and < 0.5 were used as evidence of benign, the oddsPath was equated with moderate evidence strength for pathogenic conditions. Given that the VCEP also applies PP2 for missense variants, we decided to downgrade the evidence strength to be used at a supporting level.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting** | Multiple lines of computational evidence support a deleterious effect on the gene or gene product. Splicing variants: Concordance of SpliceAl and VarSeak. Missense variants: REVEL score > 0.7. | Disease-specific |

#### In silico thresholds

| Variant type | Tool | Threshold | Comparator |
|--------------|------|-----------|------------|
| Synonymous / intronic | SpliceAI (written "SpliceAl" in source) | scores 0.5–1 | inclusive range as written |
| Synonymous / intronic | VarSeak | Class 4 and 5 | categorical |
| Missense | REVEL | > 0.7 | **strict** |

Both splicing tools must agree ("Concordance of SpliceAl and VarSeak").

*Source note: "are consider evidence of pathogenic" is transcribed verbatim.*

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** **Not Applicable.**

> PTEN EP Commentary: Phenotype specificity has been incorporated into the rule specifications for PS4 Use 2.

No PP4 point system is defined; see [PS4](#ps4---prevalence-in-affected--phenotype-specificity).

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** **Not Applicable.**

> This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PubMed: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency Above Threshold

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:**

> To be applied for variants with filtering allele frequency >0.00056 (>0.056%) in gnomAD. Please see information in BS1 section for data supporting this cutoff.

| Strength | Criteria | Comparator | Modification Type |
|----------|----------|------------|-------------------|
| **Stand Alone** | gnomAD Filtering allele frequency >0.00056 (0.056%) | **strict** (`>`) | Disease-specific |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:**

> PTEN EP Specification:
> - BS1: To be applied for variants with filtering allele frequency of 0.000043 up to 0.00056 (0.0043% up to 0.056%) in gnomAD.
> - BS1_Supporting: To be applied for variants with filtering allele frequency of 0.0000043 up to 0.000043 (0.00043% up to 0.0043%) in gnomAD.
>
> BA1, BS1, and BS1_P thresholds are based on the approach published by Whiffin et al. (PMID 28518168) using the following values:
> - Prevalence: 1 in 9,000 (based on 15 disease-associated alleles present among the gnomAD population of ~135,000 individuals)
> - Allelic heterogeneity: 22/282 (based on prevalence of most common pathogenic PTEN variants, p.R130X and p.R335X, per Tan et al. PMID 21194675 and Bubien 2013 PMID 23335809)
> - Penetrance: 10% (overall cancer by age 40 for men with pathogenic germline PTEN variants is approximately 20% per Bubien 2013 PMID 23335809)
>
> Using these data points results in a BS1 value of 0.000043. BA1 was calculated by setting allelic heterogeneity to 1, and BS1_P by reducing BS1 by an order of magnitude.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | gnomAD Filtering allele frequency from 0.000043 (0.0043%) up to 0.00056 (0.056%) | Disease-specific |
| **Supporting** | Allele frequency from 0.0000043 (0.00043%) up to 0.000043 (0.0043%). | Disease-specific, Strength |

**Comparator note:** the VCEP expresses BS1 and BS1_Supporting as ranges using the words "of … up to" / "from … up to" rather than explicit operators. The lower bound is stated inclusively ("of 0.000043", "from 0.000043"). The upper bound operator is **not stated explicitly** by the VCEP; note that BA1 is defined strictly (`>0.00056`), so a filtering allele frequency of exactly 0.00056 does not meet BA1. Transcribed as written — the guideline does not substitute operators the source omits.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

> PTEN EP Specifications:
> - BS2: Variant must be observed in the homozygous state in a healthy or PHTS-unaffected individual. Two independent observations are required if the homozygous status is not confirmed via parental testing. If BS1 is also applied, this criteria will be applied at the supporting evidence level to avoid a variant reaching benign status solely based on homozygous occurrences due to high population frequency (BS1+BS2).
> - BS2_Supporting: Two homozygous observations with no clinical data provided, or meets criteria for BS2 but BS1 is also applied.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Observed in the homozygous state in a healthy or PHTS-unaffected individual. One observation if homozygous status confirmed, two if not confirmed. To be applied at supporting evidence level if BS1 is also applied. | Disease-specific |
| **Supporting** | Two homozygous observations with no clinical data provided, or meets criteria for BS2 but BS1 is also applied. | Disease-specific, Strength |

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

> PTEN EP Specifications:
> - BS3: For intronic or synonymous variants: RNA, mini-gene, or other assay demonstrate no impact on splicing.
> - BS3_Supporting: In vitro or in vivo functional study or studies showing no damaging effect on protein function.
>
> PTEN EP Specifications: BS3_supporting may be applied to the following assays:
> - Mighell et al. 2018 (PMID: 29706350): Massively parallel functional assay interrogating phosphatase activity.
>   - In the supplementary material (Table S2) search for the variant in columns A or B and make sure the variant in question is listed as TRUE under column I (high confidence). If not, do not use as evidence.
>   - Under column G, the cumulative score is listed. Apply BS3_supporting for all variants with scores > 0.
> - For missense variants: Other studies showing lipid phosphatase activity comparable to wild type in addition to a second assay appropriate to the protein domain demonstrating no statistically significant difference from wild type. Phosphatase assays for which criteria may be applied must include a catalytic dead control, such as p.C124S (NP_ 000305.3), as well as at least three biological replicates: Myers et al. 1998 (PMID: 9811831), Stambolic et al. 1998 (PMID: 9778245), Han et al. 2000 (PMID: 10866302), Rodriguez-Escudero et al. 2011 (PMID: 21828076), Costa et al. 2015 (PMID: 26504226), Malek et al. 2017 (PMID: 29056325)
> - Examples of second assays may include:
>   - Decreased PTEN or increased pAKT expression: Tan et al. 2011 (PMID: 21194675), Spinelli et al. 2015 (PMID: 25527629).
>   - Disruption of protein cellular localization: Lobo et al. 2009 (PMID: 19457929), He et al. 2012 (PMID: 22962422), Gil et al. 2015 (PMID: 25875300).
>   - Aberrant cellular phenotypes, including defective cell migration, proliferation, and invasion: Costa et al. 2015 (PMID: 26504226) Malek et al. 2017 (PMID: 29056325).

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Well-established in vitro or in vivo functional studies shows no damaging effect on protein function. To be applied to intronic or synonymous variants, RNA, mini-gene or other splicing assay demonstrating no splicing impact. | Disease-specific |
| **Supporting** | In vitro or in vivo functional study or studies showing no damaging effect on protein function. Phosphatase activity >0 per Mighell et al. 2018, PMID: 29706350. | Disease-specific, Strength |

**Comparator note:** the Mighell benign threshold is **strict** (`> 0`).

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.
Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

> PTEN EP Specification:
> - BS4: Two or more families are require for strong evidence level.
> - BS4_Supporting: Lack of segregation in one family.

*("are require" is transcribed verbatim from the source.)*

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong** | Lack of segregation in affected members of two or more families. | Disease-specific |
| **Supporting** | Lack of segregation in affected members of one family. | Disease-specific, Strength |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | "This rule is not applicable to PTEN." |
| **BP2** | Specified (Supporting; Disease-specific) | Observed in trans with a pathogenic or likely pathogenic PTEN variant OR at least three observations in cis and/or phase unknown with different pathogenic/likely pathogenic PTEN variants. |
| **BP3** | Not Applicable | "This rule is not applicable to PTEN." |
| **BP4** | Specified (Supporting; Disease-specific) | Multiple lines of computational evidence suggest no impact on gene or gene product. Splicing variants: Concordance of SpliceAl and VarSeak. Missense variants: REVEL scores < 0.5. |
| **BP5** | Specified (Supporting; Disease-specific) | Variant found in a case with an alternate molecular basis for disease. Other gene/disorder must be considered highly penetrant AND patient's personal/family history must demonstrate no overlap between other gene and PTEN. |
| **BP6** | Not Applicable | "This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee." (PubMed: 29543229) |
| **BP7** | Specified (Supporting; Disease-specific) | A synonymous (silent) or intronic variant at or beyond +7/-21 for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice. |

#### BP2 — full VCEP text

> PTEN EP Specifications: The other variant may be either pathogenic or likely pathogenic. This rule may also be applied for at least three observations of the variant in cis or unknown phase with different pathogenic or likely pathogenic PTEN variants.

#### BP4 — full VCEP text

> PTEN EP Specification: To be applied to synonymous or intronic variants where SpliceAl and VarSeak in silico models predict no splicing impact (SpliceAl: scores 0-0.2 are considered evidence of benign. VarSeak: Class 1 and 2 are considered evidence of benign). Not to be applied for variants which may impact the intron 1 splice donor or acceptor sites, and to be used cautiously for variants which may impact the intron 6 splice acceptor. May also be applied to missense variants with REVEL score < 0.5.
>
> PTEN EP Commentary: Per Bayesian adaptation of the ACMG/AMP variant interpretation framework (Tavtigian et al., 2018), odds of pathogenicity (OddsPath) were estimated for various numbers of previously classified controls. When REVEL scores > 0.7 were used as evidence of pathogenic and < 0.5 were used as evidence of benign, the oddsPath was equated with moderate evidence strength for benign conditions. Given that the VCEP also applies PP2 for missense variants, we decided to downgrade the evidence strength to be used at a supporting level.

| Variant type | Tool | Threshold | Comparator |
|--------------|------|-----------|------------|
| Synonymous / intronic | SpliceAI (written "SpliceAl" in source) | scores 0–0.2 | inclusive range as written |
| Synonymous / intronic | VarSeak | Class 1 and 2 | categorical |
| Missense | REVEL | < 0.5 | **strict** |

BP4 exclusions stated by the VCEP: not to be applied for variants which may impact the intron 1 splice donor or acceptor sites; to be used cautiously for variants which may impact the intron 6 splice acceptor.

#### BP5 — full VCEP text

> PTEN EP Specifications: At least two such cases are required for criteria to apply. In addition, the other gene/disorder must be considered highly penetrant AND the patient's personal/family history must demonstrate no overlap between the other gene and PTEN.

*Note: the VCEP narrative requires at least two such cases, but the strength-level summary text for BP5 does not restate that requirement.*

#### BP7 — full VCEP text

> PTEN EP Specification: Intronic variants must be positioned at or beyond +7/-21.

**Comparator note:** the intronic position boundary is **inclusive** ("at or beyond +7/-21").

---

## Frequency Threshold Summary

All values are gnomAD **filtering allele frequency** unless noted. Comparators are as written by the VCEP.

| Criterion | Threshold | Comparator as written |
|-----------|-----------|-----------------------|
| **BA1** (Stand Alone) | 0.00056 (0.056%) | **strict**: `> 0.00056` |
| **BS1** (Strong) | 0.000043 up to 0.00056 (0.0043% up to 0.056%) | lower bound inclusive ("from"/"of"); upper bound operator not stated by the VCEP |
| **BS1_Supporting** | 0.0000043 up to 0.000043 (0.00043% up to 0.0043%) | lower bound inclusive ("from"/"of"); upper bound operator not stated by the VCEP |
| **PM2_Supporting** (overall) | 0.00001 (0.001%) — gnomAD or another large sequenced population; this is a raw allele frequency, not stated as a filtering AF | **strict**: `< 0.00001` |
| **PM2_Supporting** (subpopulation, when multiple alleles present in a subpopulation) | 0.00002 (0.002%) | **strict**: `< 0.00002` |

Derivation basis for BA1/BS1/BS1_Supporting (Whiffin et al., PMID 28518168): prevalence 1 in 9,000; allelic heterogeneity 22/282; penetrance 10%. BA1 was calculated by setting allelic heterogeneity to 1; BS1_Supporting by reducing BS1 by an order of magnitude.

---

## Rules for Combining Criteria

This VCEP **does** publish combining rules. Two source statements exist and are both reproduced below.

### A. Combining rules as listed in the specification document

**Pathogenic**

- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong, PM6_Very Strong) AND ≥ 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong)
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong, PM6_Very Strong) AND ≥ 2 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong, PM6_Very Strong) AND 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) AND 1 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP2, PP3)
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong, PM6_Very Strong) AND ≥ 2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP2, PP3)
- ≥ 2 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong) AND ≥ 3 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong) AND 2 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) AND ≥ 2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP2, PP3)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong) AND 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) AND ≥ 4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP2, PP3)

**Likely Pathogenic**

- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong, PM6_Very Strong) AND 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong) AND 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong) AND ≥ 2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP2, PP3)
- ≥ 3 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)
- 2 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) AND ≥ 2 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP2, PP3)
- 1 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) AND ≥ 4 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP2, PP3)
- 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM6_Strong, PP1_Strong) AND 2 Moderate (PVS1_Moderate, PS3_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate)
- 1 Very Strong (PVS1, PS2_Very Strong, PS4_Very Strong, PM6_Very Strong) AND 1 Supporting (PS3_Supporting, PS4_Supporting, PM2_Supporting, PP1, PP2, PP3)

**Benign**

- ≥ 2 Strong (BS1, BS2, BS3, BS4)
- 1 Stand Alone (BA1)

**Likely Benign**

- ≥ 2 Supporting (BS1_Supporting, BS2_Supporting, BS3_Supporting, BS4_Supporting, BP2, BP4, BP5, BP7)
- 1 Strong (BS1, BS2, BS3, BS4)

### B. Combining rules as stated in the distributed supplementary file "RULES FOR COMBINING CRITERIA FOR CLASSIFICATION"

> **RULES FOR COMBINING CRITERIA FOR CLASSIFICATION**
>
> Variants will be classified per Richards et al., 2015 with the following exceptions:
> - 1 Benign Strong (BS) = Likely Benign.
> - 1 Pathogenic Very Strong (PVS) + 1 Pathogenic Supporting (PP) = Likely Pathogenic.
> - Variants with conflicting evidence may be classified using the Bayesian points system (Tavtigian et al., 2018).

**Note:** the supplementary file permits the use of the Bayesian points system (Tavtigian et al., 2018) for variants with conflicting evidence but **does not reproduce a points table**. This VCEP does not publish its own points-per-strength ladder; if the Bayesian points system is used, consult Tavtigian et al. 2018 (PMID 29300386) directly. No points ladder is asserted here.

---

## Appendices

### Appendix A — PTEN PVS1 Decision Tree

Transcribed from the distributed supplementary file `PVS1_DecisionTree.pdf` (1 page, titled "PVS1 decision tree").

**Branch 1 — Nonsense or Frameshift**

| Variant situation | Intermediate condition | Outcome |
|---|---|---|
| Predicted to undergo NMD: stop codon or disruption at or 5' to p.D375 (c.1121) | Exon is present in biologically-relevant transcript NM_000314.8 | **PVS1** |
| Not predicted to undergo NMD: stop codon 3' to p.D375 (c.1121) | Role of region in protein function is unknown → LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) → Variant removes <10% of protein | **PVS1_Moderate** |

**Branch 2 — GT--AG 1,2 splice sites** *(the tree carries a superscript footnote marker "a" on this branch label; no footnote text is present anywhere in the distributed file)*

| Variant situation | Intermediate condition | Outcome |
|---|---|---|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD; stop codon or disruption at or 5' to p.D375 (c.1121) | Exon is present in biologically-relevant transcript NM_000314.8 | **PVS1** |
| Exon skipping or use of a cryptic splice site preserves reading frame | Truncated/altered region is critical to protein function (entire exon 3, 8 OR 9) | **PVS1_Strong** |

**Branch 3 — Deletion (single exon to full gene)**

| Variant situation | Intermediate condition | Outcome |
|---|---|---|
| Full gene deletion | — (direct) | **PVS1** |
| Single (deletion of exon 1, 2, 4, 5, 6 OR 7) to multi exon deletion — disrupts reading frame and is predicted to undergo NMD | Exon is present in biologically-relevant transcript(s) NM_000314.8 | **PVS1** |
| Single exon deletion — preserves reading frame (exon 3, 8 OR 9) | Truncated/altered region is critical to protein function (entire exon 3, 8 OR 9) | **PVS1_Strong** |

**Branch 4 — Duplication** (≥1 exon in size and must be completely contained within gene)

| Phase | Reading frame / NMD condition | Outcome |
|---|---|---|
| Proven in tandem | Reading frame disrupted and NMD predicted to occur | **PVS1** |
| Proven in tandem | No or unknown impact on reading frame and NMD | **N/A** |
| Proven in tandem | Reading frame disrupted and NMD not predicted to occur (tandem duplication of Exon 3 or 8) | **PVS1_Strong** |
| Presumed in tandem | Reading frame presumed disrupted and NMD predicted to occur | **PVS1_Strong** |
| Presumed in tandem | No or unknown impact on reading frame and NMD | **N/A** |
| Presumed in tandem | Reading frame presumed disrupted and NMD not predicted to occur (tandem duplication of exon 3 or 8) | **PVS1_Moderate** |
| Proven not in tandem | — (direct) | **N/A** |

**Branch 5 — Initiation Codon**

| Variant situation | Outcome |
|---|---|
| Initiation codon variant | **PVS1** |

---

### Appendix B — Cleveland Clinic Score (Adults)

Transcribed from the distributed supplementary file `Cleveland Clinic score.png`. Used for the adult arm of the PS4 phenotype specificity score (CC score ≥ 30 → 1 point per proband; CC score 25–29 → 0.5 points per proband). Reference: Tan et al. 2011 (PMID 21194675).

| Category | Feature | Score |
|----------|---------|-------|
| **Neurological** | Macrocephaly | 6 |
| Neurological | Extreme macrocephaly (men: ≥63 cm, women: ≥60 cm) | 10 |
| Neurological | Lhermitte-Duclos disease | 10 |
| Neurological | Autism/developmental delay | 1 |
| **Skin** | Trichilemmoma (biopsy-proven) | 10 |
| Skin | Oral papillomas | 6 |
| Skin | Penile freckling | 6 |
| Skin | Acral keratoses | 1 |
| Skin | Lipoma | 1 |
| Skin | Arteriovenous malformation | 6 |
| **Gastrointestinal** | ≥5 gastrointestinal polyps, any type | 6 |
| Gastrointestinal | Hamartoma or ganglioneuroma | 10 |
| Gastrointestinal | Glycogenic acanthosis | 10 |
| **Breast** | Cancer dx <40 yrs | 4 |
| Breast | Cancer dx 40-49 yrs | 2 |
| Breast | Cancer dx ≥50 yrs | 1 |
| Breast | Fibrocystic breast disease | 1 |
| **Thyroid** | Cancer dx <20 yrs | 10 |
| Thyroid | Cancer dx 20-49 yrs | 4 |
| Thyroid | Cancer dx ≥50 yrs | 1 |
| Thyroid | Goiter, nodules, or Hashimoto's thyroiditis | 4 |
| **Genitourinary** | Endometrial cancer dx 20-29 yrs | 10 |
| Genitourinary | Endometrial cancer dx 30-49 yrs | 6 |
| Genitourinary | Endometrial cancer dx ≥50 yrs | 1 |
| Genitourinary | Uterine fibroids | 1 |
| Genitourinary | Renal cell carcinoma | 1 |

The source table renders the "≥" symbol as an underlined ">" (e.g. "men: >63 cm", "Cancer dx >50 yrs", ">5 gastrointestinal polyps"); the v3.2 release notes describe this as "added underscores for some greater than symbols". Rendered as ≥ here. The table as distributed carries no explicit total-score row or age qualifiers beyond those shown.

---

### Appendix C — PTEN Phenotype Scoring for Pediatric Patients

Transcribed from the distributed supplementary file `PTEN Phenotype Scoring for Pediatric Patients.png`, captioned "TABLE 2 PTEN phenotype scoring for pediatric patients". Used for the pediatric arm of the PS4 phenotype specificity score (score ≥ 5 → 1 point per proband; score = 4 → 0.5 points per proband, with autism/DD/ID not contributing).

| Feature | Score (points) |
|---------|----------------|
| Macrocephaly of >2 SD to <4 SD | 2 |
| Extreme macrocephaly (≥4 SD) | 3 |
| PTEN-specific MRI characteristics (dilated Virchow-Robin, prominent perivascular spaces) | 2 |
| Autism/developmental delay (DD)/intellectual disability (ID) | 2 |
| Penile freckling | 3 |
| Lipoma | 1 |
| Oral papilloma | 3 |
| Hamartomatous polyp(s) | 3 |
| Arteriovenous malformation/hemangioma | 2 |
| Thyroid cancer | 3 |
| Thyroid nodule/Hashimoto's thyroiditis | 2 |

Note the macrocephaly bands are stated with strict comparators on both ends (">2 SD to <4 SD") while extreme macrocephaly is inclusive ("≥4 SD"); a value of exactly 2 SD is therefore not covered by the table as distributed.

---

### Appendix D — BLOSUM62 Matrix

Transcribed from the distributed supplementary file `BLOSUM matrix.png` (lower-triangular form, as distributed). Used for PM5: the variant being interrogated must have a BLOSUM62 score **equal to or less than** the known pathogenic/likely pathogenic variant at the same residue. Reference: Henikoff & Henikoff 1992 (PMID 1438297).

|  | Ala | Arg | Asn | Asp | Cys | Gln | Glu | Gly | His | Ile | Leu | Lys | Met | Phe | Pro | Ser | Thr | Trp | Tyr | Val |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Ala** | 4 | | | | | | | | | | | | | | | | | | | |
| **Arg** | −1 | 5 | | | | | | | | | | | | | | | | | | |
| **Asn** | −2 | 0 | 6 | | | | | | | | | | | | | | | | | |
| **Asp** | −2 | −2 | 1 | 6 | | | | | | | | | | | | | | | | |
| **Cys** | 0 | −3 | −3 | −3 | 9 | | | | | | | | | | | | | | | |
| **Gln** | −1 | 1 | 0 | 0 | −3 | 5 | | | | | | | | | | | | | | |
| **Glu** | −1 | 0 | 0 | 2 | −4 | 2 | 5 | | | | | | | | | | | | | |
| **Gly** | 0 | −2 | 0 | −1 | −3 | −2 | −2 | 6 | | | | | | | | | | | | |
| **His** | −2 | 0 | 1 | −1 | −3 | 0 | 0 | −2 | 8 | | | | | | | | | | | |
| **Ile** | −1 | −3 | −3 | −3 | −1 | −3 | −3 | −4 | −3 | 4 | | | | | | | | | | |
| **Leu** | −1 | −2 | −3 | −4 | −1 | −2 | −3 | −4 | −3 | 2 | 4 | | | | | | | | | |
| **Lys** | −1 | 2 | 0 | −1 | −3 | 1 | 1 | −2 | −1 | −3 | −2 | 5 | | | | | | | | |
| **Met** | −1 | −1 | −2 | −3 | −1 | 0 | −2 | −3 | −2 | 1 | 2 | −1 | 5 | | | | | | | |
| **Phe** | −2 | −3 | −3 | −3 | −2 | −3 | −3 | −3 | −1 | 0 | 0 | −3 | 0 | 6 | | | | | | |
| **Pro** | −1 | −2 | −2 | −1 | −3 | −1 | −1 | −2 | −2 | −3 | −3 | −1 | −2 | −4 | 7 | | | | | |
| **Ser** | 1 | −1 | 1 | 0 | −1 | 0 | 0 | 0 | −1 | −2 | −2 | 0 | −1 | −2 | −1 | 4 | | | | |
| **Thr** | 0 | −1 | 0 | −1 | −1 | −1 | −1 | −2 | −2 | −1 | −1 | −1 | −1 | −2 | −1 | 1 | 5 | | | |
| **Trp** | −3 | −3 | −4 | −4 | −2 | −2 | −3 | −2 | −2 | −3 | −2 | −3 | −1 | 1 | −4 | −3 | −2 | 11 | | |
| **Tyr** | −2 | −2 | −2 | −3 | −2 | −1 | −2 | −3 | 2 | −1 | −1 | −2 | −1 | 3 | −3 | −2 | −2 | 2 | 7 | |
| **Val** | 0 | −3 | −3 | −3 | −1 | −2 | −2 | −3 | −3 | 3 | 1 | −2 | 1 | −1 | −2 | −2 | 0 | −3 | −1 | 4 |

The matrix as distributed covers the 20 standard amino acids only; it contains no rows for Asx (B), Glx (Z), Xaa (X) or stop.

---

## Criteria Status Summary

| Criterion | Status | Strengths available |
|-----------|--------|---------------------|
| PVS1 | Specified | Very Strong / Strong / Moderate (per decision tree) |
| PS1 | Specified | Strong |
| PS2 | Specified | Very Strong / Strong |
| PS3 | Specified | Strong / Moderate / Supporting |
| PS4 | Specified | Very Strong / Strong / Moderate / Supporting |
| PM1 | Specified | Moderate |
| PM2 | Specified | Supporting only |
| PM3 | **Not Applicable** | — |
| PM4 | Specified | Moderate |
| PM5 | Specified | Moderate |
| PM6 | Specified | Very Strong / Strong / Moderate |
| PP1 | Specified | Strong / Moderate / Supporting |
| PP2 | Specified (no gene-specific modification) | Supporting |
| PP3 | Specified | Supporting |
| PP4 | **Not Applicable** (folded into PS4 Use 2) | — |
| PP5 | **Not Applicable** (SVI recommendation) | — |
| BA1 | Specified | Stand Alone |
| BS1 | Specified | Strong / Supporting |
| BS2 | Specified | Strong / Supporting |
| BS3 | Specified | Strong / Supporting |
| BS4 | Specified | Strong / Supporting |
| BP1 | **Not Applicable** | — |
| BP2 | Specified | Supporting |
| BP3 | **Not Applicable** | — |
| BP4 | Specified | Supporting |
| BP5 | Specified | Supporting |
| BP6 | **Not Applicable** (SVI recommendation) | — |
| BP7 | Specified | Supporting |

---

## References

As listed in the specification:

1. Costa HA, Leitner MG et al. Discovery and functional characterization of a neomorphic PTEN mutation. Proc Natl Acad Sci U S A (2015) 112 (45) p. 13976-81. doi:10.1073/pnas.1422504112 — PMID 26504226
2. Gil A, Rodríguez-Escudero I et al. A functional dissection of PTEN N-terminus: implications in PTEN subcellular targeting and tumor suppressor activity. PLoS One (2015) 10 (4) p. e0119287. doi:10.1371/journal.pone.0119287 — PMID 25875300
3. Han SY, Kato H et al. Functional evaluation of PTEN missense mutations using in vitro phosphoinositide phosphatase assay. Cancer Res (2000) 60 (12) p. 3147-51. — PMID 10866302
4. He X, Saji M et al. PTEN lipid phosphatase activity and proper subcellular localization are necessary and sufficient for down-regulating AKT phosphorylation in the nucleus in Cowden syndrome. J Clin Endocrinol Metab (2012) 97 (11) p. E2179-87. doi:10.1210/jc.2012-1991 — PMID 22962422
5. Henikoff S, Henikoff JG. Amino acid substitution matrices from protein blocks. Proc Natl Acad Sci U S A (1992) 89 (22) p. 10915-9. doi:10.1073/pnas.89.22.10915 — PMID 1438297
6. Lobo GP, Waite KA et al. Germline and somatic cancer-associated mutations in the ATP-binding motifs of PTEN influence its subcellular localization and tumor suppressive function. Hum Mol Genet (2009) 18 (15) p. 2851-62. doi:10.1093/hmg/ddp220 — PMID 19457929
7. Malek M, Kielkowska A et al. PTEN Regulates PI(3,4)P(2) Signaling Downstream of Class I PI3K. Mol Cell (2017) 68 (3) p. 566-580.e10. doi:10.1016/j.molcel.2017.09.024 — PMID 29056325
8. Mighell TL, Evans-Dutson S et al. A Saturation Mutagenesis Approach to Understanding PTEN Lipid Phosphatase Activity and Genotype-Phenotype Relationships. Am J Hum Genet (2018) 102 (5) p. 943-955. doi:10.1016/j.ajhg.2018.03.018 — PMID 29706350
9. Myers MP, Pass I et al. The lipid phosphatase activity of PTEN is critical for its tumor supressor function. Proc Natl Acad Sci U S A (1998) 95 (23) p. 13513-8. doi:10.1073/pnas.95.23.13513 — PMID 9811831
10. Richards S, Aziz N et al. Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology. Genet Med (2015) 17 (5) p. 405-24. doi:10.1038/gim.2015.30 — PMID 25741868
11. Rodríguez-Escudero I, Oliver MD et al. A comprehensive functional analysis of PTEN mutations: implications in tumor- and autism-related syndromes. Hum Mol Genet (2011) 20 (21) p. 4132-42. doi:10.1093/hmg/ddr337 — PMID 21828076
12. Spinelli L, Black FM et al. Functionally distinct groups of inherited PTEN mutations in autism and tumour syndromes. J Med Genet (2015) 52 (2) p. 128-34. doi:10.1136/jmedgenet-2014-102803 — PMID 25527629
13. Stambolic V, Suzuki A et al. Negative regulation of PKB/Akt-dependent cell survival by the tumor suppressor PTEN. Cell (1998) 95 (1) p. 29-39. doi:10.1016/s0092-8674(00)81780-8 — PMID 9778245
14. Tavtigian SV, Greenblatt MS et al. Modeling the ACMG/AMP variant classification guidelines as a Bayesian classification framework. Genet Med (2018) 20 (9) p. 1054-1060. doi:10.1038/gim.2017.210 — PMID 29300386
15. Tan MH, Mester J et al. A clinical scoring system for selection of patients for PTEN mutation testing is proposed on the basis of a prospective study of 3042 probands. Am J Hum Genet (2011) 88 (1) p. 42-56. doi:10.1016/j.ajhg.2010.11.013 — PMID 21194675

Additional PMIDs cited in criterion text but not in the specification's reference list: 30192042 (Tayoun et al. 2018, PVS1), 29543229 (SVI VCEP Review Committee, PP5/BP6), 28518168 (Whiffin et al., BA1/BS1), 23335809 (Bubien 2013, BS1 derivation). "(Lee 1999)" is cited in PM1 without a corresponding reference entry.

---

## Version History

Release notes as published with version 3.2 (Released 4/6/2026):

> **Minor Changes:**
> 1. Added disease name and MOI
> 2. Updated PS3 and PS4 < and > signs to ≥ or ≤ if necessary

General Comments field of the same release:

> Minor Changes: 1. Correct SpliceAI cutoff for BP4 rule 2. Correct the Rules for Combining Criteria 3. Add BLOSUM matrix, Cleveland Clinic core and Pediatric score tables 4. Added disease name, MOI and added underscores for some greater than symbols

The specification document carries no history for versions prior to 3.2.

---

*This document was compiled from the ClinGen VCEP specification (GN003, PTEN v3.2) and all five of its distributed supplementary files. Content not present in those sources is marked "Not specified by VCEP" rather than filled in from generic ACMG/AMP or SVI guidance. For the most current version, please refer to the ClinGen website.*
