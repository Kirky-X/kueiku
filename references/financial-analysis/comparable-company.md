# Comparable Company Analysis

## Core Concept

Inferring target company value through valuation multiples of similar companies.

Comparable Company Analysis (CCA) is based on the principle that "similar assets should be priced similarly." By screening for comparable companies similar to the target in industry, size, growth, and risk, and using their market transaction multiples, CCA infers the target company's value. It is a market-based approach that reflects current market pricing but depends on market efficiency.

> **Core Concept**: CCA reflects "what the market is willing to pay for similar companies," not "what a company is worth."
> The market approach vs. intrinsic value approach (DCF) requires cross-validation — if there's a large discrepancy, the reason must be explained.

---

## Applicable Scenarios

✅ **Best suited for**
- IPO pricing (referencing listed companies)
- M&A pricing (quick market reference)
- Industry valuation level comparison
- Private equity exit valuation

⚠️ **Use with caution**
- Unique business models (no comparable companies)
- Extreme market conditions (bubble/panic distorting multiples)
- Cross-region/cross-regulatory environment comparisons (require adjustments)
- Small sample sizes (fewer than 3 comparable companies reduces reliability)

---

## Execution Steps

### Step 1: Screen Comparable Companies

Screening criteria (ordered by importance):
- **Industry**: Same industry or similar business model
- **Size**: Similar revenue/asset/market capitalization magnitude
- **Growth**: Similar growth rates
- **Profitability**: Similar profit margins
- **Geography**: Similar primary markets
- **Risk**: Similar leverage, volatility

> Ideal number of comparable companies is 5-10, minimum 3. Screening rationale must be documented; no post-hoc cherry-picking.

### Step 2: Select Valuation Multiples

Choose appropriate multiples based on company characteristics:
- **EV/EBITDA**: Cross-capital-structure comparable, most commonly used
- **P/E**: Stable profitability companies
- **EV/Revenue**: High-growth unprofitable companies
- **P/B**: Financial industry, asset-heavy industries
- **EV/EBIT**: Cross-leverage comparable, removes capital structure effects

> Multiple selection must match company characteristics; do not mechanically apply P/E.

### Step 3: Calculate Median

Compute statistical measures for the comparable company group:
- Median (preferred, robust to outliers)
- Mean (reference)
- 25th / 75th percentile (range)
- Exclude obvious outliers with documented rationale

### Step 4: Adjust for Differences

Adjust for differences between the target company and the comparable group:
- Growth rate differences → Growth premium/discount
- Size differences → Size discount (smaller companies have lower liquidity)
- Profitability differences → Margin adjustments
- Liquidity differences → Liquidity discount (private/unlisted companies)

> Adjustments must be evidence-based; do not manipulate adjustments to reach a desired valuation.

---

## Output Template

```
Analysis Subject: [Target Company]
Valuation Date: [Date]

Comparable Company Screening:
  | Company | Industry | Revenue | Growth | Margin | Size | Screening Result |
  |------|------|------|--------|--------|------|---------|
  | A    | ...  | ...  | ...    | ...    | ...  | Include/Exclude |
  | B    | ...  | ...  | ...    | ...    | ...  | Include/Exclude |
  Exclusion Rationale: [...]

Valuation Multiples:
  | Company | EV/EBITDA | P/E | EV/Revenue | P/B |
  |------|-----------|-----|------------|-----|
  | A    | X         | X   | X          | X   |
  | B    | X         | X   | X          | X   |
  | Median | X       | X   | X          | X   |
  | 25th Percentile | X | X | X        | X   |
  | 75th Percentile | X | X | X        | X   |

Difference Adjustments:
  | Adjustment Item | Target Company | Comparable Median | Direction | Magnitude |
  |--------|---------|--------------|---------|---------|
  | Growth Rate | X%      | Y%           | Premium/Discount | ±Z% |
  | Size   | X       | Y            | Discount     | -Z% |
  | Liquidity | Listed/Unlisted | Listed      | Discount     | -Z% |

Valuation Results:
  - Selected Multiple: [EV/EBITDA etc.]
  - Adjusted Multiple: [X]
  - Target Company Metric: [Y]
  - Valuation Range: [Conservative ~ Optimistic]
  - Comparison with DCF: [Consistent/Divergence X%, Reason: ...]

Valuation Conclusion: [Description]
```

---

## Common Pitfalls

| Pitfall | Avoidance Method |
|------|---------|
| Biased comparable company selection | Pre-establish screening criteria, document exclusion rationale |
| Mechanical P/E application | Multiple selection must match company characteristics |
| Applying multiples without adjusting for differences | Growth/size/liquidity differences must be adjusted |
| Distorted multiples during extreme market periods | Combine with historical median multiples, not just current |
| Treating small sample as reliable valuation | < 3 comparable companies requires reliability disclosure |
| Using market approach without cross-validation | Cross-validate with DCF; large discrepancies require explanation |

---

## Relationship with Other Methodologies

- **Complementary DCF**: CCA is the market approach; DCF is the intrinsic value approach — cross-validate
- **Upstream DuPont Analysis**: DuPont diagnoses financial quality for comparable company screening
- **Cross-reference EVA**: CCA for valuation; EVA validates subsequent value creation capability
