#!/usr/bin/env python3
"""
ClinGen VCEP Specification Downloader
Downloads complete specifications including PDF and supplementary files from ClinGen
"""

import os
import sys
import json
import re
import argparse
import requests
from urllib.parse import urljoin, urlparse
import time

try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False


BASE_URL = "https://cspec.genome.network"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
}
MAX_DOWNLOAD_ATTEMPTS = 3


def fetch_page(url):
    """Fetch a page and return the content"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"✗ Error fetching page: {e}")
        return None


def extract_metadata(html_content):
    """Extract specification metadata from HTML page"""
    metadata = {}

    # Extract JavaScript variables
    patterns = {
        'currentVersion': r"currentVersion\s*=\s*'([^']+)'",
        'shortBaseName': r"shortBaseName\s*=\s*'([^']+)'",
        'geneName': r"geneName\s*=\s*'([^']+)'",
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, html_content)
        if match:
            metadata[key] = match.group(1)

    # Extract GN ID from data attribute
    gn_match = re.search(r'data-cspec-id=["\']([^"\']+)["\']', html_content)
    if gn_match:
        metadata['gn_id'] = gn_match.group(1)

    # Try to extract panel/disease information
    title_match = re.search(r'<title>([^<]+)</title>', html_content)
    if title_match:
        title = title_match.group(1)
        metadata['title'] = title

        # Extract panel name
        panel_match = re.search(r'ClinGen\s+([^E]+?)\s+Expert Panel', title)
        if panel_match:
            panel_name = panel_match.group(1).strip()
            panel_name = re.sub(r'[^\w\s-]', '', panel_name)
            panel_name = re.sub(r'\s+', '', panel_name)
            metadata['panel'] = panel_name

    return metadata


def find_supplementary_files(html_content, gn_id):
    """Find all downloadable supplementary files using BeautifulSoup"""
    files = []

    if not html_content:
        return files

    if not HAS_BS4:
        print("  ⚠ Warning: BeautifulSoup not installed. Falling back to regex (may miss some files)")
        print("  Install with: pip install beautifulsoup4")
        return find_supplementary_files_regex(html_content, gn_id)

    try:
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all file links with pattern /cspec/File/id/{UUID}/data
        file_links = soup.find_all('a', href=re.compile(r'/cspec/File/id/[a-f0-9-]+/data'))

        for link in file_links:
            href = link['href']

            # Construct full URL properly
            if href.startswith('http'):
                url = href
            else:
                url = f"https://cspec.genome.network{href}"

            # Extract filename from context
            filename = None

            # Method 1: Try to get from parent element text
            parent = link.find_parent(['li', 'div', 'p'])
            if parent:
                parent_text = parent.get_text(strip=True)
                # Extract text before colon (common pattern: "Filename: description")
                if ':' in parent_text:
                    filename = parent_text.split(':')[0].strip()
                else:
                    # Use first 100 chars
                    filename = parent_text[:100].strip()

            # Method 2: Try link text
            if not filename:
                filename = link.get_text(strip=True)

            # Method 3: Use a generic name
            if not filename:
                filename = f"supplementary_file"

            # Clean filename
            filename = re.sub(r'[<>:"/\\|?*\n\r\t]', '_', filename)
            filename = ' '.join(filename.split())  # Remove extra whitespace

            # Limit filename length
            if len(filename) > 150:
                filename = filename[:150]

            files.append({
                'url': url,
                'filename': filename,
                'type': 'supplementary'
            })

        # Also find images with src pointing to File/id/{UUID}/data
        img_tags = soup.find_all('img', src=re.compile(r'/cspec/File/id/[a-f0-9-]+/data'))

        for img in img_tags:
            src = img['src']

            # Construct full URL properly
            if src.startswith('http'):
                url = src
            else:
                url = f"https://cspec.genome.network{src}"

            # Extract filename from context
            filename = None

            # Try to find file-label in parent hierarchy (go up multiple levels)
            parent = img.find_parent(['div', 'span'])
            for _ in range(3):  # Look up to 3 levels
                if parent:
                    label = parent.find('span', class_='file-label')
                    if label:
                        filename = label.get_text(strip=True)
                        break
                    parent = parent.find_parent(['div', 'span'])

            # Fallback: use alt text
            if not filename and img.get('alt'):
                filename = img.get('alt').strip()

            # Fallback: generic name
            if not filename:
                filename = "image_file"

            # Clean filename
            filename = re.sub(r'[<>:"/\\|?*\n\r\t]', '_', filename)
            filename = ' '.join(filename.split())  # Remove extra whitespace

            # Limit filename length
            if len(filename) > 150:
                filename = filename[:150]

            files.append({
                'url': url,
                'filename': filename,
                'type': 'image'
            })

        # Remove duplicates based on URL
        seen_urls = set()
        unique_files = []
        for file_info in files:
            if file_info['url'] not in seen_urls:
                seen_urls.add(file_info['url'])
                unique_files.append(file_info)

        return unique_files

    except Exception as e:
        print(f"  ⚠ Error parsing HTML with BeautifulSoup: {e}")
        print("  Falling back to regex")
        return find_supplementary_files_regex(html_content, gn_id)


def find_supplementary_files_regex(html_content, gn_id):
    """Fallback regex-based file finding (less reliable)"""
    files = []

    # Pattern 1: Direct file URLs with File/id pattern (href)
    file_pattern = r'href="(https://cspec\.genome\.network/cspec/File/id/[^"]+/data)"'
    matches = re.findall(file_pattern, html_content)

    for url in matches:
        # Extract file ID for naming
        file_id_match = re.search(r'/File/id/([a-f0-9-]+)/', url)
        if file_id_match:
            file_id = file_id_match.group(1)[:8]  # Use first 8 chars of UUID
            filename = f"supplementary_file_{file_id}"
        else:
            filename = "supplementary_file"

        files.append({
            'url': url,
            'filename': filename,
            'type': 'supplementary'
        })

    # Pattern 2: Relative URLs (href)
    rel_pattern = r'href="(/cspec/File/id/[^"]+/data)"'
    rel_matches = re.findall(rel_pattern, html_content)

    for path in rel_matches:
        url = f"https://cspec.genome.network{path}"
        if url not in [f['url'] for f in files]:
            file_id_match = re.search(r'/File/id/([a-f0-9-]+)/', path)
            if file_id_match:
                file_id = file_id_match.group(1)[:8]
                filename = f"supplementary_file_{file_id}"
            else:
                filename = "supplementary_file"

            files.append({
                'url': url,
                'filename': filename,
                'type': 'supplementary'
            })

    # Pattern 3: Image src with File/id pattern
    img_pattern = r'src="(https://cspec\.genome\.network/cspec/File/id/[^"]+/data)"'
    img_matches = re.findall(img_pattern, html_content)

    for url in img_matches:
        if url not in [f['url'] for f in files]:
            file_id_match = re.search(r'/File/id/([a-f0-9-]+)/', url)
            if file_id_match:
                file_id = file_id_match.group(1)[:8]
                filename = f"image_file_{file_id}"
            else:
                filename = "image_file"

            files.append({
                'url': url,
                'filename': filename,
                'type': 'image'
            })

    # Pattern 4: Relative image src
    img_rel_pattern = r'src="(/cspec/File/id/[^"]+/data)"'
    img_rel_matches = re.findall(img_rel_pattern, html_content)

    for path in img_rel_matches:
        url = f"https://cspec.genome.network{path}"
        if url not in [f['url'] for f in files]:
            file_id_match = re.search(r'/File/id/([a-f0-9-]+)/', path)
            if file_id_match:
                file_id = file_id_match.group(1)[:8]
                filename = f"image_file_{file_id}"
            else:
                filename = "image_file"

            files.append({
                'url': url,
                'filename': filename,
                'type': 'image'
            })

    # Remove duplicates
    seen_urls = set()
    unique_files = []
    for f in files:
        if f['url'] not in seen_urls:
            seen_urls.add(f['url'])
            unique_files.append(f)

    return unique_files


def detect_file_extension(content):
    """Detect file extension from file content (magic bytes)"""
    if not content or len(content) < 4:
        return ''

    # Check magic bytes
    magic_bytes = content[:8]

    # PDF
    if magic_bytes[:4] == b'%PDF':
        return '.pdf'

    # PNG
    if magic_bytes[:8] == b'\x89PNG\r\n\x1a\n':
        return '.png'

    # JPEG
    if magic_bytes[:2] in (b'\xff\xd8', ):
        return '.jpg'

    # GIF (the signature is 6 bytes, so it cannot be matched against 4)
    if content[:6] in (b'GIF87a', b'GIF89a'):
        return '.gif'

    # Office Open XML formats (docx, xlsx, pptx) - all start with PK (ZIP)
    if magic_bytes[:2] == b'PK':
        # Check more content to determine Office type
        # Look in first 2KB which should contain [Content_Types].xml
        search_content = content[:2048].decode('latin-1', errors='ignore')

        if 'word/' in search_content or 'wordprocessingml' in search_content:
            return '.docx'
        elif 'xl/' in search_content or 'spreadsheetml' in search_content:
            return '.xlsx'
        elif 'ppt/' in search_content or 'presentationml' in search_content:
            return '.pptx'
        else:
            # Still a ZIP, but unknown Office format or plain ZIP
            return '.zip'

    # Old Office formats (OLE2/CFB). The container is shared by .doc/.xls/.ppt,
    # so look for the stream name the application writes into the directory.
    if magic_bytes[:8] == b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1':
        head = content[:8192]
        if b'W\x00o\x00r\x00k\x00b\x00o\x00o\x00k' in head or b'B\x00o\x00o\x00k' in head:
            return '.xls'
        if b'P\x00o\x00w\x00e\x00r\x00P\x00o\x00i\x00n\x00t' in head:
            return '.ppt'
        return '.doc'

    return ''


# Suffixes that are genuinely file extensions, as opposed to the trailing part
# of a version string. ClinGen names supplements like "Specifications_Table4_V1.2",
# where os.path.splitext reports ".2" — treating that as an extension leaves the
# file unreadable by openpyxl, python-docx and read_word.py.
KNOWN_EXTENSIONS = {
    '.pdf', '.png', '.jpg', '.jpeg', '.gif', '.svg', '.zip', '.csv', '.txt',
    '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.json', '.xml', '.html',
}


def has_real_extension(filename):
    """True when the filename already ends in a recognised file extension."""
    ext = os.path.splitext(filename)[1].lower()
    return ext in KNOWN_EXTENSIONS


def strip_real_extension(filename):
    """Drop a recognised file extension, leaving version suffixes intact.

    os.path.splitext would turn "Table4_V1.2" into "Table4_V1"; comparing that
    against the saved "Table4_V1.2.xlsx" makes an existing file look missing.
    """
    base, ext = os.path.splitext(filename)
    return base if ext.lower() in KNOWN_EXTENSIONS else filename


def download_file(url, output_path, description="file", max_attempts=MAX_DOWNLOAD_ATTEMPTS):
    """Download a file with proper extension detection"""
    last_error = None

    for attempt in range(1, max_attempts + 1):
        try:
            response = requests.get(url, headers=HEADERS, timeout=120, allow_redirects=True)
            response.raise_for_status()

            if not response.content:
                raise requests.exceptions.ContentDecodingError("empty response body")

            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            # Determine file extension from content when the name lacks one.
            # Append rather than replace: "Specifications_Table4_V1.2" must
            # become "...V1.2.xlsx", not "...V1.xlsx", or the version is lost.
            if not has_real_extension(output_path):
                detected_ext = detect_file_extension(response.content)
                if detected_ext:
                    output_path = output_path + detected_ext

            # Write only after a complete, non-empty response was received.
            with open(output_path, 'wb') as f:
                f.write(response.content)

            file_size = os.path.getsize(output_path)
            return True, file_size, output_path

        except requests.exceptions.RequestException as e:
            last_error = e
            if attempt < max_attempts:
                time.sleep(2 ** (attempt - 1))
                continue
            break
        except Exception as e:
            return False, str(e), output_path

    return False, f"{last_error} (after {max_attempts} attempts)", output_path


def download_pdf(metadata, output_dir):
    """Download the main PDF specification"""
    gn_id = metadata.get('gn_id', 'UNKNOWN')
    gene_name = metadata.get('geneName', 'UNKNOWN')
    version = metadata.get('currentVersion', '0.0.0')
    short_base = metadata.get('shortBaseName', 'Unknown')

    # Construct the PDF service URL
    spec_url = f"{BASE_URL}/cspec/ui/svi/doc/{gn_id}?layout=print"
    filename_base = f"ClinGen_{short_base}_ACMG_Specifications_{gene_name}_v{version}"

    pdf_service_url = f"{BASE_URL}/cspec/ui/svi/pdf"
    pdf_url = f"{pdf_service_url}?url={spec_url}&filename={filename_base}"

    # Determine output filename (use gene suffix, not full folder name with GN prefix)
    gene_suffix = determine_gene_suffix(metadata)
    pdf_filename = f"ClinGen_ACMG_Specifications_{gene_suffix}_v{version}.pdf"
    pdf_path = os.path.join(output_dir, pdf_filename)

    print(f"  Downloading PDF specification...")
    success, result, _ = download_file(pdf_url, pdf_path, "PDF specification")

    if success:
        size_str = format_size(result)
        print(f"  ✓ {pdf_filename} ({size_str})")
        return pdf_filename
    else:
        print(f"  ✗ Failed to download PDF: {result}")
        return None


def download_supplementary_files(files, output_dir):
    """Download all supplementary files"""
    if not files:
        print(f"  No supplementary files found")
        return [], []

    print(f"  Found {len(files)} supplementary file(s)")
    downloaded = []
    failures = []

    for i, file_info in enumerate(files, 1):
        filename = file_info['filename']
        file_url = file_info['url']
        output_path = os.path.join(output_dir, filename)

        # Check if file already exists (with or without extension)
        base_name = os.path.splitext(filename)[0]
        existing_files = [f for f in os.listdir(output_dir) if f.startswith(base_name)]

        if existing_files:
            existing_path = os.path.join(output_dir, existing_files[0])
            size = os.path.getsize(existing_path)
            if size > 0:
                print(f"  [{i}/{len(files)}] ✓ {existing_files[0]} ({format_size(size)}) - already exists")
                downloaded.append(existing_files[0])
                continue
            print(f"  [{i}/{len(files)}] ⚠ {existing_files[0]} is empty; re-downloading")

        print(f"  [{i}/{len(files)}] Downloading {filename}...", end=' ')
        success, result, actual_path = download_file(file_url, output_path, filename)

        if success:
            actual_filename = os.path.basename(actual_path)
            size_str = format_size(result)
            print(f"✓ ({size_str})")
            downloaded.append(actual_filename)
        else:
            print(f"✗ Error: {result}")
            failures.append({
                'filename': filename,
                'url': file_url,
                'error': str(result),
            })

        time.sleep(0.5)  # Be nice to the server

    return downloaded, failures


def save_metadata(metadata, output_dir, downloaded_files, expected_files=None, failed_files=None):
    """Save metadata JSON file"""
    gn_id = metadata.get('gn_id', 'UNKNOWN')
    gene_name = metadata.get('geneName', 'UNKNOWN')
    version = metadata.get('currentVersion', '0.0.0')
    title = metadata.get('title', '')
    panel = metadata.get('panel', 'Unknown')
    expected_files = expected_files or []
    failed_files = failed_files or []

    metadata_json = {
        "id": gn_id,
        "label": title,
        "gene": gene_name,
        "version": version,
        "panel": panel,
        "files_downloaded": len(downloaded_files),
        "download_date": time.strftime("%Y-%m-%d"),
        "files": downloaded_files,
        "expected_files": expected_files,
        "failed_files": failed_files,
        "complete": not failed_files,
    }

    json_path = os.path.join(output_dir, f"{gn_id}_data.json")
    with open(json_path, 'w') as f:
        json.dump(metadata_json, f, indent=2)

    print(f"  ✓ {gn_id}_data.json")
    return json_path


def format_size(size_bytes):
    """Format file size in human-readable format"""
    if size_bytes < 1024:
        return f"{size_bytes}B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes/1024:.1f}KB"
    else:
        return f"{size_bytes/1024/1024:.1f}MB"


def determine_gene_suffix(metadata):
    """Determine gene suffix (without GN ID prefix)"""
    gene_name = metadata.get('geneName', 'UNKNOWN')
    panel = metadata.get('panel', '')
    gn_id = metadata.get('gn_id', '')

    # Special handling for genes with multiple specifications
    if gene_name == 'ACTA1':
        if 'Dominant' in metadata.get('title', '') or 'AD' in gn_id:
            return 'ACTA1-AD'
        elif 'Recessive' in metadata.get('title', '') or 'AR' in gn_id:
            return 'ACTA1-AR'
        elif panel:
            return f"{gene_name}-{panel}"
    elif gene_name == 'RYR1' and panel:
        return f"{gene_name}-{panel}"

    return gene_name


def determine_folder_name(metadata):
    """Determine folder name: {GNid}-{GeneSymbol}"""
    gn_id = metadata.get('gn_id', '')
    gene_suffix = determine_gene_suffix(metadata)
    if gn_id:
        return f"{gn_id}-{gene_suffix}"
    return gene_suffix


def verify_specification(vcep_id, output_root):
    """Verify if a specification folder has all expected files"""

    print(f"\n{'='*80}")
    print(f"CLINGEN SPECIFICATION VERIFICATION")
    print(f"{'='*80}\n")

    # Construct specification URL
    spec_url = f"{BASE_URL}/cspec/ui/svi/doc/{vcep_id}"
    print(f"Specification: {vcep_id}")
    print(f"URL: {spec_url}\n")

    # Fetch the page
    print("Fetching specification page...")
    html_content = fetch_page(spec_url)

    if not html_content:
        print("✗ Failed to fetch specification page")
        return False

    # Extract metadata
    print("Extracting metadata...")
    metadata = extract_metadata(html_content)

    if not metadata.get('gn_id'):
        print("✗ Could not extract specification metadata")
        return False

    # Determine folder name
    folder_name = determine_folder_name(metadata)
    metadata['folder_name'] = folder_name
    output_dir = os.path.join(output_root, folder_name)

    print(f"✓ Found specification: {metadata.get('title', 'Unknown')[:80]}")
    print(f"  Gene: {metadata.get('geneName', 'Unknown')}")
    print(f"  Version: {metadata.get('currentVersion', 'Unknown')}")
    print(f"  Folder: {folder_name}/\n")

    # Check if folder exists (try new format first, then old gene-only format)
    if not os.path.exists(output_dir):
        gene_suffix = determine_gene_suffix(metadata)
        old_format_dir = os.path.join(output_root, gene_suffix)
        if os.path.exists(old_format_dir):
            print(f"  ℹ Found old-format folder: {gene_suffix}/ (expected: {folder_name}/)")
            output_dir = old_format_dir
            folder_name = gene_suffix
        else:
            print(f"✗ Folder does not exist: {output_dir}")
            print(f"\nTo download this specification, run:")
            print(f"  /vcep-spec {vcep_id}\n")
            return False

    print(f"Checking folder: {output_dir}\n")

    # Find expected files
    expected_files = []

    # Expected PDF (uses gene suffix, not full folder name)
    gene_name = metadata.get('geneName', 'UNKNOWN')
    version = metadata.get('currentVersion', '0.0.0')
    gene_suffix = determine_gene_suffix(metadata)
    pdf_filename = f"ClinGen_ACMG_Specifications_{gene_suffix}_v{version}.pdf"
    expected_files.append({
        'name': pdf_filename,
        'type': 'PDF',
        'required': True
    })

    # Expected supplementary files
    supp_files = find_supplementary_files(html_content, metadata.get('gn_id'))
    for supp in supp_files:
        # Try to find the actual filename with extension
        base_name = supp['filename']
        expected_files.append({
            'name': base_name,
            'type': supp['type'],
            'required': True
        })

    # Expected metadata JSON
    json_filename = f"{metadata.get('gn_id')}_data.json"
    expected_files.append({
        'name': json_filename,
        'type': 'metadata',
        'required': True
    })

    # Get actual files in directory
    actual_files = []
    actual_files_data = {}  # Map filename to file info
    if os.path.exists(output_dir):
        for f in os.listdir(output_dir):
            if os.path.isfile(os.path.join(output_dir, f)):
                actual_files.append(f)
                file_path = os.path.join(output_dir, f)
                # Determine file type from extension
                ext = os.path.splitext(f)[1].lower()
                if ext == '.pdf':
                    ftype = 'PDF'
                elif ext in ['.xlsx', '.xls', '.docx', '.doc', '.pptx', '.ppt']:
                    ftype = 'supplementary'
                elif ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg']:
                    ftype = 'image'
                elif ext == '.json':
                    ftype = 'metadata'
                else:
                    ftype = 'unknown'

                actual_files_data[f] = {
                    'type': ftype,
                    'size': os.path.getsize(file_path)
                }

    # Check if using regex fallback (less reliable names)
    using_regex_fallback = not HAS_BS4

    # Check each expected file
    print("Verification Results:")
    print("-" * 80)

    missing_required = []
    missing_optional = []
    found_files = []

    for expected in expected_files:
        expected_name = expected['name']
        file_type = expected['type']
        required = expected['required']

        # Check for exact match or match with extension
        found = False
        matched_file = None

        for actual in actual_files:
            # Exact match
            if actual == expected_name:
                found = True
                matched_file = actual
                break
            # Match base name (file might have extension added)
            base_expected = strip_real_extension(expected_name)
            base_actual = strip_real_extension(actual)
            if base_expected == base_actual:
                found = True
                matched_file = actual
                break

        if found:
            file_path = os.path.join(output_dir, matched_file)
            size = os.path.getsize(file_path)
            if size == 0:
                print(f"  ✗ INVALID (empty): {matched_file} [{file_type}]")
                if required:
                    missing_required.append(expected_name)
                else:
                    missing_optional.append(expected_name)
                continue
            size_str = format_size(size)
            print(f"  ✓ {matched_file} ({size_str}) [{file_type}]")
            found_files.append(matched_file)
        else:
            if required:
                print(f"  ✗ MISSING (required): {expected_name} [{file_type}]")
                missing_required.append(expected_name)
            else:
                # For optional files, don't report missing if using regex fallback
                # (names may not match but files might exist)
                if not using_regex_fallback:
                    print(f"  ⚠ MISSING (optional): {expected_name} [{file_type}]")
                    missing_optional.append(expected_name)

    # If using regex fallback, try fuzzy matching for optional files by type
    fuzzy_matched = {}
    if using_regex_fallback:
        # Count expected vs actual by type (excluding already matched files)
        expected_by_type = {}
        for exp in expected_files:
            if not exp['required']:  # Only optional files
                ftype = exp['type']
                expected_by_type[ftype] = expected_by_type.get(ftype, 0) + 1

        # Get unmatched actual files by type
        unmatched_actual_by_type = {}
        for fname in actual_files:
            if fname not in found_files:
                ftype = actual_files_data[fname]['type']
                if ftype in expected_by_type:  # Only count types we're expecting
                    if ftype not in unmatched_actual_by_type:
                        unmatched_actual_by_type[ftype] = []
                    unmatched_actual_by_type[ftype].append(fname)

        # Try to fuzzy match by type
        for ftype, expected_count in expected_by_type.items():
            actual_files_of_type = unmatched_actual_by_type.get(ftype, [])
            actual_count = len(actual_files_of_type)

            # Match up to the expected count
            matched_count = min(expected_count, actual_count)
            for i in range(matched_count):
                fname = actual_files_of_type[i]
                file_path = os.path.join(output_dir, fname)
                size = os.path.getsize(file_path)
                size_str = format_size(size)
                print(f"  ✓ {fname} ({size_str}) [{ftype}] (fuzzy match)")
                found_files.append(fname)
                fuzzy_matched[fname] = True

            # Report still missing after fuzzy match
            still_missing = expected_count - matched_count
            if still_missing > 0:
                missing_optional.append(f"{still_missing} {ftype} file(s)")

    # Check for extra files
    extra_files = [f for f in actual_files if f not in found_files]

    # If using regex fallback, categorize extra files
    if using_regex_fallback and extra_files:
        print(f"\nAdditional files found (cannot verify names without BeautifulSoup):")
        # Group by type
        extra_by_type = {'supplementary': [], 'image': [], 'other': []}
        for f in extra_files:
            ftype = actual_files_data[f]['type']
            if ftype == 'supplementary':
                extra_by_type['supplementary'].append(f)
            elif ftype == 'image':
                extra_by_type['image'].append(f)
            else:
                extra_by_type['other'].append(f)

        for f in extra_by_type['supplementary']:
            file_path = os.path.join(output_dir, f)
            size = os.path.getsize(file_path)
            size_str = format_size(size)
            print(f"  ℹ {f} ({size_str}) [supplementary]")

        for f in extra_by_type['image']:
            file_path = os.path.join(output_dir, f)
            size = os.path.getsize(file_path)
            size_str = format_size(size)
            print(f"  ℹ {f} ({size_str}) [image]")

        for f in extra_by_type['other']:
            file_path = os.path.join(output_dir, f)
            size = os.path.getsize(file_path)
            size_str = format_size(size)
            print(f"  ℹ {f} ({size_str})")
    elif extra_files:
        print(f"\nExtra files (not expected):")
        for f in extra_files:
            file_path = os.path.join(output_dir, f)
            size = os.path.getsize(file_path)
            size_str = format_size(size)
            print(f"  ℹ {f} ({size_str})")

    # Summary
    print(f"\n{'='*80}")
    print("VERIFICATION SUMMARY")
    print(f"{'='*80}")
    print(f"Expected files: {len(expected_files)}")
    print(f"Found files: {len(found_files)}")
    print(f"Missing required: {len(missing_required)}")
    print(f"Missing optional: {len(missing_optional)}")
    print(f"Extra files: {len([f for f in extra_files if f not in found_files])}")

    # Add note about BeautifulSoup for better verification
    if using_regex_fallback:
        print(f"\nℹ Note: Verification used regex fallback (BeautifulSoup not installed).")
        print(f"  File matching is approximate. Install beautifulsoup4 for exact verification:")
        print(f"  pip install beautifulsoup4")

    if missing_required:
        print(f"\n✗ INCOMPLETE - Missing required files!")
        print(f"\nTo re-download missing files, run:")
        print(f"  /vcep-spec {vcep_id}\n")
        return False
    elif missing_optional:
        print(f"\n⚠ MOSTLY COMPLETE - Some optional files missing")
        print(f"\nTo download all files, run:")
        print(f"  /vcep-spec {vcep_id}\n")
        return True
    else:
        print(f"\n✓ COMPLETE - All expected files present\n")
        return True


def download_specification(vcep_id, output_root, skip_pdf=False, skip_supplementary=False):
    """Main function to download a complete specification"""

    print(f"\n{'='*80}")
    print(f"CLINGEN SPECIFICATION DOWNLOADER")
    print(f"{'='*80}\n")

    # Construct specification URL
    spec_url = f"{BASE_URL}/cspec/ui/svi/doc/{vcep_id}"
    print(f"Specification: {vcep_id}")
    print(f"URL: {spec_url}\n")

    # Fetch the page
    print("Fetching specification page...")
    html_content = fetch_page(spec_url)

    if not html_content:
        print("✗ Failed to fetch specification page")
        return False

    # Extract metadata
    print("Extracting metadata...")
    metadata = extract_metadata(html_content)

    if not metadata.get('gn_id'):
        print("✗ Could not extract specification metadata")
        return False

    # Determine folder name
    folder_name = determine_folder_name(metadata)
    metadata['folder_name'] = folder_name
    output_dir = os.path.join(output_root, folder_name)
    os.makedirs(output_dir, exist_ok=True)

    print(f"✓ Found specification: {metadata.get('title', 'Unknown')[:80]}")
    print(f"  Gene: {metadata.get('geneName', 'Unknown')}")
    print(f"  Version: {metadata.get('currentVersion', 'Unknown')}")
    print(f"  Panel: {metadata.get('panel', 'Unknown')}")
    print(f"  Output: {folder_name}/\n")

    downloaded_files = []
    expected_files = []
    failed_files = []

    # Download PDF
    if not skip_pdf:
        gene_suffix = determine_gene_suffix(metadata)
        version = metadata.get('currentVersion', '0.0.0')
        expected_pdf = f"ClinGen_ACMG_Specifications_{gene_suffix}_v{version}.pdf"
        expected_files.append(expected_pdf)
        pdf_file = download_pdf(metadata, output_dir)
        if pdf_file:
            downloaded_files.append(pdf_file)
        else:
            failed_files.append({
                'filename': expected_pdf,
                'url': f"{BASE_URL}/cspec/ui/svi/pdf",
                'error': 'PDF download failed',
            })
        print()

    # Download supplementary files
    if not skip_supplementary:
        files = find_supplementary_files(html_content, metadata.get('gn_id'))
        expected_files.extend(file_info['filename'] for file_info in files)
        supp_files, supp_failures = download_supplementary_files(files, output_dir)
        downloaded_files.extend(supp_files)
        failed_files.extend(supp_failures)
        print()

    # Save metadata
    print("Creating metadata...")
    save_metadata(
        metadata,
        output_dir,
        downloaded_files,
        expected_files=expected_files,
        failed_files=failed_files,
    )

    print(f"\n{'='*80}")
    if failed_files:
        print(f"✗ DOWNLOAD INCOMPLETE")
    else:
        print(f"✓ DOWNLOAD COMPLETE")
    print(f"{'='*80}")
    print(f"\nFolder: {folder_name}/")
    print(f"Files downloaded: {len(downloaded_files)}")
    if failed_files:
        print(f"Files failed: {len(failed_files)}")
        for failure in failed_files:
            print(f"  ✗ {failure['filename']}: {failure['error']}")
    print(f"Location: {output_dir}\n")

    return not failed_files


def main():
    parser = argparse.ArgumentParser(
        description='Download ClinGen ACMG/AMP variant interpretation specifications',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  %(prog)s GN101                              Download ACTC1 specification
  %(prog)s GN147 -o ~/Documents/Genetics      Download to custom directory
  %(prog)s GN169 --skip-supplementary         Download only the PDF
  %(prog)s GN188 --verify                     Verify existing download completeness

Requirements:
  pip install requests beautifulsoup4
        '''
    )

    parser.add_argument('vcep_id',
                        help='VCEP specification ID (e.g., GN101, GN147)')
    parser.add_argument('-o', '--output-dir',
                        default='./ClinGen',
                        help='Output directory (default: ./ClinGen)')
    parser.add_argument('--skip-pdf',
                        action='store_true',
                        help='Skip downloading the main PDF specification')
    parser.add_argument('--skip-supplementary',
                        action='store_true',
                        help='Skip downloading supplementary files')
    parser.add_argument('--verify',
                        action='store_true',
                        help='Verify existing download completeness (no download)')

    args = parser.parse_args()

    # Check for BeautifulSoup
    if not HAS_BS4:
        print("⚠ Warning: beautifulsoup4 not installed")
        print("For best results, install with: pip install beautifulsoup4")
        print("Continuing with regex fallback (may miss some files)...\n")

    # Validate VCEP ID format
    if not re.match(r'^GN\d+$', args.vcep_id.upper()):
        print(f"✗ Error: Invalid VCEP ID format. Expected format: GN### (e.g., GN101)")
        sys.exit(1)

    # Expand output directory path
    output_dir = os.path.expanduser(args.output_dir)

    # Verify or download
    if args.verify:
        # Verification mode
        success = verify_specification(args.vcep_id.upper(), output_dir)
    else:
        # Download mode
        success = download_specification(
            args.vcep_id.upper(),
            output_dir,
            skip_pdf=args.skip_pdf,
            skip_supplementary=args.skip_supplementary
        )

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
