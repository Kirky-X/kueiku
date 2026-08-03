"""决策与优先级方法论 — RICE / Decision Matrix / ICE"""

import json
import sys

from .utils import read_csv, write_output, md_table, fmt_num

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
        conf = float(r["confidence"]) / 100.0
        effort = float(r["effort"])
        if effort <= 0:
            print(f"警告: '{r['name']}' 的 Effort={effort}，已跳过", file=sys.stderr)
            continue
        score = (reach * impact * conf) / effort
        scored.append({
            "name": r["name"], "reach": reach, "impact": impact,
            "confidence": float(r["confidence"]), "effort": effort, "score": score,
        })

    scored.sort(key=lambda x: x["score"], reverse=True)

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

    if len(scored) >= 3:
        top_third = max(1, len(scored) // 3)
        lines.append("## 分层建议\n")
        lines.append(f"- **必做 (Top {top_third})**: {', '.join(s['name'] for s in scored[:top_third])}")
        mid_end = max(top_third * 2, len(scored) - 1)
        lines.append(f"- **目标**: {', '.join(s['name'] for s in scored[top_third:mid_end])}")
        lines.append(f"- **待排期**: {', '.join(s['name'] for s in scored[mid_end:])}")

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

    options = []
    criteria = []
    data = {}
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

    total_weight = sum(weights.values())
    if abs(total_weight - 100) > 1:
        print(f"警告: 权重总和 = {total_weight}%（应为 100%）", file=sys.stderr)

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

    ranked = sorted(options, key=lambda o: totals[o], reverse=True)

    sensitivity = []
    for crit in criteria:
        orig_w = weights[crit]
        new_w = orig_w * 0.8
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
            "criterion": crit, "orig_weight": orig_w,
            "winner_if_reduced": new_ranked[0], "changed": changed,
        })

    lines = ["# 决策矩阵分析报告\n"]
    lines.append(f"方案数: {len(options)} | 标准数: {len(criteria)} | 权重总和: {total_weight}%\n")

    lines.append("## 评分矩阵\n")
    headers = ["标准", "权重"] + options
    table_rows = []
    for crit in criteria:
        row = [crit, f"{weights[crit]}%"]
        for opt in options:
            row.append(f"{data.get((opt, crit), 0):.0f}")
        table_rows.append(row)
    total_row = ["**总分**", ""]
    for opt in options:
        total_row.append(f"**{fmt_num(totals[opt])}**")
    table_rows.append(total_row)
    lines.append(md_table(headers, table_rows))

    lines.append("## 排名\n")
    for i, opt in enumerate(ranked, 1):
        marker = " ← 推荐" if i == 1 else ""
        lines.append(f"{i}. **{opt}** — {fmt_num(totals[opt])} 分{marker}")
    lines.append("")

    lines.append("## 敏感性分析\n")
    sens_headers = ["标准", "原权重", "权重降低后胜者", "结论变化?"]
    sens_rows = []
    for s in sensitivity:
        sens_rows.append([
            s["criterion"], f"{s['orig_weight']}%",
            s["winner_if_reduced"], "是 ⚠️" if s["changed"] else "否"
        ])
    lines.append(md_table(sens_headers, sens_rows))

    if len(ranked) >= 2:
        gap = totals[ranked[0]] - totals[ranked[1]]
        lines.append(f"\n第一名与第二名分差: **{fmt_num(gap)}**")
        if gap < 0.3:
            lines.append("⚠️ 分差 < 0.3，两方案势均力敌，建议做进一步评估。")

    if args.json:
        result = {
            "options": {opt: {"total": totals[opt], "details": details[opt]} for opt in options},
            "ranking": [{"rank": i + 1, "option": opt, "score": totals[opt]} for i, opt in enumerate(ranked)],
            "sensitivity": sensitivity,
        }
        write_output(json.dumps(result, ensure_ascii=False, indent=2), args.output)
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
    trows = [[i + 1, it["name"], it["impact"], it["confidence"], it["ease"], fmt_num(it["score"], 0)] for i, it in enumerate(items)]
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
