# Financial Analysis

**When to use**: Need quantitative judgment on corporate financial performance, valuation, value creation

| Methodology | One-line description | Best scenario | Reference |
| --- | --- | --- | --- |
| **DuPont Analysis** | ROE = Net Margin × Asset Turnover × Equity Multiplier 3-factor decomposition | Financial diagnostics, peer comparison, ROE anomaly analysis | `dupont.md` |
| **DCF** | Enterprise value = sum of future free cash flow present values | Enterprise valuation, investment decisions, M&A pricing | `dcf.md` |
| **Comparable Company** | Infer target company value from similar companies' valuation multiples | IPO pricing, M&A, industry comparison | `comparable-company.md` |
| **EVA** | EVA = NOPAT - capital cost × invested capital, measuring true value creation | Performance evaluation, investment decisions, value management | `eva.md` |

## Minimum Information Requirements per Methodology

- **DuPont Analysis**: Target company 3-factor data + peer comparison data
- **DCF**: Future cash flow projections + WACC estimate + terminal value assumptions
- **Comparable Company**: Comparable company list + valuation multiple data
- **EVA**: NOPAT + capital cost + invested capital data

## Routing Trigger Signals

- "ROE anomaly cause / financial diagnostics / profitability decomposition" → DuPont Analysis (primary)
- "Enterprise valuation / investment decision / M&A pricing" → DCF (primary)
- "IPO pricing / industry valuation comparison / comparable companies" → Comparable Company (primary)
- "True value creation / performance evaluation / capital efficiency" → EVA (primary)

## Common Combinations

- **Enterprise valuation**: DCF (intrinsic value) + Comparable Company (market reference) cross-validation
- **Financial diagnostics**: DuPont Analysis (ROE decomposition) → EVA (value creation verification)
- **Investment decision**: DuPont Analysis (quality assessment) → DCF (valuation) → EVA (holding period value creation)

## Relationship with Quantitative Investment

- **DCF → Factor Investing**: DCF valuation results can build value factors (EP, BP) as factor investing input
- **DCF → Portfolio Optimization**: DCF intrinsic value estimates can serve as expected return input for MVO/Black-Litterman
- **DuPont → ML Stock Selection**: Financial ratios from DuPont analysis can serve as features for ML stock selection
- **EVA → Factor Investing**: Value creation measured by EVA can build quality factors
