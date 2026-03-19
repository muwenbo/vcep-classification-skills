---
name: vcep-spec
description: "Download ClinGen VCEP specifications and generate variant interpretation guidelines. Use when given a GN### identifier, a ClinGen specification URL, asked to download ClinGen specs, create a variant classification guideline for a gene, or prepare gene-specific rules before variant classification."
---

# ClinGen VCEP Specification Downloader & Guideline Generator

Combined skill that downloads ClinGen VCEP specification documents and generates comprehensive markdown guidelines from them.

## Argument Parsing

Detect the invocation mode from the argument:

| Argument | Mode | Behavior |
|----------|------|----------|
| `GN###` | Full pipeline | Download spec, then generate guideline |
| `GN### --download-only` | Download only | Download spec files only |
| `GN### --generate-only` | Generate only | Generate guideline from existing download folder |
| `GN### --verify` | Verify | Check download completeness |
| `./GN101-ACTC1` or `./ACTC1` | Generate from path | Auto-detect folder path, generate guideline |

**Path detection:** If the argument starts with `./`, `/`, or `~`, or contains a `/`, treat it as a folder path and run generate-only mode.

**GN ID detection:** If the argument matches `GN\d+`, treat it as a VCEP ID.

---

## Step 1: Download (skip if generate-only or folder path)

Execute the download script:

```bash
python $SKILL_DIR/scripts/download.py GN### -o <output-directory>
```

### Download Arguments

- **VCEP ID** (required): Format GN### (e.g., GN101, GN147, GN169)
- **-o, --output-dir**: Output directory path (default: `./ClinGen`)
- **--skip-pdf**: Skip downloading the main PDF specification
- **--skip-supplementary**: Skip downloading supplementary files
- **--verify**: Verify existing download completeness (no download)

### Output Structure

Files are organized into folders named `{GNid}-{GeneSymbol}`:

```
{output-dir}/
├── GN101-ACTC1/                    # Single-panel genes
│   ├── ClinGen_ACMG_Specifications_ACTC1_v1.0.0.pdf
│   ├── GN101_data.json
│   └── [supplementary files]
│
├── GN147-ACTA1-AD/                 # Multi-panel genes with inheritance suffix
│   ├── ClinGen_ACMG_Specifications_ACTA1-AD_v2.0.0.pdf
│   ├── GN147_data.json
│   └── [supplementary files]
│
└── GN055-RYR1-MalignantHyperthermia/
    ├── ClinGen_ACMG_Specifications_RYR1-MalignantHyperthermia_v1.0.0.pdf
    ├── GN055_data.json
    └── [supplementary files]
```

### Automatic Folder Naming

The script determines folder names as `{GNid}-{GeneSymbol}`:
- **Single-panel genes**: `GN101-ACTC1`, `GN188-BRCA1`
- **Multi-panel genes**: `GN147-ACTA1-AD`, `GN169-ACTA1-AR`, `GN055-RYR1-MalignantHyperthermia`

### What Gets Downloaded

1. **Main PDF specification**: Complete ACMG/AMP variant interpretation guidelines
2. **Supplementary files**: Flowcharts, tables, Excel files with functional assays
3. **Embedded images**: PNG, JPG images referenced in the specification
4. **Metadata JSON**: Specification metadata (`GN###_data.json`)

### Verification Mode

The `--verify` flag checks if an existing folder has all expected files:

- Main PDF specification (required)
- Metadata JSON file (required)
- All supplementary files (optional but recommended)
- Reports missing files, extra files, and file sizes
- Automatically falls back to old-format folder names (gene-only) if new format not found

---

## Step 2: Generate Guideline (skip if download-only or verify)

### Determine the Folder Path

- If a folder path was given directly, use it
- If a GN ID was given, look for the download folder:
  1. Try `{output-dir}/GN###-*` pattern (new format)
  2. Fall back to reading `GN###_data.json` to find the gene name
  3. Try old-format folder names (gene-only, e.g., `ACTC1/`)

### Input Requirements

The folder should contain:
- **Main specification PDF**: `ClinGen_ACMG_Specifications_*.pdf`
- **Supporting criterion PDFs**: PM3, PP1, PP4, PS2_PM6, PVS1 flowcharts, etc.
- **Functional evidence files**: Excel files with PS3/BS3 assay information (optional)

**Note:** Files ending in `_data.json` should be ignored.

### Processing Steps

1. **Read all PDF files** in the folder to extract VCEP specifications
2. **Read Excel files** using the bundled script for functional assay data:
   ```bash
   python $SKILL_DIR/scripts/read_excel.py <file.xlsx>
   ```
3. **Determine output strategy (multi-gene specifications only):**
   - **Shared rules -> Single unified file:** If all genes share the same criteria rule set with only minor gene-specific notes, generate **one** combined markdown file.
   - **Independent rules -> Separate per-gene files:** If each gene has its own distinct criteria specifications, generate a **separate** markdown file for each gene.
   - **Hybrid:** If a specification contains groups of genes that share rules within a group but differ across groups, generate one file per group.

4. **Extract and organize** the following information:
   - Gene information (symbol, HGNC ID, transcript, disease, inheritance)
   - All ACMG/AMP criteria with VCEP-specific modifications
   - Point-based scoring systems (PM3, PS2/PM6, PP1, PP4)
   - Population frequency thresholds (BA1, BS1, PM2)
   - Functional assay specifications (PS3/BS3)
   - Rules for combining criteria

5. **Generate a comprehensive markdown file** following the template structure in [template.md](template.md)

### Output Naming

- **Single unified file:** `{VCEP_Name}_Variant_Interpretation_Guidelines_v{VERSION}.md`
- **Separate per-gene files:** `{GENE}_Variant_Interpretation_Guidelines_v{VERSION}.md`

### Additional Scripts

For Word documents:
```bash
python $SKILL_DIR/scripts/read_word.py <file.docx>
```

For PowerPoint files:
```bash
python $SKILL_DIR/scripts/read_ppt.py <file.pptx>
```

---

## Examples

### Full pipeline (download + generate)
```
/vcep-spec GN101
```
Downloads to `GN101-ACTC1/`, then generates guideline markdown.

### Download only
```
/vcep-spec GN147 --download-only
```
Downloads to `GN147-ACTA1-AD/` without generating guideline.

### Generate from existing folder (by GN ID)
```
/vcep-spec GN101 --generate-only
```
Finds existing `GN101-ACTC1/` folder and generates guideline.

### Generate from folder path
```
/vcep-spec ./GN101-ACTC1
```
Auto-detects as folder path, generates guideline.

### Verify download
```
/vcep-spec GN101 --verify
```
Reports download completeness without downloading.

### Standalone script usage
```bash
python $SKILL_DIR/scripts/download.py GN101 -o .
```

---

## Finding VCEP IDs

Browse all available VCEP IDs at the [ClinGen Registry](https://cspec.genome.network/cspec/ui/svi/) or run `python $SKILL_DIR/scripts/check_vcep_spec.py --list-all`.

## Requirements

Requires Python 3 with `requests` and `beautifulsoup4`.
