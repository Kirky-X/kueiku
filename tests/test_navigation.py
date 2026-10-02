"""Navigation-layer acceptance tests (complements test_consistency.py, which
guards counts; this module guards routing assets):

- all methodology links resolve (SKILL.md + every index.md backtick reference)
- every index.md carries its required routing sections
- the 4 acceptance scenarios in evals/evals.json are still backed by routing assets
- entry-skeleton field coverage: a regression floor for the stub-repair batch
- no literal "\\n" escapes in methodology files (regression for the strategy stubs)
"""

import json
import re
import unittest
from pathlib import Path

from common import ROOT

REFS = ROOT / "references"

INDEX_SECTIONS = ["Routing Trigger Signals", "Minimum Information Requirements"]
SKELETON_FIELDS = ["When NOT to use", "Failure Modes", "Evidence Strength", "Output Template"]
SKELETON_COVERAGE_FLOOR = 91  # v0.1.6 backfill batch 1: five-whys + all of go-to-market


def index_files():
    return sorted(REFS.glob("*/index.md"))


def methodology_files():
    return sorted(f for f in REFS.glob("*/*.md") if f.name != "index.md")


def backtick_md_refs(text):
    return re.findall(r"`([^`]*?\.md)`", text)


def skill_ref_exists(ref):
    """SKILL.md uses three reference styles: repo-root relative paths
    (references/.../x.md), category shorthands (strategy/index.md), and the
    generic `index.md` (covered by test_every_category_has_index)."""
    if ref == "index.md" or ref.endswith("/index.md") and not ref.startswith("references/"):
        cat = ref.split("/")[0] if "/" in ref else None
        if cat is None:
            return all((d / "index.md").exists() for d in REFS.iterdir() if d.is_dir())
        return (REFS / cat / "index.md").exists()
    return (ROOT / ref).exists()


class TestNavigationLinks(unittest.TestCase):
    """Gap ③: navigation-link integrity was verified manually; now a repo test."""

    def test_all_methodology_links_resolve(self):
        broken = []
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for ref in backtick_md_refs(skill):
            if "<" in ref:  # protocol placeholders: references/<category>/<methodology>.md
                continue
            if not skill_ref_exists(ref):
                broken.append(f"SKILL.md -> {ref}")
        for idx in index_files():
            for ref in backtick_md_refs(idx.read_text(encoding="utf-8")):
                if "<" in ref:
                    continue
                if not ((idx.parent / ref).exists() or (ROOT / ref).exists()):
                    broken.append(f"{idx.relative_to(ROOT)} -> {ref}")
        self.assertEqual(broken, [], f"broken methodology links: {broken}")

    def test_every_category_has_index(self):
        missing = [d.name for d in sorted(REFS.iterdir()) if d.is_dir() and not (d / "index.md").exists()]
        self.assertEqual(missing, [], f"categories without index.md: {missing}")

    def test_every_methodology_listed_in_its_index(self):
        unlisted = []
        for f in methodology_files():
            if f.name not in (f.parent / "index.md").read_text(encoding="utf-8"):
                unlisted.append(str(f.relative_to(ROOT)))
        self.assertEqual(unlisted, [], f"methodologies missing from their index: {unlisted}")


class TestIndexRequiredSections(unittest.TestCase):

    def test_every_index_has_routing_and_information_sections(self):
        for idx in index_files():
            text = idx.read_text(encoding="utf-8")
            for section in INDEX_SECTIONS:
                self.assertIn(section, text, f"{idx.relative_to(ROOT)} missing '{section}'")


class TestEntrySkeleton(unittest.TestCase):
    """Field coverage floor for the entry-skeleton spec (SKILL.md Maintenance Notes)."""

    def test_skeleton_coverage_floor(self):
        complete = 0
        for f in methodology_files():
            text = f.read_text(encoding="utf-8")
            if all(field in text for field in SKELETON_FIELDS):
                complete += 1
        self.assertGreaterEqual(complete, SKELETON_COVERAGE_FLOOR,
                                f"only {complete} entries carry the full skeleton "
                                f"(floor {SKELETON_COVERAGE_FLOOR})")

    def test_no_literal_newline_escapes(self):
        offenders = [str(f.relative_to(ROOT)) for f in methodology_files()
                     if "\\n" in f.read_text(encoding="utf-8")]
        self.assertEqual(offenders, [], f"literal \\n escapes remain in: {offenders}")


class TestAcceptanceScenarios(unittest.TestCase):
    """evals/evals.json holds 4 behavioral acceptance scenarios (single source
    of acceptance truth — the former test-prompts.json copy was removed in
    v0.1.6). pytest cannot execute an LLM; what it can hold is the structural
    regression: the routing assets each scenario depends on must stay in place."""

    PROMPTS = ROOT / "evals" / "evals.json"

    @classmethod
    def setUpClass(cls):
        data = json.loads(cls.PROMPTS.read_text(encoding="utf-8"))
        cls.scenarios = {s["id"]: s for s in data["evals"]}
        cls.skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

    def test_prompts_inventory(self):
        self.assertEqual(sorted(self.scenarios), [1, 2, 3, 4])
        for sid, s in self.scenarios.items():
            for key in ("scenario", "prompt", "expected_output"):
                self.assertTrue(s.get(key), f"scenario {sid} missing '{key}'")

    def test_scenario_1_root_cause_routing(self):
        # "root cause→5 Whys" quick routing must exist, and the primary reference
        # must be executable (steps + template present).
        self.assertIn("root cause→5 Whys", self.skill)
        five_whys = (ROOT / "references/problem-diagnosis/five-whys.md").read_text(encoding="utf-8")
        self.assertIn("Execution Steps", five_whys)
        self.assertIn("Output Template", five_whys)

    def test_scenario_2_combination_ordering(self):
        # The PESTLE → SWOT chain in scenario 2 is governed by the ordering table;
        # the combination cap and checkpoints must exist to sequence it.
        self.assertIn("PESTLE → SWOT", self.skill)
        self.assertIn("Combination cap", self.skill)
        self.assertIn("at most 3 methodologies", self.skill)
        for name in ("pestle", "swot"):
            self.assertTrue((ROOT / f"references/strategy/{name}.md").exists())

    def test_scenario_3_severe_information_degradation(self):
        # L4 degradation: Cynefin/Framework Selection first, then direct best judgment.
        self.assertIn("| L4 |", self.skill)
        self.assertIn("direct best judgment", self.skill)
        for ref in ("references/structured-thinking/cynefin.md",
                    "references/structured-thinking/framework-selection.md"):
            self.assertTrue((ROOT / ref).exists(), f"L4 fallback asset missing: {ref}")

    def test_scenario_4_correction_once_then_none(self):
        # Correction: stop → explain → at most one re-route → NONE terminal exit.
        self.assertIn("at most one re-route", self.skill)
        self.assertIn("return NONE", self.skill)
        # the fitness gate the replacement must clear
        self.assertIn("task alignment ≥ 4", self.skill)


if __name__ == "__main__":
    unittest.main()
