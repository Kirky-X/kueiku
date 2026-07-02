# Job Stories · 任务故事

## 核心思想
User Stories 用角色（"As a PM"）开篇，容易引导团队按用户身份思考；Job Stories 改用情境开篇，强制团队聚焦"在什么情况下，用户因为什么动机，想达成什么结果"——更贴近 JTBD 思想，避免 persona 偏见。

## 适用场景
- User Stories 写得像功能清单（"作为用户，我要一个导出按钮"）
- 同一功能被不同 persona 反复提，但本质是同一 Job
- 需求讨论陷入"用户是谁"而非"用户在什么情境下要做什么"

## 关键步骤
1. 用模板写：When [situation], I want to [motivation], so I can [expected outcome]
2. situation 要具体到场景（不是"作为管理员"，而是"当批量处理超过 1000 条记录时"）
3. motivation 是用户的内在动机，不是产品功能（不是"我要一个批量按钮"，而是"我想一次完成避免重复操作"）
4. expected outcome 是用户视角的成功（"节省时间"而非"系统返回 200"）
5. 每个 job story 拆出多个候选解决方案，避免锁定单一实现
6. 验收条件围绕 outcome 是否达成，而非功能是否实现

## 来源
Paul Adams（Intercom）；起源见 Alan Klement《When Coffee and Kale Compete》
