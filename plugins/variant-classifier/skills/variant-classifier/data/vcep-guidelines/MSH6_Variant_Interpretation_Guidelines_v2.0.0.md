# Comprehensive Variant Interpretation Guidelines for MSH6

## ClinGen InSiGHT Hereditary Colorectal Cancer/Polyposis Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for MSH6 (Version 2.0)

**Affiliation:** InSiGHT Hereditary Colorectal Cancer/Polyposis VCEP
**Specification ID:** GN138
**Version:** 2.0 (Description field of the specification reads "Version 2.0.0")
**Released:** 3/5/2026
**DOI:** 10.5281/zenodo.21434726
**Type:** Richards et al., 2015 - Combining rules
**Based on:** Richards et al., 2015 - ACMG/AMP Variant Interpretation Guidelines
**Source:** https://cspec.genome.network/cspec/ui/svi/doc/GN138

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
   - [PM3 - Co-occurrence / CMMRD](#pm3---co-occurrence--cmmrd)
   - [PM4 - Protein Length Changes](#pm4---protein-length-changes)
   - [PM5 - Novel Missense at Same Residue](#pm5---novel-missense-at-same-residue)
   - [PM6 - De Novo (Assumed)](#pm6---de-novo-assumed)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP2 - Missense in Constrained Gene](#pp2---missense-in-constrained-gene)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
   - [PP4 - Phenotype Specificity](#pp4---phenotype-specificity)
   - [PP5 - Reputable Source](#pp5---reputable-source)
3. [Benign Criteria](#3-benign-criteria)
   - [BA1 - Allele Frequency Stand Alone](#ba1---allele-frequency-stand-alone)
   - [BS1 - Frequency Greater Than Expected](#bs1---frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (No Effect)](#bs3---functional-studies-no-effect)
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
| **Gene** | MSH6 (HGNC:7329) |
| **HGNC Name** | mutS homolog 6 |
| **Reference Transcript** | NM_000179.3 |
| **Disease 1** | Lynch syndrome (MONDO:0005835) — Mode of Inheritance: Autosomal dominant inheritance |
| **Disease 2** | mismatch repair cancer syndrome 1 (MONDO:0010159) — Mode of Inheritance: Autosomal recessive inheritance |

**Lynch Syndrome (LS) tumour spectrum** (footnote d, used by PS2, BP5): colorectal/colon/rectal, endometrial, ovarian, small bowel/small intestine, renal pelvis, ureter, and stomach/gastric carcinomas, sebaceous skin tumors (adenomas and carcinomas), gliomas.

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical +/−1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**Original ACMG Caveats:**
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

#### Very Strong (PVS1) — *Modification type: General recommendation*

Nonsense/frameshift variant introducing Premature Termination Codon (PTC)<sup>a</sup> ≤ codon 1341 in *MSH6*. Refer to Appendix for details.

**OR**

Large genomic alterations<sup>a</sup> of single or multi-exon size.

**OR**

Variants at IVS±1 or IVS±2<sup>a,c</sup> where exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD. Not to be combined with PP3 and not to be used for a confirmed splice defect (see PVS1 for variants where patient mRNA assays indicate splicing aberration). If exon skipping or use of a cryptic splice site preserves reading frame and the altered region is critical to protein function<sup>b</sup> then use PVS1_Strong. If exon skipping or use of a cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD then use PVS1_Moderate.

**OR**

Variants where mRNA assays using RNA derived from patient constitutional biological samples indicate that the variant allele results in a splicing aberration (with evidence that the variant allele produces no full-length/reference transcript) leading to premature stop codon or in-frame deletion disrupting a functional domain<sup>b</sup> or protein conformation. Splicing aberration must be confirmed in a minigene assay or an additional RNA assay from an independent laboratory if it is a non-canonical splice site variant.

#### Strong (PVS1_Strong) — *Modification type: General recommendation*

Variants in the initiation codon of *MSH6*.

**OR**

Presumed by default in tandem duplication of ≥1 exon resulting in a frameshift before the last splice junction. This rule does not apply for variants that involve the UTR (i.e. exon 1 or last exon) and whole gene duplications.

**OR**

G>non-G at last base of exon if first 6 bases of the intron are not GTRRGT. If confirmed to cause a splice defect, then PVS1 should be used instead.

**OR**

Variants at IVS±1 or IVS±2<sup>a,c</sup> where exon skipping or use of a cryptic splice site preserves reading frame and altered region is critical to protein function<sup>b</sup>. Not to be combined with PP3 and not to be used for a confirmed splice defect (see PVS1 for variants where patient mRNA assays indicate splicing aberration).

#### Moderate (PVS1_Moderate) — *Modification type: Gene-specific*

Nonsense/frameshift variant introducing premature termination codon between codons 1342 & 1360 in MSH6. Refer to Appendix for details.

#### Supporting

Not specified by VCEP.

> See [Appendix A: MMR PVS1 Decision Tree](#appendix-a-mmr-pvs1-decision-tree) for the full decision tree, including the NMD boundary (≤ codon 1317 in MSH6) used for the "predicted to undergo NMD" branch.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** SpliceAI masked score option should be checked on.

#### Strong (PS1) — *Modification type: General recommendation*

A predicted missense substitution that encodes the same amino acid change with a different underlying nucleotide change previously established by this VCEP as Pathogenic (not a predicted or confirmed splice defect).

**OR**

Variants affecting the same non-canonical splice nucleotide as a confirmed Pathogenic splice variant with similar or worse splicing in silico prediction using SpliceAI.

#### Moderate (PS1_Moderate) — *Modification type: General recommendation*

A predicted missense substitution that encodes the same amino acid change with a different underlying nucleotide change as a previously established Likely Pathogenic missense variant with normal RNA result\*, and PM2_supporting is met.

\*Otherwise, if the previously established Likely Pathogenic missense variant truly is a splice defect, the new missense variant also has to be investigated on a functional level for RNA splicing.

**OR**

Variants affecting the same non-canonical splice nucleotide as a Likely Pathogenic splice variant with similar or worse splicing in silico prediction using SpliceAI.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### VCEP Point Assignment

| Evidence per proband | Points |
|----------------------|--------|
| Proband with a *de novo* variant with both maternity and paternity confirmed in a case with MMR deficient LS spectrum tumor\* (i.e. MSI/IHC consistent with affected gene, with no MLH1 methylation in tumor tissue, with the exception of MLH1 constitutional promoter methylation). Refer to Appendix for protein expression consistent with variant location. | **2 points per proband** |
| Proband with a *de novo* variant with both maternity and paternity confirmed in a case with LS spectrum tumor\* (with no tumor data for MSI/IHC/methylation). | **1 point per proband** |
| Proband with assumed *de novo* variant and maternity and/or paternity unconfirmed with LS spectrum tumor\* (No tumor data for MSI/IHC/methylation). | **0.5 points per proband** |

\*Lynch Syndrome (LS) tumors include: colorectal/colon/rectal, endometrial, ovarian, small bowel/small intestine, renal pelvis, ureter, and stomach/gastric carcinomas, sebaceous skin tumors (adenomas and carcinomas), gliomas.

#### Evidence Strength Thresholds — *Modification type: Disease-specific*

| Total *de novo* points | Strength |
|------------------------|----------|
| ≥ 4 | **PS2_VeryStrong** |
| 2 - 3.5 | **PS2 (Strong)** |
| 1 - 1.5 | **PS2_Moderate** |
| 0.5 | **PS2_Supporting** |

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:** Refer to file 'Functional assay SVI documentation (MMR genes)' for calibrated functional assays.

\*The functional assay flowchart is a general framework for evaluating functional assays that were already performed, or from historic publications, not for prospective studies on variants. The information describing these assays are generic. The VCEP recommends use of the calibrated assays for prospective testing.

#### Strength Levels — *Modification type: General recommendation*

| Strength | Criteria |
|----------|----------|
| **Strong (PS3)** | Calibrated functional assays with functional odds forpathogenicity > 18.7 *(sic — "forpathogenicity" appears without a space in the source)* |
| **Moderate (PS3_Moderate)** | Calibrated functional assays with functional odds for pathogenicity >4.3 and <= 18.7 **OR** MMR function defect following functional assay flowchart\* **OR** Variants with monoallelic expression: complete loss of expression (<10% of wild-type in cDNA without puromycin) of the variant allele. Full-length transcript should be analysed with and without NMD block. |
| **Supporting (PS3_Supporting)** | Calibrated functional odds for pathogenicity >2.08 and <= 4.3 |

> See [Appendix C: Approved Functional Assays](#appendix-c-approved-functional-assays) and [Appendix B: MMR Functional Assay Flowchart](#appendix-b-mmr-functional-assay-flowchart).

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**Status: NOT APPLICABLE**

**VCEP Comment:** Due to the availability of tumor IHC data for variant classification (see PP4), PS4 has not been utilized for MMR variant classification using proband counting.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**Status: NOT APPLICABLE**

**VCEP Comment:** There are no recognized mutational hot spots that could be used for classification purposes. While there are functional domains in the MMR genes, the distribution of pathogenic variants is generalized over all the domains (unpublished data).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

#### Supporting (PM2_Supporting) — *Modification type: General recommendation*

Absent/extremely rare allele frequency **<0.00002 (<1 in 50,000 alleles)** in gnomAD v4 dataset.

> PM2 is applied at Supporting strength only. No Moderate-level PM2 is specified by this VCEP.

---

### PM3 - Co-occurrence / CMMRD

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant. Note: This requires testing of parents (or offspring) to determine phase.

**VCEP Specifications:** Co-occurrence with a known pathogenic/likely pathogenic sequence variant in the same gene in a patient with clinical features consistent with CMMRD as per Aronson et al 2022 - Refer to "Table for CMMRD diagnosis.pdf". For MLH1 variants - the variant has to meet PM2_Supporting criteria.

#### Point Assignment

| Classification/zygosity of other variant | Points |
|------------------------------------------|--------|
| Pathogenic/Likely Pathogenic *in trans* | **1.0 point** |
| Pathogenic/Likely Pathogenic - phase unknown | **0.5 points** |

Sum all cases with the above evidence to determine the PM3 strength.

#### Evidence Strength Thresholds — *Modification type: Disease-specific*

| Total points | Strength |
|--------------|----------|
| ≥ 4 | **PM3_VeryStrong** |
| 2 - 3.5 | **PM3_Strong** |
| 1 - 1.5 | **PM3 (Moderate)** |
| = 0.5 | **PM3_Supporting** |

> See [Appendix D: CMMRD Diagnostic Scoring Table](#appendix-d-cmmrd-diagnostic-scoring-table).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**Status: NOT APPLICABLE**

**VCEP Comment:** Protein length change from an in-frame variant is not used due to lack of evidence.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

#### Moderate (PM5) — *Modification type: General recommendation*

Missense change at an amino acid residue where a different missense change was classified by this VCEP as Pathogenic on the protein level and not due to aberrant splicing. Only use PM5 if PP3 is supporting for the missense change. Use PM5_Supporting if other variant is Likely Pathogenic due to a missense alteration.

#### Supporting (PM5_Supporting) — *Modification type: General recommendation*

Missense change at an amino acid residue where a different missense change was classified as Likely Pathogenic on the protein level and not due to aberrant splicing. Only use PM5_Supporting if PP3 is supporting for the missense change. Use PM5 if other variant is Pathogenic due to a missense alteration.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**Status: NOT APPLICABLE (as a separate criterion)**

**VCEP Comment:** Please see PS2. Assumed *de novo* observations are scored within the PS2 point system.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:**

\*For multiple pedigrees, results are combined by multiplying together.

Recommended segregation analysis tool: COOL (COsegregation OnLine) v3 — https://fenglab.chpc.utah.edu/cool3/manual.html

Copy the example pedigree format and complete the fields to build the pedigree in text format. Refer to online manual for cancer types to enter into pedigree. Click on the 'Analysis' tab to view the webform for pedigree file upload and enter appropriate parameters for population and allele frequency. Penetrance file and relative risk file are not required for MMR genes. Use the 'overall Bayes Factor' to determine evidence strength.

#### Strength Levels — *Modification type: General recommendation*

| Strength | Combined\* Bayes Likelihood Ratio<sup>f</sup> |
|----------|-----------------------------------------------|
| **Strong (PP1_Strong)** | >18.7 in ≥2 families |
| **Moderate (PP1_Moderate)** | >4.3 & ≤18.7 |
| **Supporting (PP1)** | >2.08 & ≤4.3 |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**Status: NOT APPLICABLE**

**VCEP Comment:** Missense variant in a gene with low rate of benign missense changes does not apply.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

**VCEP Specifications:** SpliceAI masked score option should be checked on. For HCI-PRIORS, ensure correct gene is selected from the tabs, and enter the nucleotide number in either HGVS position or HG38 genomic co-ordinate and click 'view'. The output shows 3 substitutions at the nucleotide location, with probability based on splicing and protein predictions. Ensure the 'applicable prior' is used that corresponds to the variant under review.

#### Moderate (PP3_Moderate) — *Modification type: General recommendation*

Missense variant with HCI prior probability for pathogenicity **>0.81** as per https://hci-priors.hci.utah.edu/PRIORS

#### Supporting (PP3) — *Modification type: General recommendation*

Missense variant with HCI prior probability for pathogenicity **>0.68 & ≤0.81** as per https://hci-priors.hci.utah.edu/PRIORS

**OR**

Predicted splice defect for non-canonical splicing nucleotides using SpliceAI with delta score **>= 0.2** as per Walker et al 2023.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

<sup>e</sup>Standard MSI markers panel: BAT25, BAT26, BAT40, BAT34, D5S346, D17S250, ACTC, D18S55, D10S197, MYCL; D2S123, D18S69; NR21, NR24, NR27

**Protein Expression and consistency with variant location:** IHC evidence should be consistent with the variant gene and the protein that is tested and take into account the MutSα and MutLα heterodimers: MLH1 and PMS2 loss is consistent with an MLH1 pathogenic variant, MSH2 and MSH6 loss is consistent with an MSH2 pathogenic variant, MSH6 loss is consistent with an MSH6 pathogenic variant, and PMS2 loss is consistent with a PMS2 pathogenic variant.

#### Strength Levels — *Modification type: Disease-specific*

| Strength | Criteria |
|----------|----------|
| **Strong (PP4_Strong)** | ≥3 independent CRC/Endometrial MSI-H tumors in ≥2 families using a standard panel of 5-10 markers<sup>e</sup> or tumor genome **and/or** loss of MMR protein expression consistent with the variant location. MSI-H tumor with inconsistent protein expression does not meet PP4_Strong. Independent tumors can be from the same patient/family. |
| **Moderate (PP4_Moderate)** | 2 independent CRC/Endometrial MSI-H tumors using a standard panel of 5-10 markers<sup>e</sup> or tumor genome **and/or** loss of MMR protein expression consistent with the variant location. MSI-H tumor with inconsistent protein expression does not meet PP4_Moderate. |
| **Supporting (PP4)** | 1 CRC/Endometrial MSI-H tumor using a standard panel of 5-10 markers<sup>e</sup> or tumor genome **and/or** loss of MMR protein expression consistent with the variant location. MSI-H tumor with inconsistent protein expression does not meet PP4. |

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**Status: NOT APPLICABLE**

**VCEP Comment:** This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229).

---

## 3. Benign Criteria

### BA1 - Allele Frequency Stand Alone

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

#### Stand Alone (BA1) — *Modification type: Gene-specific*

GnomAD v4 Grpmax filtering allele frequency **≥ 0.0022 (0.22%)** and variant is excluded as founder pathogenic variant.

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### Strong (BS1) — *Modification type: Gene-specific*

GnomAD v4 Grpmax filtering allele frequency **≥ 0.00022 and < 0.0022 (0.022-0.22%)** and variant is excluded as founder pathogenic variant.

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

#### Strong (BS2) — *Modification type: Disease-specific*

Co-occurrence *in trans* with a known pathogenic sequence variant in the same gene in a patient with colorectal cancer after age 45 (or other LS cancer above the median age of onset for that cancer in LS<sup>d</sup>), and who has no previous or current evidence of clinical manifestations of CMMRD as per Aronson et al 2022 (Refer to 'Table for CMMRD diagnosis.pdf'). Confirmation of phase requires testing of parents or offspring.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** Refer to file 'Functional assay SVI documentation (MMR genes)' for calibrated functional assays.

\*The functional assay flowchart is a general framework for evaluating functional assays that were already performed, or from historic publications, not for prospective studies on variants. The information describing these assays are generic. The VCEP recommends use of the calibrated assays for prospective testing.

#### Strength Levels — *Modification type: General recommendation*

| Strength | Criteria |
|----------|----------|
| **Strong (BS3)** | Calibrated functional assays with functional odds for Pathogenicity **≤ 0.05** **OR** Synonymous substitutions and intronic variants with no associated mRNA aberration (either splicing or allelic imbalance) as determined by laboratory assays conducted with nonsense-mediated decay inhibition. Whenever abnormal transcripts are identified at similar levels in controls they will be considered naturally occurring isoforms and not mRNA aberrations. |
| **Supporting (BS3_Supporting)** | Calibrated functional assays with functional odds for Pathogenicity **>0.05 & ≤0.48** **OR** Variant-specific proficient function in protein and mRNA-based lab assays as per MMR functional assay flowchart. |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:**

\*For multiple pedigrees, results are combined by multiplying together.

Recommended segregation analysis tool: COOL (COsegregation OnLine) v3 — https://fenglab.chpc.utah.edu/cool3/manual.html

Copy the example pedigree format and complete the fields to build the pedigree in text format. Refer to online manual for cancer types to enter into pedigree. Click on the 'Analysis' tab to view the webform for pedigree file upload and enter appropriate parameters for population and allele frequency. Penetrance file and relative risk file are not required for MMR genes. Use the 'overall Bayes Factor' to determine evidence strength.

#### Strength Levels — *Modification type: General recommendation*

| Strength | Combined\* Bayes Likelihood Ratio<sup>f</sup> |
|----------|-----------------------------------------------|
| **Strong (BS4)** | Lack of co-segregation with disease in pedigree(s) with a combined Bayes Likelihood Ratio **<0.05** |
| **Supporting (BS4_Supporting)** | Lack of co-segregation with disease in pedigree(s) with a combined Bayes Likelihood Ratio **>0.05 & ≤0.48** |

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

**VCEP Specifications:** SpliceAI masked score option should be checked on. For HCI-PRIORS, ensure correct gene is selected from the tabs, and enter the nucleotide number in either HGVS position or HG38 genomic co-ordinate and click 'view'. The output shows 3 substitutions at the nucleotide location, with probability based on splicing and protein predictions. Ensure the 'applicable prior' is used that corresponds to the variant under review.

#### Supporting (BP4) — *Modification type: General recommendation*

Missense variant with HCI-prior probability of pathogenicity **<0.11** as per https://hci-priors.hci.utah.edu/PRIORS

**OR**

For intronic and synonymous variants: SpliceAI predicts no splicing impact with delta score **<= 0.1** as per Walker et al 2023.

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

#### Strength Levels — *Modification type: Disease-specific*

| Strength | Criteria |
|----------|----------|
| **Strong (BP5_Strong)** | ≥ 4 tumors: CRC/Endometrial tumors with MSS and/or no loss of MMR protein expression and/or LS spectrum tumors<sup>d</sup> with loss of MMR protein(s) that is inconsistent with the gene demonstrating genetic variation **OR** ≥2 BRAF V600E (CRC only)/*MLH1* methylation (in LS spectrum tumor only) with MSI-H/*MLH1* loss. |
| **Supporting (BP5)** | 2 or 3 tumors: CRC/Endometrial tumors with MSS and/or no loss of MMR protein expression and/or LS spectrum tumors<sup>d</sup> with loss of MMR protein(s) that is inconsistent with the gene demonstrating genetic variation **OR** 1 BRAF V600E (Colon only)/*MLH1* methylation (in LS spectrum tumor only) with MSI-H/*MLH1* loss. |

---

### BP7 - Synonymous/Intronic Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

#### Supporting (BP7) — *Modification type: General recommendation*

A synonymous (silent) or intronic variant at or beyond -21/+7 (5'/3' exonic). Variants may satisfy both BP7 and BP4.

---

## 4. Not Applicable Criteria

| Criterion | Status | VCEP Comment |
|-----------|--------|--------------|
| **PS4** | Not Applicable | Due to the availability of tumor IHC data for variant classification (see PP4), PS4 has not been utilized for MMR variant classification using proband counting. |
| **PM1** | Not Applicable | There are no recognized mutational hot spots that could be used for classification purposes. While there are functional domains in the MMR genes, the distribution of pathogenic variants is generalized over all the domains (unpublished data). |
| **PM4** | Not Applicable | Protein length change from an in-frame variant is not used due to lack of evidence. |
| **PM6** | Not Applicable | Please see PS2. |
| **PP2** | Not Applicable | Missense variant in a gene with low rate of benign missense changes does not apply. |
| **PP5** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BP1** | Not Applicable | Missense variant in a gene where only loss of function causes disease is not applicable. |
| **BP2** | Not Applicable | BS2 is used instead. |
| **BP3** | Not Applicable | In-frame deletions/insertions in a repetitive region without a known function is not used. |
| **BP6** | Not Applicable | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |

---

## 5. Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** ≥ 1 Strong |
| 1 Very Strong **AND** ≥ 2 Moderate |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting |
| 1 Very Strong **AND** ≥ 2 Supporting |
| ≥ 2 Strong |
| 1 Strong **AND** ≥ 3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** ≥ 2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** ≥ 4 Supporting |

> **Note on internal inconsistency in the source:** The v2.0 release notes state *"Correction: Changed '2 Strong' in combining rules from Pathogenic to Likely Pathogenic."* However, the published v2.0 combining-rules table still lists "≥ 2 Strong" under **Pathogenic** and does not list it under Likely Pathogenic. The table above reproduces the published table verbatim; this discrepancy is unresolved in the source document.

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** ≥ 2 Supporting |
| ≥ 3 Moderate |
| 2 Moderate **AND** ≥ 2 Supporting |
| 1 Moderate **AND** ≥ 4 Supporting |
| 1 Strong **AND** 2 Moderate |

### Benign Classification

| Criteria Combination |
|---------------------|
| ≥ 2 Strong |
| 1 Stand Alone |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong **AND** 1 Supporting |
| ≥ 2 Supporting |

### Variant of Uncertain Significance (VUS)

Not specified by VCEP — variants that do not meet any of the combinations above default to Uncertain Significance per Richards et al., 2015.

---

## 6. Appendices

### Appendix A: MMR PVS1 Decision Tree

From "MMR PVS1 Decision Tree.pdf" (PVS1 Decision Tree for MMR genes). MSH6-relevant branches:

#### Nonsense or Frameshift

| Condition | Strength |
|-----------|----------|
| Predicted to undergo NMD: ≤ codon 1317 in MSH6 (MLH1 ≤684; MSH2 ≤861; PMS2 ≤798) | **PVS1** |
| Not predicted to undergo NMD + truncated/altered region is critical to protein function: ≤ codon 1341 in MSH6 (MLH1 ≤753; MSH2 ≤891; PMS2 ≤798). Refer to Appendix for details. | **PVS1** |
| Not predicted to undergo NMD + role of region in protein function is unknown: between codons 1342 & 1360 in MSH6 (MLH1 codons 754, 755 or 756; MSH2 between codons 892 & 934; PMS2 between codons 799 & 862). Refer to Appendix for details. | **PVS1_Moderate** |

#### GT–AG ±1,2 Splice Sites<sup>a</sup>

| Condition | Strength |
|-----------|----------|
| Exon skipping or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD | **PVS1** |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is NOT predicted to undergo NMD | **PVS1_Moderate** |
| Exon skipping or use of a cryptic splice site preserves reading frame | **PVS1_Strong** |

#### Deletion (single exon to full gene)

| Condition | Strength |
|-----------|----------|
| Deletion (single exon to full gene) | **PVS1**<sup>a</sup> |

#### Duplication (≥1 exon in size and must be completely contained within gene)

| Condition | Strength |
|-----------|----------|
| Proven in tandem: large genomic duplications shown by laboratory studies (which define the breakpoints of the duplication) to result in a frameshift before the last splice junction (NMD predicted to occur) **OR** to result in an in-frame insertion disrupting a functional domain<sup>b</sup> or protein conformation | **PVS1** |
| Presumed in tandem: presumed by default in tandem duplication of ≥1 exon resulting in a frameshift before the last splice junction. Does not apply to variants involving the UTR (i.e. exon 1 or last exon) or whole gene duplications. | **PVS1_Strong** |

#### Initiation Codon

| Condition | Strength |
|-----------|----------|
| No known alternative start codon in other transcripts — variants in the initiation codon of MLH1 | **PVS1** |
| No known alternative start codon in other transcripts — variants in the initiation codon of **MSH6** or PMS2 | **PVS1_Strong** |
| Different functional transcript uses alternative start codon — for MSH2 further ATGs exist in-frame in exon 1 | **N/A** |

---

### Appendix B: MMR Functional Assay Flowchart

From "MMR Functional assay flowchart.pdf" — a general framework for interpreting functional assay data (not for prospective studies). Summary of the decision flow:

- **Entry:** MMR gene sequence variant type → branch to (a) in-frame indel or missense variant, or (b) splice site, silent, or intronic variant.
- **In-frame indel/missense:** If the variant is in the first/last 3 bases of the exon or a splicing impact is predicted → route to the splicing-assay branch. Otherwise, ask whether a calibrated functional assay was conducted.
  - **Yes** → quantitative multifactorial analysis **OR** convert functional LR to ACMG/AMP evidence weight.
  - **No** → require **2 independent assays with concordant results**:
    - Mammalian MMR activity assays → similar repair levels to deficient cell line or pathogenic controls → **Deficient function**; similar repair levels to wild-type or pathogenic controls → assessment of protein expression/stability. *(Both branch labels are as printed in the source; see notes.)*
    - Assessment of protein expression/stability: ≤25% relative expression or similar to deficient cell line control → **Deficient function**; ≥75% relative expression or similar to wild-type control → subcellular localization and cellular-based MMR activity assays → cytoplasmic, tolerant to DNA damage or high mutator phenotype → **Deficient function**; nuclear, sensitive to DNA damage and no mutator phenotype → **Proficient function**.
    - Inconclusive results at any node → **Further research calibrating against clinical data**.
- **Splice site/silent/intronic:** splicing assay → complete impact → **Deficient function**; unknown/partial impact → if in-frame or missense variant, route back to the functional-assay branch; no impact → if in-frame or missense variant, route back to the functional-assay branch, otherwise check whether NMD inhibitors were included → yes → **Proficient function**; no → further research. Patient-derived RNA assays feed back into deficient/proficient determination.

---

### Appendix C: Approved Functional Assays

From "Functional assay SVI documentation.xlsx" (sheet "MMR assays"). All assays listed are marked "Approved assay: y".

| PMID(s) | Author / Year | Assay | Normal readout threshold | Abnormal readout threshold | Proposed strength |
|---------|---------------|-------|--------------------------|----------------------------|-------------------|
| 30504929; 31965077 | Drost 2018; Drost 2020 | **CALIBRATED ASSAY:** MMR protein repair capacity as a complete process — CIMRA functional assay using cell-free system (HCT116 cells lacking PMS2/MLH1 or LoVo cells lacking MSH2/MSH6) | ≥70% for MLH1 and MSH2, and **≥100% for MSH6** and PMS2 | <23% for MLH1 and MSH2, and **<18% for MSH6** and PMS2 | PS3, PS3_Moderate, PS3_Supporting, BS3, BS3_Supporting |
| 33357406; 36550560 | Jia 2021; Scott 2022 | **CALIBRATED ASSAY:** chemical selection for MMR dysfunction + deep sequencing to identify surviving MSH2 variants | LOF score <= 0 | LOF score > 0.4 | PS3, BS3 |
| 36054288 | Rath 2022 | **CALIBRATED ASSAY:** functional impact of MLH1 variants on MMR-associated repair and damage response (hESC CRISPR) | OddsPath_Functional scores < 0.48 | OddsPath_Functional scores > 2.08 | PS3, PS3_Moderate, PS3_Supporting, BS3, BS3_Supporting |
| 24362816 | Thompson 2013 | MMR protein repair capacity as a complete process — cell-free systems | >75% in two independent assays | <25% in two independent assays | PS3_moderate, BS3_supporting |
| 24362816 | Thompson 2013 | Mammalian MMR activity complementation assays | >75% in two independent assays | <25% in two independent assays | PS3_moderate, BS3_supporting |
| 24362816 | Thompson 2013 | MMR protein expression — cellular-based assay in human/mouse expression system (MSH6 deficient: HCT15) | >75% in two independent assays | <25% in two independent assays | PS3_moderate, BS3_supporting |
| 24362816 | Thompson 2013 | MMR protein subcellular localization (mammalian/yeast cells) | Nuclear localization | Cytoplasmic in localization | PS3_moderate, BS3_supporting |
| 31332305 | Morak 2019 | cDNA analysis of full-length transcripts (FLT) for MMR genes to assess splicing and transcript integrety *(sic)* | biallelic (50 ± 10%) | Allelic loss (≤10%) | PS3_moderate, BS3_supporting |
| 30998989 | Bouvet 2019 | Cell survival following exposure to a methylating agent (HCT116 or LoVo) | Mean survival score < 68.7% (MLH1); < 45.54% (MSH2) | Mean survival score > 68.7% (MLH1); > 45.54% (MSH2) | PS3_moderate, BS3_supporting |

**Validation controls** (P/LP vs B/LB counts): Drost 10 (MLH1, MSH2) + 3 (MSH6) vs 10 (MLH1, MSH2) + 4 (MSH6); Jia/Scott 22 vs 26; Rath 11 vs 11; Thompson cell-free 23 vs 14; Thompson mammalian 7 vs 5; Thompson expression 18 vs 10; Thompson localization 16 vs 10; Morak 25 vs 33; Bouvet 10 (MLH1) + 10 (MSH2) vs 9 (MLH1) + 11 (MSH2).

---

### Appendix D: CMMRD Diagnostic Scoring Table

Table 3. Scoring system for aiding CMMRD diagnosis from C4CMMRD (adapted from Aronson et al 2022; PMID: 33622763).

**>=3 points = CMMRD features meets PM3 criteria after excluding the diagnosis of NF1 or LFS as individuals with those disorders could easily get to 3 points.**

| Malignancies/premalignancies: one is mandatory; if more than one is present in the patient, add the points | Points |
|-----------------------------------------------------------------------------------------------------------|--------|
| Carcinoma from the LS spectrum\* at age <25 years. | 3 points |
| Multiple bowel adenomas at age <25 years and absence of APC/MUTYH mutation(s) or a single high-grade dysplasia adenoma at age <25 years. | 3 points |
| WHO grade III or IV glioma at age <25 years. | 2 points |
| NHL of T cell lineage or sPNET at age <18 years | 2 points |
| Any malignancy at age <18 years. | 1 point |

| Additional features: optional; if more than one of the following is present, add the points | Points |
|----------------------------------------------------------------------------------------------|--------|
| Clinical sign of NF1 and/or ≥2 hyperpigmented and/or hypopigmented skin alterations Ø>1 cm. | 2 points |
| Diagnosis of LS in a first-degree or second-degree relative. | 2 points |
| Carcinoma from LS spectrum\* before the age of 60 in a firstdegree *(sic)*, second-degree or third-degree relative. | 1 point |
| A sibling with carcinoma from the LS spectrum\*, high-grade glioma, sPNET or NHL. | 2 points |
| A sibling with any type of childhood malignancy. | 1 point |
| Multiple pilomatricomas in the patient. | 2 points |
| One pilomatricoma in the patient. | 1 point |
| Agenesis of the corpus callosum or non-therapy-induced cavernoma in the patient. | 1 point |
| Consanguineous parents | 1 point |
| Deficiency/reduced levels of IgG2/4 and/or IgA. | 1 point |

\*Colorectal, endometrial, small bowel, ureter, renal pelvis, biliary tract, stomach, bladder carcinoma

CMMRD, constitutional mismatch repair deficiency; LS, Lynch syndrome; NF1, neurofibromatosis type 1; NHL, non-Hodgkin's lymphoma; sPNET, supratentorial primitive neuroectodermal tumours.

---

### Appendix E: Footnotes (from Appendix.docx)

| Footnote | Text |
|----------|------|
| **a** | PVS1 criteria is adapted from Tayoun et al. 2018. |
| **b** | A known functional protein domain is reported to harbor sequence variants that introduce deleterious changes to protein function (via missense alteration, protein sequence deletion, or protein truncation in the last exon) AND are associated with high risk of cancer. Physical boundaries for functional domains are shown in MMR functional domains pdf. |
| **c** | IVS±1 and IVS±2 are the least invariant nucleotides in a splice site |
| **d** | Lynch Syndrome (LS) tumors include: colorectal/colon/rectal, endometrial, ovarian, small bowel/small intestine, renal pelvis, ureter, and stomach/gastric carcinomas, sebaceous skin tumors (adenomas and carcinomas), gliomas. |
| **e** | Standard MSI markers panel: BAT25, BAT26, BAT40, BAT34, D5S346, D17S250, ACTC, D18S55, D10S197, MYCL; D2S123, D18S69; NR21, NR24, NR27 |
| **f** | Likelihood ratios for segregation can be derived by Bayes factor analysis adapted from the method of Thompson et al. 2003. Penetrance estimates for MLH1 and MSH2 are from Jenkins et al. 2015 and Dowty et al. 2013; MSH6 from Baglietto et al. 2010; PMS2 from ten Broeke et al. 2015 |

---

### Appendix F: Exon Deletions/Duplications — In-frame / Out-of-frame

Determined using https://databases.lovd.nl/shared/scripts/readingFrameChecker.php

\*First and last exon deletions/duplications are difficult to predict whether in-frame or out-of-frame.

| Exon | MLH1 | MSH2 | **MSH6** | PMS2 |
|------|------|------|----------|------|
| Exon 1 | N/A\* | N/A\* | **N/A\*** | N/A\* |
| Exon 2 | Out-of-frame | Out-of-frame | **Out-of-frame** | Out-of-frame |
| Exon 3 | In-frame | In-frame | **Out-of-frame** | In-frame |
| Exon 4 | Out-of-frame | In-frame | **Out-of-frame** | Out-of-frame |
| Exon 5 | Out-of-frame | In-frame | **Out-of-frame** | Out-of-frame |
| Exon 6 | Out-of-frame | Out-of-frame | **Out-of-frame** | In-frame |
| Exon 7 | Out-of-frame | Out-of-frame | **In-frame** | Out-of-frame |
| Exon 8 | Out-of-frame | Out-of-frame | **Out-of-frame** | Out-of-frame |
| Exon 9 | Out-of-frame | Out-of-frame | **Out-of-frame** | Out-of-frame |
| Exon 10 | Out-of-frame | Out-of-frame | **N/A\*** | In-frame |
| Exon 11 | Out-of-frame | Out-of-frame | — | Out-of-frame |
| Exon 12 | Out-of-frame | In-frame | — | In-frame |
| Exon 13 | Out-of-frame | Out-of-frame | — | Out-of-frame |
| Exon 14 | Out-of-frame | Out-of-frame | — | Out-of-frame |
| Exon 15 | Out-of-frame | Out-of-frame | — | N/A\* |
| Exon 16 | In-frame | N/A\* | — | — |
| Exon 17 | In-frame | — | — | — |
| Exon 18 | In-frame | — | — | — |
| Exon 19 | N/A\* | — | — | — |

---

### Appendix G: Important Notes (from Appendix.docx)

- PMS2 NGS results need confirmation by other orthogonal assays as well as functional assessment (e.g. Long-Range or cDNA), if variants are located in the PMS2CL pseudogene homologous regions (exons 11-15). *(MMR-panel-wide note; not MSH6-specific.)*
- Gene-specific penetrance estimates are available at http://lscarisk.org/

**Justification for last exon PVS1 boundaries — Nonsense/frameshift variant introducing Premature Termination Codon (PTC):**

1. ≤ codon 753 in MLH1 using location of known pathogenic variant MLH1 c.2252_2253del
2. ≤ codon 891 in MSH2 using location of known pathogenic variant MSH2 c.2662del
3. **≤ codon 1341 in MSH6 using location of known pathogenic variant MSH6 c.3984_3987dup**
4. ≤ codon 798 in PMS2 using ≥50 nucleotide NMD-rule.

**Derivation of probability values from Odds:**

- 0.11 probability corresponds to the odds of 0.48 for Benign Supporting level of benign evidence using 0.2 prior – consistent with ACMG Bayesian model.
- 0.68 probability corresponds to the odds of 2.08 for Pathogenic Supporting level of evidence using 0.5 prior – consistent with ACMG Bayesian model.
- 0.81 probability corresponds to the odds of 4.3 for Pathogenic Supporting level of evidence using 0.5 prior – consistent with ACMG Bayesian model.

---

### Appendix H: MSH6 Functional Domains

From "MMR functional domains.pdf" — linear schematic of mismatch repair gene functional domains according to amino acid positions. Adapted from InSiGHT criteria v2.4 (https://www.insight-group.org/content/uploads/2018/08/2018-06_InSiGHT_VIC_v2.4.pdf).

MSH6 (NM_000179.3; protein 1–1360), domains as depicted (approximate amino acid boundaries as printed in the schematic):

| Domain | Approximate aa range |
|--------|----------------------|
| PCNA interaction | ~1–30 (N-terminal) |
| PWWP | ~89–194 |
| NLS | ~249–260 |
| DNA binding | ~253–313 |
| MSH2 interaction | ~360–675 |
| Connector | ~361–405 |
| Lever | ~406–701 |
| Clamp | ~669–681 |
| ATPase | ~1132–1360 (extending from ~701) |
| MSH2 interaction (C-terminal) | ~1302–1360 |

> **Caveat:** These boundaries are read from a graphical schematic in the supplementary PDF and are approximate. For authoritative boundaries, consult the source figure directly.

---

### Appendix I: Pilot Variants (MSH6 only)

From "VCEP pilot variants - MMR.xlsx" — provisional classifications by the InSiGHT Hereditary Colon Cancer / Polyposis EP.

| Variant | ClinVar ID | EP provisional classification | Codes applied |
|---------|-----------|-------------------------------|---------------|
| NM_000179.3(MSH6):c.107C>T (p.Ala36Val) | 140779 | Benign | BS1, BP4, BS2 |
| NM_000179.3(MSH6):c.663A>C (p.Glu221Asp) | 89552 | Likely benign | BS1, BP4 |
| NM_000179.3(MSH6):c.884A>G (p.Lys295Arg) | 89573 | Uncertain significance | BS4_supporting |
| NM_000179.3(MSH6):c.1282A>G (p.Lys428Glu) | 455128 | Likely pathogenic | PM2_supporting, PP3, PP4, PS3 |
| NM_000179.3(MSH6):c.1296T>G (p.Phe432Leu) | 216294 | Likely pathogenic | PS3, PP3, PM2_supporting |
| NM_000179.3(MSH6):c.1723G>T (p.Asp575Tyr) | 216300 | Likely pathogenic | PM2_supporting, PP4_strong, PP3_moderate |
| NM_000179.3(MSH6):c.3482CTG[1] (p.Ala1162del) | 140774 | Likely pathogenic | PM2_supporting, PS3, PP4 |

---

### Appendix J: Population Frequency Thresholds Summary

| Criterion | Threshold (gnomAD v4) | Strength |
|-----------|-----------------------|----------|
| BA1 | Grpmax filtering AF ≥ 0.0022 (0.22%) and variant excluded as founder pathogenic variant | Stand Alone |
| BS1 | Grpmax filtering AF ≥ 0.00022 and < 0.0022 (0.022–0.22%) and variant excluded as founder pathogenic variant | Strong |
| PM2 | < 0.00002 (<1 in 50,000 alleles) | Supporting |

---

### Appendix K: References

1. Belman S, Parsons MT, et al. *Considerations in assessing germline variant pathogenicity using cosegregation analysis.* Genet Med (2020) 22(12) p. 2052-2059. 10.1038/s41436-020-0920-4. PMID: 32773770
2. Aronson M, Colas C, et al. *Diagnostic criteria for constitutional mismatch repair deficiency (CMMRD): recommendations from the international consensus working group.* J Med Genet (2022) 59(4) p. 318-327. 10.1136/jmedgenet-2020-107627. PMID: 33622763
3. Li S, Qian D, et al. *Tumour characteristics provide evidence for germline mismatch repair missense variant pathogenicity.* J Med Genet (2020) 57(1) p. 62-69. 10.1136/jmedgenet-2019-106096. PMID: 31391288
4. Canson DM, Dumenil T, et al. *The splicing effect of variants at branchpoint elements in cancer genes.* Genet Med (2022) 24(2) p. 398-409. 10.1016/j.gim.2021.09.020. PMID: 34906448
5. Cyr JL, Brown GD, et al. *The predicted truncation from a cancer-associated variant of the MSH2 initiation codon alters activity of the MSH2-MSH6 mismatch repair complex.* Mol Carcinog (2012) 51(8) p. 647-58. 10.1002/mc.20838. PMID: 21837758
6. Drost M, Tiersma Y, et al. *A functional assay-based procedure to classify mismatch repair gene variants in Lynch syndrome.* Genet Med (2019) 21(7) p. 1486-1496. 10.1038/s41436-018-0372-2. PMID: 30504929
7. Drost M, Tiersma Y, et al. *Two integrated and highly predictive functional analysis-based procedures for the classification of MSH6 variants in Lynch syndrome.* Genet Med (2020) 22(5) p. 847-856. 10.1038/s41436-019-0736-2. PMID: 31965077
8. Rath A, Radecki AA, et al. *A calibrated cell-based functional assay to aid classification of MLH1 DNA mismatch repair gene variants.* Hum Mutat (2022) 43(12) p. 2295-2307. 10.1002/humu.24462. PMID: 36054288
9. Rayner E, Tiersma Y, et al. *Predictive functional assay-based classification of PMS2 variants in Lynch syndrome.* Hum Mutat (2022) 43(9) p. 1249-1258. 10.1002/humu.24387. PMID: 35451539
10. Tavtigian SV, Greenblatt MS, et al. *Modeling the ACMG/AMP variant classification guidelines as a Bayesian classification framework.* Genet Med (2018) 20(9) p. 1054-1060. 10.1038/gim.2017.210. PMID: 29300386
11. Abou Tayoun AN, Pesaran T, et al. *Recommendations for interpreting the loss of function PVS1 ACMG/AMP variant criterion.* Hum Mutat (2018) 39(11) p. 1517-1524. 10.1002/humu.23626. PMID: 30192042
12. Thompson BA, Walters R, et al. *Contribution of mRNA Splicing to Mismatch Repair Gene Sequence Variant Interpretation.* Front Genet (2020) 11 p. 798. 10.3389/fgene.2020.00798. PMID: 32849802
13. Whiffin N, Minikel E, et al. *Using high-resolution variant frequencies to empower clinical genome interpretation.* Genet Med (2017) 19(10) p. 1151-1158. 10.1038/gim.2017.26. PMID: 28518168
14. Walker LC, Hoya M, et al. *Using the ACMG/AMP framework to capture evidence related to predicted and observed impact on splicing: Recommendations from the ClinGen SVI Splicing Subgroup.* Am J Hum Genet (2023) 110(7) p. 1046-1067. 10.1016/j.ajhg.2023.06.002. PMID: 37352859

---

## Document History

| Version | Released | Release Notes (verbatim from the specification) |
|---------|----------|--------------------------------------------------|
| 2.0 | 3/5/2026 | PS1 Moderate (Change to bring into closer alignment with Walker et al) — Variants affecting the same non-canonical splice nucleotide as a likely pathogenic splice variant with similar or worse splicing in silico prediction using SpliceAI.<br><br>PS2 and Similarly for PM3 - updated points range.<br><br>Fixes to capitalisation of Pathogenic/Likely Pathogenic terms.<br><br>Correction: Footnotes corrected in criteria and Appendix. Corrections to PS2 criteria. List of exons that would be in-frame and out-of-frame added to Appendix.<br><br>Correction: Changed "2 Strong" in combining rules from Pathogenic to Likely Pathogenic.<br><br>Amendment: Minor change to PM2 allele frequency format (1/50000 = 0.00002) |

---

## Source Documents

Generated from ClinGen CSpec GN138 (downloaded 2026-08-06):

- `ClinGen_ACMG_Specifications_MSH6_v2.0.pdf` (main specification)
- `MMR PVS1 Decision Tree.pdf`
- `MMR Functional assay flowchart.pdf`
- `MMR functional domains.pdf`
- `Table for CMMRD diagnosis.pdf`
- `Appendix.docx`
- `Functional assay SVI documentation.xlsx`
- `VCEP pilot variants - MMR.xlsx`

*This document was compiled from ClinGen VCEP specifications. For the most current version, please refer to https://cspec.genome.network/cspec/ui/svi/doc/GN138.*
