import importlib.util
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import Mock, patch

import requests


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "download.py"
SPEC = importlib.util.spec_from_file_location("vcep_download", SCRIPT)
download = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(download)


METADATA = {
    "gn_id": "GN009",
    "geneName": "TP53",
    "currentVersion": "2.4",
    "shortBaseName": "TP53",
    "title": "TP53 VCEP",
}
SUPPLEMENT = {
    "url": "https://example.test/pvs1",
    "filename": "PVS1 Flowchart",
    "type": "supplementary",
}


class DownloadFailureTests(unittest.TestCase):
    def test_supplementary_failure_makes_download_incomplete_and_records_error(self):
        with tempfile.TemporaryDirectory() as tmpdir, patch.object(
            download, "fetch_page", return_value="html"
        ), patch.object(download, "extract_metadata", return_value=METADATA.copy()), patch.object(
            download, "download_pdf", return_value="main.pdf"
        ), patch.object(
            download, "find_supplementary_files", return_value=[SUPPLEMENT]
        ), patch.object(
            download,
            "download_file",
            return_value=(False, "SSL EOF", str(Path(tmpdir) / "PVS1 Flowchart")),
        ), patch.object(download.time, "sleep"):
            output = io.StringIO()
            with redirect_stdout(output):
                result = download.download_specification("GN009", tmpdir)

            self.assertFalse(result)
            self.assertIn("DOWNLOAD INCOMPLETE", output.getvalue())
            self.assertIn("PVS1 Flowchart", output.getvalue())
            self.assertIn("SSL EOF", output.getvalue())

            metadata_path = Path(tmpdir) / "GN009-TP53" / "GN009_data.json"
            saved = json.loads(metadata_path.read_text(encoding="utf-8"))
            self.assertFalse(saved["complete"])
            self.assertEqual(saved["failed_files"][0]["filename"], "PVS1 Flowchart")

    def test_verify_fails_when_an_expected_supplementary_file_is_missing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            folder = Path(tmpdir) / "GN009-TP53"
            folder.mkdir()
            (folder / "ClinGen_ACMG_Specifications_TP53_v2.4.pdf").write_bytes(b"%PDF-test")
            (folder / "GN009_data.json").write_text("{}", encoding="utf-8")

            with patch.object(download, "fetch_page", return_value="html"), patch.object(
                download, "extract_metadata", return_value=METADATA.copy()
            ), patch.object(
                download, "find_supplementary_files", return_value=[SUPPLEMENT]
            ):
                output = io.StringIO()
                with redirect_stdout(output):
                    result = download.verify_specification("GN009", tmpdir)

            self.assertFalse(result)
            self.assertIn("PVS1 Flowchart", output.getvalue())
            self.assertIn("INCOMPLETE", output.getvalue())

    def test_download_file_retries_transient_ssl_failure(self):
        response = Mock()
        response.content = b"%PDF-test"
        response.raise_for_status.return_value = None

        with tempfile.TemporaryDirectory() as tmpdir, patch.object(
            download.requests,
            "get",
            side_effect=[requests.exceptions.SSLError("SSL EOF"), response],
        ) as request, patch.object(download.time, "sleep"):
            success, size, path = download.download_file(
                "https://example.test/file", str(Path(tmpdir) / "flowchart.pdf")
            )

        self.assertTrue(success)
        self.assertEqual(size, len(response.content))
        self.assertEqual(request.call_count, 2)
        self.assertTrue(path.endswith("flowchart.pdf"))


XLSX = b"PK\x03\x04" + b"\x00" * 26 + b"[Content_Types].xml xl/workbook.xml"
DOCX = b"PK\x03\x04" + b"\x00" * 26 + b"[Content_Types].xml word/document.xml"


class FetchPageRetryTests(unittest.TestCase):
    """A single transient TLS drop on the specification page aborted the whole
    spec before any file was considered; GN141 failed a full-corpus run this way."""

    def test_transient_ssl_failure_is_retried(self):
        response = Mock()
        response.text = "<html>spec</html>"
        response.raise_for_status.return_value = None

        with patch.object(
            download.requests, "get",
            side_effect=[requests.exceptions.SSLError("SSL EOF"), response],
        ) as request, patch.object(download.time, "sleep"):
            result = download.fetch_page("https://example.test/GN141")

        self.assertEqual(result, "<html>spec</html>")
        self.assertEqual(request.call_count, 2)

    def test_gives_up_after_max_attempts_and_reports(self):
        with patch.object(
            download.requests, "get",
            side_effect=requests.exceptions.SSLError("SSL EOF"),
        ) as request, patch.object(download.time, "sleep"):
            output = io.StringIO()
            with redirect_stdout(output):
                result = download.fetch_page("https://example.test/GN141")

        self.assertIsNone(result)
        self.assertEqual(request.call_count, download.MAX_DOWNLOAD_ATTEMPTS)
        self.assertIn("after 3 attempts", output.getvalue())


class ExtensionDetectionTests(unittest.TestCase):
    """ClinGen names supplements "Specifications_Table4_V1.2". splitext reports
    ".2", which the old guard accepted as an extension, so the file was saved
    without one and openpyxl/python-docx refused to open it."""

    def test_version_suffix_is_not_mistaken_for_an_extension(self):
        self.assertFalse(download.has_real_extension("Specifications_Table4_V1.2"))
        self.assertFalse(download.has_real_extension("Appendix_V1.2"))
        self.assertFalse(download.has_real_extension("PVS1 Flowchart"))
        self.assertTrue(download.has_real_extension("Table 1&2.xlsx"))
        self.assertTrue(download.has_real_extension("report.PDF"))

    def test_detected_extension_is_appended_so_the_version_survives(self):
        response = Mock()
        response.content = XLSX
        response.raise_for_status.return_value = None

        with tempfile.TemporaryDirectory() as tmpdir, patch.object(
            download.requests, "get", return_value=response
        ):
            ok, _size, path = download.download_file(
                "https://example.test/t4",
                str(Path(tmpdir) / "Specifications_Table4_V1.2"),
            )

        self.assertTrue(ok)
        self.assertTrue(path.endswith("Specifications_Table4_V1.2.xlsx"), path)

    def test_existing_real_extension_is_left_alone(self):
        response = Mock()
        response.content = DOCX
        response.raise_for_status.return_value = None

        with tempfile.TemporaryDirectory() as tmpdir, patch.object(
            download.requests, "get", return_value=response
        ):
            ok, _size, path = download.download_file(
                "https://example.test/a", str(Path(tmpdir) / "Appendix.docx")
            )

        self.assertTrue(ok)
        self.assertTrue(path.endswith("Appendix.docx"), path)

    def test_office_open_xml_types_are_distinguished(self):
        self.assertEqual(download.detect_file_extension(XLSX), ".xlsx")
        self.assertEqual(download.detect_file_extension(DOCX), ".docx")

    def test_gif_signature_is_six_bytes(self):
        self.assertEqual(download.detect_file_extension(b"GIF89a" + b"\x00" * 8), ".gif")

    def test_legacy_ole_container_distinguishes_xls_from_doc(self):
        ole = b"\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1"
        wide = lambda s: b"".join(bytes([c, 0]) for c in s.encode())  # noqa: E731
        self.assertEqual(download.detect_file_extension(ole + wide("Workbook")), ".xls")
        self.assertEqual(download.detect_file_extension(ole + b"\x00" * 64), ".doc")

    def test_verify_matches_a_file_that_gained_an_extension(self):
        supplement = {
            "url": "https://example.test/t4",
            "filename": "Specifications_Table4_V1.2",
            "type": "supplementary",
        }
        with tempfile.TemporaryDirectory() as tmpdir:
            folder = Path(tmpdir) / "GN009-TP53"
            folder.mkdir()
            (folder / "ClinGen_ACMG_Specifications_TP53_v2.4.pdf").write_bytes(b"%PDF-test")
            (folder / "GN009_data.json").write_text("{}", encoding="utf-8")
            (folder / "Specifications_Table4_V1.2.xlsx").write_bytes(XLSX)

            with patch.object(download, "fetch_page", return_value="html"), patch.object(
                download, "extract_metadata", return_value=METADATA.copy()
            ), patch.object(
                download, "find_supplementary_files", return_value=[supplement]
            ):
                output = io.StringIO()
                with redirect_stdout(output):
                    result = download.verify_specification("GN009", tmpdir)

            self.assertTrue(result, output.getvalue())
            self.assertNotIn("MISSING", output.getvalue())


if __name__ == "__main__":
    unittest.main()
