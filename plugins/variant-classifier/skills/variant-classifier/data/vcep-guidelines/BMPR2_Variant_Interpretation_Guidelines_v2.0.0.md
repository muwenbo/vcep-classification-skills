# Comprehensive Variant Interpretation Guidelines for BMPR2

## ClinGen Pulmonary Hypertension VCEP Specifications for BMPR2 (Version 2.0)

**Affiliation:** Pulmonary Hypertension Variant Curation Expert Panel (PH VCEP)
**Version:** 2.0
**Release Date:** January 30, 2026
**Specification Type:** Tavtigian et al., 2020 - Bayesian adaptation of Richards et al., 2015
**DOI:** 10.5281/zenodo.21434642
**Specification URL:** https://cspec.genome.network/cspec/ui/svi/doc/GN125 (GN125)

---

## Table of Contents

1. [Gene and Disease Information](#1-gene-and-disease-information)
2. [Point-Based Classification System](#2-point-based-classification-system)
3. [Pathogenic Criteria](#3-pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo (Confirmed)](#ps2---de-novo-confirmed)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PS4 - Prevalence in Affected](#ps4---prevalence-in-affected)
   - [PM1 - Mutational Hot Spot / Critical Domain](#pm1---mutational-hot-spot--critical-domain)
   - [PM2 - Absent from Controls](#pm2---absent-from-controls)
   - [PM4 - Protein Length Changes](#pm4---protein-length-changes)
   - [PM5 - Novel Missense at Same Residue](#pm5---novel-missense-at-same-residue)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP2 - Missense in Constrained Gene](#pp2---missense-in-constrained-gene)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
4. [Benign Criteria](#4-benign-criteria)
   - [BA1 - Stand-Alone Benign](#ba1---stand-alone-benign)
   - [BS1 - Allele Frequency Greater Than Expected](#bs1---allele-frequency-greater-than-expected)
   - [BS2 - Observed in Healthy Adult](#bs2---observed-in-healthy-adult)
   - [BS3 - Functional Studies (Benign)](#bs3---functional-studies-benign)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP2 - Observed in cis with Pathogenic Variant](#bp2---observed-in-cis-with-pathogenic-variant)
   - [BP3 - In-frame Indel in Repetitive Region](#bp3---in-frame-indel-in-repetitive-region)
   - [BP4 - Computational Evidence (Benign)](#bp4---computational-evidence-benign)
   - [BP5 - Alternate Molecular Basis](#bp5---alternate-molecular-basis)
   - [BP7 - Synonymous/Intronic Variants](#bp7---synonymousintronic-variants)
5. [Not Applicable Criteria](#5-not-applicable-criteria)
6. [Rules for Combining Criteria](#6-rules-for-combining-criteria)
7. [Appendices](#7-appendices)

---

## 1. Gene and Disease Information

| Parameter | Value |
|-----------|-------|
| **Gene** | BMPR2 (HGNC:1078) |
| **HGNC Name** | bone morphogenetic protein receptor type 2 |
| **Reference Transcript** | NM_001204.7 |
| **Disease** | pulmonary arterial hypertension |
| **MONDO ID** | MONDO:0015924 |
| **Mode of Inheritance** | Autosomal dominant inheritance |

### Key Gene/Disease Characteristics (per VCEP)

- PAH has a prevalence of 15-50 cases/million individuals.
- There is no evidence for a genetic ancestry effect on PAH prevalence.
- *BMPR2* variants exhibit incomplete penetrance and PAH exhibits variable age of onset.
- Both LOF and missense variants are known to cause PAH.
- Critical regions for protein function: ligand binding domain (aa 33-131), kinase domain (aa 203-504), heterodimerization domain (aa 485-492), and transmembrane domain (aa 151-171).
- Scope note (from VCEP pilot): the scope of work for the PH VCEP is limited to hereditary and idiopathic PAH, not PAH associated with other diseases (e.g. congenital heart disease).

---

## 2. Point-Based Classification System

The VCEP has adopted a **modified version of the Bayesian points system** for evidence code combinations developed by Tavtigian et al. (2020; PMID: 32720330). **Likely benign is defined as -2 to -6 instead of -1 to -6.**

Variants meeting BA1 are automatically classified as benign without assessing other evidence for or against pathogenicity, and are therefore not part of the point system.

### Point Values for ACMG/AMP Strength of Evidence Categories (Tavtigian et al. 2020, Table 2)

| Evidence Strength | Pathogenic | Benign |
|-------------------|-----------|--------|
| Indeterminate | 0 | 0 |
| Supporting | 1 | -1 |
| Moderate | 2 | -2 |
| Strong | 4 | -4 |
| Very strong | 8 | -8 |

### Point-Based Variant Classification Categories (Tavtigian et al. 2020, Table 3, modified)

| Category | Point Ranges (supplementary document) | Point Ranges (CSpec summary table) |
|----------|---------------------------------------|------------------------------------|
| Pathogenic | ≥10 | 10 |
| Likely pathogenic | 6 to 9 | 6 - 9 |
| Uncertain significance | -1 to 5 | -1 - 5 |
| Likely benign | -2 to -6 | -6 - -2 |
| Benign | ≤-7 | -7 |

*Note: the CSpec "Point Based Variant Classification Categories" table lists the Pathogenic and Benign bounds without explicit ≥/≤ symbols; the supplementary document "Point-based system for variant classification" gives them as ≥10 and ≤-7.*

---

## 3. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

Caveats:
- Beware of genes where LOF is not a known disease mechanism (e.g. GFAP, MYH7).
- Use caution interpreting LOF variants at the extreme 3' end of a gene.
- Use caution with splice variants that are predicted to lead to exon skipping but leave the remainder of the protein intact.
- Use caution in the presence of multiple transcripts.

**VCEP Specifications:**

Biologically relevant transcript: NM_001204.7. LOF variants 5' or at c.2816 (exons 1-12) are expected to undergo NMD. Variants 3' to c.2816 (exon 13) are not expected to undergo NMD. Exon 13 does not contain regions critical for protein function and encodes <10% of the protein. Variants p.Trp9* and p.Trp13* (W13*) are known to escape NMD and produce a truncated protein (PMID: 20095988). Critical regions for protein function: ligand binding domain (aa 33-131), kinase domain (aa 203-504), heterodimerization domain (aa 485-492), and transmembrane domain (aa 151-171). For canonical splice variants, RNA splicing assay data is not necessary for applying PVS1; follow the decision tree based on the predicted effect of disrupted splicing. Note that exons 2, 3, 4, 6 are in-frame and a loss of a canonical splice acceptor/donor is not expected to result in NMD. Non-canonical splice site variants with RNA splicing assay data may be applicable for PVS1 according to the decision tree. The initiation codon is located in exon 1. There are approximately 27 in-frame downstream AUG initiation codons including 5 sites located in ex 4-6 having translation initiation scores similar or greater than the exon 1 codon (PMID: 20095988). However, there are many P/LP variants upstream of exons 4-6.

#### Strength Levels

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Very Strong** | Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where LOF is a known mechanism of disease. Caveats: use caution interpreting LOF variants at the extreme 3' end of a gene; use caution with splice variants predicted to lead to exon skipping but leave the remainder of the protein intact. **Use the PVS1 decision tree guide. | 8 | Gene-specific |
| **Strong** | Use the PVS1 decision tree guide. | 4 | Gene-specific, Strength |
| **Moderate** | Use the PVS1 decision tree guide. | 2 | Gene-specific, Strength |

*Note: No PVS1_Supporting level is specified by the VCEP. The PVS1 decision tree guide itself is not included among the downloaded supplementary files (see "Missing/Ambiguous Content").*

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:** PS1 can be applied to non-canonical splicing variants as specified below and according to guidelines by the ClinGen SVI Splicing Subgroup (PMID: 37352859). Prerequisite: the predicted event of the variant under assessment must precisely match the predicted event of the comparison (i.e. both predicted to lead to exon skipping, or both to lead to enhanced use of a cryptic splice motif), AND the strength of the prediction for the variant under assessment must be of similar or higher than the strength of the prediction for the comparison variant.

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Strong** | Same amino acid change as a previously established ***pathogenic*** variant regardless of nucleotide change. Example: Val->Leu caused by either G>C or G>T in the same codon. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level. | 4 | None |
| **Moderate** | Same amino acid change as a previously established ***likely pathogenic*** variant regardless of nucleotide change. For splice variants outside splice donor/acceptor ± 1,2 dinucleotide positions but residing in the same splice donor motif (last 3 bases of the exon and intronic positions +3 to +6) or acceptor motif (first base of the exon and intronic positions -20 to -3) as a previously established ***pathogenic*** variant. The splice motif coordinates are as defined by Walker et al 2023 (PMID: 37352859). | 2 | Strength |
| **Supporting** | For splice variants outside splice donor/acceptor ± 1,2 dinucleotide positions, same splice donor motif (last 3 bases of the exon and intronic positions +3 to +6) or acceptor motif (first base of the exon and intronic positions -20 to -3) as a previously established ***likely pathogenic*** variant. The splice motif coordinates are as defined by Walker et al 2023 (PMID: 37352859). | 1 | Strength |

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

**VCEP Specifications:** No VCEP-specific specification statement is given for PS2 beyond the strength entry below.

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Strong** | De novo (both maternity and paternity confirmed) in a patient with the disease and no family history. Note: Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity. | 4 | No change |

*Note: The VCEP does not specify a PS2/PM6 de novo point system; only the Strong level (4 points) is defined. See PM6 below.*

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product. Note: Functional studies that have been validated and shown to be reproducible and robust in a clinical diagnostic laboratory setting are considered the most well-established.

**VCEP Specifications:** Can be applied additively with PP3 if applicable. Not applicable for splicing effects; consider PVS1 (RNA).

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Strong** | Use the BMPR2 functional assay document for guidance on allowable assays. The document is based on the recommendations by Brnich et al 2019 (PMID: 31892348). Known variant validation controls (i.e. established pathogenic and benign variants) are required. One exception is if the same functional assay has been performed for the same variant by two independent groups and demonstrated to have the same functional effect by both groups. Also applicable for non-canonical splice site variants when RNA splice site assay data is available demonstrating abnormal splicing; positive and negative controls are required, preferably from patients and matched unaffected individuals. Note that splicing assay results may be tissue-sensitive. | 4 | General recommendation, Gene-specific |
| **Supporting** | Use the BMPR2 functional assay document for guidance on allowable assays as described above. If no known variant validation controls (i.e. established pathogenic and benign variants) were used, then score at the supporting strength. | 1 | General recommendation |

#### Approved Assay Classes (from "BMPR2 Functional assay guide related to PS3")

| Assay Class | PMIDs assessed | Approved | Proposed strength |
|-------------|----------------|----------|-------------------|
| Gene reporter assay (luciferase) | 12045205 | Y | PS3_strong if study includes biological and technical replicates, positive and negative controls, proper statistics (t-test, ANOVA). PS3_supporting if no known variant validation controls (i.e. established pathogenic and benign variants) were used. |
| Protein binding assay | 18321866, 12221115, 12045205, 14583445, 17515463, 12963706 | y (several annotated "standards different in 2002/2003") | PS3_strong if study includes biological and technical replicates, positive and negative controls, proper statistics (t-test, ANOVA). PS3_supporting if no known variant validation controls were used. |
| Cell proliferation | 23937428, 15845886, 33283886, 25187962, 20186146, 16497988, 28084316, 19366699 | y (all) | PS3_strong if study includes relevant cell type (PASMC, PAEC, or similar), biological and technical replicates, positive and negative controls, proper statistics (t-test, ANOVA). PS3_supporting if no known variant validation controls **or proxy/unspecified cell type** were used. |
| SMAD phosphorylation | 31826007, 21622843, 20095988, 23590310, 17600318, 15845886, 12221115 approved; **34502015 not approved** (no variant assignment possible in assay); **19324947 not approved** (no wild-type or replicates in assay) | mixed | PS3_strong if study includes biological and technical replicates, positive and negative controls, proper statistics (t-test, ANOVA). PS3_supporting if no known variant validation controls were used. (PMID 12221115 annotated "y (moderate)".) |
| Imaging, cytoplasmic retention | 12045205 | Y | PS3 strong requires biological and technical replicates, basic positive (wt) control. Otherwise, score no higher than PS3_supporting. |

**Assay readout thresholds documented in the assay guide (selected):**

| Assay / PMID | Normal readout threshold | Abnormal readout threshold |
|--------------|--------------------------|----------------------------|
| Luciferase reporter (12045205) | 150 light units | Determined by reduction below normal threhold (p value< 0.05). *[typo "threhold" preserved from source]* |
| Radioligand binding (12045205) | wild-type binding | Binding <50% of pcDNA3.0. |
| Imaging/cytoplasmic retention (12045205) | Predominant staining at the plasma membrane with limited cytoplasmic expression. | Predominant staining in the cytoplasm, especially the perinuclear area. |
| Cell proliferation (all PMIDs) | No maximum or minimum threshold, as cells from different patients/mice can exhibit different growth rates. | Same - no fixed threshold. |

*Note: the "SMAD phosphorylation" sheet contains the instruction: "Variants tested in assay (but not always labeled on blots). Only score if variants are specifically identified in assays."*

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.
- Note 1: Relative risk (RR) or odds ratio (OR), as obtained from case-control studies, is >5.0 and the confidence interval around the estimate of RR or OR does not include 1.0. See manuscript for detailed guidance.
- Note 2: In instances of very rare variants where case-control studies may not reach statistical significance, the prior observation of the variant in multiple unrelated patients with the same phenotype, and its absence in controls, may be used as moderate level of evidence.

**VCEP Specifications:** Affected individuals are defined as having a mean pulmonary artery pressure (mPAP) >20 mm Hg by right heart catheterization (RHC), or estimated by echocardiography if RHC is not advised. Strength is based on the number of unrelated PAH (heritable and/or idiopathic) probands identified with a variant. Unpublished, VCEP-approved internal case/variant data is acceptable if the proband does not have another pathogenic or likely pathogenic BMPR2 variant. Justification for the proband thresholds is provided in the "Data and citations related to PS4" attachment. **PS4 (at any strength) and PM2_supporting can be used additively.**

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Strong** | Prior observation of the variant in >4 unrelated patients with the same phenotype, and its absence in controls. | 4 | Disease-specific |
| **Moderate** | Prior observation of the variant in >3 unrelated patients with the same phenotype, and its absence in controls. | 2 | Disease-specific, Strength |
| **Supporting** | Prior observation of the variant in >1 unrelated patients with the same phenotype, and its absence in controls. | 1 | Disease-specific, Strength |

#### PS4 Supporting Data (from "Data and citations related to PS4")

Frequency of non-recurrent and recurrent pathogenic or likely pathogenic *BMPR2* variants in PAH cases reported in two peer-reviewed manuscripts (overlapping case data):

| # Patients with the same *BMPR2* variant | Machado et al 2015 (PMID: 26387786)<br>#variants observed / total #variants | Southgate et al 2020 (PMID: 31406341)<br>#variants observed / total #variants |
|---|---|---|
| ≥3 patients | 51/384 (13.3%) | 50/486 (10.3%) |
| 2 patients | 55/384 (14.3%) | 67/486 (13.8%) |
| 1 patient | 278/384 (72.4%) | 369/486 (75.9%) |

---

### PM1 - Mutational Hot Spot / Critical Domain

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

**VCEP Specifications:** Well-established functional domains for BMPR2 include the extracellular (ligand-binding) domain, protein kinase domain, and heterodimerization motif within the kinase domain. Strong evidence based on evolutionary conservation, in vitro functional assays, and protein structural analyses indicates the critical (or non-critical) nature of specific amino acid residues within each of these domains (see attached "Data and citations related to PM1"). Strength should be applied accordingly.

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Strong** | Variant changes a *critical* amino acid (residue lists below). | 4 | Gene-specific, Strength |
| **Moderate** | Variant changes an amino acid in the extracellular domain (aa 33-131) or kinase domain (aa 203-504) but without functional evidence indicating critical or non-critical. | 2 | Gene-specific |

#### Critical Residues for PM1_Strong

| Domain | Critical residues |
|--------|-------------------|
| Extracellular domain | p.Cys34, Cys60, Cys66, Cys84, Cys94, Cys99, Cys116, Cys117, Cys118, Cys123 |
| Kinase domain | p.Gly210, Gly212, Lys230, Glu/Asn245, Asp333, Asn338, Asp351, Gly353 Glu386, Asp405, Gly410, Arg491 |
| KD heterodimerization | p.Asp485, Gln486, Asp487, Ala488, Arg489, Ala490, Arg491, Leu492 |

*Source formatting preserved: the kinase domain list reads "Gly353 Glu386" without a comma separator in the spec.*

#### Non-critical / cannot-be-designated notes (PM1 section, verbatim intent)

- Gly182Asp and Met186Val have been demonstrated ***non-critical/not necessary*** for kinase activity based on a luciferase assay (PMID: 18321866) → apply BS3.
- Glu503Asp has demonstrated lack of of effect on canonical signaling in one assay, but this has not been replicated in an independent assay; in the absence of further investigation, this variant cannot be conclusively designated non-critical (do not apply BS3). *[typo "lack of of" preserved from source]*
- Tested variants in the extracellular domain (p.Gln42Arg, Gly47Asn, Gln82His, Thr102Ala, Ser107Pro) have limited or no effect on canonical signaling, but studies have indicated that they may play a role in disruption of non-canonical/SMAD-independent pathways (PMIDs: 14583445 and 16002577). In the absence of further investigation, these variants cannot be conclusively designated non-critical (do not apply BS3).

#### PM1 Supporting Evidence (from "Data and citations related to PM1")

- **Extracellular domain:** the 10 invariant cysteine residues in the BMPR2 ECD are required for correct folding. In vitro mutagenesis and X-ray crystallography identified 10 cysteine residues conserved across the related type II BMP, MIS, and activin receptors, each necessary for receptor ligand protein folding of the ligand domain (Greenwald et al. 1999, PMID: 9886286; Machado et al. 2006, PMID: 16429395). FPAH-causing missense mutations have been identified for all 10 cysteine residues; those studied by transient transfection of GFP- or myc-tagged BMPR2 constructs each appear to lead to significant protein misfolding and/or cytoplasmic retention (Nishihara et al. 2002, PMID: 12221115; Rudarakanchana et al. 2002, PMID: 12045205).
- **Kinase domain - evolutionary alignment** (Hanks & Hunter 1995, PMID: 7768349; 60 aligned eukaryotic kinases, invariant/near-invariant defined as conserved in >95% of 370 EUK species):
  - Invariant residues in BMPR2: G212, K230, D333, N338, D351, E386, D405, R491
  - Nearly invariant residues: G210, E/N245, G353, G410
- **Kinase domain - heterodimerization (structural analysis;** HDX-MS, SAXS, MD simulations; Agnew et al., Nat Commun 2021;12:4950): the αH-αI linker (residues 485-492) forms part of the ALK2/BMPR2 C-lobe dimer interface. R491 packs into the C-lobe core forming an electrostatic interaction with the sidechain of E386 and backbone carbonyl oxygens of Q403 and Q486. PAH mutations C483R, D485G, D487V, A490D/V, and R491W/Q cluster to the C1 dimer interface. **Result: residues needed for type I dimerization: 485-492.**
- **Not all kinase domain residues are critical:** luciferase assays show p.Glu503Asp is equivalent to WT when co-transfected with type I receptors, in marked contrast to p.Asp485Gly (Nasim et al. 2008, PMID: 18321866).

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium. Caveat: Population data for indels may be poorly called by next generation sequencing.

**VCEP Specifications:** PAH has a prevalence of 15-50 cases/million individuals and the population allele frequency threshold for PM2 is based on this frequency. There is no evidence for a genetic ancestry effect on PAH prevalence, so the use of any sub-population data is acceptable (as long as there is a minimum allele count of 1,000). As specified by the SVI WG, PM2 is scored at the supporting level only. **PM2_supporting and PS4 (at any strength) can be used additively.**

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Supporting** | Present at **<0.01%** among gnomAD controls, using the subpopulation with the highest frequency and at least 1,000 allele counts. Caveat: Population data for indels may be poorly called by next generation sequencing. | 1 | Disease-specific |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Moderate** | Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants. | 2 | No change |

*No VCEP-specific specification text and no PM4_Supporting level are given.*

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Moderate** | Novel missense change at an amino acid residue where a different missense change determined to be ***pathogenic*** has been seen before. Example: Arg156His is pathogenic; now you observe Arg156Cys. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level. Also applicable for variants affecting the same splice site as a confirmed splice variant with similar or worse splicing in silico predictions | 2 | General recommendation |
| **Supporting** | Novel missense change at an amino acid residue where a different missense change determined to be ***likely pathogenic*** has been seen before. | 1 | Strength |

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease. Note: May be used as stronger evidence with increasing segregation data.

**VCEP Specifications:** Note: PAH exhibits variable age of onset and incomplete penetrance. Three levels of evidence are applied based on autosomal dominant likelihood ratios of 10 (3 meioses, LOD 0.9, supporting), 30 (5 meioses, LOD 1.5, moderate), and 100 (7 meioses, LOD 2.1, strong) provided that PM2 (absent or rare in large population cohorts) is met. Demonstration of segregation in more than one family is not necessary as *BMPR2* is a well-established PAH gene. PMID: 29300372.

| Strength | Criteria | Default Points | Modification Type | Likelihood ratio | Meioses | LOD |
|----------|----------|----------------|-------------------|------------------|---------|-----|
| **Strong** | Co-segregation with disease in ≥7 affected family members. | 4 | Strength | 100 | 7 | 2.1 |
| **Moderate** | Co-segregation with disease in ≥5 affected family members. | 2 | Strength | 30 | 5 | 1.5 |
| **Supporting** | Co-segregation with disease in ≥3 affected family members. | 1 | Strength | 10 | 3 | 0.9 |

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** BMPR2 has a z-score of 3.28 for missense variants which is above the threshold of 3.09 (PMID: 40496714) for constraint.

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Supporting** | PM2_supporting and PP3 must be met. | 1 | Gene-specific |

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.). Caveat: As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Supporting** | Two out of three REVEL/AlphaMissense/CADD predictor scores must meet the thresholds for supporting as specified in Pejaver 2022 PMID: 36413997 (CADD) and Bergquist et al 2025 PMID: 40084623 (AlphaMissense, REVEL). **CADD ≥25.3, AlphaMissense ≥0.792, REVEL ≥0.644.** The criterion can also be used for non-canonical splice variants if **SpliceAI ≥0.2**. | 1 | General recommendation |

---

## 4. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Stand Alone** | Allele frequency is above **1%** in gnomAD, including any sub-population with at least 1,000 allele counts. | Not Applicable | Disease-specific |

*Variants meeting BA1 are automatically classified as Benign without assessing other evidence, and are not part of the point system.*

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Strong** | Allele frequency **≥0.1%** among gnomAD controls, using the subpopulation with the highest frequency and at least 1,000 allele counts. | -4 | Disease-specific |

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:** Strength based on number of homozygotes observed among gnomAD controls. Criteria **not applicable for heterozygotes** as *BMPR2* variants exhibit incomplete penetrance.

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Strong** | Observed in **≥3 homozygotes** in gnomAD controls or reported in the literature (healthy adult individuals). | -4 | Disease-specific, Gene-specific |
| **Moderate** | Observed in **≥2 homozygotes** in gnomAD controls or reported in the literature (healthy adult individuals). | -2 | Disease-specific, Gene-specific |
| **Supporting** | Observed in **≥1 homozygote** in gnomAD controls or reported in the literature (healthy adult individuals). | -1 | Disease-specific, Gene-specific |

---

### BS3 - Functional Studies (Benign)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:** Not applicable for splicing effects; replaced by BP7_strong (RNA).

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Strong** | Use the BMPR2 functional assay document for acceptable assays and guidance. Note that Gly182Asp and Met186Val have been demonstrated ***non-critical/not necessary*** for kinase activity based on a luciferase assay (apply BS3). We note that Glu503Asp has demonstrated lack of of effect on canonical signaling in one assay; this has not been replicated in an independent assay; in the absence of further investigation, this variants cannot be conclusively designated non-critical (do not apply BS3). While tested variants in the extracellular domain (p.Gln42Arg, Gly47Asn, Gln82His, Thr102Ala, Ser107Pro) have limited or no effect on canonical signaling, studies have indicated that they may play a role in disruption of non-canonical/SMAD-independent pathways (PMIDs: 14583445 and 16002577). In the absence of further investigation, these variants cannot be conclusively designated non-critical (do not apply BS3).<br><br>Note that p.Cys34, Cys60, Cys66, Cys84, Cys94, Cys99, Cys116, Cys117, Cys118, Cys123, Gly210, Gly212, Lys230, Glu/Asn245, Asp333, Asn338, Asp351, Gly353 Glu386, Asp405, Gly410, Asp485, Gln486, Asp487, Ala488, Arg489, Ala490, Arg491, Arg491, and Leu492 have been demonstrated ***critical*** (apply PM1_strong). | -4 | Gene-specific |
| **Supporting** | For variants that have demonstrated limited or no effect on canonical signaling but not tested for effect on non-canonical/SMAD-independent pathways (PMID: 14583445 and 16002577). | -1 | Gene-specific, Strength |

*Typos preserved from source: "lack of of effect", "this variants cannot", "Gly353 Glu386" (missing comma), and "Arg491" listed twice in the critical-residue list.*

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family. Caveat: The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

**VCEP Specifications:** Lack of disease segregation among *BMPR2* variant carriers should not be scored due to low penetrance of PAH variants in families. Lack of variant segregation in affected family members should be scored.

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Strong** | Lack of variant segregation in affected members of a family. | -4 | No change |

---

### BP2 - Observed in cis with Pathogenic Variant

**Original ACMG Summary:** Observed in trans with a pathogenic variant for a fully penetrant dominant gene/disorder or observed in cis with a pathogenic variant in any inheritance pattern.

**VCEP Specifications:** Applicable if observed in cis with a P/LP *BMPR2* variant in an individual with PAH.

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Supporting** | No change - use as originally described | -1 | No change |

---

### BP3 - In-frame Indel in Repetitive Region

**Original ACMG Summary:** In frame-deletions/insertions in a repetitive region without a known function.

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Supporting** | In frame-deletions/insertions in a repetitive region without a known function. | -1 | No change |

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc). Caveat: As many in silico algorithms use the same or very similar input, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Supporting** | Two out of three REVEL/AlphaMissense/CADD predictor scores must meet the thresholds for supporting as specified in Pejaver 2022 PMID: 36413997 (CADD) and Bergquist et al 2025 PMID: 40084623 (AlphaMissense, REVEL). **CADD ≤22.7, AlphaMissense ≤0.169, REVEL ≤0.29.** The criterion can also be used for non-canonical splice variants if **SpliceAI ≤0.1**; can be applied in conjunction with BP7. For synonymous variants, CADD ≤22.7 is sufficient since REVEL and AlphaMissense are not applicable. | -1 | General recommendation |

---

### BP5 - Alternate Molecular Basis

**Original ACMG Summary:** Variant found in a case with an alternate molecular basis for disease.

**VCEP Specifications:** Can be applied when PVS1 or PM2 AND PP3 are not met and a pathogenic/likely pathogenic variant in a PH VCEP-defined definitive gene has been identified. Definitive genes include *ACVRL1*, *ATP13A3*, *CAV1*, *EIF2AK4*, *ENG*, *GDF2*, *KCNK3*, *KDR*, *SMAD9*, *SOX17*, and *TBX4*.

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Supporting** | No change - use as originally described | -1 | No change, Strength |

---

### BP7 - Synonymous/Intronic Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

**VCEP Specifications:** Use default Splice AI predictions. Intronic variants outside of defined splicing motifs are applicable. (PMID: 37352859).

| Strength | Criteria | Default Points | Modification Type |
|----------|----------|----------------|-------------------|
| **Strong** | If BP7 is met and negative RNA splicing assay data is available, then apply BP7_strong. Acceptable splicing assays should have positive and negative controls, preferably from patients and matched unaffected individuals. Note that splicing assay results may be tissue-sensitive. | -4 | Strength |
| **Supporting** | A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. Applicable after assignment of BP4 for no adverse splicing predictions, and inclusive of exonic and intronic variants. Not applicable for synonymous variants located at the first base or the last three bases of an exon. | -1 | No change |

---

## 5. Not Applicable Criteria

| Criterion | Original Purpose | VCEP Comment (verbatim) |
|-----------|-----------------|--------------------------|
| **PM3** | In trans with pathogenic variant (recessive) | PAH is autosomal dominant. |
| **PM6** | Assumed de novo without confirmation of parentage | Confirmation of maternity and paternity is required. |
| **PP4** | Phenotype specificity | PAH does not have a single genetic etiology. |
| **PP5** | Reputable source reports pathogenic | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229) |
| **BP1** | Missense in truncating-only disease gene | Both LOF and missense variants are known to cause PAH. |
| **BP6** | Reputable source reports benign | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee. (PMID: 29543229) |

---

## 6. Rules for Combining Criteria

This specification uses the **Tavtigian et al. 2020 Bayesian points system** (modified) rather than the Richards et al. 2015 combining rules. Sum the point values of all applied criteria (see [Section 2](#2-point-based-classification-system)) and classify by total:

| Total Points | Classification |
|--------------|----------------|
| ≥10 | **Pathogenic** |
| 6 to 9 | **Likely Pathogenic** |
| -1 to 5 | **Uncertain Significance** |
| -2 to -6 | **Likely Benign** (VCEP modification; Tavtigian default is -1 to -6) |
| ≤-7 | **Benign** |

**BA1 override:** Variants meeting BA1 are automatically classified as Benign without assessing other evidence for or against pathogenicity.

---

## 7. Appendices

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Points |
|-----------|-----------|----------|--------|
| BA1 | Allele frequency >1% in gnomAD (any sub-population with ≥1,000 allele counts) | Stand Alone | N/A (auto-Benign) |
| BS1 | Allele frequency ≥0.1% among gnomAD controls (highest-frequency subpopulation, ≥1,000 allele counts) | Strong | -4 |
| PM2 | Present at <0.01% among gnomAD controls (highest-frequency subpopulation, ≥1,000 allele counts) | Supporting | +1 |

### Appendix B: In Silico Prediction Thresholds

| Tool | PP3 (deleterious) | BP4 (benign) |
|------|-------------------|--------------|
| CADD | ≥25.3 | ≤22.7 |
| AlphaMissense | ≥0.792 | ≤0.169 |
| REVEL | ≥0.644 | ≤0.29 |
| SpliceAI (non-canonical splice variants) | ≥0.2 | ≤0.1 |

*PP3/BP4 require 2 of 3 of REVEL/AlphaMissense/CADD to meet threshold. For synonymous variants, CADD ≤22.7 alone is sufficient for BP4.*

### Appendix C: Summary of Criteria Strengths and Point Values

| Criterion | Very Strong (8) | Strong (4) | Moderate (2) | Supporting (1) |
|-----------|-----------------|-----------|--------------|----------------|
| PVS1 | ✓ | ✓ | ✓ | – |
| PS1 | – | ✓ | ✓ | ✓ |
| PS2 | – | ✓ | – | – |
| PS3 | – | ✓ | – | ✓ |
| PS4 | – | ✓ | ✓ | ✓ |
| PM1 | – | ✓ | ✓ | – |
| PM2 | – | – | – | ✓ |
| PM4 | – | – | ✓ | – |
| PM5 | – | – | ✓ | ✓ |
| PP1 | – | ✓ | ✓ | ✓ |
| PP2 | – | – | – | ✓ |
| PP3 | – | – | – | ✓ |

| Criterion | Stand Alone | Strong (-4) | Moderate (-2) | Supporting (-1) |
|-----------|-------------|-------------|---------------|-----------------|
| BA1 | ✓ | – | – | – |
| BS1 | – | ✓ | – | – |
| BS2 | – | ✓ | ✓ | ✓ |
| BS3 | – | ✓ | – | ✓ |
| BS4 | – | ✓ | – | – |
| BP2 | – | – | – | ✓ |
| BP3 | – | – | – | ✓ |
| BP4 | – | – | – | ✓ |
| BP5 | – | – | – | ✓ |
| BP7 | – | ✓ | – | ✓ |

### Appendix D: Key References

| Citation | PMID | Topic |
|----------|------|-------|
| Richards et al., 2015 | 25741868 | ACMG/AMP Variant Interpretation Guidelines |
| Tavtigian et al., 2020 | 32720330 | Bayesian points system for evidence combination |
| Walker et al., 2023 (ClinGen SVI Splicing Subgroup) | 37352859 | Splice motif coordinates; PS1/BP7 splicing guidance |
| Brnich et al., 2019 | 31892348 | Functional assay evidence framework (PS3/BS3) |
| Pejaver et al., 2022 | 36413997 | CADD thresholds for PP3/BP4 |
| Bergquist et al., 2025 | 40084623 | AlphaMissense and REVEL thresholds for PP3/BP4 |
| ClinGen SVI VCEP Review Committee | 29543229 | PP5 and BP6 not for use |
| — | 40496714 | Missense constraint z-score threshold (3.09) used for PP2 |
| — | 29300372 | PP1 segregation likelihood ratios |
| Hamid et al., 2010 | 20095988 | NMD escape (p.Trp9*, p.Trp13*); downstream AUG initiation codons |
| Machado et al., 2015 | 26387786 | PS4 proband recurrence data |
| Southgate et al., 2020 | 31406341 | PS4 proband recurrence data |
| Greenwald et al., 1999 | 9886286 | ECD invariant cysteines |
| Machado et al., 2006 | 16429395 | BMPR2 mutations in PAH; ECD cysteines |
| Nishihara et al., 2002 | 12221115 | Functional heterogeneity of BMPR2 mutants |
| Rudarakanchana et al., 2002 | 12045205 | Luciferase, radioligand binding, imaging assays |
| Hanks & Hunter, 1995 | 7768349 | Eukaryotic protein kinase domain conservation |
| Nasim et al., 2008 | 18321866 | Kinase-domain variants; Gly182Asp/Met186Val non-critical |
| Agnew et al., 2021 (Nat Commun 12:4950) | — | ALK2/BMPR2 kinase-domain heterodimerization (aa 485-492) |

### Appendix E: PH VCEP BMPR2 Pilot Variant Results

From the supplementary file "PH VCEP Pilot Results_BMPR2 final 1.2026". These are worked examples produced by the VCEP.

| Variant (NM_001204.7) | ClinVar ID | PH EP classification | Codes applied |
|---|---|---|---|
| c.218C>G (p.Ser73Ter) | 1339369 | Pathogenic | PVS1 +8, PM2 +1, PS4_supp +1. Total +10 |
| c.354T>G (p.Cys118Trp) | 8799 | Pathogenic | PS3 +4, PS4 +4, PM1_strong +4, PM2_supp +1, PM5_supp +1, PP1 +1, PP2 +1, PP3 +1. Total +17 |
| c.968-3C>G | 425852 | VUS | PS1_mod +2, PM2_supp +1, PP3 +1, PS4_supp +1. Total +5 |
| c.1042G>A (p.Val348Ile) | 333642 | Likely benign | BS1 -4. Total -4 *(a second row for the same variant lists BS1 -4, PS3_supp +1, Total -3)* |
| c.2352C>T (p.Val784=) | 333647 | VUS | BP4 -1, BP7 -1, PM2_supp +1. Total -1 |
| c.1040G>A (p.Cys347Tyr) | 8800 | Likely pathogenic | PS4 +4, PS3_supp +1, PM2_supp +1, PM5_supp +1, PP2 +1, PP3 +1. Total +9 |
| c.-924A>G | 897238 | Benign | BA1 -8, BS2_supporting -2, BP4 -1. Total -11 |
| c.1698T>A (p.Ile566=) | 898486 | VUS | PM2 +1, BP4 -1, BP7 -1. Total -1 |
| c.2186G>C (p.Gly729Ala) | 993809 | Likely benign | BS1 -4 |
| c.-669G>A | 333629 | Benign | BA1 -8 |
| c.1424C>A (p.Ser475Ter) | 425943 | Pathogenic | PVS1 +8, PM2 +1, PS4_supp +1. Total +10 |
| c.529+2T>C | 425800 | VUS | PVS1_strong +4, PM2_supp +1. Total +5 |
| c.1481C>T (p.Ala494Val) | 333645 | VUS | PM1 +2, PP3 +1, BS1 -4. Total -1 |
| c.545G>A (p.Gly182Asp) | 8813 | Likely benign | PP3 +1, BS3 -4. Total -3 |
| c.1766A>G (p.Tyr589Cys) | 425966 | Likely benign | BS1 -4 |
| c.240_241insT (p.Lys81Ter) | 425725 | Likely pathogenic | PVS1 +8, PM2_supp +1. Total +9 |
| c.247+1_247+7del | 425731 | Likely pathogenic | PVS1_strong +4, PS1_mod +2, PM2_supp +1. Total +7 |
| c.1509A>C (p.Glu503Asp) | 409828 | VUS | No criterion applied. Total 0 |
| c.1472G>A (p.Arg491Gln) | 8806 | Pathogenic | PS2 +4, PS3 +1, PS4 +4, PM1 +4, PM2_supp +1, PM5 +2, PP1 +1, PP2 +1, PP3 +1. Total +20 |
| c.2618G>A (p.Arg873Gln) | 425999 | Benign | BS1 -4, BS4 -4, BS3_supp -1. Total -9 |
| c.319T>C (p.Ser107Pro) | 425757 | *(no classification listed)* | Roberts et al 2004 PMID: 15358693 proband is PAH associated with congenital heart disease; out of PH VCEP scope |
| c.251G>A (p.Cys84Tyr) | 812796 | Pathogenic | PS4_mod +2, PM1_strong +4, PM5_mod +2, PM2_supp +1, PP2 +1, PP3_supp +1. Total +11 |
| c.2887G>T (p.Gly963Cys) | 333651 | Likely benign | BS1 -4. Total -4 |
| c.797G>C (p.Arg266Thr) | 212810 | VUS | No criterion applied. Total 0 (REVEL = 0.628, PP3 not applied) |
| c.901T>C (p.Ser301Pro) | 228460 | Pathogenic | PS3 +4, PS4 +4, PM1_mod +2, PM2_supp +1, PM6 +2, PP2 +1. Total +14 |
| c.419-38del | 548685 | Benign | BA1 -8, BS2 -4, BP4 -1, BP7 -1. Total -14 |
| c.1413+1G>A | 425938 | Pathogenic | PVS1 +8, PM2_supp +1, PS4_mod +2. Total +11 |
| c.2948G>A (p.Arg983Gln) | 333652 | Likely benign | BS1 -4 |
| c.968-5A>G | 409829 | Pathogenic | PVS1 (RNA) +8, PS4_supp +1, PM2_supp +1. Total +11 |

**Internal inconsistencies within the pilot file (relative to the v2.0 criteria):**
- The c.1042G>A note states "REVEL = 0.744, just below the threshold of 0.75", while the v2.0 PP3 REVEL threshold is ≥0.644.
- The c.901T>C row applies PM6 +2, but PM6 is listed as Not Applicable in the v2.0 specification.
- The c.2618G>A note mentions "BP5_mod -1" although BP5 is defined only at Supporting (-1).
- The c.1472G>A note states "PP1 was scored at supporting based on 4 confirmed meioses, not 8", whereas the PP1 table is expressed in affected family members (≥3 supporting / ≥5 moderate / ≥7 strong).

### Appendix F: Release Notes for Version 2.0 (verbatim from CSpec)

type of specification: points based system based on Tatvigian et al 2020

- clarified PS1 strong/moderate/supporting for non-canonical splice variants
- under PS3, edited "PVS1_strength (RNA)" to remove "strength"
- under PM1, removed Arg899Pro from the list of non-critical aa (also in BS3), fixed the Gly47Gln typo, and removed redundant lists of non-critical residues
- under BS1, fixed the ≥ symbol
- under BS2, added a moderate strength and adjusted the number of homozygotes for supporting and moderate

*(The misspelling "Tatvigian" is preserved from the source release notes.)*

### Appendix G: Supplementary Files Accompanying This Specification

| File | Content |
|------|---------|
| BMPR2 Functional assay guide related to PS3.xlsx | Assay-by-assay curation of gene reporter (luciferase), protein binding, cell proliferation, SMAD phosphorylation, and imaging/cytoplasmic retention assays; approval status and proposed PS3 strength |
| Data and citations related to PS4.docx | Recurrence frequency data justifying PS4 proband thresholds |
| Data and citations related to PM1.docx | Evidence for critical residues in the extracellular, kinase, and heterodimerization regions |
| PH VCEP Pilot Results_BMPR2 final 1.2026 (xlsx) | 29 pilot variant classifications |
| Point-based system for variant classification.docx | Tavtigian points tables and modified classification ranges |

---

## Document History

| Version | Date | Notes |
|---------|------|-------|
| 2.0 | January 30, 2026 | See Appendix F for VCEP release notes |

---

*This document was compiled from the ClinGen Pulmonary Hypertension Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for BMPR2 Version 2.0 (GN125) and its supplementary files. For the most current version, refer to https://cspec.genome.network/cspec/ui/svi/doc/GN125*
