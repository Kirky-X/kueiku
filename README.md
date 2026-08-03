# Kueiku (鬼谷子) —— 方法论指南针技能

[English](README_EN.md)

[![GitHub Release](https://img.shields.io/github/v/release/Kirky-X/kueiku?style=flat-square)](https://github.com/Kirky-X/kueiku/releases) [![GitHub License](https://img.shields.io/github/license/Kirky-X/kueiku?style=flat-square)](LICENSE)

Kueiku 是一个面向 AI agent 的工作方法论导航 skill，采用 Google Labs agent-first 格式（YAML frontmatter + Markdown 路由表）。它不是又一个分析工具，而是一张**方法论索引地图**：指导 agent 在分析问题、制定策略、做决策、设计产品、研究用户、组织思维之前，**先选择正确的框架，再正确地使用框架**。

skill 提供 95 个方法论的索引、快速路由表（任务类型 → 推荐方法论）、调用协议（宣告 → 读 reference → 收集输入 → 执行 → 门控输出）、信息不足时的 4 级降级路径，以及框架选错时的纠偏机制。完整路由表、组合规则与使用协议见 [SKILL.md](SKILL.md)。

## 功能特性

- **95 个方法论 · 18 类** —— 覆盖问题诊断 / 战略分析 / 产品增长 / 决策制定 / 用户研究 / 结构化思维 / 产品发现 / 上市策略 / 市场研究 / 数据分析 / AI 交付 / 执行 / 编程与架构 / 产品哲学 / 领导力 / 财务分析 / 研究方法论 / 行业分析
- **快速路由表** —— 30 秒内从任务类型匹配到主框架 + 备选框架
- **调用协议** —— 5 步标准流程，让框架使用过程显性化、可追溯
- **组合规则** —— 14 种常见方法论组合（如战略规划 PESTLE → SWOT → OKR）
- **降级路径** —— 信息不足分 4 级处理，绝不强行套框架
- **纠偏机制** —— 执行中发现框架不适用，立即停止并重新路由
- **自动化脚本** —— 5 个计算密集型方法论的 CLI 工具（RICE / 决策矩阵 / 风险矩阵 / 杜邦 / 帕累托）

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

### 18 类 · 95 个方法论

| 类别 | 数量 | 适用场景 |
| ---- | ---- | -------- |
| 🔍 问题诊断 | 4 | 找根因、颠覆性思考、80/20 聚焦 |
| 📊 战略分析 | 23 | 现状评估、竞争格局、商业模式、定价护城河、价值链、战略演化 |
| 🚀 产品与增长 | 8 | 用户需求、增长瓶颈、产品创新、指标体系 |
| ⚖️ 决策制定 | 9 | 优先级排序、目标制定、风险预演、选型、风险评估 |
| 👥 用户研究 | 4 | 用户旅程、同理心画像、决策旅程、需求层次 |
| 🧠 结构化思维 | 9 | MECE 表达、多视角评估、假设澄清、框架选择、系统思考 |
| 🔬 产品发现 | 8 | 持续发现、假设验证、用户访谈、实验设计 |
| 🚩 上市策略 | 7 | 滩头堡、ICP、GTM、增长飞轮、定位 |
| 📈 市场研究 | 7 | 市场规模、细分、用户画像、STP、感知图、技术采用 |
| 📉 数据分析 | 4 | 同期群、A/B 测试、指标体系、RFM |
| 🤖 AI 交付 | 2 | 交付物标准、文档代码 drift |
| 🏃 执行 | 4 | 结果导向路线图、战略红队、敏捷需求 |
| 💻 编程与架构 | 4 | TDD、小步计划、服务契约、Agent DX |
| 🎯 产品哲学 | 4 | 激进减法、垂直整合、科技人文、隐形完美 |
| 👑 领导力 | 3 | 现实扭曲力场、A 级人才密度、变革管理 |
| 💰 财务分析 | 4 | 杜邦、DCF、可比公司、EVA |
| 📚 研究方法论 | 1 | 系统化研究流程 |
| 🏭 行业分析 | 2 | 行业价值链、技术成熟度曲线 |

完整方法论列表与路由见 [SKILL.md 类别总览](./SKILL.md)。

### `references/` —— 95 个方法论参考文件

每个方法论对应一个 `references/<category>/<methodology>.md`，包含执行步骤与输出模板。仅在需要时读取对应文件，不预加载全部。

```
references/
├── problem-diagnosis/        (4)  5 Whys / Fishbone / First Principles / Pareto
├── strategy/                 (23) SWOT / PESTLE / Porter's / BMC / Ansoff / Blue Ocean / Wardley Mapping ...
├── product-growth/            (8) AARRR / JTBD / Design Thinking / Lean BML / VPC / SCAMPER / Kano / North Star
├── decision-making/           (9) RICE / Eisenhower / OKR / Pre-mortem / Decision Matrix / MoSCoW / FMEA / Risk Matrix
├── user-research/             (4) Customer Journey / Empathy Map / Consumer Decision Journey / Maslow
├── structured-thinking/       (9) MECE+Pyramid / Six Hats / Socratic / Cynefin / Second-Order / Systems Thinking ...
├── product-discovery/         (8) OST / Mom Test / ICE / Opportunity Score / Pretotypes / Assumption Mapping ...
├── go-to-market/              (7) Beachhead / ICP / GTM Motions / GTM Strategy / Growth Loops / Battlecard / Positioning
├── market-research/           (7) Market Sizing / Segmentation / User Personas / STP / Perceptual Mapping ...
├── data-analysis/             (4) Cohort / A/B Test / Lean Analytics / RFM
├── ai-delivery/               (2) Shipping Artifacts / Intended vs Implemented
├── execution/                 (4) Outcome Roadmap / Strategy Red Team / User Stories / Job Stories
├── engineering/               (4) TDD / Bite-Sized Plan / Typed Service Contracts / Agent DX
├── product-philosophy/        (4) Focus as No / Whole Widget / Technology Meets Humanities / Invisible Perfection
├── leadership/                (3) Reality Distortion Field / A-Player Density / Change Management
├── financial-analysis/        (4) DuPont / DCF / Comparable Company / EVA
├── research-methodology/      (1) Systematic Research Process
└── industry-analysis/         (2) Industry Value Chain / Gartner Hype Cycle
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
