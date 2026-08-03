#!/usr/bin/env python3
"""kueiku-calc — Kueiku 方法论计算工具集

将 5 个高计算密度方法论自动化：RICE / Decision Matrix / Risk Matrix / DuPont / Pareto。
纯 Python 标准库实现，无外部依赖。

用法:
  python kueiku-calc.py rice       -i items.csv [-o report.md]
  python kueiku-calc.py dmatrix    -i scores.csv [-o report.md]
  python kueiku-calc.py risk       -i risks.csv  [-o report.md]
  python kueiku-calc.py dupont     -i finance.csv [-o report.md]
  python kueiku-calc.py pareto     -i items.csv  [-o report.md]

每个子命令支持 --help 查看 CSV 格式要求。
"""

import argparse
import csv
import io
import json
import sys
from pathlib import Path

# ───────────────────────── 公共工具 ─────────────────────────

def read_csv(source):
    """从文件路径或 stdin 读取 CSV，返回 list[dict]。"""
    if source == "-" or source is None:
        text = sys.stdin.read()
    else:
        text = Path(source).read_text(encoding="utf-8")
    reader = csv.DictReader(io.StringIO(text))
    return [row for row in reader]


def write_output(content, output_path=None):
    """输出到文件或 stdout。"""
    if output_path:
        Path(output_path).write_text(content, encoding="utf-8")
        print(f"报告已写入: {output_path}", file=sys.stderr)
    else:
        print(content)


def md_table(headers, rows):
    """生成 Markdown 表格字符串。"""
    if not rows:
        return "(空表)\n"
    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))
    fmt = " | ".join(f"{{:<{w}}}" for w in col_widths)
    sep = "-|-".join("-" * w for w in col_widths)
    lines = [fmt.format(*headers), sep]
    for row in rows:
        lines.append(fmt.format(*[str(c) for c in row]))
    return "\n".join(lines) + "\n"


def fmt_num(n, decimals=2):
    """格式化数字，千分位 + 小数。"""
    if isinstance(n, int):
        return f"{n:,}"
    if abs(n) >= 1000:
        return f"{n:,.{decimals}f}"
    return f"{n:.{decimals}f}"


def pct(n, decimals=1):
    return f"{n:.{decimals}f}%"


# ───────────────────────── RICE Scoring ─────────────────────────

RICE_HELP = """
RICE 优先级评分: Score = (Reach × Impact × Confidence) ÷ Effort

CSV 格式 (表头必须匹配):
  name,reach,impact,confidence,effort

  name       : 需求/功能名称
  reach      : 覆盖用户数（人/月）
  impact     : 影响力 (0.25 / 0.5 / 1 / 2 / 3)
  confidence : 信心度百分比 (100 / 80 / 50)
  effort     : 工作量（人月）

示例:
  name,reach,impact,confidence,effort
  功能A,50000,2,80,2
  功能B,20000,3,50,1
"""


def cmd_rice(args):
    rows = read_csv(args.input)
    required = {"name", "reach", "impact", "confidence", "effort"}
    if not required.issubset(rows[0].keys()):
        missing = required - set(rows[0].keys())
        print(f"CSV 缺少列: {missing}", file=sys.stderr)
        sys.exit(1)

    scored = []
    for r in rows:
        reach = float(r["reach"])
        impact = float(r["impact"])
        conf = float(r["confidence"]) / 100.0  # 百分比 → 小数
        effort = float(r["effort"])
        if effort <= 0:
            print(f"警告: '{r['name']}' 的 Effort={effort}，已跳过", file=sys.stderr)
            continue
        score = (reach * impact * conf) / effort
        scored.append({
            "name": r["name"],
            "reach": reach,
            "impact": impact,
            "confidence": float(r["confidence"]),
            "effort": effort,
            "score": score,
        })

    scored.sort(key=lambda x: x["score"], reverse=True)

    # 生成报告
    lines = ["# RICE 优先级评分报告\n"]
    lines.append(f"评估项数: {len(scored)}\n")
    lines.append("## 排序结果\n")
    headers = ["排名", "名称", "Reach", "Impact", "Confidence", "Effort", "RICE 分"]
    table_rows = []
    for i, s in enumerate(scored, 1):
        table_rows.append([
            i, s["name"], fmt_num(s["reach"], 0), s["impact"],
            f"{s['confidence']:.0f}%", s["effort"], fmt_num(s["score"], 0)
        ])
    lines.append(md_table(headers, table_rows))

    # 分层建议
    if len(scored) >= 3:
        top_third = max(1, len(scored) // 3)
        lines.append("## 分层建议\n")
        lines.append(f"- **必做 (Top {top_third})**: {', '.join(s['name'] for s in scored[:top_third])}")
        mid_end = max(top_third * 2, len(scored) - 1)
        lines.append(f"- **目标**: {', '.join(s['name'] for s in scored[top_third:mid_end])}")
        lines.append(f"- **待排期**: {', '.join(s['name'] for s in scored[mid_end:])}")

    # JSON 输出
    if args.json:
        write_output(json.dumps(scored, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── Decision Matrix ─────────────────────────

DMATRIX_HELP = """
决策矩阵（Pugh Matrix）: 多方案 × 多标准加权评分

CSV 格式（长表，每行一个方案-标准组合）:
  option,criterion,weight,score

  option    : 方案名称
  criterion : 评估标准
  weight    : 权重（百分比，如 30 表示 30%）
  score     : 得分（1-5 或 1-10）

示例:
  option,criterion,weight,score
  Node.js,开发效率,30,5
  Node.js,性能,25,3
  Go,开发效率,30,4
  Go,性能,25,5
"""


def cmd_dmatrix(args):
    rows = read_csv(args.input)
    required = {"option", "criterion", "weight", "score"}
    if not required.issubset(rows[0].keys()):
        missing = required - set(rows[0].keys())
        print(f"CSV 缺少列: {missing}", file=sys.stderr)
        sys.exit(1)

    # 解析数据
    options = []
    criteria = []
    data = {}  # {(option, criterion): score}
    weights = {}

    for r in rows:
        opt = r["option"].strip()
        crit = r["criterion"].strip()
        w = float(r["weight"])
        s = float(r["score"])
        if opt not in options:
            options.append(opt)
        if crit not in criteria:
            criteria.append(crit)
        data[(opt, crit)] = s
        weights[crit] = w

    # 验证权重总和
    total_weight = sum(weights.values())
    if abs(total_weight - 100) > 1:
        print(f"警告: 权重总和 = {total_weight}%（应为 100%）", file=sys.stderr)

    # 计算加权总分
    totals = {}
    details = {}
    for opt in options:
        total = 0
        detail = {}
        for crit in criteria:
            s = data.get((opt, crit), 0)
            w = weights.get(crit, 0) / 100.0
            weighted = s * w
            total += weighted
            detail[crit] = {"score": s, "weight": weights.get(crit, 0), "weighted": weighted}
        totals[opt] = total
        details[opt] = detail

    # 排序
    ranked = sorted(options, key=lambda o: totals[o], reverse=True)

    # 敏感性分析：每个标准权重 ±10%
    sensitivity = []
    for crit in criteria:
        orig_w = weights[crit]
        new_w = orig_w * 0.8  # 降低 20%
        scale = new_w / orig_w if orig_w > 0 else 1
        new_totals = {}
        for opt in options:
            nt = 0
            for c in criteria:
                s = data.get((opt, c), 0)
                w = weights[c] / 100.0
                if c == crit:
                    w = new_w / 100.0
                nt += s * w
            new_totals[opt] = nt
        new_ranked = sorted(options, key=lambda o: new_totals[o], reverse=True)
        changed = new_ranked[0] != ranked[0]
        sensitivity.append({
            "criterion": crit,
            "orig_weight": orig_w,
            "winner_if_reduced": new_ranked[0],
            "changed": changed,
        })

    # 生成报告
    lines = ["# 决策矩阵分析报告\n"]
    lines.append(f"方案数: {len(options)} | 标准数: {len(criteria)} | 权重总和: {total_weight}%\n")

    # 评分矩阵
    lines.append("## 评分矩阵\n")
    headers = ["标准", "权重"] + options
    table_rows = []
    for crit in criteria:
        row = [crit, f"{weights[crit]}%"]
        for opt in options:
            row.append(f"{data.get((opt, crit), 0):.0f}")
        table_rows.append(row)
    # 总分行
    total_row = ["**总分**", ""]
    for opt in options:
        total_row.append(f"**{fmt_num(totals[opt])}**")
    table_rows.append(total_row)
    lines.append(md_table(headers, table_rows))

    # 排名
    lines.append("## 排名\n")
    for i, opt in enumerate(ranked, 1):
        marker = " ← 推荐" if i == 1 else ""
        lines.append(f"{i}. **{opt}** — {fmt_num(totals[opt])} 分{marker}")
    lines.append("")

    # 敏感性
    lines.append("## 敏感性分析\n")
    sens_headers = ["标准", "原权重", "权重降低后胜者", "结论变化?"]
    sens_rows = []
    for s in sensitivity:
        sens_rows.append([
            s["criterion"], f"{s['orig_weight']}%",
            s["winner_if_reduced"], "是 ⚠️" if s["changed"] else "否"
        ])
    lines.append(md_table(sens_headers, sens_rows))

    # 分差分析
    if len(ranked) >= 2:
        gap = totals[ranked[0]] - totals[ranked[1]]
        lines.append(f"\n第一名与第二名分差: **{fmt_num(gap)}**")
        if gap < 0.3:
            lines.append("⚠️ 分差 < 0.3，两方案势均力敌，建议做进一步评估。")

    if args.json:
        result = {
            "options": {opt: {"total": totals[opt], "details": details[opt]} for opt in options},
            "ranking": [{"rank": i+1, "option": opt, "score": totals[opt]} for i, opt in enumerate(ranked)],
            "sensitivity": sensitivity,
        }
        write_output(json.dumps(result, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── Risk Matrix ─────────────────────────

RISK_HELP = """
风险矩阵: 概率 × 影响 快速风险评估与排序

CSV 格式:
  name,probability,impact,category

  name        : 风险描述
  probability : 概率 (1-5)
  impact      : 影响 (1-5)
  category    : 风险类别（可选，用于分组）

示例:
  name,probability,impact,category
  服务器宕机,3,5,技术
  关键人员离职,2,4,人员
  需求变更频繁,4,3,需求
"""


def cmd_risk(args):
    rows = read_csv(args.input)
    required = {"name", "probability", "impact"}
    if not required.issubset(rows[0].keys()):
        missing = required - set(rows[0].keys())
        print(f"CSV 缺少列: {missing}", file=sys.stderr)
        sys.exit(1)

    risks = []
    for r in rows:
        p = int(r["probability"])
        i = int(r["impact"])
        risk_value = p * i
        if risk_value >= 15:
            zone = "红色"
            zone_en = "CRITICAL"
            action = "立即行动"
        elif risk_value >= 8:
            zone = "橙色"
            zone_en = "HIGH"
            action = "主动缓解"
        elif risk_value >= 4:
            zone = "黄色"
            zone_en = "MEDIUM"
            action = "持续监控"
        else:
            zone = "绿色"
            zone_en = "LOW"
            action = "接受风险"
        risks.append({
            "name": r["name"],
            "probability": p,
            "impact": i,
            "risk_value": risk_value,
            "zone": zone,
            "zone_en": zone_en,
            "action": action,
            "category": r.get("category", ""),
        })

    risks.sort(key=lambda x: x["risk_value"], reverse=True)

    # 统计
    zone_counts = {"红色": 0, "橙色": 0, "黄色": 0, "绿色": 0}
    for r in risks:
        zone_counts[r["zone"]] += 1

    # 生成报告
    lines = ["# 风险评估报告\n"]
    lines.append(f"识别风险总数: {len(risks)}\n")
    lines.append("## 风险分布\n")
    lines.append(f"- 🔴 红色（极高 15-25）: {zone_counts['红色']} 项")
    lines.append(f"- 🟠 橙色（高 8-14）: {zone_counts['橙色']} 项")
    lines.append(f"- 🟡 黄色（中 4-7）: {zone_counts['黄色']} 项")
    lines.append(f"- 🟢 绿色（低 1-3）: {zone_counts['绿色']} 项\n")

    lines.append("## 风险清单（按风险值排序）\n")
    headers = ["排名", "风险", "概率", "影响", "风险值", "区域", "应对策略"]
    table_rows = []
    for idx, r in enumerate(risks, 1):
        table_rows.append([
            idx, r["name"], r["probability"], r["impact"],
            r["risk_value"], r["zone"], r["action"]
        ])
    lines.append(md_table(headers, table_rows))

    # 风险矩阵可视化（文本版）
    lines.append("## 风险矩阵\n")
    grid = {}
    for r in risks:
        grid[(r["probability"], r["impact"])] = r["name"][:8]
    lines.append("```\n影响 →  1    2    3    4    5")
    lines.append("概率 ↓")
    for p in range(5, 0, -1):
        row_str = f"  {p}  "
        for i in range(1, 6):
            val = p * i
            cell = grid.get((p, i), "·")
            if val >= 15:
                cell = f"🔴{cell}" if cell != "·" else "🔴·"
            elif val >= 8:
                cell = f"🟠{cell}" if cell != "·" else "🟠·"
            elif val >= 4:
                cell = f"🟡{cell}" if cell != "·" else "🟡·"
            row_str += f" {cell:>5}"
        lines.append(row_str)
    lines.append("```\n")

    # Top 风险行动建议
    critical = [r for r in risks if r["risk_value"] >= 8]
    if critical:
        lines.append("## 需立即关注的风险\n")
        for r in critical:
            lines.append(f"- **{r['name']}** (风险值 {r['risk_value']}, {r['zone']}) → {r['action']}")

    if args.json:
        write_output(json.dumps(risks, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


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
            "period": r["period"],
            "revenue": rev,
            "net_income": ni,
            "total_assets": ta,
            "equity": eq,
            "net_margin": net_margin,
            "asset_turnover": asset_turnover,
            "equity_multiplier": equity_multiplier,
            "roe": roe,
        })

    # 连环替代法（相邻期间对比）
    changes = []
    for i in range(1, len(periods)):
        prev = periods[i - 1]
        curr = periods[i]
        # 连环替代
        delta_margin = (curr["net_margin"] - prev["net_margin"]) * prev["asset_turnover"] * prev["equity_multiplier"]
        delta_turnover = curr["net_margin"] * (curr["asset_turnover"] - prev["asset_turnover"]) * prev["equity_multiplier"]
        delta_leverage = curr["net_margin"] * curr["asset_turnover"] * (curr["equity_multiplier"] - prev["equity_multiplier"])
        delta_roe = curr["roe"] - prev["roe"]
        changes.append({
            "from": prev["period"],
            "to": curr["period"],
            "delta_margin": delta_margin,
            "delta_turnover": delta_turnover,
            "delta_leverage": delta_leverage,
            "delta_roe": delta_roe,
        })

    # 生成报告
    lines = ["# 杜邦分析报告\n"]

    # 三因素数据表
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

    # 原始数据
    lines.append("## 原始财务数据\n")
    headers2 = ["期间", "营业收入", "净利润", "总资产", "股东权益"]
    table_rows2 = []
    for p in periods:
        table_rows2.append([
            p["period"], fmt_num(p["revenue"], 0), fmt_num(p["net_income"], 0),
            fmt_num(p["total_assets"], 0), fmt_num(p["equity"], 0)
        ])
    lines.append(md_table(headers2, table_rows2))

    # 因素变动贡献
    if changes:
        lines.append("## 因素变动贡献（连环替代法）\n")
        for c in changes:
            lines.append(f"### {c['from']} → {c['to']}\n")
            lines.append(f"- 净利率变动贡献: {c['delta_margin']:+.4f} ({pct(c['delta_margin'] / c['delta_roe'] * 100) if c['delta_roe'] != 0 else 'N/A'})")
            lines.append(f"- 周转率变动贡献: {c['delta_turnover']:+.4f} ({pct(c['delta_turnover'] / c['delta_roe'] * 100) if c['delta_roe'] != 0 else 'N/A'})")
            lines.append(f"- 权益乘数变动贡献: {c['delta_leverage']:+.4f} ({pct(c['delta_leverage'] / c['delta_roe'] * 100) if c['delta_roe'] != 0 else 'N/A'})")
            lines.append(f"- **ROE 总变动**: {c['delta_roe']:+.4f}\n")

    # 诊断建议
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


# ───────────────────────── Pareto Analysis ─────────────────────────

PARETO_HELP = """
帕累托分析: 识别关键少数（20% 原因产生 80% 影响）

CSV 格式:
  name,value

  name  : 项目名称
  value : 影响值（数值）

示例:
  name,value
  支付失败,420
  登录异常,300
  订单不同步,180
  退款查询,120
  地址修改,90
  优惠券,60
  其他,30
"""


def cmd_pareto(args):
    rows = read_csv(args.input)
    required = {"name", "value"}
    if not required.issubset(rows[0].keys()):
        missing = required - set(rows[0].keys())
        print(f"CSV 缺少列: {missing}", file=sys.stderr)
        sys.exit(1)

    items = []
    for r in rows:
        v = float(r["value"])
        if v <= 0:
            continue
        items.append({"name": r["name"], "value": v})

    items.sort(key=lambda x: x["value"], reverse=True)
    total = sum(i["value"] for i in items)
    if total == 0:
        print("所有值为 0，无法分析", file=sys.stderr)
        sys.exit(1)

    # 计算累积百分比
    cumulative = 0
    for item in items:
        pct_val = item["value"] / total * 100
        cumulative += pct_val
        item["pct"] = pct_val
        item["cumulative"] = cumulative
        item["classification"] = "关键少数" if cumulative <= 80 else ("临界" if cumulative - pct_val < 80 else "琐碎多数")

    vital = [i for i in items if i["classification"] == "关键少数" or i["classification"] == "临界"]
    trivial = [i for i in items if i["classification"] == "琐碎多数"]

    # 生成报告
    lines = ["# 帕累托分析报告\n"]
    lines.append(f"分析项数: {len(items)} | 总值: {fmt_num(total)}\n")

    lines.append("## 排序结果\n")
    headers = ["排名", "项目", "影响值", "占比", "累积占比", "分类"]
    table_rows = []
    for idx, item in enumerate(items, 1):
        marker = " ← 80% 分界" if (item["cumulative"] >= 80 and (item["cumulative"] - item["pct"]) < 80) else ""
        table_rows.append([
            idx, item["name"], fmt_num(item["value"]),
            pct(item["pct"]), pct(item["cumulative"]),
            item["classification"] + marker
        ])
    lines.append(md_table(headers, table_rows))

    # 关键少数
    vital_pct = sum(i["pct"] for i in vital)
    lines.append(f"\n## 关键少数（{len(vital)} 项，贡献 {pct(vital_pct)} 影响）\n")
    for i, item in enumerate(vital, 1):
        lines.append(f"{i}. **{item['name']}** — 影响值: {fmt_num(item['value'])} ({pct(item['pct'])})")

    if trivial:
        trivial_pct = sum(i["pct"] for i in trivial)
        lines.append(f"\n## 琐碎多数（{len(trivial)} 项，贡献 {pct(trivial_pct)} 影响）\n")
        lines.append("处理策略: 降低投入 / 标准化处理 / 暂缓 / 删除")

    # 累积分布（文本版）
    lines.append("\n## 累积分布\n")
    lines.append("```")
    bar_max = 40
    for item in items:
        bar_len = int(item["cumulative"] / 100 * bar_max)
        bar = "█" * bar_len + "░" * (bar_max - bar_len)
        lines.append(f"  {item['name']:<15} {bar} {pct(item['cumulative'])}")
    lines.append("```\n")

    if args.json:
        write_output(json.dumps(items, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── CLI 入口 ─────────────────────────

def main():
    parser = argparse.ArgumentParser(
        prog="kueiku-calc",
        description="Kueiku 方法论计算工具集 — 5 个高计算密度方法论自动化",
    )
    subparsers = parser.add_subparsers(dest="command", help="子命令")

    # rice
    p_rice = subparsers.add_parser("rice", help="RICE 优先级评分", description=RICE_HELP,
                                    formatter_class=argparse.RawDescriptionHelpFormatter)
    p_rice.add_argument("-i", "--input", required=True, help="CSV 文件路径（- 表示 stdin）")
    p_rice.add_argument("-o", "--output", help="输出文件路径（默认 stdout）")
    p_rice.add_argument("--json", action="store_true", help="输出 JSON 格式")

    # dmatrix
    p_dm = subparsers.add_parser("dmatrix", help="决策矩阵（Pugh Matrix）", description=DMATRIX_HELP,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    p_dm.add_argument("-i", "--input", required=True, help="CSV 文件路径")
    p_dm.add_argument("-o", "--output", help="输出文件路径")
    p_dm.add_argument("--json", action="store_true", help="输出 JSON 格式")

    # risk
    p_risk = subparsers.add_parser("risk", help="风险矩阵", description=RISK_HELP,
                                    formatter_class=argparse.RawDescriptionHelpFormatter)
    p_risk.add_argument("-i", "--input", required=True, help="CSV 文件路径")
    p_risk.add_argument("-o", "--output", help="输出文件路径")
    p_risk.add_argument("--json", action="store_true", help="输出 JSON 格式")

    # dupont
    p_dp = subparsers.add_parser("dupont", help="杜邦分析", description=DUPONT_HELP,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    p_dp.add_argument("-i", "--input", required=True, help="CSV 文件路径")
    p_dp.add_argument("-o", "--output", help="输出文件路径")
    p_dp.add_argument("--json", action="store_true", help="输出 JSON 格式")

    # pareto
    p_pa = subparsers.add_parser("pareto", help="帕累托分析", description=PARETO_HELP,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    p_pa.add_argument("-i", "--input", required=True, help="CSV 文件路径")
    p_pa.add_argument("-o", "--output", help="输出文件路径")
    p_pa.add_argument("--json", action="store_true", help="输出 JSON 格式")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        "rice": cmd_rice,
        "dmatrix": cmd_dmatrix,
        "risk": cmd_risk,
        "dupont": cmd_dupont,
        "pareto": cmd_pareto,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
