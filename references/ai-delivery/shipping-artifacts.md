# Shipping Artifacts · 交付物清单

## 核心思想
AI 时代交付不是写一份厚重 PRD 就完事——交付物应分 Core 5（必交）+ Conditional 4（按场景交），并明确"Anti-PRD rule"：不要写传统 50 页 PRD，写让 agent 和人类都能执行的最小可执行文档。

## 适用场景
- AI 项目交付物标准不一，agent 与人类工程师接不上
- PRD 越写越长但执行效率越来越低
- 不同角色反复询问"我该看哪份文档"

## 关键步骤
1. Core 5（每个项目必交）：
   - Problem Statement（要解决什么问题，不写方案）
   - Spec（接口/契约定义，agent 可直接消费）
   - Tasks（拆解为可独立执行的任务列表，每条带验收条件）
   - Design Doc（关键设计决策与权衡，不超 1 页）
   - README（如何运行/测试，最小可执行入口）
2. Conditional 4（按场景交）：
   - ADR（架构决策记录，复杂决策时）
   - Runbook（上线后运维操作，生产系统时）
   - Migration Plan（涉及数据迁移时）
   - Postmortem（出过事故后）
3. Anti-PRD rule：禁止写"产品需求文档"超过 2 页——超出部分拆为 Spec + Tasks + Design Doc
4. 所有文档带显式版本与状态（Draft/Review/Approved/Deprecated）
5. 文档之间用显式链接互引，避免信息孤岛

## 来源
Product Compass（Shipping Artifacts 框架）；Anti-PRD 思想见 Shape Up 方法论
