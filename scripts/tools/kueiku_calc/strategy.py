"""战略矩阵方法论 — BCG Matrix / GE-McKinsey / Opportunity Score"""

import json
import sys

from .utils import read_csv, write_output, md_table, fmt_num, pct

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
        imp_n = (imp - 1) / 4
        sat_n = (sat - 1) / 4
        opp = imp_n * (1 - sat_n)
        items.append({"name": r["name"], "importance": imp, "satisfaction": sat,
                       "imp_norm": imp_n, "sat_norm": sat_n, "opportunity": opp})

    items.sort(key=lambda x: x["opportunity"], reverse=True)

    lines = ["# 机会评分报告\n"]
    lines.append(f"评估需求数: {len(items)}\n")
    lines.append("## 排序结果\n")
    headers = ["排名", "需求", "重要度", "满意度", "机会分"]
    trows = [[i + 1, it["name"], it["importance"], it["satisfaction"], f"{it['opportunity']:.3f}"] for i, it in enumerate(items)]
    lines.append(md_table(headers, trows))

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

    growth_threshold = 0.10
    share_threshold = 1.0

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

    quads = {}
    for it in items:
        q = it["quadrant"]
        if q not in quads:
            quads[q] = []
        quads[q].append(it)

    lines = ["# BCG 矩阵分析报告\n"]
    lines.append(f"产品/业务数: {len(items)} | 增长阈值: {pct(growth_threshold * 100)} | 份额阈值: {share_threshold}\n")

    lines.append("## 分类结果\n")
    headers = ["产品", "市场增长", "相对份额", "收入", "象限"]
    trows = [[it["product"], pct(it["growth"] * 100), f"{it['share']:.2f}",
              fmt_num(it["revenue"], 0) if it["revenue"] else "-", it["quadrant"]] for it in items]
    lines.append(md_table(headers, trows))

    lines.append("## 战略建议\n")
    for q_name, members in quads.items():
        lines.append(f"### {q_name}（{len(members)} 项）\n")
        for m in members:
            lines.append(f"- **{m['product']}** — 增长 {pct(m['growth'] * 100)}, 份额 {m['share']:.2f}")
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
