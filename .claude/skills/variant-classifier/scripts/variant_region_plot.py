#!/usr/bin/env python3
"""
Variant Region Plot

Generate a genome browser-style visualization for a genomic region around a variant.
Dynamically fetches sequence data, ClinVar variants, and gnomAD frequencies.

Usage:
    # By variant position (chr:start-end)
    python variant_region_plot.py chr3:129061736-129061746

    # By variant ID (chr-pos-ref-alt)
    python variant_region_plot.py 3-129061736-TCCCATGCCTG-T

    # With custom padding (default: 75bp on each side)
    python variant_region_plot.py chr17:7674220 --padding 100

    # Specify transcript
    python variant_region_plot.py chr20:44621100 --transcript NM_000022.4

    # Output to specific file
    python variant_region_plot.py chr17:7674220 -o my_plot.png
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Optional, Tuple

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd

# Import local modules
from refseq_sequence_fetcher import RefSeqFetcher, GenomicRegionData
from clinvar_region_query import search_clinvar_region, fetch_variant_details, create_session
from gnomad_query import GnomadClient

# Color schemes
NUCLEOTIDE_COLORS = {
    'A': '#B0F890',  # Light green
    'T': '#F0A878',  # Peach
    'G': '#E8F880',  # Light yellow
    'C': '#98D0E8',  # Light blue
    'N': '#D3D3D3',  # Gray
}

AMINO_ACID_COLORS = {
    # Hydrophobic (yellow)
    'A': '#E0E030', 'V': '#E0E030', 'I': '#E0E030', 'L': '#E0E030',
    'M': '#E0E030', 'F': '#E0E030', 'W': '#E0E030', 'P': '#E0E030',
    # Polar (green)
    'S': '#48B028', 'T': '#48B028', 'N': '#48B028', 'Q': '#48B028',
    'C': '#48B028', 'G': '#48B028', 'Y': '#48B028',
    # Positive charge (blue)
    'K': '#4048F0', 'R': '#4048F0', 'H': '#4048F0',
    # Negative charge (red)
    'D': '#C82810', 'E': '#C82810',
    # Stop codon
    '*': '#808080',
}

BACKGROUND_COLOR = '#F1F2F5'
AXIS_BG_COLOR = '#FFFFFF'
AA_OFFSET_BP = 1


def parse_variant_input(variant_str: str) -> Tuple[str, int, int, Optional[str], Optional[str]]:
    """
    Parse variant input string into components.

    Supports formats:
    - chr3:129061736-129061746 (region)
    - chr3:129061736 (single position)
    - 3-129061736-TCCCATGCCTG-T (variant ID)
    - chr17:7674220:C:T (position with alleles)

    Returns:
        Tuple of (chromosome, start, end, ref, alt)
        For position-only input, start == end
    """
    variant_str = variant_str.strip()

    # Format: chr-pos-ref-alt (gnomAD style)
    match = re.match(r'^(?:chr)?(\w+)-(\d+)-([ATCGN]+)-([ATCGN]+)$', variant_str, re.IGNORECASE)
    if match:
        chrom, pos, ref, alt = match.groups()
        pos = int(pos)
        # Calculate end position based on ref allele length
        end = pos + len(ref) - 1
        return f"chr{chrom}", pos, end, ref.upper(), alt.upper()

    # Format: chr:pos:ref:alt or chr:pos:ref>alt
    match = re.match(r'^(?:chr)?(\w+):(\d+)[:>]([ATCGN]+)[:>]([ATCGN]+)$', variant_str, re.IGNORECASE)
    if match:
        chrom, pos, ref, alt = match.groups()
        pos = int(pos)
        end = pos + len(ref) - 1
        return f"chr{chrom}", pos, end, ref.upper(), alt.upper()

    # Format: chr:start-end (region)
    match = re.match(r'^(?:chr)?(\w+):(\d+)-(\d+)$', variant_str)
    if match:
        chrom, start, end = match.groups()
        return f"chr{chrom}", int(start), int(end), None, None

    # Format: chr:pos (single position)
    match = re.match(r'^(?:chr)?(\w+):(\d+)$', variant_str)
    if match:
        chrom, pos = match.groups()
        pos = int(pos)
        return f"chr{chrom}", pos, pos, None, None

    raise ValueError(f"Unable to parse variant: {variant_str}")


def fetch_clinvar_data(chrom: str, start: int, end: int) -> pd.DataFrame:
    """Fetch ClinVar variants for a region."""
    print(f"Fetching ClinVar data for {chrom}:{start}-{end}...")

    try:
        session = create_session()
        variant_ids = search_clinvar_region(chrom, start, end, session=session)

        if not variant_ids:
            print("  No ClinVar variants found in region")
            return pd.DataFrame()

        variants = fetch_variant_details(variant_ids, session=session)

        # Convert to DataFrame
        df = pd.DataFrame(variants)
        # Ensure numeric columns
        if 'start' in df.columns:
            df['start'] = pd.to_numeric(df['start'], errors='coerce')
        if 'stop' in df.columns:
            df['stop'] = pd.to_numeric(df['stop'], errors='coerce')

        print(f"  Found {len(df)} ClinVar variants")
        return df

    except Exception as e:
        print(f"  Warning: Failed to fetch ClinVar data: {e}")
        return pd.DataFrame()


def fetch_gnomad_data(chrom: str, start: int, end: int, dataset: str = "gnomad_r4") -> list:
    """Fetch gnomAD variants for a region."""
    print(f"Fetching gnomAD data for {chrom}:{start}-{end}...")

    try:
        client = GnomadClient()
        # Remove 'chr' prefix for gnomAD
        chrom_num = chrom.replace("chr", "")
        variants = client.query_region(chrom_num, start, end, dataset=dataset)

        variant_list = [v.to_dict() for v in variants]
        print(f"  Found {len(variant_list)} gnomAD variants")
        return variant_list

    except Exception as e:
        print(f"  Warning: Failed to fetch gnomAD data: {e}")
        return []


def plot_variant_region(
    region_data: GenomicRegionData,
    clinvar_df: pd.DataFrame,
    gnomad_variants: list,
    variant_pos: Tuple[int, int],
    transcript_id: str = None,
    output_file: str = "variant_region.png"
):
    """
    Create a genome browser-style plot for a variant region.

    Args:
        region_data: GenomicRegionData from fetcher
        clinvar_df: DataFrame of ClinVar variants
        gnomad_variants: List of gnomAD variant dicts
        variant_pos: Tuple of (start, end) for the variant being analyzed
        transcript_id: Specific transcript to show (None = first one)
        output_file: Output filename
    """
    # Select transcript
    if transcript_id:
        transcript = next((t for t in region_data.transcripts
                          if t.transcript_id == transcript_id), None)
    else:
        # Use first transcript (usually canonical)
        transcript = region_data.transcripts[0] if region_data.transcripts else None

    if not transcript:
        print("Warning: No transcript found for this region")
        # Create minimal plot without transcript track
        transcript = None
        mappings = []
    else:
        mappings = region_data.amino_acid_mappings.get(transcript.transcript_id, [])

    start = region_data.start
    end = region_data.end
    dna_seq = region_data.dna_sequence
    var_start, var_end = variant_pos

    # Create figure
    region_len = end - start
    fig_width = 2096 / 150
    fig_height = 759 / 150
    fig, axes = plt.subplots(
        5, 1,
        figsize=(fig_width, fig_height),
        dpi=150,
        gridspec_kw={'height_ratios': [0.6, 1.1, 0.9, 0.7, 0.9], 'hspace': 0.0}
    )
    fig.patch.set_facecolor(BACKGROUND_COLOR)

    # Track 1: Coordinate ruler
    ax_coord = axes[0]
    ax_coord.set_facecolor('none')
    ax_coord.set_xlim(start - 0.5, end + 0.5)
    ax_coord.set_ylim(0, 1)

    # Draw ruler
    ax_coord.axhline(y=0.3, color='black', linewidth=1)

    # Determine tick intervals
    if region_len <= 200:
        major_interval, minor_interval = 10, 5
    elif region_len <= 500:
        major_interval, minor_interval = 50, 10
    else:
        major_interval, minor_interval = 100, 20

    # Major ticks
    major_start = ((start // major_interval) + 1) * major_interval
    for pos in range(major_start, end + 1, major_interval):
        ax_coord.plot([pos, pos], [0.2, 0.4], 'k-', linewidth=1)
        ax_coord.text(pos, 0.55, f'{pos:,}', ha='center', va='bottom',
                     fontsize=6, rotation=45)

    # Minor ticks
    minor_start = ((start // minor_interval) + 1) * minor_interval
    for pos in range(minor_start, end + 1, minor_interval):
        if pos % major_interval != 0:
            ax_coord.plot([pos, pos], [0.25, 0.35], 'k-', linewidth=0.5)

    ax_coord.set_yticks([])
    for spine in ax_coord.spines.values():
        spine.set_visible(False)
    ax_coord.set_xticks([])

    # Title
    gene_name = transcript.gene_name if transcript else "Unknown"
    tx_id = transcript.transcript_id if transcript else "No transcript"
    fig.text(0.02, 0.985, f"{region_data.chromosome}:{start:,}-{end:,} - {gene_name} ({tx_id})",
             fontsize=10, fontweight='bold', ha='left', va='top', color='#333333')

    # Track 2: DNA Sequence
    ax_dna = axes[1]
    ax_dna.set_facecolor(AXIS_BG_COLOR)
    ax_dna.set_xlim(start - 0.5, end + 0.5)
    ax_dna.set_ylim(0, 1)

    for i, nt in enumerate(dna_seq):
        pos = start + i
        color = NUCLEOTIDE_COLORS.get(nt.upper(), '#D3D3D3')

        # Highlight variant position
        if var_start <= pos <= var_end:
            rect = mpatches.Rectangle(
                (pos - 0.45, 0.1), 0.9, 0.8,
                facecolor='#FF6B6B',
                edgecolor='#CC0000',
                linewidth=1.5,
                alpha=0.8
            )
        else:
            rect = mpatches.Rectangle(
                (pos - 0.45, 0.3), 0.9, 0.4,
                facecolor=color,
                edgecolor='white',
                linewidth=0.3
            )
        ax_dna.add_patch(rect)

        # Add letter if zoomed in enough
        if len(dna_seq) <= 200:
            ax_dna.text(pos, 0.5, nt.upper(), ha='center', va='center',
                       fontsize=5, fontweight='bold', family='monospace')

    ax_dna.set_yticks([])
    ax_dna.set_ylabel('Sequence', fontsize=9, rotation=0, ha='right', va='center', color='#333333')
    for spine in ax_dna.spines.values():
        spine.set_visible(False)
    ax_dna.set_xticks([])

    # Track 3: Transcript with amino acids
    ax_tx = axes[2]
    ax_tx.set_facecolor(AXIS_BG_COLOR)
    ax_tx.set_xlim(start - 0.5, end + 0.5)
    ax_tx.set_ylim(0, 1.08)

    if transcript:
        # Draw transcript backbone
        ax_tx.axhline(y=0.5, color='#8A8F98', linewidth=2)

        # Draw exon regions
        for exon in transcript.exons:
            if exon.end >= start and exon.start <= end:
                ex_start = max(exon.start, start)
                ex_end = min(exon.end, end)

                rect = mpatches.Rectangle(
                    (ex_start - 0.5 + AA_OFFSET_BP, 0.4), ex_end - ex_start + 1, 0.2,
                    facecolor='#C8D8E0',
                    edgecolor='#6A8CA8',
                    linewidth=1,
                    alpha=0.6
                )
                ax_tx.add_patch(rect)

        # Draw amino acids
        for mapping in mappings:
            aa = mapping.amino_acid
            gs = mapping.genomic_start + AA_OFFSET_BP
            ge = mapping.genomic_end + AA_OFFSET_BP

            if ge < start or gs > end:
                continue

            is_split_codon = (ge - gs) > 4

            if is_split_codon:
                display_start = gs
                display_end = min(gs + 1, end)
            else:
                display_start = max(gs, start)
                display_end = min(ge, end)

            center = (display_start + display_end) / 2
            width = display_end - display_start + 1

            color = AMINO_ACID_COLORS.get(aa, '#808080')

            rect = mpatches.FancyBboxPatch(
                (display_start - 0.3, 0.32), width - 0.4, 0.36,
                boxstyle=mpatches.BoxStyle("Round", pad=0.02, rounding_size=0.2),
                facecolor=color,
                edgecolor='#333333',
                linewidth=0.5
            )
            ax_tx.add_patch(rect)

            if (end - start) <= 300 and width >= 2:
                ax_tx.text(center, 0.5, aa, ha='center', va='center',
                          fontsize=6, fontweight='bold', family='monospace')

        # AA position labels
        label_interval = max(5, len(mappings) // 15)
        for i, mapping in enumerate(mappings):
            if i % label_interval == 0:
                gs = mapping.genomic_start + AA_OFFSET_BP
                ge = mapping.genomic_end + AA_OFFSET_BP
                if (ge - gs) > 4:
                    center = gs + 0.5
                else:
                    center = (gs + ge) / 2
                ax_tx.text(center, 0.18, str(mapping.position), ha='center', va='top',
                          fontsize=5, color='#666A73')

        # Strand direction
        strand_char = '→' if transcript.strand == 1 else '←'
        ax_tx.text(start + 2, 0.9, f"{transcript.gene_name} {strand_char}",
                   fontsize=9, fontweight='bold', color='#333333')
    else:
        ax_tx.text((start + end) / 2, 0.5, "No transcript data", ha='center', va='center',
                   fontsize=10, color='#999999')

    ax_tx.set_yticks([])
    ylabel = f'Transcript\n{tx_id}' if transcript else 'Transcript'
    ax_tx.set_ylabel(ylabel, fontsize=8, rotation=0, ha='right', va='center', color='#333333')
    for spine in ax_tx.spines.values():
        spine.set_visible(False)
    ax_tx.set_xticks([])

    # Track 4: ClinVar Variants
    ax_clinvar = axes[3]
    ax_clinvar.set_facecolor(AXIS_BG_COLOR)
    ax_clinvar.set_xlim(start - 0.5, end + 0.5)
    ax_clinvar.set_ylim(0, 1.08)
    ax_clinvar.set_yticks([])
    ax_clinvar.set_ylabel('ClinVar', fontsize=9, rotation=0, ha='right', va='center', color='#333333')
    for spine in ax_clinvar.spines.values():
        spine.set_visible(False)
    ax_clinvar.set_xticks([])

    clinvar_colors = {
        'Pathogenic': '#E04030',
        'Likely pathogenic': '#E04030',
        'Pathogenic/Likely pathogenic': '#E04030',
        'Benign': '#40B850',
        'Likely benign': '#40B850',
        'Uncertain significance': '#E0A800',
        'Conflicting interpretations of pathogenicity': '#E0A800',
        'not provided': '#B8BCC6'
    }
    clinvar_levels = {
        'Pathogenic': 0.9,
        'Likely pathogenic': 0.72,
        'Uncertain': 0.5,
        'Likely benign': 0.28,
        'Benign': 0.1
    }
    clinvar_simplify = {
        'Pathogenic': 'Pathogenic',
        'Likely pathogenic': 'Likely pathogenic',
        'Pathogenic/Likely pathogenic': 'Pathogenic',
        'Uncertain significance': 'Uncertain',
        'Conflicting interpretations of pathogenicity': 'Uncertain',
        'not provided': 'Uncertain',
        'Likely benign': 'Likely benign',
        'Benign': 'Benign'
    }

    # ClinVar guide lines
    label_x = start + (end - start) * 0.0015
    clinvar_order = list(clinvar_levels.items())
    for i, (label, level) in enumerate(clinvar_order):
        ax_clinvar.hlines(level, start, end, colors='#B8BCC6', linestyles=(0, (3, 3)), linewidth=0.6, zorder=0)
        if i > 0:
            prev_level = clinvar_order[i - 1][1]
            label_y = level + (prev_level - level) * 0.1
        else:
            label_y = level + 0.01
        ax_clinvar.text(label_x, label_y, label, ha='left', va='bottom', fontsize=6, color='#6B707A')

    # Plot ClinVar variants
    if not clinvar_df.empty and 'start' in clinvar_df.columns:
        for _, variant in clinvar_df.iterrows():
            try:
                v_start = int(variant['start'])
                if start <= v_start <= end:
                    simple = clinvar_simplify.get(variant.get('classification', ''), 'Uncertain')
                    color = clinvar_colors.get(variant.get('classification', ''), '#D3D3D3')
                    level = clinvar_levels.get(simple, 0.5)
                    ax_clinvar.plot(v_start, level, 'o', color=color, markersize=4)
            except (ValueError, TypeError):
                continue

    # Track 5: gnomAD Exome Variants
    ax_gnomad = axes[4]
    ax_gnomad.set_facecolor(AXIS_BG_COLOR)
    ax_gnomad.set_xlim(start - 0.5, end + 0.5)
    ax_gnomad.set_ylim(0, 1.08)
    ax_gnomad.set_yticks([])
    ax_gnomad.set_ylabel('gnomAD\nExome', fontsize=8, rotation=0, ha='right', va='center', color='#333333')
    for spine in ax_gnomad.spines.values():
        spine.set_visible(False)
    ax_gnomad.set_xticks([])

    def gnomad_level_from_af(af: float) -> float:
        if af is None:
            af = 0
        af = max(min(float(af), 1.0), 0.0)
        log_min = np.log10(1e-6)
        log_max = 0.0
        log_af = np.log10(max(af, 1e-6))
        return (log_af - log_min) / (log_max - log_min)

    # gnomAD frequency guide lines
    gnomad_ticks = [1, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6]
    label_x = start + (end - start) * 0.0015
    gnomad_levels_list = []
    for tick in gnomad_ticks:
        level = gnomad_level_from_af(tick)
        height = 0.1 + 0.8 * level
        gnomad_levels_list.append((tick, height))
        ax_gnomad.hlines(height, start, end, colors='#B8BCC6', linestyles=(0, (3, 3)), linewidth=0.6, zorder=0)

    for i, (tick, height) in enumerate(gnomad_levels_list):
        if i > 0:
            prev_height = gnomad_levels_list[i - 1][1]
            label_y = height + (prev_height - height) * 0.1
        else:
            label_y = height + 0.01
        ax_gnomad.text(label_x, label_y, f'{tick:.0e}' if tick < 1 else '1.0',
                       ha='left', va='bottom', fontsize=6, color='#6B707A')

    # Plot gnomAD variants
    for variant in gnomad_variants:
        try:
            parts = variant['variant_id'].split('-')
            variant_start = int(parts[1])

            if start <= variant_start <= end:
                af = variant.get('exome_af') or variant.get('genome_af')
                level = gnomad_level_from_af(af)
                height = 0.1 + 0.8 * level
                ax_gnomad.plot(variant_start, height, '^', color='#40B850', markersize=3)
        except (ValueError, IndexError, KeyError):
            continue

    # Save
    plt.subplots_adjust(left=0.065, right=0.995, top=0.94, bottom=0.04, hspace=0.0)
    plt.savefig(output_file, dpi=150, facecolor=BACKGROUND_COLOR, bbox_inches=None, pad_inches=0)
    print(f"Saved plot to {output_file}")

    # Also save SVG
    svg_file = output_file.rsplit('.', 1)[0] + '.svg'
    plt.savefig(svg_file, facecolor=BACKGROUND_COLOR, bbox_inches=None, pad_inches=0)
    print(f"Saved SVG to {svg_file}")

    plt.close()


def main():
    parser = argparse.ArgumentParser(
        description="Generate genome browser plot for a variant region",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s chr3:129061736-129061746
  %(prog)s 3-129061736-TCCCATGCCTG-T
  %(prog)s chr17:7674220 --padding 100
  %(prog)s chr20:44621100 --transcript NM_000022.4 -o ada_variant.png
        """
    )
    parser.add_argument("variant", help="Variant position or ID")
    parser.add_argument("--padding", "-p", type=int, default=75,
                        help="Base pairs to add on each side (default: 75)")
    parser.add_argument("--transcript", "-t", help="Specific transcript ID (e.g., NM_000022.4)")
    parser.add_argument("--output", "-o", default="variant_region.png",
                        help="Output filename (default: variant_region.png)")
    parser.add_argument("--gnomad-dataset", default="gnomad_r4",
                        choices=["gnomad_r4", "gnomad_r3", "gnomad_r2_1"],
                        help="gnomAD dataset version")
    parser.add_argument("--no-clinvar", action="store_true",
                        help="Skip fetching ClinVar data")
    parser.add_argument("--no-gnomad", action="store_true",
                        help="Skip fetching gnomAD data")

    args = parser.parse_args()

    # Parse variant input
    try:
        chrom, var_start, var_end, ref, alt = parse_variant_input(args.variant)
        print(f"Variant: {chrom}:{var_start}-{var_end}")
        if ref and alt:
            print(f"  Ref: {ref}, Alt: {alt}")
    except ValueError as e:
        print(f"Error: {e}")
        return 1

    # Calculate region bounds
    region_start = var_start - args.padding
    region_end = var_end + args.padding
    print(f"Region: {chrom}:{region_start}-{region_end} (±{args.padding}bp padding)")

    # Fetch sequence data
    print("\n--- Fetching sequence data ---")
    fetcher = RefSeqFetcher()
    try:
        if args.transcript:
            region_data = fetcher.fetch_region(chrom, region_start, region_end,
                                               transcript_ids=[args.transcript])
        else:
            region_data = fetcher.fetch_region(chrom, region_start, region_end)
    except Exception as e:
        print(f"Error fetching sequence data: {e}")
        return 1

    # Fetch ClinVar data
    clinvar_df = pd.DataFrame()
    if not args.no_clinvar:
        print("\n--- Fetching ClinVar data ---")
        clinvar_df = fetch_clinvar_data(chrom, region_start, region_end)

    # Fetch gnomAD data
    gnomad_variants = []
    if not args.no_gnomad:
        print("\n--- Fetching gnomAD data ---")
        gnomad_variants = fetch_gnomad_data(chrom, region_start, region_end, args.gnomad_dataset)

    # Generate plot
    print("\n--- Generating plot ---")
    plot_variant_region(
        region_data=region_data,
        clinvar_df=clinvar_df,
        gnomad_variants=gnomad_variants,
        variant_pos=(var_start, var_end),
        transcript_id=args.transcript,
        output_file=args.output
    )

    print("\nDone!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
