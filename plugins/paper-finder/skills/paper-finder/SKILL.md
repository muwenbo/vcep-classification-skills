---
name: paper-finder
description: "Fetch PubMed articles by PMID and extract raw verbatim content. Scrapes PubMed for metadata/abstract and PMC for full text when available. Use when asked to find, fetch, download, or get papers by PMID. Triggers on: PMIDs, find paper, get article, fetch publication, download paper."
---

# Paper Finder

Fetch scientific articles from PubMed/PMC by PMID and save raw verbatim content to local files.

## Output Directory

**IMPORTANT:** Always save papers to the project-level `papers/` directory, NOT inside the skill folder.

## Usage

```bash
# Preview metadata only (lightweight, fast)
python .claude/skills/paper-finder/scripts/paper_fetcher.py <pmid> [pmid2 ...] --metadata-only

# Fetch full content and save to project papers/ folder
python .claude/skills/paper-finder/scripts/paper_fetcher.py <pmid> [pmid2 ...] --output-dir ./papers
```

## Recommended Workflow

1. **Preview first** - Use `--metadata-only` to quickly see what's available
2. **Review output** - Check which articles have PMC full text
3. **Fetch selectively** - Run again without `--metadata-only` for chosen PMIDs

## Examples

All examples assume running from the project root directory.

```bash
# Preview metadata for multiple articles (fast)
python .claude/skills/paper-finder/scripts/paper_fetcher.py 30128536 27720647 34521996 --metadata-only

# Fetch full content for selected articles (saves to ./papers/)
python .claude/skills/paper-finder/scripts/paper_fetcher.py 30128536 --output-dir ./papers

# Multiple articles with full content
python .claude/skills/paper-finder/scripts/paper_fetcher.py 30128536 27720647 --output-dir ./papers
```

## How It Works

### Metadata-Only Mode (`--metadata-only`)
- Single request per PMID to PubMed
- Extracts: title, authors, journal, year, DOI, PMCID availability, abstract, keywords
- Fast (0.3s delay between requests)
- No file output, displays summary table

### Full Content Mode (default)
1. **Scrape PubMed HTML** (`pubmed.ncbi.nlm.nih.gov/{PMID}/`)
   - Extract: title, authors, journal, year, DOI, PMCID, raw abstract, keywords

2. **If PMCID exists, scrape PMC HTML** (`pmc.ncbi.nlm.nih.gov/articles/{PMCID}/`)
   - Extract: full text sections, tables (as markdown), figures, references

3. **Save to `PMID_{id}.md`** with all raw content

## Metadata Preview Output

```
==========================================================================================
METADATA PREVIEW
==========================================================================================

PMID         PMC    Year   Title
------------------------------------------------------------------------------------------
30128536     Yes    2018   Association of Breast and Ovarian Cancers With Predi..
27720647     No     2016   Sanger Confirmation Is Required to Achieve Optimal S..
34521996     Yes    2021   ClinGen Variant Curation Expert Panel recommenda...

------------------------------------------------------------------------------------------

DETAILED METADATA:
------------------------------------------------------------------------------------------

[PMID 30128536]
  Title:    Association of Breast and Ovarian Cancers...
  Authors:  Hu C, Hart SN, Gnanaolivu R (+12 more)
  Journal:  JAMA (2018)
  DOI:      10.1001/jama.2017.14671
  PMCID:    PMC5833579
  Keywords: BRCA1, BRCA2, breast cancer, ovarian cancer
  Abstract: IMPORTANCE: Inherited pathogenic variants in BRCA1...

==========================================================================================
Total: 3 | Found: 3 | With PMC (full text available): 2 | With abstract: 3
==========================================================================================

To fetch full content for articles with PMC:
  python .claude/skills/paper-finder/scripts/paper_fetcher.py 30128536 34521996 --output-dir ./papers
```

## Full Content Output Format

```markdown
# Article Title

**PMID:** 12345678
**PMCID:** PMC1234567 (if available)
**DOI:** 10.xxxx/xxxxx
**Authors:** Author1, Author2, et al.
**Journal:** Journal Name (Year)

---

**Keywords:** keyword1, keyword2

## Abstract

[Raw verbatim abstract text]

---

## Full Text (if PMCID exists)

### Introduction
[Raw content]

### Methods
[Raw content]

### Results
[Raw content]

### Discussion
[Raw content]

---

## Tables
[Markdown tables]

## References
[Numbered list]
```

## Full Content Summary Output

```
======================================================================
SUMMARY
======================================================================
PMID 30128536: FOUND
  Title: Association of Breast and Ovarian Cancers...
  Content: FULL TEXT
  File: ./papers/PMID_30128536.md

PMID 27720647: FOUND
  Title: Sanger Confirmation Is Required...
  Content: ABSTRACT ONLY
  File: ./papers/PMID_27720647.md

Total: 2 | Found: 2 | Full text: 1 | Abstract only: 1
======================================================================
```

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

## Key Features

- **Two-stage workflow** - Preview metadata before heavy scraping
- **Raw verbatim content** - No summarization, exact text from source
- **Handles all PMC articles** - Not limited to Open Access subset
- **Structured extraction** - Sections, tables, figures, references
- **Rate limiting** - Configurable delays (faster for metadata-only)
