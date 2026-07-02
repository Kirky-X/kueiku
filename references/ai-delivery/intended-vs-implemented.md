# Intended vs Implemented · 意图与实现对照

## 核心思想
代码 drift 是 AI 协作时代最隐蔽的风险——文档说做 A，代码实际做 B，无人察觉直到事故。本框架要求每个关键决策点都有"documented intent ↔ cited code evidence"双向引用，并对跨模块/跨边界的 mismatch 显式标记。

## 适用场景
- AI agent 大量改动代码，人类难以逐行 review
- 文档与代码长期不同步，新成员读文档后被误导
- 跨团队接口频繁出现"我以为你们做了"的偏差

## 关键步骤
1. 在每个 Design Doc / Spec 中标注 intent：明确"我们决定这样做，因为..."
2. 在代码注释中反向引用 doc：`// implements: design.md#section-3.2`
3. CI 自动检查：每个被引用的代码段必须存在且符合 doc 描述的接口签名
4. 对跨模块/跨服务边界做显式 mismatch 标记：
   - doc 说同步调用，代码改为异步——必须显式标注并通知依赖方
   - doc 说返回 Result，代码 panic——CI 报警
5. 定期（每月）做 intent↔code 双向 audit，输出 mismatch 清单
6. mismatch 不一定是 bug，但必须显式决策：修订 doc / 修订 code / 标记为已知偏离

## 来源
Product Compass（Intended vs Implemented 框架）
