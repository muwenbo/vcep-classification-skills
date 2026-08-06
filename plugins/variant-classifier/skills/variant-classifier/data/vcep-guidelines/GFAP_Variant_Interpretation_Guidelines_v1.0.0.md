# Comprehensive Variant Interpretation Guidelines for GFAP

## ClinGen Leukodystrophy and Leukoencephalopathy VCEP Specifications for Alexander Disease (Version 1.0)

**Affiliation:** Leukodystrophy and Leukoencephalopathy Variant Curation Expert Panel (Leuko VCEP)
**Version:** 1.0
**Release Date:** August 3, 2026
**DOI:** 10.5281/zenodo.21777354
**Based on:** Richards et al., 2015 - ACMG/AMP Variant Interpretation Guidelines (Combining rules)

---

## Table of Contents

1. [Gene and Disease Information](#1-gene-and-disease-information)
2. [Pathogenic Criteria](#2-pathogenic-criteria)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PS4 - Prevalence in Affected](#ps4---prevalence-in-affected)
   - [PM1 - Mutational Hot Spot](#pm1---mutational-hot-spot)
   - [PM2 - Absent from Controls](#pm2---absent-from-controls)
   - [PM5 - Novel Missense at Same Residue](#pm5---novel-missense-at-same-residue)
   - [PM6 - De Novo (Assumed)](#pm6---de-novo-assumed)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP4 - Phenotype Specificity](#pp4---phenotype-specificity)
3. [Benign Criteria](#3-benign-criteria)
   - [BA1 - Stand-Alone Benign](#ba1---stand-alone-benign)
   - [BS1 - Allele Frequency Greater Than Expected](#bs1---allele-frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (Benign)](#bs3---functional-studies-benign)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP2 - Observed with Another Pathogenic Variant](#bp2---observed-with-another-pathogenic-variant)
   - [BP5 - Alternate Molecular Basis](#bp5---alternate-molecular-basis)
   - [BP7 - Synonymous Variants](#bp7---synonymous-variants)
4. [Not Applicable Criteria](#4-not-applicable-criteria)
5. [Rules for Combining Criteria](#5-rules-for-combining-criteria)
6. [Appendices](#6-appendices)

---

## 1. Gene and Disease Information

| Parameter | Value |
|-----------|-------|
| **Gene** | GFAP (HGNC:4235) |
| **HGNC Name** | glial fibrillary acidic protein |
| **Reference Transcript** | NM_002055.5 |
| **Disease** | Alexander disease |
| **MONDO ID** | MONDO:0008752 |
| **Mode of Inheritance** | Autosomal dominant inheritance |
| **Mechanism of Disease** | Gain of function |

### General Comments (VCEP)

Alexander Disease is caused by gain of function variants in GFAP, which lead to protein aggregation and loss of protein solubility that is damaging to astrocytes.

---

## 2. Pathogenic Criteria

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**VCEP Specification:** Previously established variant must be established as pathogenic or likely pathogenic per criteria established by this VCEP. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

| Strength | Application |
|----------|-------------|
| **PS1** (Strong) | Same amino acid change as a previously established Pathogenic or Likely Pathogenic variant regardless of nucleotide change. Previously established variant must be established as pathogenic per criteria established by this VCEP. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level. |
| **PS1_Moderate** | Not specified by VCEP |

*Modification type: No change*

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specification:** Modifications made to the SVI Recommendation for De Novo Criteria (PS2 & PM6). Instructions are provided in the attached VCEP document ("PS2 & PM6 Instructions"). Proband counting uses the VCEP Alexander disease (AxD) diagnostic criteria described in the PP4 document (see [Appendix C](#appendix-c-vcep-alexander-disease-axd-diagnostic-criteria)).

#### Points Awarded per De Novo Occurrence (GFAP-modified)

| Phenotypic consistency | De novo with confirmed parental relationships | De novo with unconfirmed parental relationships |
|------------------------|-----------------------------------------------|--------------------------------------------------|
| "Definite" diagnosis of Alexander Disease per VCEP criteria | 6 | 4 |
| "Probable" diagnosis of Alexander Disease per VCEP criteria | 4 | 3 |
| "Consistent" diagnosis of Alexander Disease per VCEP criteria | 3 | 1.5 |
| Phenotype not consistent with gene | 0 | 0 |

#### Determining Evidence Strength Level (PS2)

| Total Points | Evidence Strength |
|--------------|-------------------|
| 10 points | **PS2_VeryStrong** |
| 6 points | **PS2** (Strong) |
| 3 points | **PS2_Moderate** |
| 1.5 points | **PS2_Supporting** |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specification:** Follow the instructions in the attached VCEP document (PS3/BS3 Instructions decision tree; see [Appendix A](#appendix-a-ps3bs3-decision-tree)).

| Strength | Application |
|----------|-------------|
| **PS3_VeryStrong** | Animal model that replicates human phenotype |
| **PS3** (Strong) | Immunoassay/Western blot that demonstrates GFAP insolubility in non patient-derived cell lines that are transfected (or genome edited) with the variant in question |
| **PS3_Moderate** | Immunocytochemistry/Immunohistochemistry demonstrates abnormal GFAP aggregation (compared to wild-type control with demonstrated intermediate filament architecture) in non patient-derived cell lines that are transfected (or genome edited) with the variant in question |
| **PS3_Supporting** | Immunoassay/Western blot, Immunocytochemistry/Immunohistochemistry, or confocal/electron microscopy show protein aggregation/loss of solubility in patient-derived cell lines |

**VCEP note recorded in the specification:** "Unsure of what excel file referred to in the comments is. No excel file was submitted and there is no 'Impaired Enzyme Activity' assay type for this gene."

#### Approved Functional Assays (PS3 Excel Sheet)

| Assay class | Reference | Material / readout | Approved | Proposed strength |
|-------------|-----------|--------------------|----------|-------------------|
| Animal model (zebrafish) | Lee 2017; PMID: 28882119 | One-cell stage zebrafish embryos microinjected with GFAP expression constructs; abnormal GFAP aggregation vs. wild-type | Y | PS3_VeryStrong; BS3 not applied |
| Immunohistochemistry assay | Dotti 2009; PMID: 19444543 | SW13 (vim-) cells transfected with pcDNA3.1-hGF(WT)/variant plasmids; abnormal GFAP aggregation or astrocyte cell body enlargement | Y | PS3_Moderate; BS3 not applied |
| Immunoassay / Western blot | Kaneko 2009; PMID: 19412928 | C6 cells transfected with WT or variant GFAP plasmids; reduced GFAP solubility | Y | PS3; BS3 not applied |
| Patient-derived iPSC astrocytes | Kondo 2016; PMID: 27402089 | Patient-derived iPSCs differentiated to astrocytes; GFAP filament formation / solubility | Y | PS3_Supporting; BS3_Moderate not applied |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specification:** Follow the instructions in the provided VCEP document. Criteria were established by the VCEP using the Yoshida criteria as guidelines and making appropriate modifications based on discussion with experts on AxD. Proband counting uses the VCEP AxD diagnostic criteria (see [Appendix C](#appendix-c-vcep-alexander-disease-axd-diagnostic-criteria)).

#### Notes

- If a variant meets criteria for BS1 or BA1, PS4 cannot apply.
- Due to phenotypic variability (late onset, variable expressivity, incomplete penetrance) the possibility of pathogenic variants being present in population databases cannot be excluded.

#### Points per Proband

| Individual proband phenotype | Points per proband |
|------------------------------|--------------------|
| AxD definite diagnosis | +3 points |
| AxD probable diagnosis | +2 points |
| AxD consistent features | +1 point |

#### Determining Evidence Strength Level (PS4)

| Total cumulative points | Evidence Strength |
|-------------------------|-------------------|
| 15+ points | **PS4_VeryStrong** |
| 9-14 points | **PS4** (Strong) |
| 4-8 points | **PS4_Moderate** |
| 2-3 points | **PS4_Supporting** |

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specification:** This includes missense variants and in-frame deletions/duplications in ANY transcript expressed in astrocytes.

| Strength | Application |
|----------|-------------|
| **PM1** (Moderate) | Variant affecting an amino acid at or in between positions 59-88. This region shows variation constraint (p-value 6/45e-4), as well as a high concentration of pathogenic/likely pathogenic variants (24 variants in 30 amino acids in this region vs 41 variants in 402 amino acids outside this region). This includes missense variants and in-frame deletions/duplications. |

**Supporting evidence:** gnomAD regional missense constraint for amino acids Arg88-Asn59 (chr17:42992593-42992678, GRCh37): missense observed/expected 0.2727 (6/22.01), p-value 6.451e-4.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specification:** SVI guidance on PM2 recommends decreasing weight of criterion PM2 from moderate to supporting strength level.

| Strength | Threshold |
|----------|-----------|
| **PM2_Supporting** | Absent in gnomAD |

*Modification type: Strength. (Pilot feedback: PM2 was changed to require absence.)*

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

| Strength | Application |
|----------|-------------|
| **PM5** (Moderate) | Novel missense change at an amino acid residue where one different pathogenic or likely pathogenic variant has been identified. |

*Modification type: None*

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specification:** To assign points to the variant, follow the instructions in the provided VCEP document. Modifications were made to the SVI Recommendation for De Novo Criteria (PS2 & PM6) to adapt to GFAP. Use the same point table as [PS2](#ps2---de-novo-confirmed) (unconfirmed parental relationships column).

| Strength | Points |
|----------|--------|
| **PM6_Strong** | 6 points |
| **PM6** (Moderate) | 3 points |
| **PM6_Supporting** | 1.5 points |

**Note:** The specification records that "CSPEC editor does not allow to add VeryStrong for PM6"; no PM6_VeryStrong threshold is listed in the registry entry.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specification:**
- If PP4 is applied, PP1 cannot be applied (per ClinGen Guidance; PMID: 38103548).
- If PP4 is not met, individuals must meet "consistent", "probable", or "definite" diagnosis according to VCEP PS2/PM6 guidelines.

| Strength | Application |
|----------|-------------|
| **PP1_Strong** | ≥5 informative meioses |
| **PP1_Moderate** | ≥3 informative meioses |
| **PP1** (Supporting) | ≥2 informative meioses |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specification:**
- PP4 is only applicable if the individual meets a "consistent", "probable", or "definite" diagnosis according to VCEP PS2/PM6 guidelines (see [Appendix C](#appendix-c-vcep-alexander-disease-axd-diagnostic-criteria)).
- PP4 and PP1 are mutually exclusive; therefore if PP4 is not met, PP1 should be considered instead.

| Strength | Application |
|----------|-------------|
| **PP4_Strong** | Elevated GFAP protein levels in plasma, serum, or CSF. For clinical tests, established thresholds are dependent on age and currently only exist for individuals above the age of 18 years. Clinical lab reports clearly indicate if levels are elevated (in pg/mL). For research-based testing, levels must be significantly elevated when compared to age-matched controls. |
| **PP4_Moderate** | Existence of Rosenthal fibers in addition to gliosis and loss of myelin. |
| **PP4** (Supporting) | Not specified by VCEP |

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

| Strength | Threshold |
|----------|-----------|
| **BA1** (Stand Alone) | gnomAD (v4.1.0) filtering allele frequency **≥0.01%** |

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

| Strength | Threshold |
|----------|-----------|
| **BS1** (Strong) | gnomAD (v4.1.0) filtering allele frequency **≥0.001%** |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specification:** Observed in gnomAD in a homozygous state.

| Strength | Application |
|----------|-------------|
| **BS2** (Strong) | Observed in gnomAD in a homozygous state |

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specification:** Follow the instructions in the attached VCEP document (PS3/BS3 Instructions decision tree; see [Appendix A](#appendix-a-ps3bs3-decision-tree)).

| Strength | Application |
|----------|-------------|
| **BS3** (Strong) | Protein expression assay demonstrates loss of function when variant is transfected or genome edited into non patient-derived cell lines |
| **BS3_Moderate** | Immunoassay/Western blot that demonstrates GFAP normal solubility in non patient-derived cell lines that are transfected (or genome edited) with the variant in question **OR** Immunocytochemistry/Immunohistochemistry demonstrates normal GFAP aggregation (compared to wild-type control with demonstrated intermediate filament architecture) in non patient-derived cell lines that are transfected (or genome edited) with the variant in question **OR** Immunoassay/Western blot, Immunocytochemistry/Immunohistochemistry, or confocal/electron microscopy show normal protein distribution and solubility in patient-derived cell lines |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specification:**
- To count as affected, individuals must meet "consistent", "probable", or "definite" diagnosis according to VCEP PS2/PM6 guidelines.
- To count as unaffected, individuals must meet **both** of the following:
  - Negative MRI at or after 18 years
  - No clinical symptoms listed in the PS2/PM6 guidelines at or after 18 years
- Any individuals not meeting either criteria for affected or unaffected should not be counted as informative.

| Strength | Application |
|----------|-------------|
| **BS4** (Strong) | ≥3 informative meioses |
| **BS4_Moderate** | ≥2 informative meioses |

---

### BP2 - Observed with Another Pathogenic Variant

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

| Strength | Application |
|----------|-------------|
| **BP2** (Supporting) | Observed with another variant (regardless of phase) in GFAP that is established as pathogenic or likely pathogenic per these criteria |

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

| Strength | Application |
|----------|-------------|
| **BP5** (Supporting) | Variant found in a case with an alternate molecular basis for disease |

*Modification type: None*

---

### BP7 - Synonymous Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

| Strength | Application |
|----------|-------------|
| **BP7** (Supporting) | A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. An amino acid is considered highly conserved if the phyloP score is <2.27. PhyloP score can be found in gnomAD in the In Silico Predictors tool. |

*Conservation definition added during pilot testing (PMID: 40011430); phyloP score can also be found in the UCSC Browser.*

---

## 4. Not Applicable Criteria

The following ACMG/AMP criteria are **NOT APPLICABLE** for GFAP variant interpretation:

| Criterion | Original Purpose | Reason Not Applicable (VCEP comment) |
|-----------|-----------------|--------------------------------------|
| **PVS1** | Null variant | LOF is not a known disease mechanism |
| **PM3** | In trans with pathogenic variant | Autosomal Dominant disorder |
| **PM4** | Protein length changes | There are some in-frame deletions but mechanism is not common enough to assign this criteria |
| **PP2** | Missense in constrained gene | Not applicable because missense z score is <3.09 |
| **PP3** | Computational evidence (pathogenic) | GFAP has a gain of function mechanism of disease and no individual tool or meta predictor has provided consistent and accurate scores for GFAP variants, especially those variants associated with Type II or adult-onset presentations. Use of this criterion can be revisited in the future if modeling tools specific to this gene or designed to characterize gain of function mutations are shown to more accurately model pathogenicity of GFAP variants. |
| **PP5** | Reputable source reports pathogenic | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |
| **BP1** | Missense in truncating disease gene | GFAP is caused primarily by missense variants |
| **BP3** | In-frame deletion in repetitive region | No repetitive regions without known function |
| **BP4** | Computational evidence (benign) | GFAP has a gain of function mechanism of disease and no individual tool or meta predictor has provided consistent and accurate scores for GFAP variants, especially those variants associated with Type II or adult-onset presentations. Use of this criterion can be revisited in the future if modeling tools specific to this gene or designed to characterize gain of function mutations are shown to more accurately model pathogenicity of GFAP variants. |
| **BP6** | Reputable source reports benign | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |

---

## 5. Rules for Combining Criteria

### Pathogenic Classification

| Combination | Classification |
|-------------|----------------|
| 1 Very Strong AND ≥1 Strong | **Pathogenic** |
| 1 Very Strong AND ≥2 Moderate | **Pathogenic** |
| 1 Very Strong AND 1 Moderate AND 1 Supporting | **Pathogenic** |
| 1 Very Strong AND ≥2 Supporting | **Pathogenic** |
| ≥2 Strong | **Pathogenic** |
| 1 Strong AND ≥3 Moderate | **Pathogenic** |
| 1 Strong AND 2 Moderate AND ≥2 Supporting | **Pathogenic** |
| 1 Strong AND 1 Moderate AND ≥4 Supporting | **Pathogenic** |

### Likely Pathogenic Classification

| Combination | Classification |
|-------------|----------------|
| 1 Very Strong AND 1 Moderate | **Likely Pathogenic** |
| 1 Strong AND 1 Moderate | **Likely Pathogenic** |
| 1 Strong AND ≥2 Supporting | **Likely Pathogenic** |
| ≥3 Moderate | **Likely Pathogenic** |
| 2 Moderate AND ≥2 Supporting | **Likely Pathogenic** |
| 1 Moderate AND ≥4 Supporting | **Likely Pathogenic** |

### Benign Classification

| Combination | Classification |
|-------------|----------------|
| ≥2 Strong | **Benign** |
| 1 Stand Alone (BA1) | **Benign** |

### Likely Benign Classification

| Combination | Classification |
|-------------|----------------|
| 1 Strong (BS1) | **Likely Benign** |
| 1 Strong (BS2, BS3, BS4) AND 1 Supporting (BP2, BP5, BP7) | **Likely Benign** |

### Variant of Uncertain Significance (VUS)

- Criteria for benign and pathogenic are contradictory
- No criteria met
- Criteria met do not reach threshold for Likely Benign or Likely Pathogenic

---

## 6. Appendices

### Appendix A: PS3/BS3 Decision Tree

The VCEP provides a decision tree ("GFAP PS3/BS3 Instructions") for assigning functional evidence strength:

1. **Animal model that replicates human phenotype?**
   - Yes → **PS3_VeryStrong**
   - No → continue
2. **Assay uses patient-derived cell lines?**
   - **Yes** → Immunoassay/Western blot, Immunocytochemistry/Immunohistochemistry, or confocal/electron microscopy shows abnormal protein aggregation / loss of solubility or astrocyte cell body enlargement?
     - Yes → **PS3_Supporting**
     - No → **BS3_Moderate**
   - **No** → Is the cell line transfected or genome edited with the variant in question?
     - No → **No criteria applies**
     - Yes → continue
3. **Assay is an Immunoassay/Western blot for GFAP protein solubility?**
   - Yes → assay demonstrates GFAP protein loss of solubility?
     - Yes → **PS3**
     - No → **BS3**
   - No → Is it an Immunocytochemistry or Immunohistochemistry assay?
     - Yes → demonstrates abnormal GFAP aggregation (compared to wild-type control with demonstrated intermediate filament architecture) or astrocyte cell body enlargement?
       - Yes → **PS3_Moderate**
       - No → **BS3**
     - No → **Contact VCEP to assess the functional assay and update specifications**

---

### Appendix B: Population Frequency Thresholds Summary

| Criterion | Threshold (gnomAD v4.1.0 filtering allele frequency) | Strength |
|-----------|------------------------------------------------------|----------|
| BA1 | ≥0.01% | Stand Alone |
| BS1 | ≥0.001% | Strong |
| PM2 | Absent in gnomAD | Supporting |

---

### Appendix C: VCEP Alexander Disease (AxD) Diagnostic Criteria

Used for proband counting in PS2, PM6, PS4, PP1, PP4 and BS4. Based on the AxD Yoshida criteria (2017) with Leuko VCEP (2024) modifications.

#### Diagnostic Categories

| Category | Requirement |
|----------|-------------|
| **AxD definite diagnosis** (Yoshida criteria, 2017; LeukoVCEP, 2024) | One of the following: >1 findings in A1-A8 (neurologic features) AND >1 finding in B1-B6 OR B8 (MRI) |
| **AxD probable diagnosis** (Yoshida criteria, 2017; LeukoVCEP, 2024) | One of the following: 1 finding in A1-A8 (neurologic features) AND B1-B6 OR B8 |
| **AxD consistent features** (LeukoVCEP, 2024) | Any of: >4 findings in A1-8 without neuroimaging findings; >2 findings in A1-8 plus family history (affected sibling, parent or grandparent); >1 finding in B1-7 plus family history (affected sibling, parent or grandparent); stated clinical diagnosis of Alexander disease |

**Of note:** A diagnosis of "leukodystrophy" (general) and a GFAP variant without additional phenotype-specific information does not count.

#### (A) Neurologic Findings

| # | Finding |
|---|---------|
| A1 | Convulsions |
| A2 | Macrocephaly |
| A3 | Psychomotor developmental delay / intellectual disability / cognitive impairment / developmental regression or stagnation |
| A4 | Motor symptoms: muscle weakness, spastic paresis, cerebellar ataxia, muscle rigidity |
| A5 | Bulbar / pseudobulbar palsy: dysphagia, dysarthria, dysphonia |
| A6 | Autonomic dysfunction: orthostatic hypotension, sphincter abnormalities, sleep apnea |
| A7 | Palatal myoclonus |
| A8 | Episodic vomiting |

#### (B) Neuroimaging Findings (MRI or CT)

| # | Finding |
|---|---------|
| B1 | Cerebral white matter abnormalities with frontal lobe predominance |
| B2 | Periventricular rim, supportive features (Garland-like signal) |
| B3 | Signal abnormalities with swelling or atrophy of the basal ganglia and thalami |
| B4 | Contrast enhancement |
| B5 | Signal abnormalities in midbrain |
| B6 | Signal abnormalities or atrophy of the medulla oblongata and/or cervical cord or hyperintensities in the brainstem |
| B7 | Signal abnormalities in the hilum of the dentate nucleus |
| B8 | Neuroimaging (MRI or CT) described as characteristic for AxD upon literature review |

---

### Appendix D: Key References

| Citation | PMID | Topic |
|----------|------|-------|
| Richards et al., 2015 | 25741868 | ACMG/AMP Variant Interpretation Guidelines |
| Yoshida et al., 2017 | 23903069 | AxD diagnostic criteria (as cited by the VCEP) |
| Prust et al., 2011 | 21917775 | AxD cohort used to test the point systems (185 reported) |
| Li 2005 | 15732097 | AxD infantile and late-onset cohort used to test the point systems |
| Lee 2017 | 28882119 | Zebrafish animal model (PS3_VeryStrong assay) |
| Dotti 2009 | 19444543 | SW13 (vim-) immunohistochemistry assay (PS3_Moderate) |
| Kaneko 2009 | 19412928 | C6 cell Western blot solubility assay (PS3) |
| Kondo 2016 | 27402089 | Patient-derived iPSC astrocytes (PS3_Supporting) |
| ClinGen SVI VCEP Review Committee | 29543229 | PP5/BP6 not for use |
| ClinGen guidance (PP1/PP4 mutual exclusivity) | 38103548 | PP1 cannot be applied when PP4 is applied |
| BP7 conservation reference | 40011430 | phyloP <2.27 not highly conserved |
| Unpublished GLIA-CTN biorepository data | - | Additional evidence used by the VCEP |

---

### Appendix E: Pilot Modifications Incorporated into Version 1.0

- **PM2:** changed to require the variant be absent from gnomAD.
- **BP7:** added definition of high conservation (phyloP score <2.27 is NOT highly conserved; PMID: 40011430) — available in gnomAD or the UCSC Browser.
- **PM1:** specified that the criterion is applicable to a missense change in ANY transcript expressed in astrocytes.
- **Diagnostic criteria document:** the requirement for genetic/pathological test criterion C1 was removed, neurologic findings were broadened from A1-A3 to A1-A8, and MRI finding B8 was added to definite and probable categories; the "consistent" category family-history MRI range was extended from B1-6 to B1-7.

#### Pilot Variant Concordance Summary

| Outcome | P/LP variants | VUS | B/LB variants |
|---------|---------------|-----|---------------|
| VCEP classification consistent with ClinVar | 5 | 9 | 9 |
| Pathogenic to LP | 2 | - | - |
| LP to P | 1 | - | - |
| LP/P to VUS | 2 | - | - |
| VUS to LP/P | - | 1 | - |
| VUS to Benign/LB | - | 2 | - |
| LB/B to VUS | - | - | 1 |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | August 3, 2026 | Initial released specification for GFAP (Alexander disease) by the Leukodystrophy and Leukoencephalopathy VCEP |

---

*This document is based on the ClinGen Leukodystrophy and Leukoencephalopathy Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for GFAP Version 1.0 (DOI: 10.5281/zenodo.21777354).*
