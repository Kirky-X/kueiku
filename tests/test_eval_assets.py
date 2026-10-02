"""Static guards for the evaluation assets (no LLM in the loop):

evals/evals.json
  - routing_cases: schema, resolvable expected/acceptable names, category
    coverage floor (every category >= 1 trigger case, >= 3 `none` negatives)
triggers/trigger-queries.json
  - every `expect: "trigger"` query carries a `signal` that must appear in
    SKILL.md or some index.md, so editing the description cannot silently
    break a trigger
  - `expect: "no"` entries get structural checks only (owner enum): whether
    a query "steals" a sibling skill's job can only be proven by live evals,
    because sibling repos live outside this repository — the static guard is
    deliberately one-way

Live scoring of routing_cases (needs an LLM): lenient = landed in
`expected | acceptable`, strict = landed exactly on `expected`. Track both.
"""

import json
import re
import unittest
from pathlib import Path

from common import ROOT

REFS = ROOT / "references"

KNOWN_OWNERS = {"diting", "dayv", "ouyezi", "tiangang", "pangu", "cangjie", "none"}


def _table_names():
    """All methodology names across every index.md table (bold first cell)."""
    names = set()
    for idx in sorted(REFS.glob("*/index.md")):
        for line in idx.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\|\s*\*\*(.+?)\*\*\s*\|", line)
            if m:
                names.add(m.group(1).strip())
    return names


def _prefix_of(shorter, longer):
    a, b = shorter.split(), longer.split()
    return len(a) <= len(b) and all(b[i].lower().startswith(a[i].lower()) for i in range(len(a)))


class TestRoutingCases(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data = json.loads((ROOT / "evals" / "evals.json").read_text(encoding="utf-8"))
        cls.cases = data.get("routing_cases", [])
        cls.categories = {p.name for p in REFS.iterdir() if p.is_dir()}
        cls.names = _table_names()

    def resolves(self, name):
        return name in self.names or any(_prefix_of(name, n) for n in self.names)

    def test_schema(self):
        ids, prompts = set(), set()
        for case in self.cases:
            self.assertTrue(case.get("id"), f"missing id: {case}")
            self.assertTrue(case.get("prompt"), f"missing prompt: {case['id']}")
            self.assertIn(case.get("kind"), {"trigger", "none"}, f"bad kind: {case['id']}")
            self.assertNotIn(case["id"], ids, f"duplicate id: {case['id']}")
            self.assertNotIn(case["prompt"], prompts, f"duplicate prompt: {case['id']}")
            ids.add(case["id"])
            prompts.add(case["prompt"])
            if case["kind"] == "trigger":
                self.assertIn(case.get("category"), self.categories, f"unknown category: {case['id']}")
                self.assertTrue(self.resolves(case["expected"]), f"{case['id']}: expected "
                                f"'{case['expected']}' resolves to no methodology")
                for alt in case.get("acceptable", []):
                    self.assertTrue(self.resolves(alt), f"{case['id']}: acceptable '{alt}' "
                                    "resolves to no methodology")
            else:
                self.assertNotIn("expected", case, f"none case must not carry expected: {case['id']}")

    def test_coverage_floor(self):
        covered = {c["category"] for c in self.cases if c["kind"] == "trigger"}
        missing = sorted(self.categories - covered)
        self.assertEqual(missing, [], f"categories without a routing case: {missing}")
        negatives = [c for c in self.cases if c["kind"] == "none"]
        self.assertGreaterEqual(len(negatives), 3, "at least 3 `none` negatives required")
        self.assertGreaterEqual(len(self.cases), 22, "routing-case count regression")


class TestTriggerQueries(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        data = json.loads((ROOT / "triggers" / "trigger-queries.json").read_text(encoding="utf-8"))
        cls.queries = data["queries"]
        corpus = [(ROOT / "SKILL.md").read_text(encoding="utf-8")]
        corpus.extend(p.read_text(encoding="utf-8") for p in sorted(REFS.glob("*/index.md")))
        cls.corpus = "\n".join(corpus).lower()

    def test_structure_and_signals(self):
        prompts = set()
        for entry in self.queries:
            self.assertTrue(entry.get("q"), f"missing q: {entry}")
            self.assertNotIn(entry["q"], prompts, f"duplicate q: {entry['q']}")
            prompts.add(entry["q"])
            self.assertIn(entry.get("expect"), {"trigger", "no"}, f"bad expect: {entry['q']}")
            if entry["expect"] == "trigger":
                signal = entry.get("signal", "")
                self.assertTrue(signal, f"trigger query without signal: {entry['q']}")
                self.assertIn(signal.lower(), self.corpus,
                              f"signal '{signal}' no longer appears in SKILL.md/index.md "
                              f"(trigger silently broken): {entry['q']}")
            else:
                self.assertIn(entry.get("owner"), KNOWN_OWNERS, f"unknown owner: {entry['q']}")


if __name__ == "__main__":
    unittest.main()
