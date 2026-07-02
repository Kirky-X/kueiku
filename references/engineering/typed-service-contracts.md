# Typed Service Contracts · 类型化服务契约

## 核心思想
服务边界处不要靠"约定 + 文档"——用 Spec & Handler 模式让契约成为可执行代码；用 Design by Contract 表达前置/后置条件；用 Result Monad 替代抛异常；用 Parse don't validate 让非法状态在编译期不可表达。把错误防御从运行时提到类型层。

## 适用场景
- 微服务/模块间接口频繁因"对方改了字段我没收到通知"出错
- 大量运行时 `if (data == null)` 防御代码
- 异常被滥用为控制流，调用方无法静态知道会失败

## 关键步骤
1. Spec & Handler 模式：把每个服务调用拆为 Spec（描述输入/输出/约束的类型）+ Handler（实现 Spec 的函数），Spec 是契约的 single source of truth
2. Design by Contract：在 Spec 中显式声明前置条件（pre）/后置条件（post）/不变量（inv），CI 检查 handler 是否满足
3. Result Monad：用 `Result<T, E>` 替代 throw，让"可能失败"在类型签名中显式，强制调用方处理
4. Parse don't validate：边界处一次性 parse 输入为强类型，内部代码不再做 null/格式检查——非法数据在边界即被拒绝
5. 契约版本化：Spec 变更需 bump 版本，老版本保留 N 个 release 周期
6. 自动生成文档与客户端 SDK：从 Spec 派生，杜绝文档与代码 drift

## 来源
design.md（typed-service-contracts 设计模式汇总）；理论根基见 Bertrand Meyer《Object-Oriented Software Construction》Design by Contract、Alexis King《Parse, don't validate》
