# BCG Matrix

## Core Concept
Market growth rate × relative market share 4-quadrant product portfolio management: Stars, Cash Cows, Question Marks, Dogs.

## Applicable Scenarios
✅ **Best for**
- Product investment allocation, portfolio balance, business trade-offs

⚠️ **When NOT to use**
- A single-product company or a portfolio of one — there is no portfolio to balance
- Share and growth are poor proxies in your industry (winner-take-all markets, fast commoditization)
- You need today's cash decisions for a young portfolio — positions take years to become readable

## Key Steps
1. List all products/business units
2. For each, determine market growth rate and relative market share
3. Plot on 2×2 matrix: Stars (high growth, high share), Cash Cows (low growth, high share), Question Marks (high growth, low share), Dogs (low growth, low share)
4. Strategy: Invest in Stars, Milk Cash Cows, Decide on Question Marks, Divest Dogs

## Output Template

```
| Product | Market growth | Rel. share | Quadrant      | Action              | Next checkpoint |
| ------- | ------------- | ---------- | ------------- | ------------------- | --------------- |
| [A]     | high          | high       | Star          | Invest to hold lead | [date/metric]   |
| [B]     | low           | high       | Cash Cow      | Milk, fund Stars    | [date/metric]   |
| [C]     | high          | low        | Question Mark | Invest or exit by   | [decision date] |
| [D]     | low           | low        | Dog           | Divest / niche      | [date/metric]   |

Portfolio balance note: [is there a Cow funding the Stars? too many Question Marks?]
```

## Failure Modes
- "Dog" hall of shame: low-share/low-growth businesses that later became winners (the matrix undervalues niches and synergies) → before divesting, check complementarities the matrix cannot see
- Definitions drift: "high growth" relative to what horizon and market? → fix numeric thresholds before plotting
- Self-fulfilling divestment: cutting Dogs starves future Stars → mark Dogs as "decide by [date]" with a real review, not automatic harvest

## Evidence Strength
Contested — the share-growth logic behind the matrix has been repeatedly challenged (high share does not guarantee returns, low-growth niches can be highly profitable); it survives as a portfolio conversation starter rather than an allocation algorithm.

## Source
Boston Consulting Group (1970); Bruce Henderson.
