"""Regression tests for friendly input errors (issue: bare IndexError/ValueError)."""

from common import CSVTestCase


class TestEmptyCsv(CSVTestCase):

    def test_header_only_csv_friendly_error(self):
        """Empty table must exit with a friendly message, not rows[0] IndexError."""
        proc = self.write_and_run("empty.csv", "name,reach,impact,confidence,effort\n", "rice")
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("empty", proc.stderr.lower())
        self.assertNotIn("Traceback", proc.stderr)

    def test_zero_byte_csv_friendly_error(self):
        proc = self.write_and_run("zero.csv", "", "riskparity")
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("empty", proc.stderr.lower())
        self.assertNotIn("Traceback", proc.stderr)

    def test_empty_csv_abtest(self):
        proc = self.write_and_run("empty2.csv", "variant,users,conversions\n", "abtest")
        self.assertNotEqual(proc.returncode, 0)
        self.assertNotIn("Traceback", proc.stderr)


class TestBadNumeric(CSVTestCase):

    def test_rice_bad_float_row_message(self):
        """Non-numeric value must report the row and field, not a raw ValueError."""
        proc = self.write_and_run(
            "bad.csv",
            "name,reach,impact,confidence,effort\nA,500,2,80,2\nB,twentyk,3,50,1\n",
            "rice")
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("row 3", proc.stderr)
        self.assertIn("reach", proc.stderr)
        self.assertNotIn("Traceback", proc.stderr)

    def test_perf_bad_return_row_message(self):
        proc = self.write_and_run(
            "bad2.csv",
            "date,return\n2024-01-02,0.01\n2024-01-03,oops\n",
            "perf")
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("row 3", proc.stderr)
        self.assertIn("return", proc.stderr)
        self.assertNotIn("Traceback", proc.stderr)


if __name__ == "__main__":
    unittest.main()
