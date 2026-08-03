# Clean Architecture · 整洁架构与六边形架构

## 核心思想
软件系统应按依赖反转原则分层——外层依赖内层，内层不知道外层的存在。业务逻辑（Domain）在最内层，不依赖任何框架、数据库、UI 或外部服务。所有跨层通信通过接口（Port）+ 适配器（Adapter）实现，让核心业务可独立测试、可替换技术栈。

## 适用场景
- 新项目架构设计或大型重构
- 框架/数据库替换需要最小化影响
- 业务逻辑复杂，需要与技术细节解耦
- 团队协作中需要清晰的模块边界

## 关键步骤

### 分层模型（由内到外）

1. **Domain Layer（领域层）**
   - 实体（Entity）：业务对象，包含业务规则
   - 值对象（Value Object）：不可变的业务概念
   - 领域事件（Domain Event）：业务中发生的有意义的事
   - 领域服务（Domain Service）：不属于单个实体的业务逻辑
   - **规则**：零外部依赖，纯业务语言

2. **Application Layer（应用层）**
   - 用例（Use Case）：编排业务流程
   - 端口（Port）：定义输入/输出接口（驱动端口 + Driven 端口）
   - DTO / Command / Query：跨层数据传输对象
   - **规则**：只依赖 Domain Layer，不依赖框架

3. **Infrastructure Layer（基础设施层）**
   - 适配器（Adapter）：实现 Application 层定义的端口
   - 驱动适配器：HTTP Controller、CLI Handler、消息消费者
   - 被驱动适配器：数据库 Repository、外部 API Client、消息生产者
   - **规则**：实现接口，不暴露给 Domain/Application

### 设计原则
1. **依赖规则**：所有依赖指向内层（Domain），外层可替换
2. **Port & Adapter**：每个外部交互通过接口隔离，便于测试替身
3. **单一职责分层**：每层只做自己层级的事——Domain 不碰 I/O，Application 不碰框架
4. **显式边界**：层间通过接口通信，禁止跨层直接调用
5. **可测试性**：Domain 层可脱离框架独立单元测试

### 实施检查
- Domain 层是否 import 了框架/数据库/HTTP 库？→ 违规
- Application 层是否知道用的是 REST 还是 gRPC？→ 违规
- 能否删掉 Infrastructure 层而 Domain + Application 仍编译通过？→ 应该可以

## 来源
Robert C. Martin《Clean Architecture》(2017)；Alistair Cockburn 六边形架构 (2005)；Jeffrey Palermo Onion Architecture (2008)
