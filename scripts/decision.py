"""Decision & prioritization methodologies — RICE / Decision Matrix / ICE"""

import json
import sys

from utils import read_csv, write_output, md_table, fmt_num

# ───────────────────────── RICE Scoring ─────────────────────────

RICE_HELP = """
RICE priority scoring: Score = (Reach × Impact × Confidence) ÷ Effort

CSV Format (headers must match):
  name,reach,impact,confidence,effort

  name       : Requirement/feature name
  reach      : Number of users reached (users/month)
  impact     : Impact (0.25 / 0.5 / 1 / 2 / 3)
  confidence : Confidence percentage (100 / 80 / 50)
  effort     : Effort (person-months)

Example:
  name,reach,impact,confidence,effort
  Feature A,50000,2,80,2
  Feature B,20000,3,50,1
"""


def cmd_rice(args):
    rows = read_csv(args.input)
    required = {"name", "reach", "impact", "confidence", "effort"}
    if not required.issubset(rows[0].keys()):
        missing = required - set(rows[0].keys())
        print(f"CSV missing columns: {missing}", file=sys.stderr)
        sys.exit(1)

    scored = []
    for r in rows:
        reach = float(r["reach"])
        impact = float(r["impact"])
        conf = float(r["confidence"]) / 100.0
        effort = float(r["effort"])
        if effort <= 0:
            print(f"Warning: '{r['name']}' has Effort={effort}, skipped", file=sys.stderr)
            continue
        score = (reach * impact * conf) / effort
        scored.append({
            "name": r["name"], "reach": reach, "impact": impact,
            "confidence": float(r["confidence"]), "effort": effort, "score": score,
        })

    scored.sort(key=lambda x: x["score"], reverse=True)

    lines = ["# RICE Priority Scoring Report\n"]
    lines.append(f"Items evaluated: {len(scored)}\n")
    lines.append("## Sorted Results\n")
    headers = ["Rank", "Name", "Reach", "Impact", "Confidence", "Effort", "RICE Score"]
    table_rows = []
    for i, s in enumerate(scored, 1):
        table_rows.append([
            i, s["name"], fmt_num(s["reach"], 0), s["impact"],
            f"{s['confidence']:.0f}%", s["effort"], fmt_num(s["score"], 0)
        ])
    lines.append(md_table(headers, table_rows))

    if len(scored) >= 3:
        top_third = max(1, len(scored) // 3)
        lines.append("## Tier Recommendations\n")
        lines.append(f"- **Must do (Top {top_third})**: {', '.join(s['name'] for s in scored[:top_third])}")
        mid_end = max(top_third * 2, len(scored) - 1)
        lines.append(f"- **Target**: {', '.join(s['name'] for s in scored[top_third:mid_end])}")
        lines.append(f"- **Backlog**: {', '.join(s['name'] for s in scored[mid_end:])}")

    if args.json:
        write_output(json.dumps(scored, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── Decision Matrix ─────────────────────────

DMATRIX_HELP = """
Decision Matrix (Pugh Matrix): Multi-option × Multi-criteria weighted scoring

CSV Format (long table, one option-criterion pair per row):
  option,criterion,weight,score

  option    : Option name
  criterion : Evaluation criterion
  weight    : Weight (percentage, e.g. 30 means 30%)
  score     : Score (1-5 or 1-10)

Example:
  option,criterion,weight,score
  Node.js,Dev Efficiency,30,5
  Node.js,Performance,25,3
  Go,Dev Efficiency,30,4
  Go,Performance,25,5
"""


def cmd_dmatrix(args):
    rows = read_csv(args.input)
    required = {"option", "criterion", "weight", "score"}
    if not required.issubset(rows[0].keys()):
        missing = required - set(rows[0].keys())
        print(f"CSV missing columns: {missing}", file=sys.stderr)
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
        print(f"Warning: Total weight = {total_weight}% (should be 100%)", file=sys.stderr)

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

    lines = ["# Decision Matrix Analysis Report\n"]
    lines.append(f"Options: {len(options)} | Criteria: {len(criteria)} | Total weight: {total_weight}%\n")

    lines.append("## Scoring Matrix\n")
    headers = ["Criterion", "Weight"] + options
    table_rows = []
    for crit in criteria:
        row = [crit, f"{weights[crit]}%"]
        for opt in options:
            row.append(f"{data.get((opt, crit), 0):.0f}")
        table_rows.append(row)
    total_row = ["**Total**", ""]
    for opt in options:
        total_row.append(f"**{fmt_num(totals[opt])}**")
    table_rows.append(total_row)
    lines.append(md_table(headers, table_rows))

    lines.append("## Ranking\n")
    for i, opt in enumerate(ranked, 1):
        marker = " ← Recommended" if i == 1 else ""
        lines.append(f"{i}. **{opt}** — {fmt_num(totals[opt])} pts{marker}")
    lines.append("")

    lines.append("## Sensitivity Analysis\n")
    sens_headers = ["Criterion", "Original Weight", "Winner if Reduced", "Change?"]
    sens_rows = []
    for s in sensitivity:
        sens_rows.append([
            s["criterion"], f"{s['orig_weight']}%",
            s["winner_if_reduced"], "Yes ⚠️" if s["changed"] else "No"
        ])
    lines.append(md_table(sens_headers, sens_rows))

    if len(ranked) >= 2:
        gap = totals[ranked[0]] - totals[ranked[1]]
        lines.append(f"\nGap between 1st and 2nd: **{fmt_num(gap)}**")
        if gap < 0.3:
            lines.append("⚠️ Gap < 0.3, options are closely matched, further evaluation recommended.")

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
ICE scoring: Score = Impact × Confidence × Ease

CSV Format:
  name,impact,confidence,ease

  name       : Idea/feature name
  impact     : Impact (1-10)
  confidence : Confidence (1-10)
  ease       : Ease (1-10, higher = easier)

Example:
  name,impact,confidence,ease
  User Referral,8,7,9
  Paywall Optimization,6,5,4
"""


def cmd_ice(args):
    rows = read_csv(args.input)
    required = {"name", "impact", "confidence", "ease"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV missing columns: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    items = []
    for r in rows:
        i, c, e = float(r["impact"]), float(r["confidence"]), float(r["ease"])
        score = i * c * e
        items.append({"name": r["name"], "impact": i, "confidence": c, "ease": e, "score": score})

    items.sort(key=lambda x: x["score"], reverse=True)

    lines = ["# ICE Scoring Report\n"]
    lines.append(f"Items evaluated: {len(items)}\n")
    lines.append("## Sorted Results\n")
    headers = ["Rank", "Name", "Impact", "Confidence", "Ease", "ICE Score"]
    trows = [[i + 1, it["name"], it["impact"], it["confidence"], it["ease"], fmt_num(it["score"], 0)] for i, it in enumerate(items)]
    lines.append(md_table(headers, trows))

    if len(items) >= 3:
        top = max(1, len(items) // 3)
        lines.append("## Tier Recommendations\n")
        lines.append(f"- **Must do (Top {top})**: {', '.join(it['name'] for it in items[:top])}")
        lines.append(f"- **Candidates**: {', '.join(it['name'] for it in items[top:])}")

    if args.json:
        write_output(json.dumps(items, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)
