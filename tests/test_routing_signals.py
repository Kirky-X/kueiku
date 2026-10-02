"""Routing-layer consistency guards for every references/<category>/index.md.

Idea absorbed from cc-thinking-skills `evals/` (structural conformance checks
that run for free against static content, plus routing-boundary fixtures);
the implementation below is original. Covers the index.md layer only —
SKILL.md-layer count consistency lives in test_consistency.py.

Guards:
  1. every methodology-table Reference points to an existing file
  2. every Routing Trigger Signals target resolves to a real methodology
     (own table, any other table, a category-annotated cross-reference,
     or a controlled shorthand)
  3. "Minimum Information Requirements per Methodology" covers every
     methodology in the table (slash-merged entries like "5 Whys / Fishbone"
     count as covering both)
  4. every Common Combinations member resolves to a real methodology
"""

import re
import unittest
from pathlib import Path

from common import ROOT

REFS = ROOT / "references"

TRIGGER_SECTION = "## Routing Trigger Signals"
MININFO_SECTION = "## Minimum Information Requirements per Methodology"
COMBO_SECTION = "## Common Combinations"

# Lowercase words allowed inside a methodology name ("Intended vs Implemented");
# any other lowercase token ends the name ("Comparable Company cross-validation").
CONNECTIVES = {"and", "or", "vs", "by", "as", "of", "the", "&", "to", "for", "in", "with", "a", "an"}


def _tokens(name):
    return [t for t in re.split(r"\s+", name.strip()) if t]


def _prefix_of(shorter, longer):
    """True if `shorter` is a case-insensitive token-wise prefix of `longer`."""
    a, b = _tokens(shorter), _tokens(longer)
    return len(a) <= len(b) and all(b[i].lower().startswith(a[i].lower()) for i in range(len(a)))


def _display_to_dir():
    """SKILL.md category table: display name -> references/ directory name."""
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    row = re.compile(
        r"^\|\s*\d+\s*\|\s*([^|]+?)\s*\|\s*\d+\s*\|\s*`references/([^/]+)/index\.md`", re.M)
    return {display.strip(): directory for display, directory in row.findall(skill)}


def _section(text, header):
    m = re.search(re.escape(header) + r"\n(.*?)(?=\n## |\Z)", text, re.S)
    return m.group(1) if m else None


def _name_from_segment(segment):
    """Leading methodology name from a combination segment, or None for
    lowercase connective phrases like "if none work"."""
    cleaned = re.sub(r"\([^)]*\)", " ", segment)
    parts = _tokens(cleaned)
    if not parts or not (parts[0][0].isupper() or parts[0][0].isdigit()):
        return None
    taken = []
    for i, part in enumerate(parts):
        bare = part.rstrip(".,;:")
        if part[0].isupper() or part[0].isdigit():
            taken.append(bare)
        elif i > 0 and bare.lower() in CONNECTIVES:
            taken.append(part)
        else:
            break
    return " ".join(taken).strip() or None


class TestRoutingSignals(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.display_to_dir = _display_to_dir()
        cls.tables = {}
        for cat in sorted(p for p in REFS.iterdir() if p.is_dir()):
            idx = cat / "index.md"
            if idx.exists():
                text = idx.read_text(encoding="utf-8")
                cls.tables[cat.name] = {
                    "path": idx,
                    "text": text,
                    "names": {m.group(1).strip() for line in text.splitlines()
                              if (m := re.match(r"\|\s*\*\*(.+?)\*\*\s*\|", line))},
                }
        cls.all_names = set().union(*(c["names"] for c in cls.tables.values()))

    def resolves(self, name, cat):
        """A reference resolves if it hits a table name exactly (own or any
        category) or is a controlled shorthand: a token-wise prefix of some
        table name ("RICE" -> "RICE Scoring", "Cynefin" -> "Cynefin Framework")."""
        if name in self.all_names:
            return True
        return any(_prefix_of(name, n) for n in self.all_names)

    def resolves_annotated(self, name, annotation, cat):
        """Resolve a category-annotated reference like "JTBD (Product & Growth)"
        strictly inside the named target category."""
        target = self.display_to_dir.get(annotation)
        if target is None or target not in self.tables:
            return False
        names = self.tables[target]["names"]
        return name in names or any(_prefix_of(name, n) for n in names)

    def test_table_references_point_to_existing_files(self):
        missing = []
        for cat, info in sorted(self.tables.items()):
            for line in info["text"].splitlines():
                m = re.match(r"\|\s*\*\*(.+?)\*\*\s*\|[^|]*\|[^|]*\|\s*`([^`]+)`\s*\|\s*$", line)
                if not m:
                    continue
                name, ref = m.group(1).strip(), m.group(2).strip()
                if not (info["path"].parent / ref).exists():
                    missing.append(f"{cat}/{name}: Reference `{ref}` does not exist")
        self.assertEqual(missing, [])

    def test_trigger_signal_targets_resolve(self):
        dangling = []
        for cat, info in sorted(self.tables.items()):
            body = _section(info["text"], TRIGGER_SECTION)
            self.assertIsNotNone(body, f"{cat}: missing '{TRIGGER_SECTION}' section")
            for line in body.splitlines():
                primary = re.search(r"→\s*([^→]*?)\s*\(primary\)", line)
                if primary:
                    target = re.sub(r"^use\s+", "", primary.group(1).strip()).strip()
                    if not self.resolves(target, cat):
                        dangling.append(f"{cat}: primary trigger '{target}' resolves to no methodology")
                for m in re.finditer(r"→\s*use\s+([^;]+)", line):
                    seg = m.group(1).strip().rstrip(";").strip()
                    ann = re.search(r"\s*\(([^)]*)\)\s*$", seg)
                    if ann:
                        name, label = seg[:ann.start()].strip(), ann.group(1).strip()
                        if self.resolves_annotated(name, label, cat):
                            continue
                    if not self.resolves(seg, cat):
                        dangling.append(f"{cat}: fallback trigger '{seg}' resolves to no methodology")
        self.assertEqual(dangling, [])

    def test_minimum_info_covers_every_methodology(self):
        def covers(entry, name):
            if name == entry or _prefix_of(name, entry) or _prefix_of(entry, name):
                return True
            parts = re.split(r"\s*/\s*", entry)
            return len(parts) > 1 and any(
                name == p or _prefix_of(name, p) or _prefix_of(p, name) for p in parts)

        uncovered = []
        for cat, info in sorted(self.tables.items()):
            body = _section(info["text"], MININFO_SECTION)
            self.assertIsNotNone(body, f"{cat}: missing '{MININFO_SECTION}' section")
            entries = {m.group(1).strip() for m in
                       (re.match(r"-\s*\*\*(.+?)\*\*:", line) for line in body.splitlines()) if m}
            for name in sorted(info["names"]):
                if not any(covers(e, name) for e in entries):
                    uncovered.append(f"{cat}: '{name}' has no Minimum Information Requirements entry")
        self.assertEqual(uncovered, [])

    def test_combination_members_resolve(self):
        dangling = []
        for cat, info in sorted(self.tables.items()):
            body = _section(info["text"], COMBO_SECTION)
            if body is None:  # combinations are optional ("Where present", SKILL.md)
                continue
            for line in body.splitlines():
                if not line.strip().startswith("- **"):
                    continue
                combo = re.match(r"-\s*\*\*(.+?)\*\*:\s*(.*)$", line.strip())
                entry, rest = combo.group(1), combo.group(2)
                for segment in re.split(r"→|\+", rest):
                    name = _name_from_segment(segment)
                    if name is None:
                        continue
                    if "/" in name and not self.resolves(name, cat):
                        parts = [p.strip() for p in name.split("/")]
                        if all(self.resolves(p, cat) for p in parts):
                            continue
                    if not self.resolves(name, cat):
                        dangling.append(f"{cat}: combination '{entry}' references '{name}' "
                                        "which resolves to no methodology")
        self.assertEqual(dangling, [])


if __name__ == "__main__":
    unittest.main()
