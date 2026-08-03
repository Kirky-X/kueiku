# Security by Design · 安全左移设计

## 核心思想
安全不是上线前补的检查项，而是设计阶段就内建的属性。将安全实践前移到需求分析和架构设计阶段（Shift Left），通过威胁建模识别攻击面，通过安全编码模式消除常见漏洞，通过自动化扫描持续验证。修复设计阶段的安全问题成本是修复生产环境问题的 1/30。

## 适用场景
- 新项目安全架构设计
- 敏感数据处理系统（PII/支付/医疗）
- 合规要求（SOC2 / ISO 27001 / GDPR）
- 安全事件后的系统性加固

## 关键步骤

### 1. 威胁建模（Threat Modeling）

在架构设计阶段执行，使用 **STRIDE** 模型识别威胁：

| 威胁类型 | 含义 | 防御手段 |
| --- | --- | --- |
| **S**poofing（仿冒） | 冒充用户/系统身份 | 认证 + 多因素验证 |
| **T**ampering（篡改） | 未授权修改数据/代码 | 完整性校验 + 签名 |
| **R**epudiation（抵赖） | 否认执行过的操作 | 审计日志 + 数字签名 |
| **I**nformation Disclosure（信息泄露） | 暴露敏感信息 | 加密 + 最小权限 |
| **D**enial of Service（拒绝服务） | 使系统不可用 | 限流 + 熔断 + 冗余 |
| **E**levation of Privilege（权限提升） | 获取未授权的权限 | 最小权限 + 零信任 |

**执行步骤**：
1. 画出数据流图（DFD）：外部实体 → 进程 → 数据存储 → 数据流
2. 对每个组件应用 STRIDE 六维度检查
3. 为每个威胁分配风险等级（DREAD：Damage/Reproducibility/Exploitability/Affected Users/Discoverability）
4. 定义缓解措施，纳入开发任务

### 2. 安全编码模式

**输入验证**
- 白名单优于黑名单——只允许已知安全输入
- 服务端验证不可绕过（客户端验证仅提升体验）
- 参数化查询杜绝 SQL 注入
- 输出编码防 XSS（HTML 实体编码 / CSP Header）

**认证与授权**
- 密码存储：bcrypt / argon2（禁止 MD5/SHA1）
- Session/Token：安全存储、过期机制、刷新策略
- 权限模型：RBAC / ABAC，默认拒绝（Default Deny）
- API 鉴权：每个端点独立检查，不依赖前端隐藏

**数据保护**
- 传输加密：TLS 1.2+（禁止 SSLv3/TLS 1.0）
- 存储加密：敏感字段 AES-256 加密
- 密钥管理：使用 KMS/Vault，禁止硬编码
- 日志脱敏：PII/凭证/Token 不进入日志

**依赖安全**
- 定期扫描依赖漏洞（Snyk / Dependabot / Trivy）
- 锁定依赖版本，使用 lockfile
- 最小化依赖面——引入新依赖前评估维护状态

### 3. 持续验证
- CI 集成 SAST（Semgrep / CodeQL）——每次 PR 扫描
- CI 集成密钥检测（gitleaks）——防止凭证泄露
- 定期渗透测试——至少每年一次或重大变更后
- 安全事件响应流程：检测 → 遏制 → 根因 → 修复 → 复盘

## 来源
OWASP Top 10 (2021)；Microsoft STRIDE 框架；Adam Shostack《Threat Modeling》(2014)；NIST Cybersecurity Framework
