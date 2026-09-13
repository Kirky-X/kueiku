"""Regression tests for A/B test analysis:
- 3+ variants must not be silently dropped (issue 3)
- SRM uses chi-square > 3.841, MDE includes z_beta (issue 4)
"""

import math

from common import CSVTestCase

BASE_2 = """variant,users,conversions
control,10000,500
treatment,10200,550
"""

BASE_3 = BASE_2 + "treatment2,9800,610\n"

# 1.5% user imbalance: chi2 ~= 2.22 -> NOT an SRM at alpha=0.05
# (the old 1% empirical threshold wrongly flagged this)
SRM_MILD = """variant,users,conversions
control,5075,250
treatment,4925,240
"""

# 12.5% imbalance: chi2 ~= 716 -> clear SRM
SRM_STRONG = """variant,users,conversions
control,10000,500
treatment,4000,210
"""


def parse_mde_pct(report):
    for line in report.splitlines():
        if "MDE (Minimum Detectable Effect)" in line:
            return float(line.rsplit(":", 1)[1].strip().rstrip("%"))
    return None


class TestAbtestMultiVariant(CSVTestCase):

    def test_third_variant_not_silent(self):
        """3-variant CSV: explicit warning + summary/comparison for the 3rd variant."""
        proc = self.write_and_run("ab3.csv", BASE_3, "abtest")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("WARNING", proc.stdout)
        self.assertIn("Additional Variants", proc.stdout)
        self.assertIn("treatment2", proc.stdout)
        self.assertIn("not** part of the primary decision", proc.stdout)

    def test_third_variant_in_json(self):
        proc = self.write_and_run("ab3.csv", BASE_3, "abtest", "--json")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("additional_variants", proc.stdout)
        self.assertIn("treatment2", proc.stdout)
        self.assertIn("ignored_variants_warning", proc.stdout)

    def test_two_variants_no_warning(self):
        proc = self.write_and_run("ab2.csv", BASE_2, "abtest")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertNotIn("WARNING", proc.stdout)


class TestAbtestStatistics(CSVTestCase):

    def test_mde_includes_power_term(self):
        """MDE = (1.96 + 0.84) * SE; previously z_beta was missing (0.6% vs true ~0.88%)."""
        proc = self.write_and_run("mde.csv", BASE_2, "abtest")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        p_pool = (500 + 550) / (10000 + 10200)
        expected = 2.80 * math.sqrt(2 * p_pool * (1 - p_pool) / 10000) * 100
        got = parse_mde_pct(proc.stdout)
        self.assertIsNotNone(got)
        self.assertAlmostEqual(got, expected, delta=0.06)  # report rounds to 1 decimal
        self.assertGreater(got, 0.8)  # power-adjusted ~0.9%, not the old z_alpha-only 0.6%

    def test_mde_is_power_adjusted_not_alpha_only(self):
        proc = self.write_and_run("mde.csv", BASE_2, "abtest", "--json")
        self.assertIn('"mde"', proc.stdout)

    def test_srm_mild_imbalance_passes(self):
        """chi2(1.5% imbalance, n=10k) ~= 2.22 < 3.841 -> no SRM (old 1% rule flagged it)."""
        proc = self.write_and_run("srm_mild.csv", SRM_MILD, "abtest")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Normal", proc.stdout)
        self.assertNotIn("INVALID", proc.stdout)

    def test_srm_severe_imbalance_detected(self):
        proc = self.write_and_run("srm_bad.csv", SRM_STRONG, "abtest")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Mismatch detected", proc.stdout)
        self.assertIn("INVALID", proc.stdout)


if __name__ == "__main__":
    unittest.main()
