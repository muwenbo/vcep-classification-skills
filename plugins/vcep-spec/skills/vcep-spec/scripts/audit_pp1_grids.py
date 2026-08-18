#!/usr/bin/env python3
"""
Audit PP1 co-segregation LOD grids across all VCEP guidelines.

Background (handoff §8): the recessive Oza et al. "Table 4b" segregation grid
(a 0-10 x 0-10 affected x unaffected LOD lookup) was silently truncated in
several specs before the 2026-08 remediation. A naive `truncat` grep is
useless because it matches the ACMG BP1 boilerplate "Truncating variants...".

This audit is structural instead: it finds every guideline that INVOKES the
Oza/SVI segregation grid and reports whether a complete 11x11 grid is present.
Specs flagged SUSPECT need a human to confirm whether they legitimately use a
different framework (e.g. the Biesecker points chart, a direct affected-count
rule, or a package that ships no grid at all) or are genuinely truncated.

This prints a report and always exits 0; it is an analysis aid, not a gate.
The concrete guarantees are locked by the regression tests in
tests/test_audited_guideline_repairs.py (PP1SegregationGridTests).

Usage:
    python audit_pp1_grids.py
"""
import os
import re
import sys
from pathlib import Path

GDIR = (
    Path(__file__).resolve().parents[5]
    / "plugins" / "variant-classifier" / "skills" / "variant-classifier"
    / "data" / "vcep-guidelines"
)

# Signals that a guideline relies on the Oza/SVI recessive LOD grid lookup.
INVOKE_PATTERNS = [
    r"30311386",                                          # Oza et al. PMID
    r"Table\s*4b",
    r"affected\s+segregations?.*unaffected\s+segregations?",
    r"LOD score grid",
    r"unaffected recessive segregation",
]


def has_complete_grid(text):
    """Return True if a complete 0-10 x 0-10 Oza grid is present: a header row
    0..10 followed by 11 data rows labelled 0..10."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip().strip("*") for c in line.strip().strip("|").split("|")]
        nums = [c for c in cells if re.fullmatch(r"\d+", c)]
        if nums[:11] != [str(n) for n in range(11)]:
            continue
        labels = []
        j = i + 1
        while j < len(lines) and lines[j].strip().startswith("|"):
            rcells = [c.strip().strip("*") for c in lines[j].strip().strip("|").split("|")]
            if set("".join(rcells)) <= set("-: "):
                j += 1
                continue
            if re.fullmatch(r"\d+", rcells[0]):
                labels.append(rcells[0])
            else:
                break
            j += 1
        if labels == [str(n) for n in range(11)]:
            return True
    return False


def main():
    rows = []
    for path in sorted(GDIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        invoked = [p for p in INVOKE_PATTERNS if re.search(p, text, re.I | re.S)]
        if not invoked:
            continue
        ok = has_complete_grid(text)
        rows.append((path.name, len(invoked), ok))

    print(f"{'guideline':70} {'signals':>7}  grid")
    for name, nsig, ok in rows:
        status = "complete" if ok else "SUSPECT (no full 11x11 grid) <-- review"
        print(f"{name:70} {nsig:>7}  {status}")
    suspect = sum(1 for _, _, ok in rows if not ok)
    print(f"\n{len(rows)} guidelines invoke the PP1 LOD grid; {suspect} to review.")
    print("A SUSPECT is only a defect if the spec claims to reproduce the "
          "recessive grid. Confirm against the distributed package.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
