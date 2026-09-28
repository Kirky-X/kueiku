# Focus as No

## Core Concept
Focus is not about saying "yes" to the right things — it's about saying "no" to everything else. Radical subtraction to lock the minimum viable set. Every "yes" to a feature is a "no" to simplicity.

## Applicable Scenarios
✅ **Best for**
- Product scope decisions
- Feature trade-offs
- Preventing product bloat

⚠️ **When NOT to use**
- Compliance, safety, and platform obligations — "remove it" isn't available; scope them separately from discretionary features
- Early exploration before a core purpose is defined — subtraction needs an anchor; with no stated purpose, every feature is defensible
- Multi-sided products without per-side analysis — a feature bloating one side may be essential to the other; cut per side, not globally

## Key Steps
1. List all current features/requirements/proposals
2. For each item, ask: "If we remove this, does the product fail its core purpose?"
3. If no → it's a candidate for removal or deferral
4. Apply the "Hell Yes or No" filter: if you're not excited about it, say no
5. Lock the minimum set; defend it against scope creep

## Output Template

```
Core purpose (one sentence): [what the product must do to justify existing]

| Item          | Remove → product still serves core purpose? | Verdict        | Deferral condition        |
| ------------- | ------------------------------------------- | -------------- | ------------------------- |
| [exports]     | yes                                          | defer          | [revisit when 10+ asks/qtr]|
| [core editor] | no                                           | keep           | —                          |
| [admin theme] | yes                                          | cut            | —                          |

Scope-creep gate: new proposals answer "what does this replace?" — additions without substitutions need [explicit owner] approval
Revisit: [date] — is the minimum set still minimum, and did any cut break a promised workflow?
```

## Failure Modes
- Subtraction theater: cutting the rare-but-critical escape hatch (export, undo) that the core purpose quietly depends on → simulate the cut: walk a real task end-to-end without the item before verdicts
- "Hell yes" as veto: enthusiasm-based filtering kills necessary-but-dull requirements (onboarding, billing) → apply the excitement filter to discretionary items only; obligations get a different gate
- No defense after the workshop: the locked set erodes feature by feature → publish the list, log every exception, and count exceptions per quarter — creep that's visible gets resisted

## Evidence Strength
Practitioner consensus — a philosophy with strong practitioner advocacy (37signals lineage, essentialism literature) and intuitive support from scope-creep failure modes; there is no controlled evidence for the specific filters, and aggressive subtraction has real documented failure cases when core purpose is misstated — the method is only as good as the purpose statement it serves.

## Source
Jason Fried & David Heinemeier Hansson, *It Doesn't Have to Be Crazy at Work*; essentialism philosophy.
