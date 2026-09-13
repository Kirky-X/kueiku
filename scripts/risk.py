"""Risk assessment methodologies — Risk Matrix / FMEA / Pareto"""

import json
import sys

from utils import read_csv, write_output, md_table, fmt_num, pct, fnum, inum

# ───────────────────────── Risk Matrix ─────────────────────────

RISK_HELP = """
Risk Matrix: Probability × Impact quick risk assessment and prioritization

CSV Format:
  name,probability,impact,category

  name        : Risk description
  probability : Probability (1-5)
  impact      : Impact (1-5)
  category    : Risk category (optional, for grouping)

Example:
  name,probability,impact,category
  Server Outage,3,5,Technical
  Key Personnel Departure,2,4,Personnel
  Frequent Requirement Changes,4,3,Requirements
"""


def cmd_risk(args):
    rows = read_csv(args.input)
    required = {"name", "probability", "impact"}
    if not required.issubset(rows[0].keys()):
        missing = required - set(rows[0].keys())
        print(f"CSV missing columns: {missing}", file=sys.stderr)
        sys.exit(1)

    risks = []
    for row_no, r in enumerate(rows, 2):
        p = inum(r["probability"], "probability", row_no)
        i = inum(r["impact"], "impact", row_no)
        risk_value = p * i
        if risk_value >= 15:
            zone, zone_en, action = "Red", "CRITICAL", "Act immediately"
        elif risk_value >= 8:
            zone, zone_en, action = "Orange", "HIGH", "Proactive mitigation"
        elif risk_value >= 4:
            zone, zone_en, action = "Yellow", "MEDIUM", "Continuous monitoring"
        else:
            zone, zone_en, action = "Green", "LOW", "Accept risk"
        risks.append({
            "name": r["name"], "probability": p, "impact": i,
            "risk_value": risk_value, "zone": zone, "zone_en": zone_en,
            "action": action, "category": r.get("category", ""),
        })

    risks.sort(key=lambda x: x["risk_value"], reverse=True)

    zone_counts = {"Red": 0, "Orange": 0, "Yellow": 0, "Green": 0}
    for r in risks:
        zone_counts[r["zone"]] += 1

    lines = ["# Risk Assessment Report\n"]
    lines.append(f"Total risks identified: {len(risks)}\n")
    lines.append("## Risk Distribution\n")
    lines.append(f"- 🔴 Red (extreme 15-25): {zone_counts['Red']} items")
    lines.append(f"- 🟠 Orange (high 8-14): {zone_counts['Orange']} items")
    lines.append(f"- 🟡 Yellow (medium 4-7): {zone_counts['Yellow']} items")
    lines.append(f"- 🟢 Green (low 1-3): {zone_counts['Green']} items\n")

    lines.append("## Risk Register (sorted by risk value)\n")
    headers = ["Rank", "Risk", "Probability", "Impact", "Risk Value", "Zone", "Response Strategy"]
    table_rows = []
    for idx, r in enumerate(risks, 1):
        table_rows.append([
            idx, r["name"], r["probability"], r["impact"],
            r["risk_value"], r["zone"], r["action"]
        ])
    lines.append(md_table(headers, table_rows))

    lines.append("## Risk Matrix\n")
    grid = {}
    for r in risks:
        grid[(r["probability"], r["impact"])] = r["name"][:8]
    lines.append("```\nImpact →  1    2    3    4    5")
    lines.append("Probability ↓")
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
        lines.append("## Risks Requiring Immediate Attention\n")
        for r in critical:
            lines.append(f"- **{r['name']}** (RiskValue {r['risk_value']}, {r['zone']}) → {r['action']}")

    if args.json:
        write_output(json.dumps(risks, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── FMEA ─────────────────────────

FMEA_HELP = """
FMEA Failure Mode and Effects Analysis: RPN = Severity(S) × Occurrence(O) × Detection(D)

CSV Format:
  name,severity,occurrence,detection,category

  name      : Failure mode description
  severity  : Severity (1-10)
  occurrence: Occurrence (1-10)
  detection : Detection (1-10, 1=certain detection, 10=undetectable)
  category  : Category (optional)

Example:
  name,severity,occurrence,detection,category
  Power Overload,8,4,3,Hardware
  Data Loss,9,3,5,Software
"""


def cmd_fmea(args):
    rows = read_csv(args.input)
    required = {"name", "severity", "occurrence", "detection"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV missing columns: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    items = []
    for row_no, r in enumerate(rows, 2):
        s = inum(r["severity"], "severity", row_no)
        o = inum(r["occurrence"], "occurrence", row_no)
        d = inum(r["detection"], "detection", row_no)
        rpn = s * o * d
        if rpn >= 200:
            zone, action = "Critical", "Immediate corrective action required"
        elif rpn >= 100:
            zone, action = "High", "Develop mitigation plan ASAP"
        elif rpn >= 50:
            zone, action = "Medium", "Include in monitoring and plan improvement"
        else:
            zone, action = "Low", "Routine monitoring"
        items.append({"name": r["name"], "s": s, "o": o, "d": d, "rpn": rpn,
                       "zone": zone, "action": action, "category": r.get("category", "")})

    items.sort(key=lambda x: x["rpn"], reverse=True)

    lines = ["# FMEA Failure Mode Analysis Report\n"]
    lines.append(f"Number of failure modes: {len(items)}\n")
    lines.append("## Risk Priority Number Ranking\n")
    headers = ["Rank", "Failure Mode", "S", "O", "D", "RPN", "Risk Level", "Response Strategy"]
    trows = [[i + 1, it["name"], it["s"], it["o"], it["d"], it["rpn"], it["zone"], it["action"]] for i, it in enumerate(items)]
    lines.append(md_table(headers, trows))

    high = [it for it in items if it["rpn"] >= 100]
    if high:
        lines.append("## Failure Modes Requiring Priority Action\n")
        for it in high:
            lines.append(f"- **{it['name']}** (RPN={it['rpn']}, {it['zone']}) → {it['action']}")

    if args.json:
        write_output(json.dumps(items, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── Pareto Analysis ─────────────────────────

PARETO_HELP = """
Pareto Analysis: Identify the vital few (20% of causes produce 80% of impact)

CSV Format:
  name,value

  name  : Item name
  value : Impact value (numeric)

Example:
  name,value
  Payment Failure,420
  Login Error,300
  Order Sync Issue,180
  Refund Query,120
  Address Change,90
  Coupon Issue,60
  Other,30
"""


def cmd_pareto(args):
    rows = read_csv(args.input)
    required = {"name", "value"}
    if not required.issubset(rows[0].keys()):
        missing = required - set(rows[0].keys())
        print(f"CSV missing columns: {missing}", file=sys.stderr)
        sys.exit(1)

    items = []
    skipped = 0
    for row_no, r in enumerate(rows, 2):
        v = fnum(r["value"], "value", row_no)
        if v <= 0:
            skipped += 1
            continue
        items.append({"name": r["name"], "value": v})

    items.sort(key=lambda x: x["value"], reverse=True)
    total = sum(i["value"] for i in items)
    if total == 0:
        print("All values are 0, cannot analyze", file=sys.stderr)
        sys.exit(1)

    cumulative = 0
    for item in items:
        pct_val = item["value"] / total * 100
        cumulative += pct_val
        item["pct"] = pct_val
        item["cumulative"] = cumulative
        item["classification"] = "Vital Few" if cumulative <= 80 else ("Boundary" if cumulative - pct_val < 80 else "Trivial Many")

    vital = [i for i in items if i["classification"] == "Vital Few" or i["classification"] == "Boundary"]
    trivial = [i for i in items if i["classification"] == "Trivial Many"]

    lines = ["# Pareto Analysis Report\n"]
    if skipped:
        lines.append(f"⚠️ Skipped {skipped} input row(s) with value ≤ 0 (Pareto analysis requires positive values).\n")
    lines.append(f"Items analyzed: {len(items)} | Total value: {fmt_num(total)}\n")

    lines.append("## Sorted Results\n")
    headers = ["Rank", "Item", "Impact Value", "Percentage", "Cumulative %", "Classification"]
    table_rows = []
    for idx, item in enumerate(items, 1):
        marker = " ← 80% boundary" if (item["cumulative"] >= 80 and (item["cumulative"] - item["pct"]) < 80) else ""
        table_rows.append([
            idx, item["name"], fmt_num(item["value"]),
            pct(item["pct"]), pct(item["cumulative"]),
            item["classification"] + marker
        ])
    lines.append(md_table(headers, table_rows))

    vital_pct = sum(i["pct"] for i in vital)
    lines.append(f"\n## Vital Few ({len(vital)} items, contributing {pct(vital_pct)} impact)\n")
    for i, item in enumerate(vital, 1):
        lines.append(f"{i}. **{item['name']}** — ImpactValue: {fmt_num(item['value'])} ({pct(item['pct'])})")

    if trivial:
        trivial_pct = sum(i["pct"] for i in trivial)
        lines.append(f"\n## Trivial Many ({len(trivial)} items, contributing {pct(trivial_pct)} impact)\n")
        lines.append("Strategy: Reduce investment / Standardize process / Defer / Remove")

    lines.append("\n## Cumulative Distribution\n")
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
