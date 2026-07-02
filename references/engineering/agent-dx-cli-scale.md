# Agent DX / CLI Scale · Agent 开发者体验评分轴

## 核心思想
传统 DX（开发者体验）面向人类，agent 时代需要新评分轴。用 7 个 0–3 分维度量化工具/CLI/SDK 对 agent 的友好度，让"agent 能不能高效使用"从主观判断变成可审计的清单。

## 适用场景
- 设计 CLI/SDK 给 AI agent 使用
- 评估现有工具的 agent 友好度
- 工具文档质量参差，agent 调用频繁出错

## 关键步骤
对每个维度 0–3 打分（0=极差，3=优秀）：

1. **Machine-Readable**：输出是否有结构化格式（JSON/JSON Lines）？还是只有人类可读文本？
2. **Raw Payload**：是否能输出原始数据（不带 formatting/color/box-drawing 字符）？
3. **Schema Introspection**：agent 能否查询输入/输出 schema（命令行 `--help` 是否机器可读、是否有 schema endpoint）？
4. **Context Window**：输出是否可裁剪到必要字段（`--fields`/`--filter`），避免撑爆 agent context？
5. **Input Hardening**：输入是否容忍 agent 的常见错误（多余空格、字段顺序、引号风格）？
6. **Safety Rails**：危险操作是否需要显式 `--confirm`，避免 agent 误执行破坏性命令？
7. **Knowledge Packaging**：是否提供可被 agent 加载的精简知识包（SKILL.md / structured docs），而非让 agent 爬完整文档？

总分 = 7 维度相加（0–21）：
- 0–7：agent 难以使用，需大量 wrapper
- 8–14：可用但低效
- 15–21：agent 原生友好

## 来源
design.md（Agent DX / CLI Scale 评分轴）
