"""Regression tests for silent data skipping (issues: pareto/factor skip counting,
momentum trailing-period 0-return, Sortino denominator, periods-per-year)."""

import json
import math

from common import CSVTestCase


class TestSkipReporting(CSVTestCase):

    def test_pareto_reports_skipped_rows(self):
        """value <= 0 rows were silently dropped; now counted in the report header."""
        proc = self.write_and_run(
            "pareto.csv",
            "name,value\nA,420\nB,0\nC,-50\nD,180\n",
            "pareto")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Skipped 2 input row(s)", proc.stdout)
        self.assertIn("value ≤ 0", proc.stdout)
        # The skipped items must not appear in the ranking table
        self.assertNotIn("| B |", proc.stdout)
        self.assertNotIn("| C |", proc.stdout)

    def test_factor_reports_skipped_cross_sections(self):
        """Cross-sections with <5 assets were silently skipped; now counted."""
        rows = ["date,asset,factor_value,forward_return"]
        rows += [f"2024-01,A{i},0.{i},0.0{i}" for i in range(1, 6)]       # 5 assets -> kept
        rows += [f"2024-02,A{i},0.{i},0.0{i}" for i in range(1, 4)]       # 3 assets -> skipped
        proc = self.write_and_run("factor.csv", "\n".join(rows) + "\n", "factor")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Skipped 1 cross-section(s)", proc.stdout)
        self.assertIn("fewer than 5 assets", proc.stdout)
        self.assertIn("Cross-sections: 1", proc.stdout)

    def test_momentum_trailing_period_skipped_not_zero(self):
        """The last signal has no next-period price: skip + report, not a fake 0% return."""
        lines = ["date,A1,A2,A3,A4"]
        prices = [100.0, 102.0, 99.0, 104.0]
        for i in range(40):
            prices = [p * (1.003 if j % 2 == 0 else 0.999) for j, p in enumerate(prices)]
            lines.append(f"2024-{i + 1:03d}," + ",".join(f"{p:.4f}" for p in prices))
        proc = self.write_and_run("prices.csv", "\n".join(lines) + "\n", "momentum")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("Skipped 1 trailing signal", proc.stdout)
        self.assertIn("no next-period return", proc.stdout)


class TestStatsDefinitions(CSVTestCase):

    def test_sortino_uses_full_sample_denominator(self):
        """Downside deviation must divide by n, not by the number of loss periods."""
        rets = [0.01, -0.005, 0.02, -0.01, 0.015, 0.007, -0.002, 0.012, -0.008, 0.004,
                0.006, -0.004, 0.009, 0.011, -0.006]
        lines = ["date,return"] + [f"2024-{i + 1:03d},{r}" for i, r in enumerate(rets)]
        proc = self.write_and_run("perf.csv", "\n".join(lines) + "\n", "perf")
        self.assertEqual(proc.returncode, 0, proc.stderr)

        n = len(rets)
        mean = sum(rets) / n
        std = math.sqrt(sum((r - mean) ** 2 for r in rets) / (n - 1))
        down = math.sqrt(sum(r ** 2 for r in rets if r < 0) / n)
        expected_sortino = (mean * 252) / (down * math.sqrt(252))
        expected_sharpe = (mean * 252) / (std * math.sqrt(252))

        sortino = sharpe = None
        for line in proc.stdout.splitlines():
            if "Sortino ratio" in line:
                sortino = float(line.rsplit(":", 1)[1].strip().strip("*").strip())
            if "Sharpe ratio" in line:
                sharpe = float(line.rsplit(":", 1)[1].strip().strip("*").strip())
        self.assertAlmostEqual(sortino, expected_sortino, places=2)
        self.assertAlmostEqual(sharpe, expected_sharpe, places=2)
        # Old buggy denominator (4 loss periods) would give a visibly larger value
        self.assertLess(sortino, expected_sharpe * 2.5)

    def test_riskparity_periods_per_year_parameter(self):
        """--periods-per-year must change annualization (default 252 stays compatible)."""
        lines = ["period,stocks,bonds"]
        for t in range(1, 25):
            lines.append(f"2024-{t:02d},{0.01 + 0.001 * (t % 3)},{0.002 - 0.0002 * (t % 4)}")
        csv_text = "\n".join(lines) + "\n"
        dflt = self.write_and_run("rp.csv", csv_text, "riskparity", "--json")
        monthly = self.write_and_run("rp.csv", csv_text, "riskparity", "--json", "--periods-per-year", "12")
        self.assertEqual(dflt.returncode, 0, dflt.stderr)
        self.assertEqual(monthly.returncode, 0, monthly.stderr)
        v252 = json.loads(dflt.stdout)["portfolio_vol"]
        v12 = json.loads(monthly.stdout)["portfolio_vol"]
        # portfolio vol scales with sqrt(periods per year)
        self.assertAlmostEqual(v252 / v12, math.sqrt(252 / 12), places=6)
        # HELP text mentions the flag
        help_proc = self.run_cli("riskparity", "--help")
        self.assertIn("--periods-per-year", help_proc.stdout)


if __name__ == "__main__":
    unittest.main()
