# Quantitative Investment · 量化投资

**适用场景**：需要基于数据和模型做投资决策、构建投资组合、评估策略收益与风险

| 方法论 | 一句话描述 | 最佳场景 | Reference |
| --- | --- | --- | --- |
| **Factor Investing** | 基于 Fama-French 等多因子模型系统性获取风险溢价 | 因子选股、组合构建、归因分析 | `factor-investing.md` |
| **Portfolio Optimization** | Markowitz 均值-方差 + Black-Litterman 贝叶斯均衡 | 最优权重分配、风险收益权衡 | `portfolio-optimization.md` |
| **Risk Parity** | 按风险贡献均等分配权重，而非按资金比例 | 风险预算、资产配置、降低集中度 | `risk-parity.md` |
| **Momentum Strategy** | 利用资产价格趋势延续性获取超额收益 | 趋势跟踪、择时、轮动策略 | `momentum-strategy.md` |
| **Statistical Arbitrage** | 基于统计关系的均值回归配对/篮子交易 | 市场中性策略、配对交易、协整 | `statistical-arbitrage.md` |
| **Backtesting Framework** | 系统化回测流程：数据→信号→执行→评估 | 策略验证、参数优化、过拟合检测 | `backtesting-framework.md` |
| **ML Stock Selection** | 用机器学习模型预测收益/分类涨跌选股 | 因子非线性组合、高维特征选股 | `ml-stock-selection.md` |

## 各方法论最低信息需求

- **Factor Investing**：资产历史收益数据 + 因子暴露数据 + 因子收益率数据
- **Portfolio Optimization**：资产预期收益 + 协方差矩阵 + 约束条件（做空限制等）
- **Risk Parity**：资产类别/策略的历史收益序列 + 协方差矩阵
- **Momentum Strategy**：资产历史价格序列 + 回看期/持仓期参数
- **Statistical Arbitrage**：配对/篮子资产历史价格 + 协整检验数据
- **Backtesting Framework**：策略信号定义 + 历史行情数据 + 交易成本假设
- **ML Stock Selection**：特征工程数据（基本面/技术面/另类数据）+ 标签定义（收益率/涨跌）

## 路由触发信号

- "因子选股/多因子模型/alpha 因子/因子暴露/归因分析" → Factor Investing（主）
- "最优组合/资产配置/权重优化/有效前沿/风险收益权衡" → Portfolio Optimization（主）
- "风险预算/风险贡献/风险均配/全天候/降低集中度" → Risk Parity（主）
- "动量/趋势跟踪/轮动/追涨杀跌/价格趋势" → Momentum Strategy（主）
- "配对交易/统计套利/协整/均值回归/市场中性" → Statistical Arbitrage（主）
- "策略回测/历史验证/过拟合/夏普比率/最大回撤" → Backtesting Framework（主）
- "机器学习选股/AI 选股/特征工程/预测模型/非线性因子" → ML Stock Selection（主）

## 常见组合

- **系统化量化策略**：Factor Investing（因子选择）→ Portfolio Optimization（权重优化）→ Backtesting Framework（策略验证）
- **风险导向配置**：Risk Parity（风险预算）→ Momentum Strategy（战术增强）→ Backtesting Framework（效果验证）
- **Alpha 策略开发**：Statistical Arbitrage（信号生成）→ Backtesting Framework（回测验证）→ ML Stock Selection（信号增强）
- **基本面量化**：Factor Investing（因子构建）→ ML Stock Selection（非线性组合）→ Portfolio Optimization（组合构建）
