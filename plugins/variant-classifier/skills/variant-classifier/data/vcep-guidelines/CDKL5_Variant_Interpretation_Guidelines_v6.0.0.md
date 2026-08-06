# Comprehensive Variant Interpretation Guidelines for CDKL5

## ClinGen Rett and Angelman-like Disorders Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for CDKL5 (Version 6.0)

**Affiliation:** Rett and Angelman-like Disorders VCEP
**Version:** 6.0
**Released:** 5/1/2026
**DOI:** 10.5281/zenodo.21421679
**Type:** Richards et al., 2015 - Combining rules
**Specification ID:** GN034
**Rights Holder:** The Clinical Genome Resource (ClinGen)

**Release Notes (v6.0):**
- 1 Strong AND 3 Supporting added to benign criteria code.
- 1 Strong added to likely benign criteria code.

---

## Table of Contents

1. [Gene and Disease Information](#1-gene-and-disease-information)
2. [Pathogenic Criteria](#2-pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PS4 - Prevalence in Affected](#ps4---prevalence-in-affected)
   - [PM1 - Mutational Hot Spot](#pm1---mutational-hot-spot)
   - [PM2 - Absent from Controls](#pm2---absent-from-controls)
   - [PM3 - In Trans with Pathogenic Variant](#pm3---in-trans-with-pathogenic-variant)
   - [PM4 - Protein Length Changes](#pm4---protein-length-changes)
   - [PM5 - Novel Missense at Same Residue](#pm5---novel-missense-at-same-residue)
   - [PM6 - De Novo (Assumed)](#pm6---de-novo-assumed)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP2 - Missense in Constrained Gene](#pp2---missense-in-constrained-gene)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
   - [PP4 - Phenotype Specificity](#pp4---phenotype-specificity)
   - [PP5 - Reputable Source](#pp5---reputable-source)
3. [Benign Criteria](#3-benign-criteria)
   - [BA1 - Stand-Alone Benign](#ba1---stand-alone-benign)
   - [BS1 - Allele Frequency Greater Than Expected](#bs1---allele-frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (Benign)](#bs3---functional-studies-benign)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP1 - Missense in Truncating Disease Gene](#bp1---missense-in-truncating-disease-gene)
   - [BP2 - In Trans / In Cis with Pathogenic](#bp2---in-trans--in-cis-with-pathogenic)
   - [BP3 - In-Frame Indel in Repetitive Region](#bp3---in-frame-indel-in-repetitive-region)
   - [BP4 - Computational Evidence (Benign)](#bp4---computational-evidence-benign)
   - [BP5 - Alternate Molecular Basis](#bp5---alternate-molecular-basis)
   - [BP6 - Reputable Source (Benign)](#bp6---reputable-source-benign)
   - [BP7 - Synonymous Variants](#bp7---synonymous-variants)
4. [Not Applicable Criteria](#4-not-applicable-criteria)
5. [Rules for Combining Criteria](#5-rules-for-combining-criteria)
6. [Appendices](#6-appendices)

---

## 1. Gene and Disease Information

| Parameter | Value |
|-----------|-------|
| **Gene** | CDKL5 (HGNC:11411) |
| **HGNC Name** | cyclin dependent kinase like 5 |
| **Reference Transcript** | NM_001323289.2 |
| **Disease** | CDKL5 disorder |
| **MONDO ID** | MONDO:0100039 |
| **Mode of Inheritance** | X-linked inheritance |

**Keywords (from specification):** human biology genomics variant, variant classification, clingen, disease standards, CDKL5, NM_001323289.2, X-linked inheritance, CDKL5 disorder

**Transcript note:** The specification refers to two transcripts. NM_001323289.2 is the major brain isoform (which has an alternative C-terminus) and is the transcript listed for the specification and the PVS1 flowchart. NM_003159.2 is referred to as "the historically used transcript" in several criteria.

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats (original ACMG):**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

#### VCEP Specifications

Refer to PVS1 flow chart for additional guidance (see [Appendix A](#appendix-a-pvs1-flowchart-for-cdkl5)).

Additional notes:
- Do not use PVS1 for truncating variants in *CDKL5* C-terminus (exons 19-21, or after p.P904) **when using the historically used transcript (NM_003159.2).**
- *CDKL5* has non-coding exons. There is evidence that loss of just non-coding *CDKL5* exon 1 is pathogenic given previous de novo finding in patients affected with CDKL5-disease (GeneDx internal data); therefore, for losses involving just *CDKL5* exon 1, PVS1 can be applied.

For intragenic deletions/duplications that are predicted to result in a product that preserves reading frame:
- For single exon in-frame deletions assign the same strength (PVS1, PVS1_strong, or PVS1_moderate) as for splice site variants that preserve reading frame indicated above
- For multiple exon in-frame deletions, PVS1 can be assigned to deletions that include single in-frame exons in the PVS1 category (listed above) **OR** if the exon contains a functionally important domain as specified in PM1
- Given the extensive data available for *CDKL5*, classifications for single or multi-exon in-frame deletions are assigned as PVS1 or PVS1_strong. Exceptions are *CDKL5* exon 17 (as described above) due to a limited number of pathogenic variants reported to date.

#### Strength Levels

| Strength | Application |
|----------|-------------|
| **PVS1** (Very Strong) | Null variants up to p.R948 **when using the major brain isoform which has an alternative C-terminus (NM_001323289.2)**; Frameshift variants that result in a read-through of the stop codon; Canonical splice site variants predicted to result in an out-of-frame product; Canonical splice site variants or single in-frame deletions predicted to preserve the reading frame (exons 7, 10, 13) and for the non-coding CDKL5 exon (exon 1) **(NM_001323289.2)**; In-frame deletions including the PM1 functional domains (p.V19_K43 ATP binding domain or p.T169_Y171 TEY phosphorylation domain); Deletions and duplications ≥1 exon in size (that are completely contained within the CDKL5 gene) where the reading frame is disrupted and NMD is predicted to occur; A full gene deletion |
| **PVS1_Strong** | Cannonical [*sic*] splice site variants that flank exon 18 **(the final exon of NM_001323289.2)**; Single to multi exon deletions that disrupt the reading frame such that exon 18 **(the final exon of NM_001323289.2)** is truncated/altered; Duplications ≥1 exon in size (that are completely contained within the CDKL5 gene) where the reading frame is presumed to be disrupted and NMD is predicted to occur |
| **PVS1_Moderate** | Any truncating variant distal of p.R948 (**when using the major brain isoform, NM_001323289.2**); Canonical splice site variants that flank exon 17 (in-frame exon) (**NM_001323289.2**) |
| **PVS1_Supporting** | Applicable for initiation codon variants in *CDKL5*. |

**Modification Type:** Disease-specific (Very Strong, Strong); Disease-specific, Strength (Moderate, Supporting)

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.
*Example:* Val->Leu caused by either G>C or G>T in the same codon.
*Caveat:* Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PS1** (Strong) | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. |

**Modification Type:** None

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.
*Note:* Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### VCEP Specifications

Applicable to all genes in affected individuals identified as mosaic for the variant (as the presence of a variant in the mosaic state is confirmatory of the variant being de novo). Because of the very high de novo rate of pathogenic variants in *CDKL5*, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

| Strength | Application |
|----------|-------------|
| **PS2_Very Strong** | ≥2 independent occurrences of PS2. **OR** ≥2 independent occurrences of PM6 and one occurrence of PS2. |
| **PS2** (Strong) | 1 occurrence of PS2. |

**Modification Type:** No change (Very Strong); None (Strong)

**Note:** The specification does not define PS2 at Moderate or Supporting strength — Not specified by VCEP.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.
*Note:* Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PS3** (Strong) | RNA studies that demonstrate abnormal splicing and an out-offrame [*sic*] transcript. Do not use for canonical splice site variants and when PVS1 is used. |
| **PS3_Supporting** | RNA studies that demonstrate abnormal splicing and an inframe product (unless it affects an in-frame exon specified in the PVS1 section). See included table for acceptable functional studies. |

**Modification Type:** Disease-specific

**Note:** PS3 at Moderate strength is not specified by the VCEP.

#### Approved Functional Assays (CDKL5 Functional Assays supplementary table)

| Name of assay | Measured Parameter | Expected Deleterious Result Range (PS3_Supporting) | Expected Benign Result Range (BS3) | References |
|---|---|---|---|---|
| In vitro autophosphorylation assays | Auto-phosphorylation of CDKL5 | Absence of auto-phosphorylation | Not recommended | PMID: 16935860 |
| In vitro phosphorylation-TEY assay | Phosphorylation of TEY motif | Absence of phosphorylation | Not recommended | PMID: 16935860 |
| Subcellular localization assay | Subcellular distribution | Unidentifiable with Hoechst staining and localizes partially within the cytoplasm | Not recommended | PMID: 16935860 |
| In vitro kinase assay | Enzymatic activity of CDKL5 | Absence of phosphorylation of CDKL5 substrates (MeCP2 and Dnmt1) | Not recommended | PMID: 27265524, 16935860 |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
*Note 1:* Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
*Note 2:* In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

#### VCEP Specifications

- Detailed phenotype not needed. Need to confirm patient is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.
- Patient can be published OR an internal case OR observed at an outside lab (i.e. via ClinVar) OR described in the reputable databases (RettBASE). However independent case has to be confirmed to be a different patient than yours (compare gender/age).
- Do not use this criterion for variants where BS1 is applied or where PM2 does not apply.

| Strength | Application |
|----------|-------------|
| **PS4** (Strong) | 5+ observations. |
| **PS4_Moderate** | 3-4 observations. |
| **PS4_Supporting** | Use for 2nd independent occurrence. |

**Modification Type:** Strength

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PM1** (Moderate) | ATP binding region: aa 19-43; TEY phosphorylation site: aa 169-171 (references 1, 4, 2, 3) |

**Modification Type:** Disease-specific

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes, or Exome Aggregation Consortium.
*Caveat:* Population data for indels may be poorly called by next generation sequencing.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PM2_Supporting** | Absent/rare from controls in an ethnically-matched cohort population sample. Use if absent, zero observations in control databases. |

**Modification Type:** Strength

---

### PM3 - In Trans with Pathogenic Variant

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.
*Note:* This requires testing of parents (or offspring) to determine phase.

**Status:** **Not Applicable.** Comment: "Not applicable for CDKL5."

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PM4** (Moderate) | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. Do not use for in-frame deletions/insertions in CDKL5 C-terminus (exons 19-21, or after p.P904) **(when using the NM_003159.2 transcript)**. |
| **PM4_Supporting** | Smaller in-frame events (< 3 amino acid residues) unless they occur in a functionally important region (see PM1 for functionally important domains for each gene). |

**Modification Type:** Disease-specific (Moderate); Strength (Supporting)

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.
*Example:* Arg156His is pathogenic; now you observe Arg156Cys.
*Caveat:* Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PM5_Strong** | ≥2 different missense changes affecting the amino acid residue. Do not apply PM1 in these situations. |
| **PM5** (Moderate) | Applicable to all genes as written. A Grantham or BLOSUM score comparison can be used to determine if the variant is predicted to be as or more damaging than the established pathogenic variant. |

**Modification Type:** Strength (Strong); None (Moderate)

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

#### VCEP Specifications

Because of the very high de novo rate of pathogenic variants in *CDKL5*, de novo observation can be attributed the highest value points per proband (2 points for confirmed de novo and 1 point for assumed de novo) if the patient is known to be affected with a neurodevelopmental phenotype consistent with the gene.

| Strength | Application |
|----------|-------------|
| **PM6_Very Strong** | ≥4 independent occurrences of PM6. Evidence from literature must be fully evaluated to support independent events. |
| **PM6_Strong** | ≥2 independent occurrences of PM6. Evidence from literature must be fully evaluated to support independent events. |
| **PM6** (Moderate) | 1 occurrence of PM6. |

**Modification Type:** Strength (Very Strong, Strong); None (Moderate)

**Note:** The strength-level descriptors for PM6 in the source specification read "Confirmed de novo without confirmation of paternity and maternity" — reproduced verbatim.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.
*Note:* May be used as stronger evidence with increasing segregation data.

#### VCEP Specifications

Note: individuals must have disease consistent with reported phenotype (even if on the mild end of spectrum of the disease).

| Strength | Application |
|----------|-------------|
| **PP1_Strong** | ≥5 informative meiosis |
| **PP1_Moderate** | 3-4 informative meiosis |
| **PP1** (Supporting) | 2 informative meiosis |

**Modification Type:** Strength

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**Status:** **Not Applicable.** Comment: "Not applicable for CDKL5."

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).
*Caveat:* As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PP3** (Supporting) | For missense variants use REVEL with a score ≥ 0.644. For splice site variants use SpliceAI with a score ≥ 0.2. |

**Modification Type:** General recommendation

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **PP4** (Supporting) | Phenotype specific for disease with single genetic etiology. See gene specific clinical phenotype guidelines (below). |

**Modification Type:** Disease-specific

**Note:** No point-based PP4 system is defined in this specification — Not specified by VCEP. PP4 is available at Supporting strength only.

#### CDKL5 Clinical Phenotype Guidelines

**Core phenotype (need to be met for PP4)**
- Seizures, including infantile spasms, beginning in infancy
- Global developmental delay
- Intellectual disability
- Hypotonia
- Severely impaired gross motor function
- Cortical visual impairment in the first 12 months

**Supportive criteria** (do not need to be met for PP4, however in the absence of one core phenotype, two or more supportive phenotypes can be used in its place)
- Sleep disturbances
- Gastrointestinal dysfunction
- Subtle dysmorphic features (broad forehead, large, deep-set eyes, tapered fingers, full lips, anteverted nostrils in males)
- Bruxism
- Hand stereotypies
- Periodic breathing
- Laughing, screaming spells
- Cold hands and feet
- Peripheral vasomotor dysfunction

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**Status:** **Not Applicable.** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

#### VCEP Specifications

The frequency cutoffs are based on MECP2 expected disease allele frequency (1 in 10,000 for the disease prevalence / (1.5 alleles [assumes 50/50 male/female ratio] * 0.8 for 80% penetrance)). MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

| Strength | Threshold |
|----------|-----------|
| **BA1** (Stand Alone) | Allele frequency above 0.05%. Use large population databases (i.e. gnomAD). Use if variant is present at **≥0.000083 (0.0083%)** in any sub-population. Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles. |

**Modification Type:** Disease-specific

**Note (apparent source inconsistency, reproduced verbatim):** The BA1 heading states "Allele frequency above 0.05%" while the operative bullet states ≥0.000083 (0.0083%). Both are reproduced as written in the specification.

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### VCEP Specifications

The frequency cutoffs are based on MECP2 expected disease allele frequency divided by 10-fold. MECP2 is the most prevalent of the genes covered in the Rett/Angelman-like working group and was chosen as most conservative number.

| Strength | Threshold |
|----------|-----------|
| **BS1** (Strong) | Allele frequency greater than expected for disease (0.025%). Use large population databases (i.e. gnomAD). Use if variant is present at **≥0.0000083 (0.00083%) and <0.000083 (0.0083%)** in any sub-population. Use if allele frequency is met in any general continental population dataset of at least 2,000 observed alleles. |

**Modification Type:** Disease-specific

**Note (apparent source inconsistency, reproduced verbatim):** The BS1 heading states "(0.025%)" while the operative bullet defines the interval ≥0.00083% and <0.0083%. Both are reproduced as written in the specification.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

#### VCEP Specifications

- Should be applied in cases where the healthy adult is devoid of neurodevelopmental phenotypes.
- Best to use with internal curated data that includes clinical information or published patients that have been phenotyped.

| Strength | Application |
|----------|-------------|
| **BS2** (Strong) | Observed in the heterozygous/hemizygous state in a healthy adult: 2 unaffected (related or unrelated) heterozygotes or hemizygotes |
| **BS2_Supporting** | Observed in the heterozygous/hemizygous state in a healthy adult: 1 unaffected (related or unrelated) heterozygote or hemizygote |

**Modification Type:** Strength

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **BS3** (Strong) | RNA functional studies that demonstrate no impact on splicing and transcript composition. It can be downgraded based on quality of data. Not applicable for other functional studies. |

**Modification Type:** Disease-specific

**Note:** The CDKL5 Functional Assays table lists "Not recommended" as the Expected Benign Result Range (BS3) for all four protein-level assays.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.
*Caveat:* The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

#### VCEP Specifications

Need to confirm that the family member is 'affected with a neurodevelopmental phenotype consistent with the gene' at a minimum.

| Strength | Application |
|----------|-------------|
| **BS4** (Strong) | Absent in a similarly affected family member, when seen in two or more families |
| **BS4_Supporting** | Absent in a similarly affected family member |

**Modification Type:** Strength

---

### BP1 - Missense in Truncating Disease Gene

**Original ACMG Summary:** Missense variant in a gene for which primarily truncating variants are known to cause disease.

**Status:** **Not Applicable.** Comment: "Not applicable for CDKL5."

---

### BP2 - In Trans / In Cis with Pathogenic

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

#### VCEP Specifications

Knock out of *CDKL5* results in disease but viable phenotype (reference 5).

| Strength | Application |
|----------|-------------|
| **BP2** (Supporting) | Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder; or observed in cis with a pathogenic variant in any inheritance pattern. BP2 is not applicable for *in trans* state. |

**Modification Type:** Disease-specific

---

### BP3 - In-Frame Indel in Repetitive Region

**Original ACMG Summary:** In frame-deletions/insertions in a repetitive region without a known function.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **BP3** (Supporting) | BP3 is applicable if there are in-frame deletions/duplications in a repetitive region where other in-frame deletions/duplications have been observed with an overall frequency commensurate with the BA1 threshold for this gene. |

**Modification Type:** None

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc).
*Caveat:* As many in silico algorithms use the same or very similar input, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

#### VCEP Specifications

| Strength | Application |
|----------|-------------|
| **BP4** (Supporting) | For missense variants use REVEL with a score ≤ 0.290. For splice site variants use SpliceAI with a score ≤ 0.1. |

**Modification Type:** General recommendation

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

#### VCEP Specifications

- For example if a variant in *CKDL5* [*sic*] is identified in a patient with lissencephaly in whom a pathogenic variant is identified in the *PAFAH1B1* gene.
- Do not apply if variant is de novo.

| Strength | Application |
|----------|-------------|
| **BP5_Strong** | ≥3 cases with alternate molecular basis for disease. |
| **BP5** (Supporting) | 1 case with alternate molecular basis for disease. |

**Modification Type:** Strength (Strong); Disease-specific (Supporting)

**Note:** The specification does not define a level for exactly 2 cases — Not specified by VCEP.

---

### BP6 - Reputable Source (Benign)

**Original ACMG Summary:** Reputable source recently reports variant as benign, but the evidence is not available to the laboratory to perform an independent evaluation.

**Status:** **Not Applicable.** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

### BP7 - Synonymous Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

#### VCEP Specifications

For silent variants BP4 and BP7 can be added.

| Strength | Application |
|----------|-------------|
| **BP7** (Supporting) | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. Defined 'not highly conserved' regions in BP7 as those with PhastCons score <1 and/or PhyloP score <0.1 and/or the variant is the reference nucleotide in one primate and/or three mammal species. For splice site variants use SpliceAI with a score ≤ 0.1. |

**Modification Type:** None

---

## 4. Not Applicable Criteria

| Criterion | Reason |
|-----------|--------|
| **PM3** | Not applicable for CDKL5. |
| **PP2** | Not applicable for CDKL5. |
| **PP5** | Not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |
| **BP1** | Not applicable for CDKL5. |
| **BP6** | Not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229). |

---

## 5. Rules for Combining Criteria

### Pathogenic

| Combination |
|-------------|
| 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) **AND** ≥ 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) **AND** ≥ 2 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) **AND** 1 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) **AND** 1 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4) |
| 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) **AND** ≥ 2 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4) |
| ≥ 2 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** ≥ 3 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong **AND** 2 Moderate **AND** ≥ 2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** ≥ 4 Supporting |

### Likely Pathogenic

| Combination |
|-------------|
| 1 Very Strong (PVS1, PS2_Very Strong, PM6_Very Strong) **AND** 1 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS3, PS4, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 1 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong **AND** ≥ 2 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM4_Supporting, PP1, PP3, PP4) |
| ≥ 3 Moderate (PVS1_Moderate, PS4_Moderate, PM1, PM4, PM5, PM6, PP1_Moderate) |
| 2 Moderate **AND** ≥ 2 Supporting |
| 1 Moderate **AND** ≥ 4 Supporting |
| 1 Strong **AND** 2 Moderate |

### Benign

| Combination |
|-------------|
| ≥ 2 Strong (BS1, BS2, BS3, BS4, BP5_Strong) |
| 1 Stand Alone (BA1) |
| 1 Strong (BS1, BS2, BS3, BS4, BP5_Strong) **AND** 3 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP3, BP4, BP5, BP7) |

### Likely Benign

| Combination |
|-------------|
| ≥ 2 Supporting (BS2_Supporting, BS4_Supporting, BP2, BP3, BP4, BP5, BP7) |
| 1 Strong (BS1, BS2, BS3, BS4, BP5_Strong) |

---

## 6. Appendices

### Appendix A: PVS1 Flowchart for CDKL5

Transcript: *CDKL5* (NM_001323289.2)

#### Nonsense or Frameshift

| Condition | PVS1 Strength |
|-----------|---------------|
| Predicted to undergo NMD + Exon is present in biologically-relevant transcript(s) | **PVS1** |
| Predicted to undergo NMD + Exon is absent from biologically-relevant transcript(s) | N/A |
| Not predicted to undergo NMD + Upstream of most distal de novo LOF variant (p.R948); Frameshift that results in a read-through of the stop codon | **PVS1** |
| Not predicted to undergo NMD + Downstream of most distal de novo LOF variant (p.R948) | **PVS1_Moderate** |

#### GT--AG 1,2 Splice Sites

| Condition | PVS1 Strength |
|-----------|---------------|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD + Exon is present in biologically-relevant transcript(s) | **PVS1** |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD + Exon is absent from biologically-relevant transcript(s) | N/A |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is **NOT** predicted to undergo NMD (Exon 18) + Truncated/altered region is critical to protein function (Exon 18) | **PVS1_Strong** |
| Exon skipping or use of a cryptic splice site preserves reading frame (Exons 7, 10, 13, 17) + Role of region in protein function is unknown (Exon 17) | **PVS1_Moderate** |
| Exon skipping or use of a cryptic splice site preserves reading frame (Exons 7, 10, 13, 17) + Truncated/altered region is critical to protein function (Exons 7, 10, 13) | **PVS1** |

#### Deletion (Single Exon to Full Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Full gene deletion | **PVS1** |
| Single to multi exon deletion – disrupts reading frame and is predicted to undergo NMD + Exon is present in biologically-relevant transcript(s) | **PVS1** |
| Single to multi exon deletion – disrupts reading frame and is predicted to undergo NMD + Exon is absent from biologically-relevant transcript(s) | N/A |
| Single to multi exon deletion – disrupts reading frame and is **NOT** predicted to undergo NMD (Exon 18) + Truncated/altered region is critical to protein function (Exon 18) | **PVS1_Strong** |
| Single to multi exon deletion – preserves reading frame (single exon 7, 10, 13, 17 deletions; other in-frame combinations) / deletion of non-coding region (exon 1) + Role of region in protein function is unknown (Exon 17) + LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) (Exon 17) + Variant removes >10% of protein | **PVS1** |
| ...same path, but variant removes <10% of protein (Exon 17) | **PVS1_Moderate** |
| Single to multi exon deletion – preserves reading frame + Truncated/altered region is critical to protein function (Exons 1, 7, 10, 13, + any in-frame combination that includes the PM1 functional domains: p.19_43 (ATP binding) or p.169_171 (TEY phosphorylation)) | **PVS1** |

#### Duplication (≥1 exon in size and must be completely contained within gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Proven in tandem + Reading frame disrupted and NMD predicted to occur | **PVS1** |
| Proven in tandem / Presumed in tandem + No or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem + Reading frame presumed disrupted and NMD predicted to occur | **PVS1_Strong** |
| Proven not in tandem | N/A |

#### Initiation Codon

| Condition | PVS1 Strength |
|-----------|---------------|
| No known alternative start codon in other transcripts + No pathogenic variant(s) upstream of closest potential in-frame start codon | **PVS1_Supp** |

---

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold (as specified) | Strength |
|-----------|--------------------------|----------|
| BA1 | ≥0.000083 (0.0083%) in any sub-population | Stand Alone |
| BS1 | ≥0.0000083 (0.00083%) and <0.000083 (0.0083%) in any sub-population | Strong |
| PM2 | Absent, zero observations in control databases | Supporting |

Both BA1 and BS1 additionally require that the allele frequency is met in any general continental population dataset of at least 2,000 observed alleles, using large population databases (i.e. gnomAD).

---

### Appendix C: In Silico Thresholds Summary

| Tool | Pathogenic (PP3) | Benign (BP4 / BP7) |
|------|------------------|--------------------|
| REVEL (missense) | ≥ 0.644 | ≤ 0.290 |
| SpliceAI (splice site) | ≥ 0.2 | ≤ 0.1 |

---

### Appendix D: References (from the specification)

| # | Citation | PMID |
|---|----------|------|
| 1 | Krishnaraj R, Ho G et al. RettBASE: Rett syndrome database update. *Hum Mutat* (2017) 38 (8) p. 922-931. 10.1002/humu.23263 | 28541439 |
| 2 | Raymond L, Diebold B et al. Validation of high-resolution DNA melting analysis for mutation scanning of the CDKL5 gene: identification of novel mutations. *Gene* (2013) 512 (1) p. 70-5. 10.1016/j.gene.2012.09.056 | 23064044 |
| 3 | Hector RD, Kalscheuer VM et al. CDKL5 variants: Improving our understanding of a rare neurologic disorder. *Neurol Genet* (2017) 3 (6) p. e200. 10.1212/NXG.0000000000000200 | 29264392 |
| 4 | Rosas-Vargas H, Bahi-Buisson N et al. Impairment of CDKL5 nuclear localisation as a cause for severe infantile encephalopathy. *J Med Genet* (2008) 45 (3) p. 172-8. 10.1136/jmg.2007.053504 | 17993579 |
| 5 | Wang IT, Allen M et al. Loss of CDKL5 disrupts kinome profile and event-related potentials leading to autistic-like phenotypes in mice. *Proc Natl Acad Sci U S A* (2012) 109 (52) p. 21516-21. 10.1073/pnas.1216988110 | 23236174 |
| 6 | Pejaver V, Byrne AB et al. Calibration of computational tools for missense variant pathogenicity classification and ClinGen recommendations for PP3/BP4 criteria. *Am J Hum Genet* (2022) 109 (12) p. 2163-2177. 10.1016/j.ajhg.2022.10.013 | 36413997 |

Additional PMIDs cited in criteria or supplementary files: 29543229 (ClinGen SVI VCEP Review Committee, PP5/BP6), 30192042 (ClinGen SVI PVS1 working group), 16935860 and 27265524 (CDKL5 functional assays).

---

### Appendix E: Source Documents

| File | Content |
|------|---------|
| ClinGen_ACMG_Specifications_CDKL5_v6.0.pdf | Main criteria specification |
| PVS1 Flowchart for CDKL5.pdf | PVS1 decision flowchart (Appendix A) |
| Clinical Phenotype Guidelines for CDKL5.pdf | Phenotype guidelines referenced by PP4 |
| CDKL5 Functional Assays.xlsx | Acceptable functional studies for PS3/BS3 |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 6.0 | 5/1/2026 | 1 Strong AND 3 Supporting added to benign criteria code. 1 Strong added to likely benign criteria code. |

---

*This document was compiled from the ClinGen Rett and Angelman-like Disorders Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for CDKL5 Version 6.0 (GN034). For the most current version, refer to https://cspec.genome.network/cspec/ui/svi/doc/GN034*
