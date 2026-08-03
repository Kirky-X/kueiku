"""CLI entry point — argparse subcommand registration and dispatch."""

import argparse
import sys

from decision import RICE_HELP, DMATRIX_HELP, ICE_HELP, cmd_rice, cmd_dmatrix, cmd_ice
from risk import RISK_HELP, FMEA_HELP, PARETO_HELP, cmd_risk, cmd_fmea, cmd_pareto
from financial import DUPONT_HELP, DCF_HELP, EVA_HELP, cmd_dupont, cmd_dcf, cmd_eva
from data import ABTEST_HELP, RFM_HELP, COHORT_HELP, cmd_abtest, cmd_rfm, cmd_cohort
from strategy import OPPSCORE_HELP, BCG_HELP, GEMCKINSEY_HELP, cmd_oppscore, cmd_bcg, cmd_gemckinsey
from quant import FACTOR_HELP, MOMENTUM_HELP, RISKPARITY_HELP, PERF_HELP
from quant import cmd_factor, cmd_momentum, cmd_riskparity, cmd_perf


def main():
    parser = argparse.ArgumentParser(
        prog="kueiku-calc",
        description="Kueiku Methodology calculation toolkit — 19 computation-heavy methodology automations",
    )
    subparsers = parser.add_subparsers(dest="command", help="subcommand")

    def add_common_args(p):
        p.add_argument("-i", "--input", required=True, help="CSV file path (- for stdin)")
        p.add_argument("-o", "--output", help="Output file path (default stdout)")
        p.add_argument("--json", action="store_true", help="Output in JSON format")

    # Decision & prioritization
    p = subparsers.add_parser("rice", help="RICE priority scoring", description=RICE_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("dmatrix", help="Decision Matrix (Pugh Matrix)", description=DMATRIX_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("ice", help="ICE scoring", description=ICE_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # Risk assessment
    p = subparsers.add_parser("risk", help="Risk Matrix", description=RISK_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("fmea", help="FMEA FMEA failure mode analysis", description=FMEA_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("pareto", help="Pareto Analysis", description=PARETO_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # Financial analysis
    p = subparsers.add_parser("dupont", help="DuPont Analysis", description=DUPONT_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("dcf", help="DCF valuation", description=DCF_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)
    p.add_argument("--rate", type=float, default=0.10, help="Discount rate (WACC), default 0.10")
    p.add_argument("--growth", type=float, default=0.03, help="Perpetual growth rate, default 0.03")
    p.add_argument("--shares", type=float, default=0, help="Shares outstanding (optional)")

    p = subparsers.add_parser("eva", help="Economic Value Added", description=EVA_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # Data analysis
    p = subparsers.add_parser("abtest", help="A/B Test significance analysis", description=ABTEST_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("rfm", help="RFM UserSegmentation", description=RFM_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("cohort", help="Cohort retention analysis", description=COHORT_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # Strategy matrices
    p = subparsers.add_parser("oppscore", help="Opportunity scoring", description=OPPSCORE_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("bcg", help="BCG Matrix", description=BCG_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("gemckinsey", help="GE-McKinsey Matrix", description=GEMCKINSEY_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # Quantitative investment
    p = subparsers.add_parser("factor", help="Factor analysis (IC/Group/Monotonicity)", description=FACTOR_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("momentum", help="Momentum signal analysis", description=MOMENTUM_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("riskparity", help="Risk parityWeight", description=RISKPARITY_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("perf", help="StrategyPerformanceMetric", description=PERF_HELP,
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
        "factor": cmd_factor, "momentum": cmd_momentum,
        "riskparity": cmd_riskparity, "perf": cmd_perf,
    }
    commands[args.command](args)


if __name__ == "__main__":
    main()
