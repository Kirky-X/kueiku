# Balanced Scorecard

## Core Concept
Kaplan & Norton's answer to "how do you know your strategy is working": translate the strategy into a **linked set of objectives and measures across four perspectives** — financial, customer, internal business process, learning & growth — arranged as a strategy map. The perspectives form a causal chain: learning and growth enable process, process delivers customer outcomes, customer outcomes drive financial results. The scorecard's real content is the map (the causal links), not the list of measures.

## Applicable Scenarios
✅ **Best for**
- Translating a chosen strategy into an executable measurement system
- Balancing a metric set that has drifted into "revenue only"
- Cascading strategy across an organization that has disconnected goals from outcomes
- Linking investment in capability to results customers and shareholders feel

⚠️ **When NOT to use**
- A startup or single-team product where one metric suffices → North Star Framework plus input metrics is the right size
- The strategy itself is unsettled → BSC measures a strategy you have not chosen; settle it first (Strategy Red Team, or SWOT)
- Only two perspectives get populated — that is a scorecard, not a Balanced Scorecard, and the causal chain does not exist; use OKR + North Star instead
- Reporting and ranking only → BSC without a decision and an owner per objective is a monthly dashboard nobody acts on
- Attribution-grade questions ("which of these four caused revenue?") → BSC is a monitoring and alignment tool, not a causal-inference method
- Very small teams where measurement overhead exceeds the decision value

## Key Steps
1. Clarify the strategy in one sentence: "we will do X, unlike Y, to win at Z" — no measures yet
2. Build the strategy map: objectives per perspective, linked by explicit cause-and-effect arrows (learning → process → customer → financial); every objective should hang off something above it and support something below
3. Choose measures per objective: prefer leading (process, capability) with a lagging partner (outcome); every measure must have a decision attached ("if this moves, we do Y")
4. Set targets and initiatives: the initiative that moves the objective, not the measure
5. Assign owners and cadence: one owner per objective, a fixed review rhythm; BSC fails on cadence before it fails on content
6. Prune: every measure must have an owner and a decision; an unowned measure is deleted, not deferred

## Output Template

```
Strategy: [one sentence — what we will do differently to win]
Strategy map:
  Learning & growth: [objective] ← [initiative]
  Internal process:  [objective] ← depends on above
  Customer:          [objective] ← depends on above
  Financial:         [objective] ← depends on above
Measures:
  [objective] → [leading measure] + [lagging measure] → [decision if it moves]
Initiatives: [objective → initiative → owner]
Pruned: [measures removed for having no decision attached]
Review cadence: [who, when, what triggers a re-plan]
```

## Failure Modes
- Strategy map of wishes: boxes with arrows drawn after the fact to look causal → draw links only where you can name the mechanism ("faster release → fewer escalations → better retention")
- Activity measures crowding out outcomes ("number of training hours") → keep one outcome measure per objective, pair it with a leading indicator
- The four perspectives collapse into financial + one → the balance is gone; if only finance is filled in, use OKR
- Reporting graveyard: measures are collected and reviewed but no decision ever changes → every measure needs a decision attached; if none exists, delete the measure
- Targets copied from industry benchmarks → the benchmark knows nothing about your strategy; set targets from the strategy's own logic
- Scorecard used for individual performance appraisal → measurement becomes self-protection, numbers stop being trustworthy; keep it at the objective level and out of comp
- Created once and never revisited: the strategy changes, the map does not → set the map's re-derivation trigger (strategy shift, new objective, measure with no decisions for two cycles)
- Confusing it with OKR: BSC organizes measures against a strategy; OKR sets time-boxed goals and key results. They compose — BSC chooses what to measure, OKR moves it — but they are not interchangeable

## Evidence Strength
**Mixed.** Adoption is enormous and the two original studies (over a thousand firms, spanning diverse industries) documented real measurement-system effects. The causal claim — that introducing a BSC causes performance improvement — is weakly supported; later work and the 3.0 revision emphasize learning and strategy formulation rather than scorecard mechanics, and practitioner evidence on measurement systems correlating with performance is stronger than evidence that the causal links in a specific map are real. Use it as a disciplined way to connect strategy to measures, not as a performance formula.

## Source
Robert Kaplan & David Norton, "The Balanced Scorecard—Measures That Drive Performance", *Harvard Business Review* (1992); *The Balanced Scorecard* (1996); *The Execution Premium* (2008). Admission verdict: **Build** (v0.1.15) — the v0.1.13 Recipe verdict (OKR + North Star "own" it) was factually wrong: neither holds the strategy→measures translation, so the pointer in `okr.md` was a dead route. BSC composes with OKR rather than duplicating it (choose what to measure vs move it).
