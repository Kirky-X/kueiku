# Financial Analysis

**Applicable Scenarios**: When quantitative judgment is needed on enterprise financial performance, valuation, or value creation.

| Methodology | One-Line Description | Best Scenario | Reference |
| --- | --- | --- | --- |
| **DuPont Analysis** | ROE = Net Profit Margin × Asset Turnover × Equity Multiplier — three-factor decomposition | Financial diagnostics, peer comparison, ROE fluctuation analysis | `dupont.md` |
| **DCF** | Enterprise Value = Sum of present values of future free cash flows | Enterprise valuation, investment decisions, M&A pricing | `dcf.md` |
| **Comparable Company** | Inferring target company value through valuation multiples of similar companies | IPO pricing, M&A, industry comparison | `comparable-company.md` |
| **EVA** | EVA = NOPAT - Capital Cost × Invested Capital, measuring true value creation | Performance evaluation, investment decisions, value management | `eva.md` |

## Minimum Information Requirements

- **DuPont Analysis**: Target company three-factor data + peer comparison data
- **DCF**: Future cash flow projections + WACC estimation + terminal value assumptions
- **Comparable Company**: Comparable company list + valuation multiples data
- **EVA**: NOPAT + Capital cost + Invested capital data

## Routing Trigger Signals

- "ROE fluctuation causes / Financial diagnostics / Profitability decomposition" → DuPont Analysis (primary)
- "Enterprise valuation / Investment decisions / M&A pricing" → DCF (primary)
- "IPO pricing / Industry valuation comparison / Comparable companies" → Comparable Company (primary)
- "True value creation / Performance evaluation / Capital efficiency" → EVA (primary)

## Common Combinations

- **Enterprise Valuation**: DCF (intrinsic value) + Comparable Company (market reference) — cross-validate
- **Financial Diagnostics**: DuPont Analysis (ROE decomposition) → EVA (value creation validation)
- **Investment Decisions**: DuPont Analysis (quality assessment) → DCF (valuation) → EVA (holding period value creation)
