# API Design · API 设计原则

## 核心思想
API 是系统间通信的契约，设计质量直接决定集成效率和系统可维护性。好的 API 遵循最小惊讶原则——命名直觉正确、错误信息有用、版本演进平滑。将 API 视为产品来设计，而非技术接口的附属品。

## 适用场景
- RESTful API / GraphQL / gRPC 接口设计
- 微服务间内部 API 或面向第三方的公开 API
- API 版本管理和向后兼容策略
- 现有 API 的规范化改造

## 关键步骤

### 1. 风格选择

| 风格 | 最佳场景 | 优势 | 劣势 |
| --- | --- | --- | --- |
| **REST** | CRUD 为主的资源操作 | 简单、通用、缓存友好 | 复杂查询表达力弱 |
| **GraphQL** | 前端灵活查询、多端不同数据需求 | 客户端按需获取、无 over-fetching | 缓存复杂、N+1 风险 |
| **gRPC** | 内部微服务高性能通信 | 强类型、高性能、双向流 | 浏览器不友好、调试难 |

### 2. RESTful 设计原则

**资源建模**
- URL 用名词复数：`/users`、`/orders`（不用动词）
- 层级关系用路径表达：`/users/{id}/orders`
- 过滤/排序/分页用查询参数：`?status=active&sort=-created_at&page=2&limit=20`

**HTTP 方法语义**
| 方法 | 语义 | 幂等 | 安全 |
| --- | --- | --- | --- |
| GET | 读取 | 是 | 是 |
| POST | 创建 | 否 | 否 |
| PUT | 全量替换 | 是 | 否 |
| PATCH | 部分更新 | 是 | 否 |
| DELETE | 删除 | 是 | 否 |

**错误响应**
- 使用标准 HTTP 状态码：400（参数错误）/ 401（未认证）/ 403（无权限）/ 404（不存在）/ 409（冲突）/ 422（业务校验失败）/ 429（限流）/ 500（服务端错误）
- 响应体包含结构化错误信息：`{ "error": { "code": "VALIDATION_ERROR", "message": "...", "details": [...] } }`

**分页**
- 游标分页（Cursor）优于偏移分页（Offset）——大数据集性能稳定
- 返回分页元数据：`{ "data": [...], "pagination": { "cursor": "...", "has_more": true, "total": 100 } }`

**幂等性**
- POST 操作提供 `Idempotency-Key` Header
- PUT/PATCH 天然幂等
- DELETE 重复调用返回 404 或 204

### 3. 版本管理

| 策略 | 格式 | 适用场景 |
| --- | --- | --- |
| URL 路径 | `/v1/users` | 公开 API，变更明显 |
| Header | `Accept: application/vnd.api.v2+json` | 内部 API，URL 干净 |
| 查询参数 | `?api_version=2` | 简单但不推荐 |

- 新版本发布后，旧版本至少维护 2 个 release 周期
- 弃用提前通知（Deprecation Header + Sunset Header）
- Breaking Change 必须 bump major 版本

### 4. 文档与测试
- OpenAPI / Swagger 规范先行（API-first）
- 从规范自动生成文档和客户端 SDK
- 提供可交互的 API Playground
- 契约测试防止文档与实现 drift

## 来源
Roy Fielding 博士论文（REST 架构定义）；Google API Design Guide；Microsoft REST API Guidelines；Stripe API 设计实践
