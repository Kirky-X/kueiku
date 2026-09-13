"""Data analysis methodologies — A/B Test / RFM / Cohort"""

import json
import math
import sys

from utils import (read_csv, write_output, md_table, fmt_num, pct, z_test,
                    quintile_score, fnum, inum)

# ───────────────────────── A/B Test Analysis ─────────────────────────

ABTEST_HELP = """
A/B Test Analysis: Statistical significance testing + SRM detection + Decision matrix

CSV Format:
  variant,users,conversions

  variant     : Variant name (control / treatment)
  users       : Number of users
  conversions : Number of conversions

Two or more variants supported. The first two rows are treated as control and
primary treatment; any additional variants are summarized and compared against
the control in an 'Additional Variants' section (not part of the primary decision).

Example:
  variant,users,conversions
  control,10000,500
  treatment,10200,550
"""


def cmd_abtest(args):
    rows = read_csv(args.input)
    required = {"variant", "users", "conversions"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV missing columns: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    variants = {}
    for row_no, r in enumerate(rows, 2):
        u = inum(r["users"], "users", row_no)
        c = inum(r["conversions"], "conversions", row_no)
        variants[r["variant"]] = {"users": u, "conversions": c, "rate": c / u if u > 0 else 0}

    if len(variants) < 2:
        print("At least 2 variants required", file=sys.stderr)
        sys.exit(1)

    names = list(variants.keys())
    ctrl_name = names[0]
    treat_name = names[1]
    extra_names = names[2:]  # 3rd+ variants: summarized below, never silently dropped
    ctrl = variants[ctrl_name]
    treat = variants[treat_name]

    # SRM detection: chi-square goodness-of-fit vs 50/50 split,
    # critical value chi2 > 3.841 (alpha = 0.05, df = 1)
    total_users = ctrl["users"] + treat["users"]
    expected_ctrl = total_users * 0.5
    srm_chi2 = (ctrl["users"] - expected_ctrl) ** 2 / expected_ctrl + (treat["users"] - expected_ctrl) ** 2 / expected_ctrl
    srm_detected = srm_chi2 > 3.841

    # z-test
    z, p_val = z_test(ctrl["rate"], ctrl["users"], treat["rate"], treat["users"])
    significant = p_val < 0.05
    lift = (treat["rate"] - ctrl["rate"]) / ctrl["rate"] * 100 if ctrl["rate"] > 0 else 0

    # MDE for 80% power: (z_alpha + z_beta) * SE, z_alpha = 1.96, z_beta = 0.84
    alpha = 0.05
    z_alpha = 1.96
    z_beta = 0.84
    p_pool = (ctrl["conversions"] + treat["conversions"]) / (ctrl["users"] + treat["users"])
    mde = (z_alpha + z_beta) * math.sqrt(2 * p_pool * (1 - p_pool) / min(ctrl["users"], treat["users"]))

    if srm_detected:
        decision = "⚠️ INVALID — SRM detected sample ratio mismatch, results unreliable"
    elif significant and lift > 0:
        decision = "✅ Ship — Significant positive result, recommend launch"
    elif significant and lift < 0:
        decision = "❌ Stop — Significant negative result, stop experiment"
    elif not significant:
        decision = "🔍 Investigate — Not significant, segment analysis needed"
    else:
        decision = "🤷 Indeterminate"

    lines = ["# A/B Test Analysis Report\n"]
    lines.append(f"Control: {ctrl_name} | Treatment: {treat_name}\n")
    if extra_names:
        lines.append(f"⚠️ **WARNING**: {len(variants)} variants provided. Only the first two "
                     f"('{ctrl_name}' vs '{treat_name}') are analyzed in the primary decision; the other "
                     f"{len(extra_names)} variant(s) ({', '.join(extra_names)}) are summarized in "
                     f"'Additional Variants' below and are **not** part of the primary decision.\n")

    lines.append("## Basic Data\n")
    headers = ["Variant", "Users", "Conversions", "Conversion Rate"]
    trows = [[ctrl_name, fmt_num(ctrl["users"], 0), ctrl["conversions"], pct(ctrl["rate"] * 100)],
             [treat_name, fmt_num(treat["users"], 0), treat["conversions"], pct(treat["rate"] * 100)]]
    lines.append(md_table(headers, trows))

    lines.append(f"**Lift**: {lift:+.2f}%\n")

    lines.append("## Statistical Test\n")
    lines.append(f"- z Statistic: {z:.4f}")
    lines.append(f"- p Value: {p_val:.6f}")
    lines.append(f"- Significance level α: {alpha}")
    lines.append(f"- Conclusion: {'Significant (p < 0.05)' if significant else 'Not significant (p ≥ 0.05)'}")
    lines.append(f"- MDE (Minimum Detectable Effect): {pct(mde * 100)}\n")

    lines.append("## SRM Check\n")
    lines.append(f"- Sample ratio difference: {abs(ctrl['users'] - treat['users']) / total_users * 100:.2f}%")
    lines.append(f"- SRM Status: {'⚠️ Mismatch detected' if srm_detected else '✅ Normal'}")
    lines.append(f"- χ² = {srm_chi2:.4f}\n")

    lines.append(f"## Decision: {decision}")

    if extra_names:
        lines.append("\n## Additional Variants (vs control, informational)\n")
        a_headers = ["Variant", "Users", "Conversions", "Conversion Rate", "Lift vs Control", "z", "p Value", "Significant?"]
        a_trows = []
        for name in extra_names:
            v = variants[name]
            vz, vp = z_test(ctrl["rate"], ctrl["users"], v["rate"], v["users"])
            v_lift = (v["rate"] - ctrl["rate"]) / ctrl["rate"] * 100 if ctrl["rate"] > 0 else 0
            a_trows.append([name, fmt_num(v["users"], 0), v["conversions"], pct(v["rate"] * 100),
                            f"{v_lift:+.2f}%", f"{vz:.4f}", f"{vp:.6f}",
                            "Yes" if vp < 0.05 else "No"])
        lines.append(md_table(a_headers, a_trows))
        lines.append("\nNote: for a decision across 3+ variants, control for multiplicity "
                     "(e.g. Bonferroni: use α = 0.05 / number of comparisons) or run a chi-square test first.")

    if args.json:
        result = {"control": ctrl, "treatment": treat, "z": z, "p_value": p_val,
                   "significant": significant, "lift": lift, "srm_detected": srm_detected,
                   "srm_chi2": srm_chi2, "mde": mde, "decision": decision}
        if extra_names:
            result["ignored_variants_warning"] = (f"Only the first two variants were compared; "
                                                   f"{len(extra_names)} additional variant(s) summarized separately.")
            result["additional_variants"] = {name: variants[name] for name in extra_names}
        write_output(json.dumps(result, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── RFM Model ─────────────────────────

RFM_HELP = """
RFM User Segmentation: Recency × Frequency × Monetary → 8 segments

CSV Format:
  customer_id,recency,frequency,monetary

  customer_id : Customer identifier
  recency     : Days since last purchase
  frequency   : Number of purchases
  monetary    : Total spend

Example:
  customer_id,recency,frequency,monetary
  C001,5,20,5000
  C002,90,3,300
  C003,15,10,2000
"""


def cmd_rfm(args):
    rows = read_csv(args.input)
    required = {"customer_id", "recency", "frequency", "monetary"}
    if not required.issubset(rows[0].keys()):
        print(f"CSV missing columns: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    data = []
    for row_no, r in enumerate(rows, 2):
        data.append({"id": r["customer_id"],
                      "recency": fnum(r["recency"], "recency", row_no),
                      "frequency": fnum(r["frequency"], "frequency", row_no),
                      "monetary": fnum(r["monetary"], "monetary", row_no)})

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
            d["segment"] = "Champions"
        elif not r_hi and f_hi and m_hi:
            d["segment"] = "Loyal Customers"
        elif r_hi and not f_hi and m_hi:
            d["segment"] = "Potential Loyalists"
        elif not r_hi and not f_hi and m_hi:
            d["segment"] = "At Risk"
        elif r_hi and f_hi and not m_hi:
            d["segment"] = "Promising"
        elif not r_hi and f_hi and not m_hi:
            d["segment"] = "Need Attention"
        elif r_hi and not f_hi and not m_hi:
            d["segment"] = "New Customers"
        else:
            d["segment"] = "Lost"

    segments = {}
    for d in data:
        seg = d["segment"]
        if seg not in segments:
            segments[seg] = []
        segments[seg].append(d)

    lines = ["# RFM User Segmentation Report\n"]
    lines.append(f"Total customers: {len(data)}\n")

    lines.append("## Segment Statistics\n")
    headers = ["Segment", "Count", "Percentage", "Avg R", "Avg F", "Avg M"]
    seg_order = ["Champions", "Loyal Customers", "Potential Loyalists", "At Risk",
                  "Promising", "Need Attention", "New Customers", "Lost"]
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

    lines.append("## Customer Details (top 20)\n")
    headers2 = ["Customer", "R", "F", "M", "Recency", "Frequency", "Monetary", "Segment"]
    trows2 = [[d["id"], d["r"], d["f"], d["m"], f"{d['recency']:.0f}",
               f"{d['frequency']:.0f}", fmt_num(d["monetary"], 0), d["segment"]] for d in data[:20]]
    lines.append(md_table(headers2, trows2))

    if args.json:
        write_output(json.dumps(data, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)


# ───────────────────────── Cohort Analysis ─────────────────────────

COHORT_HELP = """
Cohort retention analysis: Track retention rates by time group

CSV Format:
  cohort,period,active,initial

  cohort  : Cohort identifier (e.g. 2024-01, 2024-02)
  period  : Period (0=initial, 1=period 1, 2=period 2, ...)
  active  : Active users
  initial : Initial users

Example:
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
        print(f"CSV missing columns: {required - set(rows[0].keys())}", file=sys.stderr)
        sys.exit(1)

    cohorts = {}
    max_period = 0
    for row_no, r in enumerate(rows, 2):
        c = r["cohort"]
        p = inum(r["period"], "period", row_no)
        a = inum(r["active"], "active", row_no)
        ini = inum(r["initial"], "initial", row_no)
        if c not in cohorts:
            cohorts[c] = {}
        cohorts[c][p] = {"active": a, "initial": ini, "retention": a / ini if ini > 0 else 0}
        max_period = max(max_period, p)

    cohort_names = sorted(cohorts.keys())
    periods = list(range(max_period + 1))

    lines = ["# Cohort Retention Analysis Report\n"]
    lines.append(f"Cohorts: {len(cohort_names)} | Max period: {max_period}\n")

    lines.append("## Retention Rate Matrix\n")
    headers = ["Cohort", "Initial"] + [f"P{p}" for p in periods if p > 0]
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

    lines.append("## Average Retention Rate by Period\n")
    avg_headers = ["Period"] + [f"P{p}" for p in periods if p > 0]
    avg_row = ["Average"]
    for p in periods:
        if p == 0:
            continue
        vals = [cohorts[c][p]["retention"] * 100 for c in cohort_names if p in cohorts[c]]
        avg_row.append(pct(sum(vals) / len(vals)) if vals else "-")
    lines.append(md_table(avg_headers, [avg_row]))

    lines.append("## PMF Signal\n")
    for p in periods:
        if p == 0:
            continue
        vals = [cohorts[c][p]["retention"] * 100 for c in cohort_names if p in cohorts[c]]
        if vals:
            avg = sum(vals) / len(vals)
            trend = "stable" if avg > 30 else "low"
            lines.append(f"- P{p} Avg Retention: {pct(avg)} — {trend}")

    if args.json:
        result = {"cohorts": {c: {str(p): cohorts[c][p] for p in cohorts[c]} for c in cohort_names}}
        write_output(json.dumps(result, ensure_ascii=False, indent=2), args.output)
    else:
        write_output("\n".join(lines), args.output)
