# Financial Analysis · 财务分析

**适用场景**：需要对企业财务表现、估值、价值创造做量化判断

| 方法论 | 一句话描述 | 最佳场景 | Reference |
| --- | --- | --- | --- |
| **DuPont Analysis** | ROE = 净利率 × 资产周转率 × 权益乘数 三因素拆解 | 财务诊断、同业对比、ROE 异动分析 | `dupont.md` |
| **DCF** | 企业价值 = 未来自由现金流现值之和 | 企业估值、投资决策、并购定价 | `dcf.md` |
| **Comparable Company** | 通过相似公司估值倍数推断目标公司价值 | IPO 定价、并购、行业对比 | `comparable-company.md` |
| **EVA** | EVA = NOPAT - 资本成本 × 投入资本，衡量真实价值创造 | 绩效评估、投资决策、价值管理 | `eva.md` |

## 各方法论最低信息需求

- **DuPont Analysis**：目标公司三因素数据 + 同业对比数据
- **DCF**：未来现金流预测 + WACC 估算 + 终值假设
- **Comparable Company**：可比公司清单 + 估值倍数数据
- **EVA**：NOPAT + 资本成本 + 投入资本数据

## 路由触发信号

- "ROE 异动原因/财务诊断/盈利能力拆解" → DuPont Analysis（主）
- "企业估值/投资决策/并购定价" → DCF（主）
- "IPO 定价/行业估值对比/可比公司" → Comparable Company（主）
- "真实价值创造/绩效评估/资本效率" → EVA（主）

## 常见组合

- **企业估值**：DCF（内在价值）+ Comparable Company（市场参照）交叉验证
- **财务诊断**：DuPont Analysis（ROE 拆解）→ EVA（价值创造验证）
- **投资决策**：DuPont Analysis（质量评估）→ DCF（估值）→ EVA（持有期价值创造）
