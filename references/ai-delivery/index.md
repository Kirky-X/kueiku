# AI Delivery · AI 交付

**适用场景**：AI 时代交付物标准、文档代码 drift 检测

| 方法论 | 一句话描述 | 最佳场景 | Reference |
| --- | --- | --- | --- |
| **Shipping Artifacts** | Core 5 + Conditional 4 文档 + Anti-PRD rule | AI 项目交付物标准 | `shipping-artifacts.md` |
| **Intended vs Implemented** | documented intent ↔ cited code 双向引用 + boundary mismatch | 文档与代码 drift 检测 | `intended-vs-implemented.md` |

## 各方法论最低信息需求

- **Shipping Artifacts**：需要项目范围 + 文档版本管理
- **Intended vs Implemented**：需要 Design Doc + 代码引用关系

## 路由触发信号

- "AI 项目交付物标准" → Shipping Artifacts（主）
- "文档与代码 drift 检测" → Intended vs Implemented（主）
