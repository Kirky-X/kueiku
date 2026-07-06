# DCF · Discounted Cash Flow

## Core Concept

Enterprise value = Sum of present values of future free cash flows.

DCF (Discounted Cash Flow) is based on the fundamental principle that "the value of an asset equals the present value of the cash flows it can generate in the future." It is an intrinsic value approach that does not rely on market transaction prices, making it the most theoretically grounded valuation method. However, DCF accuracy is highly dependent on assumptions — garbage in, garbage out.

> **Core Concept**: DCF is an "assumption-driven" valuation method.
> Valuation accuracy lies not in the formula, but in the reasonableness of cash flow projections and the accuracy of the discount rate. Sensitivity analysis is mandatory, not optional.

---

## Applicable Scenarios

✅ **Best suited for**
- Enterprise valuation (mature companies with stable cash flows)
- Investment decisions (calculating intrinsic value vs. market price)
- M&A pricing (determining bid range)
- Capital budgeting (project investment decisions)

⚠️ **Use with caution**
- Early-stage startups (unpredictable cash flows)
- Cyclical industries (require cross-cycle averaging)
- High-growth unprofitable companies (require model adjustments)
- Short-term speculative decisions (DCF measures long-term intrinsic value)

---

## Execution Steps

### Step 1: Project Free Cash Flows

Project free cash flows (FCF) for the explicit forecast period (typically 5-10 years):
- FCFF (Free Cash Flow to Firm) = EBIT × (1 - Tax Rate) + Depreciation & Amortization - Capital Expenditures - Changes in Working Capital
- FCFE (Free Cash Flow to Equity) = FCFF - After-tax Interest + Net New Borrowing

Projection basis:
- Historical financial data trends
- Industry growth forecasts
- Company competitiveness and strategic plans
- Macroeconomic assumptions

> Projections must be based on explainable assumptions, not simply extrapolating historical growth rates.

### Step 2: Estimate WACC

Calculate the Weighted Average Cost of Capital (WACC) as the discount rate:
- WACC = E/(D+E) × Re + D/(D+E) × Rd × (1 - Tax Rate)
- Re (Cost of Equity) = Rf + β × (Rm - Rf) (CAPM)
- Rd (Cost of Debt) = Pre-tax debt interest rate
- Rf: Risk-free rate (long-term government bonds)
- Rm - Rf: Equity risk premium
- β: Industry beta

### Step 3: Calculate Terminal Value

Value beyond the explicit forecast period is represented by Terminal Value:
- Perpetuity Growth Method: TV = FCF(n+1) / (WACC - g), where g is the perpetuity growth rate (typically 2-3%, not exceeding long-term GDP)
- Exit Multiple Method: TV = EBITDA(n) × Industry EV/EBITDA Multiple

> Cross-validate both methods. Terminal value typically accounts for 60-80% of valuation and is highly assumption-sensitive.

### Step 4: Discount and Sum

Calculate enterprise value:
- Enterprise Value (EV) = Σ FCFt / (1+WACC)^t + TV / (1+WACC)^n
- Equity Value = EV - Net Debt
- Value Per Share = Equity Value / Shares Outstanding

### Step 5: Sensitivity Analysis

Perform sensitivity analysis on key assumptions:
- Impact of WACC ± 1% / 2%
- Impact of perpetuity growth rate g ± 0.5%
- Impact of explicit period growth rate ± 10%
- Output valuation range (conservative / base / optimistic), not a single number

> A DCF without sensitivity analysis is irresponsible — a single number creates a false sense of precision.

---

## Output Template

```
Analysis Subject: [Company Name]
Valuation Date: [Date]

Free Cash Flow Projection (FCFF):
  | Year | Revenue | EBIT | After-tax EBIT | +D&A | -CapEx | -ΔWC | FCFF |
  |------|------|------|---------|------|--------|------|------|
  | Y1   | ...  | ...  | ...     | ...  | ...    | ...  | ...  |
  | ...  | ...  | ...  | ...     | ...  | ...    | ...  | ...  |
  | Y10  | ...  | ...  | ...     | ...  | ...    | ...  | ...  |

WACC Calculation:
  - Risk-free Rate Rf: [X%]
  - Equity Risk Premium Rm-Rf: [Y%]
  - Beta: [Z]
  - Cost of Equity Re: [X%]
  - Cost of Debt Rd (after-tax): [X%]
  - Capital Structure D/(D+E): [X%]
  - WACC: [X%]

Terminal Value Calculation:
  - Method: [Perpetuity Growth / Exit Multiple]
  - Perpetuity Growth Rate g: [X%]
  - Terminal Value TV: [X]
  - Present Value of Terminal Value: [X]

Valuation Results:
  - Enterprise Value EV: [X]
  - Net Debt: [X]
  - Equity Value: [X]
  - Value Per Share: [X]
  - Current Share Price: [X]
  - Premium/Discount: [X%]

Sensitivity Analysis:
  | WACC \ g | 1.5% | 2.0% | 2.5% | 3.0% |
  |----------|------|------|------|------|
  | 8%       | ...  | ...  | ...  | ...  |
  | 9%       | ...  | ...  | ...  | ...  |
  | 10%      | ...  | ...  | ...  | ...  |

Valuation Conclusion: [Undervalued/Fairly Valued/Overvalued], Range [Conservative ~ Optimistic]
```

---

## Common Pitfalls

| Pitfall | Avoidance Method |
|------|---------|
| Providing single-number false precision | Must perform sensitivity analysis, output range |
| Perpetuity growth rate exceeding long-term GDP | g typically ≤ 3%; exceeding requires strong justification |
| Terminal value proportion too high without scrutiny | TV > 80% of total indicates insufficient explicit period projection |
| Arbitrary WACC estimation | All parameters need documented data sources, no guessing |
| Using DCF for early-stage startups | Use comparable company or real options methods for early-stage |
| Forecast period too short | Explicit period at least 5 years, covering one business cycle |

---

## Relationship with Other Methodologies

- **Complementary Comparable Company**: DCF is intrinsic value approach; CCA is market approach — cross-validate
- **Upstream DuPont Analysis**: DuPont diagnoses historical quality, supporting FCF projection reasonableness
- **Downstream EVA**: DCF estimates value; EVA validates value creation during holding period
