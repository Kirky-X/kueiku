#!/usr/bin/env python3
"""kueiku-calc — Kueiku 方法论计算工具集（向后兼容入口）

实际逻辑已拆分至 kueiku_calc/ 包：
  kueiku_calc/
  ├── utils.py       公共工具（CSV 读写、格式化、矩阵运算、统计辅助）
  ├── decision.py    RICE / Decision Matrix / ICE
  ├── risk.py        Risk Matrix / FMEA / Pareto
  ├── financial.py   DuPont / DCF / EVA
  ├── data.py        A/B Test / RFM / Cohort
  ├── strategy.py    BCG / GE-McKinsey / Opportunity Score
  ├── quant.py       Factor / Momentum / Risk Parity / Performance
  └── main.py        CLI 入口（argparse 子命令注册）

用法:
  python kueiku-calc.py <subcommand> -i <input.csv> [-o report.md] [--json]
"""

import os
import sys

# 确保包目录在 Python 路径中
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from kueiku_calc.main import main

if __name__ == "__main__":
    main()
