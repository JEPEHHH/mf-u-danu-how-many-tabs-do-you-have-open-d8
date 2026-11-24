"""Local gate and determinism verification tests for main.py."""

import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import main as entry_main

REPO_ROOT = Path(__file__).resolve().parent
ENTRYPOINT = REPO_ROOT / "main.py"


class EntryGateTests(unittest.TestCase):
    def test_default_output_path_matches_harness(self) -> None:
        self.assertEqual(entry_main.DEFAULT_OUTPUT_PATH, Path("/output/entry.txt"))

    def test_cli_writes_valid_gate_output(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "output" / "entry.txt"
            proc = subprocess.run(
                [sys.executable, str(ENTRYPOINT), str(target)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, msg=proc.stderr)
            self.assertTrue(target.is_file(), "Output file was not created.")

            raw = target.read_bytes()
            text = raw.decode("utf-8")

            self.assertGreaterEqual(len(text), 1)
            self.assertLessEqual(len(text), 5)
            self.assertTrue(text.strip(), "Output must not be whitespace only.")
            self.assertEqual(text, text.strip(), "Output must not have surrounding whitespace.")
            self.assertTrue(text.isascii() and text.isdigit(), "Output must be ASCII digits only.")
            self.assertEqual(text, entry_main.TAB_COUNT)
            self.assertEqual(len(raw), len(entry_main.TAB_COUNT))

    def test_determinism_across_two_runs(self) -> None:
        digests: list[str] = []
        outputs: list[bytes] = []
        with tempfile.TemporaryDirectory() as tmp:
            for run_idx in range(2):
                target = Path(tmp) / f"run_{run_idx}" / "entry.txt"
                proc = subprocess.run(
                    [sys.executable, str(ENTRYPOINT), str(target)],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(proc.returncode, 0, msg=proc.stderr)
                raw = target.read_bytes()
                outputs.append(raw)
                digests.append(hashlib.sha256(raw).hexdigest())

        self.assertEqual(outputs[0], outputs[1])
        self.assertEqual(digests[0], digests[1])

    def test_validator_rejects_invalid_inputs(self) -> None:
        invalid_samples = [
            "",
            "   ",
            "\n",
            "123456",
            "2746\n",
            " 2746",
            "2,746",
            "-42",
            "42 tabs",
            "\u0662\u0667\u0664\u0666",
        ]
        for sample in invalid_samples:
            with self.subTest(sample=sample):
                with self.assertRaises(ValueError):
                    entry_main.validate_tab_count(sample)

    def test_license_file_has_osi_spdx(self) -> None:
        license_path = REPO_ROOT / "LICENSE"
        self.assertTrue(license_path.is_file(), "LICENSE file is missing.")
        content = license_path.read_text(encoding="utf-8")
        self.assertIn("SPDX-License-Identifier: MIT", content)


if __name__ == "__main__":
    unittest.main(verbosity=2)
