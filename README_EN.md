# Kueiku (鬼谷子) — Methodology Compass Skill

[![GitHub Release](https://img.shields.io/github/v/release/Kirky-X/kueiku?style=flat-square)](https://github.com/Kirky-X/kueiku/releases)
[![GitHub License](https://img.shields.io/github/license/Kirky-X/kueiku?style=flat-square)](LICENSE)

Kueiku is a methodology navigation skill for AI agents, built in the Google Labs agent-first format (YAML frontmatter + Markdown routing table). It is not yet another analysis tool — it is a **methodology index map**: it guides agents to **choose the right framework first, then use it correctly** before analyzing problems, crafting strategy, making decisions, designing products, researching users, or organizing thinking.

The skill provides an index of 35 methodologies, a quick routing table (task type → recommended methodology), a calling protocol (declare → read reference → gather inputs → execute → gated output), a 4-level degradation path for insufficient information, and a correction mechanism for when a framework turns out to be a poor fit. The full routing table, combination rules, and usage protocol are in [SKILL.md](SKILL.md).

## Features

- **35 methodologies · 6 categories** — covering Problem Diagnosis / Strategic Analysis / Product & Growth / Decision Making / User Research / Structured Thinking
- **Quick routing table** — match a task type to a primary + backup framework in under 30 seconds
- **Calling protocol** — a 5-step standard flow that makes framework usage explicit and traceable
- **Combination rules** — 14 common methodology combos (e.g. strategic planning: PESTLE → SWOT → OKR)
- **Degradation path** — 4 levels of handling for insufficient information; never force a framework
- **Correction mechanism** — stop immediately and re-route when a framework turns out to be a poor fit

## Installation

### Option 1: Install via the `skills` package (recommended)

Requires [Node.js](https://nodejs.org/) 18+ and the `skills` npm package (v1.5.12+). `skills` is the CLI of the open agent skills ecosystem, supporting 68+ agents (Claude Code / Trae / Cursor / Codex / OpenCode, etc.).

```bash
# Install to Claude Code
npx skills add https://github.com/Kirky-X/kueiku.git --agent claude-code -y

# Equivalent shorthand (owner/repo)
npx skills add Kirky-X/kueiku --agent claude-code -y

# Install to Trae
npx skills add Kirky-X/kueiku --agent trae -y

# List all discoverable skills in the repo (without installing)
npx skills add https://github.com/Kirky-X/kueiku.git --list
```

After installation the skill files live in the agent's skills directory (e.g. `.claude/skills/kueiku/`).

### Option 2: Traditional git clone

```bash
git clone https://github.com/Kirky-X/kueiku.git
# Link or copy SKILL.md + references/ into the agent skills directory
# Example skills directory paths per runtime (pick one):
#   Claude Code:  ~/.claude/skills/kueiku/
#   Trae:         ~/.trae-cn/skills/kueiku/
#   Cursor:       ~/.cursor/skills/kueiku/
#   Codex:        ~/.codex/skills/kueiku/
```

## Usage Examples

Once loaded as a skill, Kueiku is triggered by natural-language intent — no explicit command needed. The full task-type → methodology routing is in the [SKILL.md quick routing table](./SKILL.md).

| Task type | Recommended methodology | One-line function |
| --------- | ----------------------- | ----------------- |
| Find root cause | 5 Whys | Ask "why" repeatedly to pierce through symptoms |
| Strategic assessment | SWOT | Internal strengths/weaknesses × external opportunities/threats |
| Growth bottleneck | AARRR Funnel | Acquisition→Activation→Retention→Referral→Revenue |
| Requirement prioritization | RICE Scoring | Reach×Impact×Confidence÷Effort quantification |
| True user needs | JTBD | Users hire products to get a "job" done |
| Business model design | Business Model Canvas | 9-block complete business model |
| Pre-decision risk rehearsal | Pre-mortem | Imagine failure scenarios in reverse |
| Structured expression | MECE + Pyramid | Mutually exclusive, collectively exhaustive + conclusion first |

## Capability Overview

### 6 categories · 35 methodologies

| Category | Methodologies | When to use |
| -------- | ------------- | ----------- |
| 🔍 Problem Diagnosis | 5 Whys / Fishbone / First Principles / Pareto | Known problem, need root cause |
| 📊 Strategic Analysis | SWOT / PESTLE / Porter's Five Forces / BMC / Stakeholder / Ansoff / Blue Ocean / McKinsey 7S / BCG | Assess situation, set direction |
| 🚀 Product & Growth | AARRR / JTBD / Design Thinking / Lean BML / VPC / SCAMPER / Kano / North Star | Product design, growth, validation |
| ⚖️ Decision Making | RICE / Eisenhower / OKR / Pre-mortem / Decision Matrix / MoSCoW / FMEA | Defensible choices among options |
| 👥 User Research | Customer Journey / Empathy Map | Deeply understand user needs and pain points |
| 🧠 Structured Thinking | MECE+Pyramid / Six Thinking Hats / Socratic / Cynefin / Second-Order Thinking | Organize complex info, clarify assumptions |

### `references/` — 35 methodology reference files

Each methodology has a corresponding `references/xxx.md` containing execution steps and output templates. Read only the relevant file when needed; do not preload all of them.

```
references/
├── five-whys.md                  5 Whys root-cause analysis
├── fishbone.md                   Fishbone / Ishikawa diagram
├── first-principles.md           First Principles thinking
├── pareto.md                     Pareto analysis
├── swot.md                       SWOT analysis
├── pestle.md                     PESTLE macro-environmental analysis
├── porter-five-forces.md         Porter's Five Forces
├── business-model-canvas.md      Business Model Canvas
├── stakeholder-mapping.md        Stakeholder mapping
├── ansoff-matrix.md              Ansoff Matrix
├── blue-ocean.md                 Blue Ocean Strategy
├── mckinsey-7s.md                McKinsey 7S framework
├── bcg-matrix.md                 BCG Matrix
├── aarrr.md                      AARRR growth funnel
├── jtbd.md                       Jobs-to-be-Done
├── design-thinking.md            Design Thinking
├── lean-bml.md                   Lean Build-Measure-Learn
├── value-proposition-canvas.md   Value Proposition Canvas
├── scamper.md                    SCAMPER creativity triggers
├── kano.md                       Kano Model
├── north-star.md                 North Star Framework
├── rice.md                       RICE prioritization scoring
├── eisenhower.md                 Eisenhower Matrix
├── okr.md                        OKR (Objectives & Key Results)
├── premortem-counterfactual.md   Pre-mortem & Counterfactual thinking
├── decision-matrix.md            Decision Matrix
├── moscow.md                     MoSCoW method
├── fmea.md                       FMEA (Failure Mode & Effects Analysis)
├── customer-journey.md           Customer Journey Map
├── empathy-map.md                Empathy Map
├── mece-pyramid.md               MECE + Pyramid Principle
├── six-thinking-hats.md          Six Thinking Hats
├── socratic-questioning.md       Socratic Questioning
├── cynefin.md                    Cynefin framework
└── second-order-thinking.md      Second-Order Thinking
```

## Calling Protocol

Standard flow for invoking a methodology:

```
0. Pre-check    → Confirm the task type matches the routing table; confirm information sufficiency
1. Declare      → State which methodology is used and why
2. Read ref     → Extract execution steps and output template
3. Gather input → Confirm inputs item by item; handle missing items via the degradation path
4. Execute      → Output step by step, tagging the source of each piece of information
5. Gated output → Conclusion must directly answer the question + actionable advice + confidence
```

## FAQ

### Required `skills` package version?

The `skills` npm package **v1.5.12+** is required. `skills` is the CLI of the [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) ecosystem, supporting 68+ agents. Use `npx skills@latest` to get the latest version.

### When should I NOT use a framework?

- The task is simple and clear; a framework would add unnecessary complexity
- The user explicitly asks for a direct answer
- Information is severely missing (Level 4); even framework selection cannot be determined

In these cases, state it directly, give your best judgment, and label confidence and dependent assumptions.

### What if information is insufficient?

Follow the 4-level degradation path: Level 1 normal execution → Level 2 label assumptions and to-collect items → Level 3 stop and ask key questions → Level 4 fall back to best judgment. See [SKILL.md degradation path](./SKILL.md).

### What if the wrong framework was chosen?

If during execution you find the framework is a poor fit (a key dimension can't be filled and it's not an information issue, the conclusion drifts from the question, or the user says it's the wrong direction), stop immediately, explain what was done and why it doesn't fit, re-select from the routing table, and explain the switch.

## License

MIT
