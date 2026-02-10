#!/usr/bin/env python3
"""
Get UniProt domain information from HGVS nomenclature.
Input: NM_000022.4(ADA):c.872C>G(p.Ser291Trp)
"""

import re
import requests
from typing import Optional


def parse_hgvs(hgvs: str) -> dict:
    """
    Parse HGVS nomenclature to extract transcript, gene, and protein position.
    Example: NM_000022.4(ADA):c.872C>G(p.Ser291Trp)
    """
    pattern = r'(NM_\d+\.\d+)\((\w+)\):c\..*\(p\.([A-Z][a-z]{2})(\d+)'
    match = re.search(pattern, hgvs)

    if not match:
        raise ValueError(f"Could not parse HGVS: {hgvs}")

    return {
        "transcript": match.group(1),
        "gene": match.group(2),
        "ref_aa": match.group(3),
        "position": int(match.group(4))
    }


def get_uniprot_id(refseq_id: str, gene_name: str) -> Optional[str]:
    """
    Map RefSeq transcript ID or gene name to UniProt accession.
    Tries RefSeq first, then falls back to gene name.
    """
    # Try RefSeq mapping first
    refseq_base = refseq_id.split('.')[0]
    url = f"https://rest.uniprot.org/uniprotkb/search?query=xref:refseq-{refseq_base}&fields=accession&format=json"
    response = requests.get(url)
    if response.ok and response.json().get("results"):
        return response.json()["results"][0]["primaryAccession"]

    # Fallback: search by gene name (human, reviewed/Swiss-Prot)
    url = f"https://rest.uniprot.org/uniprotkb/search?query=gene:{gene_name}+AND+organism_id:9606+AND+reviewed:true&fields=accession&format=json"
    response = requests.get(url)
    if response.ok and response.json().get("results"):
        return response.json()["results"][0]["primaryAccession"]

    return None


def get_uniprot_domains(uniprot_id: str) -> list:
    """
    Get all domain/region features from UniProt.
    """
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    domain_types = {"Domain", "Region", "Motif", "Repeat", "Zinc finger", "DNA binding", "Binding site", "Active site"}
    domains = []

    for feature in data.get("features", []):
        if feature.get("type") in domain_types:
            start = feature.get("location", {}).get("start", {}).get("value")
            end = feature.get("location", {}).get("end", {}).get("value")

            domains.append({
                "type": feature.get("type"),
                "description": feature.get("description", ""),
                "start": start,
                "end": end
            })

    return domains


def analyze_variant_location(position: int, domains: list) -> dict:
    """
    Determine variant position relative to domains.
    """
    in_domains = []
    nearby_domains = []

    for domain in domains:
        start, end = domain["start"], domain["end"]

        if start <= position <= end:
            in_domains.append({
                **domain,
                "relative_position": f"{position - start + 1}/{end - start + 1} aa from start"
            })
        elif abs(position - start) <= 10 or abs(position - end) <= 10:
            if position < start:
                nearby_domains.append({**domain, "distance": f"{start - position} aa before"})
            else:
                nearby_domains.append({**domain, "distance": f"{position - end} aa after"})

    return {
        "in_domains": in_domains,
        "nearby_domains": nearby_domains
    }


def get_domain_info(hgvs: str) -> dict:
    """
    Main function: Get domain information for a variant from HGVS.
    """
    parsed = parse_hgvs(hgvs)

    uniprot_id = get_uniprot_id(parsed["transcript"], parsed["gene"])
    if not uniprot_id:
        raise ValueError(f"Could not find UniProt ID for {parsed['transcript']} / {parsed['gene']}")

    domains = get_uniprot_domains(uniprot_id)
    location_analysis = analyze_variant_location(parsed["position"], domains)

    return {
        "hgvs": hgvs,
        "gene": parsed["gene"],
        "transcript": parsed["transcript"],
        "protein_position": parsed["position"],
        "uniprot_id": uniprot_id,
        "all_domains": domains,
        "variant_in_domains": location_analysis["in_domains"],
        "variant_near_domains": location_analysis["nearby_domains"]
    }


if __name__ == "__main__":
    import sys
    import json
    import argparse

    parser = argparse.ArgumentParser(description="Get UniProt domain information from HGVS nomenclature")
    parser.add_argument("hgvs", nargs="?", default="NM_000022.4(ADA):c.872C>G(p.Ser291Trp)",
                        help="HGVS nomenclature (e.g., NM_000022.4(ADA):c.872C>G(p.Ser291Trp))")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    parser.add_argument("-o", "--output", help="Output file path")
    args = parser.parse_args()

    hgvs = args.hgvs
    if hgvs == "NM_000022.4(ADA):c.872C>G(p.Ser291Trp)" and len(sys.argv) == 1:
        print(f"Using example: {hgvs}\n", file=sys.stderr)

    result = get_domain_info(hgvs)

    if args.json:
        output = json.dumps(result, indent=2)
        if args.output:
            with open(args.output, "w") as f:
                f.write(output)
            print(f"Saved to {args.output}", file=sys.stderr)
        else:
            print(output)
    else:
        print(f"Gene: {result['gene']}")
        print(f"Transcript: {result['transcript']}")
        print(f"UniProt: {result['uniprot_id']}")
        print(f"Variant Position: {result['protein_position']}")
        print()

        if result["variant_in_domains"]:
            print("VARIANT IN DOMAIN(S):")
            for d in result["variant_in_domains"]:
                print(f"  • {d['type']}: {d['description']} ({d['start']}-{d['end']})")
                print(f"    Position: {d['relative_position']}")
        else:
            print("VARIANT NOT IN ANY ANNOTATED DOMAIN")

        if result["variant_near_domains"]:
            print("\nNEARBY DOMAINS (<10 aa):")
            for d in result["variant_near_domains"]:
                print(f"  • {d['type']}: {d['description']} ({d['start']}-{d['end']}) - {d['distance']}")

        print(f"\nALL DOMAINS ({len(result['all_domains'])}):")
        for d in result["all_domains"]:
            marker = " ◀ VARIANT" if d["start"] <= result["protein_position"] <= d["end"] else ""
            print(f"  {d['start']:4d}-{d['end']:4d}  {d['type']}: {d['description']}{marker}")

        if args.output:
            with open(args.output, "w") as f:
                json.dump(result, f, indent=2)
            print(f"\nSaved JSON to {args.output}")
