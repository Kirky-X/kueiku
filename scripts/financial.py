"""财务分析方法论 — DuPont / DCF / EVA"""

import json
import sys

from utils import read_csv, write_output, md_table, fmt_num, pct

# ───────────────────────── DuPont Analysis ─────────────────────────

DUPONT_HELP = """
杜邦分析: ROE = 净利率 × 资产周转率 × 权益乘数

CSV 格式:
  period,revenue,net_income,total_assets,equity

  period       : 期间标识（如 2023, 2024, Q1-2024）
  revenue      : 营业收入
  net_income   : 净利润
  total_assets : 总资产
  equity       : 股东权益

示例:
  period,revenue,net_income,total_assets,equity
  2023,1000000,150000,2000000,800000
  2024,1200000,180000,2200000,900000
"""


def cmd_dupont(args):
    rows = read_csv(args.input)
    required = {"period", "revenue", "net_income", "total_assets", "equity"}
    if not required.issubset(rows[0].keys()):
        missing = required - set(rows[0].keys())
        print(f"CSV 缺少列: {missing}", file=sys.stderr)
        sys.exit(1)

    periods = []
    for r in rows:
        rev = float(r["revenue"])
        ni = float(r["net_income"])
        ta = float(r["total_assets"])
        eq = float(r["equity"])
        if rev == 0 or ta == 0 or eq == 0:
            print(f"警告: '{r['period']}' 存在零值，跳过", file=sys.stderr)
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

    lines = ["# 杜邦分析报告\n"]
    lines.append("## 三因素数据\n")
    headers = ["期间", "净利率", "资产周转率", "权益乘数", "ROE"]
    table_rows = []
    for p in periods:
        table_rows.append([
            p["period"], pct(p["net_margin"] * 100),
            fmt_num(p["asset_turnover"]), fmt_num(p["equity_multiplier"]),
            pct(p["roe"] * 100)
        ])
    lines.append(md_table(headers, table_rows))

    lines.append("## 原始财务数据\n")
    headers2 = ["期间", "营业收入", "净利润", "总资产", "股东权益"]
    table_rows2 = []
    for p in periods:
        table_rows2.append([
            p["period"], fmt_num(p["revenue"], 0), fmt_num(p["net_income"], 0),
            fmt_num(p["total_assets"], 0), fmt_num(p["equity"], 0)
        ])
    lines.append(md_table(headers2, table_rows2))

    if changes:
        lines.append("## 因素变动贡献（连环替代法）\n")
        for c in changes:
            lines.append(f"### {c['from']} → {c['to']}\n")
            lines.append(f"- 净利率变动贡献: {c['delta_margin']:+.4f} ({pct(c['delta_margin'] / c['delta_roe'] * 100) if c['delta_roe'] != 0 else 'N/A'})")
            lines.append(f"- 周转率变动贡献: {c['delta_turnover']:+.4f} ({pct(c['delta_turnover'] / c['delta_roe'] * 100) if c['delta_roe'] != 0 else 'N/A'})")
            lines.append(f"- 权益乘数变动贡献: {c['delta_leverage']:+.4f} ({pct(c['delta_leverage'] / c['delta_roe'] * 100) if c['delta_roe'] != 0 else 'N/A'})")
            lines.append(f"- **ROE 总变动**: {c['delta_roe']:+.4f}\n")

    if periods:
        latest = periods[-1]
        lines.append("## 诊断建议\n")
        if latest["net_margin"] < 0.05:
            lines.append("- ⚠️ 净利率偏低 (<5%)：考虑提价 / 降本 / 产品结构升级")
        if latest["asset_turnover"] < 0.5:
            lines.append("- ⚠️ 资产周转率偏低 (<0.5)：考虑库存管理 / 应收账款优化 / 资产处置")
        if latest["equity_multiplier"] > 3:
            lines.append("- ⚠️ 权益乘数偏高 (>3)：杠杆风险较大，考虑降杠杆")

    if args.json:
        result = {"periods": periods, "changes": changes}
        write_output(json.dumps(result, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── DCF ─────────────────────────

DCF_HELP = """
DCF 现金流折现: 企业价值 = Σ FCF/(1+r)^t + 终值/(1+r)^n

CSV 格式:
  year,fcf

  year : 年份标识 (1, 2, 3, ...)
  fcf  : 自由现金流

额外参数通过命令行传入:
  --rate       折现率 (WACC), 如 0.10 表示 10%
  --growth     永续增长率, 如 0.03 表示 3%
  --shares     流通股数（可选，用于计算每股价值）

示例:
  python kueiku-calc.py dcf -i cashflows.csv --rate 0.10 --growth 0.03 --shares 1000000
"""


def cmd_dcf(args):
    rows = read_csv(args.input)
    required = {"year", "fcf"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV 缺少列: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    rate = float(args.rate) if hasattr(args, 'rate') and args.rate else 0.10
    growth = float(args.growth) if hasattr(args, 'growth') and args.growth else 0.03
    shares = float(args.shares) if hasattr(args, 'shares') and args.shares else 0

    cashflows = []
    for r in rows:
        cashflows.append({"year": int(r["year"]), "fcf": float(r["fcf"])})
    cashflows.sort(key=lambda x: x["year"])

    if not cashflows:
        print("无现金流数据", file=sys.stderr)
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

    lines = ["# DCF 现金流折现估值报告\n"]
    lines.append(f"折现率: {pct(rate * 100)} | 永续增长率: {pct(growth * 100)} | 预测期: {n} 年\n")

    lines.append("## 现金流折现\n")
    headers = ["年份", "自由现金流", "折现因子", "现值"]
    trows = [[it["year"], fmt_num(it["fcf"], 0), f"{it['discount_factor']:.4f}", fmt_num(it["pv"], 0)] for it in pv_items]
    lines.append(md_table(headers, trows))

    lines.append("## 估值汇总\n")
    lines.append(f"- 预测期现值合计: **{fmt_num(total_pv, 0)}**")
    lines.append(f"- 终值 (Gordon): **{fmt_num(terminal_value, 0)}**")
    lines.append(f"- 终值现值: **{fmt_num(terminal_pv, 0)}**")
    lines.append(f"- **企业价值**: **{fmt_num(enterprise_value, 0)}**")
    if shares > 0:
        lines.append(f"- 流通股数: {fmt_num(shares, 0)}")
        lines.append(f"- **每股价值**: **{fmt_num(per_share)}**")

    lines.append(f"\n## 敏感性分析（折现率变动）\n")
    s_headers = ["折现率", "企业价值"] + (["每股价值"] if shares > 0 else [])
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
EVA 经济增加值: EVA = NOPAT - WACC × 投入资本

CSV 格式:
  period,ebit,tax_rate,invested_capital,wacc

  period          : 期间标识
  ebit            : 息税前利润
  tax_rate        : 税率 (小数, 如 0.25)
  invested_capital: 投入资本
  wacc            : 加权平均资本成本 (小数, 如 0.10)

示例:
  period,ebit,tax_rate,invested_capital,wacc
  2023,500000,0.25,3000000,0.10
  2024,600000,0.25,3200000,0.09
"""


def cmd_eva(args):
    rows = read_csv(args.input)
    required = {"period", "ebit", "tax_rate", "invested_capital", "wacc"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV 缺少列: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    items = []
    for r in rows:
        ebit = float(r["ebit"])
        tax = float(r["tax_rate"])
        ic = float(r["invested_capital"])
        wacc = float(r["wacc"])
        nopat = ebit * (1 - tax)
        capital_charge = wacc * ic
        eva = nopat - capital_charge
        roic = nopat / ic if ic > 0 else 0
        spread = roic - wacc
        items.append({"period": r["period"], "ebit": ebit, "tax_rate": tax,
                       "invested_capital": ic, "wacc": wacc, "nopat": nopat,
                       "capital_charge": capital_charge, "eva": eva, "roic": roic, "spread": spread})

    lines = ["# EVA 经济增加值分析报告\n"]
    lines.append(f"分析期间数: {len(items)}\n")

    lines.append("## 核心指标\n")
    headers = ["期间", "NOPAT", "资本成本", "EVA", "ROIC", "Spread"]
    trows = [[it["period"], fmt_num(it["nopat"], 0), fmt_num(it["capital_charge"], 0),
              fmt_num(it["eva"], 0), pct(it["roic"] * 100), pct(it["spread"] * 100)] for it in items]
    lines.append(md_table(headers, trows))

    lines.append("## 原始数据\n")
    h2 = ["期间", "EBIT", "税率", "投入资本", "WACC"]
    t2 = [[it["period"], fmt_num(it["ebit"], 0), pct(it["tax_rate"] * 100),
           fmt_num(it["invested_capital"], 0), pct(it["wacc"] * 100)] for it in items]
    lines.append(md_table(h2, t2))

    lines.append("## 诊断\n")
    for it in items:
        if it["eva"] > 0:
            lines.append(f"- **{it['period']}**: EVA > 0，创造价值 (Spread = {pct(it['spread'] * 100)})")
        else:
            lines.append(f"- **{it['period']}**: EVA < 0，毁灭价值！ROIC ({pct(it['roic'] * 100)}) < WACC ({pct(it['wacc'] * 100)})")

    if args.json:
        write_output(json.dumps(items, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)
