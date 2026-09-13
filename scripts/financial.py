"""Financial analysis methodologies — DuPont / DCF / EVA"""

import json
import sys

from utils import read_csv, write_output, md_table, fmt_num, pct, fnum

# ───────────────────────── DuPont Analysis ─────────────────────────

DUPONT_HELP = """
DuPont Analysis: ROE = Net Profit Margin × Asset Turnover × Equity Multiplier

CSV Format:
  period,revenue,net_income,total_assets,equity

  period       : Period identifier (e.g. 2023, 2024, Q1-2024)
  revenue      : Revenue
  net_income   : Net Income
  total_assets : Total Assets
  equity       : Shareholders' Equity

Example:
  period,revenue,net_income,total_assets,equity
  2023,1000000,150000,2000000,800000
  2024,1200000,180000,2200000,900000
"""


def cmd_dupont(args):
    rows = read_csv(args.input)
    required = {"period", "revenue", "net_income", "total_assets", "equity"}
    if not required.issubset(rows[0].keys()):
        missing = required - set(rows[0].keys())
        print(f"CSV missing columns: {missing}", file=sys.stderr)
        sys.exit(1)

    periods = []
    for row_no, r in enumerate(rows, 2):
        rev = fnum(r["revenue"], "revenue", row_no)
        ni = fnum(r["net_income"], "net_income", row_no)
        ta = fnum(r["total_assets"], "total_assets", row_no)
        eq = fnum(r["equity"], "equity", row_no)
        if rev == 0 or ta == 0 or eq == 0:
            print(f"Warning: '{r['period']}' has zero value, skipped", file=sys.stderr)
            continue
        net_margin = ni / rev
        asset_turnover = rev / ta
        equity_multiplier = ta / eq
        roe = net_margin * asset_turnover * equity_multiplier
        periods.append({
            "period": r["period"], "revenue": rev, "net_income": ni,
            "total_assets": ta, "equity": eq, "net_margin": net_margin,
            "asset_turnover": asset_turnover, "equity_multiplier": equity_multiplier, "roe": roe,
        })

    changes = []
    for i in range(1, len(periods)):
        prev = periods[i - 1]
        curr = periods[i]
        delta_margin = (curr["net_margin"] - prev["net_margin"]) * prev["asset_turnover"] * prev["equity_multiplier"]
        delta_turnover = curr["net_margin"] * (curr["asset_turnover"] - prev["asset_turnover"]) * prev["equity_multiplier"]
        delta_leverage = curr["net_margin"] * curr["asset_turnover"] * (curr["equity_multiplier"] - prev["equity_multiplier"])
        delta_roe = curr["roe"] - prev["roe"]
        changes.append({
            "from": prev["period"], "to": curr["period"],
            "delta_margin": delta_margin, "delta_turnover": delta_turnover,
            "delta_leverage": delta_leverage, "delta_roe": delta_roe,
        })

    lines = ["# DuPont Analysis Report\n"]
    lines.append("## Three-Factor Data\n")
    headers = ["Period", "Net Profit Margin", "Asset Turnover", "Equity Multiplier", "ROE"]
    table_rows = []
    for p in periods:
        table_rows.append([
            p["period"], pct(p["net_margin"] * 100),
            fmt_num(p["asset_turnover"]), fmt_num(p["equity_multiplier"]),
            pct(p["roe"] * 100)
        ])
    lines.append(md_table(headers, table_rows))

    lines.append("## Raw Financial Data\n")
    headers2 = ["Period", "Revenue", "Net Income", "Total Assets", "Shareholders' Equity"]
    table_rows2 = []
    for p in periods:
        table_rows2.append([
            p["period"], fmt_num(p["revenue"], 0), fmt_num(p["net_income"], 0),
            fmt_num(p["total_assets"], 0), fmt_num(p["equity"], 0)
        ])
    lines.append(md_table(headers2, table_rows2))

    if changes:
        lines.append("## Factor Contribution Analysis (Chain Substitution Method)\n")
        for c in changes:
            lines.append(f"### {c['from']} → {c['to']}\n")
            lines.append(f"- Net profit margin contribution: {c['delta_margin']:+.4f} ({pct(c['delta_margin'] / c['delta_roe'] * 100) if c['delta_roe'] != 0 else 'N/A'})")
            lines.append(f"- Turnover ratio contribution: {c['delta_turnover']:+.4f} ({pct(c['delta_turnover'] / c['delta_roe'] * 100) if c['delta_roe'] != 0 else 'N/A'})")
            lines.append(f"- Equity multiplier contribution: {c['delta_leverage']:+.4f} ({pct(c['delta_leverage'] / c['delta_roe'] * 100) if c['delta_roe'] != 0 else 'N/A'})")
            lines.append(f"- **Total ROE change**: {c['delta_roe']:+.4f}\n")

    if periods:
        latest = periods[-1]
        lines.append("## Diagnostic Recommendations\n")
        if latest["net_margin"] < 0.05:
            lines.append("- ⚠️ Low net profit margin (<5%): consider price increase / cost reduction / product mix upgrade")
        if latest["asset_turnover"] < 0.5:
            lines.append("- ⚠️ Low asset turnover (<0.5): consider inventory management / receivables optimization / asset disposal")
        if latest["equity_multiplier"] > 3:
            lines.append("- ⚠️ High equity multiplier (>3): high leverage risk, consider deleveraging")

    if args.json:
        result = {"periods": periods, "changes": changes}
        write_output(json.dumps(result, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── DCF ─────────────────────────

DCF_HELP = """
DCF Discounted Cash Flow: Enterprise value = Σ FCF/(1+r)^t + Terminal value/(1+r)^n

CSV Format:
  year,fcf

  year : Period index starting at 1 (1, 2, 3, ...). Calendar years
         (e.g. 2024) or non-consecutive sequences are rejected with an error.
  fcf  : Free cash flow

Additional parameters via command line:
  --rate       Discount rate (WACC), e.g. 0.10 for 10%
  --growth     Perpetual growth rate, e.g. 0.03 for 3%
  --shares     Shares outstanding (optional, for per-share valuation)

Example:
  python kueiku-calc.py dcf -i cashflows.csv --rate 0.10 --growth 0.03 --shares 1000000
"""


def cmd_dcf(args):
    rows = read_csv(args.input)
    required = {"year", "fcf"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV missing columns: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    rate = float(args.rate) if hasattr(args, 'rate') and args.rate else 0.10
    growth = float(args.growth) if hasattr(args, 'growth') and args.growth else 0.03
    shares = float(args.shares) if hasattr(args, 'shares') and args.shares else 0

    cashflows = []
    for row_no, r in enumerate(rows, 2):
        cashflows.append({"year": int(fnum(r["year"], "year", row_no)), "fcf": fnum(r["fcf"], "fcf", row_no)})
    cashflows.sort(key=lambda x: x["year"])

    if not cashflows:
        print("No cash flow data", file=sys.stderr)
        sys.exit(1)

    # Validate years: the discount index t must be a period count starting at 1
    # (1, 2, 3, ...). Calendar years (e.g. 2024) or gaps would silently deflate
    # present values to ~0, so fail loudly instead.
    years = [cf["year"] for cf in cashflows]
    if years != list(range(1, len(years) + 1)) or years[-1] > 2100:
        print("Error: 'year' must be consecutive period indices starting at 1 (1, 2, 3, ...), "
              f"not calendar years or an irregular sequence. Got: {years}. "
              "Map calendar years to periods 1..n before running DCF.", file=sys.stderr)
        sys.exit(1)

    pv_items = []
    total_pv = 0
    for cf in cashflows:
        t = cf["year"]
        pv = cf["fcf"] / ((1 + rate) ** t)
        total_pv += pv
        pv_items.append({"year": t, "fcf": cf["fcf"], "pv": pv, "discount_factor": 1 / ((1 + rate) ** t)})

    last_fcf = cashflows[-1]["fcf"]
    n = cashflows[-1]["year"]
    terminal_value = last_fcf * (1 + growth) / (rate - growth)
    terminal_pv = terminal_value / ((1 + rate) ** n)
    enterprise_value = total_pv + terminal_pv
    per_share = enterprise_value / shares if shares > 0 else 0

    sensitivity = []
    for dr in [rate - 0.02, rate - 0.01, rate, rate + 0.01, rate + 0.02]:
        if dr <= growth:
            continue
        tv = last_fcf * (1 + growth) / (dr - growth)
        tpv = tv / ((1 + dr) ** n)
        spv = sum(cf["fcf"] / ((1 + dr) ** cf["year"]) for cf in cashflows)
        ev = spv + tpv
        sensitivity.append({"discount_rate": dr, "enterprise_value": ev,
                            "per_share": ev / shares if shares > 0 else 0})

    lines = ["# DCF Valuation Report\n"]
    lines.append(f"Discount rate: {pct(rate * 100)} | Perpetual growth rate: {pct(growth * 100)} | Projection period: {n} years\n")

    lines.append("## Cash Flow Discounting\n")
    headers = ["Year", "Free Cash Flow", "Discount Factor", "Present Value"]
    trows = [[it["year"], fmt_num(it["fcf"], 0), f"{it['discount_factor']:.4f}", fmt_num(it["pv"], 0)] for it in pv_items]
    lines.append(md_table(headers, trows))

    lines.append("## Valuation Summary\n")
    lines.append(f"- PV of projection period: **{fmt_num(total_pv, 0)}**")
    lines.append(f"- Terminal value (Gordon): **{fmt_num(terminal_value, 0)}**")
    lines.append(f"- PV of terminal value: **{fmt_num(terminal_pv, 0)}**")
    lines.append(f"- **Enterprise value**: **{fmt_num(enterprise_value, 0)}**")
    if shares > 0:
        lines.append(f"- Shares outstanding: {fmt_num(shares, 0)}")
        lines.append(f"- **Per-share value**: **{fmt_num(per_share)}**")

    lines.append(f"\n## Sensitivity Analysis (Discount rate variation)\n")
    s_headers = ["Discount Rate", "Enterprise Value"] + (["Per-Share Value"] if shares > 0 else [])
    s_rows = [[pct(s["discount_rate"] * 100), fmt_num(s["enterprise_value"], 0)] + ([fmt_num(s["per_share"])] if shares > 0 else []) for s in sensitivity]
    lines.append(md_table(s_headers, s_rows))

    if args.json:
        result = {"rate": rate, "growth": growth, "pv_items": pv_items,
                   "terminal_value": terminal_value, "terminal_pv": terminal_pv,
                   "enterprise_value": enterprise_value, "per_share": per_share, "sensitivity": sensitivity}
        write_output(json.dumps(result, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── EVA ─────────────────────────

EVA_HELP = """
EVA Economic Value Added: EVA = NOPAT - WACC × Invested Capital

CSV Format:
  period,ebit,tax_rate,invested_capital,wacc

  period          : Period identifier
  ebit            : Earnings before interest and tax
  tax_rate        : Tax rate (decimal, e.g. 0.25)
  invested_capital: Invested capital
  wacc            : Weighted average cost of capital (decimal, e.g. 0.10)

Example:
  period,ebit,tax_rate,invested_capital,wacc
  2023,500000,0.25,3000000,0.10
  2024,600000,0.25,3200000,0.09
"""


def cmd_eva(args):
    rows = read_csv(args.input)
    required = {"period", "ebit", "tax_rate", "invested_capital", "wacc"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV missing columns: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    items = []
    for row_no, r in enumerate(rows, 2):
        ebit = fnum(r["ebit"], "ebit", row_no)
        tax = fnum(r["tax_rate"], "tax_rate", row_no)
        ic = fnum(r["invested_capital"], "invested_capital", row_no)
        wacc = fnum(r["wacc"], "wacc", row_no)
        nopat = ebit * (1 - tax)
        capital_charge = wacc * ic
        eva = nopat - capital_charge
        roic = nopat / ic if ic > 0 else 0
        spread = roic - wacc
        items.append({"period": r["period"], "ebit": ebit, "tax_rate": tax,
                       "invested_capital": ic, "wacc": wacc, "nopat": nopat,
                       "capital_charge": capital_charge, "eva": eva, "roic": roic, "spread": spread})

    lines = ["# EVA (Economic Value Added) Analysis Report\n"]
    lines.append(f"Periods analyzed: {len(items)}\n")

    lines.append("## Core Metrics\n")
    headers = ["Period", "NOPAT", "Capital Charge", "EVA", "ROIC", "Spread"]
    trows = [[it["period"], fmt_num(it["nopat"], 0), fmt_num(it["capital_charge"], 0),
              fmt_num(it["eva"], 0), pct(it["roic"] * 100), pct(it["spread"] * 100)] for it in items]
    lines.append(md_table(headers, trows))

    lines.append("## Raw Data\n")
    h2 = ["Period", "EBIT", "Tax Rate", "Invested Capital", "WACC"]
    t2 = [[it["period"], fmt_num(it["ebit"], 0), pct(it["tax_rate"] * 100),
           fmt_num(it["invested_capital"], 0), pct(it["wacc"] * 100)] for it in items]
    lines.append(md_table(h2, t2))

    lines.append("## Diagnostics\n")
    for it in items:
        if it["eva"] > 0:
            lines.append(f"- **{it['period']}**: EVA > 0, creating value (Spread = {pct(it['spread'] * 100)})")
        else:
            lines.append(f"- **{it['period']}**: EVA < 0, destroying value! ROIC ({pct(it['roic'] * 100)}) < WACC ({pct(it['wacc'] * 100)})")

    if args.json:
        write_output(json.dumps(items, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)
