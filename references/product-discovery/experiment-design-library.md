# Experiment Design Library · 实验设计库

## 核心思想
把"用户验证"从模糊概念变成可选菜单——7 种标准实验类型覆盖从假设到验证的不同成本/保真度组合，团队按需选用即可，不用每次重新发明轮子。

## 适用场景
- 团队每次验证都要重新讨论"用什么方法"
- 实验成本与假设风险不匹配（高保真实验测低风险假设）
- 需要标准化实验流程以便横向比较

## 关键步骤
1. 识别待验证假设类型（desirability / usability / feasibility / viability）
2. 从库中匹配实验：
   - First-click test：测导航/信息架构直觉
   - Fake door test：测需求是否存在（埋点不动代码）
   - Wizard of Oz：前端真、后端人工，测用户愿不愿用
   - Technical spike：测技术可行性
   - A/B test：测已上线方案的优化方向
   - Prototype：测交互假设（高保真/低保真可选）
   - Survey：测态度/分群，不测行为
3. 按"风险 × 成本"匹配：高风险假设用高保真实验，低风险用便宜实验
4. 事先定义成功阈值与决策（GO / Pivot / Kill）
5. 实验结果归档到团队实验库，积累学习资产

## 来源
Product Compass（Experiment Design Library 框架）
