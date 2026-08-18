# Comprehensive Variant Interpretation Guidelines for MLH1

## ClinGen InSiGHT Hereditary Colorectal Cancer/Polyposis Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for MLH1 (Version 2.0)

**Affiliation:** InSiGHT Hereditary Colorectal Cancer/Polyposis VCEP
**Version:** 2.0
**Release Date:** 3/5/2026
**Specification ID:** GN115
**DOI:** 10.5281/zenodo.21434431
**Based on:** Richards et al., 2015 - ACMG/AMP Variant Interpretation Guidelines (Combining rules)

> **Description (as published):** ClinGen InSiGHT Hereditary Colorectal Cancer/Polyposis Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for MMR genes Version 2.0.0

---

## Table of Contents

1. [Gene and Disease Information](#1-gene-and-disease-information)
2. [Pathogenic Criteria](#2-pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PM2 - Absent from Controls](#pm2---absent-from-controls)
   - [PM3 - In Trans with Pathogenic Variant](#pm3---in-trans-with-pathogenic-variant)
   - [PM5 - Novel Missense at Same Residue](#pm5---novel-missense-at-same-residue)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
   - [PP4 - Phenotype Specificity](#pp4---phenotype-specificity)
3. [Benign Criteria](#3-benign-criteria)
   - [BA1 - Stand-Alone Benign](#ba1---stand-alone-benign)
   - [BS1 - Allele Frequency Greater Than Expected](#bs1---allele-frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (Benign)](#bs3---functional-studies-benign)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP4 - Computational Evidence (Benign)](#bp4---computational-evidence-benign)
   - [BP5 - Alternate Molecular Basis](#bp5---alternate-molecular-basis)
   - [BP7 - Synonymous/Intronic Variants](#bp7---synonymousintronic-variants)
4. [Not Applicable Criteria](#4-not-applicable-criteria)
5. [Rules for Combining Criteria](#5-rules-for-combining-criteria)
6. [Appendices](#6-appendices)

---

## 1. Gene and Disease Information

| Parameter | Value |
|-----------|-------|
| **Gene** | MLH1 (HGNC:7127) |
| **HGNC Name** | mutL homolog 1 |
| **Reference Transcript** | NM_000249.4 |
| **Disease 1** | Lynch syndrome 2 (MONDO:0012249) — Autosomal dominant inheritance |
| **Disease 2** | mismatch repair cancer syndrome 1 (MONDO:0010159) — Autosomal recessive inheritance |
| **Specification URL** | https://cspec.genome.network/cspec/ui/svi/doc/GN115 |

### Scope Note

This specification is registered per gene (GN115 = MLH1) but the underlying VCEP rule set is written for the four MMR genes (MLH1, MSH2, MSH6, PMS2). Gene-specific values throughout this document are the MLH1 values. Where the source documents give per-gene values for all four MMR genes, both the MLH1 value and the full source table are reproduced so nothing is lost.

### Lynch Syndrome (LS) Spectrum Tumors

Footnote definition used throughout the specification (footnote `d`):

> Lynch Syndrome (LS) tumors include: colorectal/colon/rectal, endometrial, ovarian, small bowel/small intestine, renal pelvis, ureter, and stomach/gastric carcinomas, sebaceous skin tumors (adenomas and carcinomas), gliomas.

### Functional Domain Definition

Footnote definition used throughout the specification (footnote `b`):

> A known functional protein domain is reported to harbor sequence variants that introduce deleterious changes to protein function (via missense alteration, protein sequence deletion, or protein truncation in the last exon) AND are associated with high risk of cancer. Physical boundaries for functional domains are shown in MMR functional domains pdf.

Additional footnotes:

- **a** — PVS1 criteria is adapted from Tayoun et al. 2018.
- **c** — IVS±1 and IVS±2 are the least invariant nucleotides in a splice site
- **e** — Standard MSI markers panel: BAT25, BAT26, BAT40, BAT34, D5S346, D17S250, ACTC, D18S55, D10S197, MYCL; D2S123, D18S69; NR21, NR24, NR27
- **f** — Likelihood ratios for segregation can be derived by Bayes factor analysis adapted from the method of Thompson et al. 2003. Penetrance estimates for MLH1 and MSH2 are from Jenkins et al. 2015 and Dowty et al. 2013; MSH6 from Baglietto et al. 2010; PMS2 from ten Broeke et al. 2015

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Caveats (original ACMG):**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong (PVS1)** | Nonsense/frameshift variant introducing Premature Termination Codon (PTC)^a at or before codon 753 in *MLH1*.<br>**OR** Large genomic alterations^a of single or multi-exon size.<br>**OR** Variants at IVS±1 or IVS±2^a,c where exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD. Not to be combined with PP3 and not to be used for a confirmed splice defect (see PVS1 for variants where patient mRNA assays indicate splicing aberration). If exon skipping or use of a cryptic splice site preserves reading frame and the altered region is critical to protein function^b then use PVS1_Strong. If exon skipping or use of a cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD then use PVS1_Moderate.<br>**OR** Variants where mRNA assays using RNA derived from patient constitutional biological samples indicate that the variant allele results in a splicing aberration (with evidence that the variant allele produces no full-length/reference transcript) leading to premature stop codon or in-frame deletion disrupting a functional domain^b or protein conformation. Splicing aberration must be confirmed in a minigene assay or an additional RNA assay from an independent laboratory if it is a non-canonical splice site variant.<br>**OR** Variants in the initiation codon of *MLH1*.<br>*(Modification Type: General recommendation)* |
| **Strong (PVS1_Strong)** | Presumed by default in tandem duplication of ≥1 exon resulting in a frameshift before the last splice junction. This rule does not apply for variants that involve the UTR (i.e. exon 1 or last exon) and whole gene duplications.<br>**OR** G>non-G at last base of exon if first 6 bases of the intron are not GTRRGT. If confirmed to cause a splice defect, then PVS1 should be used instead.<br>**OR** Variants at IVS±1 or IVS±2^a,c where exon skipping or use of a cryptic splice site preserves reading frame and the altered region is critical to protein function^b. Not to be combined with PP3 and not to be used for a confirmed splice defect (see PVS1 for variants where patient mRNA assays indicate splicing aberration).<br>*(Modification Type: General recommendation)* |
| **Moderate (PVS1_Moderate)** | Nonsense/frameshift variant introducing premature termination codon in codons 754, 755 or 756 in *MLH1*. Refer to Appendix for details.<br>*(Modification Type: Gene-specific)* |
| **Supporting** | Not specified by VCEP |

#### PVS1 Decision Tree (MMR genes)

From `MMR PVS1 Decision Tree.pdf`:

**Nonsense or Frameshift**

| Situation | Outcome |
|-----------|---------|
| Predicted to undergo NMD: (1) ≤ codon 684 in MLH1; (2) ≤ codon 861 in MSH2; (3) ≤ codon 1317 in MSH6; (4) ≤ codon 798 in PMS2 | **PVS1** |
| Not predicted to undergo NMD, and truncated/altered region is critical to protein function: (1) ≤ codon 753 in MLH1; (2) ≤ codon 891 in MSH2; (3) ≤ codon 1341 in MSH6; (4) ≤ codon 798 in PMS2. Refer to Appendix for details | **PVS1** |
| Not predicted to undergo NMD, and role of region in protein function is unknown: codons 754, 755 or 756 in MLH1; between codons 892 & 934 in MSH2; between codons 1342 & 1360 in MSH6; between codons 799 & 862 in PMS2. Refer to Appendix for details | **PVS1_Moderate** |

**GT-AG 1,2 splice sites^a**

| Situation | Outcome |
|-----------|---------|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD | **PVS1** |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is **NOT** predicted to undergo NMD | **PVS1_Moderate** |
| Exon skipping or use of a cryptic splice site preserves reading frame | **PVS1_Strong** |

**Deletion** (single exon to full gene) → **PVS1**^a

**Duplication** (≥1 exon in size and must be completely contained within gene)

| Situation | Outcome |
|-----------|---------|
| Proven in tandem: large genomic duplications shown by laboratory studies (which define the breakpoints of the duplication) to result in a frameshift before the last splice junction (NMD predicted to occur); **OR** large genomic duplications shown by laboratory studies (which define the breakpoints of the duplication) to result in an in-frame insertion disrupting a functional domain^b or protein conformation. | **PVS1** |
| Presumed in tandem: presumed by default in tandem duplication of ≥1 exon resulting in a frameshift before the last splice junction. This rule does not apply for variants that involve the UTR (i.e. exon 1 or last exon) and whole gene duplications. | **PVS1_Strong** |

**Initiation Codon**

| Situation | Outcome |
|-----------|---------|
| No known alternative start codon in other transcripts — variants in the initiation codon of **MLH1** | **PVS1** |
| No known alternative start codon in other transcripts — variants in the initiation codon of MSH6 or PMS2 | **PVS1_Strong** |
| Different functional transcript uses alternative start codon (for MSH2 further ATGs exist inframe in exon 1) | **N/A** |

> **Note (apparent source inconsistency, preserved verbatim):** The registry criteria table states PVS1 (Very Strong) for a PTC "at or before codon 753 in MLH1", whereas the decision tree gives ≤ codon 684 in MLH1 for the NMD-predicted branch and ≤ codon 753 for the not-predicted-to-undergo-NMD/critical-region branch. Both are reproduced above as written.

#### Justification for Last Exon PVS1 Boundaries (Appendix)

Nonsense/frameshift variant introducing Premature Termination Codon (PTC):

1. ≤ codon 753 in MLH1 using location of known pathogenic variant MLH1 c.2252_2253del
2. ≤ codon 891 in MSH2 using location of known pathogenic variant MSH2 c.2662del
3. ≤ codon 1341 in MSH6 using location of known pathogenic variant MSH6 c.3984_3987dup
4. ≤ codon 798 in PMS2 using ≥50 nucleotide NMD-rule.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** SpliceAI masked score option should be checked on.

| Strength | Criteria |
|----------|----------|
| **Strong (PS1)** | A predicted missense substitution that encodes the same amino acid change with a different underlying nucleotide change previously established by this VCEP as Pathogenic (not a predicted or confirmed splice defect).<br>**OR** Variants affecting the same non-canonical splice nucleotide as a confirmed Pathogenic splice variant with similar or worse splicing in silico prediction using SpliceAI.<br>*(Modification Type: General recommendation)* |
| **Moderate (PS1_Moderate)** | A predicted missense substitution that encodes the same amino acid change with a different underlying nucleotide change as a previously established Likely Pathogenic missense variant with normal RNA result\*, and PM2_supporting is met.<br>\*Otherwise, if the previously established Likely Pathogenic missense variant truly is a splice defect, the new missense variant also has to be investigated on a functional level for RNA splicing.<br>**OR** Variants affecting the same non-canonical splice nucleotide as a Likely Pathogenic splice variant with similar or worse splicing in silico prediction using SpliceAI.<br>*(Modification Type: General recommendation)* |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### VCEP Specifications — Points Awarded per Proband

| Evidence | Points |
|----------|--------|
| Proband with a *de novo* variant with both maternity and paternity confirmed in a case with MMR deficient LS spectrum tumor\* (i.e. MSI/IHC consistent with affected gene, with no MLH1 methylation in tumor tissue, with the exception of MLH1 constitutional promoter methylation). Refer to Appendix for protein expression consistent with variant location. | **2 points per proband** |
| Proband with a *de novo* variant with both maternity and paternity confirmed in a case with LS spectrum tumor\* (with no tumor data for MSI/IHC/methylation). | **1 point per proband** |
| Proband with assumed *de novo* variant and maternity and/or paternity unconfirmed with LS spectrum tumor\* (No tumor data for MSI/IHC/methylation). | **0.5 points per proband** |

\*Lynch Syndrome (LS) tumors include: colorectal/colon/rectal, endometrial, ovarian, small bowel/small intestine, renal pelvis, ureter, and stomach/gastric carcinomas, sebaceous skin tumors (adenomas and carcinomas), gliomas.

#### Determining Evidence Strength Level

| Strength | *De novo* points | Modification Type |
|----------|------------------|-------------------|
| **Very Strong (PS2_VeryStrong)** | ≥ 4 points | Disease-specific |
| **Strong (PS2)** | 2 - 3.5 points | Disease-specific |
| **Moderate (PS2_Moderate)** | 1 - 1.5 points | Disease-specific |
| **Supporting (PS2_Supporting)** | 0.5 points | Disease-specific |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:** Refer to file 'Functional assay SVI documentation (MMR genes)' for calibrated functional assays.

> \*The functional assay flowchart is a general framework for evaluating functional assays that were already performed, or from historic publications, not for prospective studies on variants. The information describing these assays are generic. The VCEP recommends use of the calibrated assays for prospective testing.

| Strength | Criteria |
|----------|----------|
| **Strong (PS3)** | Calibrated functional assays with functional odds for pathogenicity > 18.7<br>*(Modification Type: General recommendation)* |
| **Moderate (PS3_Moderate)** | Calibrated functional assays with functional odds for pathogenicity >4.3 and <= 18.7<br>**OR** MMR function defect following functional assay flowchart\*<br>**OR** Variants with monoallelic expression: complete loss of expression (<10% of wild-type in cDNA without puromycin) of the variant allele. Full-length transcript should be analysed with and without NMD block.<br>*(Modification Type: General recommendation)* |
| **Supporting (PS3_Supporting)** | Calibrated functional odds for pathogenicity >2.08 and <= 4.3<br>*(Modification Type: General recommendation)* |

See [Appendix B](#appendix-b-approved-functional-assays-mmr-genes) for the approved assay list and thresholds.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

| Strength | Criteria |
|----------|----------|
| **Supporting (PM2_Supporting)** | Absent/extremely rare allele frequency <0.00002 (<1 in 50,000 alleles ) in gnomAD v4 dataset<br>*(Modification Type: General recommendation)* |

> The stray space in "alleles )" is present in the source and is reproduced verbatim.

---

### PM3 - In Trans with Pathogenic Variant

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Co-occurrence with a known pathogenic/likely pathogenic sequence variant in the same gene in a patient with clinical features consistent with CMMRD as per Aronson et al 2022 - Refer to "Table for CMMRD diagnosis.pdf". For MLH1 variants - the variant has to meet PM2_Supporting criteria.

#### Points Awarded per Case

| Classification/zygosity of other variant | Points |
|------------------------------------------|--------|
| Pathogenic/Likely Pathogenic *in trans* | 1.0 point |
| Pathogenic/Likely Pathogenic - phase unknown | 0.5 points |

Sum all cases with the above evidence to determine the PM3 strength.

#### Determining Evidence Strength Level

| Strength | Points | Modification Type |
|----------|--------|-------------------|
| **Very Strong (PM3_VeryStrong)** | ≥ 4 points | Disease-specific |
| **Strong (PM3_Strong)** | 2 - 3.5 points | Disease-specific |
| **Moderate (PM3)** | 1 - 1.5 points | Disease-specific |
| **Supporting (PM3_Supporting)** | = 0.5 points | Disease-specific |

See [Appendix D](#appendix-d-cmmrd-diagnosis-scoring-system) for the CMMRD scoring system.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

| Strength | Criteria |
|----------|----------|
| **Moderate (PM5)** | Missense change at an amino acid residue where a different missense change was classified by this VCEP as Pathogenic on the protein level and not due to aberrant splicing. Only use PM5 if PP3 is supporting for the missense change. Use PM5_Supporting if other variant is Likely Pathogenic due to a missense alteration.<br>*(Modification Type: General recommendation)* |
| **Supporting (PM5_Supporting)** | Missense change at an amino acid residue where a different missense change was classified as Likely Pathogenic on the protein level and not due to aberrant splicing. Only use PM5_Supporting if PP3 is supporting for the missense change. Use PM5 if other variant is Pathogenic due to a missense alteration.<br>*(Modification Type: General recommendation)* |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

> \*For multiple pedigrees, results are combined by multiplying together.
>
> Recommended segregation analysis tool: COOL (COsegregation OnLine) v3 https://fenglab.chpc.utah.edu/cool3/manual.html
>
> Copy the example pedigree format and complete the fields to build the pedigree in text format. Refer to online manual for cancer types to enter into pedigree. Click on the 'Analysis' tab to view the webform for pedigree file upload and enter appropriate parameters for population and allele frequency. Penetrance file and relative risk file are not required for MMR genes. Use the 'overall Bayes Factor' to determine evidence strength.

| Strength | Criteria |
|----------|----------|
| **Strong (PP1_Strong)** | Co-segregation with disease in pedigree(s) with a combined\* Bayes Likelihood Ratio^f >18.7 in ≥2 families.<br>*(Modification Type: General recommendation)* |
| **Moderate (PP1_Moderate)** | Co-segregation with disease in pedigree(s) with a combined\* Bayes Likelihood Ratio^f >4.3 & ≤18.7.<br>*(Modification Type: General recommendation)* |
| **Supporting (PP1)** | Co-segregation with disease in pedigree(s) with a combined\* Bayes Likelihood Ratio^f >2.08 & ≤4.3.<br>*(Modification Type: General recommendation)* |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:** SpliceAI masked score option should be checked on. For HCI-PRIORS, ensure correct gene is selected from the tabs, and enter the nucleotide number in either HGVS position or HG38 genomic co-ordinate and click 'view'. The output shows 3 substitutions at the nucleotide location, with probability based on splicing and protein predictions. Ensure the 'applicable prior' is used that corresponds to the variant under review.

| Strength | Criteria |
|----------|----------|
| **Moderate (PP3_Moderate)** | Missense variant with HCI prior probability for pathogenicity >0.81 as per https://hci-priors.hci.utah.edu/PRIORS<br>*(Modification Type: General recommendation)* |
| **Supporting (PP3)** | Missense variant with HCI prior probability for pathogenicity >0.68 & ≤0.81 as per https://hci-priors.hci.utah.edu/PRIORS<br>**OR** Predicted splice defect for non-canonical splicing nucleotides using SpliceAI with delta score >= 0.2 as per Walker et al 2023.<br>*(Modification Type: General recommendation)* |
| **Strong** | Not specified by VCEP |

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

> ^e Standard MSI markers panel: BAT25, BAT26, BAT40, BAT34, D5S346, D17S250, ACTC, D18S55, D10S197, MYCL; D2S123, D18S69; NR21, NR24, NR27
>
> **Protein Expression and consistency with variant location:**
>
> IHC evidence should be consistent with the variant gene and the protein that is tested and take into account the MutSα and MutLα heterodimers: MLH1 and PMS2 loss is consistent with an MLH1 pathogenic variant, MSH2 and MSH6 loss is consistent with an MSH2 pathogenic variant, MSH6 loss is consistent with an MSH6 pathogenic variant, and PMS2 loss is consistent with a PMS2 pathogenic variant.

| Strength | Criteria |
|----------|----------|
| **Strong (PP4_Strong)** | ≥3 independent CRC/Endometrial MSI-H tumors in ≥2 families using a standard panel of 5-10 markers^e or tumor genome **and/or** loss of MMR protein expression consistent with the variant location. MSI-H tumor with inconsistent protein expression does not meet PP4_Strong. For *MLH1* variants, *MLH1* promoter methylation is to be excluded in the tumors. Independent tumors can be from the same patient/family.<br>*(Modification Type: Disease-specific)* |
| **Moderate (PP4_Moderate)** | 2 independent CRC/Endometrial MSI-H tumors using a standard panel of 5-10 markers^e or tumor genome **and/or** loss of MMR protein expression consistent with the variant location. MSI-H tumor with inconsistent protein expression does not meet PP4_Moderate. For *MLH1* variants, *MLH1* promoter methylation is to be excluded in the tumors. Independent tumors can be from the same patient/family.<br>*(Modification Type: Disease-specific)* |
| **Supporting (PP4)** | 1 CRC/Endometrial MSI-H tumor using a standard panel of 5-10 markers^e or tumor genome **and/or** loss of MMR protein expression consistent with the variant location. MSI-H tumor with inconsistent protein expression does not meet PP4. For *MLH1* variants, *MLH1* promoter methylation is to be excluded in the tumor.<br>*(Modification Type: Disease-specific)* |

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

| Strength | Criteria |
|----------|----------|
| **Stand Alone (BA1)** | GnomAD v4 Grpmax filtering allele frequency ≥ 0.001 (0.1%) and variant is excluded as founder pathogenic variant.<br>*(Modification Type: Gene-specific)* |

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

| Strength | Criteria |
|----------|----------|
| **Strong (BS1)** | GnomAD v4 Grpmax filtering allele frequency ≥ 0.0001 and < 0.001 (0.01-0.1%) and variant is excluded as founder pathogenic variant.<br>*(Modification Type: Gene-specific)* |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

| Strength | Criteria |
|----------|----------|
| **Strong (BS2)** | Co-occurrence *in trans* with a known pathogenic sequence variant in the same gene in a patient with colorectal cancer after age 45 (or other LS cancer above the median age of onset for that cancer in LS^d), and who has no previous or current evidence of clinical manifestations of CMMRD as per Aronson et al 2022 (Refer to 'Table for CMMRD diagnosis.pdf'). Confirmation of phase requires testing of parents or offspring.<br>*(Modification Type: Disease-specific)* |

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** Refer to file 'Functional assay SVI documentation (MMR genes)' for calibrated assays.

> \*The functional assay flowchart is a general framework for evaluating functional assays that were already performed, or from historic publications, not for prospective studies on variants. The information describing these assays are generic. The VCEP recommends use of the calibrated assays for prospective testing.

| Strength | Criteria |
|----------|----------|
| **Strong (BS3)** | Calibrated functional assays with functional odds for Pathogenicity ≤ 0.05<br>**OR** Synonymous substitutions and intronic variants with no associated mRNA aberration (either splicing or allelic imbalance) as determined by laboratory assays conducted with nonsense-mediated decay inhibition. Whenever abnormal transcripts are identified at similar levels in controls they will be considered naturally occurring isoforms and not mRNA aberrations.<br>*(Modification Type: General recommendation)* |
| **Supporting (BS3_Supporting)** | Calibrated functional assays with functional odds for Pathogenicity >0.05 & ≤0.48<br>**OR** Variant-specific proficient function in protein and mRNA-based lab assays as per MMR functional assay flowchart\*.<br>*(Modification Type: General recommendation)* |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

> \*For multiple pedigrees, results are combined by multiplying together.
>
> Recommended segregation analysis tool: COOL (COsegregation OnLine) v3 https://fenglab.chpc.utah.edu/cool3/manual.html
>
> Copy the example pedigree format and complete the fields to build the pedigree in text format. Refer to online manual for cancer types to enter into pedigree. Click on the 'Analysis' tab to view the webform for pedigree file upload and enter appropriate parameters for population and allele frequency. Penetrance file and relative risk file are not required for MMR genes. Use the 'overall Bayes Factor' to determine evidence strength.

| Strength | Criteria |
|----------|----------|
| **Strong (BS4)** | Lack of co-segregation with disease in pedigree(s) with a combined\* Bayes Likelihood Ratio^f <0.05.<br>*(Modification Type: General recommendation)* |
| **Supporting (BS4_Supporting)** | Lack of co-segregation with disease in pedigree(s) with a combined\* Bayes Likelihood Ratio^f >0.05 & ≤0.48.<br>*(Modification Type: General recommendation)* |

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

**VCEP Specifications:** SpliceAI masked score option should be checked on. For HCI-PRIORS, ensure correct gene is selected from the tabs, and enter the nucleotide number in either HGVS position or HG38 genomic co-ordinate and click 'view'. The output shows 3 substitutions at the nucleotide location, with probability based on splicing and protein predictions. Ensure the 'applicable prior' is used that corresponds to the variant under review.

| Strength | Criteria |
|----------|----------|
| **Supporting (BP4)** | Missense variant with HCI-prior probability of pathogenicity <0.11 as per https://hci-priors.hci.utah.edu/PRIORS<br>**OR** For intronic and synonymous variants: SpliceAI predicts no splicing impact with delta score <= 0.1 as per Walker et al 2023<br>*(Modification Type: General recommendation)* |

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

| Strength | Criteria |
|----------|----------|
| **Strong (BP5_Strong)** | ≥ 4 tumors: CRC/Endometrial tumors with MSS and/or no loss of MMR protein expression and/or LS spectrum tumors^d with loss of MMR protein(s) that is inconsistent with the gene demonstrating genetic variation<br>**OR** ≥2 BRAF V600E (CRC only)/*MLH1* methylation (in LS spectrum tumor only) with MSI-H/*MLH1* loss.<br>*(Modification Type: Disease-specific)* |
| **Supporting (BP5)** | 2 or 3 tumors: CRC/Endometrial tumors with MSS and/or no loss of MMR protein expression and/or LS spectrum tumors^d with loss of MMR protein(s) that is inconsistent with the gene demonstrating genetic variation.<br>**OR** 1 BRAF V600E (Colon only)/*MLH1* methylation (in LS spectrum tumor only) with MSI-H/*MLH1* loss.<br>*(Modification Type: Disease-specific)* |

---

### BP7 - Synonymous/Intronic Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

| Strength | Criteria |
|----------|----------|
| **Supporting (BP7)** | A synonymous (silent) or intronic variant at or beyond -21/+7 (5′/3′ exonic). Variants may satisfy both BP7 and BP4.<br>*(Modification Type: General recommendation)* |

> The parenthetical "(5′/3′ exonic)" is reproduced verbatim from the source; the pairing of "-21/+7" with "5′/3′" appears transposed relative to usual convention (−21 is the acceptor/3′ splice-site side). Flagged, not corrected.

---

## 4. Not Applicable Criteria

| Criterion | Original Purpose | VCEP Comment (verbatim) |
|-----------|-----------------|-------------------------|
| **PS4** | Prevalence in affected individuals | Due to the availability of tumor IHC data for variant classification (see PP4), PS4 has not been utilized for MMR variant classification using proband counting. |
| **PM1** | Mutational hot spot / critical domain | There are no recognized mutational hot spots that could be used for classification purposes. While there are functional domains in the MMR genes, the distribution of pathogenic variants is generalized over all the domains (unpublished data). |
| **PM4** | Protein length changes | Protein length change from an in-frame variant is not used due to lack of evidence. |
| **PM6** | Assumed de novo | Please see PS2 |
| **PP2** | Low rate of benign missense | Missense variant in a gene with low rate of benign missense changes does not apply. |
| **PP5** | Reputable source reports pathogenic | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229) |
| **BP1** | Missense in truncating disease gene | Missense variant in a gene where only loss of function causes disease is not applicable. |
| **BP2** | In trans with pathogenic for dominant | BS2 is used instead. |
| **BP3** | In-frame indel in repetitive region | In-frame deletions/insertions in a repetitive region without a known function is not used. |
| **BP6** | Reputable source reports benign | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229) |

---

## 5. Rules for Combining Criteria

### Pathogenic Classification

| Combination | Classification |
|-------------|----------------|
| 1 Very Strong AND ≥ 1 Strong | **Pathogenic** |
| 1 Very Strong AND ≥ 2 Moderate | **Pathogenic** |
| 1 Very Strong AND 1 Moderate AND 1 Supporting | **Pathogenic** |
| 1 Very Strong AND ≥ 2 Supporting | **Pathogenic** |
| ≥ 2 Strong | **Pathogenic** |
| 1 Strong AND ≥ 3 Moderate | **Pathogenic** |
| 1 Strong AND 2 Moderate AND ≥ 2 Supporting | **Pathogenic** |
| 1 Strong AND 1 Moderate AND ≥ 4 Supporting | **Pathogenic** |

### Likely Pathogenic Classification

| Combination | Classification |
|-------------|----------------|
| 1 Very Strong AND 1 Moderate | **Likely Pathogenic** |
| 1 Strong AND 1 Moderate | **Likely Pathogenic** |
| 1 Strong AND ≥ 2 Supporting | **Likely Pathogenic** |
| ≥ 3 Moderate | **Likely Pathogenic** |
| 2 Moderate AND ≥ 2 Supporting | **Likely Pathogenic** |
| 1 Moderate AND ≥ 4 Supporting | **Likely Pathogenic** |
| 1 Strong AND 2 Moderate | **Likely Pathogenic** |

### Benign Classification

| Combination | Classification |
|-------------|----------------|
| ≥ 2 Strong | **Benign** |
| 1 Stand Alone | **Benign** |

### Likely Benign Classification

| Combination | Classification |
|-------------|----------------|
| 1 Strong AND 1 Supporting | **Likely Benign** |
| ≥ 2 Supporting | **Likely Benign** |

### Variant of Uncertain Significance (VUS)

Not explicitly specified by VCEP. Variants that do not meet any of the combining rules above remain of Uncertain Significance.

---

## 6. Appendices

### Appendix A: Exon Deletions/Duplications — In-frame/Out-of-frame

Source: Appendix (https://databases.lovd.nl/shared/scripts/readingFrameChecker.php)

\*First and last exon deletions/duplications are difficult to predict whether in-frame or out-of-frame.

| Exon | MLH1 | MSH2 | MSH6 | PMS2 |
|------|------|------|------|------|
| Exon 1 | N/A* | N/A* | N/A* | N/A* |
| Exon 2 | Out-of-frame | Out-of-frame | Out-of-frame | Out-of-frame |
| Exon 3 | In-frame | In-frame | Out-of-frame | In-frame |
| Exon 4 | Out-of-frame | In-frame | Out-of-frame | Out-of-frame |
| Exon 5 | Out-of-frame | In-frame | Out-of-frame | Out-of-frame |
| Exon 6 | Out-of-frame | Out-of-frame | Out-of-frame | In-frame |
| Exon 7 | Out-of-frame | Out-of-frame | In-frame | Out-of-frame |
| Exon 8 | Out-of-frame | Out-of-frame | Out-of-frame | Out-of-frame |
| Exon 9 | Out-of-frame | Out-of-frame | Out-of-frame | Out-of-frame |
| Exon 10 | Out-of-frame | Out-of-frame | N/A* | In-frame |
| Exon 11 | Out-of-frame | Out-of-frame | | Out-of-frame |
| Exon 12 | Out-of-frame | In-frame | | In-frame |
| Exon 13 | Out-of-frame | Out-of-frame | | Out-of-frame |
| Exon 14 | Out-of-frame | Out-of-frame | | Out-of-frame |
| Exon 15 | Out-of-frame | Out-of-frame | | N/A* |
| Exon 16 | In-frame | N/A* | | |
| Exon 17 | In-frame | | | |
| Exon 18 | In-frame | | | |
| Exon 19 | N/A* | | | |

#### Important Notes (Appendix)

- PMS2 NGS results need confirmation by other orthogonal assays as well as functional assessment (e.g. Long-Range or cDNA), if variants are located in the PMS2CL pseudogene homologous regions (exons 11-15).
- Gene-specific penetrance estimates are available at http://lscarisk.org/

#### Derivation of Probability Values from Odds (Appendix)

- 0.11 probability corresponds to the odds of 0.48 for Benign Supporting level of benign evidence using 0.2 prior – consistent with ACMG Bayesian model.
- 0.68 probability corresponds to the odds of 2.08 for Pathogenic Supporting level of evidence using 0.5 prior – consistent with ACMG Bayesian model.
- 0.81 probability corresponds to the odds of 4.3 for Pathogenic Supporting level of evidence using 0.5 prior – consistent with ACMG Bayesian model.

> Source note: the third bullet says "Pathogenic Supporting" for the 0.81/4.3 pair, where 4.3 is the Moderate boundary elsewhere in the specification. Preserved verbatim and flagged.

---

### Appendix B: Approved Functional Assays (MMR genes)

Source: `Functional assay SVI documentation.xlsx`, sheet "MMR assays". All listed assays are marked "Approved assay: y".

| PMID(s) | Author / Year | Assay | Normal readout threshold | Abnormal readout threshold | Proposed strength |
|---------|---------------|-------|--------------------------|----------------------------|-------------------|
| 30504929; 31965077 | Drost 2018; Drost 2020 | CALIBRATED ASSAY: Assessing MMR protein repair capacity as a complete process: CIMRA Functional assay using cell-free system | ≥70% for MLH1 and MSH2, and ≥100% for MSH6 and PMS2 | <23% for MLH1 and MSH2, and <18% for MSH6 and PMS2 | PS3, PS3_Moderate, PS3_Supporting, BS3, BS3_Supporting |
| 33357406; 36550560 | Jia 2021; Scott 2022 | CALIBRATED ASSAY: Chemical selection for mismatch repair dysfunction and deep sequencing to identify the surviving MSH2 variants | LOF score <= 0 | LOF score > 0.4 | PS3, BS3 |
| 36054288 | Rath 2022 | CALIBRATED ASSAY: Measures functional impact of MLH1 variants on MMR-associated repair and damage response (hESC CRISPR) | OddsPath_Functional scores < 0.48 | OddsPath_Functional scores > 2.08 | PS3, PS3_Moderate, PS3_Supporting, BS3, BS3_Supporting |
| 24362816 | Thompson 2013 | Assessing MMR protein repair capacity as a complete process: functional assays using cell-free systems | >75% in two independent assays | <25% in two independent assays | PS3_moderate, BS3_supporting |
| 24362816 | Thompson 2013 | Mammalian MMR activity complementation assays | >75% in two independent assays | <25% in two independent assays | PS3_moderate, BS3_supporting |
| 24362816 | Thompson 2013 | Assessing MMR protein expression: cellular-based MMR functional assay using a human/mouse expression system | >75% in two independent assays | <25% in two independent assays | PS3_moderate, BS3_supporting |
| 24362816 | Thompson 2013 | Assessing MMR protein subcellular localization | Nuclear localization | Cytoplasmic in localization | PS3_moderate, BS3_supporting |
| 31332305 | Morak 2019 | cDNA analysis of full-length transcripts (FLT) for MMR genes to assess splicing and transcript integrety | biallelic (50 ± 10%) | Allelic loss (≤10%) | PS3_moderate, BS3_supporting |
| 30998989 | Bouvet 2019 | Measures cell survival following exposure to a methylating agent (MNNG) | Mean survival score < 68.7% (MLH1); Mean survival score < 45.54% (MSH2) | Mean survival score > 68.7% (MLH1); Mean survival score > 45.54% (MSH2) | PS3_moderate, BS3_supporting |

> Source typos preserved verbatim: "integrety" (Morak 2019 row) and "acheived" (Jia/Scott statistical analysis note).
>
> Source note: for Bouvet 2019 the spreadsheet lists the same numeric cut-points (68.7% MLH1, 45.54% MSH2) for both the normal (`<`) and abnormal (`>`) readout thresholds, i.e. lower survival = normal. Reproduced as written.

#### MMR Functional Assay Flowchart

Source: `MMR Functional assay flowchart.pdf`. Summary of the decision path:

- Start: MMR gene sequence variant type → branch to (a) in-frame indel or missense variant, or (b) splice site, silent, or intronic.
- **Splice site / silent / intronic:** splicing assay → *Complete impact* → **Deficient function**; *Extent of impact unknown/partial impact* → if in-frame or missense variant, route into the calibrated-assay branch; *No impact* → if not an in-frame/missense variant, check NMD-inhibitors included → if yes, **Proficient function**; if no, further research calibrating against clinical data. Patient-derived RNA assays, if available, feed directly into deficient/proficient function.
- **In-frame indel or missense:** first/last 3 bases of the exon or splicing impact predicted? → *Yes* routes to the splicing branch; *No* → calibrated functional assay conducted? → *Yes* → quantitative multifactorial analysis **OR** convert functional LR to ACMG/AMP evidence weight.
- If no calibrated assay: require **2 independent assays with concordant results** — mammalian MMR activity assays (similar repair levels to deficient cell line/pathogenic controls → deficient; similar to wild-type controls → proceed to protein expression assessment; inconclusive → further research).
- Assessment of protein expression/stability: ≤25% relative expression or similar to deficient cell line control → **Deficient function**; ≥75% relative expression or similar to wild-type control → subcellular localization and cellular-based MMR activity assays → cytoplasmic, tolerant to DNA damage or high mutator phenotype → **Deficient function**; nuclear, sensitive to DNA damage and no mutator phenotype → **Proficient function**; inconclusive → further research calibrating against clinical data.

---

### Appendix C: MMR Functional Domains

Source: `MMR functional domains.pdf` — "Linear schematic of mismatch repair gene functional domains according to amino acid positions. Adapted from InSiGHT criteria v2.4 (https://www.insight-group.org/content/uploads/2018/08/2018-06_InSiGHT_VIC_v2.4.pdf)".

MLH1 (NM_000249.4; 19 exons; protein 1-756) domains as depicted:

| Domain | Approximate amino acid boundaries |
|--------|-----------------------------------|
| ATPase | 1 - 347 |
| MutSα interaction | 1 - 329 |
| NLS | ~469-490 (marked within 410-470 region) |
| EXO1 interaction | ~410 - 650 |
| MLH3/PMS1/PMS2 interaction | ~492 - 743 |
| NES | two sites marked at ~502-520 and ~612-630 |

> The domain boundaries above are read from a graphical schematic; use the source PDF for exact coordinates.

---

### Appendix D: CMMRD Diagnosis Scoring System

Source: `Table for CMMRD diagnosis.pdf` — "Table 3. Scoring system for aiding CMMRD diagnosis from C4CMMRD (adapted from Aronson et al 2022; PMID: 33622763)".

**Threshold:** >=3 points = CMMRD features meets PM3 criteria after excluding the diagnosis of NF1 or LFS as individuals with those disorders could easily get to 3 points.

**Malignancies/premalignancies: one is mandatory; if more than one is present in the patient, add the points:**

| Feature | Points |
|---------|--------|
| Carcinoma from the LS spectrum\* at age <25 years. | 3 points |
| Multiple bowel adenomas at age <25 years and absence of APC/MUTYH mutation(s) or a single high-grade dysplasia adenoma at age <25 years. | 3 points |
| WHO grade III or IV glioma at age <25 years. | 2 points |
| NHL of T cell lineage or sPNET at age <18 years | 2 points |
| Any malignancy at age <18 years. | 1 point |

**Additional features: optional; if more than one of the following is present, add the points:**

| Feature | Points |
|---------|--------|
| Clinical sign of NF1 and/or ≥2 hyperpigmented and/or hypopigmented skin alterations Ø>1 cm. | 2 points |
| Diagnosis of LS in a first-degree or second-degree relative. | 2 points |
| Carcinoma from LS spectrum\* before the age of 60 in a firstdegree, second-degree or third-degree relative. | 1 point |
| A sibling with carcinoma from the LS spectrum\*, high-grade glioma, sPNET or NHL. | 2 points |
| A sibling with any type of childhood malignancy. | 1 point |
| Multiple pilomatricomas in the patient. | 2 points |
| One pilomatricoma in the patient. | 1 point |
| Agenesis of the corpus callosum or non-therapy-induced cavernoma in the patient. | 1 point |
| Consanguineous parents | 1 point |
| Deficiency/reduced levels of IgG2/4 and/or IgA. | 1 point |

\*Colorectal, endometrial, small bowel, ureter, renal pelvis, biliary tract, stomach, bladder carcinoma

Abbreviations: CMMRD, constitutional mismatch repair deficiency; LS, Lynch syndrome; NF1, neurofibromatosis type 1; NHL, non-Hodgkin's lymphoma; sPNET, supratentorial primitive neuroectodermal tumours.

> Source typo preserved verbatim: "firstdegree" (missing hyphen).

---

### Appendix E: Population Frequency Thresholds Summary

| Criterion | Threshold (gnomAD v4) | Strength |
|-----------|------------------------|----------|
| BA1 | Grpmax filtering AF ≥ 0.001 (0.1%), variant excluded as founder pathogenic variant | Stand Alone |
| BS1 | Grpmax filtering AF ≥ 0.0001 and < 0.001 (0.01-0.1%), variant excluded as founder pathogenic variant | Strong |
| PM2 | AF < 0.00002 (<1 in 50,000 alleles) | Supporting |

---

### Appendix F: References (as listed in the specification)

| # | Citation | PMID |
|---|----------|------|
| 1 | Belman S, Parsons MT et al. Considerations in assessing germline variant pathogenicity using cosegregation analysis. *Genet Med* (2020) 22(12):2052-2059. | 32773770 |
| 2 | Aronson M, Colas C et al. Diagnostic criteria for constitutional mismatch repair deficiency (CMMRD): recommendations from the international consensus working group. *J Med Genet* (2022) 59(4):318-327. | 33622763 |
| 3 | Li S, Qian D et al. Tumour characteristics provide evidence for germline mismatch repair missense variant pathogenicity. *J Med Genet* (2020) 57(1):62-69. | 31391288 |
| 4 | Canson DM, Dumenil T et al. The splicing effect of variants at branchpoint elements in cancer genes. *Genet Med* (2022) 24(2):398-409. | 34906448 |
| 5 | Cyr JL, Brown GD et al. The predicted truncation from a cancer-associated variant of the MSH2 initiation codon alters activity of the MSH2-MSH6 mismatch repair complex. *Mol Carcinog* (2012) 51(8):647-58. | 21837758 |
| 6 | Drost M, Tiersma Y et al. A functional assay-based procedure to classify mismatch repair gene variants in Lynch syndrome. *Genet Med* (2019) 21(7):1486-1496. | 30504929 |
| 7 | Drost M, Tiersma Y et al. Two integrated and highly predictive functional analysis-based procedures for the classification of MSH6 variants in Lynch syndrome. *Genet Med* (2020) 22(5):847-856. | 31965077 |
| 8 | Rath A, Radecki AA et al. A calibrated cell-based functional assay to aid classification of MLH1 DNA mismatch repair gene variants. *Hum Mutat* (2022) 43(12):2295-2307. | 36054288 |
| 9 | Rayner E, Tiersma Y et al. Predictive functional assay-based classification of PMS2 variants in Lynch syndrome. *Hum Mutat* (2022) 43(9):1249-1258. | 35451539 |
| 10 | Tavtigian SV, Greenblatt MS et al. Modeling the ACMG/AMP variant classification guidelines as a Bayesian classification framework. *Genet Med* (2018) 20(9):1054-1060. | 29300386 |
| 11 | Abou Tayoun AN, Pesaran T et al. Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion. *Hum Mutat* (2018) 39(11):1517-1524. | 30192042 |
| 12 | Thompson BA, Walters R et al. Contribution of mRNA Splicing to Mismatch Repair Gene Sequence Variant Interpretation. *Front Genet* (2020) 11:798. | 32849802 |
| 13 | Whiffin N, Minikel E et al. Using high-resolution variant frequencies to empower clinical genome interpretation. *Genet Med* (2017) 19(10):1151-1158. | 28518168 |
| 14 | Walker LC, Hoya M et al. Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing: Recommendations from the ClinGen SVI Splicing Subgroup. *Am J Hum Genet* (2023) 110(7):1046-1067. | 37352859 |

---

### Appendix G: Release Notes for Version 2.0 (as published)

- PS1 Moderate (Change to bring into closer alignment with Walker et al): Variants affecting the same non-canonical splice nucleotide as a likely pathogenic splice variant with similar or worse splicing in silico prediction using SpliceAI.
- PS2 and Similarly for PM3 - updated points range
- Fixes to capitalisation of Pathogenic/Likely Pathogenic terms
- Correction: Footnotes corrected in criteria and Appendix. Corrections to PS2 criteria. List of exons that would be in-frame and out-of-frame added to Appendix.
- Correction: Changed "2 Strong" in combining rules from Pathogenic to Likely Pathogenic.
- Correction: Added "2 Supporting" in combining rules to Likely Benign
- Amendment: Minor change to PM2 allele frequency format (1/50000 = 0.00002)

> Source note: the release note states that "2 Strong" was changed from Pathogenic to Likely Pathogenic, but the published v2.0 combining-rules tables still list "≥ 2 Strong" under Pathogenic (and under Benign for benign criteria), with no "2 Strong" row under Likely Pathogenic. Reproduced as published and flagged.

---

*This document was compiled from the ClinGen VCEP specification GN115 (MLH1, version 2.0) and its supplementary files. For the most current version, refer to https://cspec.genome.network/cspec/ui/svi/doc/GN115.*
