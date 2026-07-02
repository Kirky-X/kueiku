# Problem Diagnosis · 问题诊断

**适用场景**：已知问题存在，需要找到根本原因或重新定义问题

| 方法论 | 一句话描述 | 最佳场景 | Reference |
| --- | --- | --- | --- |
| **5 Whys** | 连续追问5次"为什么"，穿透表象找根因 | 线上故障、业务指标下滑、流程失误 | `five-whys.md` |
| **Fishbone / Ishikawa** | 鱼骨图：系统列举多维度成因 | 质量问题、多因素影响、团队协作分析 | `fishbone.md` |
| **First Principles** | 打破类比，从底层公理重新推导 | 创新设计、颠覆现有方案、突破思维定式 | `first-principles.md` |
| **Pareto Analysis** | 识别造成80%结果的20%关键因素，聚焦重点 | 资源分配、问题优先级、关键驱动识别 | `pareto.md` |

## 各方法论最低信息需求

- **5 Whys / Fishbone**：需要一个可量化或可观察的具体问题陈述
- **First Principles**：明确的待颠覆假设或类比
- **Pareto Analysis**：需要可量化的影响指标 + 候选项列表

## 路由触发信号

- "找根本原因" / "为什么出了问题" → 5 Whys（主）
- "颠覆性思考" / "打破假设" → First Principles（主）
- "80/20 重点识别" / "资源聚焦" → Pareto Analysis（主）
