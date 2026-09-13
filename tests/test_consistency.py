"""Consistency regression: SKILL.md / skill.json numbers must match reality (issue 1:
SKILL.md claimed 116, table summed to 128, actual files were 129)."""

import json
import re
from pathlib import Path

from common import ROOT, CSVTestCase


class TestCountConsistency(CSVTestCase):

    def count_methodologies(self):
        refs = ROOT / "references"
        counts = {}
        for cat in sorted(p for p in refs.iterdir() if p.is_dir()):
            counts[cat.name] = len([f for f in cat.glob("*.md") if f.name != "index.md"])
        return counts

    def test_skill_md_total_matches_files(self):
        counts = self.count_methodologies()
        total = sum(counts.values())
        n_cats = len(counts)
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn(f"{n_cats} categories × {total} methodologies", skill)

    def test_skill_md_table_rows_match_files(self):
        counts = self.count_methodologies()
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for cat, n in counts.items():
            # table row is: | idx | Name | types | Count | `path` | — count precedes path
            row = re.compile(rf"\|\s*\d+\s*\|[^|]+\|[^|]*\|\s*(\d+)\s*\|\s*`references/{re.escape(cat)}/index\.md`")
            m = row.search(skill)
            self.assertIsNotNone(m, f"No category table row for {cat}")
            self.assertEqual(int(m.group(1)), n, f"Count mismatch for {cat}: table={m.group(1)} actual={n}")
        # Table counts sum to the real total
        rows = re.findall(r"^\|\s*\d+\s*\|[^|]+\|[^|]*\|\s*(\d+)\s*\|", skill, re.M)
        self.assertEqual(sum(int(x) for x in rows), sum(counts.values()))

    # Directory name -> display name used in skill.json (only where they differ)
    DISPLAY_ALIASES = {"strategy": "strategic analysis"}

    def test_skill_json_description_updated(self):
        counts = self.count_methodologies()
        total = sum(counts.values())
        data = json.loads((ROOT / "skill.json").read_text(encoding="utf-8"))
        desc = data["description"]
        self.assertIn(f"{total} methodologies", desc)
        self.assertNotIn("35 methodologies", desc)
        for cat in counts:
            token = self.DISPLAY_ALIASES.get(cat, cat).replace("-", " ")
            self.assertTrue(token in desc.lower() or cat in desc.lower(),
                            f"category '{cat}' missing from skill.json description")

    def test_count_script_agrees(self):
        out = json.loads((ROOT / "scripts" / "methodology-count.json").read_text(encoding="utf-8"))
        self.assertEqual(out["total_methodologies"], sum(self.count_methodologies().values()))


if __name__ == "__main__":
    unittest.main()
