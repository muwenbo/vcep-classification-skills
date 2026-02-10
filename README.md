# VCEP Classification Skills

English | [中文](./README.zh.md)

A set of [Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin skills for genetic variant classification using ACMG/AMP criteria and ClinGen VCEP specifications.

## Skills Included

### variant-classifier

Classify genetic variants using ACMG/AMP criteria, enhanced with ClinGen VCEP (Variant Curation Expert Panel) gene-specific guidelines when available.

```
/variant-classifier "NM_000546.6:c.215C>G"
/variant-classifier rs1042522
/variant-classifier "chr17:7674220:C:T" --quick
```

Features:
- Automated VEP annotation, gnomAD frequency lookup, splice prediction
- Automatic VCEP specification matching for 50+ genes
- Point-based classification (Pathogenic / Likely Pathogenic / VUS / Likely Benign / Benign)
- Literature evidence extraction via PubMed/PMC integration
- HTML report generation with visualizations
- Custom notes and lab policy support (`--notes`, `--requirements`)

### vcep-spec

Download ClinGen VCEP specification documents and generate structured markdown interpretation guidelines.

```
/vcep-spec GN101                    # Download + generate guideline
/vcep-spec GN147 --download-only   # Download spec files only
/vcep-spec ./GN101-ACTC1           # Generate from existing folder
```

Features:
- Downloads PDF specs, supplementary files, and metadata from ClinGen
- Reads PDF, Excel, Word, and PowerPoint source documents
- Generates comprehensive markdown guidelines following a standardized template
- Handles multi-gene and inheritance-specific specifications

### paper-finder

Fetch PubMed articles by PMID and extract raw verbatim content.

```
/paper-finder 30128536 27720647 --metadata-only   # Quick preview
/paper-finder 30128536 -o ./papers                 # Full text
```

Features:
- Two-stage workflow: metadata preview then selective full-text fetch
- Scrapes PubMed for metadata/abstract and PMC for full text
- Structured markdown output with sections, tables, and references

## Installation

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI installed
- Python 3.7+
- Python packages: `requests`, `beautifulsoup4`

```bash
pip install requests beautifulsoup4
```

### Install via Plugin Marketplace (Recommended)

1. Add the marketplace in Claude Code:

```
/plugin marketplace add muwenbo/vcep-classification-skills
```

2. Install the plugins you need:

```
/plugin install variant-classifier@vcep-classification-skills
/plugin install vcep-spec@vcep-classification-skills
/plugin install paper-finder@vcep-classification-skills
```

3. Verify installation — the skills should appear as available slash commands:

```
/variant-classifier
/vcep-spec
/paper-finder
```

### Updating

Update the marketplace to get the latest versions:

```
/plugin marketplace update vcep-classification-skills
```

### Manual Installation (Alternative)

You can also clone and add the marketplace locally:

```bash
git clone https://github.com/muwenbo/vcep-classification-skills.git
```

```
/plugin marketplace add ./vcep-classification-skills
/plugin install variant-classifier@vcep-classification-skills
```

## Usage

Once installed, invoke skills from Claude Code using slash commands:

```
> /variant-classifier "NM_000546.6:c.215C>G"
> /vcep-spec GN101
> /paper-finder 30128536
```

For detailed usage of each skill, see the `SKILL.md` file in each plugin's `skills/` directory.

## License

MIT
