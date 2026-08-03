# Observability · 可观测性三支柱

## 核心思想
系统出问题时不靠"加日志重新部署"来排查——通过日志（Logs）、指标（Metrics）、链路追踪（Traces）三支柱的协同设计，让系统行为在运行时可被外部观测和理解。可观测性 ≠ 监控，监控是"已知问题的告警"，可观测性是"探索未知问题的工具"。

## 适用场景
- 生产环境故障排查和根因定位
- 微服务/分布式系统的跨服务调用链追踪
- 性能瓶颈识别和容量规划
- SLA/SLO 定义和错误预算监控

## 关键步骤

### 三支柱设计

**1. Logs（日志）**
- **结构化日志**：JSON 格式，包含 timestamp / level / service / trace_id / span_id / message
- **日志级别规范**：ERROR（需立即处理）/ WARN（异常但可恢复）/ INFO（关键业务事件）/ DEBUG（开发调试）
- **关联**：每条日志必须包含 trace_id，可关联到完整调用链
- **脱敏**：禁止记录密码/Token/PII 等敏感信息
- **采样**：高流量服务使用自适应采样，避免日志撑爆存储

**2. Metrics（指标）**
- **四类黄金信号**：
  - Latency（延迟）：P50 / P95 / P99
  - Traffic（流量）：QPS / 并发连接数
  - Errors（错误）：错误率 = 错误请求 / 总请求
  - Saturation（饱和度）：CPU / 内存 / 连接池使用率
- **RED 方法**（面向请求）：Rate / Errors / Duration
- **USE 方法**（面向资源）：Utilization / Saturation / Errors
- **告警规则**：基于 SLO 的错误预算消耗速率，而非简单阈值

**3. Traces（链路追踪）**
- **Trace 结构**：一条 Trace = 多个 Span，每个 Span 记录服务名 / 操作名 / 开始时间 / 持续时间 / 状态
- **传播**：通过 HTTP Header（W3C Trace Context）或 gRPC Metadata 跨服务传播 trace_id
- **采样策略**：
  - 头部采样：固定比例（如 1%）
  - 尾部采样：保留错误/慢请求的完整 Trace
- **可视化**：Trace → Span 瀑布图，快速定位慢 Span

### 协同设计
1. **关联**：Logs 带 trace_id → 可从 Metric 告警 → 定位到 Trace → 展开到具体 Span → 关联到 Logs
2. **Dashboard**：以 SLO 为核心——错误预算消耗、延迟分布、流量趋势
3. **告警分级**：
   - P0（立即响应）：核心功能不可用 / 错误率 > SLO
   - P1（1 小时内）：性能降级 / 单点故障
   - P2（下个工作日）：非核心功能异常 / 容量预警
4. **On-Call 流程**：告警 → 确认 → 定位 → 缓解 → 根因修复 → Postmortem

## 来源
Google《Site Reliability Engineering》(2016)；Cindy Sridharan《Distributed Systems Observability》(2018)；OpenTelemetry 标准
