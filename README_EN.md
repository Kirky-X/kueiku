# Kueiku (鬼谷子) — Methodology Compass Skill

[中文](README.md)

[![GitHub Release](https://img.shields.io/github/v/release/Kirky-X/kueiku?style=flat-square)](https://github.com/Kirky-X/kueiku/releases) [![GitHub License](https://img.shields.io/github/license/Kirky-X/kueiku?style=flat-square)](LICENSE)

Kueiku is a methodology navigation skill for AI agents, built in the Google Labs agent-first format (YAML frontmatter + Markdown routing table). It is not yet another analysis tool — it is a **methodology index map**: it guides agents to **choose the right framework first, then use it correctly** before analyzing problems, crafting strategy, making decisions, designing products, researching users, or organizing thinking.

The skill provides an index of 95 methodologies, a quick routing table (task type → recommended methodology), a calling protocol (declare → read reference → gather inputs → execute → gated output), a 4-level degradation path for insufficient information, and a correction mechanism for when a framework turns out to be a poor fit. The full routing table, combination rules, and usage protocol are in [SKILL.md](SKILL.md).

## Features

- **95 methodologies · 18 categories** — covering Problem Diagnosis / Strategic Analysis / Product & Growth / Decision Making / User Research / Structured Thinking / Product Discovery / Go-to-Market / Market Research / Data Analysis / AI Delivery / Execution / Engineering / Product Philosophy / Leadership / Financial Analysis / Research Methodology / Industry Analysis
- **Quick routing table** — match a task type to a primary + backup framework in under 30 seconds
- **Calling protocol** — a 5-step standard flow that makes framework usage explicit and traceable
- **Combination rules** — 14 common methodology combos (e.g. strategic planning: PESTLE → SWOT → OKR)
- **Degradation path** — 4 levels of handling for insufficient information; never force a framework
- **Correction mechanism** — stop immediately and re-route when a framework turns out to be a poor fit
- **Automation tools** — CLI tool for 15 computation-heavy methodologies (RICE / Decision Matrix / Risk Matrix / DuPont / Pareto / FMEA / ICE / Opportunity Score / DCF / EVA / A/B Test / RFM / Cohort / BCG / GE-McKinsey)

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

### 18 categories · 95 methodologies

| Category | Count | When to use |
| -------- | ----- | ----------- |
| 🔍 Problem Diagnosis | 4 | Find root cause, disruptive thinking, 80/20 focus |
| 📊 Strategic Analysis | 23 | Situation assessment, competition, business model, pricing, value chain, strategic evolution |
| 🚀 Product & Growth | 8 | User needs, growth bottleneck, product innovation, metrics |
| ⚖️ Decision Making | 9 | Prioritization, goal setting, risk rehearsal, selection, risk assessment |
| 👥 User Research | 4 | User journey, empathy mapping, decision journey, needs hierarchy |
| 🧠 Structured Thinking | 9 | MECE expression, multi-perspective, assumption clarification, framework selection, systems thinking |
| 🔬 Product Discovery | 8 | Continuous discovery, hypothesis validation, user interviews, experiment design |
| 🚩 Go-to-Market | 7 | Beachhead, ICP, GTM, growth loops, positioning |
| 📈 Market Research | 7 | Market sizing, segmentation, personas, STP, perceptual mapping, tech adoption |
| 📉 Data Analysis | 4 | Cohort, A/B testing, metrics, RFM |
| 🤖 AI Delivery | 2 | Shipping artifacts, doc-code drift |
| 🏃 Execution | 4 | Outcome roadmap, strategy red team, agile requirements |
| 💻 Engineering | 4 | TDD, bite-sized plan, service contracts, Agent DX |
| 🎯 Product Philosophy | 4 | Radical focus, vertical integration, tech+humanities, invisible perfection |
| 👑 Leadership | 3 | Reality distortion field, A-player density, change management |
| 💰 Financial Analysis | 4 | DuPont, DCF, comparable company, EVA |
| 📚 Research Methodology | 1 | Systematic research process |
| 🏭 Industry Analysis | 2 | Industry value chain, Gartner Hype Cycle |

Full methodology list and routing: see [SKILL.md category overview](./SKILL.md).

### `references/` — 95 methodology reference files

Each methodology has a corresponding `references/<category>/<methodology>.md` containing execution steps and output templates. Read only the relevant file when needed; do not preload all of them.

```
references/
├── problem-diagnosis/        (4)  5 Whys / Fishbone / First Principles / Pareto
├── strategy/                 (23) SWOT / PESTLE / Porter's / BMC / Ansoff / Blue Ocean / Wardley Mapping ...
├── product-growth/            (8) AARRR / JTBD / Design Thinking / Lean BML / VPC / SCAMPER / Kano / North Star
├── decision-making/           (9) RICE / Eisenhower / OKR / Pre-mortem / Decision Matrix / MoSCoW / FMEA / Risk Matrix
├── user-research/             (4) Customer Journey / Empathy Map / Consumer Decision Journey / Maslow
├── structured-thinking/       (9) MECE+Pyramid / Six Hats / Socratic / Cynefin / Second-Order / Systems Thinking ...
├── product-discovery/         (8) OST / Mom Test / ICE / Opportunity Score / Pretotypes / Assumption Mapping ...
├── go-to-market/              (7) Beachhead / ICP / GTM Motions / GTM Strategy / Growth Loops / Battlecard / Positioning
├── market-research/           (7) Market Sizing / Segmentation / User Personas / STP / Perceptual Mapping ...
├── data-analysis/             (4) Cohort / A/B Test / Lean Analytics / RFM
├── ai-delivery/               (2) Shipping Artifacts / Intended vs Implemented
├── execution/                 (4) Outcome Roadmap / Strategy Red Team / User Stories / Job Stories
├── engineering/               (4) TDD / Bite-Sized Plan / Typed Service Contracts / Agent DX
├── product-philosophy/        (4) Focus as No / Whole Widget / Technology Meets Humanities / Invisible Perfection
├── leadership/                (3) Reality Distortion Field / A-Player Density / Change Management
├── financial-analysis/        (4) DuPont / DCF / Comparable Company / EVA
├── research-methodology/      (1) Systematic Research Process
└── industry-analysis/         (2) Industry Value Chain / Gartner Hype Cycle
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
