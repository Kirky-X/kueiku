"""Shared helpers for kueiku script regression tests (stdlib only)."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAIN = ROOT / "scripts" / "main.py"


class CSVTestCase(unittest.TestCase):
    """Base class providing temp-dir CSV writing and CLI invocation."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def write_csv(self, name, text):
        path = self.tmp / name
        path.write_text(text, encoding="utf-8")
        return str(path)

    def run_cli(self, *args):
        """Run scripts/main.py with args; returns CompletedProcess."""
        return subprocess.run(
            [sys.executable, str(MAIN), *args],
            capture_output=True, text=True,
        )

    def write_and_run(self, csv_name, csv_text, *args):
        return self.run_cli(*args, "-i", self.write_csv(csv_name, csv_text))
