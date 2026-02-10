# Variant Classification Report

**Generated:** {{date}}

---

## 1. Variant Summary

| Field | Value |
|-------|-------|
| **Variant** | {{variant}} |
| **Gene** | {{gene}} |
| **Transcript** | {{transcript}} |
| **HGVSc** | {{hgvsc}} |
| **HGVSp** | {{hgvsp}} |
| **Chromosome** | {{chromosome}} |
| **Position** | {{position}} |
| **Reference** | {{ref}} |
| **Alternate** | {{alt}} |
| **Consequence** | {{consequence}} |

---

## 2. VCEP Specification Status

{{#if vcep_spec}}
### VCEP Specification Applied

| Field | Value |
|-------|-------|
| **VCEP Name** | {{vcep_spec.name}} |
| **Version** | {{vcep_spec.version}} |
| **Disease** | {{vcep_spec.disease}} |
| **Inheritance** | {{vcep_spec.inheritance}} |
| **Specification URL** | [Link]({{vcep_spec.url}}) |

Gene-specific thresholds from the VCEP were applied to this classification.

{{#if vcep_guideline_exists}}
**Guideline File:** `{{vcep_guideline_path}}`
{{else}}
**Note:** VCEP guideline markdown file not found. Standard ACMG criteria were used with VCEP thresholds from the registry.
{{/if}}

{{else}}
### No VCEP Specification Available

No ClinGen VCEP specification exists for **{{gene}}**. Standard ACMG/AMP criteria were applied.

To add gene-specific guidelines, place a markdown file at:
`data/vcep-guidelines/{{gene}}_Guidelines.md`
{{/if}}

---

## 3. Final Classification

| | |
|---|---|
| **Classification** | **{{classification}}** |
| **Confidence** | {{confidence}} |
| **Pathogenic Points** | +{{pathogenic_points}} |
| **Benign Points** | -{{benign_points}} |
| **Net Score** | {{net_score}} |

### Criteria Summary

#### Pathogenic Criteria Met

| Criterion | Strength | Points | Evidence | Source |
|-----------|----------|--------|----------|--------|
{{#each pathogenic_criteria_met}}
| {{criterion}}{{#if vcep_modified}} (VCEP){{/if}} | {{strength}} | +{{points}} | {{evidence}} | {{source}} |
{{/each}}
{{#unless pathogenic_criteria_met}}
| *None* | - | - | - | - |
{{/unless}}

#### Benign Criteria Met

| Criterion | Strength | Points | Evidence | Source |
|-----------|----------|--------|----------|--------|
{{#each benign_criteria_met}}
| {{criterion}}{{#if vcep_modified}} (VCEP){{/if}} | {{strength}} | -{{points}} | {{evidence}} | {{source}} |
{{/each}}
{{#unless benign_criteria_met}}
| *None* | - | - | - | - |
{{/unless}}

---

## 4. Evidence Details

### Population Frequency

| Database | Allele Frequency | Allele Count | Note |
|----------|------------------|--------------|------|
| gnomAD v4 Global | {{gnomad_af}} | {{gnomad_ac}}/{{gnomad_an}} | {{frequency_note}} |
{{#if gnomad_max_pop}}
| gnomAD Max Population | {{gnomad_max_pop_af}} | - | {{gnomad_max_pop_name}} |
{{/if}}

**Thresholds Applied:**
- BA1: AF > {{ba1_threshold}} ({{ba1_status}})
- BS1: AF > {{bs1_threshold}} ({{bs1_status}})
- PM2: AF < {{pm2_threshold}} ({{pm2_status}})

### Computational Predictions

| Predictor | Score | Prediction | Threshold |
|-----------|-------|------------|-----------|
{{#if sift}}
| SIFT | {{sift.score}} | {{sift.prediction}} | ≤0.05 deleterious |
{{/if}}
{{#if polyphen}}
| PolyPhen-2 | {{polyphen.score}} | {{polyphen.prediction}} | ≥0.85 prob. damaging |
{{/if}}
{{#if cadd}}
| CADD PHRED | {{cadd.score}} | {{cadd.interpretation}} | ≥25 deleterious |
{{/if}}
{{#if revel}}
| REVEL | {{revel.score}} | {{revel.interpretation}} | ≥0.7 pathogenic |
{{/if}}
{{#if spliceai}}
| SpliceAI (max) | {{spliceai.max_score}} | {{spliceai.interpretation}} | ≥0.5 high impact |
{{/if}}

**Computational Consensus:** {{computational_consensus}}

### Splice Predictions

{{#if splice_predictions}}
| Tool | Score Type | Score | Position | Effect |
|------|------------|-------|----------|--------|
{{#each splice_predictions.spliceai}}
| SpliceAI | {{score_type}} | {{score}} | {{position}}bp | {{effect}} |
{{/each}}
{{#each splice_predictions.pangolin}}
| Pangolin | {{score_type}} | {{score}} | {{position}}bp | {{effect}} |
{{/each}}

**Splice Impact Assessment:** {{splice_assessment}}
{{else}}
No significant splice impact predicted.
{{/if}}

### Case-Level Evidence

{{#if case_evidence}}
| Evidence Type | Status | Details |
|---------------|--------|---------|
{{#each case_evidence}}
| {{type}} | {{status}} | {{details}} |
{{/each}}
{{else}}
No case-level evidence was provided for this classification.

**To add case evidence, provide:**
- De novo observations (PS2/PM6)
- Co-segregation data (PP1)
- Case-control studies (PS4)
- Compound heterozygosity (PM3)
- Phenotype specificity (PP4)
{{/if}}

---

## 5. Literature Sources

{{#if pmids}}
### Associated Publications

| PMID | Title | Relevance |
|------|-------|-----------|
{{#each pmids}}
| [{{this.pmid}}](https://pubmed.ncbi.nlm.nih.gov/{{this.pmid}}/) | {{this.title}} | {{this.relevance}} |
{{/each}}

**Note:** Full text analysis may be required to extract case-level evidence.
{{else}}
No PubMed IDs were associated with this variant through VEP annotation.

**To add literature evidence:**
1. Use `/paper-finder` to search for relevant publications
2. Review papers for case-level evidence
3. Document findings in case evidence file
{{/if}}

---

## 6. Visualization

{{#if visualization_path}}
![Genome Browser View]({{visualization_path}})

*Genome browser visualization showing variant position relative to gene structure.*
{{else}}
No visualization generated. To create a genome browser view:

```bash
python scripts/genome_browser_demo.py --region {{chromosome}}:{{position_start}}-{{position_end}}
```
{{/if}}

---

## 7. Recommendations

{{#if is_pathogenic}}
### Pathogenic/Likely Pathogenic Variant

- **Clinical Action:** This variant is classified as disease-causing
- **Family Screening:** Consider testing at-risk family members
- **Genetic Counseling:** Recommended for patient and family
- **Management:** Follow gene-specific clinical guidelines
{{/if}}

{{#if is_benign}}
### Benign/Likely Benign Variant

- **Clinical Action:** Variant unlikely to be disease-causing
- **Interpretation:** Should not be used for clinical decision-making
- **Note:** Consider other genetic or non-genetic causes
{{/if}}

{{#if is_vus}}
### Variant of Uncertain Significance (VUS)

- **Clinical Action:** Insufficient evidence for classification
- **Recommendations:**
  - Do not use for clinical decision-making
  - Consider periodic reclassification
  - Functional studies may help resolve classification
  - Additional case-level data collection recommended

**Evidence Gaps:**
{{#each evidence_gaps}}
- {{this}}
{{/each}}
{{/if}}

---

## Appendix: Classification Methodology

### ACMG/AMP Framework
This classification follows the ACMG/AMP standards and guidelines (Richards et al., 2015) with modifications per ClinGen Sequence Variant Interpretation recommendations.

### Point-Based System
Classification uses the point-based system (Tavtigian et al., 2020):
- **Pathogenic:** ≥10 points
- **Likely Pathogenic:** 6-9 points
- **VUS:** -5 to +5 points
- **Likely Benign:** -6 to -9 points
- **Benign:** ≤-10 points or BA1 met

### Data Sources
- **VEP:** Ensembl Variant Effect Predictor REST API
- **gnomAD:** gnomAD v4 population frequencies
- **SpliceAI/Pangolin:** Broad Institute splice prediction APIs
- **ClinVar:** NCBI ClinVar database
- **VCEP Registry:** ClinGen VCEP specification registry

---

*Report generated by variant-classifier skill*
