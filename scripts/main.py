"""CLI 入口 — argparse 子命令注册与分发。"""

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
        description="Kueiku 方法论计算工具集 — 19 个高计算密度方法论自动化",
    )
    subparsers = parser.add_subparsers(dest="command", help="子命令")

    def add_common_args(p):
        p.add_argument("-i", "--input", required=True, help="CSV 文件路径（- 表示 stdin）")
        p.add_argument("-o", "--output", help="输出文件路径（默认 stdout）")
        p.add_argument("--json", action="store_true", help="输出 JSON 格式")

    # 决策与优先级
    p = subparsers.add_parser("rice", help="RICE 优先级评分", description=RICE_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("dmatrix", help="决策矩阵（Pugh Matrix）", description=DMATRIX_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("ice", help="ICE 评分", description=ICE_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # 风险评估
    p = subparsers.add_parser("risk", help="风险矩阵", description=RISK_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("fmea", help="FMEA 失效模式分析", description=FMEA_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("pareto", help="帕累托分析", description=PARETO_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # 财务分析
    p = subparsers.add_parser("dupont", help="杜邦分析", description=DUPONT_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("dcf", help="现金流折现估值", description=DCF_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)
    p.add_argument("--rate", type=float, default=0.10, help="折现率 (WACC), 默认 0.10")
    p.add_argument("--growth", type=float, default=0.03, help="永续增长率, 默认 0.03")
    p.add_argument("--shares", type=float, default=0, help="流通股数（可选）")

    p = subparsers.add_parser("eva", help="经济增加值", description=EVA_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # 数据分析
    p = subparsers.add_parser("abtest", help="A/B 测试显著性分析", description=ABTEST_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("rfm", help="RFM 用户分层", description=RFM_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("cohort", help="同期群留存分析", description=COHORT_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # 战略矩阵
    p = subparsers.add_parser("oppscore", help="机会评分", description=OPPSCORE_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("bcg", help="BCG 矩阵", description=BCG_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("gemckinsey", help="GE-McKinsey 矩阵", description=GEMCKINSEY_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    # 量化投资
    p = subparsers.add_parser("factor", help="因子分析（IC/分组/单调性）", description=FACTOR_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("momentum", help="动量信号分析", description=MOMENTUM_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("riskparity", help="风险平价权重", description=RISKPARITY_HELP,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    add_common_args(p)

    p = subparsers.add_parser("perf", help="策略绩效指标", description=PERF_HELP,
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
