---
name: paper-finder
description: "Fetch PubMed articles by PMID and extract raw verbatim content. Scrapes PubMed for metadata/abstract and PMC for full text when available. Use when asked to find, fetch, download, or get papers by PMID. Triggers on: PMIDs, find paper, get article, fetch publication, download paper."
---

# Paper Finder

Fetch scientific articles from PubMed/PMC by PMID and save raw verbatim content to local files.

## Script Directory
Scripts located in scripts/ subdirectory.
Path Resolution: SKILL_DIR = this SKILL.md's directory

## Output Directory

**IMPORTANT:** Always save papers to the project-level `papers/` directory, NOT inside the skill folder.

## Usage

```bash
# Preview metadata only (lightweight, fast)
python $SKILL_DIR/scripts/paper_fetcher.py <pmid> [pmid2 ...] --metadata-only

# Fetch full content and save to project papers/ folder
python $SKILL_DIR/scripts/paper_fetcher.py <pmid> [pmid2 ...] --output-dir ./papers
```

## Recommended Workflow

1. **Preview first** - Use `--metadata-only` to quickly see what's available
2. **Review output** - Check which articles have PMC full text
3. **Fetch selectively** - Run again without `--metadata-only` for chosen PMIDs

## Examples

```bash
# Preview metadata for multiple articles (fast)
python $SKILL_DIR/scripts/paper_fetcher.py 30128536 27720647 34521996 --metadata-only

# Fetch full content for selected articles (saves to ./papers/)
python $SKILL_DIR/scripts/paper_fetcher.py 30128536 --output-dir ./papers

# Multiple articles with full content
python $SKILL_DIR/scripts/paper_fetcher.py 30128536 27720647 --output-dir ./papers
```

## How It Works

### Metadata-Only Mode (`--metadata-only`)
- Single request per PMID to PubMed
- Extracts: title, authors, journal, year, DOI, PMCID availability, abstract, keywords
- Fast (0.3s delay between requests)
- No file output, displays summary table

### Full Content Mode (default)
1. **Scrape PubMed HTML** - Extract: title, authors, journal, year, DOI, PMCID, abstract, keywords
2. **If PMCID exists, scrape PMC HTML** - Extract: full text sections, tables (as markdown), figures, references
3. **Save to `PMID_{id}.md`** with all raw content

## Output Format Examples

Metadata preview shows a summary table with PMID, PMC availability, year, and title, followed by detailed metadata per article (authors, journal, DOI, abstract, keywords).

Full content files are saved as markdown with frontmatter (PMID, DOI, authors, journal) followed by sections: Abstract, Full Text (Introduction/Methods/Results/Discussion), Tables, and References.

## CLI Options

| Option | Short | Description |
|--------|-------|-------------|
| `--metadata-only` | `-m` | Fetch only metadata/abstract (lightweight preview) |
| `--output-dir` | `-o` | Output directory for saved papers (default: ./papers) |
| `--delay` | `-d` | Delay between requests in seconds (default: 0.3 metadata, 0.5 full) |

## Requirements

- Python 3.7+
- `requests` and `beautifulsoup4` packages

```bash
pip install requests beautifulsoup4
```
