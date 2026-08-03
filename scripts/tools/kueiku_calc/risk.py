"""风险评估方法论 — Risk Matrix / FMEA / Pareto"""

import json
import sys

from .utils import read_csv, write_output, md_table, fmt_num, pct

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
            zone, zone_en, action = "红色", "CRITICAL", "立即行动"
        elif risk_value >= 8:
            zone, zone_en, action = "橙色", "HIGH", "主动缓解"
        elif risk_value >= 4:
            zone, zone_en, action = "黄色", "MEDIUM", "持续监控"
        else:
            zone, zone_en, action = "绿色", "LOW", "接受风险"
        risks.append({
            "name": r["name"], "probability": p, "impact": i,
            "risk_value": risk_value, "zone": zone, "zone_en": zone_en,
            "action": action, "category": r.get("category", ""),
        })

    risks.sort(key=lambda x: x["risk_value"], reverse=True)

    zone_counts = {"红色": 0, "橙色": 0, "黄色": 0, "绿色": 0}
    for r in risks:
        zone_counts[r["zone"]] += 1

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

    critical = [r for r in risks if r["risk_value"] >= 8]
    if critical:
        lines.append("## 需立即关注的风险\n")
        for r in critical:
            lines.append(f"- **{r['name']}** (风险值 {r['risk_value']}, {r['zone']}) → {r['action']}")

    if args.json:
        write_output(json.dumps(risks, ensure_ascii=False, indent=2), args.output)
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
    trows = [[i + 1, it["name"], it["s"], it["o"], it["d"], it["rpn"], it["zone"], it["action"]] for i, it in enumerate(items)]
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

    cumulative = 0
    for item in items:
        pct_val = item["value"] / total * 100
        cumulative += pct_val
        item["pct"] = pct_val
        item["cumulative"] = cumulative
        item["classification"] = "关键少数" if cumulative <= 80 else ("临界" if cumulative - pct_val < 80 else "琐碎多数")

    vital = [i for i in items if i["classification"] == "关键少数" or i["classification"] == "临界"]
    trivial = [i for i in items if i["classification"] == "琐碎多数"]

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

    vital_pct = sum(i["pct"] for i in vital)
    lines.append(f"\n## 关键少数（{len(vital)} 项，贡献 {pct(vital_pct)} 影响）\n")
    for i, item in enumerate(vital, 1):
        lines.append(f"{i}. **{item['name']}** — 影响值: {fmt_num(item['value'])} ({pct(item['pct'])})")

    if trivial:
        trivial_pct = sum(i["pct"] for i in trivial)
        lines.append(f"\n## 琐碎多数（{len(trivial)} 项，贡献 {pct(trivial_pct)} 影响）\n")
        lines.append("处理策略: 降低投入 / 标准化处理 / 暂缓 / 删除")

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
