# EVA · Economic Value Added

## Core Concept

EVA = NOPAT - Capital Cost × Invested Capital, measuring true value creation.

Traditional accounting profit (e.g., net income) only deducts the cost of debt capital (interest), but not the cost of equity capital — meaning a company with "accounting profits" may actually be destroying shareholder value. EVA deducts all capital costs (debt + equity), and only when returns exceed the opportunity cost of all capital is true value being created.

> **Core Concept**: Accounting profit ≠ Value creation.
> A company that is profitable on paper but has ROIC < WACC is fundamentally destroying value — the capital it ties up could earn higher returns elsewhere.

| Metric | Formula | Meaning |
|------|------|------|
| NOPAT | EBIT × (1 - Tax Rate) | Net Operating Profit After Tax |
| Invested Capital | Equity + Interest-Bearing Debt - Cash | Capital actually deployed in operations |
| Capital Cost | WACC | Weighted opportunity cost of all capital |
| EVA | NOPAT - WACC × Invested Capital | Economic Value Added |

---

## Applicable Scenarios

✅ **Best suited for**
- Performance evaluation (measuring true contribution of business units)
- Investment decisions (whether a project creates value)
- Value management (guiding management to focus on capital efficiency)
- Incentive compensation (tying bonuses to EVA to avoid short-term accounting manipulation)

⚠️ **Use with caution**
- Early-stage high-growth companies (short-term negative EVA but long-term value creation)
- Short-term evaluation of capital-intensive industries (need cross-cycle analysis)
- Overly complex accounting adjustments (losing comparability)

---

## Execution Steps

### Step 1: Calculate NOPAT

NOPAT (Net Operating Profit After Tax) reflects after-tax profitability of core operations:
- Starting point: EBIT (Operating Profit)
- Adjustments: Add back non-recurring gains/losses, subtract non-operating income
- Tax adjustment: EBIT × (1 - Effective Tax Rate)

> Accounting adjustments should be conservative. Over-adjusting loses comparability and credibility. 5-10 core adjustments are sufficient.

### Step 2: Calculate Capital Cost

Calculate WACC (Weighted Average Cost of Capital):
- Cost of Equity Re = Rf + β × (Rm - Rf)
- Cost of Debt Rd (after-tax) = Rd × (1 - Tax Rate)
- WACC = E/(D+E) × Re + D/(D+E) × Rd(after-tax)

> WACC estimation follows the same methodology as DCF. See the DCF methodology.

### Step 3: Calculate Invested Capital

Invested capital reflects capital actually deployed in operations:
- Invested Capital = Equity + Interest-Bearing Debt - Cash & Equivalents
- Or: Invested Capital = Net Working Capital + Net Fixed Assets + Intangible Assets
- Adjustments needed: Remove non-operating assets

> Both calculation methods should yield the same result and can be used for cross-validation.

### Step 4: Calculate EVA

- EVA = NOPAT - WACC × Invested Capital
- Or: EVA = (ROIC - WACC) × Invested Capital

**Judgment**:
- EVA > 0: Value created (returns exceed capital cost)
- EVA = 0: Breakeven (returns equal capital cost)
- EVA < 0: Value destroyed (returns below capital cost)

> ROIC = NOPAT / Invested Capital. The spread between ROIC and WACC is the source of value creation.

---

## Output Template

```
Analysis Subject: [Company/Business Unit]
Analysis Period: [Year/Quarter]

NOPAT Calculation:
  - EBIT: [X]
  - Accounting Adjustments: [± items]
  - Adjusted EBIT: [X]
  - Effective Tax Rate: [X%]
  - NOPAT = Adjusted EBIT × (1 - Tax Rate): [X]

Capital Cost (WACC):
  - Cost of Equity Re: [X%]
  - After-tax Cost of Debt Rd: [X%]
  - Capital Structure D/(D+E): [X%]
  - WACC: [X%]

Invested Capital Calculation:
  - Equity: [X]
  - Interest-Bearing Debt: [X]
  - Cash & Equivalents: [X]
  - Invested Capital = Equity + Debt - Cash: [X]

EVA Calculation:
  - NOPAT: [X]
  - Capital Cost = WACC × Invested Capital: [X]
  - EVA = NOPAT - Capital Cost: [X]
  - ROIC = NOPAT / Invested Capital: [X%]
  - ROIC - WACC: [X%]

Value Creation Assessment:
  - EVA [>0 / =0 / <0], [Creating / Breakeven / Destroying] value
  - Trend Comparison: [Prior Year EVA, Current Year EVA, Change]

Improvement Directions:
  - Increase NOPAT: [Specific measures]
  - Reduce Capital Employed: [Specific measures]
  - Optimize Capital Structure: [Specific measures]
```

---

## Common Pitfalls

| Pitfall | Avoidance Method |
|------|---------|
| Looking only at accounting profit, ignoring capital cost | Must calculate EVA; accounting profit ≠ value creation |
| Overly complex accounting adjustments | Keep to 5-10 core adjustments for comparability |
| Arbitrary WACC estimation | Use the same WACC methodology as DCF |
| Invested capital includes non-operating assets | Exclude non-operating assets |
| Drawing conclusions from single-period EVA | Use at least 3 years of trends to identify improvement/deterioration |
| Dismissing high-growth companies for negative short-term EVA | Distinguish between "investment-phase negative EVA" and "value destruction" |

---

## Relationship with Other Methodologies

- **Upstream DuPont Analysis**: DuPont examines ROE structure; EVA validates whether value is truly being created
- **Complementary DCF**: DCF estimates value; EVA measures value creation capability
- **Cross-reference Comparable Company**: CCA reflects market valuation; EVA reflects intrinsic value creation
- **Downstream Performance Management**: EVA ties to incentive compensation, avoiding short-term accounting manipulation
