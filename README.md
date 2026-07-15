# Kueiku (鬼谷子) —— 方法论指南针技能

[English](README_EN.md)

[![GitHub Release](https://img.shields.io/github/v/release/Kirky-X/kueiku?style=flat-square)](https://github.com/Kirky-X/kueiku/releases) [![GitHub License](https://img.shields.io/github/license/Kirky-X/kueiku?style=flat-square)](LICENSE)

Kueiku 是一个面向 AI agent 的工作方法论导航 skill，采用 Google Labs agent-first 格式（YAML frontmatter + Markdown 路由表）。它不是又一个分析工具，而是一张**方法论索引地图**：指导 agent 在分析问题、制定策略、做决策、设计产品、研究用户、组织思维之前，**先选择正确的框架，再正确地使用框架**。

skill 提供 35 种方法论的索引、快速路由表（任务类型 → 推荐方法论）、调用协议（宣告 → 读 reference → 收集输入 → 执行 → 门控输出）、信息不足时的 4 级降级路径，以及框架选错时的纠偏机制。完整路由表、组合规则与使用协议见 [SKILL.md](SKILL.md)。

## 功能特性

- **35 种方法论 · 6 大类** —— 覆盖问题诊断 / 战略分析 / 产品增长 / 决策制定 / 用户研究 / 结构化思维
- **快速路由表** —— 30 秒内从任务类型匹配到主框架 + 备选框架
- **调用协议** —— 5 步标准流程，让框架使用过程显性化、可追溯
- **组合规则** —— 14 种常见方法论组合（如战略规划 PESTLE → SWOT → OKR）
- **降级路径** —— 信息不足分 4 级处理，绝不强行套框架
- **纠偏机制** —— 执行中发现框架不适用，立即停止并重新路由

## 安装

### 方式一：通过 `skills` 包安装（推荐）

需 [Node.js](https://nodejs.org/) 18+ 和 `skills` npm 包（v1.5.12+）。`skills` 是 open agent skills 生态的 CLI，支持 68+ agents（Claude Code / Trae / Cursor / Codex / OpenCode 等）。

```bash
# 安装到 Claude Code
npx skills add https://github.com/Kirky-X/kueiku.git --agent claude-code -y

# 等价简写（owner/repo）
npx skills add Kirky-X/kueiku --agent claude-code -y

# 安装到 Trae
npx skills add Kirky-X/kueiku --agent trae -y

# 列出仓库中可被发现的所有 skills（不安装）
npx skills add https://github.com/Kirky-X/kueiku.git --list
```

安装后 skill 文件位于对应 agent 的 skills 目录（如 `.claude/skills/kueiku/`）。

### 方式二：传统 git clone

```bash
git clone https://github.com/Kirky-X/kueiku.git
# 将 SKILL.md + references/ 链接或复制到 agent skills 目录
# 各 runtime 的 skills 目录路径示例（任选其一）：
#   Claude Code:  ~/.claude/skills/kueiku/
#   Trae:         ~/.trae-cn/skills/kueiku/
#   Cursor:       ~/.cursor/skills/kueiku/
#   Codex:        ~/.codex/skills/kueiku/
```

## 使用示例

Kueiku 作为 skill 被 agent 加载后，通过自然语言意图触发，无需显式命令。任务类型到方法论的完整路由见 [SKILL.md 快速路由表](./SKILL.md)。

| 任务类型 | 推荐方法论 | 一句话功能 |
| -------- | ---------- | ---------- |
| 找根本原因 | 5 Whys | 连续追问穿透表象找根因 |
| 战略现状评估 | SWOT | 内部优劣势 × 外部机遇威胁 |
| 增长瓶颈分析 | AARRR Funnel | 获取→激活→留存→推荐→营收漏斗 |
| 需求优先级排序 | RICE Scoring | Reach×Impact×Confidence÷Effort 量化 |
| 用户真实需求 | JTBD | 用户购买的是「任务完成」 |
| 商业模式设计 | Business Model Canvas | 9 模块完整商业模式 |
| 重大决策风险预演 | Pre-mortem | 逆向想象失败场景 |
| 结构化表达 | MECE + Pyramid | 相互独立完全穷尽 + 结论先行 |

## 能力概览

### 6 大类 · 35 种方法论

| 类别 | 方法论 | 适用场景 |
| ---- | ------ | -------- |
| 🔍 问题诊断 | 5 Whys / Fishbone / First Principles / Pareto | 已知问题，需找根本原因 |
| 📊 战略分析 | SWOT / PESTLE / Porter's Five Forces / BMC / Stakeholder / Ansoff / Blue Ocean / McKinsey 7S / BCG | 评估形势，制定方向 |
| 🚀 产品增长 | AARRR / JTBD / Design Thinking / Lean BML / VPC / SCAMPER / Kano / North Star | 产品设计、用户增长、需求验证 |
| ⚖️ 决策制定 | RICE / Eisenhower / OKR / Pre-mortem / Decision Matrix / MoSCoW / FMEA | 多选项中做可辩护决定 |
| 👥 用户研究 | Customer Journey / Empathy Map | 深度理解用户需求与痛点 |
| 🧠 结构化思维 | MECE+Pyramid / Six Thinking Hats / Socratic / Cynefin / Second-Order Thinking | 组织复杂信息，澄清假设 |

### `references/` —— 35 个方法论参考文件

每个方法论对应一个 `references/xxx.md`，包含执行步骤与输出模板。仅在需要时读取对应文件，不预加载全部。

```
references/
├── five-whys.md                  5 Whys 根因分析
├── fishbone.md                   鱼骨图 / 因果图
├── first-principles.md           第一性原理
├── pareto.md                     帕累托分析
├── swot.md                       SWOT 分析
├── pestle.md                     PESTLE 宏观环境分析
├── porter-five-forces.md         波特五力模型
├── business-model-canvas.md      商业模式画布
├── stakeholder-mapping.md        利益相关者分析
├── ansoff-matrix.md              安索夫矩阵
├── blue-ocean.md                 蓝海战略
├── mckinsey-7s.md                麦肯锡 7S 模型
├── bcg-matrix.md                 波士顿矩阵
├── aarrr.md                      AARRR 增长漏斗
├── jtbd.md                       JTBD 用户任务框架
├── design-thinking.md            设计思维
├── lean-bml.md                   精益 Build-Measure-Learn
├── value-proposition-canvas.md   价值主张画布
├── scamper.md                    SCAMPER 创意触发
├── kano.md                       狩野模型
├── north-star.md                 北极星框架
├── rice.md                       RICE 优先级评分
├── eisenhower.md                 艾森豪威尔矩阵
├── okr.md                        OKR 目标与关键结果
├── premortem-counterfactual.md   逆向规划与反事实思维
├── decision-matrix.md            决策矩阵
├── moscow.md                     莫斯科法
├── fmea.md                       失效模式与影响分析
├── customer-journey.md           客户旅程地图
├── empathy-map.md                同理心地图
├── mece-pyramid.md               MECE + 金字塔原则
├── six-thinking-hats.md          六顶思考帽
├── socratic-questioning.md       苏格拉底式提问
├── cynefin.md                    肯尼芬框架
└── second-order-thinking.md      二阶思维
```

## 调用协议

调用一个方法论的标准流程：

```
0. 前置检查   → 确认任务类型匹配路由表，确认信息充分度
1. 宣告框架   → 说明使用何种方法论及选择原因
2. 读取 reference → 提取执行步骤与输出模板
3. 收集输入   → 逐项确认输入数据，缺失项按降级路径处理
4. 执行框架   → 按步骤输出，每步标注信息来源
5. 门控输出   → 结论必须直接回答问题 + 可执行建议 + 置信度
```

## FAQ

### `skills` 包版本要求？

需 `skills` npm 包 **v1.5.12+**。`skills` 是 [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) 生态的 CLI，支持 68+ agents。用 `npx skills@latest` 自动获取最新版。

### 何时不应使用框架？

- 任务本身简单明确，框架会增加不必要复杂性
- 用户明确要求直接回答
- 框架所需信息严重缺失（Level 4），连框架选择都无法判断

此时直接说明并给出最佳判断，标注置信度与依赖假设。

### 信息不足时怎么办？

按 4 级降级路径处理：Level 1 正常执行 → Level 2 标注假设与待收集项 → Level 3 停止并提关键问题 → Level 4 退化为直接最佳判断。详见 [SKILL.md 信息不足降级路径](./SKILL.md)。

### 框架选错怎么办？

执行中发现框架不适用（关键维度无法填充且非信息问题、结论与问题脱节、用户反馈方向不对），立即停止，说明已完成部分与不适合理由，从路由表重新选择并说明切换理由。

## 许可证

MIT
