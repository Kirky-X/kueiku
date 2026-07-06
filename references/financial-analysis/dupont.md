# DuPont Analysis

## Core Concept

ROE = Net Profit Margin × Asset Turnover × Equity Multiplier — a three-factor decomposition.

DuPont Analysis decomposes Return on Equity (ROE) into three independent driving factors, revealing the true operating model behind a high ROE: whether it comes from high profit margins, high asset efficiency, or high financial leverage. The same 20% ROE with different three-factor structures represents entirely different business models and risk levels.

> **Core Concept**: ROE is the outcome; the three-factor structure is the cause.
> An undecomposed ROE hides risk — an ROE propped up by high leverage collapses when the cycle turns.

| Factor | Formula | Reflects |
|------|------|------|
| Net Profit Margin | Net Income / Revenue | Profitability |
| Asset Turnover | Revenue / Total Assets | Operational Efficiency |
| Equity Multiplier | Total Assets / Shareholders' Equity | Financial Leverage |

---

## Applicable Scenarios

✅ **Best suited for**
- Diagnosing causes of ROE fluctuations
- Comparing financial models of peer companies
- Identifying directions for operational improvement
- Assessing financial quality of investment targets

⚠️ **Use with caution**
- Financial industry (special balance sheet structure, requires adjustments)
- Cross-industry comparison (large structural differences, proceed with caution)
- Single-year analysis (requires multi-year trend comparison)

---

## Execution Steps

### Step 1: Collect Three-Factor Data

Extract data from financial statements:
- Net Income (Income Statement)
- Revenue (Income Statement)
- Total Assets (Balance Sheet, average of opening + closing)
- Shareholders' Equity (Balance Sheet, average of opening + closing)

Calculate three factors:
- Net Profit Margin = Net Income / Revenue
- Asset Turnover = Revenue / Average Total Assets
- Equity Multiplier = Average Total Assets / Average Shareholders' Equity
- Verification: Net Profit Margin × Asset Turnover × Equity Multiplier ≈ ROE

### Step 2: Calculate Each Factor's Contribution

Use chain substitution or difference analysis to calculate each factor's contribution to ROE change:
- Base Period ROE = Margin₀ × Turnover₀ × Multiplier₀
- Substitute Margin: ΔROE(Margin) = (Margin₁ - Margin₀) × Turnover₀ × Multiplier₀
- Substitute Turnover: ΔROE(Turnover) = Margin₁ × (Turnover₁ - Turnover₀) × Multiplier₀
- Substitute Multiplier: ΔROE(Multiplier) = Margin₁ × Turnover₁ × (Multiplier₁ - Multiplier₀)

### Step 3: Peer Comparison

Compare three factors with peer companies to identify differences:
- Margin higher/lower than peers → Pricing power or cost structure differences
- Turnover higher/lower than peers → Asset operational efficiency differences
- Multiplier higher/lower than peers → Financial leverage strategy differences

> Comparisons should use peers with similar business models; cross-model comparisons will be distorted.

### Step 4: Identify Improvement Directions

Based on contribution analysis and peer comparison, identify improvement directions:
- Low Net Profit Margin → Price increases / Cost reduction / Product mix upgrade
- Low Asset Turnover → Inventory management / Receivables management / Asset disposal
- Excessive Equity Multiplier → De-leverage (reduces risk but may lower ROE)

---

## Output Template

```
Analysis Subject: [Company Name]
Analysis Period: [Year/Quarter]

Three-Factor Data:
  | Metric | Current Period | Prior Period | Peer Average |
  |------|------|------|---------|
  | Net Profit Margin | X% | Y% | Z% |
  | Asset Turnover | X | Y | Z |
  | Equity Multiplier | X | Y | Z |
  | ROE (Verification) | X% | Y% | Z% |

Factor Contributions (Chain Substitution):
  - Margin Change Contribution: +X%
  - Turnover Change Contribution: +Y%
  - Multiplier Change Contribution: +Z%
  - Total: +ΔROE%

Peer Comparison Conclusions:
  - Margin: [Above/Below/In line with] peers, Reason: [...]
  - Turnover: [Above/Below/In line with] peers, Reason: [...]
  - Leverage: [Above/Below/In line with] peers, Reason: [...]

Improvement Directions:
  1. [Primary Direction] — Expected Impact: [...]
  2. [Secondary Direction] — Expected Impact: [...]
```

---

## Common Pitfalls

| Pitfall | Avoidance Method |
|------|---------|
| Looking only at ROE without examining structure | Must decompose three factors; structure matters more than outcome |
| Direct cross-industry comparison | Select peers with similar business models |
| Ignoring leverage risk | High multiplier ROE must flag risk |
| Single-point analysis without trends | At least 3 years of trend comparison |
| Using closing balances instead of averages | Use opening + closing averages for assets/equity |

---

## Relationship with Other Methodologies

- **Downstream EVA**: DuPont examines ROE structure; EVA validates whether value is truly being created (above capital cost)
- **Complementary DCF**: DuPont diagnoses historical quality; DCF projects future value
- **Cross-reference Comparable Company**: Peer comparison supplements financial dimensions
