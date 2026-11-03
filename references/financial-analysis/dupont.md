# DuPont Analysis

## Core Concept
Decompose ROE into 3 factors: Net Profit Margin × Asset Turnover × Equity Multiplier. Identifies which driver is responsible for ROE changes and enables peer comparison.

## Applicable Scenarios
✅ **Best for**
- Financial diagnostics
- Peer comparison
- ROE anomaly analysis

⚠️ **When NOT to use**
- Questionable accounting quality — the decomposition is exact arithmetic on reported numbers, so earnings management and one-offs pass straight through; normalize or validate earnings first (audit the data with **Cognitive & Statistical Bias Checklist**)
- Banks and financial institutions — leverage is the business model, so a high equity multiplier is normal, not a red flag; the standard reading misleads
- Negative or near-zero equity — the multiplier explodes or flips sign and ROE itself stops meaning anything at the extremes
- Single-period snapshots — one year's decomposition is noise-prone; compare trends and peers, never an isolated reading

## Key Steps
1. Gather financial data: Revenue, Net Income, Total Assets, Equity
2. Calculate 3 factors: Net Profit Margin = NI/Revenue; Asset Turnover = Revenue/TA; Equity Multiplier = TA/Equity
3. Verify: ROE = NPM × AT × EM
4. Compare with peers or prior periods
5. Identify which factor drives ROE differences
6. Use chain substitution method for period-over-period decomposition

## Output Template

```
Company: [x] — period: [FY] — basis: [reported / normalized]
Net Profit Margin: [x%] (NI [x] / Revenue [x])
Asset Turnover: [x] (Revenue [x] / Total Assets [x])
Equity Multiplier: [x] (Total Assets [x] / Equity [x])
Identity check: NPM × AT × EM = [x%] — equals reported ROE? [yes/no]
Comparison: vs peer [x] or prior period [x] — NPM [x vs x], AT [x vs x], EM [x vs x]
Driver verdict: ROE differs mainly via [margin / turnover / leverage] — evidence: [numbers]
Chain substitution: ROE change [x pp] = margin [x pp] + turnover [x pp] + leverage [x pp]
```

## Failure Modes
- Trusting reported numbers: one-off gains, capitalized costs, and managed accruals distort NI and assets → normalize before decomposing and note what was adjusted
- Leverage read as quality: ROE lifted by the equity multiplier is added risk, not efficiency → report EM separately and flag when ROE growth comes from it
- Canceling drivers: two factors moving in opposite directions hide inside the ROE total → use chain substitution to attribute the change factor by factor
- Cross-industry comparison: turnover norms differ radically (retail vs software) → compare within industry or explicitly adjust expectations
- Point-in-time balance sheets: year-end asset snapshots misrepresent the year → use averages where feasible

## Evidence Strength
Practitioner consensus — the decomposition is an exact arithmetic identity, taught and used universally for a century; it reliably locates which driver differs across firms or periods, but it is a diagnostic on reported numbers, so its accuracy is capped by accounting quality and it explains drivers, not future returns.

## Source
Donaldson Brown, DuPont Corporation (1920s).
