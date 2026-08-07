# Handoff — remediation of the 69 unremediated VCEP guidelines

**Written:** 2026-08-07, revised 2026-08-07 after two further rounds
**Branch:** `vcep-registry-refresh-2026-08` (branched from `main`, **not merged**)
**Head at writing:** `4c91f2c`

This picks up where the 2026-08-06 session's handoff left off. That document's
"decide remediation scope for the ~84 unaudited guidelines" is still the open
question; what changed is that we now know **how not to do it**, and roughly
what it costs to do it properly.

**Revision note (round 2 and 3).** Two batches have been completed since this
document was first written, and both changed what it says. The three "ranges"
suspects turned out to be almost entirely false positives (§1), and the
zero-supplement premise turned out to be too broad (§2a). One genuinely
predictive signal did emerge, and it is greppable — see **§2a**. Read §1, §2a
and §7 before planning any further work; the rest of the document stands.

---

## 1. The headline: the cheap signature does not work

The prior handoff proposed grepping the corpus for a phantom PS2/PM6 point
system (the `2/1/0.5/0.25` matrix plus a `0.5/1/2/4` strength ladder) to size
the problem before committing to per-spec work. **That approach was tried and
it failed.** Do not repeat it.

The refined grep — files containing both `#### PS2/PM6 Point System` and
`#### Evidence Strength Thresholds` — matched 34 files. Eight of those were
then regenerated directly from source. In **every** case where the spec ships
`PS2_PM6.pdf`, the table is **genuine**: that PDF is ClinGen SVI's de novo
Recommendation v1.1, distributed by the VCEPs themselves, and it really does
contain both tables. Confirmed source-backed for RMRP, F9, IL7R, DCLRE1C,
FOXN1, JAK3, RAG1 and IL2RG.

The signature was detecting a **shipping manifest, not a fabrication.**

One narrower variant of it appeared to survive. Where the "Evidence Strength
Thresholds" block prints *ranges or operators* rather than four bare values,
that looked like interpolation — F9's `≥4 / 2-3.5 / 1-1.5 / 0.5` does not exist
in its source, which gives four exact values and is silent on intermediate
totals. Seven files had that shape; four were remediated, and the last three
were checked in round 2.

**That variant is now dead too.** Two of the three remaining suspects were
false positives, for exactly the reason the parent signature failed — the
ranges are printed verbatim in the specifications:

- **FBN1 (GN022)** — source reads "Strong: **two-three points**". The local
  `2.0-3.0` was faithful transcription.
- **GUCY2D (GN167)** — the spec's own PS2 rows state "Total of 2.00 - 3.75
  points required for Strong level", and likewise for the other three bands.
  Its PM3 ranges are separately source-backed the same way.
- **SERPINC1 (GN084)** — a real hit, but trivial: the source says "Required 4
  points / 2 points / 1 point / 0.5 point" with no operator, and the local file
  had invented `≥`. Now recorded as unstated per §10.

So F9 remains the only substantive instance. **Do not build another signature
out of table shape.** Both attempts failed the same way: VCEPs copy shared
ClinGen SVI material verbatim, so shape tells you about the template, not about
whether this document transcribed it honestly. Only source comparison works.

---

## 2. Scope: 69 specs remain

122 unique spec IDs; 53 covered so far (6 audited, 14 major bumps, 8 new specs,
13 minor bumps, BRCA2, the 3 range-suspects of round 2, and the 8
zero-supplement specs of round 3). **69 remain.** Full list: run the snippet
in §6.

Grouped by VCEP, because panels share source conventions and defects tend to
repeat within a panel:

| n | VCEP |
|---|---|
| 16 | RASopathy |
| 7 | Cardiomyopathy |
| 7 | Congenital Myopathies |
| 7 | Limb Girdle Muscular Dystrophy |
| 5 | Epilepsy Sodium Channel |
| 4 | Platelet Disorders |
| 3 | Monogenic Diabetes |
| 3 | Leber Congenital Amaurosis / early-onset Retinal Dystrophy |
| 2 each | Lysosomal, Mitochondrial, HBOP Cancer, Cerebral Creatine, von Willebrand, X-linked Retinal, Hereditary Hemorrhagic Telangiectasia |
| 1 each | 13 further panels |

**Batch by panel, not alphabetically.** The 2026-08-07 run put nine sibling
SCID specs in flight together and they corroborated each other — the same
PS3 sentence was independently traced across four of them, which is what
turned a vague suspicion into a precise upstream query. The RASopathy group
(16) is the single biggest win available.

---

## 2a. The one signal that does predict fabrication

Round 3 audited all specs ClinGen distributes with **no supplementary files**,
on the theory that any appendix in them is unverifiable on its face. **That
theory is too broad: five of eight were clean.** RYR1's PM1 domain boundaries,
PDHA1's four residue lists, POLG's cis variants and disorder spectrum, ETHE1's
clinical features and mtDNA's cybrid/single-fibre assay descriptions are all
verbatim in their sources. A thin spec is not a fabricated guideline.

Brain Malformations (AKT3, GN018) is the **model to copy**: it cites
"Supplementary Document 1" and "Supplementary Table 3" — references that
genuinely appear in its own source text — and where the content is unavailable
it writes *"See Supplementary Document"* in the cell instead of inventing a
table. Its PS4 thresholds are exact. That is what a correct guideline looks
like when the package is incomplete.

The signal that actually works is narrower, and came out of FBN1 in round 2:

> **An appendix that claims supplemental provenance in a spec that ships no
> such supplement.** Phrases like "provided in the supplemental material",
> "listed in Supp. Table 4", "from Supplementary Figure 2" — where the cited
> artefact is in neither the package nor the source PDF's own text.

This caught **all three** defective specs in round 3 (LDLR, GAA, Hearing Loss)
with **no false positives**, and it is greppable. The distinction that makes it
work is the second clause: Brain Malformations cites supplements *its source
also cites* and is honest; LDLR cites a "Supplementary Figure 2" that **its
source never mentions at all**, and the content under it is invented.

Practical check per spec:

1. Grep the guideline for `supplement|Supp\.|attached|attachment|accompanying`.
2. For each hit, grep the **source PDF text** for the same reference.
3. Hits present in the guideline but absent from the source are where the
   fabrications are. Hits present in both are honest citations — verify the
   content is marked unavailable rather than filled in.

Note this is a *fabrication* detector, not a correctness detector. It says
nothing about modes 2 and 3 below, which remain invisible to any signature.

---

## 3. What the defects actually look like

Regenerating 13 specs from source found four distinct failure modes. Only the
first is even theoretically grep-detectable, and only sometimes.

**1. Fabricated content** — whole appendices absent from every source file.
ADA had four (functional-evidence controls, PIDTC 2022 criteria definitions,
an approved-assay table citing a PMID that appears nowhere, invented PS3
activity sub-ranges). Also RAG2's protein domain map, RUNX1's "Traditional
Combining Rules" and Appendix B, F9's four "Standard ACMG/AMP" combination
tables, ACADVL's PS2 rationale. Rounds 2–3 added FBN1's Appendix B (invented
exon mappings and a "258 cysteine residues across cbEGF1-cbEGF43" count),
LDLR's 60-row cysteine table with a fabricated Guo et al. attribution, and
Hearing Loss's BA1/BS1 exclusion list — two OTOF variants with ClinVar IDs,
pathogenicity calls and subpopulation frequencies, invented in full.

**1b. The generic-flowchart graft** — a distinct and recurring sub-mode worth
naming, because it hides inside a *correct-looking* appendix and reverses the
error direction. Where a spec says only "follow the adapted flowchart" and
ClinGen ships no flowchart, the guideline substitutes the generic SVI/Tayoun
PVS1 decision tree, whose branches turn on **"role of region unknown"** and
**">10% / <10% of protein removed"**. Those branches are almost never what the
VCEP wrote, and they **under-call**:

- **FBN1** — the graft assigns PVS1_Moderate to an NMD-escaping frameshift
  removing <10% of protein. The VCEP assigns **Strong**, unconditionally. The
  fabricated Appendix A contradicted the same document's own correct PVS1
  table.
- **GAA** — same graft, and here it converted a purely *positional* rule
  (codon 916) into a percentage rule, inventing a **PVS1_Strong pathway for
  premature termination codons that the VCEP does not have at all**.

Grep candidates: `>10%|10% of the protein|role of (the )?region|Tayoun` in any
appendix of a spec that ships no flowchart. Check the strength assignments in
the body — if the body table and the appendix disagree, the body is usually
right and the appendix is the graft.

**2. Qualifying clauses stripped from genuine tables.** The table is real; the
rule that constrains it is gone. The SVI autosomal-recessive de novo downgrade
was dropped from IL7R and DCLRE1C — both AR genes, where it is load-bearing.
IL2RG lost the X-linked carrier-mother and mosaicism provisions. DCLRE1C lost
the heterogeneity-row cap. **This is the most common mode and it is invisible
to any signature**, because what is present is correct.

Round 2 confirms how systematic this is: the SVI de novo Table 1 footnote
**"Maximum allowable value of 1 may contribute to overall score"** — the
heterogeneity-row cap — was missing from **all three** of FBN1, GUCY2D and
SERPINC1, the same clause previously lost from DCLRE1C. GUCY2D had separately
dropped the PM3 Table 1 footnote requiring variants to meet PM2. When you
reproduce a shared SVI table, **transcribe its footnotes**; they are the part
that gets lost, and they are the part that constrains the numbers.

**3. Source contradictions silently reconciled.** The spec disagrees with
itself; the guideline picks one reading and presents it as settled. IL2RG's
PS4 defines strength by proband count in one place and by summed case scores
in another, with gaps between the bands — merged as if equivalent. RAG2's PVS1
flowchart contradicts its prose by one strength level and was harmonised
*downward*, under-calling the commonest LoF class. Also RUNX1 PM4, ACADVL
exon 20. The output is internally consistent, so nothing looks wrong. The only
defence is the instruction to report contradictions rather than resolve them.

**4. Fabricated provenance.** Invented sourcing is what makes invented content
look verified. FOXN1 cited PMID 30311386 — Oza et al. co-segregation LOD — as
the de novo recommendation; the spec attaches no PMID there at all. PTEN
supplied full author/title/journal strings for bare PMIDs. RMRP listed
attachments the package does not ship. Note the corpus disagrees with itself
about PMID 30311386, attributing it to both "Jarvik & Browning, 2016" and
"Oza AM, DiStefano MT" across 20 files.

Two load-bearing numeric errors also turned up, both from misreading an image:
PTEN's Cleveland Clinic score for endometrial cancer dx 20-29 was recorded as
6 where the source says **10**; RUNX1's Grantham Tyr→Lys was 110 where the
correct value is **85** (110 is the Lys→Trp cell two rows down). Expect more of
these wherever a spec ships a matrix as a PNG.

---

## 4. Method that works, and what it costs

Per spec, one agent, given the already-downloaded source folder:

- **Do not read the superseded local file before drafting.** Read it only
  afterward, for the changelog. This is what prevents stale values being
  carried forward, and it is why defects surface at all.
- **Transcribe every supplementary file.** List the folder, confirm each opens,
  extract embedded images from `.docx`/`.pptx` (several tables exist only as
  PNGs inside the archives), render vector flowcharts via LibreOffice when
  arrow topology matters. If a file will not open, say so — never infer.
- **Never fill a gap the spec leaves open.** Mark absent criteria
  "Not specified by VCEP". Do not substitute generic ACMG/AMP content.
- **Report contradictions; do not resolve them.**
- **When remediating existing content, split it two ways** (policy decision,
  round 3 — apply this consistently from here):
  - Content that **contradicts** the source, or is a **generic graft** (mode
    1b), is **deleted**, with a note in the Version History saying what was
    removed and why.
  - Content that merely **exceeds** the source — gene-specific, plausible,
    operationally useful, and likely copied from a real document ClinGen does
    not distribute — is **retained under an explicit banner**:
    `> **⚠️ NOT IN DISTRIBUTED PACKAGE — could not be source-verified.**`
    followed by what the source actually says instead.

  The rationale: deleting probably-genuine clinical detail degrades the tool,
  but leaving it unmarked is the confabulation risk we are trying to remove.
  GAA is the worked example — its PP4 point system, pseudodeficiency variants
  and Kroos classification are all retained under banners, while its Tayoun
  graft was deleted outright.
- **Preserve source typos verbatim** and flag them.
- **Record inclusive (`>=`/`<=`) vs strict (`>`/`<`)** for every threshold.
- **Write to a scratch path only.** The parent merges the registry centrally —
  concurrent agents editing `vcep_registry.json` will conflict.

Cost observed: **~10 minutes and ~130k tokens per spec**, 13 in parallel with
no contention. Extrapolated, the remaining 80 is roughly 8–10 batches.

**Two operational lessons from the 2026-08-07 run:**

- *Isolate scratch directories per agent.* A stale PNG left by a sibling run
  nearly got transcribed into ACADVL as a decision tree belonging to another
  spec. That agent caught it by re-rendering to a clean directory and
  cross-checking the PDF text layer — but it was luck, not process.
- *Verify sources are complete before dispatching.* RAG1 had to be re-run
  because a supplement had been silently lost by a downloader bug (§5).

---

## 5. Source material is already downloaded and now trustworthy

**`/tmp/vcep-supplement-survey-2026-08-07/ClinGen/`** holds all 122 spec
folders — 813 files, every one with a correct extension, none zero-byte. This
is ephemeral (`/tmp`); re-download with
`scratchpad/fetch_all.py`-style driver logic if it has been cleared, pacing
8s + jitter between specs to stay under ClinGen's rate limits.

Three `download.py` bugs were found and fixed this session, all of which
silently produced incomplete sources while reporting success:

- **`9604d5e`** — supplements saved with no extension. `os.path.splitext` on
  `Specifications_Table4_V1.2` returns `.2`, which the guard accepted, so
  magic-byte detection never ran. openpyxl and python-docx refuse such files.
  This is the leading explanation for the BRCA1/BRCA2 untranscribed-supplement
  defects: all ten of their supplement names end in `_V1.2`.
- **`fb765d6`** — `fetch_page` had no retry, so one dropped TLS handshake
  aborted an entire spec. GN141 failed a full-corpus run this way.
- **`711e732`** — the already-exists check matched by *prefix*, so a supplement
  advertised as "PM3" was treated as satisfied by `PM3 Criterion.pdf`, never
  downloaded, and recorded as present. GN123 lost `PM3.docx` this way; GN006
  and GN157 were also affected. `save_metadata` now records `duplicate_files`
  and treats any repeat as incomplete.

If a future run finds a spec whose guideline omits supplement content, check
whether one of these bugs was in play at download time before assuming the
generation prompt was at fault. Conversely: **APC's supplements downloaded
correctly all along**, so its omissions are a generation-prompt failure, not a
tooling one. Mode 2 has at least two independent causes.

---

## 6. Reproducing the remaining-spec list

```python
import json
reg = json.load(open("plugins/variant-classifier/skills/variant-classifier/data/vcep_registry.json"))["specifications"]
byid = {}
for e in reg: byid.setdefault(e["spec_id"], []).append(e)
genes_of = {gn: {g["symbol"] for e in v for g in e["genes"]} for gn, v in byid.items()}

audited   = {"GN009","GN007","GN002","GN089","GN092","GN005"}
major     = {gn for gn, gs in genes_of.items() if gs & {
             "SLC6A8","TCF4","SLC9A6","CDKL5","FOXG1","MECP2","UBE3A","CYP1B1",
             "CTLA4","BMPR2","MLH1","MSH2","MSH6","PMS2"}}
new_specs = {"GN105","GN156","GN157","GN158","GN160","GN170","GN173","GN226"}
bumps     = {"GN003","GN008","GN021","GN080","GN088","GN113","GN114","GN116",
             "GN119","GN121","GN123","GN124","GN129"}
brca2     = {"GN097"}
ranges    = {"GN022","GN167","GN084"}                       # round 2
zero_supp = {"GN010","GN011","GN012","GN013","GN014","GN015","GN018","GN023"}  # round 3

remaining = sorted(set(byid) - (audited | major | new_specs | bumps | brca2
                                | ranges | zero_supp))
print(len(remaining))  # 69
```

To re-derive the zero-supplement set (it is a property of the download, not the
registry), a spec has none when every entry in its `files` list starts with
`ClinGen_ACMG_Specifications`:

```python
md = json.load(open(f"{srcdir}/{gn}_data.json"))
supp = [f for f in md["files"] if not f.startswith("ClinGen_ACMG_Specifications")]
```

---

## 7. Suggested prioritisation

~~1. The three `ranges` suspects~~ — **done, round 2** (`2f9674b`). Two false
positives; see §1.

~~2. The nine zero-supplement specs~~ — **done, round 3** (`4c91f2c`). FBN1 was
the ninth and was covered by round 2. Five of the remaining eight were clean;
see §2a.

3. **RASopathy panel (16 specs).** Biggest single batch; siblings corroborate.
   **Start here.**
4. **Limb Girdle (7) and Congenital Myopathies (7).** Both ship 7–8
   supplements per spec, so mode-2 exposure is high.
5. **Cardiomyopathy (7).** MYH7 is already audited and known bad (phantom
   PS2/PM6, Appendix A listing strengths the spec never defines) — its six
   siblings share conventions and are likely to share defects. Note MYH7's
   defect is now recognisable as **mode 1b**, the generic-flowchart graft, so
   check its siblings' PVS1 appendices specifically.

**Before dispatching any batch, run the §2a grep across the whole panel
first.** It is cheap, it needs no agent, and it tells you which specs in the
batch are likely to be the expensive ones.

---

## 8. Loose ends unrelated to the 69

- **GN094 LZTR1 registry inconsistency**: `version` is `1.3.0` but
  `guideline_file` is `LZTR1_..._v2.0.0.md`. Pre-existing, predates this
  session. Either the field or the filename is wrong — check against the live
  spec. Also 17 title/version mismatches, mostly benign mtDNA suffixes.
- **`read_word.py` cannot reach images embedded inside `.docx`.** Agents worked
  around it by unzipping the archive manually. Worth fixing properly; several
  tables exist only as embedded PNGs.
- **`read_ppt.py` silently drops text.** The F9 agent found most of slide 2
  missing and had to read raw `slide2.xml`. Same class of bug.
- **PP1 co-segregation LOD grids** are damaged in at least five specs — ADA and
  DCLRE1C truncated 11×11 → 6×6, IL7R omitted entirely, ACADVL truncated with
  an admission, JAK3 5 of 10 rows, Hearing Loss fabricated. For AR genes this
  grid is the operative lookup. A corpus-wide grep for this was attempted and
  **produced a false result** (the regex stem `truncat` matches the ACMG BP1
  boilerplate "**Truncating** variants…", which appears ~460 times). Detecting
  it properly needs source comparison.

---

## 9. Upstream queries for ClinGen (not our bugs)

Accumulated across sessions; worth sending as a batch.

- **PS3 proband gate, SCID VCEP.** The sentence *"at least one previously
  observed proband meeting PP4 is required to apply PS3 at any strength on the
  basis of a cellular model/in vitro study"* appears in the `Corrections`
  attachments for ADA, DCLRE1C, JAK3 and RAG2, but in **no** spec table.
  Evidence points both ways and the query should say so: ADA's release notes
  state it was deliberately *removed*, while RAG2 prints `PP4_Strong¹` with a
  dangling superscript whose only footnote on the page is unrelated —
  suggesting accidental *omission*. RAG1 is the strongest case for loss: it
  ships no Corrections file at all, the gate appears nowhere in its nine
  sources, yet local v2.1.0 carried it twice, and a release note attributes a
  "PS3_Moderate specification edit" to a file that was never delivered.
- **PVS1 flowchart footnote markers `a`, `b`, `d` are cited but never defined**
  — in F9, IL7R, DCLRE1C, FOXN1, ACADVL, IL2RG and RAG2. One shared template
  whose footnote block was never populated.
- **InSiGHT (MLH1/MSH2/MSH6/PMS2):** all four v2.0 specs publish an erratum
  ("Changed '2 Strong' in combining rules from Pathogenic to Likely
  Pathogenic") that none of their own tables reflect. Which is authoritative?
- **Pulmonary Hypertension (BMPR2 v2.0):** all three PVS1 strengths reference a
  "PVS1 decision tree guide" never published as an attachment.
- **Advertised-but-missing files:** ADA's "SCID VCEP PS3 Functional Evidence
  (ADA) 6.2.26" (so v2.2 ships no approved-assay list at all); RUNX1's
  "PVS1_Variable splicing table"; RAG1's "Corrections 1.6.26"; **GUCY2D's
  "PS2/PM6 file"**, cited in the spec text as "file attached" but absent from
  the distributed package.
- **Criteria that cannot be applied as distributed** (rounds 2–3). These are
  worse than a missing attachment — the criterion has no content at all
  without it:
  - **GAA (GN010) PP4** — the entire criterion reads "Points-based system.
    **See main specifications document**." That document is not distributed,
    so the package defines no point values, categories or thresholds.
  - **LDLR (GN013) PVS1** — all three strengths read only "See PVS1 flow
    diagram (Figure 1)". Figure 1 is not distributed.
  - **LDLR (GN013) PM1** — "one of 60 highly conserved cysteine residues
    (**listed in Supp. Table 4**)". Supp. Table 4 is not distributed, so the
    60 residues are unknowable from the package.
  - **FBN1 (GN022) PVS1** — "Follow the adapted flowchart"; FBN1 ships no
    supplementary files whatsoever. (Its body strength table is complete, so
    this one is recoverable; the other three are not.)
- **F8 contamination in F9's PVS1 file:** the only footnote definitions shipped
  are F8's (citing c.6852, exons 8/14, codon 32); marker `d` is undefined and
  F9's own footnotes are absent. This survived the v2.1 "PVS1 correction".
- **Duplicate publication:** RAG1's `PM3.docx` and
  `PM3 Minor Amendments 12.12.2025.docx` are the same document — byte-identical
  embedded image, differing only in Word run-splitting.
- **Hemoglobinopathy (HBB GN170, HBA2 GN173):** BS2 references "normal
  haematological values in Appendix 3"; the distributed Appendix 3 contains
  only the PS4 phenotype table.
- Minor: F9's assay workbook ships a dummy `Example` row (PMID 1234567,
  "Jones", 1985) marked "Approved assay: y". RAG1's PM3 PDF carries a
  Wondershare PDFelement trial watermark. PTEN spells **"SpliceAl"** (lowercase
  L) in all six criterion-text occurrences, correctly only once.

---

## 10. Threshold comparators — resolved, keep the discipline

`97bb356` made frequency thresholds carry their operator. VCEPs genuinely
differ on inclusivity and it is not cosmetic: **PTEN v3.2 flipped PS4 from
CC score `>30` to `≥30`**, a third confirmed instance after GALT and SLC6A8.
A proband sitting exactly on 30 previously scored 0.5 points instead of 1,
silently.

When regenerating, keep recording inclusive vs strict per criterion — several
specs state a bound with **no operator at all** (RUNX1 BS1, PTEN BS1 "up to",
F9's point table), and those should be recorded as unstated rather than
guessed.

---

## 11. Verification discipline

Every remediation batch should end with:

1. **Central merge behind a gate.** `json.dumps` **cannot** round-trip this
   registry — it uses a house style (inline `genes`/`mondo_ids` for single-gene
   entries, one-per-line for multi-gene) and a byte-level gate will fail. Use
   per-entry raw-text edits plus a *structural* gate: parse before and after,
   assert only the intended fields changed on exactly the intended entries.
   Working implementation: `scratchpad/merge_bumps.py` from this session.
2. `check_updates.py` — confirm live vs local is in sync.
3. Registry/disk consistency — entry count, orphans, missing, and that every
   `guideline_file` matches `v{version}.md`.
4. `check_vcep_spec.py <gene>` for every touched gene.
5. Full test suite: `plugins/vcep-spec/skills/vcep-spec/tests` (26) and
   `plugins/variant-classifier/skills/variant-classifier/tests` (17).
6. **Sanity-check outputs against their own source folder** — after the ACADVL
   near-miss, confirm no guideline contains content its package does not have.

**Registry state at writing:** 125 entries, 125 files, no orphans, all
filenames normalised `x.y.z`, live registry in sync (0 new, 0 outdated).
GN094 LZTR1 is the only `version`/`guideline_file` mismatch and is
pre-existing (§8).

**Corrections that do not change the ClinGen version** (rounds 2–3 were all of
this kind) **must not rename files or touch the registry.** Edit the guideline
in place and record what changed in its Version History under a dated
"Document corrections" block, stating which source file each finding was
verified against. This keeps `guideline_file` matching `v{version}.md`, leaves
the registry byte-identical, and means step 2 of the gate above
(`check_updates.py`) is a no-op you can legitimately skip — live-vs-local sync
cannot have changed if the registry JSON did not.

---

## 12. Changelogs from the 2026-08-07 batch

Per-spec changelogs — transcription status for every supplementary file,
catalogued source defects, and what was removed from the superseded file and
why — are at **`/tmp/vcep-bumps-2026-08-07/`**. Ephemeral; copy anything worth
keeping before `/tmp` is cleared. They are the best available worked examples
of the method in §4.

For rounds 2 and 3 the changelogs are **in the guidelines themselves**, under
"Document corrections" in each Version History, and in the two commit
messages (`2f9674b`, `4c91f2c`) — which are deliberately detailed and are not
ephemeral. Prefer that pattern going forward: a finding recorded in `/tmp` is
a finding you will lose.

---

## 13. Round 2 and 3 summary

**Round 2 — `2f9674b`** — FBN1 (GN022), GUCY2D (GN167), SERPINC1 (GN084).
Closed the `ranges` lead (§1). FBN1 turned out to carry two fabricated
appendices, including the mode-1b PVS1 graft that contradicted its own body
table. All three had lost the SVI heterogeneity-row cap footnote.

**Round 3 — `4c91f2c`** — the eight zero-supplement specs. Clean: RYR1
(GN012), Brain Malformations/AKT3 (GN018), the GN014 nuclear set
(ETHE1/PDHA1/POLG/SLC19A3), mtDNA (GN015), Platelet Disorders (GN011).
Defective: LDLR (GN013), GAA (GN010), Hearing Loss (GN023) — all three caught
by the §2a signal.

Incidental finding, harmless but confusing: the downloader mislabels the two
Mitochondrial specs by gene — GN014's folder is `GN014-CDKL5` and GN015's is
`GN015-UNKNOWN`. **The PDFs themselves are correct** (GN014's keywords list
SLC19A3/PDHA1/POLG/ETHE1; GN015 is the mtDNA document). The registry is right
and needs no change; only the ephemeral download folder names are wrong. Do
not "fix" a registry entry on the strength of a source folder name.
