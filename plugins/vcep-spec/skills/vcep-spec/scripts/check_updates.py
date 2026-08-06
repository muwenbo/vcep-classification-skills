#!/usr/bin/env python3
"""
Compare the live ClinGen CSpec registry against the local VCEP registry.

Reports released specifications that are missing locally, and specifications
whose upstream version is newer than the local copy.

Usage:
    python check_updates.py                    Show new and updated specs
    python check_updates.py --json             Machine-readable output
    python check_updates.py --new-only         Only specs missing locally
    python check_updates.py --updated-only     Only version bumps
    python check_updates.py --registry <path>  Use a specific local registry

Exit codes:
    0  local registry is up to date
    1  updates are available
    2  could not reach or parse the live registry

Dependencies:
    requests
"""

import argparse
import json
import re
import sys
from pathlib import Path

REGISTRY_URL = "https://cspec.genome.network/cspec/ui/svi/"
SPEC_URL = "https://cspec.genome.network/cspec/ui/svi/doc/{}"

# plugins/vcep-spec/skills/vcep-spec/scripts/ -> plugins/
PLUGINS_DIR = Path(__file__).resolve().parents[4]
DEFAULT_REGISTRY = (PLUGINS_DIR / "variant-classifier" / "skills" / "variant-classifier"
                    / "data" / "vcep_registry.json")


def normalize_version(version):
    """
    Normalize a version to a comparable 3-tuple.

    CSpec versions are inconsistent - the same spec may say "1.0" in one field
    and "1.0.0" in another - so pad to three components before comparing.
    """
    parts = re.findall(r"\d+", str(version))
    while len(parts) < 3:
        parts.append("0")
    return tuple(int(p) for p in parts[:3])


def fetch_live_specs():
    """
    Fetch the live registry.

    The registry index embeds the full specification list as a `svisData`
    JavaScript array; that is the same payload served by the page's JSON
    download link, and it carries the released flag and gene labels.
    """
    import requests

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"}
    response = requests.get(REGISTRY_URL, headers=headers, timeout=60)
    response.raise_for_status()

    marker = response.text.find("svisData")
    if marker == -1:
        raise ValueError("could not find svisData in the registry page")
    start = response.text.index("[", marker)
    specs, _ = json.JSONDecoder().raw_decode(response.text[start:])
    return specs


def load_local_registry(path):
    """Map spec_id -> local entry. A spec_id may appear more than once
    (multi-gene panels split into per-gene entries); the first wins, since
    all such entries share a version."""
    with open(path) as f:
        registry = json.load(f)

    local = {}
    for entry in registry["specifications"]:
        local.setdefault(entry["spec_id"], entry)
    return local


def compare(live_specs, local):
    """Diff live released specs against the local registry."""
    new, updated = [], []

    for spec in live_specs:
        if not spec.get("isReleased"):
            continue

        spec_id = spec["sviId"]
        live_version = spec.get("version", "")
        genes = [g["label"] for g in spec.get("genes", [])]
        record = {
            "spec_id": spec_id,
            "genes": genes,
            "vcep_name": spec.get("vcepName", ""),
            "live_version": live_version,
            "title": spec.get("title", ""),
            "specification_url": SPEC_URL.format(spec_id),
        }

        if spec_id not in local:
            new.append(record)
        else:
            local_version = local[spec_id].get("version", "")
            if normalize_version(live_version) != normalize_version(local_version):
                record["local_version"] = local_version
                updated.append(record)

    new.sort(key=lambda r: r["spec_id"])
    updated.sort(key=lambda r: r["spec_id"])
    return new, updated


def format_genes(genes):
    return ", ".join(genes) if genes else "-"


def print_report(new, updated, local_count, released_count, show_new, show_updated):
    print(f"Live registry: {released_count} released specifications")
    print(f"Local registry: {local_count} specifications\n")

    if show_new:
        print(f"NEW - released upstream, missing locally: {len(new)}")
        for r in new:
            print(f"  {r['spec_id']}  {format_genes(r['genes'])[:38]:<38} "
                  f"v{r['live_version']:<8} {r['vcep_name']}")
        print()

    if show_updated:
        print(f"UPDATED - newer version upstream: {len(updated)}")
        for r in updated:
            print(f"  {r['spec_id']}  {format_genes(r['genes'])[:30]:<30} "
                  f"local v{r['local_version']:<8} -> live v{r['live_version']:<8} "
                  f"{r['vcep_name']}")
        print()

    total = (len(new) if show_new else 0) + (len(updated) if show_updated else 0)
    if total == 0:
        print("Local registry is up to date.")
    else:
        print(f"Download with: /vcep-spec <GN###>")


def main():
    parser = argparse.ArgumentParser(
        description="Compare the live ClinGen CSpec registry against the local registry",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                       Show new and updated specifications
  %(prog)s --new-only            Only specs released upstream but missing locally
  %(prog)s --json                Machine-readable output
        """,
    )
    parser.add_argument("--registry", default=str(DEFAULT_REGISTRY),
                        help="Path to vcep_registry.json")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--new-only", action="store_true",
                        help="Only report specs missing locally")
    parser.add_argument("--updated-only", action="store_true",
                        help="Only report version bumps")

    args = parser.parse_args()

    registry_path = Path(args.registry).expanduser()
    if not registry_path.exists():
        print(f"Error: local registry not found: {registry_path}", file=sys.stderr)
        sys.exit(2)

    try:
        live_specs = fetch_live_specs()
    except ImportError:
        print("Error: requests is required (pip install requests)", file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"Error fetching live registry: {e}", file=sys.stderr)
        sys.exit(2)

    local = load_local_registry(registry_path)
    new, updated = compare(live_specs, local)

    show_new = not args.updated_only
    show_updated = not args.new_only

    if args.json:
        output = {
            "live_released": sum(1 for s in live_specs if s.get("isReleased")),
            "local_count": len(local),
        }
        if show_new:
            output["new"] = new
        if show_updated:
            output["updated"] = updated
        print(json.dumps(output, indent=2))
    else:
        print_report(new, updated, len(local),
                     sum(1 for s in live_specs if s.get("isReleased")),
                     show_new, show_updated)

    pending = (len(new) if show_new else 0) + (len(updated) if show_updated else 0)
    sys.exit(1 if pending else 0)


if __name__ == "__main__":
    main()
