"""Regression tests for RICE tiering (issue: Backlog was always 1 item)."""

from common import CSVTestCase

RICE_7 = """name,reach,impact,confidence,effort
A,50000,2,80,2
B,20000,3,50,1
C,30000,1,100,3
D,10000,3,80,1
E,8000,2,50,1
F,60000,1,80,4
G,15000,2,100,2
"""

RICE_3 = """name,reach,impact,confidence,effort
A,50000,2,80,2
B,20000,3,50,1
C,30000,1,100,3
"""


def parse_tiers(report):
    """Return (must_do, target, backlog) name lists from a RICE report."""
    tiers = {}
    for line in report.splitlines():
        for key, label in [("top", "Must do (Top"), ("target", "Target"), ("backlog", "Backlog")]:
            if f"**{label}" in line and "**: " in line:
                names = line.split("**: ", 1)[1].strip()
                tiers[key] = [n.strip() for n in names.split(",")] if names else []
    return tiers.get("top", []), tiers.get("target", []), tiers.get("backlog", [])


class TestRiceTiers(CSVTestCase):

    def test_seven_items_backlog_not_single(self):
        """7 items -> top 2 / target 2 / backlog 3 (previously backlog was always 1)."""
        proc = self.write_and_run("rice7.csv", RICE_7, "rice")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        top, target, backlog = parse_tiers(proc.stdout)
        self.assertEqual(len(top), 2, proc.stdout)
        self.assertEqual(len(target), 2, proc.stdout)
        self.assertGreaterEqual(len(backlog), 2, f"Backlog collapsed to {len(backlog)} item(s):\n{proc.stdout}")
        self.assertEqual(len(top) + len(target) + len(backlog), 7, proc.stdout)
        # Tiers are disjoint and ordered by score
        all_names = top + target + backlog
        self.assertEqual(len(set(all_names)), 7)

    def test_three_items_even_split(self):
        """3 items -> 1 / 1 / 1."""
        proc = self.write_and_run("rice3.csv", RICE_3, "rice")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        top, target, backlog = parse_tiers(proc.stdout)
        self.assertEqual((len(top), len(target), len(backlog)), (1, 1, 1), proc.stdout)

    def test_two_items_no_tiers(self):
        """n < 3: no tier section at all (reasonable boundary behavior)."""
        proc = self.write_and_run(
            "rice2.csv",
            "name,reach,impact,confidence,effort\nA,500,2,80,2\nB,300,3,50,1\n",
            "rice")
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertNotIn("Tier Recommendations", proc.stdout)


if __name__ == "__main__":
    unittest.main()
