"""Quantitative investment methodologies — Factor / Momentum / Risk Parity / Backtesting Performance"""

import json
import math
import sys

from utils import (read_csv, write_output, md_table, fmt_num, pct,
                    mat_mult, quad_form, spearman_ic)

# ───────────────────────── Factor Analysis ─────────────────────────

FACTOR_HELP = """
Factor Analysis: IC/IC_IR calculation + Group return + Monotonicity test

CSV Format (long table, one asset per cross-section):
  date,asset,factor_value,forward_return

  date           : Cross-section date
  asset          : Asset identifier
  factor_value   : Factor value
  forward_return : Forward return rate (decimal)

Example:
  date,asset,factor_value,forward_return
  2024-01,A001,0.5,0.03
  2024-01,A002,-0.2,-0.01
  2024-01,A003,0.8,0.05
  2024-02,A001,0.6,0.02
"""


def cmd_factor(args):
    rows = read_csv(args.input)
    required = {"date", "asset", "factor_value", "forward_return"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV missing columns: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    dates = {}
    for r in rows:
        d = r["date"]
        if d not in dates:
            dates[d] = []
        dates[d].append({
            "asset": r["asset"],
            "fv": float(r["factor_value"]),
            "ret": float(r["forward_return"]),
        })

    sorted_dates = sorted(dates.keys())
    if len(sorted_dates) < 2:
        print("At least 2 cross-section dates required", file=sys.stderr)
        sys.exit(1)

    ic_series = []
    group_returns = {g: [] for g in range(1, 6)}
    ls_returns = []

    for d in sorted_dates:
        assets = dates[d]
        if len(assets) < 5:
            continue
        fvs = [a["fv"] for a in assets]
        rets = [a["ret"] for a in assets]

        ic = spearman_ic(fvs, rets)
        ic_series.append({"date": d, "ic": ic})

        sorted_assets = sorted(assets, key=lambda a: a["fv"])
        n = len(sorted_assets)
        group_means = []
        for g in range(5):
            start = g * n // 5
            end = (g + 1) * n // 5
            group = sorted_assets[start:end]
            avg_ret = sum(a["ret"] for a in group) / len(group)
            group_means.append(avg_ret)
            group_returns[g + 1].append(avg_ret)

        ls_returns.append(group_means[4] - group_means[0])

    ic_values = [x["ic"] for x in ic_series]
    ic_mean = sum(ic_values) / len(ic_values) if ic_values else 0
    ic_std = math.sqrt(sum((v - ic_mean) ** 2 for v in ic_values) / len(ic_values)) if len(ic_values) > 1 else 1
    ic_ir = ic_mean / ic_std if ic_std > 0 else 0
    ic_positive_rate = sum(1 for v in ic_values if v > 0) / len(ic_values) if ic_values else 0

    group_avg = {}
    for g in range(1, 6):
        vals = group_returns[g]
        group_avg[g] = sum(vals) / len(vals) if vals else 0

    monotonic = all(group_avg[i] <= group_avg[i + 1] for i in range(1, 5))
    ls_avg = sum(ls_returns) / len(ls_returns) if ls_returns else 0

    lines = ["# Factor Analysis Report\n"]
    lines.append(f"Cross-sections: {len(ic_series)} | Assets per cross-section: ~{len(rows) // max(len(sorted_dates), 1)}\n")

    lines.append("## IC Statistics\n")
    lines.append(f"- IC Mean: **{ic_mean:.4f}**")
    lines.append(f"- IC Std Dev: {ic_std:.4f}")
    lines.append(f"- IC_IR: **{ic_ir:.4f}**")
    lines.append(f"- IC > 0 ratio: {pct(ic_positive_rate * 100)}")
    lines.append(f"- Factor Effectiveness: {'✅ Effective (|IC| > 0.03)' if abs(ic_mean) > 0.03 else '⚠️ Weak (|IC| ≤ 0.03)'}")
    lines.append(f"- IC_IR Quality: {'✅ Excellent (>0.5)' if ic_ir > 0.5 else ('⚠️ Average' if ic_ir > 0.3 else '❌ Poor (<0.3)')}\n")

    lines.append("## Group Return (avg forward return)\n")
    headers = ["Group", "Avg Return", "Annualized"]
    trows = []
    for g in range(1, 6):
        label = f"G{g}" + (" (Bottom)" if g == 1 else " (Top)" if g == 5 else "")
        trows.append([label, pct(group_avg[g] * 100), pct(group_avg[g] * 252 * 100)])
    trows.append(["Long-Short (Top-Bottom)", pct(ls_avg * 100), pct(ls_avg * 252 * 100)])
    lines.append(md_table(headers, trows))

    lines.append(f"\n## Monotonicity Test: {'✅ Perfect monotonic' if monotonic else '⚠️ Non-perfect monotonic'}\n")

    lines.append("## IC Time Series (last 10 periods)\n")
    ic_headers = ["Date", "IC"]
    ic_trows = [[x["date"], f"{x['ic']:.4f}"] for x in ic_series[-10:]]
    lines.append(md_table(ic_headers, ic_trows))

    if args.json:
        result = {"ic_mean": ic_mean, "ic_std": ic_std, "ic_ir": ic_ir,
                   "ic_positive_rate": ic_positive_rate, "monotonic": monotonic,
                   "group_avg": {str(k): v for k, v in group_avg.items()},
                   "ls_avg": ls_avg, "ic_series": ic_series}
        write_output(json.dumps(result, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── Momentum Analysis ─────────────────────────

MOMENTUM_HELP = """
Momentum signal analysis: Multi-period return calculation + Cross-section ranking + Group return

CSV Format (wide table, one date per row, asset prices as columns):
  date,asset1,asset2,asset3,...

  date  : Date
  assetN: Asset price (closing price)

Example:
  date,A001,A002,A003
  2024-01-01,100,50,200
  2024-01-02,102,49,203
  2024-01-03,105,48,205
"""


def cmd_momentum(args):
    rows = read_csv(args.input)
    if len(rows) < 2:
        print("At least 2 rows of data required", file=sys.stderr)
        sys.exit(1)

    assets = [k for k in rows[0].keys() if k != "date"]
    if len(assets) < 3:
        print("At least 3 assets required", file=sys.stderr)
        sys.exit(1)

    dates = []
    prices = {a: [] for a in assets}
    for r in rows:
        dates.append(r["date"])
        for a in assets:
            prices[a].append(float(r[a]))

    n_dates = len(dates)

    lookbacks = [1, 5, 10, 21, 63]
    returns_by_lb = {}
    for lb in lookbacks:
        if n_dates <= lb:
            continue
        rets = {}
        for a in assets:
            p_now = prices[a][-1]
            p_prev = prices[a][-1 - lb]
            rets[a] = (p_now - p_prev) / p_prev if p_prev != 0 else 0
        returns_by_lb[lb] = rets

    lines = ["# Momentum Signal Analysis Report\n"]
    lines.append(f"Assets: {len(assets)} | Data points: {n_dates} | Date range: {dates[0]} ~ {dates[-1]}\n")

    lines.append("## Multi-Period Returns\n")
    headers = ["Asset"] + [f"{lb} periods" for lb in returns_by_lb.keys()]
    trows = []
    for a in assets:
        row = [a]
        for lb in returns_by_lb:
            row.append(pct(returns_by_lb[lb].get(a, 0) * 100))
        trows.append(row)
    lines.append(md_table(headers, trows))

    if returns_by_lb:
        main_lb = max(returns_by_lb.keys())
        rets = returns_by_lb[main_lb]
        ranked = sorted(assets, key=lambda a: rets.get(a, 0), reverse=True)

        lines.append(f"## Cross-Section Ranking ({main_lb} period momentum)\n")
        r_headers = ["Rank", "Asset", "Return", "Quintile"]
        r_trows = []
        for i, a in enumerate(ranked, 1):
            q = "Top" if i <= len(ranked) * 0.2 else ("Bottom" if i > len(ranked) * 0.8 else "Mid")
            r_trows.append([i, a, pct(rets.get(a, 0) * 100), q])
        lines.append(md_table(r_headers, r_trows))

        n = len(ranked)
        lines.append("## Group Return\n")
        g_headers = ["Group", "Assets", "Avg Return"]
        g_trows = []
        for g in range(5):
            start = g * n // 5
            end = (g + 1) * n // 5
            group = ranked[start:end]
            avg = sum(rets.get(a, 0) for a in group) / len(group) if group else 0
            label = f"G{g + 1}" + (" (Top)" if g == 0 else " (Bottom)" if g == 4 else "")
            g_trows.append([label, len(group), pct(avg * 100)])
        top_avg = sum(rets.get(a, 0) for a in ranked[:max(1, n // 5)]) / max(1, n // 5)
        bot_avg = sum(rets.get(a, 0) for a in ranked[-max(1, n // 5):]) / max(1, n // 5)
        g_trows.append(["Long-Short (Top-Bottom)", "-", pct((top_avg - bot_avg) * 100)])
        lines.append(md_table(g_headers, g_trows))

    if n_dates > 21:
        lines.append("## Rolling Momentum Signal\n")
        lb_ts = min(21, n_dates - 1)
        skip = 1
        eff_lb = lb_ts + skip
        portfolio_rets = []
        for t in range(eff_lb, n_dates):
            mom = {}
            for a in assets:
                p1 = prices[a][t - eff_lb]
                p2 = prices[a][t - skip]
                mom[a] = (p2 - p1) / p1 if p1 != 0 else 0
            ranked_a = sorted(assets, key=lambda x: mom.get(x, 0), reverse=True)
            top_n = max(1, len(ranked_a) // 5)
            top_assets = ranked_a[:top_n]
            port_ret = sum(
                (prices[a][t + 1] - prices[a][t]) / prices[a][t]
                for a in top_assets if prices[a][t] != 0
            ) / len(top_assets) if t + 1 < n_dates else 0
            portfolio_rets.append(port_ret)

        if portfolio_rets:
            avg_ret = sum(portfolio_rets) / len(portfolio_rets)
            vol = math.sqrt(sum((r - avg_ret) ** 2 for r in portfolio_rets) / len(portfolio_rets)) if len(portfolio_rets) > 1 else 0
            sharpe = (avg_ret * 252) / (vol * math.sqrt(252)) if vol > 0 else 0
            win_rate = sum(1 for r in portfolio_rets if r > 0) / len(portfolio_rets)
            lines.append(f"- Lookback period: {lb_ts} periods, skip last {skip} period")
            lines.append(f"- Equal-weight Top 20% Portfolio avg daily return: {pct(avg_ret * 100)}")
            lines.append(f"- Annualized volatility: {pct(vol * math.sqrt(252) * 100)}")
            lines.append(f"- Annualized Sharpe: {sharpe:.2f}")
            lines.append(f"- Daily win rate: {pct(win_rate * 100)}")

    if args.json:
        result = {"assets": assets, "n_dates": n_dates,
                   "returns": {lb: rets for lb, rets in returns_by_lb.items()}}
        write_output(json.dumps(result, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── Risk Parity ─────────────────────────

RISKPARITY_HELP = """
Risk Parity Weighting: Iterative risk contribution equal weighting + Risk decomposition

CSV Format (wide table, one period per row, asset returns as columns):
  period,asset1,asset2,asset3,...

  period : Period identifier
  assetN : Period return (decimal)

Example:
  period,stocks,bonds,commodities,reits
  2020-01,0.02,-0.01,0.03,0.01
  2020-02,-0.03,0.02,-0.01,-0.02
  2020-03,0.01,0.01,0.02,0.03
"""


def cmd_riskparity(args):
    rows = read_csv(args.input)
    assets = [k for k in rows[0].keys() if k != "period"]
    n_assets = len(assets)
    if n_assets < 2:
        print("At least 2 assets required", file=sys.stderr)
        sys.exit(1)

    returns = []
    for r in rows:
        returns.append([float(r[a]) for a in assets])
    n_obs = len(returns)
    if n_obs < n_assets + 1:
        print(f"Insufficient data: {n_obs} periods, recommend at least {n_assets + 1} periods", file=sys.stderr)

    means = [sum(returns[t][i] for t in range(n_obs)) / n_obs for i in range(n_assets)]
    cov = [[0.0] * n_assets for _ in range(n_assets)]
    for i in range(n_assets):
        for j in range(n_assets):
            s = sum((returns[t][i] - means[i]) * (returns[t][j] - means[j]) for t in range(n_obs))
            cov[i][j] = s / (n_obs - 1) * 252

    # Volatility-inverse weighting as initial value
    asset_vols_init = [math.sqrt(max(cov[i][i], 1e-12)) for i in range(n_assets)]
    w = [1.0 / v for v in asset_vols_init]
    total = sum(w)
    w = [x / total for x in w]

    lr = 0.05
    eps = 1e-7
    for iteration in range(5000):
        sw = mat_mult(cov, [[w[i]] for i in range(n_assets)])
        sp2 = max(sum(w[i] * sw[i][0] for i in range(n_assets)), 1e-15)
        sp = math.sqrt(sp2)
        target = sp / n_assets
        rc = [w[i] * sw[i][0] / sp for i in range(n_assets)]

        obj = sum((rc[i] - target) ** 2 for i in range(n_assets))
        if obj < 1e-14:
            break

        grad = [0.0] * n_assets
        for k in range(n_assets):
            wp = w[:]
            wp[k] += eps
            sw_p = mat_mult(cov, [[wp[i]] for i in range(n_assets)])
            sp_p = math.sqrt(max(sum(wp[i] * sw_p[i][0] for i in range(n_assets)), 1e-15))
            target_p = sp_p / n_assets
            rc_p = [wp[i] * sw_p[i][0] / sp_p for i in range(n_assets)]
            obj_p = sum((rc_p[i] - target_p) ** 2 for i in range(n_assets))
            grad[k] = (obj_p - obj) / eps

        w_new = [max(1e-8, w[i] - lr * grad[i]) for i in range(n_assets)]
        total = sum(w_new)
        w_new = [x / total for x in w_new]

        if max(abs(w_new[i] - w[i]) for i in range(n_assets)) < 1e-10:
            w = w_new
            break
        w = w_new

    sigma_w_final = mat_mult(cov, [[w[i]] for i in range(n_assets)])
    sigma_p_final = math.sqrt(sum(w[i] * sigma_w_final[i][0] for i in range(n_assets)))
    rc_final = [w[i] * sigma_w_final[i][0] / sigma_p_final for i in range(n_assets)]
    rc_pct = [rc / sigma_p_final * 100 if sigma_p_final > 0 else 0 for rc in rc_final]
    mrc = [sigma_w_final[i][0] / sigma_p_final if sigma_p_final > 0 else 0 for i in range(n_assets)]

    w_eq = [1.0 / n_assets] * n_assets
    sigma_eq = math.sqrt(quad_form(w_eq, cov))
    asset_vols = [math.sqrt(cov[i][i]) for i in range(n_assets)]

    lines = ["# Risk Parity Configuration Report\n"]
    lines.append(f"Assets: {n_assets} | Data periods: {n_obs}\n")

    lines.append("## Asset Volatility\n")
    v_headers = ["Asset", "Annualized Volatility"]
    v_trows = [[assets[i], pct(asset_vols[i] * 100)] for i in range(n_assets)]
    lines.append(md_table(v_headers, v_trows))

    lines.append("## Risk Parity Weights\n")
    headers = ["Asset", "RP Weight", "Risk Contribution", "Risk Contribution %", "Marginal Risk"]
    trows = []
    for i in range(n_assets):
        trows.append([
            assets[i], pct(w[i] * 100), f"{rc_final[i]:.4f}",
            pct(rc_pct[i]), f"{mrc[i]:.4f}"
        ])
    trows.append(["Total", pct(sum(w) * 100), f"{sigma_p_final:.4f}", pct(sum(rc_pct)), "-"])
    lines.append(md_table(headers, trows))

    div_rp = sigma_eq / sigma_p_final if sigma_p_final > 0 else 1
    lines.append("## Comparison Analysis\n")
    c_headers = ["Approach", "Portfolio Volatility", "Diversification Ratio"]
    c_trows = [
        ["Risk Parity", pct(sigma_p_final * 100), f"{div_rp:.2f}x"],
        ["Equal Weight", pct(sigma_eq * 100), "1.00x"],
    ]
    lines.append(md_table(c_headers, c_trows))

    lines.append("## Risk Balance Check\n")
    max_dev = max(abs(rc_pct[i] - 100 / n_assets) for i in range(n_assets))
    lines.append(f"- Target risk contribution: {pct(100 / n_assets)} (per asset)")
    lines.append(f"- Max deviation: {pct(max_dev)}")
    lines.append(f"- Balance status: {'✅ Converged' if max_dev < 1 else '⚠️ Not fully converged'}")

    if args.json:
        result = {
            "assets": assets, "weights": {assets[i]: w[i] for i in range(n_assets)},
            "risk_contributions": {assets[i]: rc_final[i] for i in range(n_assets)},
            "risk_contrib_pct": {assets[i]: rc_pct[i] for i in range(n_assets)},
            "portfolio_vol": sigma_p_final, "equal_weight_vol": sigma_eq,
            "diversification_ratio": div_rp,
        }
        write_output(json.dumps(result, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── Strategy Performance ─────────────────────────

PERF_HELP = """
Strategy Performance Metrics: Sharpe / Sortino / Calmar / Max Drawdown / VaR / Win Rate

CSV Format:
  date,return

  date   : Date
  return : Period return (decimal)

Optional column:
  benchmark : Benchmark return (decimal, for information ratio/excess return)

Example:
  date,return,benchmark
  2024-01-02,0.005,0.003
  2024-01-03,-0.002,0.001
  2024-01-04,0.008,0.005
"""


def cmd_perf(args):
    rows = read_csv(args.input)
    required = {"date", "return"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV missing columns: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    has_benchmark = "benchmark" in rows[0].keys()
    dates = []
    rets = []
    bench_rets = []
    for r in rows:
        dates.append(r["date"])
        rets.append(float(r["return"]))
        if has_benchmark:
            bench_rets.append(float(r["benchmark"]))

    n = len(rets)
    if n < 5:
        print("At least 5 periods of data required", file=sys.stderr)
        sys.exit(1)

    mean_ret = sum(rets) / n
    var_ret = sum((r - mean_ret) ** 2 for r in rets) / (n - 1) if n > 1 else 0
    std_ret = math.sqrt(var_ret)
    ann_ret = mean_ret * 252
    ann_vol = std_ret * math.sqrt(252)

    cum = 1.0
    cum_rets = []
    for r in rets:
        cum *= (1 + r)
        cum_rets.append(cum)
    total_ret = cum - 1

    peak = cum_rets[0]
    max_dd = 0
    dd_start = 0
    dd_end = 0
    current_dd_start = 0
    for i, c in enumerate(cum_rets):
        if c > peak:
            peak = c
            current_dd_start = i
        dd = (peak - c) / peak
        if dd > max_dd:
            max_dd = dd
            dd_start = current_dd_start
            dd_end = i

    dd_duration = dd_end - dd_start

    downside_rets = [r for r in rets if r < 0]
    down_std = math.sqrt(sum(r ** 2 for r in downside_rets) / len(downside_rets)) if downside_rets else 0
    ann_down_std = down_std * math.sqrt(252)

    sharpe = ann_ret / ann_vol if ann_vol > 0 else 0
    sortino = ann_ret / ann_down_std if ann_down_std > 0 else 0
    calmar = ann_ret / max_dd if max_dd > 0 else 0

    win_rate = sum(1 for r in rets if r > 0) / n

    avg_win = sum(r for r in rets if r > 0) / sum(1 for r in rets if r > 0) if any(r > 0 for r in rets) else 0
    avg_loss = abs(sum(r for r in rets if r < 0) / sum(1 for r in rets if r < 0)) if any(r < 0 for r in rets) else 0
    pl_ratio = avg_win / avg_loss if avg_loss > 0 else 0

    sorted_rets = sorted(rets)
    var_95 = sorted_rets[max(0, int(n * 0.05))]
    var_99 = sorted_rets[max(0, int(n * 0.01))]

    cvar_95_n = max(1, int(n * 0.05))
    cvar_95 = sum(sorted_rets[:cvar_95_n]) / cvar_95_n

    if std_ret > 0:
        skew = sum((r - mean_ret) ** 3 for r in rets) / n / (std_ret ** 3)
        kurt = sum((r - mean_ret) ** 4 for r in rets) / n / (std_ret ** 4) - 3
    else:
        skew = 0
        kurt = 0

    excess_data = {}
    if has_benchmark:
        bench_mean = sum(bench_rets) / n
        bench_cum = 1.0
        bench_cum_rets = []
        for r in bench_rets:
            bench_cum *= (1 + r)
            bench_cum_rets.append(bench_cum)
        bench_total = bench_cum - 1
        bench_ann = bench_mean * 252

        excess_rets = [rets[i] - bench_rets[i] for i in range(n)]
        excess_mean = sum(excess_rets) / n
        excess_ann = excess_mean * 252
        excess_var = sum((r - excess_mean) ** 2 for r in excess_rets) / (n - 1)
        te = math.sqrt(excess_var * 252)
        ir = excess_ann / te if te > 0 else 0

        excess_data = {
            "bench_total": bench_total, "bench_ann": bench_ann,
            "excess_ann": excess_ann, "te": te, "ir": ir,
        }

    lines = ["# Strategy Performance Analysis Report\n"]
    lines.append(f"Data periods: {n} | Date range: {dates[0]} ~ {dates[-1]}\n")

    lines.append("## Return Metrics\n")
    lines.append(f"- Cumulative return: **{pct(total_ret * 100)}**")
    lines.append(f"- Annualized return: **{pct(ann_ret * 100)}**")
    lines.append(f"- Daily avg return: {pct(mean_ret * 100)}")
    if has_benchmark:
        lines.append(f"- Benchmark cumulative return: {pct(excess_data['bench_total'] * 100)}")
        lines.append(f"- Annualized excess return: {pct(excess_data['excess_ann'] * 100)}")
    lines.append("")

    lines.append("## Risk Metrics\n")
    lines.append(f"- Annualized volatility: {pct(ann_vol * 100)}")
    lines.append(f"- Max drawdown: **{pct(max_dd * 100)}**")
    lines.append(f"- Drawdown period: {dates[dd_start]} ~ {dates[dd_end]} ({dd_duration} periods)")
    lines.append(f"- VaR (95%): {pct(var_95 * 100)}")
    lines.append(f"- CVaR (95%): {pct(cvar_95 * 100)}")
    lines.append(f"- VaR (99%): {pct(var_99 * 100)}")
    lines.append("")

    lines.append("## Risk-Adjusted Return\n")
    lines.append(f"- Sharpe ratio: **{sharpe:.2f}**")
    lines.append(f"- Sortino ratio: **{sortino:.2f}**")
    lines.append(f"- Calmar ratio: **{calmar:.2f}**")
    if has_benchmark:
        lines.append(f"- Information ratio: **{excess_data['ir']:.2f}**")
        lines.append(f"- Tracking error: {pct(excess_data['te'] * 100)}")
    lines.append("")

    lines.append("## Trading Statistics\n")
    lines.append(f"- Win rate: {pct(win_rate * 100)}")
    lines.append(f"- Profit/loss ratio: {pl_ratio:.2f}")
    lines.append(f"- Avg win: {pct(avg_win * 100)}")
    lines.append(f"- Avg loss: {pct(avg_loss * 100)}")
    lines.append(f"- Max single-day gain: {pct(max(rets) * 100)}")
    lines.append(f"- Max single-day loss: {pct(min(rets) * 100)}")
    lines.append("")

    lines.append("## Distribution Features\n")
    lines.append(f"- Skewness: {skew:.3f}")
    lines.append(f"- Excess kurtosis: {kurt:.3f}")
    lines.append("- Positive skew indicates longer right tail; high kurtosis indicates extreme events more likely than normal")

    lines.append("\n## Quality Rating\n")
    if sharpe >= 2:
        lines.append("- Sharpe: ✅ Excellent (≥2)")
    elif sharpe >= 1:
        lines.append("- Sharpe: ⚠️ Acceptable (1-2)")
    else:
        lines.append("- Sharpe: ❌ Poor (<1)")
    if max_dd < 0.10:
        lines.append("- Max drawdown: ✅ Controllable (<10%)")
    elif max_dd < 0.20:
        lines.append("- Max drawdown: ⚠️ Moderate (10-20%)")
    else:
        lines.append("- Max drawdown: ❌ Severe (>20%)")
    if win_rate >= 0.55:
        lines.append("- Win rate: ✅ Good (≥55%)")
    else:
        lines.append("- Win rate: ⚠️ Low (<55%)")

    if args.json:
        result = {
            "n_periods": n, "total_return": total_ret, "ann_return": ann_ret,
            "ann_vol": ann_vol, "max_drawdown": max_dd, "dd_start": dates[dd_start],
            "dd_end": dates[dd_end], "sharpe": sharpe, "sortino": sortino,
            "calmar": calmar, "win_rate": win_rate, "pl_ratio": pl_ratio,
            "var_95": var_95, "cvar_95": cvar_95, "skewness": skew, "kurtosis": kurt,
        }
        if has_benchmark:
            result.update(excess_data)
        write_output(json.dumps(result, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)
