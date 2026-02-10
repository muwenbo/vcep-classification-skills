# Example Workflow: Downloading and Generating a VCEP Guideline

This document shows how to use the vcep-spec skill to download ClinGen VCEP specification documents and process them into variant interpretation guidelines.

## Prerequisites

Ensure Python dependencies are installed:
```bash
pip install requests beautifulsoup4
```

## Invocation

### Full pipeline (download + generate):

```
/vcep-spec GN101
```

### Download only:

```
/vcep-spec GN147 --download-only
```

### Generate from existing folder:

```
/vcep-spec ./GN101-ACTC1
```

### Verify download completeness:

```
/vcep-spec GN101 --verify
```

## Expected Input Structure

After download, the folder will contain:

```
GN101-ACTC1/
├── ClinGen_ACMG_Specifications_ACTC1_v1.0.0.pdf    # Main specifications
├── PM3_SVI_recommendations.pdf                       # In trans criterion
├── PP1.pdf                                           # Segregation evidence
├── PP4_updates.pdf                                   # Phenotype specificity
├── PS2_PM6.pdf                                       # De novo criteria
├── PVS1_flowchart.pdf                                # Loss of function
├── VCEP_PS3_BS3_Functional_Evidence.xlsx             # Functional assays
└── GN101_data.json                                   # Metadata (ignored by generator)
```

## Expected Output

The skill generates a comprehensive markdown file:

```
GN101-ACTC1/
└── ACTC1_Variant_Interpretation_Guidelines_vX.X.X.md
```

## Processing Notes

1. **PDF Reading**: Claude reads PDFs directly and extracts structured information
2. **Excel Processing**: The `read_excel.py` script converts spreadsheets to markdown tables
3. **Information Synthesis**: Claude combines all sources into a unified guideline
4. **Template Compliance**: Output follows the standardized template structure

## Key Sections Generated

- Gene information table
- All 28 ACMG/AMP criteria with VCEP modifications
- Point-based scoring systems (PM3, PS2/PM6, PP1, PP4)
- Population frequency thresholds
- Functional assay specifications
- Rules for combining criteria
- Appendices and references

## Troubleshooting

### Missing Information
If certain criteria show as "Not specified", the corresponding information may be missing from the input PDFs.

### Excel Errors
Run the script manually to debug:
```bash
python scripts/read_excel.py your_file.xlsx
```

### Large Files
For very large PDFs, Claude may need multiple reads. The skill handles pagination automatically.
