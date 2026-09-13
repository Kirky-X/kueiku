#!/usr/bin/env python3
"""Count methodology reference files per category.

Single source of truth for the "N categories × M methodologies" figures in
SKILL.md and skill.json. A methodology = one non-index .md file under
references/<category>/.

Run after adding/removing any file under references/ and update SKILL.md,
skill.json accordingly:

    python3 scripts/count_methodologies.py
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFS = ROOT / "references"


def main():
    categories = sorted(p for p in REFS.iterdir() if p.is_dir())
    if not categories:
        print("No category directories found under references/", file=sys.stderr)
        sys.exit(1)

    counts = {}
    for cat in categories:
        mds = sorted(f for f in cat.glob("*.md") if f.name != "index.md")
        counts[cat.name] = [f.relative_to(ROOT).as_posix() for f in mds]

    total = sum(len(v) for v in counts.values())
    print(f"Categories: {len(categories)} | Total methodologies: {total}\n")
    print(f"{'Category':<28} {'Count':>5}  Files")
    print("-" * 72)
    for name, files in counts.items():
        print(f"{name:<28} {len(files):>5}  {', '.join(Path(f).stem for f in files)}")
    print("-" * 72)
    print(f"{'TOTAL':<28} {total:>5}")

    # Machine-readable summary for updating skill.json / SKILL.md tables
    summary = {
        "categories": len(counts),
        "total_methodologies": total,
        "per_category": {name: len(files) for name, files in counts.items()},
    }
    (ROOT / "scripts" / "methodology-count.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("\nWrote scripts/methodology-count.json")


if __name__ == "__main__":
    main()
