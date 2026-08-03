# Decision Making · 决策制定

**适用场景**：需要在多个选项中做出可辩护的决定

| 方法论 | 一句话描述 | 最佳场景 | Reference |
| --- | --- | --- | --- |
| **RICE Scoring** | Reach×Impact×Confidence÷Effort 量化优先级 | 产品路线图排序、需求优先级 | `rice.md` |
| **Eisenhower Matrix** | 重要性×紧迫性 四象限时间管理 | 个人/团队任务管理、资源分配 | `eisenhower.md` |
| **OKR** | Objectives + Key Results 目标拆解体系 | 季度/年度目标制定、团队对齐 | `okr.md` |
| **Pre-mortem & Counterfactual** | 逆向想象失败场景，预演风险并识别关键变量 | 重大决策前、项目启动、投资评估 | `premortem-counterfactual.md` |
| **Decision Matrix** | 多方案多标准加权评分，将选择量化 | 技术选型、策略选择、候选人评估 | `decision-matrix.md` |
| **MoSCoW Method** | Must/Should/Could/Won't 四级需求裁剪 | 范围管理、需求分类、Sprint规划 | `moscow.md` |
| **FMEA** | 严重度×频度×探测度 排序失效风险 | 产品/流程风险识别、质量工程、安全关键系统 | `fmea.md` |
| **Death Filter** | “如果这是最后一个决策”存在主义过滤器 | 重大人生决策、职业选择、创业方向选择 | `death-filter.md` |
| **Risk Matrix** | 概率×影响 2 维快速风险评估与排序 | 项目启动风险筛选、战略规划风险扫描、技术选型风险对比 | `risk-matrix.md` |

## 各方法论最低信息需求

- **RICE**：需要候选项列表 + 基本量级认知
- **OKR**：需要明确的时间周期和负责主体
- **Pre-mortem**：需要已有明确计划/决策方案
- **Decision Matrix**：需要至少 3 个备选方案 + 评估标准列表
- **MoSCoW**：需要需求列表 + 利益相关者参与
- **FMEA**：需要系统/流程的组件分解
- **Death Filter**：需要重大不可逆决策 + 候选选项（不适用于日常/紧急决策）
- **Eisenhower Matrix**：需要待分类的任务清单（个人/团队任务管理）
- **Risk Matrix**：需要已识别风险列表 + 概率/影响刻度定义

## 路由触发信号

- "功能/需求优先级排序" → RICE Scoring（主）⚡ 若评估维度需自定义（非 R/I/C/E）→用 Decision Matrix；若需 30 分钟内快速粗筛→用 ICE
- "个人/团队任务管理" → Eisenhower Matrix（主）
- "目标制定与追踪" → OKR（主）
- "重大决策前风险预演" → Pre-mortem & Counterfactual（主）
- "多方案多标准选型（评估维度需自定义）" → Decision Matrix（主）⚡ 若评估维度固定为 Reach/Impact/Confidence/Effort→用 RICE
- "需求裁剪/范围管理" → MoSCoW Method（主）
- "系统性风险识别/失效模式分析" → FMEA（主）
- "重大人生决策/职业选择/创业方向（价值型决策）" → Death Filter（主）
- "快速风险评估/风险排序/风险全景扫描" → Risk Matrix（主）

## 常见组合

- **重大决策**：苏格拉底提问（澄清假设）→ Decision Matrix → Pre-mortem（风险审查）
- **需求全流程管理**：Kano（分类性质）→ MoSCoW（裁剪范围）→ RICE（排优先级）
- **风险全面评估**：FMEA（系统化识别）→ Pre-mortem（想象式补充）→ Second-Order Thinking（连锁效应）
- **重大人生/创业决策**：Death Filter（过滤真实倾向）→ Pre-mortem（预演选定方向风险）→ Second-Order Thinking（长期效应）
- **项目启动风险评估**：Pre-mortem（识别风险）→ Risk Matrix（量化排序）→ FMEA（高风险项深度分析）
- **技术选型风险**：Decision Matrix（方案对比）→ Risk Matrix（风险排序）→ Second-Order Thinking（连锁效应）

## 相似方法论消歧决策树

当用户意图在以下方法论之间模糊时，按决策树消歧：

```
"多选项评估排序"
  ├─ 评估维度已固定为 Reach/Impact/Confidence/Effort？
  │   └─ 是 → RICE Scoring
  ├─ 评估维度需要自定义？（如技术选型的性能/成本/风险）
  │   └─ 是 → Decision Matrix
  └─ 需要 30 分钟内快速粗筛，不需要精确量化？
      └─ 是 → ICE Framework

"任务/需求排序"
  ├─ 是个人/团队日常任务管理？
  │   └─ 是 → Eisenhower Matrix
  ├─ 是产品功能/需求优先级？
  │   └─ 是 → RICE Scoring
  └─ 是需求范围裁剪（做/不做）？
      └─ 是 → MoSCoW Method

"风险评估"
  ├─ 已有明确计划，需预演失败场景？
  │   └─ 是 → Pre-mortem
  ├─ 需系统化识别失效模式？
  │   └─ 是 → FMEA
  └─ 需快速风险全景扫描与排序？
      └─ 是 → Risk Matrix
```

## 方法论互斥与先后约束

| 约束对 | 规则 | 原因 |
| --- | --- | --- |
| RICE ↔ ICE | **ICE 粗筛后→RICE 精排**，不要并行使用 | ICE 是 RICE 的简化版，并行使用产生冗余输出 |
| RICE vs Decision Matrix | **按评估维度选择**：固定 R/I/C/E→RICE；自定义维度→Decision Matrix | 核心差异在于维度是否固定，输入结构相似但用途不同 |
| FMEA → Pre-mortem | **FMEA 先于 Pre-mortem**（风险全面评估场景） | FMEA 系统化识别，Pre-mortem 作为想象式补充 |
