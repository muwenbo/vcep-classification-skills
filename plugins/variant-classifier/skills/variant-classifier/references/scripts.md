# Script CLI Reference

All scripts are located in `$SKILL_DIR/scripts/`.

## vep_annotate.py - Variant Annotation

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

### Annotation sources and fallback

Queries Ensembl VEP REST first and falls back to the GeneBe public API
(`https://api.genebe.net/cloud/api-public/v1/`, no auth) when Ensembl errors,
times out, or returns nothing. Both sources are mapped to the same output schema;
`annotation_source` in the output records which one was used.

```bash
--source auto      # Ensembl VEP, GeneBe on failure (default)
--source ensembl   # Ensembl only, fail loudly instead of falling back
--source genebe    # force GeneBe

--assembly hg38    # default
--assembly hg19    # GRCh37 input; routed to GeneBe, results lifted over to GRCh38
```

GeneBe fallback notes:
- Output coordinates are **always GRCh38**. With `--assembly hg19` the output
  carries `input_assembly: GRCh37` and `lifted_over: true`.
- HGVS input is resolved to coordinates via GeneBe `/hgvs`; rsID input is
  resolved via NCBI dbSNP esummary (GeneBe has no rsID endpoint). Multi-allelic
  rsIDs use the first alternate allele and print a warning — prefer explicit
  coordinates or HGVS.
- **Not available:** SIFT, PolyPhen, CADD, EVE, ClinPred, BLOSUM62, LOFTEE/LoF,
  NMD, LOEUF, dosage sensitivity, UniProt, PMIDs.
- **Reduced:** SpliceAI is a max delta score only (`spliceai.max_score`, tagged
  `source: genebe`) — no DS_AG/DS_AL/DS_DG/DS_DL. Use `splice_predictor.py` when
  the components matter.
- **Extra:** `bayesdel_noaf`, `phylop100way`, `dbscsnv_ada`,
  `clinvar_review_status`, `clinvar_conditions`.
- **`external_acmg`:** GeneBe's own automated ACMG verdict (classification,
  score, criteria, per-gene breakdown). Advisory cross-check only — it is a
  generic auto-call, not a VCEP classification, and must not replace the skill's
  own criteria evaluation.

## gnomad_query.py - Population Frequencies

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

## check_vcep_spec.py - VCEP Specification Lookup

```bash
python scripts/check_vcep_spec.py <GENE> -j -o $OUTDIR/vcep_spec.json

# Examples:
python scripts/check_vcep_spec.py TP53 -j -o $OUTDIR/vcep_spec.json
python scripts/check_vcep_spec.py BRCA1 -j
python scripts/check_vcep_spec.py --list-all  # List all genes with VCEP specs
```

## splice_predictor.py - Splice Site Predictions

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

## classify_variant.py - Generate Classification Report

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

## clinvar_region_query.py - ClinVar Lookup

```bash
# Region format: chr:start-end
python scripts/clinvar_region_query.py <REGION> [-o output.csv] [--format {csv,json}]

# Examples:
python scripts/clinvar_region_query.py chr20:44621004-44621201
python scripts/clinvar_region_query.py chr17:7674200-7674400 -o clinvar.csv
python scripts/clinvar_region_query.py chr20:44621004-44621201 --format json -o clinvar.json
```

## get_uniprot_domains.py - Protein Domain Info

```bash
# IMPORTANT: Requires FULL HGVS with gene name and protein change
# Format: NM_XXXXX.X(GENE):c.XXX(p.XXX)
python scripts/get_uniprot_domains.py "<FULL_HGVS>" [--json] [-o output.json]

# Examples:
python scripts/get_uniprot_domains.py "NM_000022.4(ADA):c.872C>G(p.Ser291Trp)" --json
python scripts/get_uniprot_domains.py "NM_000545.8(HNF1A):c.745T>C(p.Ser249Pro)" --json -o $OUTDIR/domains.json

# NOTE: Gene-only queries will NOT work - must include full HGVS with protein change
```

## genome_sequence_fetcher.py - Genomic Sequences (Ensembl)

```bash
# Fetches sequences via Ensembl REST API
# Used internally for transcript/protein coordinate mapping
python scripts/genome_sequence_fetcher.py
```

## refseq_sequence_fetcher.py - RefSeq Transcript Data (UCSC)

```bash
# Fetches RefSeq transcripts and amino acid mappings via UCSC API
# Used internally by variant_region_plot.py
python scripts/refseq_sequence_fetcher.py
```

## variant_region_plot.py - Visualization

```bash
# Generate genome browser plot around a variant
# For full visualization options, use /variant-region-viz skill
python scripts/variant_region_plot.py chr17:7674220 -o $OUTDIR/plot.png
python scripts/variant_region_plot.py 3-129061736-TCCCATGCCTG-T --padding 100
```
