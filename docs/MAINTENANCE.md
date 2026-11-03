# Kueiku Maintenance & Contribution Rules

维护者文档——不随 agent 会话加载（SKILL.md 只留一行指针）。改动 kueiku 前先读这里。

## Methodology counts are generated

"N categories × M methodologies" figures in SKILL.md and `skill.json` come from:

```bash
python3 scripts/count_methodologies.py   # also writes scripts/methodology-count.json
```

After adding/removing anything under `references/`, re-run it and update the numbers in SKILL.md and `skill.json`.

## Adding a methodology

Update the category's `index.md` table, minimum information requirements, and routing trigger signals.

**Entry skeleton** — Every methodology entry must carry a **When NOT to use** boundary (where the framework misleads or wastes effort, not only where it shines), **Failure Modes** (how its output typically goes wrong + the countermeasure), **Evidence Strength** (an honest grade — strong / mixed / contested / practitioner consensus; never launder numbers), and **Output Template** (a copy-pasteable scaffold), on top of Core Concept / Applicable Scenarios / Key Steps / Source. **Write mechanism, not persona** — entries prescribe judgment rules, never style imitation. Worked example: `references/product-growth/jtbd.md`.

Backfill status: entries added from v0.1.5 on ship complete, and the legacy corpus reached full coverage in v0.1.14 (**149/149 as of 2026-11-04**; batches: five-whys + all of go-to-market in v0.1.6, then the remaining 58 in v0.1.14 across quant+financial, decision+structured-thinking, market/user-research+product-growth+product-discovery+strategy, engineering, leadership+industry+product-philosophy+data-analysis). `tests/test_navigation.py` holds the regression floor at 149 — new entries must ship complete. The floor test checks presence only; content quality remains a human review duty.

## Admission verdict — one of four

**Build** (new entry) / **Fold into X** (merge into an existing entry) / **Recipe** (cross-reference it from an index or combination, no new file) / **Reject** (outside a navigation map's scope). Record the verdict and reason in the entry's Source section; never add a stub to pad the count.

Precedents: Inversion → Fold into `references/decision-making/premortem-counterfactual.md` (same failure-rehearsal mechanism, v0.1.6); cognitive-bias self-check → Recipe (data-analysis already owns `Cognitive & Statistical Bias Checklist`; structured-thinking holds a compact pointer in `socratic-questioning.md`, v0.1.6); Thomas–Kilmann conflict modes → Fold into `references/decision-making/principled-negotiation.md` (stance selection as negotiation preamble, v0.1.13); Balanced Scorecard → Recipe (pointer in `okr.md`, strategy→metrics translation, v0.1.13); Fault Tree Analysis → Recipe (pointer in `fmea.md`, deductive top-down twin of FMEA's bottom-up, v0.1.13).

## Adding a category

Add a row to the SKILL.md category overview table and create the corresponding `index.md`.

## Add-must-trim budget rule (SKILL.md)

SKILL.md is resident context in every session where the skill loads — its size is a per-session token tax. Therefore: **any batch that adds content to SKILL.md must trim or compress an equal amount elsewhere in the same batch.** Soft cap: keep SKILL.md under 17,500 characters — measured 17,499 as of the 2026-10-04 doc-drift batch (the v0.1.6 rework took it from 18,662 down to 17,431, and the description unification with skill.json spent part of the trim surplus on restoring trigger words to the marketplace chain). Verify with `wc -m SKILL.md` after every batch. Contributor-facing content (maintenance rules, long usage examples) belongs in `docs/MAINTENANCE.md`, not SKILL.md.

## Repo tooling

- `scripts/skill_lint.py` — repo health lint: `python3 scripts/skill_lint.py .` checks SKILL.md frontmatter, internal `.md` links, JSON assets, and SKILL.md ↔ skill.json version consistency (FAIL blocks, WARN advises; this repo currently passes with 0 FAIL / 1 WARN).
- `scripts/install-skill.sh` — in-repo installer for project-level agent directories: `install | update | uninstall | list-skills | list-agents | status | generate-commands`, with `--target` / `--agent` / `--all-agents` (claude, cursor, windsurf, trae, gemini, copilot, opencode, roocode, qoder); auto-detects multi-skill workspace vs standalone-repo mode.

## Evaluation assets

Three assets, three different jobs — do not merge them:

| Asset | Job | Guard |
| --- | --- | --- |
| `evals/evals.json` | Single source of acceptance truth: 4 end-to-end `evals` scenarios + `routing_cases` (methodology-level routing) | `tests/test_navigation.py` (scenarios), `tests/test_eval_assets.py` (routing cases) |
| `triggers/trigger-queries.json` | Skill-level trigger/near-miss queries; `expect: no` entries carry the owning sibling skill (`owner`) | `tests/test_eval_assets.py` |
| `scripts/validate_skill.py` | Structure validation: frontmatter whitelist, name/description limits, SKILL.md ↔ skill.json description & version consistency | runs in CI (`.github/workflows/release.yml`) and locally before any release |

**routing_cases schema**: `id`, `category` (references/ directory name), `prompt` (real-user phrasing), `kind` (`trigger` or `none`), and for triggers `expected` (methodology name as written in the index table) + `acceptable` (defensible alternatives). **Live scoring is lenient/strict**: lenient = landed in `expected ∪ acceptable`; strict = landed exactly on `expected`. Strict exists to expose "picked something defensible but imprecise" — track both numbers when running evals with an LLM; pytest cannot run them.

**trigger-queries.json convention**: every `expect: "trigger"` query carries a `signal` field quoting a phrase that must exist in the SKILL.md description or some index.md — the static guard fails if editing the description silently breaks a trigger. Known one-way limit: `expect: "no"` entries only get structural checks (owner enum); "does not steal sibling skills' work" can only be proven by live evals, because the sibling repos are outside this repository.

## Release checklist

1. `python3 -m pytest tests -q` — all green
2. `python3 scripts/validate_skill.py` — structure + description/version consistency
3. `python3 scripts/count_methodologies.py` — counts match SKILL.md/skill.json
4. `wc -m SKILL.md` — under the budget cap (characters, not bytes)
5. Bump `skill.json` version and SKILL.md `metadata.version` together (patch +0.0.1 per change batch); tag `vX.Y.Z` to trigger the release workflow

## Reading principle

Only read the corresponding reference file when needed; do not preload all files.
