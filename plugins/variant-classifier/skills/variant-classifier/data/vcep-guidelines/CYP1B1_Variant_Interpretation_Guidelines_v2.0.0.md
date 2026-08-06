# Comprehensive Variant Interpretation Guidelines for CYP1B1

## ClinGen Glaucoma VCEP Specifications for CYP1B1 (Version 2.0)

**Affiliation:** Glaucoma Variant Curation Expert Panel (Glaucoma VCEP)
**Version:** 2.0
**Release Date:** July 16, 2026
**Status:** Released
**DOI:** 10.5281/zenodo.21434369
**Specification URL:** https://cspec.genome.network/cspec/ui/svi/doc/GN104
**Type:** Tavtigian et al., 2020 - Bayesian (point-based) adaptation of Richards et al., 2015 ACMG/AMP Variant Interpretation Guidelines

### Release Notes (v2.0)

Updates:
- **PP3/BP4:** Add the use of AlphaMissense for missense variants where REVEL scores are not available (e.g. due to change of more than 1 nucleotide)
- **PVS1 (RNA):** Apply PVS1 decision tree to spliceogenic variants outside of splice donor/acceptor ± 1,2 dinucleotides if in vitro analysis results in aberrant splicing profile interpretable via PVS1 decision process

---

## Table of Contents

1. [Gene and Disease Information](#1-gene-and-disease-information)
2. [Pathogenic Criteria](#2-pathogenic-criteria)
   - [PVS1 - Null Variant](#pvs1---null-variant)
   - [PS1 - Same Amino Acid Change](#ps1---same-amino-acid-change)
   - [PS2 - De Novo (PS2/PM6 Combined)](#ps2---de-novo-ps2pm6-combined)
   - [PS3 - Functional Studies](#ps3---functional-studies)
   - [PM1 - Mutational Hot Spot / Functional Domain](#pm1---mutational-hot-spot--functional-domain)
   - [PM2 - Absent from Controls](#pm2---absent-from-controls)
   - [PM3 - In Trans with Pathogenic Variant](#pm3---in-trans-with-pathogenic-variant)
   - [PM4 - Protein Length Changes](#pm4---protein-length-changes)
   - [PM5 - Novel Missense at Same Residue](#pm5---novel-missense-at-same-residue)
   - [PP1 - Co-segregation](#pp1---co-segregation)
   - [PP3 - Computational Evidence](#pp3---computational-evidence)
3. [Benign Criteria](#3-benign-criteria)
   - [BA1 - Stand-Alone Benign](#ba1---stand-alone-benign)
   - [BS1 - Allele Frequency Greater Than Expected](#bs1---allele-frequency-greater-than-expected)
   - [BS4 - Lack of Segregation](#bs4---lack-of-segregation)
   - [BP4 - Computational Evidence (Benign)](#bp4---computational-evidence-benign)
   - [BP7 - Synonymous/Intronic Variants](#bp7---synonymousintronic-variants)
4. [Not Applicable Criteria](#4-not-applicable-criteria)
5. [Rules for Combining Criteria](#5-rules-for-combining-criteria)
6. [Criterion Point Value Summary](#6-criterion-point-value-summary)
7. [Appendices](#7-appendices)

---

## 1. Gene and Disease Information

| Parameter | Value |
|-----------|-------|
| **Gene** | CYP1B1 (HGNC:2597) |
| **HGNC Name** | cytochrome P450 family 1 subfamily B member 1 |
| **Reference Transcript** | NM_000104.4 |
| **Disease** | CYP1B1-related glaucoma with or without anterior segment dysgenesis |
| **MONDO ID** | MONDO:0800472 |
| **Mode of Inheritance** | Autosomal recessive inheritance |
| **Mechanism of Disease** | Loss of Function (LoF) |

### Key Gene Characteristics

- The *CYP1B1* primary transcript (NM_000104.4) consists of 5,218 bp and encodes a 543 amino acid protein. It contains 3 exons, although only exons 2 and 3 are coding.
- *CYP1B1* variants cause the phenotype through a loss of function (LoF) disease mechanism.
- NMD is predicted to be activated for nonsense or frameshift variants where the premature termination codon is prior to amino acid 330 (last 50 bp of exon 2).
- Amino acid 489 marks the last 10% of the protein.
- CYP1B1 is an enzyme that relies on a haem group for its activity. The haem-binding domain (position aa460-493, located in exon 3) is vital for CYP1B1 enzymatic activity.
- There are no other biologically relevant transcripts of this very small gene; options related to exons being absent from biologically relevant transcript(s) are not applicable and were removed from the original PVS1 decision tree.
- Codon R348 is encoded across the exon 2/3 boundary; there are no in-frame exons, so exon skipping or use of a cryptic splice site preserving the reading frame is not applicable.

### CYP1B1-Related Diseases (Supplementary Material)

*CYP1B1*-related diseases include:

- Primary congenital glaucoma (PCG)
- Juvenile open angle glaucoma (JOAG)
- Primary open angle glaucoma (POAG)
- Anterior segment dysgenesis (ASD)

These phenotypes are part of a disease spectrum. Other terms that have been used to refer to glaucoma related to *CYP1B1* or that fall under these phenotypes include (but not limited to):

- Congenital glaucoma
- (Primary) Childhood glaucoma
- (Primary) Infantile glaucoma
- (Primary) Pediatric glaucoma
- (Primary) Early age of onset glaucoma
- (Primary) Juvenile onset glaucoma

Anterior segment dysgenesis (ASD) can include the following in the context of *CYP1B1*-related diseases:

- Axenfeld-Rieger anomaly (ARA) or Axenfeld-Rieger syndrome (ARS)
- Axenfeld anomaly or Axenfeld syndrome
- Rieger anomaly or Rieger syndrome
- Iridogoniodysgenesis
- Peters anomaly or Peters syndrome
- Aniridia or partial aniridia
- Congenital ectropion uveae
- Congenital iris hypoplasia

---

## 2. Pathogenic Criteria

### PVS1 - Null Variant

**Original ACMG Summary:** Null variant (nonsense, frameshift, canonical ±1 or 2 splice sites, initiation codon, single or multi-exon deletion) in a gene where loss of function (LOF) is a known mechanism of disease.

**VCEP Specification:** Use the *CYP1B1* decision tree for PVS1 (Figure 2) adapted from Abou Tayoun et al. (PMID: 30192042).

#### General VCEP Notes

- The haem-binding domain is considered vital for CYP1B1 enzymatic activity and the biological effect of removing the haem-binding domain is equivalent to NMD. Truncating variants that are predicted to escape NMD but remove the haem-binding domain can meet PVS1.
- Missense variants within the haem-binding domain (e.g. R469W, C470Y and S485F) and truncating variants prior to this domain have no activity, even when detectable by Western blot in an overexpression system (e.g. p.E262*). Thus, truncating variants that remove this domain are expected to be null variants. Additionally, there are a number of known pathogenic truncating variants in exon 3 (e.g. R444*, T404Sfs*30, R355Hfs*69).
- There are no LoF variants in gnomAD after the end of the haem-binding domain at residue 493; therefore the branch of the decision tree referring to variants escaping NMD in a region of unknown function with LoF variants frequent in the general population is not applicable.
- Since the haem-binding domain ends at aa493 and residue 489 marks the last 10% of the protein, the option related to a variant removing >10% of the protein is not applicable. If the variant is after the haem-binding domain, it is within the last 10% and PVS1_Moderate would apply as per the decision tree.

#### Splice Variants

- *CYP1B1* only has 2 coding exons and the splice site is after the point at which NMD could occur, but more importantly, it is upstream of the haem-binding domain. There are also no in-frame exons, with codon R348 being encoded across the exon 2/3 boundary. Therefore, exon skipping or the use of a cryptic splice site preserving the reading frame is not applicable.
- Similar to nonsense and frameshift variants, PVS1 applies to splice variants predicting to escape NMD but removing the haem-binding domain.
- **For spliceogenic variants outside of splice donor/acceptor ± 1,2 dinucleotides:** Use the PVS1 decision tree if *in vitro* analysis results in aberrant splicing profile interpretable via PVS1 decision process (as per Walker et al., PMID: 37352859). Consider design & results when assessing confidence in RNA findings. **Apply PVS1 one level of evidence down** based on considerations of construct-based assays design. **This replaces PP3.**

#### Deletions

- *CYP1B1* variation causes glaucoma through a LoF disease mechanism, supported by mice model *Cyp1b1* deficient showing developmental eye abnormalities and phenotype similar to humans. Consequently, **PVS1_stand alone (PVS1_SA)** can be applied to full gene deletions.
- *CYP1B1* has only one transcript and only 2 exons that disrupt the reading frame. There is no experimental evidence to suggest whether NMD occurs in the context of deletions in this 2 exon gene, therefore these two options have been combined. Moreover, deletion of either exon disrupts/removes the haem-binding domain because none of the exons are in frame.
- Similar to other truncating variants, PVS1 applies to deletions disrupting/removing the haem-binding domain.
- The deletion of exon 1 is harder to interpret as it is a non-coding exon in the 5'UTR. It would not be expected to alter reading frame, is in a region of unknown function for the protein, LoF variants in this exon are not common and it would alter <10% of the protein. Following these options on the original decision tree leads to PVS1_Moderate. **The VCEP recommends downgrading this to PVS1_Supporting** as the effect on the protein is not known.

#### Duplications

- Similar to other truncating variants, PVS1 applies to duplications disrupting/removing the haem-binding domain and these have been combined to deletions predicted to undergo NMD under PVS1 as they lead to the same outcome.

#### Initiation Codon

- *CYP1B1* has only 1 transcript and there are reported pathogenic variants upstream of the closest potential alternative in-frame start codon (aa132). Therefore, the option if there are no pathogenic variants upstream of the closest potential start is not applicable.
- The option for a different functional transcript that uses an alternative start codon has been listed, in case such a transcript is reported in the future.

#### Strength Levels

| Strength | Points | Applies to |
|----------|--------|------------|
| **PVS1_SA** (Stand Alone) | Stand alone for Pathogenic | Full gene deletions (per Additional Notes of the point-based categories; see also decision tree) |
| **PVS1** (Very Strong) | 8 | • Nonsense/frameshifts variants predicted to undergo NMD (aa1-330) or removing the haem-binding domain (aa331-493)<br>• GT-AG 1,2 splice sites variants leading to exon skipping or use of a cryptic splice site disrupting reading frame predicted to undergo NMD (aa1-330) or removing the haem-binding domain (aa331-493)<br>• Full gene deletions and deletions removing exon 2 and/or exon 3<br>• Duplications (≥1 exon and completely contained within the gene) disrupting the reading frame, predicted to undergo NMD (aa1-330) or removing the haem-binding domain (aa331-493), AND proven in tandem |
| **PVS1_Strong** | 4 | • Duplications (≥1 exon and completely contained within the gene) disrupting the reading frame, predicted to undergo NMD (aa1-330) or removing the haem-binding domain (aa331-493), AND presumed in tandem |
| **PVS1_Moderate** | 2 | • Nonsense/frameshifts variants NOT removing the haem-binding domain (aa494-Ter)<br>• GT-AG 1,2 splice sites variants leading to exon skipping or use of a cryptic splice site disrupting reading frame and NOT predicted to undergo NMD (aa1-330) or removing the haem-binding domain (aa331-493)<br>• Duplications (≥1 exon and completely contained within the gene) disrupting the reading frame after the haem-binding domain (aa4934-Ter)¹ AND proven in tandem<br>• Initiation codon variants when there is no known alternative start codon in other transcripts and ≥1 pathogenic variant upstream of closest potential in-frame start codon |
| **PVS1_Supporting** | 1 | • Deletions removing exon 1 only<br>• Duplications (≥1 exon and completely contained within the gene) disrupting the reading frame after the haem-binding domain (aa4934-Ter)¹ AND presumed in tandem |

¹ *Reproduced verbatim from the specification. "aa4934-Ter" appears to be a typographical error in the source document; the equivalent nonsense/frameshift row and Figure 2 use "aa494-Ter".*

**Modification Type:** PVS1 (Very Strong) = Gene-specific; PVS1_Strong / PVS1_Moderate / PVS1_Supporting = Gene-specific, Strength.

#### PVS1 Decision Tree (Figure 2)

##### Nonsense or Frameshift

| Condition | PVS1 Strength |
|-----------|---------------|
| Predicted to undergo NMD (aa1-330 NM_000104.4) | **PVS1** |
| Not predicted to undergo NMD (aa331-Ter) + Removes haem binding domain (aa1-493) | **PVS1** |
| Not predicted to undergo NMD (aa331-Ter) + Does not remove haem binding domain (aa494-Ter) | **PVS1_Moderate** |

##### GT-AG 1,2 Splice Sites

| Condition | PVS1 Strength |
|-----------|---------------|
| Exon skipping, intron inclusion or use of a cryptic splice site disrupts reading frame and is predicted to undergo NMD (aa1-330) | **PVS1** |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is **NOT** predicted to undergo NMD (aa331-Ter) + disrupts reading frame prior to haem domain (aa331-493) | **PVS1** |
| Exon skipping or use of a cryptic splice site disrupts reading frame and is **NOT** predicted to undergo NMD (aa331-Ter) + alters reading frame after haem domain (aa494-Ter) | **PVS1_Moderate** |

##### Deletion (Single Exon to Full Gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Full gene deletion | **PVS1_SA** |
| Removes exon 2 and/or exon 3 (disrupts reading frame and removes or alters haem binding domain aa460-493) | **PVS1** |
| Removes exon 1 only (no alteration to reading frame or haem binding domain) | **PVS1_supporting** |

##### Duplication (≥1 exon and completely within the gene)

| Condition | PVS1 Strength |
|-----------|---------------|
| Proven in tandem + Reading frame disrupted and NMD predicted (aa1-330) | **PVS1** |
| Proven in tandem + Reading frame in the haem domain disrupted, but no NMD predicted (aa331-493) | **PVS1** |
| Proven in tandem + Reading frame disrupted after the haem domain (aa494-Ter) | **PVS1_Moderate** |
| Presumed in tandem + Reading frame disrupted and NMD predicted (aa1-330) | **PVS1_Strong** |
| Presumed in tandem + Reading frame in the haem domain disrupted, but no NMD predicted (aa331-493) | **PVS1_Strong** |
| Presumed in tandem + Reading frame disrupted after the haem domain (aa494-Ter) | **PVS1_Supporting** |
| No impact on reading frame OR proven not in tandem | N/A |

##### Initiation Codon

| Condition | PVS1 Strength |
|-----------|---------------|
| No known alternative start codon in other transcripts and ≥1 pathogenic variant upstream of closest potential in-frame start codon | **PVS1_Moderate** |
| Different functional transcript uses alternative start codon | N/A |

**Figure 2 footnotes:** a. NMD prediction based on the premature termination codon not occurring in the 3′ most exon or the 3′-most 50 bp of the penultimate exon. b. Relevant domain indicated by experimental evidence proving a critical role of the domain and/or presence of non-truncating pathogenic variants in the region. c. The role of the region in protein function is unknown, loss-of-function variants in this exon are not frequent in the general population, and the variant removes <10% of the protein.

---

### PS1 - Same Amino Acid Change

**Original ACMG Summary:** Same amino acid change as a previously established pathogenic variant regardless of nucleotide change.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

- The combination of PP3, PM1 and PS1 should not be higher than 6 points.
- This rule does not apply to initiation codons.

| Strength | Points | Application |
|----------|--------|-------------|
| **PS1** (Strong) | 4 | For missense variants that do not affect splicing (SpliceAI ≤ 0.2): same amino acid change as a previously established **pathogenic** variant.<br>For variants that affect splicing (SpliceAI > 0.2), refer to Table 3. |
| **PS1_Moderate** | 2 | For missense variants that do not affect splicing (SpliceAI ≤ 0.2): same amino acid change as a previously established **likely pathogenic** variant.<br>For variants that affect splicing (SpliceAI > 0.2), refer to Table 3. |
| **PS1_Supporting** | 1 | For variants that affect splicing (SpliceAI > 0.2), refer to Table 3. |

**Modification Type:** Strong = Clarification; Moderate/Supporting = Clarification, Strength.

#### Table 3: PS1 Code Weights for Variants with the Same Predicted Splicing Event as a Known (Likely) Pathogenic Variant

| Variant under assessment (VUA) | Baseline computational/predictive code applicable to VUA | Position of comparison variant relative to VUA | PS1 code with P comparison variant | PS1 code with LP comparison variant |
|---|---|---|---|---|
| Located outside splice donor/acceptor ± 1,2 dinucleotide positions | PP3 | same nucleotide | PS1 | PS1_Moderate |
| Located outside splice donor/acceptor ± 1,2 dinucleotide positions | PP3 | within same splice donor/acceptor motif (including at ±1,2 positions) | PS1_Moderate | PS1_Supporting |
| Located at splice donor/acceptor ± 1,2 dinucleotide positions | PVS1 | within same splice donor/acceptor ± 1,2 dinucleotide | PS1_Supporting | N/A |
| Located at splice donor/acceptor ± 1,2 dinucleotide positions | PVS1 | within same splice donor/acceptor region, but outside ± 1,2 dinucleotideᵃ | PS1_Supporting | PS1_Supporting |
| Located at splice donor/acceptor ± 1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | within same splice donor/acceptor ± 1,2 dinucleotide | PS1 | N/A |
| Located at splice donor/acceptor ± 1,2 dinucleotide positions | PVS1_Strong, PVS1_Moderate, or PVS1_Supporting | within same splice donor/acceptor motif, but outside ± 1,2 dinucleotideᵃ | PS1_Moderate | PS1_Supporting |

**Prerequisite for all:** the predicted event of the VUA must precisely match the predicted event of the comparison (likely) pathogenic variant (e.g., both predicted to lead to exon skipping, or both to lead to enhanced use of a cryptic splice motif, AND the strength of the prediction for the VUA must be of similar or higher strength than the strength of the prediction for the comparison [likely] pathogenic variant). For an exonic variant, predicted or proven functional effect of missense substitution(s) encoded by the VUA and (likely) pathogenic variant should also be considered before application of this code. Dinucleotide positions refer to donor and acceptor dinucleotides in reference transcript(s) used for curation. Designated donor and acceptor motif ranges should be based on position weight matrices for intron category (see methods). For GT-AG introns these are defined as follows: the donor motif, last 3 bases of the exon and 6 nucleotides of intronic sequence adjacent to the exon; acceptor motif, first base of the exon and 20 nucleotides upstream from the exon boundary. Consider other motif ranges for non-GT-AG introns.

ᵃ If relevant, splicing assay data for a pathogenic variant outside a ±1,2 dinucleotide position may be used to update a PVS1 decision tree and hence the applicable PVS1 code for a ±1,2 dinucleotide variant.

---

### PS2 - De Novo (PS2/PM6 Combined)

**Original ACMG Summary:** De novo (both maternity and paternity confirmed) in a patient with the disease and no family history.

**Note:** Confirmation of paternity only is insufficient. Egg donation, surrogate motherhood, errors in embryo transfer, etc. can contribute to non-maternity.

#### VCEP Specifications

**PS2 and PM6 have been combined under PS2.** See Table 2 for point system. The proposed SVI point recommendations for "phenotype consistent with gene but not highly specific" applies to PCG and "phenotype consistent with the gene but not highly specific and with high genetic heterogeneity" applies to other *CYP1B1*-related glaucoma phenotypes (JOAG, POAG, ASD). See Supplementary Material for phenotype list.

- Paternity and/or maternity of the non-carrier parent(s) need to be proven for confirmed de novo variants.
- Both parents need to be clinically assessed and should not have a diagnosis of *CYP1B1*-related glaucoma phenotypes. If a parent has glaucoma or suspicious signs of glaucoma, the age at diagnosis and the phenotype should be considered before applying criteria due to the prevalence of JOAG/POAG in the population and the possibility of phenocopies.
- **Decrease the strength of evidence by one level for de novo occurrences without an additional P/LP variant.**

#### Table 2: Point System for PS2

| Phenotype | Confirmed de novo | Assumed de novo |
|-----------|-------------------|-----------------|
| PCG | 1 | 0.5 |
| Other *CYP1B1*-related glaucoma phenotype (JOAG, POAG, ASD) | 0.5 | 0.25 |

#### Evidence Strength Thresholds

| Total Points | Evidence Strength | Points Value |
|--------------|-------------------|--------------|
| ≥ 0.5 points | **PS2_Supporting** | 1 |
| ≥ 1.0 points | **PS2_Moderate** | 2 |
| ≥ 2.0 points | **PS2** (Strong) | 4 |
| ≥ 4.0 points | **PS2_VeryStrong** | 8 |

**Modification Type:** Very Strong = Disease-specific, Strength; Strong = Disease-specific; Moderate/Supporting = Disease-specific, Strength.

---

### PS3 - Functional Studies

**Original ACMG Summary:** Well-established in vitro or in vivo functional studies supportive of a damaging effect on the gene or gene product.

#### VCEP Specifications

The mechanism by which *CYP1B1* variants cause the associated phenotype is a LoF mechanism. Cyp1b1-deficient mice show oxidative damage to trabecular meshwork cells, leading to apoptosis and increased IOP. CYP1B1 is an enzyme involved in the metabolism of different substrates, including retinol and steroid. The underlying mechanism by which CYP1B1 variants cause glaucoma is currently unknown, however it is hypothesized that the reduction of the enzyme activity and protein abundance is linked to the potential role of CYP1B1 in the development and function of the eye. Although there is evidence connecting estrogen to glaucoma, the specific substrates implicated in the development of CYP1B1-associated glaucoma have not yet been characterised.

Animal models of specific variants (e.g. knock in mice models) have not been reported at this stage. They would need to replicate the phenotype reported in humans (e.g. increase in IOP, degeneration of the optic nerve and/or damage to trabecular meshwork cells) in order to meet PS3.

The Glaucoma VCEP followed the SVI recommendations from Brnich et al. (PMID: 31892348) when assessing functional assays. Variants classified as LB/B and LP/P without the use of functional studies (pilot phase) were used as validation controls to determine OddsPath. A limited number of LB/B variants have been assessed by published studies overall, therefore **PS3 could only be applied at a Supporting level at this stage**.

The Glaucoma VCEP decided to apply PS3 to animal models that replicate the glaucoma phenotype as well as assays that show lack of enzymatic activity (regardless of substrate) OR low protein stability if it meets the following:

- It has an appropriate number of validation controls (level of evidence to be established based on validation controls and associated OddsPath).
- The results show clear differentiation between LP/P and LB/B variants to establish threshold (or include indeterminate results in OddsPath calculation).
- The assay includes both negative and positive controls as well as technical and/or biological replicates.
- Controls from the same general class of assays and with same methodology can be combined to calculate OddsPath.
- If the results from different assays are conflicting for a single variant, then the level of validation of each assay should be considered to decide whether the results from one assay can override the results from another.
- Ideally variants should be assessed against their background haplotype.

| Strength | Points | Application |
|----------|--------|-------------|
| **PS3** (Strong) | 4 | Assays with OddsPath >18.7 as per the SVI recommendations.<br>Animal models that replicate the glaucoma phenotype. |
| **PS3_Moderate** | 2 | Assays with OddsPath >4.3 as per the SVI recommendations. |
| **PS3_Supporting** | 1 | Assays with OddsPath >2.1 as per the SVI recommendations.<br>As of 06/11/25, the following studies meet the criteria to apply PS3_supporting: Chavarria-Soley et al. 2008 (PMID: 18470941), Pasutto et al. 2010 (PMID: 19643970) and Mammen et al. 2003 (PMID: 12807732). |

**Modification Type:** Strong = Disease-specific, Gene-specific; Moderate = Disease-specific, Gene-specific, Strength; Supporting = Disease-specific, Gene-specific, Strength.

#### Approved Assays (Table 6)

| Assay class | Product measured | Vector / Cell line / Detection | References | LP/P controls | LB/B controls | OddsPath | Threshold | Recommendation |
|---|---|---|---|---|---|---|---|---|
| 17β Estradiol Activity | Luciferin derivative (CYP450-GLO kit) | pYeDP60 / INVSc1-HR (yeast) / luminescence | Chavarria-Soley 2008 (PMID: 18470941); Pasutto 2010 (PMID: 19643970) | 2 | 3 | 3 | <20% relative activity compared to background haplotype | **Use at PS3_supp** |
| Benzo[a]pyrene Activity | Oxidation products of B[a]P-7,8-diol | pYes2 / S. cerevisiae JL20 / HPLC | Mammen 2003 (PMID: 12807732) | 6 | 4 | 4 | <20% activity compared to background haplotype | **Use at PS3_supp** |

All other assay/study combinations reviewed in Table 6 (protein stability, protein abundance, other 17β estradiol assays, EROD activity, retinol/retinoid activity, arachidonic acid metabolism) were assessed as **Not suitable**, either because of insufficient OddsPath or because an appropriate threshold could not be determined (overlap between pathogenic and benign control variants).

---

### PM1 - Mutational Hot Spot / Functional Domain

**Original ACMG Summary:** Located in a mutational hot spot and/or critical and well-established functional domain (e.g. active site of an enzyme) without benign variation.

#### VCEP Specifications

- Although the crystal structure of CYP1B1 has not yet been established, cytochrome P450 proteins have known conserved regions and CYP1B1 structure can be predicted by comparative modeling. CYP proteins are characterized by a highly conserved structural core divisible into α-rich and β-rich domains comprising ~14 helices and four to six β-sheets. Their structure comprises five functional relevant regions: the haem-binding region, the meander-region, the hinge-region, residues in alpha-helices (stabilization and interaction 3D) and residues in beta-sheets.
- The Glaucoma VCEP analysed the presence of known pathogenic and benign variants in each of the characterized domains and helices and supporting functional evidence and decided to apply PM1 to the Hinge region (aa51-61) and the haem-binding domain (aa 463-472)¹ which are critical and well-established functional domains without benign variation. Moreover, the whole L-helix region (aa 460-493) was included as opposed to the smaller haem-binding domain as there are functional variants detected in the larger region and the whole region is important for protein function. The Meander region (aa 437-445) was excluded as containing benign variation. The G helix (aa 253-282) and I helix (aa 339-365) do not have benign variation. These are important for substrate binding and contain evaluated functional variants. PM1_Supporting applies to variants in these helices as they are less well defined in the context of CYP1B1 (as opposed to other CYPs).
- **Combination caps:** The combination of PP3 and PM1 should not be higher than 4 points, the combination of PP3, PM1 and PM5 should not be higher than 5 points, and the combination of PP3, PM1 and PS1 should not be higher than 6 points.

¹ *Reproduced verbatim from the specification. The coordinate range "aa 463-472" for the haem-binding domain is inconsistent with the haem-binding domain coordinates used elsewhere in this specification (aa460-493); the PM1_Moderate strength row below uses aa460-493.*

| Strength | Points | Application |
|----------|--------|-------------|
| **PM1** (Moderate) | 2 | Missense variants and in-frame indels in the hinge region (aa51-61) or the L-helix including the haem-binding domain (aa460-493). |
| **PM1_Supporting** | 1 | Missense variants and in-frame indels in the G helix (aa253-282) or the I helix (339-365). |

**Modification Type:** Moderate = Gene-specific; Supporting = Gene-specific, Strength.

---

### PM2 - Absent from Controls

**Original ACMG Summary:** Absent from controls (or at extremely low frequency if recessive) in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

**Caveat:** Population data for indels may be poorly called by next generation sequencing.

#### VCEP Specifications

- The highest allele frequency in population databases should be used.
- Only applies to populations of ≥ 2,000 alleles.
- PM2 should be used at a Supporting level as per the SVI recommendations.

The Whiffin/Ware calculator (PMID: 28518168) for autosomal recessive disorders was used to obtain a population allele frequency threshold for PM2 using the lowest prevalence reported in populations (Europeans). The prevalence of PCG in European populations is among the lowest. MacKinnon et al. previously reported a disease frequency for PCG in Australia at 1/30,000 (PMID: 14746584). Dimasi et al. identified biallelic *CYP1B1* variants in 22% of families with a maximum allelic contribution of 19% (PMID: 17718864). Based on these figures and setting the penetrance at 100%, the maximum credible allele frequency calculated was 0.000515.

| Strength | Points | Threshold |
|----------|--------|-----------|
| **PM2_Supporting** | 1 | Allele frequency **≤ 0.0005** in population databases |

**Modification Type:** Gene-specific.

---

### PM3 - In Trans with Pathogenic Variant

**Original ACMG Summary:** For recessive disorders, detected in trans with a pathogenic variant.

**Note:** This requires testing of parents (or offspring) to determine phase.

#### VCEP Specifications

See Table 1 for point system for PM3.

- The Glaucoma VCEP decided to follow the SVI recommendations with some modifications. SVI recommendations are that variants should meet PM2 to ensure that they are rare. Since some known pathogenic variants do not meet PM2, instead the Glaucoma VCEP specified that variants assessed for PM3 must not meet BS1. Variants need to meet PM4 (for in-frame indels) or PVS1 at any strength (for null variants) and must not meet BS1 or BP4.
- **Affected** is defined as a diagnosis of PCG, ASD, JOAG or POAG (see Supplementary Material for phenotype list).
- To avoid circularity, in all instances (phasing confirmed or unknown), the classification of the variant on the other allele should not use evidence from the variant being interrogated.
- The variant on the other allele must have been classified following these VCEP specifications.
- Multiple probands from different studies can be counted if they are independent. However, the number of points given to multiple compound heterozygous cases that have the same genotype has been capped to two when the variants are not confirmed *in trans* to avoid counting evidence if the variants are actually *in cis* and inherited together.
- The number of points per proband if homozygosity occurrence is due to consanguinity has been decreased to 0.25 points (max points 0.5) to account for homozygous variants being present by chance in consanguineous couples.
- Testing of one parent (or an unaffected first-degree relative carrying one of the two variants) is sufficient to confirm *in trans* for compound heterozygous cases.
- Parental testing is not required for homozygous cases.
- Individuals with multiple VUS/LP/P variants cannot be considered as evidence of either variant when the phase is unknown or for multiple variants in cis.

#### Table 1: Point System for PM3

| Classification/Zygosity of other variant | Non consanguinity | Consanguinity |
|---|---|---|
| Homozygous occurrence (max points 1.0) | 0.5 | 0.25 |

| Classification/Zygosity of other variant | Confirmed in trans | Phase unknown |
|---|---|---|
| Compound Heterozygous occurrence with Pathogenic/Likely Pathogenic | 1.0 | 0.5* |
| Compound Heterozygous occurrence with Variant of uncertain significance (max points 0.5) | 0.25 | 0.0 |

*No more than 2 cases can be counted when multiple compound heterozygous cases have the same genotype and the variants are not confirmed *in trans*.

#### Evidence Strength Thresholds

| Total Points | Evidence Strength | Points Value |
|--------------|-------------------|--------------|
| ≥ 0.5 points | **PM3_Supporting** | 1 |
| ≥ 1.0 points | **PM3** (Moderate) | 2 |
| ≥ 2.0 points | **PM3_Strong** | 4 |
| ≥ 4.0 points | **PM3_VeryStrong** | 8 |

**Modification Type:** General recommendation (with Strength modification for Very Strong, Strong and Supporting).

---

### PM4 - Protein Length Changes

**Original ACMG Summary:** Protein length changes due to in-frame deletions/insertions in a non-repeat region or stop-loss variants.

| Strength | Points | Application |
|----------|--------|-------------|
| **PM4** (Moderate) | 2 | Stop loss variants are not a known disease mechanism, therefore PM4 does not apply to that variant type. |

**Modification Type:** Gene-specific.

*Note: The specification defines PM4 only at Moderate strength and states solely that stop-loss variants are excluded; no further gene-specific restriction on in-frame deletions/insertions is given.*

---

### PM5 - Novel Missense at Same Residue

**Original ACMG Summary:** Novel missense change at an amino acid residue where a different missense change determined to be pathogenic has been seen before.

**Caveat:** Beware of changes that impact splicing rather than at the amino acid/protein level.

#### VCEP Specifications

- The novel change must not affect splicing (SpliceAI ≤ 0.2), must meet PP3 and have a Grantham score equal or greater than the previously established pathogenic or likely pathogenic variant.
- The combination of PP3, PM1 and PM5 should not be higher than 5 points.

| Strength | Points | Application |
|----------|--------|-------------|
| **PM5_Strong** | 4 | Same residue as 2 previously established pathogenic variants (in which case both variants must be assessed independently of PM5). |
| **PM5** (Moderate) | 2 | Same residue as previously established pathogenic variant (assessed independently of PM5) or 2 previously established likely pathogenic variants (in which case both variants must be assessed independently of PM5). |
| **PM5_Supporting** | 1 | Same residue as previously established likely pathogenic variant (assessed independently of PM5). |

**Modification Type:** Strong = Clarification, Strength; Moderate = Clarification; Supporting = Clarification, Strength.

---

### PM6 - De Novo (Assumed)

**Original ACMG Summary:** Assumed de novo, but without confirmation of paternity and maternity.

**Status:** **Not Applicable.** Comment: Refer to PS2 (PS2 and PM6 have been combined under PS2).

---

### PP1 - Co-segregation

**Original ACMG Summary:** Co-segregation with disease in multiple affected family members in a gene definitively known to cause the disease.

**Note:** May be used as stronger evidence with increasing segregation data.

#### VCEP Specifications

See Table 4 for number of segregations for each level of strength.

- Affected segregations are affected family members in whom compound heterozygous (in trans) or homozygous variants segregate.
- **Affected** is defined as a diagnosis of PCG, ASD, JOAG or POAG (see Supplementary Material for phenotype list). Use caution and consider phenotypes of the affected segregations, age at diagnosis and pedigree structure before applying to segregations with POAG due to the risk of phenocopy.
- Segregations from multiple families can be added.
- Unaffected family members are individuals at risk to inherit the two variants identified in the proband and are either wild-type for both variants or a heterozygous carrier for a single variant (PMID: 30311386).
- The variant in trans needs to be independently assessed and classified as VUS/LP/P.

| Strength | Points | Application |
|----------|--------|-------------|
| **PP1_Strong** | 4 | ≥ 3 affected segregations **or** 2 affected segregations AND ≥ 3 unaffected segregations **or** 1 affected segregation AND ≥ 8 unaffected segregations. |
| **PP1_Moderate** | 2 | 2 affected segregations **or** 1 affected segregation AND ≥ 5 unaffected segregations **or** ≥ 10 unaffected segregations. |
| **PP1** (Supporting) | 1 | 1 affected segregation **or** ≥ 5 unaffected segregations. |

**Modification Type:** Strong/Moderate = Clarification, Strength; Supporting = Clarification.

#### Table 4: Recommendations for Counting Segregations (General recommendations, phenocopy not an issue)

LOD-equivalent values by number of affected segregations (rows) and unaffected recessive segregations (columns):

| Affected \ Unaffected | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **0** | 0 | 0.12 | 0.25 | 0.37 | 0.5 | 0.62 | 0.75 | 0.87 | 1 | 1.12 | 1.25 |
| **1** | 0.6 | 0.73 | 0.85 | 0.98 | 1.1 | 1.23 | 1.35 | 1.48 | 1.6 | 1.73 | 1.85 |
| **2** | 1.2 | 1.33 | 1.45 | 1.58 | 1.7 | 1.83 | 1.95 | 2.08 | 2.2 | 2.33 | 2.45 |
| **3** | 1.81 | 1.93 | 2.06 | 2.18 | 2.31 | 2.43 | 2.56 | 2.68 | 2.81 | 2.93 | 3.06 |
| **4** | 2.41 | 2.53 | 2.66 | 2.78 | 2.91 | 3.03 | 3.16 | 3.28 | 3.41 | 3.53 | 3.66 |
| **5** | 3.01 | 3.14 | 3.26 | 3.39 | 3.51 | 3.63 | 3.76 | 3.88 | 4.01 | 4.13 | 4.26 |
| **6** | 3.61 | 3.74 | 3.86 | 3.99 | 4.11 | 4.24 | 4.36 | 4.49 | 4.61 | 4.74 | 4.86 |
| **7** | 4.21 | 4.34 | 4.46 | 4.59 | 4.71 | 4.84 | 4.96 | 5.09 | 5.21 | 5.34 | 5.46 |
| **8** | 4.82 | 4.94 | 5.07 | 5.19 | 5.32 | 5.44 | 5.57 | 5.69 | 5.82 | 5.94 | 6.07 |
| **9** | 5.42 | 5.54 | 5.67 | 5.79 | 5.92 | 6.04 | 6.17 | 6.29 | 6.42 | 6.54 | 6.67 |
| **10** | 6.02 | 6.15 | 6.27 | 6.4 | 6.52 | 6.65 | 6.77 | 6.9 | 7.02 | 7.15 | 7.27 |

**Colour coding in the source table:** white = PP1 not met; green = PP1 (Supporting); orange = PP1_Moderate; red/pink = PP1_Strong. The counts listed in the strength table above are the authoritative VCEP thresholds.

---

### PP3 - Computational Evidence

**Original ACMG Summary:** Multiple lines of computational evidence support a deleterious effect on the gene or gene product (conservation, evolutionary, splicing impact, etc.).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm should not be counted as an independent criterion. PP3 can be used only once in any evaluation of a variant.

#### VCEP Specifications

- The Glaucoma VCEP recommended using only one *in silico* predictor, in line with a recent study showing a lower rate of concordance when multiple software is used (PMID: 29179779). Follow the SVI recommendations (PMID: 36413997) for the REVEL thresholds calculated for the different levels of evidence.
- Apply the highest level of strength met.
- Apply AlphaMissense to missense variants where REVEL scores are not available (e.g. due to changes of >1 nucleotide). Apply at PP3_Supporting level until the VCEP can validate the use of AlphaMissense scores in a large sample size.
- The combination of PP3 and PM1 should not be higher than 4 points, the combination of PP3, PM1 and PM5 should not be higher than 5 points, and the combination of PP3, PM1 and PS1 should not be higher than 6 points.

| Strength | Points | Threshold |
|----------|--------|-----------|
| **PP3_Strong** | 4 | For missense variants: REVEL score of **≥ 0.932** |
| **PP3_Moderate** | 2 | For missense variants: REVEL score of **0.773-0.931** |
| **PP3** (Supporting) | 1 | For missense variants: **SpliceAI ≥ 0.2 OR REVEL score of 0.644-0.772**<br>For missense variants where REVEL scores are not available: **AlphaMissense ≥ 0.792** (PMID: 40084623)<br>For all other variants located outside of donor/acceptor ±1,2 dinucleotide positions, when splicing assay is not available: **SpliceAI ≥ 0.2** |

**Modification Type:** Strong/Moderate = Gene-specific, Strength; Supporting = Gene-specific.

**Note:** For spliceogenic variants outside of splice donor/acceptor ±1,2 dinucleotides with *in vitro* analysis showing an aberrant splicing profile, PVS1 (applied one level down) **replaces PP3**.

---

## 3. Benign Criteria

### BA1 - Stand-Alone Benign

**Original ACMG Summary:** Allele frequency is above 5% in Exome Sequencing Project, 1000 Genomes or Exome Aggregation Consortium.

#### VCEP Specifications

- The highest allele frequency in population databases should be used.
- Variant must be present in ≥ 5 alleles in any validated general continental population dataset of at least 2,000 observed alleles.

The Whiffin/Ware calculator (PMID: 28518168) for autosomal recessive disorders was used to obtain a population allele frequency threshold for maximum credible allele frequency using the population with the highest ever reported genetic contribution and prevalence for the disease in a small population with founder effect (Romani people in Slovakia). The prevalence of PCG in Romani people in Slovakia was reported at 1/2,210 (PMID: 2676634). A single *CYP1B1* variant was reported to account for all families in this population due to founder effect (penetrance, genetic and allelic contribution 100%) (PMID: 10227395). Based on these figures, the maximum credible allele frequency calculated was 0.0213. **However, the VCEP revised the threshold for BA1 to 0.05** based on the justification below.

It should be noted that populations with the highest incidences of PCG (India, Pakistan, Romani populations) are currently not well represented in gnomAD v4. Therefore, the allele frequency of some potential pathogenic variants in populations with high incidence remains uncertain. Based on gnomAD v4.1.0, only two variants currently in ClinVar have a highest allele frequency between 0.02 and 0.05: A443G (0.04963) and R368H (0.03079). There is currently insufficient evidence to classify R368H as either benign or pathogenic. It has multiple conflicting interpretations in ClinVar ranging from Benign to Pathogenic ((P (4); LP (2); VUS (11); B (1); LB (2)), highlighting the complexity of its role. LB/B classifications come from the fact that it has been considered too common in some populations with high occurrence of the phenotype (South Asian 0.0379, Middle Eastern 0.02343), while accounting for a minority of cases in Saudi Arabia (PMID: 29556725) and around 30-50% of cases in South Asia (PMIDs: 15475877, 16384942). Published evidence does not support an incomplete or low penetrance for this variant. Additionally, functional evidence (meeting criteria for PS3_Supporting) supports an impact of the variant on the protein, and computational evidence (PP3), cases, segregations (PP1_Strong) and de novo evidence (PS2_Supporting) support a pathogenic impact. An exclusion rule from BA1 is not appropriate as it would disregard its high frequency in some populations. Based on the fact that this variant would meet BA1 if the threshold was set at 0.02, and that the allele frequency of potential pathogenic variants in high incidence populations is not well represented in current population datasets available, the threshold for BA1 was set at 0.05 until more evidence becomes available to reassess it.

| Strength | Points | Threshold |
|----------|--------|-----------|
| **BA1** (Stand Alone) | Not Applicable | Allele frequency **≥ 0.05** in population databases |

**Modification Type:** Clarification.

---

### BS1 - Allele Frequency Greater Than Expected

**Original ACMG Summary:** Allele frequency is greater than expected for disorder.

#### VCEP Specifications

- The highest allele frequency in population databases should be used.
- The variant must be present in ≥ 5 alleles in any validated general continental population dataset of at least 2,000 observed alleles.

The Whiffin/Ware calculator for autosomal recessive disorders was used to obtain a population allele frequency threshold for BS1 using the population with the highest genetic contribution and prevalence for the disease in a well-defined population (Saudi Arabia) (PMID: 28518168). The prevalence of PCG in the Saudi Arabian population is among the highest. Abouelhoda et al. recently estimated the disease frequency for PCG in Saudi Arabia at 1/4,500 (PMID: 27884173). Alsaif et al. published on the largest PCG cohort from Saudi Arabia: biallelic *CYP1B1* variants accounted for 77% of families with a penetrance of 91% and the most common variant was p.G61E which accounted for 76% of families attributable to *CYP1B1* variants (PMID: 29556725). Based on these figures, the maximum credible allele frequency calculated was 0.01.

| Strength | Points | Threshold |
|----------|--------|-----------|
| **BS1** (Strong) | -4 | Allele frequency is **≥ 0.01 (1%)** in population databases |

**Modification Type:** Disease-specific.

---

### BS4 - Lack of Segregation

**Original ACMG Summary:** Lack of segregation in affected members of a family.

**Caveat:** The presence of phenocopies for common phenotypes (i.e. cancer, epilepsy) can mimic lack of segregation among affected individuals. Also, families may have more than one pathogenic variant contributing to an autosomal dominant disorder, further confounding an apparent lack of segregation.

| Strength | Points | Application |
|----------|--------|-------------|
| **BS4** (Strong) | -4 | Non-segregations with PCG, ASD or JOAG. Use caution and consider phenotypes of the affected segregations, age at diagnosis and pedigree structure before applying to non-segregations with JOAG or POAG. |

**Modification Type:** Clarification.

---

### BP4 - Computational Evidence (Benign)

**Original ACMG Summary:** Multiple lines of computational evidence suggest no impact on gene or gene product (conservation, evolutionary, splicing impact, etc).

**Caveat:** As many in silico algorithms use the same or very similar input for their predictions, each algorithm cannot be counted as an independent criterion. BP4 can be used only once in any evaluation of a variant.

#### VCEP Specifications

- Similar to PP3, the Glaucoma VCEP decided to follow the SVI recommendations (PMID: 36413997) to apply the REVEL thresholds calculated for the different levels of evidence and to use SpliceAI for variants located outside of donor/acceptor ±1,2 dinucleotide positions (PMID: 37352859).
- Apply the highest level of strength met.
- Apply AlphaMissense to missense variants where REVEL scores are not available (e.g. due to changes of >1 nucleotide). Apply at BP4_Supporting level until the VCEP can validate the use of AlphaMissense scores in a large sample size.

| Strength | Points | Threshold |
|----------|--------|-----------|
| **BP4_Strong** | -4 | For missense variants: **SpliceAI ≤ 0.1 AND REVEL score of ≤ 0.016** |
| **BP4_Moderate** | -2 | For missense variants: **SpliceAI ≤ 0.1 AND REVEL score of 0.017-0.183** |
| **BP4** (Supporting) | -1 | For missense variants: **SpliceAI ≤ 0.1 AND REVEL score of 0.184-0.290**<br>For missense variants where REVEL scores are not available: **AlphaMissense ≤ 0.169** (PMID: 40084623)<br>For all other variants (not meeting PVS1 or PM4) located outside of donor/acceptor ±1,2 dinucleotide positions, when splicing assay is not available: **SpliceAI ≤ 0.1** |

**Modification Type:** Strong/Moderate = Gene-specific, Strength; Supporting = Gene-specific.

---

### BP7 - Synonymous/Intronic Variants

**Original ACMG Summary:** A synonymous variant for which splicing prediction algorithms predict no impact to the splice consensus sequence nor the creation of a new splice site AND the nucleotide is not highly conserved.

| Strength | Points | Application |
|----------|--------|-------------|
| **BP7** (Supporting) | -1 | Applies to intronic/noncoding variants outside the donor/acceptor splice region (intronic variants at or beyond positions +7/-21) and synonymous (silent) exonic variants located outside of the first and the last 3 bases of the exon **if BP4 is met**. |

**Modification Type:** Clarification.

---

## 4. Not Applicable Criteria

The following ACMG/AMP criteria are **NOT APPLICABLE** for *CYP1B1* variant interpretation:

| Criterion | Original Purpose | Reason Given by VCEP |
|-----------|-----------------|----------------------|
| **PS4** | Prevalence in affected individuals | *CYP1B1* variants cause autosomal recessive disorders associated with glaucoma. The number of probands with the variant will be addressed by PM3. |
| **PM6** | Assumed de novo | Refer to PS2 (PS2 and PM6 combined under PS2). |
| **PP2** | Low rate of benign missense | Although pathogenic missense variants are common in CYP1B1, the gene also has a significant amount of benign missense variants as shown by the missense constraint z score in gnomAD (z = -0.75) supporting tolerance to variation. |
| **PP4** | Phenotype specificity | The phenotype associated with CYP1B1 variants is not highly specific and there is genetic heterogeneity. |
| **PP5** | Reputable source reports pathogenic | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |
| **BS2** | Observed in healthy adult | CYP1B1 variants can have an incomplete penetrance and late age of onset. Adults with known pathogenic homozygous CYP1B1 variants who had a normal eye examination have been reported. |
| **BS3** | Functional studies (no damaging effect) | Given that normal protein abundance and stability does not rule out impact on enzymatic activity, and that normal enzymatic activity for one substrate is not indicative of other substrates, the Glaucoma VCEP decided to not apply BS3. |
| **BP1** | Missense in truncating disease gene | Both truncating and missense CYP1B1 variants are causative. |
| **BP2** | In trans with pathogenic (dominant) / in cis | Two missense variants in cis could act synergistically or the effect of a variant occurring after a truncating variant may not be predicted. |
| **BP3** | In-frame indel in repetitive region | CYP1B1 does not have a repetitive region without a known function. |
| **BP5** | Alternate molecular basis for disease | Multiple molecular diagnoses are possible and variants in different genes could have an additive effect. |
| **BP6** | Reputable source reports benign | This criterion is not for use as recommended by the ClinGen Sequence Variant Interpretation VCEP Review Committee (PMID: 29543229). |

---

## 5. Rules for Combining Criteria

This specification uses the **Tavtigian et al., 2020 Bayesian point-based** classification system. Criteria are converted to points (see [Section 6](#6-criterion-point-value-summary)) and summed.

### Point-Based Variant Classification Categories

| Category | Point Ranges |
|----------|--------------|
| **Pathogenic** | 10 |
| **Likely Pathogenic** | 6 - 9 |
| **Uncertain Significance** | -1 - 5 |
| **Likely Benign** | -6 - -2 |
| **Benign** | -7 |

**Additional Notes:** PVS1_SA is stand alone for Pathogenic.

*Note: The Pathogenic ("10") and Benign ("-7") categories are given as single values in the source specification; per the Tavtigian point framework these are the lower/upper bounds of open-ended ranges (i.e. ≥10 and ≤-7 respectively).*

### Combination Caps (Gene-Specific)

| Combination | Maximum Total Points |
|-------------|----------------------|
| PP3 + PM1 | 4 points |
| PP3 + PM1 + PM5 | 5 points |
| PP3 + PM1 + PS1 | 6 points |

---

## 6. Criterion Point Value Summary

| Criterion | Very Strong | Strong | Moderate | Supporting |
|-----------|-------------|--------|----------|------------|
| **PVS1** | 8 | 4 | 2 | 1 |
| **PS1** | — | 4 | 2 | 1 |
| **PS2** | 8 | 4 | 2 | 1 |
| **PS3** | — | 4 | 2 | 1 |
| **PS4** | Not applicable | | | |
| **PM1** | — | — | 2 | 1 |
| **PM2** | — | — | — | 1 |
| **PM3** | 8 | 4 | 2 | 1 |
| **PM4** | — | — | 2 | — |
| **PM5** | — | 4 | 2 | 1 |
| **PM6** | Not applicable (see PS2) | | | |
| **PP1** | — | 4 | 2 | 1 |
| **PP2** | Not applicable | | | |
| **PP3** | — | 4 | 2 | 1 |
| **PP4** | Not applicable | | | |
| **PP5** | Not applicable | | | |
| **BA1** | Stand Alone (points Not Applicable) | | | |
| **BS1** | — | -4 | — | — |
| **BS2** | Not applicable | | | |
| **BS3** | Not applicable | | | |
| **BS4** | — | -4 | — | — |
| **BP1, BP2, BP3, BP5, BP6** | Not applicable | | | |
| **BP4** | — | -4 | -2 | -1 |
| **BP7** | — | — | — | -1 |

---

## 7. Appendices

### Appendix A: Population Frequency Thresholds Summary

| Criterion | Threshold | Strength | Additional Requirement |
|-----------|-----------|----------|------------------------|
| **BA1** | ≥ 0.05 | Stand Alone | ≥ 5 alleles in a validated general continental population dataset of ≥ 2,000 observed alleles |
| **BS1** | ≥ 0.01 | Strong | ≥ 5 alleles in a validated general continental population dataset of ≥ 2,000 observed alleles |
| **PM2** | ≤ 0.0005 | Supporting | Only applies to populations of ≥ 2,000 alleles |

Use the highest allele frequency in population databases for all three criteria.

### Appendix B: Computational Thresholds Summary

| Tool | PP3_Strong | PP3_Moderate | PP3_Supporting | BP4_Supporting | BP4_Moderate | BP4_Strong |
|------|-----------|--------------|----------------|----------------|--------------|------------|
| **REVEL** (missense) | ≥ 0.932 | 0.773-0.931 | 0.644-0.772 | 0.184-0.290 | 0.017-0.183 | ≤ 0.016 |
| **AlphaMissense** (missense, REVEL unavailable) | — | — | ≥ 0.792 | ≤ 0.169 | — | — |
| **SpliceAI** (missense) | — | — | ≥ 0.2 | ≤ 0.1 (AND REVEL in range) | ≤ 0.1 (AND REVEL in range) | ≤ 0.1 (AND REVEL in range) |
| **SpliceAI** (all other variants outside donor/acceptor ±1,2, no splicing assay) | — | — | ≥ 0.2 | ≤ 0.1 | — | — |

### Appendix C: Key References

| Citation | PMID | Topic |
|----------|------|-------|
| Jansson I, Stoilov I et al., Pharmacogenetics 2001 | 11740343 | Effect of G61E and R469W on stability and endogenous steroid substrate metabolism |
| Abou Tayoun AN, Pesaran T et al., Hum Mutat 2018 | 30192042 | SVI recommendations for the LoF PVS1 criterion |
| Medina-Trillo C, Ferre-Fernández JJ et al., Acta Ophthalmol 2016 | 27060699 | Functional characterization of eight rare missense CYP1B1 variants |
| Teixeira LB, Zhao Y et al., Vet Pathol 2015 | 24879660 | Ultrastructural abnormalities of trabecular meshwork ECM in Cyp1b1-deficient mice |
| Walker LC, Hoya M et al., Am J Hum Genet 2023 | 37352859 | SVI Splicing Subgroup recommendations |
| Campos-Mollo E, López-Garrido MP et al., Mol Vis 2009 | 19234632 | CYP1B1 mutations in Spanish PCG patients |
| Ghosh R, Oak N et al., Genome Biol 2017 | 29179779 | Evaluation of in silico algorithms for ACMG/AMP guidelines |
| Pejaver V, Byrne AB et al., Am J Hum Genet 2022 | 36413997 | Calibration of computational tools; SVI PP3/BP4 recommendations |
| Bergquist T, Stenton SL et al., Genet Med 2025 | 40084623 | Calibration of additional computational tools (incl. AlphaMissense) |
| Choudhary D, Jansson I et al., Drug Metab Dispos 2004 | 15258110 | Metabolism of retinoids and arachidonic acid by CYP1B1 |
| Vasiliou V, Gonzalez FJ, Annu Rev Pharmacol Toxicol 2008 | 17914928 | Role of CYP1B1 in glaucoma |
| Zhao Y, Wang S et al., Mol Cell Biol 2013 | 23979599 | Cyp1b1 mediates periostin regulation of trabecular meshwork development |
| Brnich SE, Abou Tayoun AN et al., Genome Med 2019 | 31892348 | SVI recommendations for PS3/BS3 functional evidence |
| Whiffin N, Minikel E et al., Genet Med 2017 | 28518168 | High-resolution variant frequencies (Whiffin/Ware calculator) |
| Dimasi DP, Hewitt AW et al., Clin Genet 2007 | 17718864 | Prevalence of CYP1B1 mutations in Australian PCG patients |
| MacKinnon JR, Giubilato A et al., Clin Exp Ophthalmol 2004 | 14746584 | Primary infantile glaucoma in an Australian population |
| Oza AM, DiStefano MT et al., Hum Mutat 2018 | 30311386 | Expert specification of ACMG/AMP guidelines (segregation) |
| Alsaif HS, Khan AO et al., Hum Genet 2019 | 29556725 | Congenital glaucoma and CYP1B1: an old story revisited |
| Reddy AB, Kaur K et al., Mol Vis 2004 | 15475877 | CYP1B1 mutation spectrum in Indian PCG patients |
| Chakrabarti S, Kaur K et al., Invest Ophthalmol Vis Sci 2006 | 16384942 | Global structuring of CYP1B1 mutations in PCG |
| Plásilová M, Stoilov I et al., J Med Genet 1999 | 10227395 | Single ancestral CYP1B1 mutation in Slovak Gypsies (Roms) with PCG |
| Genčík A, Dev Ophthalmol 1989 | 2676634 | Epidemiology and genetics of PCG in Slovakia |
| Abouelhoda M, Faquih T et al., Genome Biol 2016 | 27884173 | Revisiting the morbid genome of Mendelian disorders |
| Chavarria-Soley G et al. 2008 | 18470941 | Functional assay meeting PS3_Supporting (17β estradiol, yeast) |
| Pasutto F et al. 2010 | 19643970 | Functional assay meeting PS3_Supporting (17β estradiol, yeast) |
| Mammen SE et al. 2003 | 12807732 | Functional assay meeting PS3_Supporting (benzo[a]pyrene, yeast) |
| ClinGen SVI VCEP Review Committee | 29543229 | PP5/BP6 not for use |

### Appendix D: Supplementary Files Accompanying the Specification

| File | Content |
|------|---------|
| Figure 1 | Schematic diagram of CYP1B1 (3 exons; haem-binding domain aa460-493 in red; aa330 = NMD activation site; aa489 = last 10% of protein) |
| Figure 2 | PVS1 decision tree |
| Table 1 | Point system for PM3 |
| Table 2 | Point system for PS2 |
| Table 3 | PS1 code weights for variants with the same predicted splicing event as a known (likely) pathogenic variant |
| Table 4 | Recommendations for counting segregations |
| Table 5 | Assay characteristics (per-study functional assay detail) |
| Table 6 | Combined assays, validation controls, OddsPath and recommendations |
| Table 7 | Classification of variants with functional evidence (validation control variants) |
| CYP1B1 Pilot list | List of variants, criteria applied and evidence summaries for CYP1B1 variants in the pilot list |
| Supplementary Material | CYP1B1-related diseases (phenotype list) |

### Appendix E: Functional Evidence Validation Controls (Table 7)

Classification of control variants derived without the use of functional evidence:

| Variant | Rules Applied | Points | Classification |
|---------|---------------|--------|----------------|
| c.74T>G (Leu24Arg) | PM2_Supporting, PM3_Supporting | 2.0 | VUS |
| c.83C>G (Ser28Trp) | PM2_Supporting | 1.0 | VUS |
| c.142C>G (Arg48Gly) | BA1, BP4_Moderate | | B |
| c.155C>T (Pro52Leu) | PM1, PP3_Moderate | 4.0 | VUS |
| c.171G>T/G>C (Trp57Cys) | PM2_Supporting, PP3, PM1, PM3_Supporting | 5.0 | VUS |
| c.182G>A (Gly61Glu) | PP3_Moderate, PM1, PP1_Strong, PM3_VeryStrong | 16.0 | P |
| c.241T>A (Tyr81Asn) | BS1, PP3_Moderate | -2.0 | LB |
| c.266T>C (Leu89Pro) | PM2_Supporting, PP3_Moderate, PM3_Supporting | 4.0 | VUS |
| c.317C>A (Ala106Asp) | PM3_VeryStrong, PP1_Moderate, PP3_Moderate, PM2_Supporting | 13.0 | P |
| c.349C>T (Arg117Trp) | PP1_Strong, PM3, PP3, PM2_Supporting, PM5_Supporting | 9.0 | LP |
| c.350G>C (Arg117Pro) | PM3, PP3, PM2_Supporting, PM5 | 6.0 | LP |
| c.355G>T (Ala119Ser) | BA1, BP4_Moderate | | B |
| c.367T>C (Phe123Leu) | PM2_Supporting | 1.0 | VUS |
| c.395T>G (Met132Arg) | PM2_Supporting, PP1, PM3_Supporting | 3.0 | VUS |
| c.431A>G (Gln144Arg) | PM2_Supporting | 1.0 | VUS |
| c.432G>T (Gln144His) | PM2_Supporting | 1.0 | VUS |
| c.433C>T (Arg145Trp) | PM2_Supporting, PP3_Moderate | 3.0 | VUS |
| c.434_443del (Arg145ProfsTer4) | PM2_Supporting, PVS1, PM3, PP1_Moderate | 13.0 | P |
| c.503G>A (Gly168Asp) | PM2_Supporting | 1.0 | VUS |
| c.517G>T (Glu173Ter) | PM2_Supporting, PVS1, PM3_Strong | 13.0 | P |
| c.565G>C (Ala189Pro) | PM2_Supporting | 1.0 | VUS |
| c.570C>A (Phe190Leu) | PM2_Supporting | 1.0 | VUS |
| c.608A>G (Asn203Ser) | PM2_Supporting, PP3_Moderate | 3.0 | VUS |
| c.685G>A (Glu229Lys) | BA1 | | B |
| c.710C>A (Ala237Glu) | PM2_Supporting, PP3, PM3_Strong | 6.0 | LP |
| c.783C>A (Phe261Leu) | PM2_Supporting, PM1_Supporting, PM3 | 4.0 | VUS |
| c.784G>T (Glu262Ter) | PVS1, PM2_Supporting, PM3_Supporting | 10.0 | P |
| c.835C>G (His279Asp) | PM2_Supporting, PP3_Moderate, PM1_Supporting | 4.0 | VUS |
| c.872A>G (Asp291Gly) | PM2_Supporting, PP3_Moderate | 3.0 | VUS |
| c.875T>A (Met292Lys) | PM2_Supporting, PP3 | 2.0 | VUS |
| c.985G>A (Gly329Ser) | PM3, PP3, PM2_Supporting | 4.0 | VUS |
| c.986G>T (Gly329Val) | PM2_Supporting, PP3, PM3 | 4.0 | VUS |
| c.986G>A (Gly329Asp) | PM2_Supporting, PP3 | 2.0 | VUS |
| c.988G>T (Ala330Ser) | PM2_Supporting, PP3_Moderate | 3.0 | VUS |
| c.988_989delinsTT (Ala330Phe) | PM2_Supporting, PM3_Strong | 5.0 | VUS |
| c.1033_1035del (Leu345del) | PM3_Strong, PM4, PM1_Supporting, PM2_Supporting | 8.0 | LP |
| c.1064_1076del (Arg355Hisfs*69) | PVS1, PM3_VeryStrong, PP1_Strong, PM2_Supporting | 21.0 | P |
| c.1093G>T (Gly365Trp) | PM2_Supporting, PP3_Moderate, PM1_Supporting, PM3_Supporting, PP1, PS2_Moderate | 8.0 | LP |
| c.1103G>A (Arg368His) | BS1, PP1_Strong, PP3, PS2_Supporting | 2.0 | VUS |
| c.1120G>A (Asp374Asn) | PP3, PP1_Strong, PM3, PM2_Supporting | 8.0 | LP |
| c.1159G>A (Glu387Lys) | PM2_Supporting, PP3_Strong, PP1_Strong, PM3_VeryStrong | 17.0 | P |
| c.1168C>A (Arg390Ser) | PM2_Supporting, PP3_Strong, PM5, PP1_Strong, PM3_VeryStrong | 18.0 | P |
| c.1198C>T (Pro400Ser) | PM3, PP1_Moderate, PP3, PM2_Supporting | 6.0 | LP |
| c.1225G>T (Val409Phe) | PM2_Supporting | 1.0 | VUS |
| c.1294C>G (Leu432Val) | BA1 | | B |
| c.1310C>T (Pro437Leu) | PM3_VeryStrong, PP1_Strong, PP3_Moderate, PM2_Supporting | 15.0 | P |
| c.1328G>C (Ala443Gly) | BA1, BP4 | | B |
| c.1331G>A (Arg444Gln) | PM3_VeryStrong, PP1_Strong, PP3_Moderate, PM2_Supporting | 15.0 | P |
| c.1334T>G (Phe445Cys) | PM2_Supporting, PP3_Moderate | 3.0 | VUS |
| c.1358A>G (Asn453Ser) | BA1, BP4 | | B |
| c.1394T>C (Val465Ala) | PM2_Supporting, BP4_Moderate, PM1 | 1.0 | VUS |
| c.1405C>T (Arg469Trp) | PM3_VeryStrong, PP1_Strong, PM1, PP3 | 15.0 | P |
| c.1409G>A (Cys470Tyr) | PM2_Supporting, PP3_Strong, PM1, PM3_Supporting | 6.0 | LP |
| c.1454C>T (Ser485Phe) | PM1, PM3_Strong, PP1_Moderate, PP3_Moderate, PM2_Supporting | 11.0 | P |
| c.1568G>C (Arg523Thr) | PP1_Strong, PP3_Strong, PM3_Supporting, PM2_Supporting | 10.0 | P |
| c.1589A>G (Asp530Gly) | PM2_Supporting | 1.0 | VUS |

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | July 16, 2026 | PP3/BP4: added AlphaMissense for missense variants where REVEL scores are not available (e.g. due to change of more than 1 nucleotide). PVS1 (RNA): apply PVS1 decision tree to spliceogenic variants outside of splice donor/acceptor ± 1,2 dinucleotides if in vitro analysis results in aberrant splicing profile interpretable via PVS1 decision process. |

---

*This document is based on the ClinGen Glaucoma Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines for CYP1B1 Version 2.0 (https://cspec.genome.network/cspec/ui/svi/doc/GN104; DOI 10.5281/zenodo.21434369).*
