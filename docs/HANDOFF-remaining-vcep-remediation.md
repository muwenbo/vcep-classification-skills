# Handoff — remediation of the remaining VCEP guidelines

**Written:** 2026-08-07, revised 2026-08-17 after the final remediation round
**Branch:** `vcep-registry-refresh-2026-08` (branched from `main`, **not merged**)
**Round 4 remediation commit:** `3b62aeb`
**Round 5 remediation commit:** `78ad52b`
**Round 6 remediation commit:** `0bad381`
**Round 7 remediation commit:** `16212de`
**Round 8 remediation commit:** `bb87729`
**Round 9 remediation commit:** `f298ac8`
**Round 10 remediation commit:** `983d931`
**Round 11 remediation commit:** `efe4f3d`
**Round 12 remediation commit:** `71c56ff`
**Round 13 remediation commit:** `69a9d62`
**Round 14 remediation commit:** `07cb4af`
**Working tree:** All remaining specifications are remediated and committed; this handoff revision follows round 14.

This picks up where the 2026-08-06 session's handoff left off. That document's
"decide remediation scope for the ~84 unaudited guidelines" is now closed.
The durable lesson is **how not to do it**, and what source-first remediation
costs when done properly.

**Revision note (rounds 2–14).** Thirteen batches have been completed since this
document was first written. The three "ranges" suspects turned out to be
almost entirely false positives (§1), the zero-supplement premise turned out
to be too broad (§2a), and all 16 RASopathy specs have now been remediated
source-first (§13). All seven Limb Girdle Muscular Dystrophy specs are now also
remediated source-first (§7a, §13), as are all seven Congenital Myopathies
specs (§7b, §13), all seven Cardiomyopathy specs (§7c, §13), and all five
Epilepsy Sodium Channel specs (§7d, §13), all three Monogenic Diabetes specs
(§7e, §13), all three remaining Platelet Disorders specs (§7f, §13), both
Hereditary Hemorrhagic Telangiectasia specs (§7g, §13), both HBOP Cancer
specs (§7h, §13), both Cerebral Creatine specs (§7i, §13), and the final
15-spec cross-panel batch (§7j, §13). **No specifications remain in this
remediation inventory.** The source-first method and warnings remain relevant
for future releases.

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

The signature was detecting a **shipping manifest, not a fabrication.** Round
7 reinforces the rule from the opposite direction: TNNI3, TNNT2, and TPM1
contained the full local matrix even though their packages ship no
`PS2_PM6.pdf`; their cores only say to refer to external SVI guidance. Those
three matrices were genuine remediation targets, but only package-level source
comparison established that fact. The grep alone still cannot distinguish
them from the many source-backed instances.

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

So F9 remains the only substantive *range/operator* instance from that narrow
lead. **Do not build another signature out of table shape.** Both attempts
failed the same way: VCEPs copy shared ClinGen SVI material verbatim, so shape
tells you about the template, not about whether this document transcribed it
honestly. Only source comparison works.

---

## 2. Scope: complete — 0 specs remain

122 unique spec IDs; all 122 covered (6 audited, 14 major bumps, 8 new specs,
13 minor bumps, BRCA2, the 3 range-suspects of round 2, the 8 zero-supplement
specs of round 3, the 16 RASopathy specs of round 4, and the 7 Limb Girdle
specs of round 5, the 7 Congenital Myopathies specs of round 6, the 7
Cardiomyopathy specs of round 7, and the 5 Epilepsy Sodium Channel specs of
round 8, the 3 Monogenic Diabetes specs of round 9, the 3 remaining
Platelet Disorders specs of round 10, the 2 HHT specs of round 11, the 2 HBOP
Cancer specs of round 12, the 2 Cerebral Creatine specs of round 13, and the
final 15 specifications of round 14). **0 remain.**

The final batch was grouped by VCEP because panels share source conventions and
defects tend to repeat within a panel:

| n | VCEP |
|---|---|
| 2 each | von Willebrand, X-linked Retinal, Leber Congenital Amaurosis / early-onset Retinal Dystrophy |
| 1 each | 9 further panels |

**Batch by panel, not alphabetically.** The 2026-08-07 run put nine sibling
SCID specs in flight together and they corroborated each other — the same
PS3 sentence was independently traced across four of them, which is what
turned a vague suspicion into a precise upstream query. The RASopathy group
(16) has now been completed the same way; its recurring shared-source defects
would have been much harder to identify one gene at a time.

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

For round 14 the older directory was empty and the final 15 packages were
re-downloaded to `/tmp/vcep-remaining15-round14.YeYW6l/ClinGen/`. All metadata
reported complete; disk and manifests matched; every PDF and Office archive
passed structural checks; all 70 page/contact-sheet montages were visually
reviewed. That directory is also ephemeral. Exact physical filenames are now
durable in each guideline's 2026-08-17 correction history and in round-14
regression tests.

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
rasopathy = {"GN038","GN039","GN040","GN041","GN042","GN043","GN044","GN045",
             "GN046","GN047","GN048","GN049","GN087","GN094","GN127","GN128"}  # round 4
limb_girdle = {"GN180","GN184","GN185","GN186","GN187","GN188","GN189"}  # round 5
congenital_myopathies = {"GN146","GN147","GN148","GN149","GN150","GN169","GN179"}  # round 6
cardiomyopathy = {"GN095","GN098","GN099","GN100","GN101","GN102","GN103"}  # round 7
epilepsy_sodium = {"GN067","GN068","GN069","GN070","GN076"}  # round 8
monogenic_diabetes = {"GN017","GN085","GN086"}  # round 9
platelet_disorders = {"GN079","GN082","GN083"}  # round 10
hht = {"GN135","GN136"}  # round 11
hbop = {"GN020","GN077"}  # round 12
cerebral_creatine = {"GN025","GN026"}  # round 13
final_round = {"GN006","GN019","GN024","GN071","GN078","GN081","GN090",
               "GN091","GN106","GN112","GN120","GN126","GN141","GN164",
               "GN208"}  # round 14

remaining = sorted(set(byid) - (audited | major | new_specs | bumps | brca2
                                | ranges | zero_supp | rasopathy | limb_girdle
                                | congenital_myopathies | cardiomyopathy
                                | epilepsy_sodium | monogenic_diabetes
                                | platelet_disorders | hht | hbop
                                | cerebral_creatine | final_round))
print(len(remaining))  # 0
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

~~3. RASopathy panel (16 specs)~~ — **done, round 4** (`3b62aeb`). See §13.
~~4. Limb Girdle (7)~~ — **done, round 5** (`78ad52b`). See §7a and §13.
~~5. Congenital Myopathies (7)~~ — **done, round 6** (`0bad381`). See §7b and
   §13.
~~6. Cardiomyopathy (7)~~ — **done, round 7** (`16212de`). See §7c and §13.
~~7. Epilepsy Sodium Channel (5)~~ — **done, round 8** (`bb87729`). SCN1A (GN067), SCN2A
   (GN068), SCN3A (GN069), SCN8A (GN070), and SCN1B (GN076). Preflight the
   full panel before opening local guideline bodies; see §7d and §13.
~~8. Monogenic Diabetes (3)~~ — **done, round 9** (`f298ac8`). HNF1A
   (GN017), HNF4A (GN085), and GCK (GN086); see §7e and §13.
~~9. Platelet Disorders (3)~~ — **done, round 10** (`983d931`). GP1BA
   (GN079), GP1BB (GN082), and GP9 (GN083); see §7f and §13.
~~10. Hereditary Hemorrhagic Telangiectasia (2)~~ — **done, round 11**
   (`efe4f3d`). ACVRL1 (GN135) and ENG (GN136); see §7g and §13.
~~11. HBOP Cancer (2)~~ — **done, round 12** (`71c56ff`). ATM (GN020) and
   PALB2 (GN077); see §7h and §13.
~~12. Cerebral Creatine (2)~~ — **done, round 13** (`69a9d62`). GATM (GN025)
   and GAMT (GN026); see §7i and §13.
~~13. Final cross-panel inventory (15)~~ — **done, round 14** (`07cb4af`).
PAH (GN006), MYOC (GN019), DICER1 (GN024), F8 (GN071), VHL (GN078), both VWF
specifications (GN081/GN090), IDUA (GN091), RPGR (GN106), KCNQ1 (GN112),
RPE65 (GN120), RS1 (GN126), PIK3CD (GN141), ABCA4 (GN164), and AIPL1 (GN208);
see §7j and §13.

There is no next remediation batch in this inventory. For a future ClinGen
release or newly added specification, retain the same panel-first preflight and
run the §2a provenance grep before opening the superseded local body.

---

## 7a. Limb Girdle preflight and remediation — complete

The §2a preflight was completed on 2026-08-07 for all seven Limb Girdle
Muscular Dystrophy specs. The source-first remediation followed on 2026-08-09
and is committed as `78ad52b`.

| Spec | Substantive files | Provenance result | PVS1 result |
|---|---:|---|---|
| ANO5 (GN188) | 7/7 | clean | genuine shipped flowchart |
| CAPN3 (GN187) | 8/8 | clean | genuine shipped flowchart |
| DYSF (GN180) | 9/9 | clean | genuine shipped flowchart |
| SGCA (GN189) | 9/9 | clean | genuine shipped flowchart |
| SGCB (GN184) | 9/9 | clean | genuine shipped flowchart |
| SGCD (GN186) | 9/9 | clean | genuine shipped flowchart |
| SGCG (GN185) | 9/9 | clean | genuine shipped flowchart |

All 60 advertised substantive files are present, readable, correctly typed and
non-empty. Metadata and disk agree; there are no missing, duplicate, extra or
zero-byte files. Every guideline claim involving PVS1, PM3, PS1 splicing,
experimental splice data, benign-frequency exceptions, PP4 or PS3 appears in
the corresponding ClinGen PDF and has a physical artifact in that gene's
package.

The PVS1 appendices trigger the §1b signature (`role of region unknown`,
`>10%`/`<10%` of protein), but they are **not grafts**. ClinGen ships a distinct
gene-specific `PVS1 flowchart <GENE>.pptx` for all seven. Each uses that shared
template with a gene-specific transcript, NMD boundary and in-frame exon list.
Do not delete the shared branches merely because they resemble Tayoun/SVI.

Carry these source caveats into remediation without resolving them:

- Every flowchart uses strict `>10%` and `<10%` branches, leaving exactly 10%
  unassigned.
- Footnote markers `a`, `b`, `c` and `d` appear without a definition block in
  the slide or its speaker notes.
- SGCD deliberately differs from its siblings: premature truncation in codons
  1–34 is `PVS1_Supporting`; the other six use `PVS1_Moderate`.
- SGCD's local bibliography expands PMID 27618451 to “Abou Tayoun et al.,
  2018”, while the distributed package supplies only the bare PMID in the
  PVS1 PowerPoint. Treat the expanded provenance as unverified unless another
  distributed source supports it.

Shared supplements are byte-identical across all seven for PM3 co-application,
PM3 scoring, PS1 splicing, experimental splice data and benign-frequency
exceptions. PP4 PowerPoints and PS3 workbooks are gene-specific. This is a good
panel for sibling corroboration, but gene-specific PVS1, PP4 and PS3 content
must still be transcribed independently.

### Round 5 outcome

All seven guidelines — ANO5 (GN188), CAPN3 (GN187), DYSF (GN180), SGCA
(GN189), SGCB (GN184), SGCD (GN186), and SGCG (GN185) — were independently
drafted from their complete packages before comparison with the local files.
All 60 substantive artifacts were opened; Office XML, speaker notes, workbook
cells, original PNGs, and rendered arrow topology were inspected. No registry
entry or filename changed.

Recurring findings:

- PVS1 transcriptions had stripped the exon-presence gate from NMD-producing
  nonsense/frameshift, splice, and deletion paths in multiple genes. This is a
  load-bearing over-call: the source assigns N/A when the exon is absent from
  the biologically relevant transcript.
- Visibly struck-through critical-region and initiation-codon paths were
  presented as active in several local files. SGCB's initiation outcomes were
  reversed; SGCA also had source-contradicting initiation assignments. These
  operative contradictions were removed or marked inactive, not retained as
  alternative guidance.
- All seven local classification tables had inferred `>=10`/`<=-7` outer
  comparators. The core PDFs print bare `10` and `-7`; the guidelines now state
  that the operator is unspecified. SGCA also carried a generic traditional
  combination-rule graft absent from its package; it was deleted.
- The byte-identical experimental-splice PNG had been mistranscribed in several
  ways, including routing the silent/intronic branch through a protein-impact
  question that belongs only to "other variants". All seven now follow the
  actual arrows. The source image itself begins with a clipped incoming arrow
  at its left boundary, though no visible criterion text is missing, and its
  `(d)`/`(e)` markers are undefined.
- Shared PM3 footnotes, PS1 qualifications, benign-frequency exception rows,
  and gene-specific PS3 workbook fields were incompletely represented in
  several files. SGCD and SGCG permit PS3_Moderate in their criteria PDFs but
  ship no populated Moderate assay instance; only Supporting instances exist
  in their workbooks. This limitation is now explicit.
- All seven core-PDF DOIs were restored. Unsupplied bibliographic expansions
  were removed, including SGCD's "Abou Tayoun et al., 2018" expansion of the
  bare PMID 27618451.

The preflight caveats remain unresolved source issues, not local defects:
strict `>10%`/`<10%` leaves exactly 10% unassigned, PVS1 markers `a`–`d` have
no definitions, and SGCD deliberately assigns codons 1–34
PVS1_Supporting while the other six use PVS1_Moderate.

---

## 7b. Congenital Myopathies remediation — complete

Round 6 (`0bad381`) remediated NEB (GN146), ACTA1-AD (GN147), DNM2
(GN148), MTM1 (GN149), RYR1-AD (GN150), ACTA1-AR (GN169), and RYR1-AR
(GN179). The panel-wide §2a preflight found all 24 advertised artifacts
present, readable, correctly typed, and source-cited. Each guideline was then
drafted source-first before local comparison. All spreadsheet cells, embedded
images, raw Office XML, speaker notes, PDF pages, and flowchart connectors were
inspected. No registry entry or filename changed.

Recurring and high-impact findings:

- Package-absent generic content recurred. NEB and RYR1-AR had generic
  PS2/PM6 point systems; NEB also had a generic PM3 per-proband table; both
  RYR1 specs had generic PP1 threshold grids despite shipping no segregation
  chart. ACTA1-AD's generic likelihood/LOD PP1 table contradicted its actual
  attached point chart. These grafts were deleted and the missing conversion
  or artifact was stated explicitly.
- PVS1 flowcharts again lost transcript-presence, frequency/exon, splice,
  deletion, duplication, and initiation-codon gates. MTM1 had two reversed
  initiation outcomes; RYR1-AR had omitted transcript gates on all predicted-
  NMD branches. Undefined `a`–`d` markers and strict `>10%`/`<10%` exact-10%
  gaps recur in NEB, MTM1, ACTA1-AR, and RYR1-AR.
- MTM1 contained a fabricated mouse-model assay row. Its actual workbook has
  19 approved Supporting instances, all with zero P/LP and B/LB validation
  controls, and several unresolved source defects: questioned/blank fields,
  apparently cross-assigned localization thresholds, and variant lists placed
  under `Proposed strength (modified)` instead of `Variants evaluated`.
- ACTA1-AD omitted most of its 15 approved Supporting assay instances and
  replaced the byte-identical AD/AR PP1 attachment with the wrong framework.
  The attachment supplies segregation points but no point-to-strength mapping;
  its +5-point-per-allele cap coexists with the core PDFs' Strong cap.
  ACTA1-AD separately says to stack "the two assays" while listing three
  Supporting assay categories.
- DNM2's workbook proposes Supporting for every populated assay but leaves all
  `Approved assay (y/n)` cells blank. Its 11×11 segregation grid was truncated
  locally to six columns. PS4 Moderate/Supporting are bare values while Strong
  is inclusive only in the core PDF, leaving attainable totals such as 0.75
  unmapped.
- RYR1-AD's approved PMID 16958053 assay defines abnormality as **reduced**
  voltage-gated calcium release, contradicting the core PS3_Moderate rule's
  **increased** release. Its PS4 source pair also leaves 0.75 unmapped.
  RYR1-AR's PVS1 PowerPoint contains three broken raw connector bindings even
  though the rendered deletion arrows remain visually continuous; both raw
  and rendered readings are now reported.
- Several core combination tables invoke undefined or inapplicable strengths.
  MTM1 is the inverse case: it defines operative PVS1 criteria at four
  strengths but omits PVS1 entirely from every Pathogenic/Likely Pathogenic
  combination. No contradiction was silently reconciled.
- All seven core-PDF DOIs and source-supplied reference DOIs were restored;
  unsupplied bibliographic expansions were removed. Exact source typos,
  missing comparators, blank cells, and bare point values remain explicit.

Round 6 found no plausible gene-specific excess that needed a warning banner:
the removed material was either generic, source-contradicting, or fabricated.

---

## 7c. Cardiomyopathy remediation — complete

Round 7 (`16212de`) remediated MYBPC3 (GN095), TNNI3 (GN098), TNNT2
(GN099), TPM1 (GN100), ACTC1 (GN101), MYL2 (GN102), and MYL3 (GN103).
The panel-wide preflight found all 15 advertised PDFs present, readable,
correctly typed, and source-cited: seven core specifications, seven copies of
the shared three-page PS4 examples, and the MYBPC3 PVS1 decision tree. The
PS4 copies are byte-identical (SHA-256
`3375902edf77e2e4048bf84bd3cad83a44211b94993859d01b3f37c85a59e57f`).
All 163 core pages were text-extracted and visually inspected in full-page
renders; the four unique supplemental pages were rendered at higher
resolution and checked for table values and arrow topology. The independent
baseline was saved before opening any guideline body at
`/tmp/cardiomyopathy-round7.hVgVNY/SOURCE_BASELINE.md`. No registry entry or
filename changed.

Recurring and high-impact findings:

- TNNI3, TNNT2, and TPM1 carried the complete `2/1/0.5/0.25` de novo matrix
  and `0.5/1/2/4` strength ladder even though their packages ship no SVI de
  novo attachment. Their cores only refer to external SVI guidance, mention
  points without defining them, and print PS2 under Strong and PM6 under
  Moderate. The undistributed numeric grafts and derived point-based
  applicability claims were removed; the source limitation is explicit.
- MYBPC3's genuine shipped PVS1 tree had been normalized in ways that erased
  source information. The guideline now preserves undefined markers `a`–`d`,
  full-gene `PVS1 d`, initiation `PVS1_Supp`, the presumed-in-tandem
  no/unknown-impact N/A route, and strict `>10%`/`<10%` branches that leave
  exactly 10% unassigned. The gray critical-region paths remain visible but
  are not treated as pre-authorized: the attachment explicitly says no
  MYBPC3 critical regions/domains have been pre-defined.
- The shared PS4 supplement was incompletely represented in several files.
  All seven now retain its nine exact comparisons, ancestry-matched Variant B
  decision, and Variant C conclusion that Strong is acceptable while Moderate
  is also appropriate under conservative clinical judgment. The literal
  `gnomAF` typo is recorded rather than silently corrected.
- TNNI3 had inferred distinct negative assay outcomes for BS3 Strong,
  Moderate, and Supporting. The source says only `See PS3 specifications` at
  all three strengths; the inferred outcomes were deleted. Several files also
  invented a distinct positive PM4 Supporting condition. The cores permit a
  downgrade from Moderate based on predicted impact but supply no separate
  Supporting condition or numeric size/location/conservation threshold.
- For TNNI3, TNNT2, TPM1, ACTC1, MYL2, and MYL3, PVS1 says LoF is not an
  established mechanism while the shared BP1 comment says "the current
  genes" have null variants as a known mechanism. Both source statements are
  now reported without harmonization; BP1 remains N/A as printed.
- MYL3's phenotype appendix had categorized DCM as excluded, although the
  source calls for careful consideration because end-stage HCM can resemble
  DCM. That overstatement, invented version-history bullets, generic resource
  appendix, and stale generated-date footer were removed.
- All seven specification DOIs and every source-supplied reference DOI were
  restored. No plausible gene-specific excess needed a warning banner; the
  removed material was source-contradicting, generic, or derived from an
  undistributed external table.

Unresolved source issues are preserved rather than repaired: the MYBPC3 PVS1
marker definitions and exact-10% route are absent; its critical regions are
not pre-defined; the three point-matrix packages reference external SVI
guidance they do not distribute; PM4 gives no separate Supporting rule; the
six LoF/BP1 statements conflict; and the shared PS4 PDF contains `gnomAF`.

---

## 7d. Epilepsy Sodium Channel remediation — complete

Round 8 (`bb87729`) remediated SCN1A (GN067), SCN2A (GN068), SCN3A
(GN069), SCN8A (GN070), and SCN1B (GN076). The panel-wide provenance
preflight found all 32 advertised substantive artifacts present, readable,
correctly typed, and source-cited. Each specification was drafted source-first
in an isolated scratch directory before local comparison. All 103 PDF pages,
four one-slide PVS1 PowerPoints (including notes and raw connector topology),
and every populated workbook cell/sheet were inspected. Four shared artifacts
were byte-identical wherever shipped: `Combining Rules.pdf`, `PM1 Table.xlsx`,
`PS1_Variants impacting splicing.pdf`, and `Paralogous Gene Table.xlsx`.

Recurring and high-impact findings:

- SCN1A's core says a PVS1 decision tree is included, but no tree exists in
  the manifest or package. The guideline now states that only the full-gene-
  deletion prose and raw exon table are available; no generic SVI/Tayoun tree
  was substituted. Its core transcript `.3` conflicts with workbook `.4`.
- The four shipped PVS1 trees had been simplified or reversed locally.
  Remediation restored initiation-codon outcomes, role-unknown/LoF-frequency/
  transcript-presence gates, strict `>10%` and `<10%` branches, duplication
  topology, and branches whose negative outcome is genuinely unspecified.
  SCN3A has a core `.3` versus supplement `.4` transcript conflict; SCN1B has
  core `.4` versus supplement `.5`.
- SCN1B's source visibly co-prints `>10%` with `>=200 aa` and `<10%` with
  `<200 aa` for a short protein, without saying AND or OR. The incompatible
  labels and exact-10% gap are preserved rather than repaired. Its PM3 table
  also supplies no phase-unknown homozygous value; a local invented 0.5 was
  removed. Three visually continuous PPTX connectors have incomplete raw
  endpoint bindings and are reported as a source defect.
- SCN2A, SCN3A, and SCN8A each have a BA1 contradiction (`>0.02%` in VCEP
  prose versus `>0.01%` plus a count floor in the Stand Alone block). All
  three readings are now explicit. Their full-gene-deletion prose/tree/points
  outcomes also conflict. SCN1B has the same three-way full-deletion conflict.
- Several local PS1 descriptions overgeneralized the shared six-row splice
  matrix or shifted its last two baseline-code rows into the wrong column.
  Every file now retains the position- and baseline-dependent outcomes.
- PS2/PM6 bare totals had repeatedly been converted into invented `>=`
  ladders, and several files asserted cross-criterion pooling not present in
  the package. Exact totals are restored and pooling is not inferred.
- Generic or explicitly superseded combination recipes, criterion-by-strength
  enumerations, and an unsupported “Approved Functional Assay” label were
  deleted. Only the shipped point weights, bands, posterior probabilities,
  and two caveats remain operative. Source spelling `Tavtigan`, punctuation,
  `16+`, and literal `-7 and below` are preserved.

No plausible undistributed gene-specific excess needed a warning banner. PM1,
exon, paralog, PS1-splicing, combining, and gene-specific PVS1 material was
either physically distributed or removed when generic/source-contradicting.

---

## 7e. Monogenic Diabetes remediation — complete

Round 9 (`f298ac8`) remediated HNF1A (GN017), HNF4A (GN085), and GCK
(GN086). The panel-wide preflight found all 12 advertised PDFs present,
readable, correctly typed, and source-cited. All 68 pages were rendered and
visually inspected before local comparison, including all three PVS1 diagrams,
GCK's PS3/BS3 tree, its PM1 and PM3 supplements, and the shared de novo table.

Recurring and high-impact findings:

- The shared de novo attachment prints exact bare values `0.5`, `1`, `2`, and
  `4`, not ranges or thresholds, and says those occurrence points are not the
  Tavtigian et al. 2020 classification points. All three local files had
  altered some title, value, cell, or footnote detail; exact source forms are
  now retained. Core PM6 Not Applicable rules remain visibly in tension with
  the attachment's generic PM6 labels.
- HNF1A's PVS1 appendix omitted the full-gene-deletion and every duplication
  branch. HNF4A omitted the Presumed-in-tandem/no-or-unknown-impact N/A path.
  GCK's PS3/BS3 summary collapsed RSI and GKRP/GKA outcomes. All visually
  verified connectors and terminal outcomes are now represented.
- HNF1A's core requires diabetes “without clear evidence of an autoimmune
  etiology” and then prints positive-autoantibody/very-low-C-peptide bullets
  without a connector. The ambiguity is surfaced rather than interpreted.
  Its plausible local-only PM3 inheritance rationale is retained only under
  the required undistributed-package warning banner; a generic PM6 graft was
  removed.
- HNF4A's core places PVS1_Supporting at `c.1258 (G)/p.Gly420 and 3'`, while
  its tree says `3' of c.1257 (Gly420)`. Its PP4 sections also differ between
  inclusive `>=50%` and strict `>50%`; the PVS1 tree prints footnote markers
  `a`–`d` without definitions. All remain unresolved and explicit.
- GCK's header uses `NM_000162.5` while detailed PVS1 prose uses
  `NM_000162.3`. Its initiation tree supplies only one path, and its PVS1
  duplication tree has no Presumed-in-tandem N/A branch; no missing outcomes
  were invented. The PS3/BS3 tree's RAI `<=0.5` and Kcat/S0.5 `<0.5`
  comparators and three-way GKRP/GKA outcome are preserved exactly.
- Source-derived convenience appendices are labeled as editorial summaries;
  physically supplied artifacts remain controlling. Source typos, verbal
  comparators, compact spacing, malformed examples, and missing footnotes are
  disclosed rather than normalized.

The independent per-spec reviews and final cross-panel gate passed. No
undistributed generic decision tree, de novo pooling rule, or inferred numeric
interval remains operative.

---

## 7f. Platelet Disorders remediation — complete

Round 10 (`983d931`) remediated GP1BA (GN079), GP1BB (GN082), and GP9
(GN083). Each complete package contained a 15-page core PDF, three DOCX
attachments, a four-sheet PS3 workbook, and a one-slide gene-specific PVS1
deck. All 18 advertised files were inspected source-first. The combining,
PS2/PM6, and workbook files are byte-identical across all three genes;
GP1BA/GP1BB share a BSS-specific PM3 document while GP9 ships a different,
generic PM3 document.

Recurring and high-impact findings:

- The local PVS1 summaries omitted or misrouted many branches and reversed
  some initiation-codon outcomes. The remediations now preserve every visible
  nonsense/frameshift, splice, deletion, duplication, and initiation route,
  exact `>10%`/`<10%` and amino-acid cutoffs, and literal terminal labels such
  as `PVS1_Supp`. The slides' red X symbols and `a`–`d` markers have no legend
  or definitions; several raw connectors have incomplete endpoint bindings.
  Those source limitations remain explicit.
- The shared de novo document's two-level headers, four-row phenotype table,
  maximum-one heterogeneity footnote, exact code labels, and bare
  `0.5`/`1`/`2`/`4` totals are restored. All three cores make PM6 Not
  Applicable/use PS2 while the attachment labels both PS2 and PM6, and the
  attachment also supplies PS2_Supporting absent from some core blocks. No
  precedence is inferred.
- Local PM3 tables invented consanguinity categories or altered cells. GP9 in
  particular assigned `0.5` instead of `0.25` to a phase-unknown LP partner.
  Exact attachment cells and footnotes are restored, with no inferred
  `>=` ladder or pooling rule. GP9's generic attachment requires all variants
  to meet PM2, while its core exempts qualifying P/LP partners from
  PM2_Supporting when BS1/BA1 do not apply; the contradiction remains open.
- The conflicting-evidence DOCX applies Tavtigian et al. 2020 only when benign
  and pathogenic criteria coexist. Its complete pathogenic/benign point
  weights and classification bands are restored. Superscripts `a` and `b`
  appear in embedded images but have no supplied definitions.
- Every one of the workbook's 305 populated cells was inspected: visible
  `GPIX` 93, `GPIBA` 108, `GPIBB` 77, and hidden `Mufti` 27. Each guideline
  uses only its gene sheet operationally. Sibling sheets remain disclosed,
  and the hidden sheet's sparse VWF/FVIII material is reported as unrelated
  working-source contamination rather than converted into criteria.
- Source-derived tables are labeled as editorial accessibility summaries;
  their named Office artifacts remain controlling. Source typos, exact verbal
  comparator forms, compact labels, URLs, and same-group assay PMIDs were
  preserved. No plausible undistributed gene-specific excess remained, so no
  warning banner was needed.

All three independent reviews and the final cross-panel gate passed after
targeted exactness and provenance fixes.

---

## 7g. Hereditary Hemorrhagic Telangiectasia remediation — complete

Round 11 (`efe4f3d`) remediated ACVRL1 (GN135) and ENG (GN136). Each package
contained a 16-page core PDF, a one-slide gene-specific PVS1 deck, the shared
one-page HHT phenotype DOCX, and the shared seven-sheet functional-assay
workbook. All eight advertised files were present and inspected source-first;
the phenotype and workbook artifacts are byte-identical across the two genes.

Recurring and high-impact findings:

- ACVRL1's generic local PVS1 prose asserted last-exon and penultimate-exon
  rules absent from the shipped tree. ENG's appendix was more dangerous: it
  invented Strong routes for non-NMD nonsense and splice outcomes and replaced
  strict source `>10%` branches with `≥10%`. Both appendices now transcribe the
  actual nonsense/frameshift, splice, deletion, duplication, and initiation
  routes and leave unsupplied outcomes open.
- ACVRL1's tree supplies no role-unknown route for removal of 10% or more.
  ENG supplies no critical-region or ≥10% route for non-NMD
  nonsense/frameshift or splice-frame-disrupting variants; where `>10%` and
  `<10%` branches do exist, exact 10% is unmapped. Both deletion trees require
  an NMD-producing deleted exon to be present in a biologically relevant
  transcript but supply no negative outcome. Raw connector endpoint bindings
  are incomplete for 13/51 ACVRL1 and 15/51 ENG connectors.
- The shared phenotype document is now fully transcribed. It forbids treating
  nosebleeds alone as sufficient for PS4, defines the four Curaçao categories
  and three-of-four PP4 threshold, and says an individual cannot be assigned
  unaffected status with confidence for segregation analysis.
- The workbook contains 729 populated cells representing 39 approved assay
  instances across seven visible sheets. Columns B:F of the intracellular
  signaling sheet are hidden but populated. Both guidelines now retain every
  populated assay-instance field, blank, literal question mark, control,
  threshold, DOI/PMID, approval, and proposed strength.
- Source conflicts remain explicit: all five mRNA rows propose unqualified
  `PS3; BS3_Supporting`, although two are not splicing assays and the core
  reserves PS3 Strong for mRNA splicing; protein rows propose BS3_Supporting
  although the core says normal expression cannot establish benignity; the
  morphology tubulogenesis bands overlap; and the somatic threshold leaves
  exactly 0.01% unmapped. The source gives no numeric assay-stacking rule.
- ENG's prior functional appendix carried unsourced assay PMIDs and both files
  lacked source DOI provenance. Those citations were removed or replaced with
  the workbook transcription, all source-supplied reference DOIs were restored,
  and ENG's controlling classification-combination member lists were expanded.

Regression tests now lock the gene-specific PVS1 routes, source gaps, complete
39-instance workbook transcription, shared conflicts, and correction-history
provenance. No registry entry, version, or guideline filename changed.

---

## 7h. HBOP Cancer remediation — complete

Round 12 (`71c56ff`) remediated ATM (GN020) and PALB2 (GN077). ATM's complete
package comprised a 20-page core PDF, three decision/point-table PDFs and a
two-sheet functional workbook; PALB2 comprised a 21-page core PDF and a
30-page Word attachment with two nested operative tables and six embedded
images. All 96 rendered source/workbook pages and all original embedded images
were inspected source-first. PALB2's packaged document renderer lacked
`pdf2image`, so the documented LibreOffice plus Poppler fallback was used and
visually verified. Its XML contains 18 visible tracked insertions, no tracked
deletions and no comment part.

Recurring and high-impact findings:

- ATM's local appendix summarized six dense PVS1 canonical-site lists but
  omitted every row. The remediation restores Lists A-F, the explicit
  non-coding and functional-GC N/A substitutions, last-exonic-G motif rule,
  initiation/NMD/domain/deletion/duplication routes and small-indel PROVEAN
  scores.
- ATM's local Scott viability thresholds were reversed relative to the literal
  workbook. They now preserve the source's counterintuitive proposed `<10`
  normal / `>10` abnormal direction. All 149 populated cells across the six
  kinase/radiosensitivity assay columns are represented, including blank Scott
  approval cells, controls, replicate limitations, readouts and DOIs.
- The ATM package conflicts on benign radiosensitivity: the core permits
  BS3_Supporting when either ATM-specific function or radiosensitivity is
  rescued, while the workbook says radiosensitivity alone receives no weight.
  Both are reported. The core also contains a stray PALB2 name in ATM RNA
  guidance; the ATM attachment supplies the applicable ATM wording.
- PALB2 had no operative PVS1 tree locally. The remediation restores the
  initiation, NMD/non-NMD C-terminal, deletion, duplication and splice routes,
  Lists A-D, exon-map overhang semantics, YHYS branches and special exon 2/3/6
  caveats. It also restores the complete PS1 splice matrix and the omitted PM3
  and BS2 per-proband point tables.
- PALB2's local domain appendix elevated a stray Word sentence about FATKIN
  into a real PALB2 domain. FATKIN is absent from the supplied PALB2 map and
  decision tree; the fabricated domain row is removed and the upstream
  carry-over is explicitly recorded.
- Further PALB2 source conflicts remain explicit: Ensembl transcript `.8`
  versus `.9`, PS1 PMID 37352859 versus 36865205, a deletion box that says
  `<10% (>356 nt)`, and incompatible core-versus-Word Very Strong + Supporting
  combination-member lists.

Regression tests lock both source DOIs, ATM Lists/GC exclusions and literal
workbook thresholds, PALB2 PVS1/PS1/PM3/BS2 content, source discrepancies and
removal of the PALB2 FATKIN domain. No registry entry, version or guideline
filename changed.

---

## 7i. Cerebral Creatine remediation — complete

Round 13 (`69a9d62`) remediated GATM (GN025) and GAMT (GN026). The complete
pair comprised two core PDFs, three PVS1 artifacts, two exon workbooks, two
functional workbooks, two MAF slide decks, and a GAMT REVEL slide. All 11
artifacts were inventoried and inspected source-first: 41 core-PDF pages and
25 rendered Office pages, with raw workbook cells, PowerPoint XML, images,
notes, and flowchart topology checked where print layout obscured content.
The independent baseline was frozen before either local body was opened at
`/tmp/cerebral-creatine-round13.Ncii69/SOURCE_BASELINE.md`.

Recurring and high-impact findings:

- Both guidelines carried a full numeric PM3 point matrix even though neither
  distributed package ships it; both cores only refer to external SVI PM3
  guidance. The undistributed matrices were removed while the four permitted
  strengths and phasing requirements were retained.
- GATM's PVS1 appendix had collapsed a genuine shipped tree, losing the
  biologically relevant transcript gate, frequent-LoF/exon-absence routes,
  duplication outcomes, and conditional initiation branches. Its core assigns
  every initiation variant Moderate, while the shipped tree can assign N/A,
  Moderate, or Supporting. Both readings are now explicit, along with the
  strict `>10%`/`<10%` exact-10% gap.
- GAMT's flowchart had omitted both no/unknown-impact duplication routes and
  the proven non-tandem N/A route. Its workbook tab is literally `GAA_PVS1`,
  an apparent carry-over, though its content is GAMT-specific. GAMT's core
  also retains stale language routing noncanonical splice assay evidence to
  PS3 despite its v2 release notes and governing SVI paragraph moving RNA
  evidence under PVS1.
- Both functional workbooks say normal/abnormal thresholds were not provided,
  while their cores supply pathogenic `<`/`<=15%` and benign `>=30%` cutoffs.
  GATM additionally contains a wrong-gene `% ... GAMT activity` label and
  contradictory duplicate-versus-triplicate replicate statements. GAMT's
  three approved Supporting columns have questioned technical replicates and
  uneven validation controls. The local invented GATM 16%-29% indeterminate
  band was removed.
- Source typos and coordinate conflicts are preserved: GATM exon 9 prints
  `*985` while calling c.1272 the final stop nucleotide; GAMT exon 6 prints
  `*333` while calling c.711 the final stop nucleotide. GAMT's PVS1 sheet also
  spells `cryptic` as `crytpic`; GATM's slide spells `predicted` as `precited`.
- GAMT's local REVEL table had inferred exclusive upper bounds. The core gives
  Strong `>=0.932`, Moderate `0.773-0.932`, and Supporting `0.644-0.773`
  without endpoint operators for the ranges, producing an unresolved boundary
  ambiguity. The REVEL slide itself gives only P/LP n=20, VUS n=24, and B/LB
  n=3, with no cutoffs.
- Both MAF decks are now transcribed beyond their final thresholds, including
  prevalence assumptions, maximum allelic contributions, calculator values,
  and source annotations. Both specification DOIs and every physical source
  filename are recorded in the guidelines' dated correction histories.

Round 13 final gate: both exact registry-to-guideline mappings passed;
`plugins/vcep-spec/skills/vcep-spec/tests` passed 32/32;
`plugins/variant-classifier/skills/variant-classifier/tests` passed 17/17;
registry/disk consistency passed at 125 entries and 125 files with no missing
or orphaned guidelines; the registry SHA-256 remained
`491a29987395a72c76361d13091d6b5aefaeb7bd0c908550bfd7b6fa9342c8dc`;
`git diff --check` was clean; and the only version/filename mismatch remains
the pre-existing GN094 LZTR1 issue. `check_updates.py` was deliberately
skipped because this same-version correction did not touch the registry.

---

## 7j. Final 15-spec remediation — complete

Round 14 (`07cb4af`) remediated PAH (GN006), MYOC (GN019), DICER1 (GN024),
F8 (GN071), VHL (GN078), VWF type 2 (GN081), VWF type 2N (GN090), IDUA
(GN091), RPGR (GN106), KCNQ1 (GN112), RPE65 (GN120), RS1 (GN126), PIK3CD
(GN141), ABCA4 (GN164), and AIPL1 (GN208). The older shared `/tmp` source
directory was empty, so all 15 packages were freshly downloaded with pacing.
All 92 substantive physical files were present, non-empty, correctly typed,
and readable. Two pairs are byte-identical duplicates: PAH's two REVEL Word
files and ABCA4's two functional workbooks. The independent extraction produced
795 audit images and 70 contact-sheet montages; every montage was visually
reviewed before the local guideline bodies were compared.

Material findings:

- RPE65 and AIPL1 had expanded exact PS2/PM6 and PM3 attachment values
  `0.5/1/2/4` into invented ranges and an outer `>=` operator. VWF type 2N had
  likewise converted its four exact de novo totals to `>=` thresholds. The
  source prints no mapping for intermediate values, so all three now retain
  exact totals and state the gap.
- PAH's core PDF defines PP3_Supporting as REVEL `0.644–0.733`, while both
  byte-identical `PAH PP3 REVEL data explanation` files describe the relevant
  review bin as `0.644–0.773`. The contradiction is now explicit; the core's
  operative criterion is not silently extended.
- IDUA's local bibliography truncated Pejaver PMID `36413997` to `3641399`.
  MYOC named a nonexistent `..._v2.1.0.pdf` instead of the physical
  `ClinGen_ACMG_Specifications_MYOC_v2.1.pdf`. Both provenance errors are
  corrected.
- ABCA4 claimed the local Markdown was "Prepared by" the VCEP and assigned it
  a local January 2026 update date. Those unsupported authorship/update claims
  were removed; the panel is identified as the source of the distributed
  package, not the author of this transcription.
- Pilot workbooks (F8, KCNQ1, RPE65, PIK3CD), working curation tables (PAH),
  review-history documents (PIK3CD), SOPs and worked reports (RPGR) are now
  explicitly separated from normative criterion tables. Duplicate files are
  recorded as duplicates, not independent evidence.
- Every physical source filename is recorded in a dated correction history.
  The two VWF specifications preserve their shared artifacts but enforce the
  2A/2B/2M versus 2N rule-set boundary.

No registry entry, guideline filename, or ClinGen version changed. Round 14
added regression coverage for all 15 package manifests and the concrete
threshold/conflict/provenance repairs.

---

## 8. Loose ends unrelated to the completed remediation inventory

- **GN094 LZTR1 registry inconsistency**: source-first remediation confirmed
  that the governing distributed specification and registry version are
  `1.3.0`, while `guideline_file` remains `LZTR1_..._v2.0.0.md`. The mismatch
  predates round 4 and was deliberately not folded into a same-version content
  correction. Resolve the filename separately if desired; do not change the
  registry version to 2.0.0. Also 17 title/version mismatches remain, mostly
  benign mtDNA suffixes.
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

- **PAH PP3_Supporting upper bound.** The v2.0 core criterion prints REVEL
  `0.644–0.733`, but both distributed, byte-identical REVEL explanation Word
  files describe the 30-variant review bin as `0.644–0.773`. Please clarify
  whether `0.733` is intentional and how scores above 0.733 through 0.773
  should be handled.

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
- **PVS1 flowchart footnote markers are cited but never defined.** Markers
  `a`, `b`, `d` are affected in F9, IL7R, DCLRE1C, FOXN1, ACADVL, IL2RG and
  RAG2. The Limb Girdle preflight found the same problem for `a`, `b`, `c` and
  `d` in all seven ANO5/CAPN3/DYSF/SGCA/SGCB/SGCD/SGCG flowcharts; their
  speaker notes contain only template instructions, not definitions.
- **Limb Girdle PVS1 exact-10% gap.** All seven distributed gene-specific
  flowcharts use strict `>10%` and `<10%` branches with no path for a variant
  that removes exactly 10% of the protein.
- **Limb Girdle experimental-splice artifact is incomplete.** The byte-identical
  PNG shipped with all seven packages starts with an incoming arrow clipped at
  its left boundary; no visible criterion text is missing, but its off-canvas
  predecessor is unknowable. Markers `(d)` and `(e)` are also printed without
  definitions in any package.
- **SGCD/SGCG PS3 Moderate assay gap.** Both criteria PDFs permit
  PS3_Moderate for a clinically validated membrane-localization assay with at
  least 11 qualifying controls and direct readers to their gene workbooks.
  Those workbooks contain only Supporting Soheili assay instances (3 P/LP
  controls for SGCD, 4 for SGCG) and no populated Moderate assay. Is a
  Moderate assay attachment missing, or is the criterion intentionally
  prospective?
- **Congenital Myopathies missing segregation material.** NEB references an
  absent AR segregation Table 5. RYR1-AD and RYR1-AR both direct users to an
  Oza et al. segregation chart that is neither listed nor distributed. The
  ACTA1 AD/AR chart is present but supplies points without mapping them to PP1
  strengths, while its +5-point cap differs in form from the core Strong cap.
- **NEB incomplete/conflicting package.** The core lists transcript
  NM_001164507.1 while the PVS1 flowchart lists NM_001164507.2; its PM3 chart
  is an external link rather than a distributed artifact; its in-frame/exon-55
  PVS1 strengths conflict; and the functional workbook's exon-55 deletion
  coordinates differ from the core BA1 exclusion.
- **Congenital Myopathies functional-assay gaps.** ACTA1-AD says to stack "the
  two assays" but lists three Supporting categories. DNM2 proposes Supporting
  for populated assay entries while leaving every approval result blank.
  MTM1 approves 19 Supporting entries with zero validation controls and
  contains apparently cross-assigned threshold fields. RYR1-AD approves a
  reduced-calcium-release assay while its core criterion requires increased
  release. Which readings and assay instances are intended to be operative?
- **MTM1 classification combinations omit PVS1.** The criteria and flowchart
  define PVS1 at four strengths, but every published Pathogenic/Likely
  Pathogenic combination omits PVS1 and names PS2_Very Strong as the only Very
  Strong member. Is that omission intentional?
- **Cardiomyopathy MYBPC3 PVS1 gaps.** The shipped tree prints footnote markers
  `a`–`d` without definitions and uses strict `>10%`/`<10%` branches with no
  exactly-10% route. Its gray critical-region branches end at Strong while the
  same attachment says critical regions/domains have not been pre-defined.
  What evidence is intended to activate those gray routes?
- **Cardiomyopathy LoF/BP1 contradiction.** TNNI3, TNNT2, TPM1, ACTC1, MYL2,
  and MYL3 each say in PVS1 that LoF is not an established mechanism, but the
  shared BP1 comment says the current genes have null variants as a known
  mechanism. Is the BP1 rationale stale template text?
- **Cardiomyopathy external de novo mapping.** TNNI3, TNNT2, and TPM1 refer to
  SVI case-combination guidance and to assigned points but distribute no de
  novo attachment or numeric map. Which SVI version and point-to-strength
  conversion should curators use?
- **Cardiomyopathy PM4 Supporting gap.** All seven cores permit downgrading
  PM4 to Supporting based on predicted impact but provide no separate positive
  Supporting condition or numeric size/location/conservation threshold. Is
  the downgrade intentionally left to unrestricted clinical judgment?
- **Epilepsy Sodium Channel missing SCN1A PVS1 tree.** GN067 repeatedly says
  the tree is included, but its complete manifest contains no decision-tree
  artifact. Which gene-specific tree and version should curators use?
- **Epilepsy Sodium Channel full-gene-deletion conflict.** SCN2A, SCN3A,
  SCN8A, and SCN1B say full-gene deletion warrants Pathogenic in the core,
  assign PVS1 in the shipped tree, and give PVS1 eight points while the shipped
  points table calls 6-9 points Likely Pathogenic. Which outcome is intended?
- **Epilepsy Sodium Channel BA1 conflict.** SCN2A, SCN3A, and SCN8A each print
  strict `>0.02%` in VCEP prose but strict `>0.01%` plus a count floor in the
  Stand Alone block. Which threshold and qualifier set governs?
- **SCN1B PVS1 size labels.** The tree co-prints strict `>10%` with `>=200 aa`
  and `<10%` with `<200 aa` for a short protein, without AND/OR, and leaves
  exactly 10% unassigned. Is `200 aa` a copied threshold or intentional? Three
  rendered connectors also have incomplete raw endpoint bindings.
- **Monogenic Diabetes source conflicts.** HNF1A's autoimmune-phenotype bullets
  have no logical connector. HNF4A differs between core `c.1258` and tree
  `3' of c.1257`, inclusive/strict PP4 thresholds, and prints undefined PVS1
  markers `a`–`d`. GCK uses transcript `.5` in the header versus `.3` in PVS1
  and ships only one initiation-codon path. Across all three, the shared de
  novo table labels PM6 strengths although the gene cores make PM6 Not
  Applicable. Which readings and missing branch/footnote definitions are
  intended?
- **Platelet Disorders source conflicts and undefined flowchart notation.**
  GP1BA, GP1BB, and GP9 cores make PM6 Not Applicable or direct users to PS2,
  while the shared de novo attachment labels PM6 strengths, including
  Supporting. Their PVS1 slides also print undefined markers `a`–`d`, red-X
  symbols, and in some cases connectors whose raw endpoint bindings are
  incomplete. Which attachment precedence, marker definitions, and connector
  paths are intended?
- **GP9 PM3 rarity conflict.** The GP9-specific PM3 attachment says that all
  variants being evaluated must meet PM2, while the core permits a Pathogenic
  or Likely Pathogenic variant in trans without requiring rarity. Neither
  artifact declares precedence. Which condition governs?
- **Platelet Disorders hidden workbook material.** The shared functional-assay
  workbook contains 93 visible GPIX, 108 visible GPIBA, 77 visible GPIBB, and
  27 hidden `Mufti` populated cells. The hidden sheet is unrelated VWF/FVIII
  working material. Was it intentionally distributed, and should curators
  ignore it?
- **HHT PVS1 tree gaps.** ACVRL1 supplies no role-unknown route for removal of
  10% or more. ENG supplies no critical-region or ≥10% route for non-NMD
  nonsense/frameshift and frame-disrupting splice variants; its other branches
  use strict `>10%`/`<10%`, leaving exact 10% open. Both deletion trees omit
  the outcome when the deleted exon is absent from biologically relevant
  transcripts. The decks also contain 13/51 and 15/51 incomplete raw connector
  endpoint bindings. Which paths and endpoints are intended?
- **HHT functional-assay conflicts.** The shared workbook proposes unqualified
  `PS3; BS3_Supporting` for all five mRNA rows, including two entries not
  described as splicing, and proposes BS3_Supporting for protein-expression
  rows although the core excludes normal expression as benign evidence. It
  also overlaps normal/abnormal tubulogenesis time bands and omits exactly
  0.01% from its somatic frequency thresholds. Which artifact and boundaries
  govern, and what conversion should be used when multiple Supporting assays
  are concordant?
- **RASopathy shared scoring conflicts.** The PDF bodies give BS2 Strong at
  -4 while the distributed image gives -3. The bodies give BP2/BP5 tiers
  `>=(-4)`/`>=(-2)`/`>=(-1)`, while the shared image gives -3/N/A/-1 with no
  operators. The PS2/PM6 image also supplies strengths omitted from the body
  criterion blocks. Which artifact is authoritative?
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
5. Full test suite: `plugins/vcep-spec/skills/vcep-spec/tests` (34) and
   `plugins/variant-classifier/skills/variant-classifier/tests` (17).
6. **Sanity-check outputs against their own source folder** — after the ACADVL
   near-miss, confirm no guideline contains content its package does not have.

**Registry state at writing:** 125 entries, 125 files, no orphans, all
filenames normalised `x.y.z`, live registry in sync (0 new, 0 outdated).
GN094 LZTR1 is the only `version`/`guideline_file` mismatch and is
pre-existing (§8).

**Corrections that do not change the ClinGen version** (rounds 2–14 were all of
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

For rounds 2–14 the durable changelogs are **in the guidelines themselves**,
under dated "Document corrections" entries. The remediation commits are
`2f9674b` (round 2), `4c91f2c` (round 3), `3b62aeb` (round 4), `78ad52b`
(round 5), `0bad381` (round 6), `16212de` (round 7), `bb87729`
(round 8), `f298ac8` (round 9), `983d931` (round 10), `efe4f3d`
(round 11), `71c56ff` (round 12), `69a9d62` (round 13), and `07cb4af`
(round 14). Rounds 5–14
source-first scratch drafts live in isolated `/tmp` directories and are ephemeral. Prefer the in-guideline
pattern going forward: a finding recorded only in `/tmp` is a finding you will
lose.

---

## 13. Rounds 2–14 summary

**Round 2 — `2f9674b`** — FBN1 (GN022), GUCY2D (GN167), SERPINC1 (GN084).
Closed the `ranges` lead (§1). FBN1 turned out to carry two fabricated
appendices, including the mode-1b PVS1 graft that contradicted its own body
table. All three had lost the SVI heterogeneity-row cap footnote.

**Round 3 — `4c91f2c`** — the eight zero-supplement specs. Clean: RYR1
(GN012), Brain Malformations/AKT3 (GN018), the GN014 nuclear set
(ETHE1/PDHA1/POLG/SLC19A3), mtDNA (GN015), Platelet Disorders (GN011).
Defective: LDLR (GN013), GAA (GN010), Hearing Loss (GN023) — all three caught
by the §2a signal.

**Round 4 — `3b62aeb`** — all 16 RASopathy specs:
SHOC2 (GN038), NRAS (GN039), RAF1 (GN040), SOS1 (GN041), SOS2 (GN042),
PTPN11 (GN043), KRAS (GN044), MAP2K1 (GN045), HRAS (GN046), RIT1 (GN047),
MAP2K2 (GN048), BRAF (GN049), MRAS (GN087), LZTR1 (GN094), RRAS2 (GN127)
and PPP1CB (GN128). Each was drafted source-first from its complete package,
then remediated in place. The registry was not changed and no file was renamed.

Recurring panel findings:

- The PDF body and distributed images disagree: BS2 Strong is -4 versus -3;
  BP2/BP5 are PDF `>=(-4)`/`>=(-2)`/`>=(-1)` versus image -3/N/A/-1.
  Both readings are now reported; invented image comparators were removed.
- The PS2/PM6 image adds PS2_Supporting and PM6_VeryStrong to criterion blocks
  that omit them.
- Functional workbooks contained omitted assay details, miscategorised
  validation controls and, in several local guidelines, generic or fabricated
  assay prose. Source-contradicting content was removed; plausible but
  unverifiable gene-specific history was retained only under the required
  warning banner.
- Analogous-residue files were frequently working sheets or image alignments,
  not authoritative exhaustive lookup tables. Their limitations are now
  explicit.
- BP1 repeatedly cites dosage-sensitivity material that is not distributed.
- LZTR1's apparently generic PVS1 and inheritance flowcharts are genuine
  shipped artifacts. Its source is v1.3; the pre-existing v2.0.0 filename
  mismatch remains deliberately unresolved (§8).

Round 4 final gate: all 16 `check_vcep_spec.py` lookups passed;
`plugins/vcep-spec/skills/vcep-spec/tests` passed 26/26;
`plugins/variant-classifier/skills/variant-classifier/tests` passed 17/17;
`git diff --check` was clean. The remediation commit contains the 16 guidelines
and the contemporaneous handoff update.

**Round 5 — `78ad52b`** — all seven Limb Girdle specs: ANO5 (GN188), CAPN3
(GN187), DYSF (GN180), SGCA (GN189), SGCB (GN184), SGCD (GN186), and SGCG
(GN185). Every package was complete and source-first drafting covered all 60
substantive artifacts. Recurring defects were omitted PVS1 exon-presence
gates, operative transcription of struck-through flowchart paths, incorrect
experimental-splice routing, stripped shared-table footnotes/qualifications,
partial benign-exception and PS3 workbook transcription, invented
classification endpoint comparators, and unsupplied provenance. SGCA also had
a generic combination-rule graft. Full findings and unresolved source caveats
are in §7a.

Round 5 final gate: all seven `check_vcep_spec.py` lookups passed;
`plugins/vcep-spec/skills/vcep-spec/tests` passed 26/26;
`plugins/variant-classifier/skills/variant-classifier/tests` passed 17/17;
registry/disk consistency passed at 125 entries and 125 files with no missing
or orphaned guidelines; the registry SHA-256 remained
`491a29987395a72c76361d13091d6b5aefaeb7bd0c908550bfd7b6fa9342c8dc`;
and `git diff --check` was clean. The only version/filename mismatch remains
the pre-existing GN094 LZTR1 issue.

**Round 6 — `0bad381`** — all seven Congenital Myopathies specs: NEB (GN146),
ACTA1-AD (GN147), DNM2 (GN148), MTM1 (GN149), RYR1-AD (GN150), ACTA1-AR
(GN169), and RYR1-AR (GN179). The complete 24-artifact panel was preflighted,
then every guideline was drafted source-first. Recurring defects included
package-absent generic PS2/PM6, PM3 and PP1 tables; omitted PVS1 transcript and
branch gates; incomplete assay workbooks; missing segregation artifacts;
unmapped point totals; comparator inventions; and unsupplied provenance. MTM1
contained a fabricated mouse-model assay row. Full findings and upstream
questions are in §7b and §9.

Round 6 final gate: all seven exact registry-to-guideline mappings passed;
`plugins/vcep-spec/skills/vcep-spec/tests` passed 26/26;
`plugins/variant-classifier/skills/variant-classifier/tests` passed 17/17; all
24 source filenames appeared in the dated correction histories; registry/disk
consistency passed at 125 entries and 125 files with no missing or orphaned
guidelines; the registry SHA-256 remained
`491a29987395a72c76361d13091d6b5aefaeb7bd0c908550bfd7b6fa9342c8dc`;
and `git diff --check` was clean. The only version/filename mismatch remains
the pre-existing GN094 LZTR1 issue.

**Round 7 — `16212de`** — all seven Cardiomyopathy specs: MYBPC3 (GN095),
TNNI3 (GN098), TNNT2 (GN099), TPM1 (GN100), ACTC1 (GN101), MYL2 (GN102),
and MYL3 (GN103). The complete 15-PDF panel was preflighted and drafted
source-first. Recurring defects were undistributed de novo point matrices,
inferred PM4/BS3 qualification logic, incomplete PS4 examples, stripped
MYBPC3 PVS1 routes/markers, source contradictions silently harmonized, and
missing DOI provenance. Full findings and upstream questions are in §7c and
§9.

Round 7 final gate: all seven exact registry-to-guideline mappings passed;
`plugins/vcep-spec/skills/vcep-spec/tests` passed 26/26;
`plugins/variant-classifier/skills/variant-classifier/tests` passed 17/17 plus
8 subtests; all 15 source filenames appeared in the dated correction
histories; registry/disk consistency passed at 125 entries and 125 files with
no missing or orphaned guidelines; the registry SHA-256 remained
`491a29987395a72c76361d13091d6b5aefaeb7bd0c908550bfd7b6fa9342c8dc`;
and `git diff --check` was clean. The only version/filename mismatch remains
the pre-existing GN094 LZTR1 issue.

**Round 8 — `bb87729`** — all five Epilepsy Sodium Channel specs: SCN1A
(GN067), SCN2A (GN068), SCN3A (GN069), SCN8A (GN070), and SCN1B (GN076).
The complete 32-artifact panel was preflighted and drafted source-first.
Recurring defects were incomplete/reversed PVS1 topology, invented comparator
operators and de novo pooling, overgeneralized PS1 splice rules, silently
resolved BA1/transcript/full-deletion conflicts, generic or superseded
combination recipes, and imprecise attachment provenance. SCN1A's advertised
PVS1 tree is absent; SCN1B's shipped tree contains incompatible percentage/
absolute-length labels. Full findings and unresolved source caveats are in
§7d and §9.

Round 8 final gate: all five exact registry-to-guideline mappings passed;
`plugins/vcep-spec/skills/vcep-spec/tests` passed 26/26;
`plugins/variant-classifier/skills/variant-classifier/tests` passed 17/17; all
32 advertised source filenames appeared in the dated correction histories;
registry/disk consistency passed at 125 entries and 125 files with no missing
or orphaned guidelines; the registry SHA-256 remained
`491a29987395a72c76361d13091d6b5aefaeb7bd0c908550bfd7b6fa9342c8dc`;
the independent five-spec scratch review passed; and `git diff --check` was
clean. The only version/filename mismatch remains the pre-existing GN094
LZTR1 issue.

**Round 9 — `f298ac8`** — all three Monogenic Diabetes specs: HNF1A
(GN017), HNF4A (GN085), and GCK (GN086). The complete 12-PDF panel was
preflighted and drafted source-first. Recurring defects were incomplete PVS1
and functional-tree topology, altered shared de novo titles/cells/footnotes,
generic PM6 instructions, comparator and typography normalization, silently
interpreted source conflicts, and unclear editorial-appendix provenance. Full
findings and unresolved source caveats are in §7e and §9.

Round 9 final gate: all three exact registry-to-guideline mappings passed;
`check_updates.py` reported 0 new and 0 outdated released specifications;
`plugins/vcep-spec/skills/vcep-spec/tests` passed 26/26;
`plugins/variant-classifier/skills/variant-classifier/tests` passed 17/17; all
12 advertised source filenames appeared in the dated correction histories;
registry/disk consistency passed at 125 entries and 125 files with no missing
or orphaned guidelines; the registry SHA-256 remained
`491a29987395a72c76361d13091d6b5aefaeb7bd0c908550bfd7b6fa9342c8dc`;
the independent three-spec cross-panel scratch review passed; and
`git diff --check` was clean. The only version/filename mismatch remains the
pre-existing GN094 LZTR1 issue.

**Round 10 — `983d931`** — all three remaining Platelet Disorders specs:
GP1BA (GN079), GP1BB (GN082), and GP9 (GN083). The complete 18-file panel was
preflighted and drafted source-first. Recurring defects were collapsed or
reversed PVS1 topology, altered PS2 and PM3 tables, generic or invented PM3
categories, normalized source typography, omitted conflicting-evidence
tables, incomplete workbook provenance, and silently resolved contradictions.
Full findings and unresolved source caveats are in §7f and §9.

Round 10 final gate: all three exact registry-to-guideline mappings passed;
`check_updates.py` reported 0 new and 0 outdated released specifications;
`plugins/vcep-spec/skills/vcep-spec/tests` passed 26/26;
`plugins/variant-classifier/skills/variant-classifier/tests` passed 17/17; all
18 advertised source filenames appeared in the dated correction histories;
registry/disk consistency passed at 125 entries and 125 files with no missing
or orphaned guidelines; the registry SHA-256 remained
`491a29987395a72c76361d13091d6b5aefaeb7bd0c908550bfd7b6fa9342c8dc`;
the independent three-spec cross-panel scratch review passed; and
`git diff --check` was clean. The only version/filename mismatch remains the
pre-existing GN094 LZTR1 issue.

**Round 11 — `efe4f3d`** — both Hereditary Hemorrhagic Telangiectasia specs:
ACVRL1 (GN135) and ENG (GN136). The complete eight-artifact pair was
preflighted and drafted source-first. Recurring defects were generic or
invented PVS1 topology, changed strict comparators, incomplete phenotype and
functional-attachment transcription, unsourced assay citations, compressed
classification member lists, and missing DOI provenance. Full findings and
unresolved source caveats are in §7g and §9.

Round 11 final gate: both exact registry-to-guideline mappings passed;
`check_updates.py` reported 0 new and 0 outdated released specifications;
`plugins/vcep-spec/skills/vcep-spec/tests` passed 28/28;
`plugins/variant-classifier/skills/variant-classifier/tests` passed 17/17 plus
8 subtests; all eight advertised source filenames appeared in the dated
correction histories; the shared 39-instance workbook transcription matched
both byte-identical source files; registry/disk consistency passed at 125
entries and 125 files with no missing or orphaned guidelines; the registry
SHA-256 remained
`491a29987395a72c76361d13091d6b5aefaeb7bd0c908550bfd7b6fa9342c8dc`;
and `git diff --check` was clean. The only version/filename mismatch remains
the pre-existing GN094 LZTR1 issue.

**Round 12 — `71c56ff`** — both HBOP Cancer specs: ATM (GN020) and PALB2
(GN077). The complete seven-artifact pair was preflighted and drafted
source-first, including ATM's image-only PVS1 lists and workbook, and PALB2's
nested Word tables and six embedded figures. Recurring defects were omitted
operative attachment tables, a reversed workbook threshold, compressed assay
transcription, an attachment carry-over promoted into a false PALB2 FATKIN
domain, missing DOI provenance and silently reconciled package conflicts. Full
findings and unresolved source caveats are in §7h.

Round 12 final gate: both exact registry-to-guideline mappings passed;
`plugins/vcep-spec/skills/vcep-spec/tests` passed 30/30;
`plugins/variant-classifier/skills/variant-classifier/tests` passed 17/17;
registry/disk consistency passed at 125 entries and 125 files with no missing
or orphaned guidelines; the registry was byte-unchanged; `git diff --check`
was clean; and the only version/filename mismatch remains the pre-existing
GN094 LZTR1 issue. `check_updates.py` was deliberately skipped because this
same-version correction did not touch the registry.

**Round 13 — `69a9d62`** — both Cerebral Creatine specs: GATM (GN025) and
GAMT (GN026). The complete 11-artifact pair was inspected source-first,
including both gene-specific PVS1 artifacts, exon and assay workbooks, MAF
decks, and the GAMT REVEL plot. Recurring defects were undistributed PM3
matrices, incomplete PVS1 routes, an invented assay activity band, normalized
source-coordinate typos, inferred REVEL endpoint operators, incomplete MAF
and functional transcription, missing DOI provenance, and silently reconciled
core/appendix conflicts. Full findings and unresolved source caveats are in
§7i.

Round 13 final gate: both exact registry-to-guideline mappings passed;
`plugins/vcep-spec/skills/vcep-spec/tests` passed 32/32;
`plugins/variant-classifier/skills/variant-classifier/tests` passed 17/17;
registry/disk consistency passed at 125 entries and 125 files with no missing
or orphaned guidelines; the registry was byte-unchanged; `git diff --check`
was clean; and the only version/filename mismatch remains the pre-existing
GN094 LZTR1 issue. `check_updates.py` was deliberately skipped because this
same-version correction did not touch the registry.

**Round 14 — `07cb4af`** — the final 15 specifications: PAH (GN006), MYOC
(GN019), DICER1 (GN024), F8 (GN071), VHL (GN078), VWF type 2 (GN081), VWF
type 2N (GN090), IDUA (GN091), RPGR (GN106), KCNQ1 (GN112), RPE65 (GN120),
RS1 (GN126), PIK3CD (GN141), ABCA4 (GN164), and AIPL1 (GN208). All 92
substantive physical artifacts were freshly downloaded, structurally checked,
independently extracted, and visually audited before local comparison.
Material repairs were unsupported exact-value interpolation in three specs, a
PAH core/attachment REVEL conflict, an IDUA PMID truncation, a MYOC physical
filename error, and fabricated ABCA4 local-document provenance. Every package
manifest and source boundary is now durable in the guideline corrections and
regression suite. Full findings are in §7j.

Round 14 final gate: all 15 exact registry-to-guideline mappings passed;
`plugins/vcep-spec/skills/vcep-spec/tests` passed 34/34;
`plugins/variant-classifier/skills/variant-classifier/tests` passed 17/17;
all 92 physical source filenames appeared in the dated correction histories;
registry/disk consistency passed at 125 entries and 125 files with no missing
or orphaned guidelines; the registry SHA-256 remained
`491a29987395a72c76361d13091d6b5aefaeb7bd0c908550bfd7b6fa9342c8dc`;
`git diff --check` was clean; and the only version/filename mismatch remains
the pre-existing GN094 LZTR1 issue. `check_updates.py` was deliberately
skipped because this same-version correction did not touch the registry.

Incidental finding, harmless but confusing: the downloader mislabels the two
Mitochondrial specs by gene — GN014's folder is `GN014-CDKL5` and GN015's is
`GN015-UNKNOWN`. **The PDFs themselves are correct** (GN014's keywords list
SLC19A3/PDHA1/POLG/ETHE1; GN015 is the mtDNA document). The registry is right
and needs no change; only the ephemeral download folder names are wrong. Do
not "fix" a registry entry on the strength of a source folder name.

---

## 14. Suggested skills for future updates

- Use `pdf:pdf` for complete page rendering and visual verification of every
  source PDF whose tables, strikeouts, footnotes, or arrow relationships matter.
- A future session handling new or bumped specifications should work panel-first
  and load only the artifact skills its packages require. Use `documents:documents`,
  `presentations:Presentations`, and `spreadsheets:Spreadsheets` when DOCX,
  PPTX, or XLSX artifacts are present; inspect raw Office XML/media when
  renderers omit text, notes, or connector topology.
- Update this handoff only if a future release creates a new remediation batch;
  the present inventory is complete.
