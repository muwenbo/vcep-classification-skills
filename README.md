# VCEP Classification Skills

A set of [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skills for genetic variant classification using ACMG/AMP criteria and ClinGen VCEP specifications.

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

### Install Skills

1. Clone this repository:

```bash
git clone https://github.com/<your-username>/vcep-classification-skills.git
```

2. Copy the skills into your project's `.claude/skills/` directory:

```bash
# From your project root
mkdir -p .claude/skills
cp -r vcep-classification-skills/.claude/skills/* .claude/skills/
```

Or, to install into a specific project:

```bash
cp -r vcep-classification-skills/.claude/skills/* /path/to/your/project/.claude/skills/
```

3. Verify installation — start Claude Code in your project and the skills should appear as available slash commands:

```
/variant-classifier
/vcep-spec
/paper-finder
```

### Updating

Pull the latest changes and re-copy:

```bash
cd vcep-classification-skills
git pull
cp -r .claude/skills/* /path/to/your/project/.claude/skills/
```

## Usage

Once installed, invoke skills from Claude Code using slash commands:

```
> /variant-classifier "NM_000546.6:c.215C>G"
> /vcep-spec GN101
> /paper-finder 30128536
```

For detailed usage of each skill, see the `SKILL.md` file in each skill's directory.

## License

MIT
