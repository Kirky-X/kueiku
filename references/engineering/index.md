# Engineering · 编程与架构

**适用场景**：测试驱动开发、小步可执行计划、服务契约设计、Agent 友好度评估

## 编程方法论

| 方法论 | 一句话描述 | 最佳场景 | Reference |
| --- | --- | --- | --- |
| **TDD Red-Green-Refactor** | Red(写测试→失败)→Green(最简实现→通过)→Refactor(清理→保持绿) | 回归 bug 频发、重构缺安全网 | `tdd-red-green-refactor.md` |
| **Bite-Sized Plan** | 每步 2-5 分钟 + No Placeholders + exact file paths + Self-Review 三查 | agent/人类都能照做的计划 | `bite-sized-plan.md` |

## 架构方法论

| 方法论 | 一句话描述 | 最佳场景 | Reference |
| --- | --- | --- | --- |
| **Typed Service Contracts** | Spec&Handler + Design by Contract + Result Monad + Parse don't validate | 服务边界契约设计、边界错误防御 | `typed-service-contracts.md` |
| **Agent DX / CLI Scale** | 7 轴 0-3 评分：Machine-Readable/Raw Payload/Schema/Context/Hardening/Safety/Knowledge | CLI/SDK 的 agent 友好度评估 | `agent-dx-cli-scale.md` |

## 各方法论最低信息需求

- **TDD Red-Green-Refactor**：需要可运行的测试框架
- **Bite-Sized Plan**：需要任务拆解能力 + 文件路径明确性
- **Typed Service Contracts**：需要服务边界识别 + 类型系统支持
- **Agent DX / CLI Scale**：需要待评估的 CLI/SDK + 7 维度打分能力

## 路由触发信号

- "测试驱动开发" → TDD Red-Green-Refactor（主）
- "小步可执行计划" → Bite-Sized Plan（主）
- "服务边界契约设计" → Typed Service Contracts（主）
- "Agent 友好度评估" → Agent DX / CLI Scale（主）
