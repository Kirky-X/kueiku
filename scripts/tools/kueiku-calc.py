#!/usr/bin/env python3
"""kueiku-calc — Kueiku 方法论计算工具集

将 15 个高计算密度方法论自动化：RICE / Decision Matrix / Risk Matrix / DuPont / Pareto /
FMEA / ICE / Opportunity Score / DCF / EVA / A/B Test / RFM / Cohort / BCG / GE-McKinsey。
纯 Python 标准库实现，无外部依赖。

用法:
  python kueiku-calc.py <subcommand> -i <input.csv> [-o report.md] [--json]

子命令:
  rice       RICE 优先级评分          dmatrix  决策矩阵（Pugh Matrix）
  risk       风险矩阵                  dupont   杜邦分析
  pareto     帕累托分析                fmea     FMEA 失效模式分析
  ice        ICE 评分                  oppscore 机会评分
  dcf        现金流折现估值            eva      经济增加值
  abtest     A/B 测试显著性分析        rfm      RFM 用户分层
  cohort     同期群留存分析            bcg      BCG 矩阵
  gemckinsey GE-McKinsey 矩阵

每个子命令支持 --help 查看 CSV 格式要求。
"""

import argparse
import csv
import io
import json
import math
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


# ───────────────────────── FMEA ─────────────────────────

FMEA_HELP = """
FMEA 失效模式与影响分析: RPN = 严重度(S) × 频度(O) × 探测度(D)

CSV 格式:
  name,severity,occurrence,detection,category

  name      : 失效模式描述
  severity  : 严重度 (1-10)
  occurrence: 频度 (1-10)
  detection : 探测度 (1-10, 1=必能检出, 10=无法检出)
  category  : 类别（可选）

示例:
  name,severity,occurrence,detection,category
  电源过载,8,4,3,硬件
  数据丢失,9,3,5,软件
"""


def cmd_fmea(args):
    rows = read_csv(args.input)
    required = {"name", "severity", "occurrence", "detection"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV 缺少列: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    items = []
    for r in rows:
        s, o, d = int(r["severity"]), int(r["occurrence"]), int(r["detection"])
        rpn = s * o * d
        if rpn >= 200:
            zone, action = "极高", "立即采取纠正措施"
        elif rpn >= 100:
            zone, action = "高", "尽快制定缓解方案"
        elif rpn >= 50:
            zone, action = "中", "纳入监控并计划改善"
        else:
            zone, action = "低", "常规监控"
        items.append({"name": r["name"], "s": s, "o": o, "d": d, "rpn": rpn,
                       "zone": zone, "action": action, "category": r.get("category", "")})

    items.sort(key=lambda x: x["rpn"], reverse=True)

    lines = ["# FMEA 失效模式分析报告\n"]
    lines.append(f"失效模式数: {len(items)}\n")
    lines.append("## 风险优先数排序\n")
    headers = ["排名", "失效模式", "S", "O", "D", "RPN", "风险等级", "应对策略"]
    trows = [[i+1, it["name"], it["s"], it["o"], it["d"], it["rpn"], it["zone"], it["action"]] for i, it in enumerate(items)]
    lines.append(md_table(headers, trows))

    high = [it for it in items if it["rpn"] >= 100]
    if high:
        lines.append("## 需优先处理的失效模式\n")
        for it in high:
            lines.append(f"- **{it['name']}** (RPN={it['rpn']}, {it['zone']}) → {it['action']}")

    if args.json:
        write_output(json.dumps(items, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── ICE Framework ─────────────────────────

ICE_HELP = """
ICE 评分: Score = Impact × Confidence × Ease

CSV 格式:
  name,impact,confidence,ease

  name       : 想法/功能名称
  impact     : 影响力 (1-10)
  confidence : 信心度 (1-10)
  ease       : 容易度 (1-10, 越容易分越高)

示例:
  name,impact,confidence,ease
  用户推荐,8,7,9
  付费墙优化,6,5,4
"""


def cmd_ice(args):
    rows = read_csv(args.input)
    required = {"name", "impact", "confidence", "ease"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV 缺少列: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    items = []
    for r in rows:
        i, c, e = float(r["impact"]), float(r["confidence"]), float(r["ease"])
        score = i * c * e
        items.append({"name": r["name"], "impact": i, "confidence": c, "ease": e, "score": score})

    items.sort(key=lambda x: x["score"], reverse=True)

    lines = ["# ICE 评分报告\n"]
    lines.append(f"评估项数: {len(items)}\n")
    lines.append("## 排序结果\n")
    headers = ["排名", "名称", "Impact", "Confidence", "Ease", "ICE 分"]
    trows = [[i+1, it["name"], it["impact"], it["confidence"], it["ease"], fmt_num(it["score"], 0)] for i, it in enumerate(items)]
    lines.append(md_table(headers, trows))

    if len(items) >= 3:
        top = max(1, len(items) // 3)
        lines.append("## 分层建议\n")
        lines.append(f"- **必做 (Top {top})**: {', '.join(it['name'] for it in items[:top])}")
        lines.append(f"- **候选**: {', '.join(it['name'] for it in items[top:])}")

    if args.json:
        write_output(json.dumps(items, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── Opportunity Score ─────────────────────────

OPPSCORE_HELP = """
机会评分: Opportunity = Importance × (1 - Satisfaction)

CSV 格式:
  name,importance,satisfaction

  name         : 需求/功能名称
  importance   : 重要度 (1-5)
  satisfaction : 当前满意度 (1-5)

示例:
  name,importance,satisfaction
  快速响应,5,2
  界面美观,3,4
"""


def cmd_oppscore(args):
    rows = read_csv(args.input)
    required = {"name", "importance", "satisfaction"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV 缺少列: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    items = []
    for r in rows:
        imp, sat = float(r["importance"]), float(r["satisfaction"])
        imp_n = (imp - 1) / 4  # 归一化到 0-1
        sat_n = (sat - 1) / 4
        opp = imp_n * (1 - sat_n)
        items.append({"name": r["name"], "importance": imp, "satisfaction": sat,
                       "imp_norm": imp_n, "sat_norm": sat_n, "opportunity": opp})

    items.sort(key=lambda x: x["opportunity"], reverse=True)

    lines = ["# 机会评分报告\n"]
    lines.append(f"评估需求数: {len(items)}\n")
    lines.append("## 排序结果\n")
    headers = ["排名", "需求", "重要度", "满意度", "机会分"]
    trows = [[i+1, it["name"], it["importance"], it["satisfaction"], f"{it['opportunity']:.3f}"] for i, it in enumerate(items)]
    lines.append(md_table(headers, trows))

    # 分类
    opportunities = [it for it in items if it["opportunity"] >= 0.5]
    satisfied = [it for it in items if it["satisfaction"] >= 4 and it["importance"] >= 4]
    low_priority = [it for it in items if it["importance"] <= 2]

    lines.append("## 分类建议\n")
    if opportunities:
        lines.append(f"### 蓝海机会（{len(opportunities)} 项）\n")
        for it in opportunities:
            lines.append(f"- **{it['name']}** — 重要度 {it['importance']}, 满意度 {it['satisfaction']}, 机会分 {it['opportunity']:.3f}")
    if satisfied:
        lines.append(f"\n### 已满足的高重要需求（{len(satisfied)} 项）\n")
        for it in satisfied:
            lines.append(f"- {it['name']} — 维持现状即可")
    if low_priority:
        lines.append(f"\n### 低优先级（{len(low_priority)} 项）\n")
        for it in low_priority:
            lines.append(f"- {it['name']} — 不值得投入")

    if args.json:
        write_output(json.dumps(items, ensure_ascii=False, indent=2), args.output)
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

    # 折现计算
    pv_items = []
    total_pv = 0
    for cf in cashflows:
        t = cf["year"]
        pv = cf["fcf"] / ((1 + rate) ** t)
        total_pv += pv
        pv_items.append({"year": t, "fcf": cf["fcf"], "pv": pv, "discount_factor": 1 / ((1 + rate) ** t)})

    # 终值 (Gordon Growth Model)
    last_fcf = cashflows[-1]["fcf"]
    n = cashflows[-1]["year"]
    terminal_value = last_fcf * (1 + growth) / (rate - growth)
    terminal_pv = terminal_value / ((1 + rate) ** n)
    enterprise_value = total_pv + terminal_pv

    per_share = enterprise_value / shares if shares > 0 else 0

    # 敏感性分析
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
    lines.append(f"折现率: {pct(rate*100)} | 永续增长率: {pct(growth*100)} | 预测期: {n} 年\n")

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
    s_rows = [[pct(s["discount_rate"]*100), fmt_num(s["enterprise_value"], 0)] + ([fmt_num(s["per_share"])] if shares > 0 else []) for s in sensitivity]
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
              fmt_num(it["eva"], 0), pct(it["roic"]*100), pct(it["spread"]*100)] for it in items]
    lines.append(md_table(headers, trows))

    lines.append("## 原始数据\n")
    h2 = ["期间", "EBIT", "税率", "投入资本", "WACC"]
    t2 = [[it["period"], fmt_num(it["ebit"], 0), pct(it["tax_rate"]*100),
           fmt_num(it["invested_capital"], 0), pct(it["wacc"]*100)] for it in items]
    lines.append(md_table(h2, t2))

    # 诊断
    lines.append("## 诊断\n")
    for it in items:
        if it["eva"] > 0:
            lines.append(f"- **{it['period']}**: EVA > 0，创造价值 (Spread = {pct(it['spread']*100)})")
        else:
            lines.append(f"- **{it['period']}**: EVA < 0，毁灭价值！ROIC ({pct(it['roic']*100)}) < WACC ({pct(it['wacc']*100)})")

    if args.json:
        write_output(json.dumps(items, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


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


def _z_test(p1, n1, p2, n2):
    """双比例 z 检验，返回 (z_stat, p_value_approx)。"""
    p_pool = (n1 * p1 + n2 * p2) / (n1 + n2)
    se = math.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))
    if se == 0:
        return 0, 1.0
    z = (p2 - p1) / se
    # 近似 p-value (two-tailed)
    p_val = 2 * (1 - _norm_cdf(abs(z)))
    return z, p_val


def _norm_cdf(x):
    """标准正态分布 CDF 近似。"""
    # Abramowitz & Stegun 近似
    a1, a2, a3, a4, a5 = 0.254829592, -0.284496736, 1.421413741, -1.453152027, 1.061405429
    p = 0.3275911
    sign = 1 if x >= 0 else -1
    x = abs(x) / math.sqrt(2)
    t = 1.0 / (1.0 + p * x)
    y = 1.0 - (((((a5*t + a4)*t) + a3)*t + a2)*t + a1)*t * math.exp(-x*x)
    return 0.5 * (1.0 + sign * y)


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
    expected_ratio = ctrl["users"] / (ctrl["users"] + treat["users"])
    actual_ratio = ctrl["users"] / (ctrl["users"] + treat["users"])
    total_users = ctrl["users"] + treat["users"]
    expected_ctrl = total_users * 0.5  # 假设 1:1 分配
    srm_chi2 = (ctrl["users"] - expected_ctrl)**2 / expected_ctrl + (treat["users"] - expected_ctrl)**2 / expected_ctrl
    srm_detected = abs(ctrl["users"] - treat["users"]) / total_users > 0.01

    # z 检验
    z, p_val = _z_test(ctrl["rate"], ctrl["users"], treat["rate"], treat["users"])
    significant = p_val < 0.05
    lift = (treat["rate"] - ctrl["rate"]) / ctrl["rate"] * 100 if ctrl["rate"] > 0 else 0

    # MDE (Minimum Detectable Effect)
    alpha = 0.05
    z_alpha = 1.96
    z_beta = 0.84  # power = 0.8
    p_pool = (ctrl["conversions"] + treat["conversions"]) / (ctrl["users"] + treat["users"])
    mde = z_alpha * math.sqrt(2 * p_pool * (1 - p_pool) / min(ctrl["users"], treat["users"]))

    # 决策
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
    trows = [[ctrl_name, fmt_num(ctrl["users"], 0), ctrl["conversions"], pct(ctrl["rate"]*100)],
             [treat_name, fmt_num(treat["users"], 0), treat["conversions"], pct(treat["rate"]*100)]]
    lines.append(md_table(headers, trows))

    lines.append(f"**提升幅度**: {lift:+.2f}%\n")

    lines.append("## 统计检验\n")
    lines.append(f"- z 统计量: {z:.4f}")
    lines.append(f"- p 值: {p_val:.6f}")
    lines.append(f"- 显著性水平 α: {alpha}")
    lines.append(f"- 结论: {'显著 (p < 0.05)' if significant else '不显著 (p ≥ 0.05)'}")
    lines.append(f"- MDE (最小可检测效应): {pct(mde*100)}\n")

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


def _quintile_score(values, reverse=False):
    """将值映射到 1-5 分位。reverse=True 表示值越小分越高（如 recency）。"""
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    scores = {}
    for i, v in enumerate(sorted_vals):
        q = min(4, int(i / n * 5))
        scores[v] = (5 - q) if reverse else (q + 1)
    return [scores[v] for v in values]


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

    r_scores = _quintile_score(r_vals, reverse=True)
    f_scores = _quintile_score(f_vals)
    m_scores = _quintile_score(m_vals)

    for i, d in enumerate(data):
        d["r"] = r_scores[i]
        d["f"] = f_scores[i]
        d["m"] = m_scores[i]
        # 8 段分类
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

    # 统计各段
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
            trows.append([seg, len(members), pct(len(members)/len(data)*100),
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

    # 留存矩阵
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

    # 平均留存
    lines.append("## 各期平均留存率\n")
    avg_headers = ["期数"] + [f"P{p}" for p in periods if p > 0]
    avg_row = ["平均"]
    for p in periods:
        if p == 0:
            continue
        vals = [cohorts[c][p]["retention"] * 100 for c in cohort_names if p in cohorts[c]]
        avg_row.append(pct(sum(vals)/len(vals)) if vals else "-")
    lines.append(md_table(avg_headers, [avg_row]))

    # PMF 判断
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


# ───────────────────────── BCG Matrix ─────────────────────────

BCG_HELP = """
BCG 矩阵: 市场增长率 × 相对市场份额 → 4 象限分类

CSV 格式:
  product,market_growth,relative_share,revenue

  product        : 产品/业务名称
  market_growth  : 市场增长率 (小数, 如 0.15 表示 15%)
  relative_share : 相对市场份额 (小数, 如 1.5 表示市场领先)
  revenue        : 收入（可选，用于气泡大小）

示例:
  product,market_growth,relative_share,revenue
  产品A,0.25,1.8,5000
  产品B,0.05,2.5,8000
  产品C,0.30,0.6,2000
  产品D,0.02,0.4,1000
"""


def cmd_bcg(args):
    rows = read_csv(args.input)
    required = {"product", "market_growth", "relative_share"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV 缺少列: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    growth_threshold = 0.10  # 10% 作为高/低增长分界
    share_threshold = 1.0    # 1.0 作为高/低份额分界

    items = []
    for r in rows:
        g = float(r["market_growth"])
        s = float(r["relative_share"])
        rev = float(r.get("revenue", 0))
        if g >= growth_threshold and s >= share_threshold:
            quadrant = "⭐ 明星 (Star)"
        elif g < growth_threshold and s >= share_threshold:
            quadrant = "💰 现金牛 (Cash Cow)"
        elif g >= growth_threshold and s < share_threshold:
            quadrant = "❓ 问号 (Question Mark)"
        else:
            quadrant = "🐕 瘦狗 (Dog)"
        items.append({"product": r["product"], "growth": g, "share": s,
                       "revenue": rev, "quadrant": quadrant})

    # 统计
    quads = {}
    for it in items:
        q = it["quadrant"]
        if q not in quads:
            quads[q] = []
        quads[q].append(it)

    lines = ["# BCG 矩阵分析报告\n"]
    lines.append(f"产品/业务数: {len(items)} | 增长阈值: {pct(growth_threshold*100)} | 份额阈值: {share_threshold}\n")

    lines.append("## 分类结果\n")
    headers = ["产品", "市场增长", "相对份额", "收入", "象限"]
    trows = [[it["product"], pct(it["growth"]*100), f"{it['share']:.2f}",
              fmt_num(it["revenue"], 0) if it["revenue"] else "-", it["quadrant"]] for it in items]
    lines.append(md_table(headers, trows))

    lines.append("## 战略建议\n")
    for q_name, members in quads.items():
        lines.append(f"### {q_name}（{len(members)} 项）\n")
        for m in members:
            lines.append(f"- **{m['product']}** — 增长 {pct(m['growth']*100)}, 份额 {m['share']:.2f}")
        if "Star" in q_name:
            lines.append("→ 策略: 加大投资，维持增长\n")
        elif "Cash Cow" in q_name:
            lines.append("→ 策略: 收割利润，减少投资\n")
        elif "Question" in q_name:
            lines.append("→ 策略: 选择性投资，或放弃\n")
        else:
            lines.append("→ 策略: 考虑退出或重组\n")

    if args.json:
        write_output(json.dumps(items, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── GE-McKinsey Matrix ─────────────────────────

GEMCKINSEY_HELP = """
GE-McKinsey 矩阵: 行业吸引力 × 竞争实力 → 9 格分类

CSV 格式:
  business,attractiveness,strength,revenue

  business       : 业务/产品名称
  attractiveness : 行业吸引力评分 (1-5)
  strength       : 竞争实力评分 (1-5)
  revenue        : 收入（可选）

示例:
  business,attractiveness,strength,revenue
  业务A,4.5,4.0,5000
  业务B,2.0,3.5,3000
  业务C,3.8,2.0,2000
"""


def cmd_gemckinsey(args):
    rows = read_csv(args.input)
    required = {"business", "attractiveness", "strength"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV 缺少列: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    items = []
    for r in rows:
        a = float(r["attractiveness"])
        s = float(r["strength"])
        rev = float(r.get("revenue", 0))
        # 9 格分类
        if a >= 3.67 and s >= 3.67:
            cell = "投资/成长"
        elif a >= 3.67 and s >= 2.33:
            cell = "选择性投资"
        elif a >= 3.67:
            cell = "选择性投资"
        elif a >= 2.33 and s >= 3.67:
            cell = "选择性投资"
        elif a >= 2.33 and s >= 2.33:
            cell = "选择性维持"
        elif a >= 2.33:
            cell = "收割"
        elif s >= 3.67:
            cell = "选择性维持"
        elif s >= 2.33:
            cell = "收割"
        else:
            cell = "退出/剥离"
        items.append({"business": r["business"], "attractiveness": a,
                       "strength": s, "revenue": rev, "cell": cell})

    # 统计
    cells = {}
    for it in items:
        c = it["cell"]
        if c not in cells:
            cells[c] = []
        cells[c].append(it)

    lines = ["# GE-McKinsey 矩阵分析报告\n"]
    lines.append(f"业务数: {len(items)}\n")

    lines.append("## 分类结果\n")
    headers = ["业务", "行业吸引力", "竞争实力", "收入", "策略区域"]
    trows = [[it["business"], f"{it['attractiveness']:.1f}", f"{it['strength']:.1f}",
              fmt_num(it["revenue"], 0) if it["revenue"] else "-", it["cell"]] for it in items]
    lines.append(md_table(headers, trows))

    # 3x3 矩阵可视化
    lines.append("## 矩阵视图\n")
    lines.append("```")
    lines.append("              竞争实力")
    lines.append("              强(>3.67)  中(2.33-3.67)  弱(<2.33)")
    for a_label, a_range in [("高(>3.67)", (3.67, 5.01)), ("中(2.33-3.67)", (2.33, 3.67)), ("低(<2.33)", (0, 2.33))]:
        lines.append(f"吸引力 {a_label}")
        for s_label, s_range in [("强", (3.67, 5.01)), ("中", (2.33, 3.67)), ("弱", (0, 2.33))]:
            in_cell = [it for it in items if a_range[0] <= it["attractiveness"] < a_range[1]
                        and s_range[0] <= it["strength"] < s_range[1]]
            names = ", ".join(it["business"][:6] for it in in_cell) if in_cell else "·"
            lines.append(f"              {names:<20}")
    lines.append("```\n")

    lines.append("## 战略建议\n")
    for cell_name, members in cells.items():
        lines.append(f"### {cell_name}（{len(members)} 项）\n")
        for m in members:
            lines.append(f"- **{m['business']}** — 吸引力 {m['attractiveness']:.1f}, 实力 {m['strength']:.1f}")
        if cell_name == "投资/成长":
            lines.append("→ 积极投资，扩大市场份额\n")
        elif cell_name == "选择性投资":
            lines.append("→ 有针对性地投资，聚焦优势领域\n")
        elif cell_name == "选择性维持":
            lines.append("→ 维持现状，控制成本\n")
        elif cell_name == "收割":
            lines.append("→ 最大化现金流，减少新投资\n")
        else:
            lines.append("→ 考虑退出或剥离\n")

    if args.json:
        write_output(json.dumps(items, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── CLI 入口 ─────────────────────────

def main():
    parser = argparse.ArgumentParser(
        prog="kueiku-calc",
        description="Kueiku 方法论计算工具集 — 15 个高计算密度方法论自动化",
    )
    subparsers = parser.add_subparsers(dest="command", help="子命令")

    # 公共参数辅助函数
    def add_common_args(p):
        p.add_argument("-i", "--input", required=True, help="CSV 文件路径（- 表示 stdin）")
        p.add_argument("-o", "--output", help="输出文件路径（默认 stdout）")
        p.add_argument("--json", action="store_true", help="输出 JSON 格式")

    # rice
    p = subparsers.add_parser("rice", help="RICE 优先级评分", description=RICE_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # dmatrix
    p = subparsers.add_parser("dmatrix", help="决策矩阵（Pugh Matrix）", description=DMATRIX_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # risk
    p = subparsers.add_parser("risk", help="风险矩阵", description=RISK_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # dupont
    p = subparsers.add_parser("dupont", help="杜邦分析", description=DUPONT_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # pareto
    p = subparsers.add_parser("pareto", help="帕累托分析", description=PARETO_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # fmea
    p = subparsers.add_parser("fmea", help="FMEA 失效模式分析", description=FMEA_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # ice
    p = subparsers.add_parser("ice", help="ICE 评分", description=ICE_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # oppscore
    p = subparsers.add_parser("oppscore", help="机会评分", description=OPPSCORE_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # dcf
    p = subparsers.add_parser("dcf", help="现金流折现估值", description=DCF_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)
    p.add_argument("--rate", type=float, default=0.10, help="折现率 (WACC), 默认 0.10")
    p.add_argument("--growth", type=float, default=0.03, help="永续增长率, 默认 0.03")
    p.add_argument("--shares", type=float, default=0, help="流通股数（可选）")

    # eva
    p = subparsers.add_parser("eva", help="经济增加值", description=EVA_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # abtest
    p = subparsers.add_parser("abtest", help="A/B 测试显著性分析", description=ABTEST_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # rfm
    p = subparsers.add_parser("rfm", help="RFM 用户分层", description=RFM_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # cohort
    p = subparsers.add_parser("cohort", help="同期群留存分析", description=COHORT_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # bcg
    p = subparsers.add_parser("bcg", help="BCG 矩阵", description=BCG_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # gemckinsey
    p = subparsers.add_parser("gemckinsey", help="GE-McKinsey 矩阵", description=GEMCKINSEY_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        "rice": cmd_rice, "dmatrix": cmd_dmatrix, "risk": cmd_risk,
        "dupont": cmd_dupont, "pareto": cmd_pareto, "fmea": cmd_fmea,
        "ice": cmd_ice, "oppscore": cmd_oppscore, "dcf": cmd_dcf,
        "eva": cmd_eva, "abtest": cmd_abtest, "rfm": cmd_rfm,
        "cohort": cmd_cohort, "bcg": cmd_bcg, "gemckinsey": cmd_gemckinsey,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
