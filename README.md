# Kueiku（鬼谷子）— 方法论导航罗盘

> AI agent 的方法论导航图：先选对框架，再用对框架。19 类 × 142 个方法论的索引地图，含选择路由、调用协议、信息不足降级路径与框架纠偏机制。

[![version](https://img.shields.io/github/v/tag/Kirky-X/kueiku?style=flat-square)](https://github.com/Kirky-X/kueiku/tags) [![license](https://img.shields.io/github/license/Kirky-X/kueiku?style=flat-square)](LICENSE) [![python](https://img.shields.io/badge/python-3.8%2B-blue?style=flat-square)](scripts/)

中文 | [English](README_EN.md)

## ✨ 功能特性

- **19 类 × 142 个方法论索引**：每个方法论一个 `references/<类别>/<方法论>.md`（执行步骤 + 输出模板），按需读取、不全量预载；数目由 `scripts/count_methodologies.py` 脚本生成（`methodology-count.json`）
- **快速路由表**：任务类型 → 主框架 + 备选框架，30 秒内完成选择（见 [SKILL.md](SKILL.md)）
- **调用协议**：声明 → 读参考 → 收集输入 → 执行 → 门控输出，五步标准流程，方法论使用可追溯
- **信息不足降级路径**：4 级处理——正常执行 → 标注假设与待收集项 → 停下追问关键问题 → 回退最佳判断，绝不硬套框架
- **框架纠偏机制**：执行中发现框架不适配（关键维度填不上、结论漂移、用户否定方向）立即停止、说明原因、重新路由
- **组合规则**：常见方法论组合及互斥对（如 Lean Canvas ↔ Startup Canvas 二选一、ICE 粗筛 → RICE 精排）；高频多步组合按 playbook 格式（每步产物 + 条件分支 + 最终交付物）编排
- **硬性出口**：质量门禁六检（含 stop_reason 终止原因标注与 Reassess When 重选触发条件）、Red Flags 负面门禁（欺诈/零数据/紧急生存不进分析）、信息缺失三入口模式（Guided / Context dump / Best guess）
- **评估与校验资产**：`evals/evals.json` 路由评测集（22 条路由用例 + 4 条端到端场景；用例带 `expected`/`acceptable` 字段，live 评测按 lenient/strict 双口径计分）、`triggers/trigger-queries.json` 触发守卫（signal 词静态检查）、`scripts/validate_skill.py` 结构校验（CI 常跑）
- **计算工具 CLI**（`kueiku-calc`，19 个子命令）：RICE / 决策矩阵 / ICE / 风险矩阵 / FMEA / 帕累托 / 杜邦 / DCF / EVA / A-B 测试 / RFM / Cohort / 机会分 / BCG / GE-McKinsey / 因子分析 / 动量信号 / 风险平价 / 绩效指标

| 类别（计数） | 类别（计数） | 类别（计数） |
| ------------ | ------------ | ------------ |
| 问题诊断（7） | 战略分析（24） | 产品增长（8） |
| 决策制定（12） | 用户研究（5） | 结构化思考（9） |
| 产品发现（8） | 上市策略（7） | 市场研究（7） |
| 数据分析（5） | AI 交付（2） | 执行落地（4） |
| 工程实践（21） | 产品哲学（4） | 领导力（3） |
| 财务分析（5） | 研究方法论（2） | 行业分析（2） |
| 量化投资（7） | | |

## 📦 安装

```bash
# 方式 1：多 skill 工作区一键部署——需在 kueiku/ 与 scripts/ 同层的工作区根执行
# （scripts/sync-skills.sh 属多 skill 工作区，不随本仓分发；单独 clone 本仓请用方式 2/3。
#   同步到 ~/.zcode/skills/ 与 ~/.claude/skills/，LF 强制归一）
bash scripts/sync-skills.sh kueiku

# 方式 2：手动拷贝到 agent 技能目录
cp -r kueiku/ ~/.zcode/skills/kueiku/
# 方式三：远程安装（GitHub 仓库）
npx skills add Kirky-X/kueiku --agent claude-code -y
```

首跑依赖：仅需 Python 3.8+（CLI 工具全部使用标准库），无 requirements.txt。

## 🚀 快速开始

前置：skill 已部署到 agent 技能目录，在支持 skills 的 agent 会话中用自然语言触发。

```text
用 SWOT 分析一下我们的出海策略          # 路由 → 战略分析 → swot
这三个需求先做哪个？                    # 路由 → 决策制定 → RICE
给这批用户做分层                        # 路由 → 数据分析 → RFM
```

计算类方法论可直接用 CLI（确定性、可复现，输入 CSV）：

```bash
python3 ~/.zcode/skills/kueiku/scripts/main.py rice -i items.csv     # RICE 优先级打分
python3 ~/.zcode/skills/kueiku/scripts/main.py abtest -i ab.csv --json   # A/B 显著性 + SRM 检测
# ab.csv 格式：variant,users,conversions 两行（control / treatment）
python3 ~/.zcode/skills/kueiku/scripts/main.py dcf -i cashflows.csv --rate 0.10 --growth 0.03 --shares 1000000   # DCF 估值 + 每股价值（--rate 贴现率，--growth 永续增长率）
# cashflows.csv 格式：year,fcf；全部子命令支持 -i -（stdin）与 -o <file>（写文件，默认 stdout）
```

### 调用协议（五步）

进入某方法论后的五步标准流程：

```text
0. 预检      → 任务类型匹配路由表；确认信息充分性
1. 声明      → 说明使用哪个方法论、为什么
2. 读参考    → 提取执行步骤与输出模板
3. 收集输入  → 逐项确认框架所需输入，缺失项走降级路径
4. 执行      → 逐步输出，标注每条信息的来源
5. 门控输出  → 结论直答 + 可执行建议 + 置信度 + stop_reason 终止原因 + Reassess When 重选触发条件
```

## ✅ 测试与验证

pytest 套件实测（2026-10-01，Python 3.12，45 用例 / 9 文件）：

```text
$ python3 -m pytest tests -q
.............................................                         [100%]
45 passed in 0.60s
```

覆盖 9 个测试文件：`test_abtest`（A/B 显著性）、`test_dcf`（DCF 估值）、`test_rice_tiers`（RICE 分档）、`test_input_validation`（输入校验）、`test_consistency`（口径一致性）、`test_skips`（跳过逻辑）、`test_navigation`（导航链接完整性 + index 必含章节 + 验收场景资产回归 + 条目骨架覆盖下限 91/142）、`test_routing_signals`（index.md 层路由一致性守卫）、`test_eval_assets`（路由评测集 schema/覆盖下限守卫 + trigger 查询 signal 词静态守卫）。

验收事实源收敛在 `evals/evals.json`：4 条端到端场景 + `routing_cases` 路由用例（19 类每类 ≥1 条正例 + 3 条 `none` 负例；用例带 `expected`/`acceptable` 字段，lenient/strict 双口径计分发生在跑 LLM 的 live 评测中——本仓无打分脚本，pytest 不执行，口径定义见 [docs/MAINTENANCE.md](docs/MAINTENANCE.md)）。v0.1.5 时代的重复拷贝 `test-prompts.json` 已删除。结构校验：`python3 scripts/validate_skill.py`（frontmatter 白名单、name/description 限制、SKILL.md ↔ skill.json 版本与 description 一致性），已挂入 CI。

方法论计数口径：`python3 scripts/count_methodologies.py`（写入 `scripts/methodology-count.json`），SKILL.md 与 skill.json 的计数以其为准。

## 📁 目录结构

```text
kueiku/
├── SKILL.md                 # 入口：路由表 + 调用协议 + 降级路径 + 纠偏机制
├── skill.json               # 元数据（v0.1.6，MIT）
├── references/              # 19 个类别目录，每目录 index.md + 各方法论 .md
│   ├── strategy/            # 24 个：SWOT / PESTLE / 五力 / BMC / 蓝海 / Wardley …
│   ├── engineering/         # 21 个：TDD / DDD / API 设计 / 代码评审清单 / 事件响应 …
│   ├── quantitative-investment/  # 7 个：因子 / 动量 / 风险平价 / 回测 / ML 选股 …
│   └── …（另 16 类）
├── evals/                   # 验收事实源：端到端场景 + routing_cases 路由用例
├── triggers/                # skill 级触发/近失查询（signal 词静态守卫的对象）
├── docs/MAINTENANCE.md      # 维护与贡献规则（条目骨架 / 准入裁决 / 加必配删预算）
├── scripts/
│   ├── main.py              # kueiku-calc CLI 入口（19 子命令）
│   ├── count_methodologies.py  # 方法论计数（生成 methodology-count.json）
│   ├── validate_skill.py    # 结构校验（frontmatter / description / 版本一致性）
│   ├── install-skill.sh     # 安装器：install/update/uninstall 等 7 子命令，支持 9 种 agent 与 standalone 仓模式
│   ├── skill_lint.py        # 仓库体检：frontmatter/链接/JSON/版本一致性门禁（FAIL/WARN 两级）
│   └── decision|financial|quant|risk|strategy|data|utils.py  # 各域计算实现
└── tests/                   # pytest 套件（45 用例，9 文件）
```

## 🔮 边界

- **简单任务不套框架**：任务简单明确或用户要直接答案时，跳过框架直接回答
- **信息严重不足不硬选**：连框架选择都无法确定时，先澄清提问（降级路径 L3+）
- **只导航与计算，不执行改动**：本 skill 提供方法论选择、推理框架与计算工具；实际改代码、跑安全扫描由执行型 skill 承担（代码审查→diting，SAST→tiangang）
- **互斥组合不并用**：Lean Canvas ↔ Startup Canvas 二选一；ICE 只做粗筛，与 RICE 并行会产生冗余输出

## 📄 License 与归属

MIT License（© 2026 Kirky-X）。
