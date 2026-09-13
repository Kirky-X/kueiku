"""Regression tests for DCF year validation (issue: calendar years silently gave EV=0)."""

from common import CSVTestCase

VALID = "year,fcf\n" + "".join(f"{y},{1000 + y * 100}\n" for y in range(1, 6))
CALENDAR_YEARS = "year,fcf\n2024,1000\n2025,1100\n2026,1200\n2027,1300\n2028,1400\n"
GAPPED = "year,fcf\n1,1000\n2,1100\n4,1200\n"


class TestDcfYearValidation(CSVTestCase):

    def test_calendar_years_rejected(self):
        """year=2024 must fail loudly, not produce a silent EV=0 report."""
        proc = self.write_and_run("dcf_cal.csv", CALENDAR_YEARS, "dcf", "--rate", "0.10", "--growth", "0.03")
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("period indices starting at 1", proc.stderr)
        self.assertIn("2024", proc.stderr)
        self.assertNotIn("Enterprise value", proc.stdout)

    def test_non_consecutive_periods_rejected(self):
        proc = self.write_and_run("dcf_gap.csv", GAPPED, "dcf", "--rate", "0.10", "--growth", "0.03")
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("consecutive period indices", proc.stderr)

    def test_valid_periods_still_work(self):
        proc = self.write_and_run("dcf_ok.csv", VALID, "dcf", "--rate", "0.10", "--growth", "0.03")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Enterprise value", proc.stdout)
        self.assertNotIn("0.00", proc.stdout.split("Enterprise value")[1].splitlines()[0])


if __name__ == "__main__":
    unittest.main()
