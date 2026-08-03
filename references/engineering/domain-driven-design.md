# DDD · 领域驱动设计

## 核心思想
复杂业务系统的设计不应从技术架构出发，而应从业务领域出发。通过限界上下文（Bounded Context）划分系统边界，用统一语言（Ubiquitous Language）消除业务与技术之间的歧义，让代码结构直接反映业务结构。核心产出不是文档，而是可执行的领域模型。

## 适用场景
- 业务逻辑复杂的大型系统（ERP/金融/医疗/供应链）
- 微服务边界划分——限界上下文即服务边界
- 团队沟通中业务与技术频繁产生歧义
- 遗留系统重构——从贫血模型恢复业务逻辑

## 关键步骤

### 战略设计（系统级）

1. **事件风暴（Event Storming）**
   - 识别领域事件（Domain Event）：业务中发生的不可变事实（用过去时态命名）
   - 识别触发命令（Command）：谁/什么触发了这个事件
   - 识别聚合（Aggregate）：命令作用的业务对象
   - 识别限界上下文（Bounded Context）：一组内聚的聚合
   - 定义上下文映射（Context Map）：上下文间的集成关系

2. **上下文映射模式**
   - **Partnership**：两个上下文协同演进
   - **Shared Kernel**：共享一小部分模型
   - **Customer-Supplier**：上游供应，下游消费
   - **Conformist**：下游完全遵从上游模型
   - **Anti-Corruption Layer (ACL)**：下游通过翻译层隔离上游模型
   - **Open Host Service / Published Language**：上游提供标准协议

### 战术设计（模型级）

3. **聚合（Aggregate）**
   - 聚合根（Aggregate Root）：外部唯一入口，保证一致性边界
   - 聚合内对象通过本地引用，聚合间通过 ID 引用
   - 一个事务只修改一个聚合

4. **实体（Entity）vs 值对象（Value Object）**
   - Entity：有唯一标识，生命周期内可变
   - Value Object：无标识，不可变，通过属性值相等判断

5. **领域服务（Domain Service）**
   - 不属于单个实体/值对象的业务操作
   - 无状态，操作领域对象

6. **领域事件（Domain Event）**
   - 记录业务中发生的重要事实
   - 命名用过去时态：`OrderPlaced`、`PaymentReceived`
   - 携带足够上下文，消费者无需回查

### 实施检查
- 代码中是否有统一语言？技术术语是否被排除在领域层外？
- 聚合边界是否清晰？跨聚合引用是否只通过 ID？
- 限界上下文之间是否有显式的映射关系？
- 领域逻辑是否在领域层？还是在 Application/Infrastructure 层？

## 来源
Eric Evans《Domain-Driven Design》(2003)；Vaughn Vernon《Implementing Domain-Driven Design》(2013)；Event Storming by Alberto Brandolini (2013)
