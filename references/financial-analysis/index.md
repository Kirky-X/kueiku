# Financial Analysis

**When to use**: Need quantitative judgment on corporate financial performance, valuation, value creation

| Methodology | One-line description | Best scenario | Reference |
| --- | --- | --- | --- |
| **DuPont Analysis** | ROE = Net Margin × Asset Turnover × Equity Multiplier 3-factor decomposition | Financial diagnostics, peer comparison, ROE anomaly analysis | `dupont.md` |
| **DCF** | Enterprise value = sum of future free cash flow present values | Enterprise valuation, investment decisions, M&A pricing | `dcf.md` |
| **Comparable Company** | Infer target company value from similar companies' valuation multiples | IPO pricing, M&A, industry comparison | `comparable-company.md` |
| **EVA** | EVA = NOPAT - capital cost × invested capital, measuring true value creation | Performance evaluation, investment decisions, value management | `eva.md` |
| **Unit Economics** | Per-customer profit: CAC, contribution margin, margin-based LTV, payback period + LTV:CAC / payback health heuristics | Growth-spend decisions, startup viability, channel/segment comparison | `unit-economics.md` |

## Minimum Information Requirements per Methodology

- **DuPont Analysis**: Target company 3-factor data + peer comparison data
- **DCF**: Future cash flow projections + WACC estimate + terminal value assumptions
- **Comparable Company**: Comparable company list + valuation multiple data
- **EVA**: NOPAT + capital cost + invested capital data
- **Unit Economics**: Acquisition spend + new customers acquired + per-customer revenue & variable costs + churn rate or lifespan

## Routing Trigger Signals

- "ROE anomaly cause / financial diagnostics / profitability decomposition" → DuPont Analysis (primary)
- "Enterprise valuation / investment decision / M&A pricing" → DCF (primary)
- "IPO pricing / industry valuation comparison / comparable companies" → Comparable Company (primary)
- "True value creation / performance evaluation / capital efficiency" → EVA (primary)
- "Scale acquisition spend / unit economics health / LTV:CAC / CAC payback" → Unit Economics (primary)

## Common Combinations

- **Enterprise valuation**: DCF (intrinsic value) + Comparable Company (market reference) cross-validation
- **Financial diagnostics**: DuPont Analysis (ROE decomposition) → EVA (value creation verification)
- **Investment decision**: DuPont Analysis (quality assessment) → DCF (valuation) → EVA (holding period value creation)
- **Startup financial health**: Unit Economics (per-customer viability, payback vs runway) → DuPont Analysis (firm-level ROE decomposition)

## Relationship with Quantitative Investment

- **DCF → Factor Investing**: DCF valuation results can build value factors (EP, BP) as factor investing input
- **DCF → Portfolio Optimization**: DCF intrinsic value estimates can serve as expected return input for MVO/Black-Litterman
- **DuPont → ML Stock Selection**: Financial ratios from DuPont analysis can serve as features for ML stock selection
- **EVA → Factor Investing**: Value creation measured by EVA can build quality factors
