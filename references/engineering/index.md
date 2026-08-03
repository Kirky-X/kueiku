# Engineering · 编程与架构

**适用场景**：测试驱动开发、小步可执行计划、服务契约设计、Agent 友好度评估、代码审查、架构设计、CI/CD、可观测性、领域驱动设计、性能优化、安全设计、API 设计、数据库设计、故障响应、Git 工作流、依赖管理、微服务、重构

## 编程方法论

| 方法论 | 一句话描述 | 最佳场景 | Reference |
| --- | --- | --- | --- |
| **TDD Red-Green-Refactor** | Red(写测试→失败)→Green(最简实现→通过)→Refactor(清理→保持绿) | 回归 bug 频发、重构缺安全网 | `tdd-red-green-refactor.md` |
| **Bite-Sized Plan** | 每步 2-5 分钟 + No Placeholders + exact file paths + Self-Review 三查 | agent/人类都能照做的计划 | `bite-sized-plan.md` |
| **Code Review Checklist** | 安全/架构/性能/可维护性四维度清单驱动审查 | PR 合并前质量门禁、重构影响评估 | `code-review-checklist.md` |
| **Refactoring Patterns** | 代码异味→重构手法对照表 + 测试保护下的小步改善 | 遗留代码改善、大函数/大类拆分 | `refactoring-patterns.md` |
| **Git Workflow Strategies** | Trunk-Based / GitHub Flow / Git Flow / GitLab Flow 策略选择矩阵 | 团队分支策略选择、多环境发布流程 | `git-workflow-strategies.md` |
| **Dependency Management** | 引入评估 + 版本策略 + 安全监控 + 健康度审计 | 依赖选型、漏洞响应、依赖健康度审计 | `dependency-management.md` |

## 架构方法论

| 方法论 | 一句话描述 | 最佳场景 | Reference |
| --- | --- | --- | --- |
| **Typed Service Contracts** | Spec&Handler + Design by Contract + Result Monad + Parse don't validate | 服务边界契约设计、边界错误防御 | `typed-service-contracts.md` |
| **Agent DX / CLI Scale** | 7 轴 0-3 评分：Machine-Readable/Raw Payload/Schema/Context/Hardening/Safety/Knowledge | CLI/SDK 的 agent 友好度评估 | `agent-dx-cli-scale.md` |
| **Clean Architecture** | 依赖反转分层 + Port & Adapter + 领域层零外部依赖 | 新项目架构设计、框架/数据库替换 | `clean-architecture.md` |
| **Domain-Driven Design** | 限界上下文 + 聚合根 + 统一语言 + 事件风暴 | 复杂业务系统建模、微服务边界划分 | `domain-driven-design.md` |
| **Microservices Patterns** | Saga/CQRS/Event Sourcing + 服务治理 + 弹性模式 | 单体拆分、分布式数据一致性、服务治理 | `microservices-patterns.md` |
| **API Design** | RESTful/GraphQL/gRPC 选型 + 版本管理 + 幂等性 + 错误响应 | 接口设计、API 规范化、版本兼容 | `api-design.md` |
| **Database Schema Design** | 数据建模 + 索引策略 + 安全迁移 + 规范化/反规范化 | 新项目数据模型、Schema 重构、查询优化 | `database-schema-design.md` |

## 流程方法论

| 方法论 | 一句话描述 | 最佳场景 | Reference |
| --- | --- | --- | --- |
| **CI/CD Pipeline Design** | 7 阶段流水线（Trigger→Build→Test→Security→Quality→Deploy→Post-Deploy）+ 门禁 + 回滚 | 流水线搭建、发布策略设计、质量门禁 | `cicd-pipeline-design.md` |
| **Security by Design** | STRIDE 威胁建模 + 安全编码模式 + CI 持续验证 | 安全架构设计、合规要求、安全加固 | `security-by-design.md` |
| **Observability** | Logs + Metrics + Traces 三支柱协同 + SLO 驱动告警 | 生产故障排查、分布式系统追踪、容量规划 | `observability.md` |
| **Performance Optimization** | 度量→定位→优化→验证循环 + 瓶颈分层 + 反模式警告 | 性能排查、基线建立、资源成本优化 | `performance-optimization.md` |
| **Incident Response & Postmortem** | 检测→响应→缓解→修复 + 无责复盘 + Action Item 闭环 | 生产故障应急、On-Call 流程建设、经验沉淀 | `incident-response-postmortem.md` |

## 各方法论最低信息需求

- **TDD Red-Green-Refactor**：需要可运行的测试框架
- **Bite-Sized Plan**：需要任务拆解能力 + 文件路径明确性
- **Code Review Checklist**：需要待审查的 PR/MR + 项目架构上下文
- **Refactoring Patterns**：需要待重构代码 + 测试覆盖
- **Git Workflow Strategies**：需要团队规模 + 发布节奏 + CI/CD 成熟度
- **Dependency Management**：需要项目依赖清单 + 安全扫描工具
- **Typed Service Contracts**：需要服务边界识别 + 类型系统支持
- **Agent DX / CLI Scale**：需要待评估的 CLI/SDK + 7 维度打分能力
- **Clean Architecture**：需要业务领域分析 + 技术栈约束
- **Domain-Driven Design**：需要业务专家参与 + 领域知识
- **Microservices Patterns**：需要现有系统架构 + 团队组织结构
- **API Design**：需要 API 使用场景 + 消费方需求
- **Database Schema Design**：需要业务实体关系 + 查询模式
- **CI/CD Pipeline Design**：需要项目类型 + 部署环境 + 团队规模
- **Security by Design**：需要系统数据流图 + 合规要求
- **Observability**：需要系统架构 + SLA/SLO 定义
- **Performance Optimization**：需要性能基线数据 + SLO 目标
- **Incident Response & Postmortem**：需要故障时间线 + 监控数据

## 路由触发信号

- "测试驱动开发" → TDD Red-Green-Refactor（主）
- "小步可执行计划" → Bite-Sized Plan（主）
- "代码审查/Code Review/PR 审查" → Code Review Checklist（主）
- "重构/代码异味/清理代码" → Refactoring Patterns（主）
- "Git 分支策略/工作流/发布流程" → Git Workflow Strategies（主）
- "依赖管理/依赖选型/依赖漏洞/依赖审计" → Dependency Management（主）
- "服务边界契约设计" → Typed Service Contracts（主）
- "Agent 友好度评估" → Agent DX / CLI Scale（主）
- "架构设计/分层/六边形/洋葱架构" → Clean Architecture（主）
- "领域驱动/DDD/限界上下文/事件风暴/聚合根" → Domain-Driven Design（主）
- "微服务/分布式系统/Saga/CQRS/服务治理" → Microservices Patterns（主）
- "API 设计/RESTful/GraphQL/gRPC/接口设计" → API Design（主）
- "数据库设计/Schema/索引/数据建模/迁移" → Database Schema Design（主）
- "CI/CD/流水线/持续集成/持续部署/发布策略" → CI/CD Pipeline Design（主）
- "安全设计/威胁建模/STRIDE/安全编码" → Security by Design（主）
- "可观测性/监控/日志/链路追踪/告警" → Observability（主）
- "性能优化/性能排查/延迟/吞吐量" → Performance Optimization（主）
- "故障响应/On-Call/Postmortem/复盘" → Incident Response & Postmortem（主）
