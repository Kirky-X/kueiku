"""量化投资方法论 — Factor / Momentum / Risk Parity / Backtesting Performance"""

import json
import math
import sys

from utils import (read_csv, write_output, md_table, fmt_num, pct,
                    mat_mult, quad_form, spearman_ic)

# ───────────────────────── Factor Analysis ─────────────────────────

FACTOR_HELP = """
因子分析: IC/IC_IR 计算 + 分组收益 + 单调性检验

CSV 格式（长表，每行一个资产-截面）:
  date,asset,factor_value,forward_return

  date           : 截面日期
  asset          : 资产标识
  factor_value   : 因子值
  forward_return : 前瞻收益率（小数）

示例:
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
        print(f"CSV 缺少列: {required - set(rows[0].keys())}", file=sys.stderr)
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
        print("至少需要 2 个截面日期", file=sys.stderr)
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

    lines = ["# 因子分析报告\n"]
    lines.append(f"截面数: {len(ic_series)} | 每截面资产数: ~{len(rows) // max(len(sorted_dates), 1)}\n")

    lines.append("## IC 统计\n")
    lines.append(f"- IC 均值: **{ic_mean:.4f}**")
    lines.append(f"- IC 标准差: {ic_std:.4f}")
    lines.append(f"- IC_IR: **{ic_ir:.4f}**")
    lines.append(f"- IC > 0 占比: {pct(ic_positive_rate * 100)}")
    lines.append(f"- 因子有效性: {'✅ 有效 (|IC| > 0.03)' if abs(ic_mean) > 0.03 else '⚠️ 弱 (|IC| ≤ 0.03)'}")
    lines.append(f"- IC_IR 质量: {'✅ 优秀 (>0.5)' if ic_ir > 0.5 else ('⚠️ 一般' if ic_ir > 0.3 else '❌ 较差 (<0.3)')}\n")

    lines.append("## 分组收益（平均前瞻收益）\n")
    headers = ["分组", "平均收益", "年化"]
    trows = []
    for g in range(1, 6):
        label = f"G{g}" + (" (Bottom)" if g == 1 else " (Top)" if g == 5 else "")
        trows.append([label, pct(group_avg[g] * 100), pct(group_avg[g] * 252 * 100)])
    trows.append(["多空 (Top-Bottom)", pct(ls_avg * 100), pct(ls_avg * 252 * 100)])
    lines.append(md_table(headers, trows))

    lines.append(f"\n## 单调性检验: {'✅ 完美单调' if monotonic else '⚠️ 非完美单调'}\n")

    lines.append("## IC 时序（最近 10 期）\n")
    ic_headers = ["日期", "IC"]
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
动量信号分析: 多期收益计算 + 截面排名 + 分组收益

CSV 格式（宽表，每行一个日期，各列资产价格）:
  date,asset1,asset2,asset3,...

  date  : 日期
  assetN: 资产价格（收盘价）

示例:
  date,A001,A002,A003
  2024-01-01,100,50,200
  2024-01-02,102,49,203
  2024-01-03,105,48,205
"""


def cmd_momentum(args):
    rows = read_csv(args.input)
    if len(rows) < 2:
        print("至少需要 2 行数据", file=sys.stderr)
        sys.exit(1)

    assets = [k for k in rows[0].keys() if k != "date"]
    if len(assets) < 3:
        print("至少需要 3 个资产", file=sys.stderr)
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

    lines = ["# 动量信号分析报告\n"]
    lines.append(f"资产数: {len(assets)} | 数据点数: {n_dates} | 日期范围: {dates[0]} ~ {dates[-1]}\n")

    lines.append("## 多期收益率\n")
    headers = ["资产"] + [f"{lb}期" for lb in returns_by_lb.keys()]
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

        lines.append(f"## 截面排名（{main_lb} 期动量）\n")
        r_headers = ["排名", "资产", "收益率", "分位"]
        r_trows = []
        for i, a in enumerate(ranked, 1):
            q = "Top" if i <= len(ranked) * 0.2 else ("Bottom" if i > len(ranked) * 0.8 else "Mid")
            r_trows.append([i, a, pct(rets.get(a, 0) * 100), q])
        lines.append(md_table(r_headers, r_trows))

        n = len(ranked)
        lines.append("## 分组收益\n")
        g_headers = ["分组", "资产数", "平均收益"]
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
        g_trows.append(["多空 (Top-Bottom)", "-", pct((top_avg - bot_avg) * 100)])
        lines.append(md_table(g_headers, g_trows))

    if n_dates > 21:
        lines.append("## 滚动动量信号\n")
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
            lines.append(f"- 回看期: {lb_ts} 期, 跳过近 {skip} 期")
            lines.append(f"- 等权 Top 20% 组合日均收益: {pct(avg_ret * 100)}")
            lines.append(f"- 年化波动率: {pct(vol * math.sqrt(252) * 100)}")
            lines.append(f"- 年化夏普: {sharpe:.2f}")
            lines.append(f"- 日胜率: {pct(win_rate * 100)}")

    if args.json:
        result = {"assets": assets, "n_dates": n_dates,
                   "returns": {lb: rets for lb, rets in returns_by_lb.items()}}
        write_output(json.dumps(result, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── Risk Parity ─────────────────────────

RISKPARITY_HELP = """
风险平价权重: 迭代求解风险贡献均等权重 + 风险分解

CSV 格式（宽表，每行一期，各列为资产收益率）:
  period,asset1,asset2,asset3,...

  period : 期间标识
  assetN : 该期收益率（小数）

示例:
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
        print("至少需要 2 个资产", file=sys.stderr)
        sys.exit(1)

    returns = []
    for r in rows:
        returns.append([float(r[a]) for a in assets])
    n_obs = len(returns)
    if n_obs < n_assets + 1:
        print(f"数据点不足: {n_obs} 期，建议至少 {n_assets + 1} 期", file=sys.stderr)

    means = [sum(returns[t][i] for t in range(n_obs)) / n_obs for i in range(n_assets)]
    cov = [[0.0] * n_assets for _ in range(n_assets)]
    for i in range(n_assets):
        for j in range(n_assets):
            s = sum((returns[t][i] - means[i]) * (returns[t][j] - means[j]) for t in range(n_obs))
            cov[i][j] = s / (n_obs - 1) * 252

    # 波动率倒数加权作为初始值
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

    lines = ["# 风险平价配置报告\n"]
    lines.append(f"资产数: {n_assets} | 数据期数: {n_obs}\n")

    lines.append("## 资产波动率\n")
    v_headers = ["资产", "年化波动率"]
    v_trows = [[assets[i], pct(asset_vols[i] * 100)] for i in range(n_assets)]
    lines.append(md_table(v_headers, v_trows))

    lines.append("## 风险平价权重\n")
    headers = ["资产", "RP 权重", "风险贡献", "风险贡献占比", "边际风险"]
    trows = []
    for i in range(n_assets):
        trows.append([
            assets[i], pct(w[i] * 100), f"{rc_final[i]:.4f}",
            pct(rc_pct[i]), f"{mrc[i]:.4f}"
        ])
    trows.append(["合计", pct(sum(w) * 100), f"{sigma_p_final:.4f}", pct(sum(rc_pct)), "-"])
    lines.append(md_table(headers, trows))

    div_rp = sigma_eq / sigma_p_final if sigma_p_final > 0 else 1
    lines.append("## 对比分析\n")
    c_headers = ["方案", "组合波动率", "分散化比率"]
    c_trows = [
        ["风险平价", pct(sigma_p_final * 100), f"{div_rp:.2f}x"],
        ["等权", pct(sigma_eq * 100), "1.00x"],
    ]
    lines.append(md_table(c_headers, c_trows))

    lines.append("## 风险均衡检验\n")
    max_dev = max(abs(rc_pct[i] - 100 / n_assets) for i in range(n_assets))
    lines.append(f"- 目标风险贡献: {pct(100 / n_assets)}（每个资产）")
    lines.append(f"- 最大偏差: {pct(max_dev)}")
    lines.append(f"- 均衡状态: {'✅ 收敛' if max_dev < 1 else '⚠️ 未完全收敛'}")

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
策略绩效指标: Sharpe / Sortino / Calmar / 最大回撤 / VaR / 胜率

CSV 格式:
  date,return

  date   : 日期
  return : 期间收益率（小数）

可选列:
  benchmark : 基准收益率（小数，用于计算信息比率/超额收益）

示例:
  date,return,benchmark
  2024-01-02,0.005,0.003
  2024-01-03,-0.002,0.001
  2024-01-04,0.008,0.005
"""


def cmd_perf(args):
    rows = read_csv(args.input)
    required = {"date", "return"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV 缺少列: {required - set(rows[0].keys())}", file=sys.stderr)
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
        print("至少需要 5 期数据", file=sys.stderr)
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

    lines = ["# 策略绩效分析报告\n"]
    lines.append(f"数据期数: {n} | 日期范围: {dates[0]} ~ {dates[-1]}\n")

    lines.append("## 收益指标\n")
    lines.append(f"- 累计收益: **{pct(total_ret * 100)}**")
    lines.append(f"- 年化收益: **{pct(ann_ret * 100)}**")
    lines.append(f"- 日均收益: {pct(mean_ret * 100)}")
    if has_benchmark:
        lines.append(f"- 基准累计收益: {pct(excess_data['bench_total'] * 100)}")
        lines.append(f"- 年化超额收益: {pct(excess_data['excess_ann'] * 100)}")
    lines.append("")

    lines.append("## 风险指标\n")
    lines.append(f"- 年化波动率: {pct(ann_vol * 100)}")
    lines.append(f"- 最大回撤: **{pct(max_dd * 100)}**")
    lines.append(f"- 回撤区间: {dates[dd_start]} ~ {dates[dd_end]}（{dd_duration} 期）")
    lines.append(f"- VaR (95%): {pct(var_95 * 100)}")
    lines.append(f"- CVaR (95%): {pct(cvar_95 * 100)}")
    lines.append(f"- VaR (99%): {pct(var_99 * 100)}")
    lines.append("")

    lines.append("## 风险调整收益\n")
    lines.append(f"- Sharpe 比率: **{sharpe:.2f}**")
    lines.append(f"- Sortino 比率: **{sortino:.2f}**")
    lines.append(f"- Calmar 比率: **{calmar:.2f}**")
    if has_benchmark:
        lines.append(f"- 信息比率: **{excess_data['ir']:.2f}**")
        lines.append(f"- 跟踪误差: {pct(excess_data['te'] * 100)}")
    lines.append("")

    lines.append("## 交易统计\n")
    lines.append(f"- 胜率: {pct(win_rate * 100)}")
    lines.append(f"- 盈亏比: {pl_ratio:.2f}")
    lines.append(f"- 平均盈利: {pct(avg_win * 100)}")
    lines.append(f"- 平均亏损: {pct(avg_loss * 100)}")
    lines.append(f"- 最大单日盈利: {pct(max(rets) * 100)}")
    lines.append(f"- 最大单日亏损: {pct(min(rets) * 100)}")
    lines.append("")

    lines.append("## 分布特征\n")
    lines.append(f"- 偏度: {skew:.3f}")
    lines.append(f"- 超额峰度: {kurt:.3f}")
    lines.append(f"- 正偏态表示右尾较长；高峰度表示极端事件概率高于正态")

    lines.append("\n## 质量评级\n")
    if sharpe >= 2:
        lines.append("- Sharpe: ✅ 优秀 (≥2)")
    elif sharpe >= 1:
        lines.append("- Sharpe: ⚠️ 合格 (1-2)")
    else:
        lines.append("- Sharpe: ❌ 较差 (<1)")
    if max_dd < 0.10:
        lines.append("- 最大回撤: ✅ 可控 (<10%)")
    elif max_dd < 0.20:
        lines.append("- 最大回撤: ⚠️ 中等 (10-20%)")
    else:
        lines.append("- 最大回撤: ❌ 严重 (>20%)")
    if win_rate >= 0.55:
        lines.append("- 胜率: ✅ 良好 (≥55%)")
    else:
        lines.append("- 胜率: ⚠️ 偏低 (<55%)")

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
