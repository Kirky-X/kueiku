"""Strategy matrices methodologies — BCG Matrix / GE-McKinsey / Opportunity Score"""

import json
import sys

from utils import read_csv, write_output, md_table, fmt_num, pct, fnum

# ───────────────────────── Opportunity Score ─────────────────────────

OPPSCORE_HELP = """
Opportunity Scoring: Opportunity = Importance × (1 - Satisfaction)

CSV Format:
  name,importance,satisfaction

  name         : Requirement/feature name
  importance   : Importance (1-5)
  satisfaction : Current satisfaction (1-5)

Example:
  name,importance,satisfaction
  Fast Response,5,2
  UI Aesthetics,3,4
"""


def cmd_oppscore(args):
    rows = read_csv(args.input)
    required = {"name", "importance", "satisfaction"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV missing columns: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    items = []
    for row_no, r in enumerate(rows, 2):
        imp = fnum(r["importance"], "importance", row_no)
        sat = fnum(r["satisfaction"], "satisfaction", row_no)
        imp_n = (imp - 1) / 4
        sat_n = (sat - 1) / 4
        opp = imp_n * (1 - sat_n)
        items.append({"name": r["name"], "importance": imp, "satisfaction": sat,
                       "imp_norm": imp_n, "sat_norm": sat_n, "opportunity": opp})

    items.sort(key=lambda x: x["opportunity"], reverse=True)

    lines = ["# Opportunity Scoring Report\n"]
    lines.append(f"Requirements evaluated: {len(items)}\n")
    lines.append("## Sorted Results\n")
    headers = ["Rank", "Requirement", "Importance", "Satisfaction", "Opportunity Score"]
    trows = [[i + 1, it["name"], it["importance"], it["satisfaction"], f"{it['opportunity']:.3f}"] for i, it in enumerate(items)]
    lines.append(md_table(headers, trows))

    opportunities = [it for it in items if it["opportunity"] >= 0.5]
    satisfied = [it for it in items if it["satisfaction"] >= 4 and it["importance"] >= 4]
    low_priority = [it for it in items if it["importance"] <= 2]

    lines.append("## Classification Recommendations\n")
    if opportunities:
        lines.append(f"### Blue Ocean Opportunities ({len(opportunities)} items)\n")
        for it in opportunities:
            lines.append(f"- **{it['name']}** — Importance {it['importance']}, Satisfaction {it['satisfaction']}, Opportunity {it['opportunity']:.3f}")
    if satisfied:
        lines.append(f"\n### Satisfied High-Importance Requirements ({len(satisfied)} items)\n")
        for it in satisfied:
            lines.append(f"- {it['name']} — Maintain current state")
    if low_priority:
        lines.append(f"\n### Low Priority ({len(low_priority)} items)\n")
        for it in low_priority:
            lines.append(f"- {it['name']} — Not worth investing")

    if args.json:
        write_output(json.dumps(items, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── BCG Matrix ─────────────────────────

BCG_HELP = """
BCG Matrix: Market growth rate × Relative market share → 4-quadrant classification

CSV Format:
  product,market_growth,relative_share,revenue

  product        : Product/business name
  market_growth  : Market growth rate (decimal, e.g. 0.15 for 15%)
  relative_share : Relative market share (decimal, e.g. 1.5 means market leader)
  revenue        : Revenue (optional, for bubble size)

Example:
  product,market_growth,relative_share,revenue
  ProductA,0.25,1.8,5000
  ProductB,0.05,2.5,8000
  ProductC,0.30,0.6,2000
  ProductD,0.02,0.4,1000
"""


def cmd_bcg(args):
    rows = read_csv(args.input)
    required = {"product", "market_growth", "relative_share"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV missing columns: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    growth_threshold = 0.10
    share_threshold = 1.0

    items = []
    for row_no, r in enumerate(rows, 2):
        g = fnum(r["market_growth"], "market_growth", row_no)
        s = fnum(r["relative_share"], "relative_share", row_no)
        rev = fnum(r.get("revenue", 0), "revenue", row_no)
        if g >= growth_threshold and s >= share_threshold:
            quadrant = "⭐ Star"
        elif g < growth_threshold and s >= share_threshold:
            quadrant = "💰 Cash Cow"
        elif g >= growth_threshold and s < share_threshold:
            quadrant = "❓ Question Mark"
        else:
            quadrant = "🐕 Dog"
        items.append({"product": r["product"], "growth": g, "share": s,
                       "revenue": rev, "quadrant": quadrant})

    quads = {}
    for it in items:
        q = it["quadrant"]
        if q not in quads:
            quads[q] = []
        quads[q].append(it)

    lines = ["# BCG Matrix Analysis Report\n"]
    lines.append(f"Products/Businesses: {len(items)} | Growth threshold: {pct(growth_threshold * 100)} | Share threshold: {share_threshold}\n")

    lines.append("## Classification Results\n")
    headers = ["Product", "Market Growth", "Relative Share", "Revenue", "Quadrant"]
    trows = [[it["product"], pct(it["growth"] * 100), f"{it['share']:.2f}",
              fmt_num(it["revenue"], 0) if it["revenue"] else "-", it["quadrant"]] for it in items]
    lines.append(md_table(headers, trows))

    lines.append("## Strategic Recommendations\n")
    for q_name, members in quads.items():
        lines.append(f"### {q_name} ({len(members)} items)\n")
        for m in members:
            lines.append(f"- **{m['product']}** — Growth {pct(m['growth'] * 100)}, Share {m['share']:.2f}")
        if "Star" in q_name:
            lines.append("→ Strategy: Increase investment, maintain growth\n")
        elif "Cash Cow" in q_name:
            lines.append("→ Strategy: Harvest profits, reduce investment\n")
        elif "Question" in q_name:
            lines.append("→ Strategy: Selective investment, or divest\n")
        else:
            lines.append("→ Strategy: Consider exit or restructuring\n")

    if args.json:
        write_output(json.dumps(items, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── GE-McKinsey Matrix ─────────────────────────

GEMCKINSEY_HELP = """
GE-McKinsey Matrix: Industry Attractiveness × Competitive Strength → 9-cell classification

CSV Format:
  business,attractiveness,strength,revenue

  business       : Business/product name
  attractiveness : Industry attractiveness score (1-5)
  strength       : Competitive strength score (1-5)
  revenue        : Revenue (optional)

Example:
  business,attractiveness,strength,revenue
  BusinessA,4.5,4.0,5000
  BusinessB,2.0,3.5,3000
  BusinessC,3.8,2.0,2000
"""


def cmd_gemckinsey(args):
    rows = read_csv(args.input)
    required = {"business", "attractiveness", "strength"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV missing columns: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    items = []
    for row_no, r in enumerate(rows, 2):
        a = fnum(r["attractiveness"], "attractiveness", row_no)
        s = fnum(r["strength"], "strength", row_no)
        rev = fnum(r.get("revenue", 0), "revenue", row_no)
        if a >= 3.67 and s >= 3.67:
            cell = "Invest/Grow"
        elif a >= 3.67 and s >= 2.33:
            cell = "Selective Investment"
        elif a >= 3.67:
            cell = "Selective Investment"
        elif a >= 2.33 and s >= 3.67:
            cell = "Selective Investment"
        elif a >= 2.33 and s >= 2.33:
            cell = "Selective Maintain"
        elif a >= 2.33:
            cell = "Harvest"
        elif s >= 3.67:
            cell = "Selective Maintain"
        elif s >= 2.33:
            cell = "Harvest"
        else:
            cell = "Exit/Divest"
        items.append({"business": r["business"], "attractiveness": a,
                       "strength": s, "revenue": rev, "cell": cell})

    cells = {}
    for it in items:
        c = it["cell"]
        if c not in cells:
            cells[c] = []
        cells[c].append(it)

    lines = ["# GE-McKinsey Matrix Analysis Report\n"]
    lines.append(f"Businesses: {len(items)}\n")

    lines.append("## Classification Results\n")
    headers = ["Business", "Industry Attractiveness", "Competitive Strength", "Revenue", "Strategy Zone"]
    trows = [[it["business"], f"{it['attractiveness']:.1f}", f"{it['strength']:.1f}",
              fmt_num(it["revenue"], 0) if it["revenue"] else "-", it["cell"]] for it in items]
    lines.append(md_table(headers, trows))

    lines.append("## Matrix View\n")
    lines.append("```")
    lines.append("              Competitive Strength")
    lines.append("              Strong(>3.67)  Medium(2.33-3.67)  Weak(<2.33)")
    for a_label, a_range in [("High(>3.67)", (3.67, 5.01)), ("Medium(2.33-3.67)", (2.33, 3.67)), ("Low(<2.33)", (0, 2.33))]:
        lines.append(f"Attractiveness {a_label}")
        for s_label, s_range in [("Strong", (3.67, 5.01)), ("Medium", (2.33, 3.67)), ("Weak", (0, 2.33))]:
            in_cell = [it for it in items if a_range[0] <= it["attractiveness"] < a_range[1]
                        and s_range[0] <= it["strength"] < s_range[1]]
            names = ", ".join(it["business"][:6] for it in in_cell) if in_cell else "·"
            lines.append(f"              {names:<20}")
    lines.append("```\n")

    lines.append("## Strategic Recommendations\n")
    for cell_name, members in cells.items():
        lines.append(f"### {cell_name} ({len(members)} items)\n")
        for m in members:
            lines.append(f"- **{m['business']}** — Attractiveness {m['attractiveness']:.1f}, Strength {m['strength']:.1f}")
        if cell_name == "Invest/Grow":
            lines.append("→ Aggressive investment, expand market share\n")
        elif cell_name == "Selective Investment":
            lines.append("→ Targeted investment, focus on strengths\n")
        elif cell_name == "Selective Maintain":
            lines.append("→ Maintain current position, control costs\n")
        elif cell_name == "Harvest":
            lines.append("→ Maximize cash flow, reduce new investment\n")
        else:
            lines.append("→ Consider exit or divestiture\n")

    if args.json:
        write_output(json.dumps(items, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)
