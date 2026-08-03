# Git Workflow Strategies · Git 分支与工作流策略

## 核心思想
分支策略是团队协作的骨架——它决定了谁在什么时候可以合并什么代码。没有"最好"的策略，只有最匹配团队规模和发布节奏的策略。核心原则：主干保持可发布、合并冲突最小化、发布可追溯。

## 适用场景
- 团队选择或调整 Git 分支策略
- 多环境（dev/staging/prod）发布流程设计
- 代码合并冲突频繁的团队优化协作流程
- CI/CD 流水线与分支策略对齐

## 关键步骤

### 策略选择矩阵

| 策略 | 团队规模 | 发布节奏 | 复杂度 | 最佳场景 |
| --- | --- | --- | --- | --- |
| **Trunk-Based** | 5-50 人 | 持续部署（每天多次） | 低 | 成熟 CI/CD、Feature Flag 体系 |
| **GitHub Flow** | 3-30 人 | 每天~每周 | 低 | 开源项目、SaaS 持续交付 |
| **Git Flow** | 10-100 人 | 定期发布（每 2 周~月） | 高 | 有版本号的桌面/移动应用 |
| **GitLab Flow** | 5-50 人 | 每周~每 2 周 | 中 | 多环境部署、需要环境分支 |

### 各策略核心规则

**1. Trunk-Based Development**
- 所有人直接向 `main` 提交短生命周期分支（< 1 天）
- Feature Flag 控制未完成功能——代码可合并但功能不可见
- 必须有小粒度提交 + 快速 CI 反馈
- Release 通过 tag 标记，从 main 切出 release 分支仅做 hotfix

**2. GitHub Flow**
- `main` 始终可部署
- 从 main 切 feature 分支 → 开发 → 开 PR → Review → 合并回 main
- 合并即部署（或手动触发部署）
- 无 release 分支——通过 tag 标记版本

**3. Git Flow**
- `main`：生产代码，只接受 merge，永远保持 tag
- `develop`：集成分支，日常开发合并到这里
- `feature/*`：从 develop 切出，完成后合并回 develop
- `release/*`：从 develop 切出，冻结功能只做 bugfix，完成后合并到 main + develop
- `hotfix/*`：从 main 切出，修复后合并到 main + develop

**4. GitLab Flow（环境分支）**
- `main` 是上游
- 环境分支：`pre-production`、`production`
- 代码从 main → pre-production → production 单向合并
- 功能分支从 main 切出，PR 合并回 main

### 通用最佳实践
1. **提交规范**：Conventional Commits（`feat:` / `fix:` / `docs:` / `refactor:`）
2. **PR 粒度**：单个 PR 做一件事，< 400 行变更
3. **保护分支**：main / develop 禁止 force push，必须通过 PR + Review
4. **合并策略**：Feature 分支用 Squash Merge 保持 main 历史干净；Release 分支用 Merge Commit 保留上下文
5. **Tag 规范**：语义化版本（SemVer）`vMAJOR.MINOR.PATCH`

## 来源
GitHub 官方文档（GitHub Flow）；Vincent Driessen（Git Flow, 2010）；Atlassian Git Workflow 指南；Trunk Based Development (trunkbaseddevelopment.com)
