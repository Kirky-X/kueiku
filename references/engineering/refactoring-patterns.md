# Refactoring Patterns · 系统化重构手法

## 核心思想
重构是在不改变外部行为的前提下改善代码内部结构。关键前提：必须有测试保护——没有测试的重构是"冒险"。重构不是一次性大工程，而是每次提交代码时的小步改善（Boy Scout Rule：离开时比来时更干净）。

## 适用场景
- 遗留代码的渐进式改善
- 代码异味（Code Smell）的系统化消除
- 大函数/大类的职责拆分
- 设计模式的渐进式引入（而非一开始就过度设计）

## 关键步骤

### 前置条件
1. **必须有测试**：重构前确认关键路径有测试覆盖
2. **小步前进**：每步重构后跑测试，确认不破坏行为
3. **一次只做一件事**：不要同时重命名 + 提取函数 + 改逻辑

### 代码异味 → 重构手法对照表

**1. 过大函数（Long Method）**
- **Extract Function**：将一段代码提取为独立函数，函数名表达意图
- **Replace Temp with Query**：将临时变量替换为函数调用
- **Introduce Parameter Object**：将多个参数合并为对象
- 目标：函数长度 < 20 行，做且只做一件事

**2. 过大类（Large Class）**
- **Extract Class**：将相关字段和方法提取到新类
- **Extract Interface**：为类提取接口，降低耦合
- 目标：类职责单一，可通过类名理解其用途

**3. 重复代码（Duplicated Code）**
- **Extract Function**：将重复代码提取为公共函数
- **Pull Up Method**：将子类中的相同方法上移到父类
- **Template Method**：将相同流程上移，差异部分留给子类实现
- 目标：同一逻辑只存在一处（DRY）

**4. 过长参数列表（Long Parameter List）**
- **Introduce Parameter Object**：将参数组合为对象
- **Replace Parameter with Method**：参数可通过调用对象获得时，移除参数
- 目标：参数 ≤ 3 个，超过则考虑封装

**5. 条件表达式复杂（Complex Conditional）**
- **Decompose Conditional**：将条件分支提取为语义清晰的函数
- **Replace Conditional with Polymorphism**：用多态替代条件判断
- **Replace Nested Conditional with Guard Clauses**：用卫语句减少嵌套
- 目标：条件逻辑一目了然，无需注释解释

**6. 过度耦合（Feature Envy / Inappropriate Intimacy）**
- **Move Method**：将方法移到它最常调用的数据所在的类
- **Replace Dependency with Factory**：将对象创建委托给工厂
- 目标：类只关心自己的数据（Tell, Don't Ask）

**7. 命名不清（Mysterious Name）**
- **Rename Variable / Function / Class**：用业务语言命名
- 目标：名称即文档，无需注释解释"这是什么"

### 重构安全网
1. **测试覆盖**：重构前确认关键路径有测试
2. **小步提交**：每步重构后提交，方便回滚
3. **IDE 支持**：使用 IDE 的自动化重构功能（Rename / Extract / Inline）
4. **类型系统**：强类型语言的重构安全性远高于弱类型
5. **CI 验证**：PR 合并后 CI 自动跑全量测试

### 反模式警告
- **大爆炸重构**：一次性重写整个模块 → 高风险，应渐进式
- **无测试重构**：没有测试保护就重构 → 无法确认行为不变
- **重构中加功能**：重构的同时改逻辑 → 两类变更混在一起，出问题无法定位
- **完美主义**：追求"完美设计"而过度重构 → 够用就好

## 来源
Martin Fowler《Refactoring: Improving the Design of Existing Code》(1999, 2018 第二版)；Kent Beck《Implementation Patterns》(2007)
