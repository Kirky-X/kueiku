# Strategy Red Team · 战略红队演练

## 核心思想
团队制定战略后容易陷入"自我说服"。Red Team 演练强制先 steelman（把对手最强论点表达得比对手自己更好）再攻击，避免稻草人谬误。然后按 impact × likelihood × cheapness-to-test 排序，优先验证最值得验证的反驳。

## 适用场景
- 战略即将拍板，需要最后一轮压力测试
- 团队对战略过度自信，缺乏异见
- 投资人/董事会可能提出的挑战需提前准备

## 关键步骤
1. 写出待 challenge 的战略命题（一句话清晰表述）
2. Steelman：找一个真正的对手视角，把反对论点表达得比对手更强（不许用"对手会说"这种弱化版本）
3. Attack：基于 steelman 找出战略的薄弱假设与失效条件
4. 对每条反驳评估 3 维：
   - Impact：若成立对战略的破坏程度（高/中/低）
   - Likelihood：成立概率（高/中/低）
   - Cheapness-to-test：验证成本（低/中/高）
5. 排序：高 Impact + 高 Likelihood + 低 cost 优先验证
6. 设计验证实验（参考 experiment-design-library.md），结果回写战略修订

## 来源
Product Compass（Strategy Red Team 框架）；红队概念源自军事与网络安全
