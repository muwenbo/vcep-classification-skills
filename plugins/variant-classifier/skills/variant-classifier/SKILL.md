---
name: variant-classifier
description: "Classify genetic variants using ACMG/AMP criteria with ClinGen VCEP specifications."
argument-hint: <variant-notation> [--quick] [--notes "text"] [--requirements file.md]
allowed-tools: Bash, Read, Write, Glob, AskUserQuestion, Skill
---

# Variant Classifier Skill

Classify genetic variants using ACMG/AMP criteria, enhanced with ClinGen VCEP (Variant Curation Expert Panel) specifications when available.

## Triggers

Use this skill when the user wants to:
- Classify a genetic variant
- Interpret variant pathogenicity
- Apply ACMG criteria to a variant
- Get variant classification/interpretation
- Assess pathogenicity of a mutation

## Usage Examples

```
/variant-classifier "NM_000546.6:c.215C>G"
/variant-classifier rs1042522
/variant-classifier "chr17:7674220:C:T"
/variant-classifier "17-7674220-C-T" --quick
/variant-classifier "NM_000546.6:c.215C>G" --notes "Patient has family history of cancer; consider PP4"
/variant-classifier "NM_000546.6:c.215C>G" --requirements /path/to/lab_policy.md
```

## Custom Classification Input

### --notes "text"
Inline text for additional context or requirements to consider during classification:
- Patient-specific information (family history, phenotype details)
- Lab-specific policies or criteria modifications
- Instructions to weight certain evidence types
- Disease context (e.g., "Classify for Li-Fraumeni syndrome")

### --requirements file.md
Path to a markdown file containing detailed custom requirements:
- Internal lab classification policies
- Gene-specific interpretation notes not in VCEP
- Custom population frequency thresholds
- Required evidence combinations

**When provided, these custom inputs will be:**
1. Displayed at the User Verification Checkpoint (Step 4)
2. Incorporated into criteria evaluation decisions
3. Noted in the final classification report under "Additional Considerations"

## Workflow

Follow this workflow to classify a variant:

## Script Directory
Scripts located in scripts/ subdirectory.

Path Resolution:

1. SKILL_DIR = this SKILL.md's directory
2. Script path = $SKILL_DIR/scripts/main.py


### Output Directory

All intermediate and result files should be saved in a project subfolder for easy tracking:

```
{project_root}/output/<GENE>_<VARIANT_SHORT>/
```

Where `<VARIANT_SHORT>` is a filesystem-safe short identifier (e.g., `c.215C-G`, `m.10406G-A`, `rs1042522`).

Create this directory at the start of the workflow:
```bash
mkdir -p {project_root}/output/<GENE>_<VARIANT_SHORT>
```

Use `$OUTDIR` below as shorthand for this path.

### Step 1: Parse Input and Annotate Variant

Run VEP annotation to get basic variant information:

```bash
python scripts/vep_annotate.py "<VARIANT>" --json -o $OUTDIR/vep_annotation.json
```

Extract key information from the annotation:
- Gene symbol
- Consequence (missense, nonsense, frameshift, etc.)
- Amino acid change
- Population frequencies from gnomAD
- SIFT/PolyPhen predictions
- Associated PMIDs

### Step 2: Check for VCEP Specification

Check if the gene has a ClinGen VCEP specification:

```bash
python scripts/check_vcep_spec.py <GENE> --json -o $OUTDIR/vcep_spec.json
```

If a VCEP specification exists:
- Note the specification name, version, and URL
- Check if guideline file exists in `data/vcep-guidelines/`
- If guideline exists, read it for gene-specific criteria modifications

### Step 3: Retrieve Paper Metadata (if PMIDs available)

If VEP annotation returned PMIDs, get paper metadata using the paper-finder skill:

```bash
# Use paper-finder skill for metadata
/paper-finder <PMID1> <PMID2> ... --metadata-only
```

### Step 4: User Verification Checkpoint

**IMPORTANT:** Before proceeding, present findings to user with AskUserQuestion:

Present the following information:
1. Variant annotation summary (gene, consequence, protein change)
2. VCEP specification status (available/not available)
3. Paper metadata table (if PMIDs found)
4. gnomAD allele frequency
5. **Custom notes/requirements** (if --notes or --requirements provided, display them here)

If `--requirements` file was provided, read it and summarize the key requirements that will be applied.

Ask user to choose:
1. **Proceed without literature analysis** (computational evidence only — skip full text retrieval and case-level extraction)
2. **Fetch full text for specific PMIDs** (for case-level evidence extraction)
3. **Add additional PMIDs** (user provides)
4. **Add internal case data** (user provides de novo, segregation, etc.)

If user selects option 2, use paper-finder to fetch full text, then proceed to Step 5.

### Step 5: Extract Case-Level Evidence (Claude's Task)

**This step requires Claude to read and analyze literature.**

If user requested full text analysis:

1. Read the fetched papers
2. Look for evidence relevant to these criteria:
   - **PS2/PM6**: De novo observations (with/without confirmed parentage)
   - **PS4**: Case counts, case-control data
   - **PP1**: Segregation data, family pedigrees
   - **PP4**: Phenotype descriptions matching gene-disease association
   - **PM3**: Compound heterozygosity / in trans observations
   - **BS4**: Lack of segregation in affected family members
   - **BP2**: In trans with dominant pathogenic OR in cis with pathogenic
   - **BP5**: Case with alternate molecular cause

3. Document findings in structured format:
```json
{
  "de_novo_confirmed": false,
  "de_novo_assumed": false,
  "case_count": 0,
  "cosegregation": false,
  "in_trans_pathogenic": false,
  "phenotype_specific": false,
  "literature_sources": []
}
```

### Step 6: Get Splice Predictions (if relevant)

For variants near splice sites or synonymous variants:

```bash
python scripts/splice_predictor.py <CHROM> <POS> <REF> <ALT> --json -o $OUTDIR/splice_pred.json
```

### Step 7: Run Classification

Run the classifier with all available evidence:

```bash
python scripts/classify_variant.py \
  --annotation $OUTDIR/vep_annotation.json \
  --vcep-spec $OUTDIR/vcep_spec.json \
  --evidence $OUTDIR/case_evidence.json \
  --splice $OUTDIR/splice_pred.json \
  -o $OUTDIR/classification_report.md
```

### Step 8: Present Results

Present the classification report to the user:
1. Final classification (Pathogenic, Likely Pathogenic, VUS, Likely Benign, Benign)
2. Criteria met with evidence summary
3. Point totals (pathogenic vs benign)
4. Confidence level
5. Recommendations
6. **Additional Considerations** (if --notes or --requirements provided):
   - How the custom requirements influenced criteria decisions
   - Any deviations from standard ACMG/VCEP guidelines per lab policy
   - User-provided context that affected interpretation

### Step 9: Generate HTML Report (Optional)

After presenting results in Step 8, ask the user if they would like a full HTML report generated. Only proceed with this step if the user confirms.

Generate the HTML classification report **using the template file**. Do NOT write HTML from scratch.

**Procedure:**

1. **Read the template:** Read `templates/classification_report_template.html` (relative to this skill's directory at `$SKILL_DIR/variant-classifier/`)
2. **Populate the template:** Replace all `{{PLACEHOLDER}}` values with actual data from the classification. Key placeholders:
   - `{{VARIANT_HGVS}}`, `{{GENE}}`, `{{CHROMOSOME}}`, `{{POSITION}}`, `{{CONSEQUENCE}}`
   - `{{CLASSIFICATION}}`, `{{CLASSIFICATION_CLASS}}` (CSS class: pathogenic, likely-pathogenic, vus, likely-benign, benign)
   - `{{TOTAL_POINTS}}`, `{{MARKER_POSITION}}` (calculate: `((points + 10) / 22) * 100`)
   - `{{VCEP_NAME}}`, `{{VCEP_VERSION}}`, `{{TRANSCRIPT}}`, `{{DATE}}`, `{{DISEASE}}`, `{{INHERITANCE}}`
   - `{{DISCUSSION_TEXT}}`
3. **Fill dynamic sections:** Replace HTML comments like `<!-- INSERT ... -->` with actual content:
   - Gene structure SVG and exon table rows
   - Variant detail SVG
   - Sequence context display
   - Criteria assessment table rows (use `.pathogenic` or `.benign` CSS classes)
   - ClinVar context table rows
   - Literature evidence cards (use `.literature-card` class from template)
   - Recommendation list items
4. **Conditional sections:** Include/remove the PVS1 Decision Tree section based on whether PVS1 applies
5. **Preserve all CSS and structure** from the template — do not rewrite styles or layout

**Output location:** Save the populated report to `$OUTDIR/classification_report.html`

**Open in browser:**
```bash
open $OUTDIR/classification_report.html
```

## Quick Mode (--quick)

If user specifies `--quick` or computational-only mode:
- Skip literature search and case evidence
- Use only computational criteria: PVS1, PM2, PP3, BP4, BP7, BA1, BS1
- Faster classification with limited evidence

## Multiple VCEP Specifications

Some genes have multiple VCEP specifications for different inheritance patterns:
- Example: ACTA1-AD vs ACTA1-AR
- Example: RYR1-CongenitalMyopathies vs RYR1-MalignantHyperthermia

If multiple specs exist, ask user to select the appropriate one based on:
- Inheritance pattern in the patient/family
- Clinical presentation
- Disease context

## Integration with Other Skills

### paper-finder
Use for retrieving paper content when PMIDs are identified:
```
/paper-finder 12345678 23456789 --metadata-only  # Metadata preview
/paper-finder 12345678 -o papers/               # Full text
```

### vcep-spec
Use to download VCEP specification and generate guideline:
```
/vcep-spec GN###                    # Download + generate guideline
/vcep-spec GN### --download-only    # Download only
/vcep-spec ./GN101-ACTC1            # Generate from existing folder
```

### variant-region-viz
Use to visualize the variant in genomic context:
```
/variant-region-viz chr17:7674220
/variant-region-viz 3-129061736-TCCCATGCCTG-T --padding 100
```

## Available Scripts

All scripts are located in `$SKILL_DIR/variant-classifier/scripts/`.

### vep_annotate.py - Variant Annotation
```bash
python scripts/vep_annotate.py "<VARIANT>" -j -o $OUTDIR/vep_annotation.json

# Accepts: HGVS, rsID, or genomic coordinates
# Examples:
python scripts/vep_annotate.py "NM_000546.6:c.215C>G" -j -o $OUTDIR/vep.json
python scripts/vep_annotate.py rs1042522 -j -o $OUTDIR/vep.json
python scripts/vep_annotate.py "chr17:7674220:C:T" -j -o $OUTDIR/vep.json
python scripts/vep_annotate.py "17-7674220-C-T" -j -o $OUTDIR/vep.json

# Get only PMIDs from a variant:
python scripts/vep_annotate.py "NM_000546.6:c.215C>G" --pmids-only
```

### gnomad_query.py - Population Frequencies

**IMPORTANT:** This script does NOT accept `--json` or `-j` flags (unlike other scripts).
Output is always JSON when using `-o`. Without `-o`, it prints a human-readable summary.

```bash
# Single variant query (returns detailed info including in silico predictors)
# Variant ID format: CHROM-POS-REF-ALT (e.g., 17-7674220-C-T)
python scripts/gnomad_query.py variant <VARIANT_ID> [--dataset gnomad_r4] [-o output.json]

# Examples:
python scripts/gnomad_query.py variant 17-7674220-C-T
python scripts/gnomad_query.py variant 12-120994195-T-C -o $OUTDIR/gnomad.json
python scripts/gnomad_query.py variant 17-7674220-C-T --dataset gnomad_r2_1  # for GRCh37

# Gene query (all variants in a gene)
python scripts/gnomad_query.py gene <GENE_SYMBOL> [--max-af 0.001] [-o output.json]
python scripts/gnomad_query.py gene TP53 --max-af 0.01

# Region query
python scripts/gnomad_query.py region <CHR:START-STOP> [--max-af 0.001] [-o output.json]
python scripts/gnomad_query.py region 17:7674200-7674400
```

### check_vcep_spec.py - VCEP Specification Lookup
```bash
python scripts/check_vcep_spec.py <GENE> -j -o $OUTDIR/vcep_spec.json

# Examples:
python scripts/check_vcep_spec.py TP53 -j -o $OUTDIR/vcep_spec.json
python scripts/check_vcep_spec.py BRCA1 -j
python scripts/check_vcep_spec.py --list-all  # List all genes with VCEP specs
```

### splice_predictor.py - Splice Site Predictions
```bash
# Positional arguments: CHROM POS REF ALT
python scripts/splice_predictor.py <CHROM> <POS> <REF> <ALT> -j -o $OUTDIR/splice_pred.json

# Or use --variant flag with variant string
python scripts/splice_predictor.py --variant "chr17-7674220-C-T" -j -o $OUTDIR/splice_pred.json

# Examples:
python scripts/splice_predictor.py chr17 7674220 C T -j -o $OUTDIR/splice.json
python scripts/splice_predictor.py 8 140300616 T G -j
python scripts/splice_predictor.py -v "17:7674220:C:T" -j -o $OUTDIR/splice.json
python scripts/splice_predictor.py chr8 140300616 T G --spliceai-only  # Skip Pangolin
```

### classify_variant.py - Generate Classification Report
```bash
# Required: --annotation (VEP result)
# Optional: --vcep-spec, --evidence, --splice
python scripts/classify_variant.py \
  --annotation $OUTDIR/vep_annotation.json \
  --vcep-spec $OUTDIR/vcep_spec.json \
  --evidence $OUTDIR/case_evidence.json \
  --splice $OUTDIR/splice_pred.json \
  -o $OUTDIR/classification_report.md

# Minimal usage:
python scripts/classify_variant.py -a $OUTDIR/vep_annotation.json -o $OUTDIR/report.md

# JSON output instead of markdown:
python scripts/classify_variant.py -a $OUTDIR/vep.json -j -o $OUTDIR/classification.json
```

### clinvar_region_query.py - ClinVar Lookup
```bash
# Region format: chr:start-end
python scripts/clinvar_region_query.py <REGION> [-o output.csv] [--format {csv,json}]

# Examples:
python scripts/clinvar_region_query.py chr20:44621004-44621201
python scripts/clinvar_region_query.py chr17:7674200-7674400 -o clinvar.csv
python scripts/clinvar_region_query.py chr20:44621004-44621201 --format json -o clinvar.json
```

### get_uniprot_domains.py - Protein Domain Info
```bash
# IMPORTANT: Requires FULL HGVS with gene name and protein change
# Format: NM_XXXXX.X(GENE):c.XXX(p.XXX)
python scripts/get_uniprot_domains.py "<FULL_HGVS>" [--json] [-o output.json]

# Examples:
python scripts/get_uniprot_domains.py "NM_000022.4(ADA):c.872C>G(p.Ser291Trp)" --json
python scripts/get_uniprot_domains.py "NM_000545.8(HNF1A):c.745T>C(p.Ser249Pro)" --json -o $OUTDIR/domains.json

# NOTE: Gene-only queries will NOT work - must include full HGVS with protein change
```

### genome_sequence_fetcher.py - Genomic Sequences (Ensembl)
```bash
# Fetches sequences via Ensembl REST API
# Used internally for transcript/protein coordinate mapping
python scripts/genome_sequence_fetcher.py
```

### refseq_sequence_fetcher.py - RefSeq Transcript Data (UCSC)
```bash
# Fetches RefSeq transcripts and amino acid mappings via UCSC API
# Used internally by variant_region_plot.py
python scripts/refseq_sequence_fetcher.py
```

### variant_region_plot.py - Visualization
```bash
# Generate genome browser plot around a variant
# For full visualization options, use /variant-region-viz skill
python scripts/variant_region_plot.py chr17:7674220 -o $OUTDIR/plot.png
python scripts/variant_region_plot.py 3-129061736-TCCCATGCCTG-T --padding 100
```

## Data Files

| File | Description |
|------|-------------|
| `data/vcep_registry.json` | ClinGen VCEP specification registry |
| `data/acmg_criteria.json` | Standard ACMG thresholds |
| `data/vcep-guidelines/*.md` | Gene-specific VCEP guidelines (user-managed) |
| `templates/classification_report.md` | Markdown report template |
| `templates/classification_report_template.html` | HTML report template with visualizations |

## Criteria Reference

### Pathogenic Criteria

| Criterion | Strength | Evidence Source |
|-----------|----------|-----------------|
| PVS1 | Very Strong | Computational (null variant) |
| PS1 | Strong | Database (same AA change) |
| PS2 | Strong | Case (de novo confirmed) |
| PS3 | Strong | Literature (functional studies) |
| PS4 | Strong | Case (prevalence in affected) |
| PM1 | Moderate | Computational (hotspot/domain) |
| PM2 | Supporting | Computational (absent from population) |
| PM3 | Moderate | Case (in trans with pathogenic) |
| PM4 | Moderate | Computational (protein length) |
| PM5 | Moderate | Database (novel missense) |
| PM6 | Moderate | Case (de novo assumed) |
| PP1 | Supporting | Case (cosegregation) |
| PP2 | Supporting | Computational (missense constraint) |
| PP3 | Supporting | Computational (predictions) |
| PP4 | Supporting | Case (phenotype specific) |

### Benign Criteria

| Criterion | Strength | Evidence Source |
|-----------|----------|-----------------|
| BA1 | Standalone | Computational (AF > 5%) |
| BS1 | Strong | Computational (AF > expected) |
| BS2 | Strong | Case (healthy adults) |
| BS3 | Strong | Literature (functional studies) |
| BS4 | Strong | Case (no segregation) |
| BP1 | Supporting | Computational (missense in truncating gene) |
| BP2 | Supporting | Case (in trans/cis with pathogenic) |
| BP3 | Supporting | Computational (in-frame in repeat) |
| BP4 | Supporting | Computational (predictions) |
| BP5 | Supporting | Case (alternate cause) |
| BP7 | Supporting | Computational (silent, no splice) |

## Point-Based Classification

| Classification | Point Range |
|----------------|-------------|
| Pathogenic | ≥ 10 |
| Likely Pathogenic | 6-9 |
| VUS | -5 to +5 |
| Likely Benign | -6 to -9 |
| Benign | ≤ -10 or BA1 |

Points: Very Strong = 8, Strong = 4, Moderate = 2, Supporting = 1

## Example Session

```
User: /variant-classifier "NM_000546.6:c.215C>G"

Claude: Analyzing variant NM_000546.6:c.215C>G...

[Runs VEP annotation]

Variant Summary:
- Gene: TP53
- Consequence: missense_variant
- Protein Change: p.Pro72Arg (P72R)
- gnomAD AF: 0.287 (28.7%)

[Checks VCEP registry]

VCEP Status: TP53 VCEP specification available (Version 2.4.0)

[Presents options to user...]

Classification Result: **Benign**
- BA1 met: AF > 5% in gnomAD (standalone benign)
- This is a common polymorphism (rs1042522)
```
