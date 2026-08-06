# Comprehensive Variant Interpretation Guidelines for ABCD1

## ClinGen Peroxisomal Disorders VCEP Specifications for ABCD1 (Version 1.0)

**Affiliation:** Peroxisomal Disorders Variant Curation Expert Panel (Perox VCEP)
**Version:** 1.0
**Release Date:** April 6, 2026
**Status:** Released
**DOI:** 10.5281/zenodo.21434373
**Based on:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015 (ACMG/AMP)

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
   - [PM4 - Protein Length Changes](#pm4---protein-length-changes)
   - [PM5 - Novel Missense at Same Residue](#pm5---novel-missense-at-same-residue)
   - [PM6 - De Novo (Assumed)](#pm6---de-novo-assumed)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
   - [PP4 - Phenotype Specificity](#pp4---phenotype-specificity)
3. [Benign Criteria](#3-benign-criteria)
   - [BA1 - Stand-Alone Benign](#ba1---stand-alone-benign)
   - [BS1 - Allele Frequency Greater Than Expected](#bs1---allele-frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (Benign)](#bs3---functional-studies-benign)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP2 - Observed in cis with Pathogenic Variant](#bp2---observed-in-cis-with-pathogenic-variant)
   - [BP4 - Computational Evidence (Benign)](#bp4---computational-evidence-benign)
   - [BP7 - Synonymous/Intronic Variants](#bp7---synonymousintronic-variants)
4. [Not Applicable Criteria](#4-not-applicable-criteria)
5. [Rules for Combining Criteria](#5-rules-for-combining-criteria)
6. [Appendices](#6-appendices)

---

## 1. Gene and Disease Information

| Parameter | Value |
|-----------|-------|
| **Gene** | ABCD1 (HGNC:61) |
| **HGNC Name** | ATP binding cassette subfamily D member 1 |
| **Reference Transcript** | NM_000033.4 |
| **Disease** | Adrenoleukodystrophy |
| **MONDO ID** | MONDO:0018544 |
| **Mode of Inheritance** | X-linked inheritance |
| **Specification Type** | Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015 |

### Key Gene Characteristics

- ABCD1 encodes ALDP, a peroxisomal ATP-binding cassette transporter; deficiency impairs peroxisomal beta-oxidation of very long-chain fatty acids (VLCFA)
- ABCD1 is **not constrained for missense** variation (missense Z score: 1.87); missense variants are also known to cause disease
- Exons 1 and 9 are **in-frame**
- Four ABCD1 pseudogenes exist (on chromosomes 2, 10, 16 and 22); sequencing laboratories are routinely expected to exclude them in analysis

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

#### General Caveats

- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

#### VCEP Specification (Default Point Value: 8; Modification Type: Disease-specific, Strength)

The Perox VCEP will utilize SVI's PVS1 recommendation for determining the applicable PVS1 strength level (Abou Tayoun et al., 2018; PMID: 30192042). Refer to the ABCD1-modified PVS1 decision tree.

- **PVS1_RNA** is applicable for splicing defects demonstrated by RNA studies on patient mRNA or when a variant is expressed in human/mammalian host cells. Strength level may be decided based on the assay as well as the abundance of normal splice products as recommended by Walker et al., 2023.
- Exons 1 and 9 are in-frame. Exon skipping consequences for splice site variants are listed in the exon table below.

#### ABCD1 NMD Boundaries (NM_000033.4)

| Variant type | Predicted to undergo NMD | NOT predicted to undergo NMD |
|--------------|--------------------------|------------------------------|
| Nonsense | up to c.1941 | from c.1942 |
| Frameshift −1, +2 | up to c.1903 | from c.1904 |
| Frameshift +1, −2 | up to c.1866 | from c.1867 |

#### PVS1 Decision Tree - Nonsense or Frameshift

| Condition | PVS1 Strength |
|-----------|---------------|
| Predicted to undergo NMD + exon is present in biologically-relevant transcript(s) | **PVS1** |
| Not predicted to undergo NMD + role of region in protein function is unknown + LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) + variant removes >10% of protein | **PVS1_Strong** |
| Not predicted to undergo NMD + role of region in protein function is unknown + LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) + variant removes <10% of protein | **PVS1_Moderate** |

#### PVS1 Decision Tree - GT–AG ±1,2 Splice Sites

| Condition | PVS1 Strength |
|-----------|---------------|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD (**exons 2 through 8**) + exon is present in biologically-relevant transcript(s) | **PVS1** |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is **NOT** predicted to undergo NMD (**exon 10**) + role of region unknown + LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) + variant removes >10% of protein | **PVS1_Strong** |
| Exon skipping or use of a cryptic splice site preserves reading frame (**exons 1 and 9**) + role of region unknown + LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) + variant removes >10% of protein (**exon 1**) | **PVS1_Strong** |
| Exon skipping or use of a cryptic splice site preserves reading frame (**exons 1 and 9**) + role of region unknown + LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) + variant removes <10% of protein (**exon 9**) | **PVS1_Moderate** |

#### PVS1 Decision Tree - Deletions (Single Exon to Full Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Full gene deletion | **PVS1** |
| Single to multi exon deletion - disrupts reading frame and is predicted to undergo NMD + exon is present in biologically-relevant transcript(s) | **PVS1** |
| Single to multi exon deletion - disrupts reading frame and is **NOT** predicted to undergo NMD, OR preserves reading frame + role of region unknown + LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) + variant removes >10% of protein | **PVS1_Strong** |
| Single to multi exon deletion - disrupts reading frame and is **NOT** predicted to undergo NMD, OR preserves reading frame + role of region unknown + LoF variants in this exon are not frequent in the general population and exon is present in biologically-relevant transcript(s) + variant removes <10% of protein (**exon 9**) | **PVS1_Moderate** |

#### PVS1 Decision Tree - Duplications (≥1 Exon, Completely Contained Within Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Proven in tandem + reading frame disrupted and NMD predicted to occur | **PVS1** |
| Proven in tandem or presumed in tandem + no or unknown impact on reading frame and NMD | N/A |
| Presumed in tandem + reading frame presumed disrupted and NMD predicted to occur + detected in >1 case | **PVS1_Strong** |
| Proven not in tandem | N/A |

#### PVS1 Decision Tree - Initiation Codon

| Condition | PVS1 Strength |
|-----------|---------------|
| No known alternative start codon in other transcripts + ≥1 (4) pathogenic variant(s) upstream of closest potential in-frame start codon | **PVS1_Moderate** |

#### ABCD1 Exon Table (Exon Skipping Consequences)

| Exon | Length | Range | Canonical splice defect outcome |
|------|--------|-------|---------------------------------|
| 1 | 1311 | c.1_900 | Ex 1 skipping |
| 2 | 181 | c.901_1081 | Ex 2 skipping; fs |
| 3 | 143 | c.1082_1224 | Ex 3 skipping; fs |
| 4 | 169 | c.1225_1393 | Ex 4 skipping; fs |
| 5 | 95 | c.1394_1488 | Ex 5 skipping; fs |
| 6 | 146 | c.1489_1634 | Ex 6 skipping; fs |
| 7 | 146 | c.1635_1780 | Ex 7 skipping; fs |
| 8 | 85 | c.1781_1865 | Ex 8 skipping; fs |
| 9 | 126 | c.1866_1991 | Ex 9 skipping |
| 10 | 1267 | c.1992_2238 | Ex 10 skipping; fs |

*fs = frameshift*

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Points | Application |
|----------|--------|-------------|
| **PS1 (Strong)** | 4 | Applied for **1 previously established pathogenic variant**. PS1 can also be applied at the strong level for **1 previously established pathogenic canonical splice site variant (at the same position)** |
| **PS1_Moderate** | 2 | Applied for **1 previously established likely pathogenic variant**. PS1 can also be applied at the moderate level for **1 previously established likely pathogenic canonical splice site variant (at the same position)** |

#### Requirements (both strength levels)

- Splicing abnormalities (using VCEP-specified prediction algorithms or evidence from literature) should be excluded for all missense variants
- The other variant(s) used for evidence should also have been curated using Perox VCEP rule specifications and reach a pathogenic/likely pathogenic classification **without using PS1**

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### VCEP Specifications (Default Point Value: 4; Modification Type: Disease-specific)

- Confirmed maternity and paternity by WES Trio, or paternity and maternity testing for **affected females**. Confirmation of **maternity is sufficient in the case of affected males**.
- Use the SVI-recommended point system at the **2nd tier ("phenotype consistent with gene but not highly specific")** for probands meeting **PP4**, and at the **1st tier ("phenotype highly specific for gene")** for probands meeting **PP4_Moderate**.

#### Points Awarded per Proband

| Phenotypic consistency | Confirmed de novo | Assumed de novo |
|------------------------|-------------------|-----------------|
| Phenotype highly specific for gene (**PP4_Moderate**) | 2 | 1 |
| Phenotype consistent with gene but not highly specific (**PP4**) | 1 | 0.5 |
| Phenotype consistent with gene but not highly specific and high genetic heterogeneity | 0.5 | 0.25 |
| Phenotype not consistent with gene | 0 | 0 |

#### Determining Evidence Strength Level

| Total Points | Evidence Strength |
|--------------|-------------------|
| 0.5 | PS2_Supporting or PM6_Supporting |
| 1 | PS2_Moderate or PM6 |
| 2 | PS2 (Strong) or PM6_Strong |
| 4 | PS2_VeryStrong or PM6_VeryStrong |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **PS3_Supporting** | 1 | Applicable for **beta-oxidation activity assays** OR **immunofluorescence assays showing absence or mislocalization of protein** OR **immunoblotting assay showing absence or reduced protein levels** |

**Notes:**

- For variants meeting PS1, functional studies on a different variant (different nucleotide change, same amino acid change) may be applicable to the variant being curated. **PS3_Supporting may be used in addition to PS1.**
- There are not many benign variants to curate for functional evidence at this time. The VCEP would favor using **PS3_Moderate** in the event that more variants with functional evidence are classified as benign by the Peroxisomal Disorders VCEP.
- **PS3_Strong is not specified by the VCEP.**

#### Approved Assay Instances (from ABCD1 functional assays supplement)

##### Beta-oxidation activity assays

| PMID | Author (Year) | Assay | Material | Approved | Proposed strength |
|------|---------------|-------|----------|----------|-------------------|
| 23430809 | Morita et al. (2013) | Beta-oxidation activity in CADDS fibroblasts lacking ABCD1, transfected with empty vector or WT/mutant ABCD1 plasmids; C14-C24:0 substrate | CADDS fibroblasts | yes | PS3_moderate |
| 11438993 | Dvoráková (2001) | Beta-oxidation activity in X-ALD fibroblasts transfected with WT/mutant ABCD1 plasmids; C14-C24:0 substrate; C24/C16 ratio | X-ALD and normal fibroblasts | yes | PS3_moderate |
| 23300730 | Amorosi (2012) | Beta-oxidation activity in normal and X-ALD fibroblasts transfected with WT/mutant ABCD1 plasmids; D3-C22:0 substrate | X-ALD and normal fibroblasts | yes | PS3_moderate |
| 17542813 | Takahashi (2007) | Beta-oxidation activity in normal and X-ALD fibroblasts transfected with empty vector or WT/mutant ABCD1 plasmids; C14-C24:0 substrate | X-ALD and normal fibroblasts | yes | PS3_moderate |

*Note: the supplement's "Proposed strength" column lists PS3_moderate for beta-oxidation assays, while the released specification text assigns PS3 at the **Supporting** level (Default Point Value: 1) with the note above about favoring PS3_moderate in the future.*

##### Immunoblotting assays

| PMID | Author (Year) | Readout | Approved | Proposed strength |
|------|---------------|---------|----------|-------------------|
| 23430809 | Morita et al. (2013) | Qualitative: presence/absence of ABCD1 band (CADDS fibroblasts, anti-ABCD1) | yes | PS3_Supporting |
| 17542813 | Takahashi (2007) | Quantitative: ratio of His-ALDP to catalase; expression ratio (%) vs WT = 100% | yes | PS3_Supporting |
| 29926352 | Morita (2019) | Qualitative: presence/absence of ABCD1-GFP band (CHO cells, anti-GFP) | yes | PS3_Supporting |

##### Immunofluorescence assays

| PMID | Author (Year) | Readout | Approved | Proposed strength |
|------|---------------|---------|----------|-------------------|
| 23430809 | Morita et al. (2013) | Qualitative: correct peroxisomal localization (CHO/GFP-SKL cells, anti-ABCD1) | yes | PS3_Supporting |
| 29926352 | Morita (2019) | Qualitative: correct peroxisomal localization (CHO cells, anti-GFP) | yes | PS3_Supporting |

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

#### VCEP Specifications

Applicable when multiple unrelated probands are reported with the same variant. All probands counted should meet at least **PP4_supporting** phenotype criteria. When multiple unrelated individuals are reported with the variant, use the proband that would meet the highest strength level for PP4 and count the remaining ones (at least meeting PP4_supporting strength) towards PS4.

| Strength | Points | Number of probands |
|----------|--------|--------------------|
| **PS4_Very Strong** | 8 | ≥ 16 probands |
| **PS4 (Strong)** | 4 | 4-15 probands |
| **PS4_Moderate** | 2 | 2-3 probands |
| **PS4_Supporting** | 1 | 1 proband |

**Note:** The VCEP cautions against applying PS4 for >4 cases (meeting phenotype criteria D/E and F) with the same variant identified **solely on newborn screening**.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **PM1 (Moderate)** | 2 | Applied for variants within the **Walker A (aa 507-520; c.1519-c.1560)** and **Walker B (aa 617-641; c.1849-c.1923)** domains |

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

#### VCEP Specification

| Strength | Points | Threshold |
|----------|--------|-----------|
| **PM2_Supporting** | 1 | Variant is **absent in hemizygotes** AND has a maximum allele frequency of **<0.00017% (0.0000017)** in heterozygotes in the latest version of gnomAD |

**Additional Requirement:** Use the highest population MAF from a **non-bottleneck population** from the latest version of gnomAD.

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **PM4 (Moderate)** | 2 | Used as written in the original ACMG/AMP guideline: protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants (Modification Type: No change) |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

| Strength | Points | Application |
|----------|--------|-------------|
| **PM5 (Moderate)** | 2 | Applied for **1 pathogenic variant** with no benign variation at the residue |
| **PM5_Supporting** | 1 | Applied for **1 likely pathogenic variant** with no benign variation at the residue |

#### Requirements

- Splicing abnormalities (using VCEP-specified prediction algorithms or evidence from literature) should be excluded for all missense variants
- The other variant(s) used for evidence should also have been curated using the Perox VCEP rule specifications and must reach a pathogenic/likely pathogenic classification **without PM5**

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

#### VCEP Specification (Default Point Value: 2; Modification Type: Disease-specific)

See the [PS2 specification](#ps2---de-novo-confirmed). Use the SVI-recommended point system at the **2nd tier** for probands meeting **PP4** and at the **1st tier** for probands meeting **PP4_Moderate**, applying the "Assumed de novo" column of the points table.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

#### VCEP Specifications

Segregations can be counted **across families**. All individuals counted for segregation must be **genotype positive AND phenotype positive**. In the absence of a pedigree available to determine relationships, segregations among related individuals can be counted conservatively (assuming closest relationships).

| Strength | Points | Application |
|----------|--------|-------------|
| **PP1_Strong** | 4 | 3 affected segregations (in addition to proband) |
| **PP1_Moderate** | 2 | 2 affected segregations (in addition to proband) |
| **PP1_Supporting** | 1 | 1 affected segregation (in addition to proband) |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **PP3_Supporting** | 1 | For **missense variants**, use **REVEL with a score of >0.85**. For **variants with a splicing impact (loss of canonical splice sites AND creation of cryptic sites)**, use **SpliceAI with a score of ≥ 0.5** |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

#### VCEP Specifications

- Use the **ABCD1 PP4 phenotype table** (below) to determine the appropriate PP4 strength level
- When multiple unrelated individuals are reported with the variant, use the proband that would meet the highest strength level for PP4 and count the remaining ones (at least meeting PP4_supporting strength) toward **PS4**

| Strength | Points |
|----------|--------|
| **PP4_Moderate** | 2 |
| **PP4 (Supporting)** | 1 |

**PP4_Strong is not specified by the VCEP.**

#### Evidence Types

| Code | Evidence |
|------|----------|
| **A** | Primary adrenal insufficiency |
| **B** | Myelopathy with or without peripheral neuropathy (adrenomyeloneuropathy, AMN) |
| **C** | Rapidly progressive inflammatory white matter demyelination developing in childhood (childhood cerebral ALD, CCALD), adolescence (adolescent cerebral ALD) or, less frequently, adulthood |
| **D** | Family history: family members affected with any of the described phenotypes, with an X-linked inheritance pattern (within a family, different phenotypes, including just elevated VLCFAs, can be present). At least one family member affected should be a male |
| **E** | Panel-based testing OR exome/genome sequencing excluding other peroxisomal disorders (*ACOX1*, *HSD17B4*, *ACBD5*, and all *PEX* genes except *PEX7*). If *ABCD1* is sequenced as a single-gene test, exclusion of the 4 pseudogenes (on chromosomes 2, 10, 16 & 22) is assumed |
| **F** | Abnormal diagnostic testing - abnormal results for any **ONE** of the following is sufficient: (1) abnormal biochemical genetic testing: increased plasma or serum C26:0 with elevated C24:0 to C22:0 and C26:0 to C22:0 ratios (VLCFA testing); indicating "abnormal" test result is sufficient (specific values are not necessary); **OR** (2) abnormal biochemical genetic testing: increased C26:0-lysophosphatidylcholine and ratios; indicating "abnormal" test result is sufficient (specific values are not necessary); **OR** (3) decreased beta-oxidation activity / absence of ALDP on immunoblot / mislocalization by immunofluorescence in patient cells (fibroblasts) |

#### PP4 Evidence Combinations

Each column indicates the criteria required to reach supporting or moderate PP4 strength level.

| Strength | Sex | Combination | Clinical findings (A / B / C) | Family history (D / E) | Diagnostic testing (F) |
|----------|-----|-------------|-------------------------------|------------------------|------------------------|
| **Supporting** | Male | 1 | A OR B OR C | NR | F |
| **Supporting** | Male | 2 | A OR (B OR C) | D | NA (**) |
| **Supporting** | Male | 3 | NR (*) | D OR E | F |
| **Supporting** | Female | 4 | B | NR | F |
| **Supporting** | Female | 5 | A¥ OR C¥ OR NR (*) | D | F |
| **Moderate** | Male | 6 | A OR B OR C | D OR E | F |
| **Moderate** | Female | 7 | NR (for A) / B€ (for B, C) | D OR E | F |
| **Moderate** | Female | 8 | NR (*) | D AND E | F |

**Legend:**
- **NR** = Not Required; **NA** = Not available
- **(\*)** Asymptomatic patient
- **(\*\*)** Biochemical genetic testing results are NOT reported/available. Does NOT apply to negative results.
- **¥** Very rare in females as an isolated phenotype
- **€** Adult patient

#### PP4 Clinical Notes

- Primary adrenal insufficiency is characterized by low cortisol production despite high ACTH. Lifetime prevalence in males with ABCD1 deficiency is ~80%; onset is typically in the first decade of life. Adrenal insufficiency is rare in women carrying ABCD1 pathogenic variants (~1% of patients). Adrenal insufficiency has also been reported in patients with Zellweger spectrum disorder.
- AMN manifests as slowly progressive spastic paraparesis and sensory ataxia, with onset in the 2nd to 5th decade in men and usually later (5th decade) in women. ~70% of males with AMN will also develop adrenal insufficiency. AMN is the most common clinical presentation in women, with approximately half developing myelopathy and/or peripheral neuropathy over time.
- Cerebral ALD: if untreated, patients rapidly develop severe cognitive and motor disability; death occurs on average 2 years after symptom onset. Cerebral ALD in women is exceedingly rare.
- Approximately 20% of women carrying an ABCD1 pathogenic variant have normal VLCFA results in plasma/serum (evidence E), even when symptomatic. C26:0-lysophosphatidylcholine in dried blood spots or plasma has much higher sensitivity for detecting ALD heterozygotes (evidence F).
- Abnormal biochemical genetic testing is present in patients with Zellweger spectrum disorder (ZSD) and other peroxisomal disorders, although the overall clinical presentation is usually suggestive of ABCD1 deficiency.
- ABCD1 pseudogene exclusion (PMID: 9215666; PMID: 35053399) is not required for application of PP4, but is essential to note in curations when available.

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

#### VCEP Specification

| Strength | Threshold |
|----------|-----------|
| **BA1 (Stand Alone)** | Total Grpmax filtering allele frequency (FAF) cutoff of **≥0.017% (0.00017)** from the most recent version of gnomAD |

##### Calculation Parameters (Whiffin-Ware Calculator)

- Prevalence: 1 in 5,000 (actual prevalence in hemizygotes and heterozygotes is reported to be 1 in 16,800 - GeneReviews, Bezman et al. 2001; however, a more conservative BA1 was designated based on a value 1 order of magnitude higher than the BS1 cut-off)
- Penetrance: 60% (based on penetrance in heterozygotes by expert judgment)
- Maximum allelic contribution and maximum genetic contribution: 100%

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### VCEP Specification

| Strength | Points | Threshold |
|----------|--------|-----------|
| **BS1 (Strong)** | −4 | Total Grpmax filtering allele frequency (FAF) cutoff of **≥0.0017% (0.000017)** from the most recent version of gnomAD |

##### Calculation Parameters (Whiffin-Ware Calculator)

- Prevalence: 1 in 50,000 (upper limit of prevalence range in hemizygotes; GeneReviews)
- Penetrance: 60% (based on penetrance in heterozygotes by expert judgment)
- Maximum allelic contribution and maximum genetic contribution: 100%

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **BS2 (Strong)** | −4 | Applicable when **>10 hemizygous healthy adult (>40y) males** are observed |

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **BS3_Supporting** | −1 | Applicable for **beta-oxidation activity assay in ALD fibroblasts transfected with variant, showing >57% activity of WT** (PMID: 34946879) |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **BS4 (Strong)** | −4 | Use as is when there is a lack of segregation in **1 affected male** in the family in addition to the proband |

---

### BP2 - Observed in cis with Pathogenic Variant

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **BP2_Supporting** | −1 | Use when the variant is found to be **in cis with another pathogenic variant**. The "in-cis" variant should also be curated by the Perox VCEP to apply the rule |

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **BP4_Supporting** | −1 | For **missense variants**, use **REVEL with a score of ≤ 0.5 AND SpliceAI with a score < 0.1**. For **variants with splicing impact** (exonic and intronic variants; not applicable for UTR variants), use **SpliceAI with a score < 0.1** |

---

### BP7 - Synonymous/Intronic Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

#### VCEP Specification

| Strength | Points | Application |
|----------|--------|-------------|
| **BP7_Supporting** | −1 | Can be applied to **synonymous variants meeting BP4 criteria** OR **intronic variants meeting BP4 criteria that are beyond the Walker et al. (PMID: 37352859) defined splice region of +7/−21** |

**Note:** Conservation does **not** have to be considered for this code to apply.

---

## 4. Not Applicable Criteria

The following ACMG/AMP criteria are **NOT APPLICABLE** for ABCD1 variant interpretation:

| Criterion | Original Purpose | Reason Not Applicable |
|-----------|-----------------|----------------------|
| **PM3** | In trans with a pathogenic variant (recessive disorders) | Not Applicable (ABCD1-related disease is X-linked) |
| **PP2** | Low rate of benign missense variation | Not applicable. ABCD1 is not constrained for missense (Z score: 1.87) variants |
| **PP5** | Reputable source reports pathogenic | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |
| **BP1** | Missense in truncating disease gene | Not applicable. Missense variants are also known to cause disease |
| **BP3** | In-frame deletion/insertion in repetitive region | Not applicable. Repetitive regions without a known function are not well-described in ABCD1 |
| **BP5** | Alternate molecular basis for disease | Not applicable. Adrenoleukodystrophy has variable age of onset and there is variable expressivity in affected individuals |
| **BP6** | Reputable source reports benign | Not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229) |

---

## 5. Rules for Combining Criteria

The Perox VCEP has adopted the **Bayesian points scale** for all criteria combinations (Tavtigian et al., 2020; PMID: 32720330 - Table 2 for the points scale; PMID: 29300386 - Supplementary Excel table for rule combinations).

**Implementation note:** The ClinGen Variant Curation Interface (VCI) currently uses the 2015 ACMG/AMP criteria combinations for pathogenicity classifications. In curations where the VCI classification differs from the Bayesian interpretation, curators will have to manually modify the classification.

### Point Values for ACMG/AMP Strength of Evidence Categories

| Evidence Strength | Pathogenic | Benign |
|-------------------|-----------|--------|
| Indeterminate | 0 | 0 |
| Supporting | 1 | −1 |
| Moderate | 2 | −2 |
| Strong | 4 | −4 |
| Very Strong | 8 | −8 |

### Point-Based Variant Classification Categories

| Category | Point Range |
|----------|-------------|
| **Pathogenic** | ≥ 10 |
| **Likely Pathogenic** | 6 to 9 |
| **Uncertain Significance** | 0 to 5 |
| **Likely Benign** | −1 to −6 |
| **Benign** | ≤ −7 |

### ABCD1 Default Point Values by Criterion

| Criterion | Strength(s) specified | Default point value(s) |
|-----------|----------------------|------------------------|
| PVS1 | Very Strong (with Strong/Moderate via decision tree) | 8 |
| PS1 | Strong; Moderate | 4; 2 |
| PS2 | Strong | 4 |
| PS3 | Supporting | 1 |
| PS4 | Very Strong; Strong; Moderate; Supporting | 8; 4; 2; 1 |
| PM1 | Moderate | 2 |
| PM2 | Supporting | 1 |
| PM3 | Not Applicable | — |
| PM4 | Moderate | 2 |
| PM5 | Moderate; Supporting | 2; 1 |
| PM6 | Moderate | 2 |
| PP1 | Strong; Moderate; Supporting | 4; 2; 1 |
| PP2 | Not Applicable | — |
| PP3 | Supporting | 1 |
| PP4 | Moderate; Supporting | 2; 1 |
| PP5 | Not Applicable | — |
| BA1 | Stand Alone | Not Applicable |
| BS1 | Strong | −4 |
| BS2 | Strong | −4 |
| BS3 | Supporting | −1 |
| BS4 | Strong | −4 |
| BP1 | Not Applicable | — |
| BP2 | Supporting | −1 |
| BP3 | Not Applicable | — |
| BP4 | Supporting | −1 |
| BP5 | Not Applicable | — |
| BP6 | Not Applicable | — |
| BP7 | Supporting | −1 |

---

## 6. Appendices

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold (gnomAD, Total Grpmax FAF) | Strength |
|-----------|--------------------------------------|----------|
| **BA1** | ≥ 0.017% (0.00017) | Stand Alone |
| **BS1** | ≥ 0.0017% (0.000017) | Strong |
| **PM2** | < 0.00017% (0.0000017) in heterozygotes AND absent in hemizygotes | Supporting |

### Appendix B: In Silico Thresholds Summary

| Tool | Criterion | Threshold |
|------|-----------|-----------|
| REVEL | PP3_Supporting (missense) | > 0.85 |
| SpliceAI | PP3_Supporting (splicing impact) | ≥ 0.5 |
| REVEL | BP4_Supporting (missense) | ≤ 0.5 (AND SpliceAI < 0.1) |
| SpliceAI | BP4_Supporting (splicing impact) | < 0.1 |
| Splice region definition | BP7_Supporting | Beyond +7/−21 (Walker et al., PMID: 37352859) |

### Appendix C: Key References

| Citation | PMID | Topic |
|----------|------|-------|
| Richards et al., 2015 | 25741868 | ACMG/AMP Variant Interpretation Guidelines (editorial addition — PMID not printed in the spec documents) |
| Tavtigian et al., 2020 | 32720330 | Bayesian points scale (Table 2) |
| Tavtigian et al., 2018 | 29300386 | Rule combinations (Supplementary Excel table) |
| Abou Tayoun et al., 2018 | 30192042 | ClinGen SVI PVS1 recommendations |
| Biesecker et al. / SVI VCEP Review Committee | 29543229 | PP5 and BP6 not for use |
| Walker et al., 2023 | 37352859 | Splice region definition (+7/−21); RNA evidence |
| — | 34946879 | Beta-oxidation activity assay, BS3_Supporting >57% of WT |
| — | 9215666 | ABCD1 pseudogenes |
| — | 35053399 | Dutch ABCD1 database |

### Appendix D: PP4 Phenotype Table References

1. Huffnagel IC, et al. The Natural History of Adrenal Insufficiency in X-Linked Adrenoleukodystrophy: An International Collaboration. J Clin Endocrinol Metab. 2019;104(1):118-126. PMID: 30252065
2. Engelen M, et al. X-linked adrenoleukodystrophy (X-ALD): clinical presentation and guidelines for diagnosis, follow-up and management. Orphanet J Rare Dis. 2012;7:51
3. Engelen M, et al. X-linked adrenoleukodystrophy in women: a cross-sectional cohort study. Brain. 2014;137(Pt 3):693-706
4. Schirinzi T, et al. Natural history of a cohort of ABCD1 variant female carriers. Eur J Neurol. 2019;26(2):326-332
5. Huffnagel IC, et al. Comparison of C26:0-carnitine and C26:0-lysophosphatidylcholine as diagnostic markers in dried blood spots from newborns and patients with adrenoleukodystrophy. Mol Genet Metab. 2017;122:209-15
6. Turk BR, et al. X-linked adrenoleukodystrophy: Pathology, pathophysiology, diagnostic testing, newborn screening and therapies. Int J Dev Neurosci. 2020;1-21
7. Jaspers YRJ, et al. Comparison of the Diagnostic Performance of C26:0-Lysophosphatidylcholine and Very Long-Chain Fatty Acids Analysis for Peroxisomal Disorders. Front Cell Dev Biol. 2020;8:690

### Appendix E: Supplementary Documents in the Specification

| Document | Content |
|----------|---------|
| ABCD1 PP4 phenotype table | PP4 evidence types, combinations and clinical notes |
| PS2 table | SVI de novo points-per-proband table and strength thresholds |
| PVS1 tables | ABCD1 exon table with canonical splice defect outcomes; PVS1 decision tree |
| ABCD1_PVS1_decisiontree | ABCD1-modified PVS1 decision tree (NM_000033.4) |
| ABCD1 rules for combining criteria | Bayesian points scale and point-based classification categories |
| ABCD1 functional assays | Approved beta-oxidation, immunoblotting and immunofluorescence assay instances |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | April 6, 2026 | Initial released ABCD1 specifications (Peroxisomal Disorders VCEP) |

---

*This document is based on the ClinGen Peroxisomal Disorders Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for ABCD1 Version 1.0 (https://cspec.genome.network/cspec/ui/svi/doc/GN105; DOI: 10.5281/zenodo.21434373)*
