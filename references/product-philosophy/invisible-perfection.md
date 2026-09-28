# Invisible Perfection

## Core Concept
Internal craft quality determines external user experience. The unseen parts (code quality, internal tools, infrastructure) must be polished to the same standard as user-facing features. Users may never see the internals, but they feel the difference.

## Applicable Scenarios
✅ **Best for**
- Code quality standards
- Internal tool investment decisions
- Craft standard setting

⚠️ **When NOT to use**
- As a blanket rule against pragmatism: some internals genuinely are throwaway (spikes, prototypes) — polish proportional to lifespan
- Used to gold-plate: infinite refactoring in the name of craft while user-visible problems rot — the philosophy says internals shape experience, not that internals outrank experience
- Uneconomic domains: internal quality standard must still price the benefit; polish with no plausible user-experience payoff is cost

## Key Steps
1. List all "invisible" quality points: code quality, test coverage, internal tools, documentation, infrastructure
2. For each, assess: does this affect the user experience (directly or indirectly)?
3. Set quality standards for invisible items equal to visible items
4. Invest in internal tooling with the same rigor as external products
5. Monitor: are invisible quality points degrading?

## Output Template

```
| Invisible quality point | Path to user experience                     | Standard (same bar as visible?) | Current state | Trend |
| ----------------------- | ------------------------------------------- | ------------------------------- | ------------- | ----- |
| [build pipeline speed]  | [slow builds → slower fixes → stale bugs]   | [p95 < 10 min]                  | [18 min]      | ↓     |
| [error messages from API]| [direct user contact]                       | [actionable, localized]         | [stack traces] | →    |
| [internal admin tool]   | [support latency → user wait time]           | [support task < 5 min]          | [meets bar]   | →     |

Investment queue (UX-linked, ranked by user-experience impact): 1. [...] 2. [...]
Explicitly unpolished (prototype-grade, lifespan-limited): [items + why acceptable]
Monitor: [definition of done includes invisible items? degradation alerts on pipeline/tooling?]
```

## Failure Modes
- Craft as identity: polishing invisible internals nobody experiences while shipping quality slips on what users see → every invisible investment states its user-experience causal path; no path, no slot in the queue
- Uniform standard applied blindly: prototype code polished to production bar, production code left rough → standards attach to lifespan and blast radius, not to "internal vs external" alone
- No monitoring: decay invisible by definition — nobody notices until users feel it → the quality points list gets the same alerts/owners as user-facing SLOs

## Evidence Strength
Practitioner consensus — the causal chain (internal quality → iteration speed → user-experienced quality) is well argued and consistent with software-engineering research linking code quality to development velocity; the specific "equal polish" prescription is philosophy rather than measured policy, and its economics are context-dependent.

## Source
Pixar's philosophy: "The art challenges the technology, and the technology inspires the art." Applied to software engineering.
