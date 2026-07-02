# Pricing Strategy · 定价策略

## 核心思想
定价是产品战略的一部分，不是工程上线后的附属决策。通过 Van Westendorp 价格敏感度计量找出可接受价格区间，结合价值计量单位（value metric）与分层设计（tier design），让定价同时反映用户价值与商业目标。

## 适用场景
- 新产品定价/老产品调价
- 不知道用户愿意付多少
- 现有定价与用户感知价值脱节

## 关键步骤
1. 选定价值计量单位（value metric）：用户每多用一单位就多获得一单位价值（如 API 调用数、座位数、存储量）
2. 用 Van Westendorp Price Sensitivity Meter 调研 4 个问题：
   - 太便宜（怀疑质量）的价格
   - 便宜（划算）的价格
   - 贵（仍会考虑）的价格
   - 太贵（不会买）的价格
3. 交叉分析得出 4 个价格点：可接受下限/上限 + 最优价格点/无差异价格点
4. 设计分层：Free / Basic / Pro / Enterprise，每层对应明确的 value metric 阈值与功能边界
5. 验证：用 pretotype 或 A/B 测试真实付费转化率，不要只信问卷

## 来源
综合：Van Westendorp（1976）PSM 方法 + OpenView Pricing Framework + April Dunford 定价思想
