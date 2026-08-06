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


if __name__ == "__main__":
    unittest.main()
