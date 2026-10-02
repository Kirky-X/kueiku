#!/usr/bin/env python3
"""Skill structure validation (pattern absorbed from anthropics/skills
quick_validate; implementation original, stdlib only).

Guards the failure modes that actually bit this repo:
  - frontmatter keys outside the allowed set
  - name not kebab-case / over the length limit
  - description empty / over 1024 chars / containing angle brackets
  - SKILL.md metadata.version drifting from skill.json version
  - SKILL.md description drifting from skill.json description (the
    marketplace chain exposes only skill.json — a fork there silently
    drops every trigger word; this fork shipped in v0.1.5)

Exit 0 with an OK line, or exit 1 printing every finding (failures are
never swallowed). Run in CI (release.yml) and before any release:

    python3 scripts/validate_skill.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_MD = ROOT / "SKILL.md"
SKILL_JSON = ROOT / "skill.json"

ALLOWED_FRONTMATTER_KEYS = {"name", "description", "license", "metadata"}
ALLOWED_METADATA_KEYS = {"version", "author", "repo", "tags"}
MAX_NAME_LEN = 64
MAX_DESCRIPTION_LEN = 1024


def parse_frontmatter(text):
    """Return (dict of top-level keys, error string). Minimal YAML: only what
    this skill's frontmatter uses (quoted strings, one nested mapping)."""
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}, "SKILL.md has no frontmatter block (--- ... ---)"
    fields, current_key = {}, None
    for lineno, line in enumerate(m.group(1).splitlines(), start=2):
        if not line.strip():
            continue
        if line.startswith("  "):
            if current_key is None:
                return {}, f"line {lineno}: indented line outside a mapping"
            sub = line.strip().split(":", 1)
            if len(sub) == 2:
                fields[current_key][sub[0].strip()] = sub[1].strip().strip('"')
        else:
            key, _, value = line.partition(":")
            current_key = key.strip()
            fields[current_key] = value.strip()
            if fields[current_key] == "":
                fields[current_key] = {}
    return fields, ""


def strip_quotes(value):
    if isinstance(value, dict):  # empty frontmatter value parsed as a mapping
        return ""
    return value[1:-1] if len(value) >= 2 and value[0] == value[-1] == '"' else value


def main():
    findings = []

    text = SKILL_MD.read_text(encoding="utf-8")
    fields, err = parse_frontmatter(text)
    if err:
        print(err)
        sys.exit(1)

    unexpected = set(fields) - ALLOWED_FRONTMATTER_KEYS
    if unexpected:
        findings.append(f"frontmatter has keys outside {sorted(ALLOWED_FRONTMATTER_KEYS)}: {sorted(unexpected)}")

    name = strip_quotes(fields.get("name", ""))
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        findings.append(f"name '{name}' is not kebab-case")
    if len(name) > MAX_NAME_LEN:
        findings.append(f"name exceeds {MAX_NAME_LEN} chars")

    description = strip_quotes(fields.get("description", ""))
    if not description:
        findings.append("description is empty")
    if len(description) > MAX_DESCRIPTION_LEN:
        findings.append(f"description is {len(description)} chars (limit {MAX_DESCRIPTION_LEN})")
    if "<" in description or ">" in description:
        findings.append("description contains angle brackets")

    metadata = fields.get("metadata", {})
    if not isinstance(metadata, dict):
        findings.append("metadata is not a mapping")
        metadata = {}
    bad_meta = set(metadata) - ALLOWED_METADATA_KEYS
    if bad_meta:
        findings.append(f"metadata has keys outside {sorted(ALLOWED_METADATA_KEYS)}: {sorted(bad_meta)}")
    fm_version = strip_quotes(metadata.get("version", ""))

    if not SKILL_JSON.exists():
        findings.append("skill.json missing")
    else:
        import json
        try:
            data = json.loads(SKILL_JSON.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            findings.append(f"skill.json is not valid JSON: {e}")
            data = {}
        if data.get("name") != name:
            findings.append(f"skill.json name '{data.get('name')}' != SKILL.md name '{name}'")
        if data.get("version") != fm_version:
            findings.append(f"version drift: skill.json {data.get('version')!r} != "
                            f"SKILL.md metadata.version {fm_version!r}")
        if data.get("description") != description:
            findings.append("description drift: skill.json and SKILL.md descriptions differ — "
                            "the marketplace chain exposes only skill.json, so a fork here "
                            "silently drops trigger words; make both byte-identical")
        if not data.get("license"):
            findings.append("skill.json has no license")

    if findings:
        print("validate_skill: FAILED")
        for f in findings:
            print(f"  - {f}")
        sys.exit(1)
    print(f"validate_skill: OK (name={name} version={fm_version} description={len(description)} chars)")


if __name__ == "__main__":
    main()
