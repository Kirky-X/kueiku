"""数据分析方法论 — A/B Test / RFM / Cohort"""

import json
import math
import sys

from .utils import read_csv, write_output, md_table, fmt_num, pct, z_test, quintile_score

# ───────────────────────── A/B Test Analysis ─────────────────────────

ABTEST_HELP = """
A/B 测试分析: 统计显著性检验 + SRM 检测 + 决策矩阵

CSV 格式:
  variant,users,conversions

  variant     : 变体名称 (control / treatment)
  users       : 用户数
  conversions : 转化数

示例:
  variant,users,conversions
  control,10000,500
  treatment,10200,550
"""


def cmd_abtest(args):
    rows = read_csv(args.input)
    required = {"variant", "users", "conversions"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV 缺少列: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    variants = {}
    for r in rows:
        u, c = int(r["users"]), int(r["conversions"])
        variants[r["variant"]] = {"users": u, "conversions": c, "rate": c / u if u > 0 else 0}

    if len(variants) < 2:
        print("至少需要 2 个变体", file=sys.stderr)
        sys.exit(1)

    names = list(variants.keys())
    ctrl_name = names[0]
    treat_name = names[1]
    ctrl = variants[ctrl_name]
    treat = variants[treat_name]

    # SRM 检测
    total_users = ctrl["users"] + treat["users"]
    expected_ctrl = total_users * 0.5
    srm_chi2 = (ctrl["users"] - expected_ctrl) ** 2 / expected_ctrl + (treat["users"] - expected_ctrl) ** 2 / expected_ctrl
    srm_detected = abs(ctrl["users"] - treat["users"]) / total_users > 0.01

    # z 检验
    z, p_val = z_test(ctrl["rate"], ctrl["users"], treat["rate"], treat["users"])
    significant = p_val < 0.05
    lift = (treat["rate"] - ctrl["rate"]) / ctrl["rate"] * 100 if ctrl["rate"] > 0 else 0

    # MDE
    alpha = 0.05
    z_alpha = 1.96
    p_pool = (ctrl["conversions"] + treat["conversions"]) / (ctrl["users"] + treat["users"])
    mde = z_alpha * math.sqrt(2 * p_pool * (1 - p_pool) / min(ctrl["users"], treat["users"]))

    if srm_detected:
        decision = "⚠️ INVALID — SRM 检测到样本比例失衡，结果不可信"
    elif significant and lift > 0:
        decision = "✅ Ship — 显著正向，建议上线"
    elif significant and lift < 0:
        decision = "❌ Stop — 显著负向，停止实验"
    elif not significant:
        decision = "🔍 Investigate — 不显著，需拆分 segment 分析"
    else:
        decision = "🤷 无法判断"

    lines = ["# A/B 测试分析报告\n"]
    lines.append(f"对照组: {ctrl_name} | 实验组: {treat_name}\n")

    lines.append("## 基础数据\n")
    headers = ["变体", "用户数", "转化数", "转化率"]
    trows = [[ctrl_name, fmt_num(ctrl["users"], 0), ctrl["conversions"], pct(ctrl["rate"] * 100)],
             [treat_name, fmt_num(treat["users"], 0), treat["conversions"], pct(treat["rate"] * 100)]]
    lines.append(md_table(headers, trows))

    lines.append(f"**提升幅度**: {lift:+.2f}%\n")

    lines.append("## 统计检验\n")
    lines.append(f"- z 统计量: {z:.4f}")
    lines.append(f"- p 值: {p_val:.6f}")
    lines.append(f"- 显著性水平 α: {alpha}")
    lines.append(f"- 结论: {'显著 (p < 0.05)' if significant else '不显著 (p ≥ 0.05)'}")
    lines.append(f"- MDE (最小可检测效应): {pct(mde * 100)}\n")

    lines.append("## SRM 检测\n")
    lines.append(f"- 样本比例差异: {abs(ctrl['users'] - treat['users']) / total_users * 100:.2f}%")
    lines.append(f"- SRM 状态: {'⚠️ 检测到失衡' if srm_detected else '✅ 正常'}")
    lines.append(f"- χ² = {srm_chi2:.4f}\n")

    lines.append(f"## 决策: {decision}")

    if args.json:
        result = {"control": ctrl, "treatment": treat, "z": z, "p_value": p_val,
                   "significant": significant, "lift": lift, "srm_detected": srm_detected,
                   "mde": mde, "decision": decision}
        write_output(json.dumps(result, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── RFM Model ─────────────────────────

RFM_HELP = """
RFM 用户分层: Recency × Frequency × Monetary → 8 段分类

CSV 格式:
  customer_id,recency,frequency,monetary

  customer_id : 客户标识
  recency     : 距上次购买天数
  frequency   : 购买次数
  monetary    : 消费总额

示例:
  customer_id,recency,frequency,monetary
  C001,5,20,5000
  C002,90,3,300
  C003,15,10,2000
"""


def cmd_rfm(args):
    rows = read_csv(args.input)
    required = {"customer_id", "recency", "frequency", "monetary"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV 缺少列: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    data = []
    for r in rows:
        data.append({"id": r["customer_id"], "recency": float(r["recency"]),
                      "frequency": float(r["frequency"]), "monetary": float(r["monetary"])})

    r_vals = [d["recency"] for d in data]
    f_vals = [d["frequency"] for d in data]
    m_vals = [d["monetary"] for d in data]

    r_scores = quintile_score(r_vals, reverse=True)
    f_scores = quintile_score(f_vals)
    m_scores = quintile_score(m_vals)

    for i, d in enumerate(data):
        d["r"] = r_scores[i]
        d["f"] = f_scores[i]
        d["m"] = m_scores[i]
        r_hi = d["r"] >= 4
        f_hi = d["f"] >= 4
        m_hi = d["m"] >= 4
        if r_hi and f_hi and m_hi:
            d["segment"] = "重要价值用户"
        elif not r_hi and f_hi and m_hi:
            d["segment"] = "重要保持用户"
        elif r_hi and not f_hi and m_hi:
            d["segment"] = "重要发展用户"
        elif not r_hi and not f_hi and m_hi:
            d["segment"] = "重要挽留用户"
        elif r_hi and f_hi and not m_hi:
            d["segment"] = "一般价值用户"
        elif not r_hi and f_hi and not m_hi:
            d["segment"] = "一般保持用户"
        elif r_hi and not f_hi and not m_hi:
            d["segment"] = "一般发展用户"
        else:
            d["segment"] = "一般挽留用户"

    segments = {}
    for d in data:
        seg = d["segment"]
        if seg not in segments:
            segments[seg] = []
        segments[seg].append(d)

    lines = ["# RFM 用户分层报告\n"]
    lines.append(f"客户总数: {len(data)}\n")

    lines.append("## 分层统计\n")
    headers = ["分层", "人数", "占比", "平均 R", "平均 F", "平均 M"]
    seg_order = ["重要价值用户", "重要保持用户", "重要发展用户", "重要挽留用户",
                  "一般价值用户", "一般保持用户", "一般发展用户", "一般挽留用户"]
    trows = []
    for seg in seg_order:
        if seg in segments:
            members = segments[seg]
            avg_r = sum(m["recency"] for m in members) / len(members)
            avg_f = sum(m["frequency"] for m in members) / len(members)
            avg_m = sum(m["monetary"] for m in members) / len(members)
            trows.append([seg, len(members), pct(len(members) / len(data) * 100),
                           f"{avg_r:.0f}", f"{avg_f:.1f}", fmt_num(avg_m, 0)])
    lines.append(md_table(headers, trows))

    lines.append("## 客户明细（前 20）\n")
    headers2 = ["客户", "R", "F", "M", "Recency", "Frequency", "Monetary", "分层"]
    trows2 = [[d["id"], d["r"], d["f"], d["m"], f"{d['recency']:.0f}",
               f"{d['frequency']:.0f}", fmt_num(d["monetary"], 0), d["segment"]] for d in data[:20]]
    lines.append(md_table(headers2, trows2))

    if args.json:
        write_output(json.dumps(data, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── Cohort Analysis ─────────────────────────

COHORT_HELP = """
同期群留存分析: 按时间分组追踪留存率

CSV 格式:
  cohort,period,active,initial

  cohort  : 同期群标识 (如 2024-01, 2024-02)
  period  : 期数 (0=初始, 1=第1期, 2=第2期, ...)
  active  : 活跃用户数
  initial : 初始用户数

示例:
  cohort,period,active,initial
  2024-01,0,1000,1000
  2024-01,1,600,1000
  2024-01,2,400,1000
  2024-02,0,800,800
  2024-02,1,500,800
"""


def cmd_cohort(args):
    rows = read_csv(args.input)
    required = {"cohort", "period", "active", "initial"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV 缺少列: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    cohorts = {}
    max_period = 0
    for r in rows:
        c = r["cohort"]
        p = int(r["period"])
        a = int(r["active"])
        ini = int(r["initial"])
        if c not in cohorts:
            cohorts[c] = {}
        cohorts[c][p] = {"active": a, "initial": ini, "retention": a / ini if ini > 0 else 0}
        max_period = max(max_period, p)

    cohort_names = sorted(cohorts.keys())
    periods = list(range(max_period + 1))

    lines = ["# 同期群留存分析报告\n"]
    lines.append(f"同期群数: {len(cohort_names)} | 最大期数: {max_period}\n")

    lines.append("## 留存率矩阵\n")
    headers = ["Cohort", "初始"] + [f"P{p}" for p in periods if p > 0]
    trows = []
    for c in cohort_names:
        ini = cohorts[c].get(0, {}).get("initial", 0)
        row = [c, str(ini)]
        for p in periods:
            if p == 0:
                continue
            if p in cohorts[c]:
                row.append(pct(cohorts[c][p]["retention"] * 100))
            else:
                row.append("-")
        trows.append(row)
    lines.append(md_table(headers, trows))

    lines.append("## 各期平均留存率\n")
    avg_headers = ["期数"] + [f"P{p}" for p in periods if p > 0]
    avg_row = ["平均"]
    for p in periods:
        if p == 0:
            continue
        vals = [cohorts[c][p]["retention"] * 100 for c in cohort_names if p in cohorts[c]]
        avg_row.append(pct(sum(vals) / len(vals)) if vals else "-")
    lines.append(md_table(avg_headers, [avg_row]))

    lines.append("## PMF 信号\n")
    for p in periods:
        if p == 0:
            continue
        vals = [cohorts[c][p]["retention"] * 100 for c in cohort_names if p in cohorts[c]]
        if vals:
            avg = sum(vals) / len(vals)
            trend = "稳定" if avg > 30 else "偏低"
            lines.append(f"- P{p} 平均留存: {pct(avg)} — {trend}")

    if args.json:
        result = {"cohorts": {c: {str(p): cohorts[c][p] for p in cohorts[c]} for c in cohort_names}}
        write_output(json.dumps(result, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)
