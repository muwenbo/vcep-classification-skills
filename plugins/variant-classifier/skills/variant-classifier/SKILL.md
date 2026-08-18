---
name: variant-classifier
description: "Classify genetic variants using ACMG/AMP criteria with ClinGen VCEP specifications. Use when the user wants to classify a genetic variant, interpret variant pathogenicity, apply ACMG criteria, get variant classification/interpretation, or assess pathogenicity of a mutation. Accepts HGVS notation, rsIDs, or genomic coordinates. Supports --quick mode, --notes, and --requirements options."
---

# Variant Classifier Skill

Classify genetic variants using ACMG/AMP criteria, enhanced with ClinGen VCEP (Variant Curation Expert Panel) specifications when available.

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

# For GRCh37/hg19 input coordinates (routed to GeneBe, lifted over to GRCh38):
python scripts/vep_annotate.py "<VARIANT>" --assembly hg19 --json -o $OUTDIR/vep_annotation.json
```

The script queries Ensembl VEP and automatically falls back to the GeneBe public
API if Ensembl is unavailable. Check `annotation_source` in the output
(`ensembl_vep` or `genebe`) — the GeneBe fallback returns a reduced field set:
no SIFT/PolyPhen/CADD/EVE/LOFTEE/LOEUF, no PMIDs, and SpliceAI as a max delta
score only (no DS_AG/DS_AL/DS_DG/DS_DL components). It adds BayesDel, phyloP100way,
and dbscSNV instead. If annotation came from GeneBe, run `splice_predictor.py`
for full SpliceAI components and `gnomad_query.py` for detailed frequencies.

Extract key information from the annotation:
- Gene symbol
- Consequence (missense, nonsense, frameshift, etc.)
- Amino acid change
- Population frequencies from gnomAD
- SIFT/PolyPhen predictions
- Associated PMIDs

**`external_acmg` (GeneBe fallback only):** GeneBe returns its own automated ACMG
verdict. This is advisory context for cross-checking your own work — it is a
generic auto-classification, NOT a VCEP call. Never adopt it as the
classification, and never let it substitute for evaluating criteria against the
VCEP specification in the steps below. If your final call disagrees with it, that
is expected and requires no comment in the report.

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
1. **Proceed without literature analysis** (computational evidence only -- skip full text retrieval and case-level extraction)
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

**Frequency thresholds must state their comparator.** VCEPs differ on whether a
threshold is inclusive — GALT states BA1/BS1/PM2 as `>=` / `<=`, and SLC6A8
v2.1 explicitly flipped strict to inclusive — so a variant sitting exactly on
the boundary depends on it. In `vcep_spec.json`, write the operator alongside
the value whenever the source spec is inclusive:

```json
{
  "BA1_threshold": {"threshold": 0.05, "op": ">="},
  "BS1_threshold": {"threshold": 0.01, "op": ">="},
  "PM2_threshold": {"threshold": 0.0001, "op": "<="}
}
```

A bare number (`"BA1_threshold": 0.05`) is still accepted and keeps the ACMG
default comparator — `>` for BA1/BS1, `<` for PM2. Only omit `op` when the
source spec really is strict; the applied rule is echoed in the report's
evidence column, so check it there.

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
5. **Preserve all CSS and structure** from the template -- do not rewrite styles or layout

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

## Scripts

All scripts in `scripts/` directory. For detailed CLI docs, see `references/scripts.md`.

| Script | Purpose | Key flags |
|--------|---------|-----------|
| vep_annotate.py | Ensembl VEP annotation (GeneBe fallback) | `-j`, `-o`, `--pmids-only`, `--source`, `--assembly` |
| gnomad_query.py | gnomAD population frequencies | `-o` (no `-j` flag!) |
| check_vcep_spec.py | VCEP registry lookup | `-j`, `-o`, `--list-all` |
| splice_predictor.py | SpliceAI/Pangolin predictions | `-j`, `-o`, `--spliceai-only` |
| classify_variant.py | Point-based classification | `-a`, `-j`, `-o` |
| clinvar_region_query.py | ClinVar region lookup | `-o`, `--format` |
| get_uniprot_domains.py | Protein domain info | `--json`, `-o` |
| variant_region_plot.py | Genome browser visualization | `-o`, `--padding` |

## Data Files

| File | Description |
|------|-------------|
| `data/vcep_registry.json` | ClinGen VCEP specification registry |
| `data/acmg_criteria.json` | Standard ACMG thresholds |
| `data/vcep-guidelines/*.md` | Gene-specific VCEP guidelines (user-managed) |
| `templates/classification_report.md` | Markdown report template |
| `templates/classification_report_template.html` | HTML report template with visualizations |

For ACMG criteria reference and point values, see `references/acmg-criteria.md`.
