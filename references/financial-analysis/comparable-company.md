# Comparable Company Analysis

## Core Concept
Infer a target company's value by applying valuation multiples from similar publicly traded companies. Common multiples: P/E, EV/EBITDA, EV/Revenue, P/B.

## Applicable Scenarios
✅ **Best for**
- IPO pricing
- M&A valuation
- Industry comparison

⚠️ **When NOT to use**
- No true peers — companies differing in growth, margin structure, or capital intensity make any multiple comparison garbage; if you adjust more than you compare, switch to **DCF**
- Broken denominators — negative or trough-cycle earnings make P/E and EV/EBITDA exist but signal nothing
- Sector-wide mispricing — comps price relative to today's market mood; in a bubble or panic you inherit it with false precision, so pair with an intrinsic check (**DCF**) and give a range, not a point (**Probabilistic Reasoning**)
- Owner-specific value questions — comps give the market-clearing range; synergy or strategic value to a specific acquirer needs a different model

## Key Steps
1. Select 5-10 comparable companies (similar industry, size, growth)
2. Gather financial data and calculate valuation multiples
3. Compute median/mean multiples for the peer group
4. Apply peer multiples to target company's metrics
5. Derive valuation range; cross-validate with DCF if available
6. Document adjustments for differences (growth, margin, risk)

## Output Template

```
Target: [company] — basis: [LTM / NTM], currency, adjustments: [state them]
Peer set: [5-10 companies] — comparability criteria: [industry, size, growth, margin band]
  Excluded: [who and why]
Multiples:
  P/E: peers [x, x, x] — median [x] — selected [x] (why)
  EV/EBITDA: peers [..] — median [x]
  EV/Revenue: peers [..] — median [x]
Applied: target metric [x] × selected multiple [x] → implied value range [low – high]
Adjustment rationale: [growth / margin / risk differences and how the selected multiple accounts for them]
Cross-check: DCF intrinsic value [x] — gap and explanation: [..]
```

## Failure Modes
- Garbage comps: peers chosen for convenience rather than comparability → write the comparability criteria down and name what was excluded and why
- Flattering-multiple selection: switching to EV/Revenue when EBITDA is negative → show all multiples and justify the pick; be suspicious when the chosen one is the highest
- Unadjusted quality gaps: identical multiples across different growth and margins → adjust for the differences or state why they cancel
- Definition drift: peers' "adjusted EBITDA" means different things → normalize non-GAAP definitions before comparing
- Cycle blindness: peak-cycle multiples extrapolated as permanent → use mid-cycle metrics for cyclicals

## Evidence Strength
Practitioner consensus — comps are the market-standard first-pass valuation and benchmark in every deal; the method reliably produces a market-anchored range, but its output is only as good as the peer set and the honesty of the adjustments, and it prices relative value, never intrinsic value.

## Source
Standard investment banking methodology.
