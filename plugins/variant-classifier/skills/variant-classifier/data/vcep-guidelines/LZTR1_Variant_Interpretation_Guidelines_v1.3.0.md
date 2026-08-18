# ClinGen RASopathy VCEP Variant Interpretation Guidelines for LZTR1

**Version:** 1.3
**Released:** 12/3/2024
**Affiliation:** RASopathy VCEP
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines
**DOI:** 10.5281/zenodo.21434326

> **Repository version reconciled (2026-08-18):** The governing ClinGen PDF and GN094 package metadata identify this specification as **version 1.3**. The guideline file and registry `guideline_file` were previously carried as `v2.0.0`; both have been renamed to `LZTR1_Variant_Interpretation_Guidelines_v1.3.0.md` to match the registry `1.3.0` entry. The registry `version` field was already `1.3.0` and is unchanged.

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | LZTR1 (HGNC:6742) |
| **HGNC Name** | Leucine zipper like transcription regulator 1 |
| **Transcript** | NM_006767.4 |
| **Disease** | RASopathy (MONDO:0021060) |
| **Inheritance** | Autosomal recessive inheritance, Autosomal dominant inheritance |

---

## Table of Contents

1. [Pathogenic Criteria](#pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PS4 - Prevalence in Affected](#ps4---prevalence-in-affected)
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
   - [BA1 - Allele Frequency >5%](#ba1---allele-frequency-5)
   - [BS1 - Frequency Greater Than Expected](#bs1---frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (No Effect)](#bs3---functional-studies-no-effect)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP1-BP7 - Benign Supporting](#bp1-bp7---benign-supporting)
3. [Rules for Combining Criteria](#rules-for-combining-criteria)
4. [Appendices](#appendices)
   - [Appendix A: Population Frequency Thresholds Summary](#appendix-a-population-frequency-thresholds-summary)
   - [Appendix B: Computational Predictor Thresholds](#appendix-b-computational-predictor-thresholds)
   - [Appendix C: Key PMIDs and References](#appendix-c-key-pmids-and-references)
   - [Appendix D: RASopathy Phenotype Reference](#appendix-d-rasopathy-phenotype-reference)
   - [Appendix E: Distributed Package and Source-Fidelity Notes](#appendix-e-distributed-package-and-source-fidelity-notes)
   - [Appendix F: Pilot-Variant Source Notes](#appendix-f-pilot-variant-source-notes)

---

## Important Notes

### Case Level Inheritance Determination

The distributed `Case Level Inheritance Flowchart.pdf` determines which ACMG/AMP criteria can be applied to autosomal dominant (AD) versus autosomal recessive (AR) LZTR1 variants. Its visual arrow topology is:

1. **Step 1 — case data:** branch to AD, AR, or Unknown inheritance.
2. **AD:** follow the standard RASopathy specifications and score case evidence with PS4.
3. **AR:** include PVS1, PM3, and PM2_Supporting assessments. The flowchart prints `AF <0.0025%` for this branch.
4. **Unknown — Step 2, variant data:**
   - a typical loss-of-function variant flows to AR;
   - a missense, atypical loss-of-function, or unique variant with functional data has dotted paths to **both AD and AR**;
   - such a variant without functional data flows to VUS.

**Application constraints:**

- PVS1 applies only when curating AR disease.
- Dominant-negative variants use point-based scoring for AD cases.
- Loss-of-function usage is case-specific according to inheritance.
- Only PS4 **or** PM3 can be applied to a single case, not both.
- AR Noonan syndrome cases use PM3; AD isolated schwannomatosis cases use PS4.

> **Source contradiction — do not resolve silently:** The inheritance flowchart prints the strict AR threshold **AF <0.0025%**, whereas the main PDF's PM2 criterion prints **PM2_P ≤0.0025%**. Both source presentations are retained; the package does not identify which comparator controls at the boundary.

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/-1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7)
- Use caution interpreting LOF variants at the extreme 3' end of a gene
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact
- Use caution in the presence of multiple transcripts

**VCEP Specifications:** Follow SVI recommendations for application. **This rule can be applied when curating for AR disease only.** Please reference the attached, LZTR1-specific PVS1 Decision Tree before applying PVS1.

#### Strength Levels

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Very Strong (PVS1)** | Null variant in a gene where loss of function is a known mechanism of disease | Disease-specific, Gene-specific |
| **Strong (PVS1_Strong)** | Null variant in a gene where loss of function is a known mechanism of disease | Disease-specific, Gene-specific, Strength |
| **Moderate (PVS1_Moderate)** | Null variant in a gene where loss of function is a known mechanism of disease | Disease-specific, Gene-specific, Strength |
| **Supporting (PVS1_Supporting)** | Null variant in a gene where loss of function is a known mechanism of disease | Disease-specific, Gene-specific, Strength |

#### PVS1 Decision Tree

The following generic-looking decision tree is not a local graft: `PVS1 Decision Tree.jpg` is one of the nine artifacts distributed in the GN094 LZTR1 package. Its LZTR1-specific annotations identify NM_006767.4, the NMD cutoff, and the in-frame exons below.

**For Nonsense or Frameshift variants:**

| Scenario | Exon Status | NMD Prediction | Strength |
|----------|-------------|----------------|----------|
| Predicted to undergo NMD (`c.2357` or `p.786` are the terminal nucleotide and codon, respectively, predicted to undergo NMD) | Present in biologically-relevant transcript(s) (NM_006767.4) | Yes | PVS1 |
| Predicted to undergo NMD | Absent from biologically-relevant transcript(s) | Yes | N/A |
| Not predicted to undergo NMD | LoF variants in exon frequent OR exon absent from relevant transcript | - | N/A |
| Not predicted to undergo NMD | LoF not frequent, exon present, variant removes >10% of protein | - | PVS1_Strong |
| Not predicted to undergo NMD | LoF not frequent, exon present, variant removes <10% of protein | - | PVS1_Moderate |

**For GT-AG +/-1,2 splice site variants:**

| Scenario | NMD/Reading Frame | Strength |
|----------|-------------------|----------|
| Exon skipping or cryptic splice disrupts reading frame, predicted to undergo NMD | Exon present in relevant transcript | PVS1 |
| Exon skipping or cryptic splice disrupts reading frame, NOT predicted to undergo NMD | LoF frequent OR exon absent | N/A |
| Exon skipping or cryptic splice disrupts reading frame, NOT predicted to undergo NMD, LoF not frequent, exon present | Removes >10% of protein | PVS1_Strong |
| Exon skipping or cryptic splice disrupts reading frame, NOT predicted to undergo NMD, LoF not frequent, exon present | Removes <10% of protein | PVS1_Moderate |
| Exon skipping preserves reading frame (Exons 10, 11, 12, 13, 20, 21 are in frame) | LoF frequent OR exon absent | N/A |
| Exon skipping preserves reading frame, LoF not frequent, exon present | Removes >10% of protein | PVS1_Strong |
| Exon skipping preserves reading frame, LoF not frequent, exon present | Removes <10% of protein | PVS1_Moderate |

**For Deletion variants:**

| Type | NMD/Function | Strength |
|------|--------------|----------|
| Full gene deletion | - | PVS1^d |
| Single to multi exon deletion - Disrupts reading frame, predicted to undergo NMD | Exon present in relevant transcript | PVS1 |
| Single to multi exon deletion - Disrupts reading frame, predicted to undergo NMD | Exon absent | N/A |
| Single to multi exon deletion - Disrupts reading frame, NOT predicted to undergo NMD | Truncated region critical to protein function | PVS1_Strong |
| Single to multi exon deletion - Disrupts reading frame, NOT predicted to undergo NMD | LoF frequent OR exon absent | N/A |
| Single to multi exon deletion - Disrupts reading frame, NOT predicted to undergo NMD, LoF not frequent, exon present | Removes >10% of protein | PVS1_Strong |
| Single to multi exon deletion - Disrupts reading frame, NOT predicted to undergo NMD, LoF not frequent, exon present | Removes <10% of protein | PVS1_Moderate |
| Single to multi exon deletion - Preserves reading frame | Truncated region critical to protein function | PVS1_Strong |
| Single to multi exon deletion - Preserves reading frame | Role unknown and LoF frequent OR region absent from relevant transcript | N/A |
| Single to multi exon deletion - Preserves reading frame, role unknown, LoF not frequent, region present | Removes >10% of protein | PVS1_Strong |
| Single to multi exon deletion - Preserves reading frame, role unknown, LoF not frequent, region present | Removes <10% of protein | PVS1_Moderate |

**For Duplication variants (>=1 exon, completely contained within gene):**

| Tandem Status | Reading Frame Impact | Strength |
|---------------|---------------------|----------|
| Proven in tandem | Reading frame disrupted, NMD predicted | PVS1 |
| Proven in tandem | No or unknown impact on reading frame/NMD | N/A |
| Presumed in tandem | Reading frame presumed disrupted, NMD predicted | PVS1_Strong |
| Proven not in tandem | - | N/A |

**For Initiation Codon variants:**

| Alternative Start | Upstream P/LP Variants | Strength |
|-------------------|------------------------|----------|
| No known alternative start codon in other transcripts | >=1 pathogenic variant(s) upstream of closest potential in-frame start codon | PVS1_Moderate |
| No known alternative start codon in other transcripts | No pathogenic variant(s) upstream | PVS1_Supp |
| Different functional transcript uses alternative start | - | N/A |

> **Decision-tree source limitations:** The image uses strict **>10%** and **<10%** branches and gives no path for exactly 10%. It also prints `PVS1` with superscript `d` for a full-gene deletion but defines no footnote `d` anywhere in the image or distributed package. These gaps are reported without inferring a rule.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Example:** Val->Leu caused by either G>C or G>T in the same codon.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (PS1)** | Same amino acid change as a previously established pathogenic variant in LZTR1 regardless of nucleotide change | No change |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PM6 (see Reference 1) and phenotypic specifications.

#### PS2/PM6 Point System

| Phenotypic Consistency | Confirmed *de novo* (PS2) | Assumed *de novo* (PM6) |
|------------------------|---------------------------|-------------------------|
| Phenotype is consistent with a RASopathy* | 2 points | 1 point |
| Limited phenotypic information** | 1 point | 0.5 points |
| Phenotype not consistent with RASopathy | 0 points | 0 points |

*\*Exclusive of prenatal cases*

*\*\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.*

#### Evidence Strength Thresholds

The main PDF's displayed PS2 block contains Very Strong (4 points), Strong (2), and Moderate (1), but no Supporting row. Its displayed PM6 block contains Strong (2), Moderate (1), and Supporting (0.5), but no Very Strong row. The distributed `PS2_PM6 Scoring.jpg` instead presents this shared exact-value scale:

| Points (exact values printed in image) | Strength Level |
|--------|----------------|
| 0.5 | Supporting (PS2_Supporting or PM6_Supporting) |
| 1.0 | Moderate (PS2_Moderate or PM6) |
| 2.0 | Strong (PS2 or PM6_Strong) |
| 4.0 | Very Strong (PS2_VeryStrong or PM6_VeryStrong) |

> **Source discrepancy — do not resolve silently:** `PS2_PM6 Scoring.jpg` adds PS2_Supporting and PM6_VeryStrong to the strengths shown in the respective PDF criterion blocks. The image prints exact point values without comparator symbols. Both presentations are retained; the package does not state which controls when they differ.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**Note:** Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Approved assays for PS3 usage are available in the supplemental materials.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate (PS3_Moderate)** | Two or more different approved assays | Gene-specific, Strength |
| **Supporting (PS3_Supporting)** | One approved assay | Gene-specific, Strength |

#### Approved Functional Studies for LZTR1

The distributed `Approved Functional Studies.xlsx` contains four approved LZTR1 assay types. Every LZTR1 row designates **PS3_Supporting; BS3_NA**. Two or more different approved assay types support PS3_Moderate; a single approved assay supports PS3_Supporting.

The workbook's `READ ME` states that assays are evaluated under the functional-evidence framework (PMID 31892348), pathway-level controls may be shared across RASopathy genes, gene-specific assays require gene-specific controls, animal models and variant-specific assays are excluded, and an unlisted assay can receive at most PS3_Supporting or BS3_Supporting. That general allowance does not override the explicit **BS3_NA** designation for every approved LZTR1 assay below.

##### RAS Activation Assay

- **Citations:** Motta (2019), PMID 30481304, DOI 10.1093/hmg/ddy412; Bigenzahn (2018), PMID 30442766, DOI 10.1126/science.aap8210.
- **Materials/readout:** HEK293T cells; semi-quantitative RAS/RBD activation readout.
- **Replicates/controls/statistics:** Biological and technical replicates met; WT and mock controls; Student's t-test.
- **Thresholds:** WT-like activation is normal; increased RAS/RBD activation is abnormal.
- **Validation examples:** The row headed `5 Variants` / P/LP lists M91V (VUS), R170Q (P/LP), Y193H (LP/VUS), G248R (P/LP), and R284C (P). No B/LB validation examples are listed.
- **Approved strength:** PS3_Supporting; BS3_NA.

##### MEK Activation Assay

- **Citations:** Motta (2019), PMID 30481304, DOI 10.1093/hmg/ddy412; Bigenzahn (2018), PMID 30442766, DOI 10.1126/science.aap8210.
- **Materials/readout:** HEK293T cells; semi-quantitative MEK activation.
- **Replicates/controls:** Biological and technical replicates met; WT and mock controls.
- **Thresholds:** WT pattern is normal; constitutive, increased, and/or prolonged activation is abnormal **for AD LZTR1 variants only**.
- **Validation examples:** The row headed 17 P/LP variants includes entries labeled VUS, NA, or with mixed classifications. No B/LB validation examples are listed.
- **Approved strength:** PS3_Supporting; BS3_NA.

##### ERK Activation Assay

- **Citations:** Motta (2019), PMID 30481304, DOI 10.1093/hmg/ddy412; Bigenzahn (2018), PMID 30442766, DOI 10.1126/science.aap8210.
- **Materials/readout:** HEK293T cells; semi-quantitative ERK activation.
- **Replicates/controls:** Biological and technical replicates met; WT and mock controls.
- **Thresholds:** WT pattern is normal; constitutive, increased, and/or prolonged activation is abnormal **for AD LZTR1 variants only**.
- **Validation examples:** The row headed 14 P/LP variants includes entries labeled VUS, NA, or with mixed classifications. No B/LB validation examples are listed.
- **Approved strength:** PS3_Supporting; BS3_NA.

##### LZTR1 Stability and Localization Assay

| Parameter | Details |
|-----------|---------|
| **PMID / DOI** | 30481304 / 10.1093/hmg/ddy412; 30442766 / 10.1126/science.aap8210 |
| **Authors / year** | Motta, 2019; Bigenzahn, 2018 |
| **Assay description** | Expression, stability, and localization of Noonan-syndrome and dominant-schwannomatosis LZTR1 variants |
| **Material used** | Transfected COS-1 cells basally and after CHX treatment; transfected HeLa and HEK293T cells under basal conditions |
| **Readout type** | Semi-quantitative (qualitative) |
| **Biological / technical replicates** | Met / met; stability and localization assayed in tandem |
| **Controls** | WT; empty, LZTR1 ΔBTB2, ΔKelch, and/or ΔBTB1+2 |
| **Statistical analysis** | Student's t-test |
| **Threshold for normal** | Normal LZTR1 protein abundance/Golgi localization; observed for dominant-negative variants and a subset of LoF variants |
| **Threshold for abnormal** | Reduced LZTR1 abundance/abnormal cellular localization; applies to a subset of LoF variants in recessive Noonan syndrome |
| **Approved strength** | PS3_Supporting; BS3_NA |
| **Limitation** | Limited control availability and inter-laboratory reproducibility restrict this gene-specific assay to Supporting |

The P/LP-headed row labeled 7 variants lists H121D (P), E217A (NA), E563Q (LP), I821T (VUS), V456G (NA), P520L (VUS), and R688C (LP/VUS). The B/LB-headed row contains 12 entries whose adjacent labels are instead P/LP, VUS, NA, or mixed, including M91V, R170Q, Y193H, Y193N, G286R, M400R, S247N, G248R, and R284C.

> **Workbook contradictions — do not resolve silently:** Several validation rows have headings inconsistent with their entry-level classifications, most conspicuously the stability/localization B/LB row. These source labels are reported without reclassifying any variant. Normal readouts do **not** support BS3 under this package because every approved LZTR1 row explicitly says BS3_NA.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Note 1:** Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0.

**Note 2:** In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** Please reference the Case Level Inheritance Flowchart before applying PS4.

**For Dominant-negative variants:** Strength adjustment using point-based scoring for autosomal dominant cases with RASopathy phenotypic specifications.

**For Dominant loss-of-function variants:** Usage of this rule is case specific based on the inheritance of the variant and only PS4 OR PM3 can be applied to a single case. 1 point awarded for autosomal dominant cases with isolated schwannomatosis consistent with the loss-of-function disease mechanism. Loss-of-function variants observed in cases with autosomal recessive NS should only be counted using PM3.

#### PS4 Point System

| Phenotypic Consistency | Points per Proband |
|------------------------|-------------------|
| Individual well-phenotyped with features of a RASopathy | 1 |
| Limited phenotypic information compatible with RASopathy* | 0.5 |
| No clinical information or isolated clinical features | 0 |
| Well-phenotyped but consistent with non-RASopathy disorder** | -1 |

*\*Applicable to prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES). Phenotypes for prenatal cases include hypertrophic cardiomyopathy, increased nuchal translucency, cystic hygroma, or hydrops.*

*\*\*Negative points for PS4 represent proband affected with a non-RASopathy congenital disorder rather than a healthy individual (BS2). This typically applies to probands tested by exome analysis with multiple other clinical features supporting a distinct syndromic disorder (e.g. CHARGE, CdLS).*

#### PS4 Evidence Strength Thresholds

| Aggregate points (main PDF) | Strength Level |
|--------|----------------|
| >=1 | Supporting (PS4_Supporting) |
| >=3 | Moderate (PS4_Moderate) |
| >=5 | Strong (PS4) |

> **Source discrepancy — do not resolve silently:** The main PDF explicitly prints the inclusive thresholds **≥1**, **≥3**, and **≥5**. The distributed `PS4 Scoring.jpg` labels the corresponding strength rows with exact **1**, **3**, and **5** values and no comparator symbols. Both presentations are retained; do not convert the image's values into inferred inequalities.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** *Not Applicable*

**Comments:** Not applicable at this time.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:** The variant must be absent from controls (gnomAD). For variants in LZTR1, PM2_P <=0.0025% may be applied to support AR disease.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting (PM2_Supporting)** | The variant must be absent from controls (gnomAD). For variants in LZTR1, PM2_P <=0.0025% may be applied to support AR disease. | Disease-specific, Gene-specific, Strength |

> **Source contradiction — do not resolve silently:** `Case Level Inheritance Flowchart.pdf` assigns PM2_Supporting to the AR branch with **AF <0.0025%**, while the main PDF uses **PM2_P ≤0.0025%**. The threshold boundary is therefore inconsistent within the distributed package.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Please reference the Case Level Inheritance Flowchart before applying PM3.

Usage of this rule is case specific based on the inheritance of the variant and only PS4 OR PM3 can be applied to a single case. Cases with autosomal recessive NS are scored using PM3, as defined by SVI. Cases with autosomal dominant isolated schwannomatosis should be counted using PS4.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Very Strong (PM3_VeryStrong)** | >=4 points | Disease-specific, Gene-specific, Strength |
| **Strong (PM3_Strong)** | >=2 points | Disease-specific, Gene-specific, Strength |
| **Moderate (PM3)** | >=1 points | Disease-specific, Gene-specific |
| **Supporting (PM3_Supporting)** | >=0.5 points | Disease-specific, Gene-specific, Strength |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Moderate (PM4)** | No known repetitive areas in gene. Use as described. | General recommendation |

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Example:** Arg156His is pathogenic; now you observe Arg156Cys.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** Applicable for observed analogous residue positions in LZTR1. PM1 and PM5 may be used in conjunction at moderate levels, however, PM1 may not be applied if PM5_Strong is applied to avoid overweighting.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (PM5_Strong)** | >=2 different [likely] pathogenic residue changes at the same codon observed in >=5 probands | Strength |
| **Moderate (PM5)** | 1 [likely] pathogenic residue change at the same codon | Disease-specific |

The version 1.3 release note states that “Observed in ≥5 probands” was removed from PM5 at Moderate strength. The requirement remains printed for PM5_Strong. The PDF also retains its PM1/PM5 co-application sentence even though PM1 is designated Not Applicable; this source inconsistency is not resolved here.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Follow SVI recommendations for point-based scoring in conjunction with PS2 (see Reference 1) and phenotypic specifications: full points awarded with RASopathy phenotypes, reduced points applicable to cases with minimal phenotypic information (i.e. prenatal cases, cases with a clinical order of a RASopathy panel without clinical information, and cases with limited clinical information in other global tests (such as WES)).

| Strength | Points | Modification Type |
|----------|--------|-------------------|
| **Strong (PM6_Strong)** | 2 points | Strength |
| **Moderate (PM6)** | 1 point | None |
| **Supporting (PM6_Supporting)** | 0.5 points | Strength |

*See PS2 section for full point scoring table.*

`PS2_PM6 Scoring.jpg` additionally maps 4 exact points to PM6_VeryStrong, although the main PDF's displayed PM6 criterion block stops at Strong. See the PS2 source-discrepancy note; the supplement-only strength is reported without silently merging it into the PDF block.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** Segregation in more than one family is recommended.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (PP1_Strong)** | >=7 informative meioses | Strength |
| **Moderate (PP1_Moderate)** | >=5 informative meioses | Strength |
| **Supporting (PP1)** | >=3 informative meioses | Disease-specific |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** *Not Applicable*

**Comments:** Not applicable because missense z score is <3.09 in gnomAD.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:** For missense variants: REVEL >= 0.7. For splicing impact, predicted outcome must match disease mechanism.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Supporting (PP3)** | For missense variants: REVEL >= 0.7. For splicing impact, predicted outcome must match disease mechanism. | Disease-specific |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:** *Not Applicable*

**Comments:** PP4 is not applicable due to genetic heterogeneity.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** *Not Applicable*

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229)

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**VCEP Specifications:** GnomAD filtering allele frequency >=0.05%.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Stand Alone (BA1)** | GnomAD filtering allele frequency >=0.05% | Disease-specific |

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specifications:** GnomAD filtering allele frequency >=0.025%.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (BS1)** | GnomAD filtering allele frequency >=0.025% | Disease-specific |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** Strength adjustment using point-based scoring based on phenotypic specifications. Phenotypic specifications: based on healthy homozygote or heterozygote individuals, reduced points for apparently unaffected heterozygous individuals, applicable to parent or sibling samples during clinical family evaluations.

#### BS2 Point System

| Phenotypic Consistency | Points per Individual |
|------------------------|----------------------|
| Healthy homozygous individual assessed for a RASopathy | -3 |
| Healthy heterozygous individual assessed for a RASopathy | -1 |
| No phenotypic information other than "unaffected" heterozygote* | -0.25 |
| No clinical information or nonspecific clinical features | 0 |

*\*Typically applicable to parental or sibling samples during clinical family evaluations.*

#### BS2 Evidence Strength Thresholds

The main PDF body specifies **Strong at -4 points** and **Supporting at -1 point**; it does not display a Moderate row or comparator symbols for either value.

The distributed `BS2 Scoring.jpg` instead gives:

| Points (exact values printed in image) | Strength Level |
|--------|----------------|
| -1 | Supporting (BS2_Supporting) |
| N/A | Moderate (not applicable) |
| -3.0 | Strong (BS2) |

> **Source contradiction — do not resolve silently:** The PDF body assigns BS2 Strong at **-4**, whereas `BS2 Scoring.jpg` assigns Strong at **-3.0**. Neither source supplies a comparator for these totals. Both presentations are retained; no `≤` comparator is inferred.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** *Not Applicable*

**Comments:** Approved functional studies are available for each individual gene in the supplemental material. Additional functional studies can be submitted to the expert panel for approval.

All four approved LZTR1 assay rows in `Approved Functional Studies.xlsx` explicitly designate **BS3_NA**. A WT-like or normal readout in an approved LZTR1 assay must therefore not be converted into BS3 evidence under this package.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:** Lack of segregation in affected members of a family.

| Strength | Criteria | Modification Type |
|----------|----------|-------------------|
| **Strong (BS4)** | Requires only one informative meiosis | General recommendation |

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Specification |
|-----------|--------|---------------|
| **BP1** | *Not Applicable* | Not applicable, both missense and truncating variants can cause disease |
| **BP2** | Applicable | For each case, -1 point applies when phenotype inconsistent with a RASopathy and causative variant has been identified (ex. WES cases) OR alternative molecular cause of a RASopathy and the phenotype is consistent with expected severity of the RASopathy in the same gene (and/or in conjunction with BP5 in a different gene) |
| **BP3** | *Not Applicable* | No known benign repetitive areas in RASopathy genes |
| **BP4** | Applicable | For missense variants: REVEL <=0.3. For splicing variants: predicted outcome is negligible or does not match disease mechanism |
| **BP5** | Applicable | For each case, -1 point applies when phenotype inconsistent with a RASopathy and causative variant has been identified (ex. WES cases) OR alternative molecular cause of a RASopathy and the phenotype is consistent with expected severity of the RASopathy in a different gene (and/or in conjunction with BP2 in the same gene) |
| **BP6** | *Not Applicable* | This criterion is not for use as recommended by the ClinGen SVI VCEP Review Committee (PMID: 29543229) |
| **BP7** | Applicable | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. This rule is also applicable for intronic positions (except canonical splice sites) or non-coding variants and should be used in conjunction with BP4 |

#### BP2/BP5 Point System

| Phenotypic Consistency | Points per Individual |
|------------------------|----------------------|
| Phenotype inconsistent with a RASopathy and causative variant has been identified, **OR** Molecular cause of a RASopathy is identified in a different RASopathy gene, **OR** Molecular cause of a RASopathy is identified in *trans* or *cis* with the variant being classified | -1 |
| Phenotype inconsistent with a RASopathy and no causative variant identified/reported | 0 |

#### BP2/BP5 Evidence Strength Thresholds

The main PDF body defines inclusive aggregate thresholds for both BP2 and BP5:

| Aggregate points (main PDF) | Strength Level |
|--------|----------------|
| >=(-1) | Supporting (BP5/BP2) |
| >=(-2) | Moderate (BP5_Moderate/BP2_Moderate) |
| >=(-4) | Strong (BP5_Strong/BP2_Strong) |

The distributed `BP5_BP2 Scoring.jpg` instead gives:

| Points (exact values printed in image) | Strength Level |
|--------|----------------|
| -1 | Supporting (BP5/BP2) |
| N/A | Moderate (not applicable) |
| -3.0 | Strong (BP5_Strong/BP2_Strong) |

> **Source contradiction — do not resolve silently:** The PDF body prints **≥(-4)**, **≥(-2)**, and **≥(-1)**; the image prints exact **-3.0**, **N/A**, and **-1** with no comparator symbols. Both source presentations are retained and neither is converted into the other.

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1, PS2_VeryStrong, PM3_VeryStrong) **AND** >=1 Strong (PVS1_Strong, PS1, PS2, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Very Strong (PVS1, PS2_VeryStrong, PM3_VeryStrong) **AND** >=2 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) |
| 1 Very Strong (PVS1, PS2_VeryStrong, PM3_VeryStrong) **AND** 1 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) **AND** 1 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3) |
| 1 Very Strong (PVS1, PS2_VeryStrong, PM3_VeryStrong) **AND** >=2 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3) |
| >=2 Strong (PVS1_Strong, PS1, PS2, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** >=3 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 2 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) **AND** >=2 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 1 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) **AND** >=4 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3) |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong (PVS1, PS2_VeryStrong, PM3_VeryStrong) **AND** 1 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** 1 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) |
| 1 Strong (PVS1_Strong, PS1, PS2, PS4, PM3_Strong, PM5_Strong, PM6_Strong, PP1_Strong) **AND** >=2 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3) |
| >=3 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) |
| 2 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) **AND** >=2 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3) |
| 1 Moderate (PVS1_Moderate, PS2_Moderate, PS4_Moderate, PM3, PM4, PM5, PM6, PP1_Moderate) **AND** >=4 Supporting (PVS1_Supporting, PS3_Supporting, PS4_Supporting, PM2_Supporting, PM3_Supporting, PM6_Supporting, PP1, PP3) |

### Benign Classification

| Criteria Combination |
|---------------------|
| >=2 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) |
| 1 Stand Alone (BA1) |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) **AND** 1 Supporting (BS2_Supporting, BP1, BP2, BP4, BP5, BP7) |
| >=2 Supporting (BS2_Supporting, BP1, BP2, BP4, BP5, BP7) |
| 1 Strong (BS1, BS2, BS4, BP2_Strong, BP5_Strong) |
| 1 Strong (BS1) |

---

## Appendices

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength |
|-----------|-----------|----------|
| BA1 | >=0.05% (gnomAD FAF) | Stand Alone |
| BS1 | >=0.025% (gnomAD FAF) | Strong |
| PM2 | <=0.0025% (gnomAD FAF) | Supporting |

### Appendix B: Computational Predictor Thresholds

| Criterion | Tool | Threshold | Interpretation |
|-----------|------|-----------|----------------|
| PP3 | REVEL | >= 0.7 | Supports pathogenicity |
| BP4 | REVEL | <= 0.3 | Supports benign interpretation |

### Appendix C: Key PMIDs and References

| Reference | Description |
|-----------|-------------|
| PMID: 29543229 | ClinGen SVI recommendations for PP5/BP6 |
| PMID: 30311384 | RASopathy phenotype reference (Table 1) |
| PMID: 30481304 | Motta et al. - LZTR1 functional studies |
| PMID: 30442766 | Bigenzahn et al. - LZTR1 functional studies |
| SVI De Novo Criteria v1.1 | https://clinicalgenome.org/site/assets/files/3461/svi_proposal_for_de_novo_criteria_v1_1.pdf |

### Appendix D: RASopathy Phenotype Reference

For phenotypic assessment in PS2/PM6 and PS4 scoring, refer to Table 1 in PMID: 30311384 for consistent RASopathy phenotypes.

**Phenotypes for prenatal cases include:**
- Hypertrophic cardiomyopathy
- Increased nuchal translucency
- Cystic hygroma
- Hydrops

---

### Appendix E: Distributed Package and Source-Fidelity Notes

The GN094 metadata reports a complete version 1.3 package with nine downloaded source artifacts and no failures:

1. `ClinGen_ACMG_Specifications_LZTR1_v1.3.pdf`
2. `Case Level Inheritance Flowchart.pdf`
3. `Approved Functional Studies.xlsx`
4. `Pilot Variants.xlsx`
5. `PS4 Scoring.jpg`
6. `PVS1 Decision Tree.jpg`
7. `BS2 Scoring.jpg`
8. `BP5_BP2 Scoring.jpg`
9. `PS2_PM6 Scoring.jpg`

All PDF pages, all five JPGs (four scoring images and one decision tree), and all visible and hidden worksheets in both workbooks were inspected. Neither workbook contains embedded media or chart objects.

The following contradictions and source defects remain unresolved because the distributed package does not choose between them:

1. The PM2 PDF criterion uses **≤0.0025%**; the inheritance flowchart uses **<0.0025%**.
2. The PDF's displayed PS2 block omits Supporting and its displayed PM6 block omits Very Strong; `PS2_PM6 Scoring.jpg` includes both at exact 0.5 and 4 points, respectively.
3. The PS4 PDF body uses inclusive **≥1**, **≥3**, and **≥5**; `PS4 Scoring.jpg` prints exact 1, 3, and 5 values without comparators.
4. The BS2 PDF body gives Strong at **-4**; `BS2 Scoring.jpg` gives Strong at exact **-3.0**, with Moderate N/A and Supporting at exact -1.
5. The BP2/BP5 PDF body gives **≥(-4)** Strong, **≥(-2)** Moderate, and **≥(-1)** Supporting; `BP5_BP2 Scoring.jpg` gives exact -3.0 Strong, Moderate N/A, and exact -1 Supporting.
6. `PVS1 Decision Tree.jpg` leaves exactly 10% unassigned between its strict >10% and <10% branches and uses an undefined superscript `d` for full-gene deletion.
7. The PDF retains a PM1/PM5 co-application statement despite designating PM1 Not Applicable.
8. `Approved Functional Studies.xlsx` contains validation-row headings that conflict with entry-level classifications, especially the stability/localization B/LB row. All LZTR1 rows nevertheless agree on PS3_Supporting and BS3_NA.
9. `Pilot Variants.xlsx` applies PS1_M to c.1149+1G>T although the PDF defines PS1 only at Strong, applies BP3 to c.651+10_651+46del although the PDF defines BP3 Not Applicable, and uses a strict BA1 `>0.0005` summary for c.2373C>T although the PDF uses inclusive `≥0.05%` (≥0.0005 as a fraction).
10. The pilot workbook refers to “RASopathy VCEP specifications version 2,” while the governing LZTR1 PDF and GN094 metadata identify version 1.3.

These notes report source content; they do not reconcile conflicts, infer missing boundary rules, or reclassify workbook variants.

### Appendix F: Pilot-Variant Source Notes

`Pilot Variants.xlsx` tests the panel framework across 147 variants. The LZTR1 worksheet contains 24 populated rows. Representative applications include:

| Variant | Inheritance / classification in workbook | Applied evidence shown in workbook | Source note |
|---------|------------------------------------------|-------------------------------------|-------------|
| c.742G>A | AD / LP | PM2_P, PP3, PS3_P, PS4_M, PS2 | AD case and functional/de novo example |
| c.1084C>T | AR / P | PVS1, PM3 | Illustrates AR-only PVS1 use |
| c.1149+1G>T | AR / LP | PVS1_M, PM2_P, PM3, PS1_M | PS1_M conflicts with PDF's Strong-only PS1 |
| c.27dup | inheritance blank / P | PVS1, PS3_P | Inheritance is not inferred here |
| c.1234C>T | AD / VUS | PS4_P | AD case-level application |
| c.650A>C | AR / VUS | PM2_P, PS3_P, PM3_P | AR criteria plus functional evidence |
| c.1723G>A | not stated / VUS | BP4 | Workbook example |
| c.651+10_651+46del | not stated / LB | BP3, BP4, BP7 | BP3 conflicts with PDF's Not Applicable status |
| c.2373C>T | not stated / B | BA1, BP4, BP7 | Summary uses strict `>0.0005`, unlike PDF `≥0.05%` |

The workbook also includes c.850C>T (AD/LP), c.1149+1G>A (AR/LP), c.2178C>A (AR/P), c.842C>T (AD/P), and c.1687G>C (AR/VUS). Pilot entries are examples, not overrides of the governing criterion text.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.3 | 12/3/2024 | “Observed in ≥5 probands” removed from PM5 at Moderate strength |

**Document corrections (2026-08-07), source-verified against `ClinGen_ACMG_Specifications_LZTR1_v1.3.pdf`, `Case Level Inheritance Flowchart.pdf`, `Approved Functional Studies.xlsx`, `Pilot Variants.xlsx`, `PS4 Scoring.jpg`, `PVS1 Decision Tree.jpg`, `BS2 Scoring.jpg`, `BP5_BP2 Scoring.jpg`, and `PS2_PM6 Scoring.jpg`. No change to the underlying ClinGen specification version; the pre-existing filename/registry version mismatch was deliberately left unresolved.**

- Corrected the document metadata to identify the governing ClinGen source as version 1.3 and added its DOI, while leaving the v2.0.0 filename and registry untouched.
- Transcribed the inheritance-flowchart arrow topology, including Unknown-to-variant-data branching and the dotted functional-data paths to both AD and AR; reported its strict PM2 comparator against the PDF's inclusive comparator.
- Verified that the apparently generic PVS1 decision tree is genuinely distributed for LZTR1; restored the deletion branches and documented the exactly-10% gap and undefined full-gene-deletion footnote.
- Separated the PDF-body and scoring-image presentations for PS2/PM6, PS4, BS2, and BP2/BP5, preserving every printed comparator and exact-value semantic without synthesizing a rule.
- Restored all four LZTR1 assay types from `Approved Functional Studies.xlsx`, their AD/AR readout qualifiers, the explicit BS3_NA status, citations, validation limitations, and the workbook's internally inconsistent control-category labels.
- Removed the locally supplied generic PM3 per-proband table because it is not present in the distributed GN094 package; retained the PDF's SVI instruction and exact aggregate thresholds.
- Added source-auditable pilot examples and reported PS1_M, BP3, BA1-comparator, and version-provenance conflicts without reclassifying variants or resolving them by inference.
- Replaced the unsupported two-version local history with the source PDF's version 1.3 release note.

---

*This document was compiled from the distributed ClinGen RASopathy VCEP specifications for LZTR1. For the most current version, refer to the ClinGen website.*
