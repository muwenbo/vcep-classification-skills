#!/usr/bin/env python3
"""
Read Excel files (.xlsx, .xls) and convert to markdown format.

Usage:
    python read_excel.py <path_to_excel_file> [--sheet SHEET_NAME] [--json]

Arguments:
    path_to_excel_file    Path to the Excel file to read
    --sheet SHEET_NAME    Read only the specified sheet (optional)
    --json                Output as JSON instead of markdown (optional)

Output:
    Markdown tables for each sheet (default) or JSON structure

Dependencies:
    pandas, openpyxl (auto-installed if missing)
"""

import sys
import json
import argparse

def install_dependencies():
    """Install required packages if not present."""
    import subprocess
    packages = ['pandas', 'openpyxl', 'tabulate']
    for pkg in packages:
        try:
            __import__(pkg)
        except ImportError:
            print(f"Installing {pkg}...", file=sys.stderr)
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", pkg, "-q"],
                stderr=subprocess.DEVNULL
            )

def read_excel_file(file_path, sheet_name=None):
    """
    Read an Excel file and return its contents.

    Args:
        file_path: Path to the Excel file
        sheet_name: Specific sheet to read (None for all sheets)

    Returns:
        Dictionary with sheet names as keys and sheet data as values
    """
    try:
        import pandas as pd
    except ImportError:
        install_dependencies()
        import pandas as pd

    excel_file = pd.ExcelFile(file_path)
    result = {}

    sheets_to_read = [sheet_name] if sheet_name else excel_file.sheet_names

    for name in sheets_to_read:
        if name not in excel_file.sheet_names:
            print(f"Warning: Sheet '{name}' not found", file=sys.stderr)
            continue

        df = pd.read_excel(excel_file, sheet_name=name)

        # Clean up column names
        df.columns = [str(col).strip() for col in df.columns]

        # Convert NaN to empty strings for cleaner output
        df = df.fillna('')

        result[name] = {
            'columns': df.columns.tolist(),
            'data': df.to_dict(orient='records'),
            'shape': {'rows': df.shape[0], 'columns': df.shape[1]},
            'markdown': df.to_markdown(index=False)
        }

    return result

def format_output(data, output_format='markdown'):
    """Format the extracted data for output."""
    if output_format == 'json':
        # Remove markdown from JSON output to reduce size
        for sheet in data.values():
            del sheet['markdown']
        return json.dumps(data, indent=2, default=str)

    # Markdown format
    output = []
    for sheet_name, sheet_data in data.items():
        output.append(f"\n## Sheet: {sheet_name}")
        output.append(f"*Dimensions: {sheet_data['shape']['rows']} rows x {sheet_data['shape']['columns']} columns*\n")
        output.append(sheet_data['markdown'])
        output.append("\n" + "-" * 80)

    return '\n'.join(output)

def main():
    parser = argparse.ArgumentParser(
        description='Read Excel files and convert to markdown or JSON'
    )
    parser.add_argument('file_path', help='Path to the Excel file')
    parser.add_argument('--sheet', help='Specific sheet to read')
    parser.add_argument('--json', action='store_true', help='Output as JSON')

    args = parser.parse_args()

    try:
        data = read_excel_file(args.file_path, args.sheet)

        if not data:
            print("No data found in file", file=sys.stderr)
            sys.exit(1)

        output_format = 'json' if args.json else 'markdown'
        print(format_output(data, output_format))

    except FileNotFoundError:
        print(f"Error: File not found: {args.file_path}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading Excel file: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
