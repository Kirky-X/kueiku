# Product Philosophy · 产品哲学

**适用场景**：需要在产品方向、架构与工艺标准上做底层判断，而非执行层排期

| 方法论 | 一句话描述 | 最佳场景 | Reference |
| --- | --- | --- | --- |
| **Focus as No** | 聚焦不是说"是"，而是说"不"，激进减法锁定最小集 | 产品范围决策、功能取舍、防止产品臃肿 | `focus-as-no.md` |
| **Whole Widget** | 端到端负责，关键决策不外包的垂直整合架构 | 产品架构决策、垂直整合 vs 水平分工选择 | `whole-widget.md` |
| **Technology Meets Humanities** | 科技 × 人文 × 商业三维评估，单一视角不足以做出好产品 | 产品评估、设计决策、团队组建 | `technology-meets-humanities.md` |
| **Invisible Perfection** | 内部工艺质量决定外部体验，看不见的地方也要打磨 | 代码质量、内部工具、工艺标准制定 | `invisible-perfection.md` |

## 各方法论最低信息需求

- **Focus as No**：当前功能/需求清单 + 业务目标优先级
- **Whole Widget**：产品关键决策点清单 + 各环节外包成本/收益数据
- **Technology Meets Humanities**：产品的技术指标 + 用户人文感受数据 + 商业模型
- **Invisible Perfection**：内部工艺点清单 + 现有质量标准 + 自动化检查能力

## 路由触发信号

- "功能太多/产品臃肿/什么都想做" → Focus as No（主）
- "这个环节要不要自研还是外包/买方案" → Whole Widget（主）
- "产品评估只看技术指标不够/缺少人文视角" → Technology Meets Humanities（主）
- "代码质量/内部工具要不要花时间打磨" → Invisible Perfection（主）

## 常见组合

- **产品范围决策**：Focus as No（锁定最小集）→ RICE（执行排序）→ Invisible Perfection（工艺标准）
- **架构决策**：Whole Widget（识别关键决策点）→ Technology Meets Humanities（三维评估）
- **新品评估**：Technology Meets Humanities（三维评估）→ Focus as No（剔除诱惑项）
