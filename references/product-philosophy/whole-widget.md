# Whole Widget

## Core Concept
End-to-end ownership of critical decisions. If a component is core to your product's differentiation, don't outsource it — own the whole widget. Vertical integration for strategic control.

## Applicable Scenarios
✅ **Best for**
- Product architecture decisions
- Build vs buy decisions
- Vertical integration strategy

⚠️ **When NOT to use**
- Everything called "core": integration desire for control flags on every component — the analysis exists to rank, so most components must lose
- Thin markets with excellent suppliers — commodity components with multiple strong vendors punish ownership (you maintain what others share)
- Small teams: owning the whole widget means staffing every layer — the build decision includes a permanent team, not just this quarter's budget

## Key Steps
1. Identify all components/decisions in your product chain
2. For each, ask: "Is this core to our differentiation?"
3. If yes → own it (build in-house, control the decision)
4. If no → consider outsourcing/partnering
5. Validate: do you have end-to-end control of the user experience?

## Output Template

```
Component inventory:
  | Component       | Core to differentiation? | Vendor options today | Decision | Cost of owning      |
  | [input method]  | yes — the moat            | poor fit             | OWN      | [team + roadmap]    |
  | [payments]      | no                        | several excellent    | PARTNER  | [integration cost]  |
  | [cloud hosting] | no                        | several excellent    | BUY      | —                   |

Differentiation chain: [own everything between the user's intent and the differentiated experience]
User-experience control check: where can a partner decision degrade our UX without warning? [list + SLA/escape plan]
Re-decide trigger: [vendor quality collapse / differentiation shifts / cost inversion]
```

## Failure Modes
- Core creep: everything deemed strategic, nothing bought — integration as instinct → force the ranking: name the top-3 differentiating experiences; a component is core only if it shapes those
- Owning a fast-moving commodity: rebuilding what the market iterates monthly (auth, payments rails) → ownership makes sense when your iteration rate can beat the market's, which for commodities it rarely can
- Half ownership: own the component but depend on a vendor for its critical inputs — control theater → check the layer below your "owned" layer before claiming end-to-end control

## Evidence Strength
Practitioner consensus — vertical integration of differentiating layers has iconic case support (integrated hardware/software advantages are well documented) while the transaction-cost literature also explains when markets beat hierarchies; the practical difficulty is that "core" judgments are forward-looking and often wrong in both directions.

## Source
Steve Jobs' philosophy; Horace Dediu's "Whole Widget" concept.
