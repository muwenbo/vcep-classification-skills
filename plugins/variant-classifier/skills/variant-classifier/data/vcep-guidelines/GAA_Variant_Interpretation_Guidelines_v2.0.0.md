# ClinGen Lysosomal Storage Disorders VCEP Variant Interpretation Guidelines for GAA

**Version:** 2.0.0
**Released:** June 2, 2021
**Affiliation:** ClinGen Lysosomal Storage Disorders Variant Curation Expert Panel
**Expert Panel Page:** https://clinicalgenome.org/affiliation/50009/
**Based on:** Richards et al., 2015 ACMG/AMP Guidelines

---

## Gene Information

| Attribute | Value |
|-----------|-------|
| **Gene** | GAA (HGNC:4065) |
| **HGNC Name** | alpha glucosidase |
| **Transcript** | NM_000152.4 |
| **Disease** | Glycogen storage disease II (Pompe disease) (MONDO:0009290) |
| **Inheritance** | Autosomal recessive |

---

## Release Notes (v2.0.0)

1. Specifications for PS3 and BS3 have been revised and the strength has been downgraded.
2. PM2 has been downgraded to PM2_Supporting.
3. PP4 has been revised to allow the use of additional evidence types with strength of evidence based on a points system.
4. Cases are no longer required to meet the strict PP4 criterion in order to be counted for PM3.
5. Specifications for PM1 and BS2 are now included.
6. The tools used for in silico prediction of the impact of splice variants and in frame insertions and deletions for PP3 and BP4 have been revised.

---

## General Notes

- Criteria will be combined as described in Richards et al, 2015.
- SpliceAI will be used to analyze all variants, including exonic variants such as missense, nonsense, and frameshift, for potential impact on splicing.
- If the variant is described only as an amino acid change in an evidence source, and the cDNA change is not provided, this is not sufficient and the evidence should not be used.

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

---

## Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specifications:**

Acid alpha-glucosidase is a monomeric lysosomal enzyme coded for by a single locus (GAA), with no evidence of alternative active isoforms. Loss of function (LoF) is a known mechanism for Pompe disease. There are numerous published examples of LoF variants in GAA in individuals with Pompe disease. The specifications below are based on published guidance for assigning weight of evidence for PVS1 (Abou Tayoun et al, 2018, PMID 30192042).

**Additional considerations:**
- If PVS1 is applied, PM4 will not be applied.
- If PVS1 is applied, in general, PS3 and PP3 will not be applied except for rare circumstances when approved by experts in the VCEP. However, the results of splicing assays and in silico prediction may be used to inform the strength of evidence for PVS1.
- Curators are encouraged to record any data that supports the weight of evidence assigned for PVS1, and the application of this code.

#### Strength Levels

| Strength | Criteria |
|----------|----------|
| **Very Strong** | Any nonsense, frameshift, or splice variant creating a premature stop codon before codon 916. In frame deletions of an entire exon containing critical active site/substrate binding residues (exons 8 and 10), or for which another variant removing the exon is known to be pathogenic (exons 2 and 18). |
| **Strong** | In frame loss of an exon which is part of the catalytic barrel domain and contains pathogenic/likely pathogenic non-truncating variants (exons 6 and 9). Initiator codon variant. |
| **Moderate** | Premature termination codon in the 3' end of GAA (3' to codon 916), not predicted to be detected by nonsense-mediated decay. Predicted exon-skipping due to canonical splice variant or exon deletion resulting in an in frame deletion of <10% of the gene product (exons 17, 19, and 20). |

#### Variant-Specific Guidance

> **⚠️ NOT IN DISTRIBUTED PACKAGE — could not be source-verified.** Everything in this subsection, and the introductory paragraph and "Additional considerations" above, is **absent from the GAA specification PDF**, which is the only file the package ships. That PDF states the three strength tiers above and nothing more; it does not cite Abou Tayoun et al., does not discuss intron 19, NMD, transcript structure, or interactions with PM4/PS3/PP3. This material is plausibly drawn from the "main specifications document" that the spec's PP4 criterion refers to but ClinGen does not distribute. **The strength table above is authoritative; treat the guidance below as unverified.**

**Nonsense and frameshift variants:**
- All nonsense and frameshift variants will meet PVS1 (Very Strong), unless the variant is predicted to be missed by nonsense-mediated decay (NMD) — i.e. if the resulting premature termination codon is in the last exon (exon 20) or in the last 50 nucleotides of the penultimate exon (exon 19; after c.2749, codon 916). In this case, PVS1_Moderate will be applied because <10% of the primary amino acid sequence is predicted to be lost.

> **Removed as contradicting the specification (2026-08-07):** a further rule stating that for frameshift variants 3' of c.2749 not undergoing NMD, PVS1 applies at **Strong** if >10% of the normal sequence length is altered and Moderate if <10%. The specification defines **no PVS1_Strong pathway for premature termination codons at all** — its Strong tier covers only in-frame loss of exons 6/9 and initiator codon variants — and it assigns **Moderate** to PTCs 3' of codon 916 without qualification. The removed rule would have promoted such variants to Strong on a criterion the VCEP does not use.

**Canonical splice site variants (+1, +2, -1, -2):**
- All donor/acceptor splice sites in GAA follow the GT/AG rule, except for the donor splice site of intron 19 (the last intron) which begins with GC.
- Variants in the donor splice junction of intron 19 will not meet PVS1 because the impact of alterations to GC donor splice sites is not well understood. PS3 could be applied if functional evidence is available. In silico splice site predictors should not be used for the donor splice site of intron 19 because they are designed for recognition of GT/AG splice sites.
- For all variants involving the +1 or +2 position of GT donor splice sites, the exon immediately 5' of the variant is predicted to be skipped. For all variants of the -1 or -2 position of AG acceptor splice sites, the exon immediately 3' of the variant is predicted to be skipped. See Appendix A for in frame/out of frame consequences.
- Use SpliceAI in analysis of all canonical splice site variants (see PP3 and BP4 for thresholds). If there is a nearby (within +/- 20 nucleotides) splice site sequence that may reconstitute in-frame splicing, this should be taken into consideration.
- Non +/- 1 or 2 canonical splice variants (e.g., +3 or -3) will not meet PVS1, but could meet PS3 and/or PP3 criteria.

**Initiation codon:**
- All initiator codon variants will meet PVS1_Strong based on the observation that patients (n=3) homozygous for c.1A>G are CRIM-negative (Bali et al 2012, PMID 22252923). The next in-frame methionine is at position 122 but the likelihood of this start site being used is low and, even if used, the gene product would be missing the signal sequence.
- While multiple initiator variants have been reported in GAA, PS1 or PM5 should not be used for these variants.

**Deletions:**
- If a single or multi-exon deletion results in an out-of-frame consequence, use PVS1 (Very Strong) if NMD is predicted to occur. If NMD is not predicted to occur, use PVS1_Moderate.
- If a deletion results in an in-frame consequence, the deletion must encompass one or more exons for PVS1 to apply. Consult Appendix A and use professional judgement regarding the strength of evidence to apply.
- If an in-frame deletion is smaller than one exon, PVS1 does not apply; consider using PM4.

**Duplications:**
- Single and multi-exon duplications have not yet been reported in GAA.
- Use the PVS1 decision tree to assess the impact of single and multi-exon duplications.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Same amino acid change as a previously established pathogenic variant regardless of nucleotide change. Applied as described in the original ACMG criterion. |

**Notes:**
- To avoid circularity, the classification of the other variant (Variant B) should not use evidence from the variant being interrogated (Variant A). If there is a question as to whether PS1 should be applied to variant A or variant B, use the classification of the variant with a greater level of evidence to support the classification of the variant with less evidence.

---

### PS2 - De Novo (Confirmed)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**VCEP Specifications:** Not Applicable

**Comments:** De novo variants are rarely reported in GAA (PMIDs 7981676, 27142047). The occurrence of de novo variants in GAA is not a mechanism of disease for Pompe disease, and the observation that a variant in GAA has arisen de novo does not support its causality. Any de novo variants will be assessed based on the variant type, functional evidence, and in trans data as described in these guidelines.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

**VCEP Specifications:**

Data from any studies on samples from patients, such as GAA activity measurement in cultured skin fibroblasts or dried blood spots, is included in PP4 and should NOT be used for PS3.

Any variant meeting the requirements below for either in vitro expression or splicing assays can meet PS3 (at the appropriate strength). If a variant meets the description for both (e.g., a splice site variant with evidence of abnormal splicing and deficient GAA activity in vitro), PS3 must only be counted once but may be upgraded if both types of evidence are available.

Note that these assays are in vitro, research-based, and may not truly reflect in vivo function.

| Strength | Criteria |
|----------|----------|
| **Strong** | RT-PCR evidence of mis-splicing for non-canonical intronic variants with **no** evidence of normal splice products. |
| **Moderate** | <5% wild type GAA activity when the variant is expressed in a heterologous cell type **and** evidence of abnormal GAA synthesis and/or processing. RT-PCR evidence of mis-splicing for non-canonical intronic variants **with** evidence of normal splice products. |
| **Supporting** | <30% wild type GAA activity when the variant is expressed in a heterologous cell type. RT-PCR evidence of mis-splicing for non-canonical intronic variants **with** evidence of normal splice products. |

#### Approved Assay Instances

**In vitro expression assays:**

1. **Kroos et al, 2008 (PMID 18425781) and Kroos et al, 2012 (PMID 22644586) — Erasmus Medical Center (Reuser group):**
   - These studies include expression of GAA sequence variants in cultured cells with measurement of GAA activity, and analysis of GAA synthesis and processing by Western blot and/or pulse chase.
   - PS3_Moderate: Variants in severity Classes A and B, or equivalent (GAA activity <5% and reduced mature, active GAA protein represented by 76 and 70 kD bands).
   - PS3_Supporting: Variants in severity Classes C and D, or equivalent (5-30% GAA activity).

2. **Flanagan et al (PMID 19862843):**
   - Expression of 76 different GAA variants in COS cells, measurement of enzyme activity, Western blot and immunolocalization for some variants.
   - PS3_Supporting: All variants in Table 2 (all <15% WT activity) and Table 3 (all <2% WT activity).

3. **Additional studies:**
   - After assessment of parameters and discussion with the VCEP, results from other studies can be used at PS3_Supporting for variants with <30% WT activity if appropriate, considering:
     - Were clones sequenced to verify the variant and absence of artifacts?
     - Were appropriate controls included (negative: empty vector/antisense; positive: wild type GAA/normal cells)?
     - Was the experiment replicated?
     - If cells have intrinsic GAA activity (e.g., COS cells), the level of activity should be stated.

**Splicing assays:**
- Apply PS3 for splicing assays (at appropriate strength) only for non +/-1 or 2 splicing variants. For canonical +/- 1 or 2 splicing variants, results should inform the strength of PVS1.
- PS3 can be applied for in vitro splicing assays such as mini-gene assay, RT-PCR, or RNA-Sequencing performed on mRNA from patient-derived cells or heterologous cultured cells transfected with the variant.
- For non +/-1 or 2 canonical splicing variants: use PS3 if there is RT-PCR and/or RNA sequencing evidence demonstrating only abnormal splice products with no evidence of normal splicing. The impact of the splicing defect (in frame or out of frame; number of amino acids deleted/inserted) should be taken into account.
  - Out of frame consequence → PS3
  - Use of a cryptic splice site resulting in a small insertion → PS3_Moderate
- Consider downgrading to PS3_Moderate or PS3_Supporting if there is evidence of normal splice products.
- PP3 may also be used for non-canonical splice variants meeting PS3 at any strength.

---

### PS4 - Prevalence in Affected

**Original ACMG Summary:** The prevalence of the variant in affected individuals is significantly increased compared to the prevalence in controls.

**VCEP Specifications:** Not Applicable

**Comments:** There are no case-control studies for Pompe disease. As this is a recessive disorder, the prevalence of the variant in affected individuals may not be increased compared to controls (who could be heterozygous carriers). The number of patients with the variant will be addressed by the PM3 evidence code.

---

### PM1 - Mutational Hot Spot

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g., active site of an enzyme) without benign variation.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Missense substitution or in frame deletion of residues important in the active site architecture and substrate binding of GAA: **D282, W376, D404, L405, I441, W481, W516, D518, M519, R600, W613, D616, W618, F649, L650, H674**. |

**Notes:**
- Based on crystal structures of native GAA and rhGAA (Deming et al, 2017; Roig-Zamboni et al, 2017, PMID 29061980).
- D518 is the catalytic nucleophile and D616 is the catalytic acid/base (Hermans et al, 1991, PMID 1856189).
- Other residues are important in active site architecture and substrate binding.
- There are no benign or likely benign variants of these residues in ClinVar, Erasmus, or gnomAD.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in population databases.

**VCEP Specification (Supporting only):**
- Minor allele frequency **<0.1% (0.001)** in all continental populations with >2000 alleles in gnomAD.
- The weight of evidence is downgraded from PM2 to PM2_Supporting based on guidance from the ClinGen SVI.
- Variants may be observed in the homozygous state because Pompe disease can present in adulthood, and some variants may be hypomorphic. The presence and number of homozygotes should be noted.
- Known pathogenic variants with higher frequency (e.g., c.-32-13T>G at 0.53% in European non-Finnish, c.2560C>T at 0.19% in Africans, c.1935C>A at 0.17% in East Asians) can still be classified as pathogenic without PM2_Supporting.

---

### PM3 - In Trans with Pathogenic

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**VCEP Specifications:**

- To meet PM3, the patient must be described as having Pompe disease, at a minimum. If the case meets PP4 and PM3, both criteria are applied. PP4 criteria need not necessarily be met in order to apply PM3, as long as the patient is stated to have Pompe disease.
- For rare variants that are routinely observed to be in cis with a pseudodeficiency variant, substantial additional evidence must be available. The variant must meet PM2_Supporting, functional data should be available to support a deleterious impact, and cases considered for PM3 must have other clinical and laboratory findings supporting a diagnosis of Pompe disease. Do not apply this exception for a novel variant with a single report.
- If multiple unrelated compound heterozygous cases have the same genotype and the variants are not confirmed in trans, then no more than two cases should be used for assigning points (i.e., maximum of 1 point). Care must be taken to ensure reports do not represent the same case.
- To be "confirmed in trans," parental testing in at least one parent, or another appropriate molecular method (such as cloning each allele separately followed by sequencing), must have been performed. Otherwise, the phase of the variants is unknown.
- To avoid circularity, the classification of the variant on the other allele should not use evidence from the variant being interrogated.

#### PM3 Point System (Per Proband)

| Classification/Zygosity of Other Variant | Confirmed in Trans | Phase Unknown |
|------------------------------------------|-------------------|---------------|
| Pathogenic or Likely pathogenic variant | 1.0 | 0.5 (P) / 0.25 (LP) |
| Homozygous occurrence (max points = 1.0) | 0.5 | N/A |

#### PM3 Evidence Strength Thresholds

| Total Points | Strength Level |
|--------------|----------------|
| 0.5 | PM3_Supporting |
| 1.0 | PM3 (Moderate) |
| 2.0 | PM3_Strong |
| 4.0 | PM3_VeryStrong |

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | In frame deletion/insertions of two or more amino acids but less than one exon. |
| **Supporting** | In frame deletion/insertions of one amino acid. |

**Notes:**
- In-frame deletions and insertions have been reported in GAA.
- Stop loss has not been reported in GAA other than as a result of frameshift variants.
- For in-frame deletions of one or more exons, use PVS1 instead.

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before. Caveat: Beware of changes that impact splicing rather than at the amino acid/protein level.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Moderate** | Missense change at an amino acid residue where a different missense change determined to be **pathogenic** has been seen before. |
| **Supporting** | Missense change at an amino acid residue where a different missense change determined to be **likely pathogenic** has been seen before. |

**Notes:**
- If the pathogenicity of another missense change at the same amino acid residue is unknown, determine its pathogenicity using these guidelines in order to determine if this criterion can be used.
- To avoid circularity, the classification of the other variant (variant B) should not use evidence from the variant being interrogated (variant A). If there is a question as to whether PM5 should be applied to variant A or variant B, use the classification of the variant with a greater level of evidence to support the classification of the variant with less evidence.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**VCEP Specifications:** Not Applicable

**Comments:** See explanation for PS2. De novo variants are rarely reported in GAA and the occurrence of de novo variants is not a mechanism of disease for Pompe disease.

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**VCEP Specifications:** Not Applicable

**Comments:** Sib-ships large enough to meet this criterion are extremely rare. In addition, because GAA is the only gene involved in Pompe disease, all patients are expected to be bi-allelic, regardless of whether the pathogenic variants can be, or have been, detected. A variant under assessment may not be the true pathogenic variant but instead in linkage disequilibrium with an unidentified pathogenic variant. For this reason, this criterion does not facilitate assessment of pathogenicity.

---

### PP2 - Missense in Constrained Gene

**Original ACMG Summary:** Missense variant in a gene that has a low rate of benign missense variation and where missense variants are a common mechanism of disease.

**VCEP Specifications:** Not Applicable

**Comments:** Does not apply; there are benign and pathogenic missense variants in GAA.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product.

**VCEP Specifications:**

| Variant Type | Tool | Threshold for PP3 |
|-------------|------|-------------------|
| Missense | REVEL | Score **>0.7** |
| In frame deletion/insertion | PROVEAN, MutationTaster, MutPred-InDel | Predicted deleterious by **2 out of 3** tools (PROVEAN score <-2.5 = "deleterious"; MutationTaster = "disease-causing"; MutPred-InDel score >0.5 = "pathogenic") |
| Non-canonical splice variants | SpliceAI | Score **>0.5** |

**Notes:**
- For non-canonical splice site variants (e.g., +3, -3), evidence for use of a cryptic splice site and the impact on the gene product should also be assessed.

---

### PP4 - Phenotype Specificity

**Original ACMG Summary:** Patient's phenotype or family history is highly specific for a disease with a single genetic etiology.

**VCEP Specifications:**

Because the evidence to support a diagnosis of Pompe disease in the published literature varies according to the types of evidence presented and the level of detail provided, a points scheme for determining weight of evidence for PP4 will be used.

- In order to count any evidence, the authors must also state that the patient has Pompe disease.
- Do not apply this rule if the variant meets BA1, or otherwise meets criteria for benign or likely benign status.
- If either of the pseudodeficiency variants c.1726G>A (p.Gly576Ser) or c.2065G>A (p.Glu689Lys) are present, whether heterozygous or homozygous, deficiency of GAA activity cannot be used to apply PP4. If c.271G>A (p.Asp91Asn) is present, deficiency of GAA activity cannot be used to apply PP4 if glycogen was the assay substrate, but the data can be used if 4-MU was the substrate (Nino et al, 2020; PMID 33162552).

#### PP4 Strength Thresholds

> **⚠️ NOT IN DISTRIBUTED PACKAGE — could not be source-verified.** The GAA specification's entire PP4 entry reads: *"Phenotype specific for disease with single genetic etiology. Points-based system. **See main specifications document**."* That main specifications document is **not distributed** — the package ships the specification PDF alone. Neither the thresholds below nor the point table that follows appears in any file available to us. They are detailed and Pompe-specific, so they are plausibly a faithful copy of genuine VCEP content; but they cannot be verified, and must not be treated as authoritative. (Logged as an upstream query to ClinGen.)

| Total Points | Strength |
|--------------|----------|
| <1 | PP4 not met |
| 1 to <2 | PP4 (Supporting) |
| ≥2 | PP4_Moderate |

#### PP4 Point System

| Description of Evidence | Points |
|--------------------------|--------|
| Deficient GAA activity, documented as either 1) <10% of normal mean control level of GAA activity in leukocytes, lymphocytes, or muscle samples, and/or <30% in cultured fibroblasts, or 2) Activity in the affected range (which must be provided in the publication) in any appropriate tissue (muscle, cultured skin fibroblasts, leukocytes, lymphocytes, whole blood or dried blood spot). | 2 |
| Patient reported to have Infantile Onset Pompe disease (IOPD) AND documentation of symptoms of that condition. At a minimum, cardiomegaly, hypertrophic cardiomyopathy, left ventricular hypertrophy or a related term, AND hypotonia, muscle weakness, or a related term, must be reported. | 1 |
| Cross reactive immunological material (CRIM) study of cultured skin fibroblasts or peripheral blood mononuclear cells reported to show absence of the 76 kDa and 70 kDa bands (mature, active GAA enzyme). This includes patients described as CRIM-negative (no detectable GAA protein on Western blot), or those who are CRIM-positive but do not make the mature protein (e.g., only 110 kDa and 95 kDa bands are present). | 1 |
| The patient is reported to be on enzyme replacement therapy (ERT) for Pompe disease. | 1 |
| GAA activity is reported to be deficient but the data are not provided (i.e., values for the patient and normal range not given). | 0.5 |
| Patient identified as affected by newborn screening. | 0.25 |
| Urinary Glc4 (glucose tetrasaccharide) is elevated above the normal range. | 0.25 |
| Muscle MRI shows evidence of Pompe disease. | 0.25 |
| Muscle histology is consistent with Pompe disease; there is glycogen storage in the lysosomes of muscle cells appearing as vacuoles that stain positively with periodic acid-Schiff. | 0.25 |

**Notes on PP4 evidence:**
- <10% activity in muscle is used because activity of GAA in muscle samples can overlap in patients with LOPD and carriers.
- <30% in fibroblasts accounts for higher residual GAA activity in patients with late onset Pompe disease (LOPD).
- Symptoms in IOPD are fairly specific with few other conditions mimicking this disorder; therefore documentation of symptoms alone is not sufficient for PP4 without stating the patient has Pompe disease.
- If a patient is receiving ERT, the assumption is that their diagnosis of Pompe disease is well supported by clinical and laboratory evaluations.
- Elevated urinary Glc4 has high sensitivity and specificity for Pompe disease (Young et al, 2012, PMID 22252961; Piraud et al, 2020, PMID 32382504).
- While histochemical evidence of glycogen storage in muscle is supportive of a glycogen storage disorder, it is not specific for Pompe disease.

---

### PP5 - Reputable Source

**Original ACMG Summary:** Reputable source recently reports variant as pathogenic, but the evidence is not available to the laboratory to perform an independent evaluation.

**VCEP Specifications:** Not Applicable

This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID 29543229).

---

## Benign Criteria

### BA1 - Allele Frequency >5%

**Original ACMG Summary:** Allele frequency is above 5% in population databases.

**VCEP Specification (Stand Alone):**
- Highest minor allele frequency **>1% (0.01)** in any continental population in gnomAD with >2000 alleles.
- Continental populations: European non-Finnish, African, East Asian, South Asian, and Latino (Ghosh et al, 2018, PMID 30311383).

---

### BS1 - Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

**VCEP Specification (Strong):**
- Highest minor allele frequency **>0.5% (0.005)** in any continental population in gnomAD with >2000 alleles.
- Continental populations: European non-Finnish, African, East Asian, South Asian, Latino (Ghosh et al, 2018, PMID 30311383).
- **Exception:** c.-32-13T>G is exempted from meeting BS1 because it is the most common pathogenic variant in patients with late onset Pompe disease (highest allele frequency 0.53% in European non-Finnish; Kroos et al, 2012, PMID 22253258).

---

### BS2 - Observed in Healthy Adult

**Original ACMG Summary:** Observed in a healthy adult individual for a recessive (homozygous), dominant (heterozygous), or X-linked (hemizygous) disorder, with full penetrance expected at an early age.

**VCEP Specifications:**

| Strength | Criteria |
|----------|----------|
| **Strong** | Homozygous individual of any age with normal GAA activity. Values for GAA activity and the reference range for the laboratory must be provided. |

**Notes:**
- Patients with late onset Pompe disease can present late in life (5th-6th decade), can have mild symptoms, and may remain undiagnosed. Therefore, it is possible that homozygotes for hypomorphic GAA variants could be present in population databases.

---

### BS3 - Functional Studies (No Effect)

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies show no damaging effect on protein function or splicing.

**VCEP Specifications:**

The same assays outlined for PS3 are used for BS3.

| Strength | Criteria |
|----------|----------|
| **Supporting** | >50% activity when the variant is expressed in a heterologous cell type, **or** >30% activity if there is also evidence of normal synthesis and processing. This includes Class E and F variants in Kroos et al, 2008 (PMID 18425781) and Kroos et al, 2012 (PMID 22644586). |

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**VCEP Specifications:** Not Applicable

---

### BP1-BP7 - Benign Supporting

| Criterion | Status | Comment |
|-----------|--------|---------|
| **BP1** | Not Applicable | Does not apply. All types of variants cause Pompe disease. |
| **BP2** | Applied (Supporting) | Observed in cis with a pathogenic variant (modified to account for autosomal recessive inheritance; "in trans with pathogenic for dominant disorder" portion is removed). |
| **BP3** | Not Applicable | There are no known repetitive regions without known function in GAA. |
| **BP4** | Applied (Supporting) | See table below for computational thresholds. |
| **BP5** | Not Applicable | An individual could be a carrier of a pathogenic variant in GAA and have another disorder. There is no known alternate molecular basis for deficiency of GAA activity other than variants in GAA. |
| **BP6** | Not Applicable | Per ClinGen SVI recommendation (PMID 29543229). |
| **BP7** | Applied (Supporting) | A synonymous (silent) variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved. PhyloP score <0.1, or the variant is the reference nucleotide in 1 primate and/or 3 mammalian species. |

#### BP4 Computational Thresholds

| Variant Type | Tool | Threshold for BP4 |
|-------------|------|-------------------|
| Missense | REVEL | Score **<0.5** |
| In frame deletion/insertion | PROVEAN, MutationTaster, MutPred-InDel | Predicted benign by **all 3** tools (PROVEAN score >-2.5; MutationTaster = "polymorphism"; MutPred-InDel score <0.5) |
| Non-canonical splice variants | SpliceAI | Score **<0.2** |

**Notes:**
- If there is any evidence for possible creation of a cryptic splice site, BP4 should not be applied.

---

## Rules for Combining Criteria

### Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** ≥1 Strong |
| 1 Very Strong **AND** ≥2 Moderate |
| 1 Very Strong **AND** 1 Moderate **AND** 1 Supporting |
| 1 Very Strong **AND** ≥2 Supporting |
| ≥2 Strong |
| 1 Strong **AND** ≥3 Moderate |
| 1 Strong **AND** 2 Moderate **AND** ≥2 Supporting |
| 1 Strong **AND** 1 Moderate **AND** ≥4 Supporting |

### Likely Pathogenic Classification

| Criteria Combination |
|---------------------|
| 1 Very Strong **AND** 1 Moderate |
| 1 Strong **AND** 1 Moderate |
| 1 Strong **AND** ≥2 Supporting |
| ≥3 Moderate |
| 2 Moderate **AND** ≥2 Supporting |
| 1 Moderate **AND** ≥4 Supporting |

### Benign Classification

| Criteria Combination |
|---------------------|
| 1 Stand Alone (BA1) |
| ≥2 Strong |

### Likely Benign Classification

| Criteria Combination |
|---------------------|
| 1 Strong **AND** 1 Supporting |
| ≥2 Supporting |

---

## Appendices

### Appendix A: PVS1 — as specified by the VCEP

> **Rewritten 2026-08-07.** This appendix previously presented a Tayoun-style flowchart (attributed to Figure 1 of Abou Tayoun et al, 2018, PMID 30192042 — a citation the GAA specification does not make) whose frameshift, splice, deletion and duplication branches turned on whether ">10%" or "<10% of normal sequence length" was altered. **The GAA VCEP uses no such rule.** Its rule is *positional*: codon 916. Under the removed flowchart a frameshift escaping NMD and altering <10% of the sequence was called PVS1_Moderate; where such a variant creates a premature stop **before** codon 916 the VCEP calls it **PVS1 (Very Strong)**. The grafted branches have been deleted and the criterion is reproduced below verbatim.

The GAA specification states PVS1 as three strength tiers, not a decision tree:

| Strength | Criteria as published |
|----------|-----------------------|
| **Very Strong (PVS1)** | Null variant in a gene where loss of function is a known mechanism of disease, **or** in-frame loss of an exon that contains residues involved in the active site of GAA. Specifically: any nonsense, frameshift, or splice variant creating a premature stop codon **before codon 916**; in-frame deletions of an entire exon containing critical active site / substrate binding residues (**exons 8 and 10**), or for which another variant removing the exon is known to be pathogenic (**exons 2 and 18**). |
| **Strong (PVS1_Strong)** | Null variant in a gene where loss of function is a known mechanism of disease. Specifically: in-frame loss of an exon which is part of the catalytic barrel domain and contains pathogenic/likely pathogenic nontruncating variants (**exons 6 and 9**); **initiator codon variant**. |
| **Moderate (PVS1_Moderate)** | Null variant in a gene where loss of function is a known mechanism of disease. Specifically: premature termination codon in the 3' end of GAA (**3' to codon 916**), not predicted to be detected by nonsense-mediated decay; predicted exon-skipping due to canonical splice variant or exon deletion resulting in an in-frame deletion of **<10% of the gene product** (**exons 17, 19 and 20**). |

**Modification Type:** Very Strong — None; Strong and Moderate — Strength, Disease-specific.

> **Note on the "<10%" figure:** the specification uses it in exactly one place — to characterise the in-frame loss of exons 17, 19 and 20 — and not as a general test applied to frameshifts or deletions.

**Not specified by the VCEP:** handling of duplications; handling of full gene deletions; whether the intron 19 donor site (which begins GC rather than GT) is excluded from PVS1; and whether exon 1 is untranslated. Statements on all of these previously appeared here without any source and have been removed.

### Appendix B: Active Site Residues (PM1)

The specification lists these as "residues important in the active site architecture and substrate binding of GAA". Missense substitution or in-frame deletion of any of them meets PM1 at Moderate.

D282, W376, D404, L405, I441, W481, W516, D518, M519, R600, W613, D616, W618, F649, L650, H674.

> A per-residue "Role" column was previously shown here, singling out D518 as the "catalytic nucleophile" and D616 as the "catalytic acid/base" and labelling the other fourteen "active site architecture / substrate binding". **Removed as unsourced** — the VCEP draws no distinction between these residues, and the three supporting references previously cited (Hermans 1991 PMID 1856189; Deming 2017; Roig-Zamboni 2017 PMID 29061980) appear nowhere in the specification.

### Appendix C: Population Frequency Thresholds Summary

| Criterion | Threshold | Population | Strength |
|-----------|-----------|------------|----------|
| BA1 | >1% (0.01) | Highest MAF in any continental population in gnomAD with >2000 alleles | Stand Alone |
| BS1 | >0.5% (0.005) | Highest MAF in any continental population in gnomAD with >2000 alleles | Strong |
| PM2 | <0.1% (0.001) | All continental populations with >2000 alleles in gnomAD | Supporting |

Continental populations: European non-Finnish, African, East Asian, South Asian, Latino.

**BS1 Exception:** c.-32-13T>G is exempted from BS1 (highest frequency 0.53% in European non-Finnish) as it is the most common pathogenic variant in late onset Pompe disease.

### Appendix D: Pseudodeficiency Variants

> **⚠️ NOT IN DISTRIBUTED PACKAGE — could not be source-verified.** The word "pseudodeficiency" does not appear anywhere in the GAA specification PDF, nor do any of the three variants below. This is plausibly genuine content from the undistributed main specifications document, but it is unverified.

The following pseudodeficiency variants affect the interpretation of enzyme activity results and must be considered when applying PP4:

| Variant | Effect on PP4 |
|---------|--------------|
| c.1726G>A (p.Gly576Ser) | If present (heterozygous or homozygous), deficiency of GAA activity cannot be used to apply PP4. |
| c.2065G>A (p.Glu689Lys) | If present (heterozygous or homozygous), deficiency of GAA activity cannot be used to apply PP4. |
| c.271G>A (p.Asp91Asn) | Deficiency of GAA activity cannot be used if glycogen was the assay substrate, but data can be used if 4-MU was the substrate (Nino et al, 2020; PMID 33162552). |

### Appendix E: Reference PMIDs

| PMID | Reference |
|------|-----------|
| 1856189 | Hermans et al, 1991 — Active site residues and catalytic mechanism |
| 7981676 | De novo GAA variant report |
| 15520017 | Moreland et al, 2005 — GAA processing details |
| 18425781 | Kroos et al, 2008 — In vitro expression studies with severity classification |
| 19862843 | Flanagan et al — Expression of 76 GAA variants in COS cells |
| 22252923 | Bali et al, 2012 — CRIM analysis; initiator codon variant data |
| 22252961 | Young et al, 2012 — Urinary Glc4 sensitivity/specificity |
| 22253258 | Kroos et al, 2012 — c.-32-13T>G as most common LOPD variant |
| 22644586 | Kroos et al, 2012 — In vitro expression studies |
| 26693141 | Bali et al, 2015 — CRIM analysis in Pompe disease |
| 27142047 | De novo GAA variant report |
| 29061980 | Roig-Zamboni et al, 2017 — GAA crystal structure |
| 29543229 | ClinGen SVI recommendation on PP5/BP6 |
| 30192042 | Abou Tayoun et al, 2018 — PVS1 weight of evidence guidance |
| 30311383 | Ghosh et al, 2018 — Population frequency threshold calculations |
| 32382504 | Piraud et al, 2020 — Urinary Glc4 reference |
| 33162552 | Nino et al, 2020 — Pseudodeficiency variant p.Asp91Asn |

### Appendix F: GAA Processing Overview

> **⚠️ NOT IN DISTRIBUTED PACKAGE — could not be source-verified.** Neither the processing description nor the Kroos severity classification below appears in the GAA specification PDF; "Kroos", "kDa" and PMID 15520017 are absent from it entirely. The class → PS3/BS3 strength mapping at the end of this appendix is therefore **an unverified claim about how criteria are assigned**, and the specification's own PS3 and BS3 entries (which are stated in terms of % wild-type activity, not Kroos classes) should be preferred where they conflict.

GAA is synthesized as a 110 kDa precursor that undergoes processing to form the 95 kDa intermediate, and then the mature, active forms (76 kDa and 70 kDa). Abnormal synthesis and/or processing is evidenced by absence or reduced levels of the mature 76 kDa and 70 kDa bands on Western blot (see Moreland et al, 2005, PMID 15520017 for details).

**Severity classification (Kroos et al):**
| Class | GAA Activity | Processing |
|-------|-------------|------------|
| A | Very severely reduced (<5%) | Reduced mature protein |
| B | Severely reduced (<5%) | Reduced mature protein |
| C | Reduced (5-30%) | Variable |
| D | Reduced (5-30%) | Variable |
| E | Normal or near-normal (>50%) | Normal |
| F | Normal or near-normal (>30% with normal processing) | Normal |

- Classes A and B → PS3_Moderate
- Classes C and D → PS3_Supporting
- Classes E and F → BS3_Supporting

---

## Criteria Summary Table

| Criterion | Strength | Status | Key Specification |
|-----------|----------|--------|-------------------|
| PVS1 | Very Strong / Strong / Moderate | Applied | LoF variants; strength varies by variant type and NMD prediction |
| PS1 | Strong | Applied | Same amino acid change as established pathogenic variant |
| PS2 | — | Not Applicable | De novo not a mechanism for Pompe disease |
| PS3 | Strong / Moderate / Supporting | Applied | In vitro expression (<5% or <30% activity) and splicing assays |
| PS4 | — | Not Applicable | No case-control studies for Pompe disease |
| PM1 | Moderate | Applied | 16 active site residues specified |
| PM2 | Supporting only | Applied | MAF <0.1% in all continental populations in gnomAD |
| PM3 | Very Strong / Strong / Moderate / Supporting | Applied | Points-based system for in trans evidence |
| PM4 | Moderate / Supporting | Applied | ≥2 aa = Moderate; 1 aa = Supporting |
| PM5 | Moderate / Supporting | Applied | P variant at same residue = Moderate; LP = Supporting |
| PM6 | — | Not Applicable | See PS2 |
| PP1 | — | Not Applicable | Sib-ships too rare; linkage disequilibrium concern |
| PP2 | — | Not Applicable | Benign and pathogenic missense variants exist |
| PP3 | Supporting | Applied | REVEL >0.7; SpliceAI >0.5; 2/3 in-frame tools |
| PP4 | Moderate / Supporting | Applied | Points-based phenotype system |
| PP5 | — | Not Applicable | Per ClinGen SVI recommendation |
| BA1 | Stand Alone | Applied | MAF >1% in any continental population |
| BS1 | Strong | Applied | MAF >0.5% (c.-32-13T>G exempted) |
| BS2 | Strong | Applied | Homozygous with normal GAA activity |
| BS3 | Supporting | Applied | >50% activity (or >30% with normal processing) |
| BS4 | — | Not Applicable | — |
| BP1 | — | Not Applicable | All variant types cause disease |
| BP2 | Supporting | Applied | Observed in cis with pathogenic variant only |
| BP3 | — | Not Applicable | No repetitive regions without known function |
| BP4 | Supporting | Applied | REVEL <0.5; SpliceAI <0.2; all 3 in-frame tools benign |
| BP5 | — | Not Applicable | No alternate molecular basis for GAA deficiency |
| BP6 | — | Not Applicable | Per ClinGen SVI recommendation |
| BP7 | Supporting | Applied | Synonymous, no splice impact, PhyloP <0.1 |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | June 2, 2021 | PS3/BS3 strength revised and downgraded; PM2 downgraded to Supporting; PP4 revised with points system; PM3 no longer requires PP4; PM1 and BS2 specifications added; PP3/BP4 in silico tools revised |

**Document corrections (2026-08-07), source-verified against `ClinGen_ACMG_Specifications_GAA_v2.0.pdf` — the only file the GAA package distributes. No change to the underlying ClinGen specification version.**

The GAA specification is unusually thin: its PP4 criterion explicitly defers to a "main specifications document" that ClinGen does not distribute. Much of this guideline's detail has no counterpart in the shipped PDF. Content that merely goes beyond the source has been retained under explicit warnings; content that contradicts it has been removed.

- **Appendix A rewritten.** It previously presented a Tayoun-style flowchart, attributed to a PMID the specification never cites, whose frameshift/splice/deletion/duplication branches turned on ">10%" vs "<10% of normal sequence length altered". **The VCEP uses no such rule** — its test is positional (codon 916). The appendix now reproduces the three published strength tiers verbatim. Statements about duplications, full gene deletions, the intron 19 GC donor site and exon 1 being untranslated were removed as unsourced.
- **Contradicting frameshift rule removed** from the PVS1 body: it promoted PTCs 3' of c.2749 to PVS1_Strong when >10% of sequence length was altered. The specification defines **no PVS1_Strong pathway for premature termination codons** and assigns Moderate to that class unconditionally.
- **Flagged as unverifiable (retained under warning):** the PVS1 introductory prose and "Additional considerations"; the "Variant-Specific Guidance" subsection; the entire PP4 threshold table and 9-row point system; Appendix D (pseudodeficiency variants); Appendix F (GAA processing and the Kroos severity classification with its PS3/BS3 mapping). None of this appears in the distributed PDF.
- **Appendix B** — the 16 active-site residues are source-backed and retained; a per-residue "Role" column distinguishing catalytic nucleophile / acid-base, and three supporting references, were removed as unsourced.

---

*This document was compiled from ClinGen Lysosomal Storage Disorders VCEP specifications and ClinGen SVI recommendations. For the most current version, please refer to: https://www.clinicalgenome.org/affiliation/50009/docs/assertion-criteria*
