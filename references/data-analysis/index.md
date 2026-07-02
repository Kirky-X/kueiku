# Data Analysis · 数据分析

**适用场景**：留存分析、A/B 测试、指标体系

| 方法论 | 一句话描述 | 最佳场景 | Reference |
| --- | --- | --- | --- |
| **Cohort Analysis** | 同期群留存曲线 + drop-off 模式 + engagement 趋势 | 留存是否在改善、PMF 判断 | `cohort-analysis.md` |
| **A/B Test Analysis** | 样本量+统计显著性+Ship/Extend/Stop/Investigate+SRM 检测 | A/B 测试设计与决策 | `ab-test-analysis.md` |
| **Lean Analytics Metrics** | 4 准则+8 种指标类型+NSM 四层 | 指标体系选型、好指标准则 | `lean-analytics-metrics.md` |
| **RFM Model** | Recency/Frequency/Monetary 三维度用户细分 | 用户分层、精准营销、流失预警、用户价值评估 | `rfm-model.md` |

## 各方法论最低信息需求

- **Cohort Analysis**：需要按时间分组的用户留存数据
- **A/B Test Analysis**：需要 A/B 测试平台 + 统计学基础
- **Lean Analytics Metrics**：需要 dashboard 数据 + NSM 候选
- **RFM Model**：需要用户交易数据（最近购买日期/购买次数/消费金额）

## 路由触发信号

- "同期群留存分析" → Cohort Analysis（主）
- "A/B 测试设计与决策" → A/B Test Analysis（主）
- "指标体系选型/好指标准则" → Lean Analytics Metrics（主）
- "用户分层/精准营销/流失预警/用户价值评估" → RFM Model（主）

## 常见组合

- **用户价值运营**：RFM Model（分层）→ Cohort Analysis（留存演变）→ A/B Test（策略验证）
- **增长分析**：Lean Analytics Metrics（选指标）→ Cohort Analysis（看留存）→ RFM Model（分层运营）
