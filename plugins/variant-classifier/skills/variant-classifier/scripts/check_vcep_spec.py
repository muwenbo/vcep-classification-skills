#!/usr/bin/env python3
"""
VCEP Specification Checker

Check if a gene has a ClinGen VCEP (Variant Curation Expert Panel) specification.
Looks up the local registry and finds corresponding guideline files.

Usage:
    python check_vcep_spec.py BRCA1
    python check_vcep_spec.py TP53 --json
    python check_vcep_spec.py ADA -o spec_info.json
"""

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional


# Default paths relative to this script
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR.parent / "data"
REGISTRY_FILE = DATA_DIR / "vcep_registry.json"
GUIDELINES_DIR = DATA_DIR / "vcep-guidelines"


@dataclass
class VCEPSpec:
    """VCEP Specification information"""
    spec_id: str
    vcep_name: str
    title: str
    gene: str
    hgnc_id: str
    disease_condition: str
    mondo_ids: List[str]
    inheritance: str
    status: str
    version: str
    specification_url: str
    guideline_file: str
    guideline_path: Optional[str] = None
    guideline_exists: bool = False
    all_genes: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization"""
        return {
            "spec_id": self.spec_id,
            "vcep_name": self.vcep_name,
            "title": self.title,
            "gene": self.gene,
            "all_genes": self.all_genes,
            "hgnc_id": self.hgnc_id,
            "disease_condition": self.disease_condition,
            "mondo_ids": self.mondo_ids,
            "inheritance": self.inheritance,
            "status": self.status,
            "version": self.version,
            "specification_url": self.specification_url,
            "guideline_file": self.guideline_file,
            "guideline_path": self.guideline_path,
            "guideline_exists": self.guideline_exists,
        }


class VCEPRegistry:
    """Registry of ClinGen VCEP specifications"""

    def __init__(self, registry_file: Path = REGISTRY_FILE,
                 guidelines_dir: Path = GUIDELINES_DIR):
        self.registry_file = Path(registry_file)
        self.guidelines_dir = Path(guidelines_dir)
        self._specs: List[VCEPSpec] = []
        self._gene_index: Dict[str, List[VCEPSpec]] = {}
        self._loaded = False

    def _ensure_loaded(self):
        """Load registry if not already loaded"""
        if not self._loaded:
            self.load()

    def load(self) -> None:
        """Load and parse the VCEP registry JSON"""
        if not self.registry_file.exists():
            raise FileNotFoundError(f"Registry file not found: {self.registry_file}")

        self._specs = []
        self._gene_index = {}

        with open(self.registry_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        for entry in data.get("specifications", []):
            genes_list = entry.get("genes", [])
            all_gene_symbols = [g["symbol"] for g in genes_list]
            gene_field = "; ".join(all_gene_symbols)
            hgnc_field = "; ".join(g.get("hgnc_id", "") for g in genes_list)

            guideline_file = entry.get("guideline_file", "")
            guideline_path = str(self.guidelines_dir / guideline_file) if guideline_file else None
            guideline_exists = guideline_path is not None and Path(guideline_path).exists()

            spec = VCEPSpec(
                spec_id=entry.get("spec_id", ""),
                vcep_name=entry.get("vcep_name", ""),
                title=entry.get("title", ""),
                gene=gene_field,
                all_genes=all_gene_symbols,
                hgnc_id=hgnc_field,
                disease_condition=entry.get("disease_condition", ""),
                mondo_ids=entry.get("mondo_ids", []),
                inheritance=entry.get("inheritance", ""),
                status=entry.get("status", ""),
                version=entry.get("version", ""),
                specification_url=entry.get("specification_url", ""),
                guideline_file=guideline_file,
                guideline_path=guideline_path,
                guideline_exists=guideline_exists,
            )

            self._specs.append(spec)

            # Index by each gene
            for gene_symbol in all_gene_symbols:
                gene_upper = gene_symbol.upper()
                if gene_upper not in self._gene_index:
                    self._gene_index[gene_upper] = []
                self._gene_index[gene_upper].append(spec)

        self._loaded = True

    def find_spec(self, gene: str) -> List[VCEPSpec]:
        """
        Find VCEP specifications for a gene.

        Args:
            gene: Gene symbol (case-insensitive)

        Returns:
            List of matching VCEPSpec objects (may be multiple for
            different inheritance patterns or disease conditions)
        """
        self._ensure_loaded()
        return self._gene_index.get(gene.upper(), [])

    def has_spec(self, gene: str) -> bool:
        """Check if gene has any VCEP specification"""
        return len(self.find_spec(gene)) > 0

    def get_all_genes(self) -> List[str]:
        """Get list of all genes with VCEP specifications"""
        self._ensure_loaded()
        return sorted(self._gene_index.keys())

    def get_all_specs(self) -> List[VCEPSpec]:
        """Get all VCEP specifications"""
        self._ensure_loaded()
        return self._specs


def load_registry(registry_file: Path = REGISTRY_FILE) -> VCEPRegistry:
    """Load the VCEP registry from file"""
    registry = VCEPRegistry(registry_file)
    registry.load()
    return registry


def find_spec(gene: str, registry: Optional[VCEPRegistry] = None) -> List[VCEPSpec]:
    """
    Find VCEP specifications for a gene.

    Args:
        gene: Gene symbol
        registry: Optional pre-loaded registry

    Returns:
        List of matching specifications
    """
    if registry is None:
        registry = load_registry()
    return registry.find_spec(gene)


def get_guideline_path(spec: VCEPSpec) -> Optional[str]:
    """
    Get the path to the guideline markdown file for a specification.

    Returns:
        Path to guideline file if it exists, None otherwise
    """
    if spec.guideline_exists:
        return spec.guideline_path
    return None


def format_spec_summary(spec: VCEPSpec) -> str:
    """Format a specification for human-readable display"""
    lines = [
        f"VCEP: {spec.vcep_name}",
        f"Spec ID: {spec.spec_id}",
        f"Gene(s): {spec.gene}",
        f"Disease: {spec.disease_condition}",
        f"Inheritance: {spec.inheritance}",
        f"Version: {spec.version}",
        f"Status: {spec.status}",
        f"URL: {spec.specification_url}",
    ]

    if spec.guideline_exists:
        lines.append(f"Guideline: {spec.guideline_file} (exists)")
    else:
        lines.append(f"Guideline: {spec.guideline_file} (NOT FOUND - user must provide)")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Check if a gene has a ClinGen VCEP specification",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s BRCA1
  %(prog)s TP53 --json
  %(prog)s ADA -o spec_info.json
  %(prog)s --list-all
        """,
    )
    parser.add_argument(
        "gene",
        nargs="?",
        help="Gene symbol to look up"
    )
    parser.add_argument(
        "--json", "-j",
        action="store_true",
        help="Output as JSON"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output file path"
    )
    parser.add_argument(
        "--list-all",
        action="store_true",
        help="List all genes with VCEP specifications"
    )
    parser.add_argument(
        "--registry",
        type=Path,
        default=REGISTRY_FILE,
        help=f"Path to registry JSON file (default: {REGISTRY_FILE})"
    )

    args = parser.parse_args()

    try:
        registry = load_registry(args.registry)

        # List all genes mode
        if args.list_all:
            genes = registry.get_all_genes()
            if args.json:
                output = json.dumps({"genes": genes, "count": len(genes)}, indent=2)
            else:
                output = f"Genes with VCEP specifications ({len(genes)}):\n"
                output += "\n".join(f"  {g}" for g in genes)
        elif args.gene:
            # Single gene lookup
            specs = find_spec(args.gene, registry)

            if not specs:
                if args.json:
                    output = json.dumps({
                        "gene": args.gene,
                        "has_vcep": False,
                        "specifications": []
                    }, indent=2)
                else:
                    output = f"No VCEP specification found for {args.gene}"
                    output += "\n\nStandard ACMG/AMP criteria will be used."
            else:
                if args.json:
                    output = json.dumps({
                        "gene": args.gene,
                        "has_vcep": True,
                        "specification_count": len(specs),
                        "specifications": [s.to_dict() for s in specs]
                    }, indent=2)
                else:
                    lines = [f"Found {len(specs)} VCEP specification(s) for {args.gene}:", ""]
                    for i, spec in enumerate(specs, 1):
                        if len(specs) > 1:
                            lines.append(f"--- Specification {i} ---")
                        lines.append(format_spec_summary(spec))
                        lines.append("")
                    output = "\n".join(lines)
        else:
            parser.error("Gene symbol required (or use --list-all)")

        # Write output
        if args.output:
            with open(args.output, "w") as f:
                f.write(output)
            print(f"Output saved to {args.output}", file=sys.stderr)
        else:
            print(output)

        return 0

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
