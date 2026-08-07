# VCEP Classification Skills

English | [中文](./README.zh.md)

AI coding agent skills for genetic variant classification using ACMG/AMP criteria and ClinGen VCEP specifications. Compatible with any agent that supports the skill/plugin format (Claude Code, Gemini CLI, etc.).

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

- An AI coding agent with skill support ([Claude Code](https://docs.anthropic.com/en/docs/claude-code), Codex, Cursor, Gemini CLI, and others)
- Python 3.7+ and Node.js 18+ (Node is only needed for the `npx skills` installer)
- Python packages: `requests`, `beautifulsoup4`

```bash
pip install requests beautifulsoup4
```

### Recommended: `npx skills` (any agent)

Installs all three skills into whichever agents you select, using the
[open agent skills](https://github.com/vercel-labs/skills) installer:

```bash
npx skills add muwenbo/vcep-classification-skills
```

The interactive prompt lets you pick skills, target agents, and scope. To skip it:

```bash
# Preview what the repo provides
npx skills add muwenbo/vcep-classification-skills --list

# All skills, Claude Code, user-wide (~/.claude/skills), non-interactive
npx skills add muwenbo/vcep-classification-skills --skill '*' -a claude-code -g -y

# Just the classifier, into the current project (./.claude/skills)
npx skills add muwenbo/vcep-classification-skills --skill variant-classifier -a claude-code -y
```

Bundled `scripts/`, `references/`, and the VCEP guideline library under `data/`
are installed along with each `SKILL.md`.

### Alternative: Claude Code plugin marketplace

Use this if you want the skills managed as Claude Code plugins rather than
plain skill directories:

```bash
claude plugin marketplace add muwenbo/vcep-classification-skills
claude plugin install variant-classifier@vcep-classification-skills
claude plugin install vcep-spec@vcep-classification-skills
claude plugin install paper-finder@vcep-classification-skills
```

The same commands work as slash commands inside a Claude Code session
(`/plugin marketplace add …`, `/plugin install …`), or interactively via `/plugin`.

### Manual

```bash
git clone https://github.com/muwenbo/vcep-classification-skills.git
```

Each skill is self-contained under `plugins/<skill>/skills/<skill>/` with a
`SKILL.md` entry point — copy or symlink those directories into your agent's
skills directory (`~/.claude/skills/` for Claude Code, `~/.agents/skills/` for
Codex and others).

### Updating

```bash
npx skills update                                        # npx installs
claude plugin marketplace update vcep-classification-skills   # plugin installs
git pull                                                 # manual installs
```

## Usage

Just ask — each skill's description tells the agent when to load it:

```
Classify NM_000546.6:c.215C>G
Download the ClinGen spec GN101 and generate a guideline
Get me PMID 30128536
```

Agents that expose skills as slash commands accept the direct form too:

```
/variant-classifier "NM_000546.6:c.215C>G"
/vcep-spec GN101
/paper-finder 30128536
```

For detailed usage of each skill, see the `SKILL.md` file in each plugin's `skills/` directory.

## License

MIT
