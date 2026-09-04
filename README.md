# English Learning Memory

这是一个长期英语学习记忆库，用来保存学习计划、真实学习记录、进度证据、薄弱点、复习安排和阶段总结。

它不是普通笔记仓库。它的工作方式是：每次学习都从历史记录出发，判断已经学过什么、哪些内容仍不稳定、现在最值得学习或复习什么。

## 当前状态

- 系统初始化日期：2026-09-04
- 时区：Asia/Dubai
- 学习者档案：待确认
- 英语基线水平：待确认
- 已确认学习次数：0
- 已确认学习时长：0 分钟
- 所有未知信息都会保留为“待确认”，不会凭空填写。

## 导航

- [语音学习入口](VOICE_CONTEXT.md)
- [学习者档案](profile/learner.md)
- [2026-09-04学习者自述基线](progress/baselines/2026-09-04-self-report.md)
- [课程内容库](curriculum/README.md)
- [教材资料清单](curriculum/sources.md)
- [Interchange 第五版 Level 1 课程地图](curriculum/interchange-level-1-5e/course-map.md)
- [年度计划](plans/yearly.md)
- [本月计划](plans/monthly/2026-09.md)
- [本周计划](plans/weekly/2026-W36.md)
- [进度总览](progress/dashboard.md)
- [每日记录说明](progress/daily/README.md)
- [第一个里程碑](progress/milestones/milestone-001.md)
- [知识库索引](knowledge/README.md)
- [待复习内容](review/due.md)
- [复习日志](review/review-log.md)
- [已掌握内容](review/mastered.md)
- [系统规则](system/rules.md)
- [记录模板](system/templates/README.md)
- [系统变更记录](system/changelog.md)

## 以后可以直接这样说

- “把今天的学习记录保存下来。”
- “根据我的历史进度安排今天学什么。”
- “记录这个错误，并安排复习。”
- “继续上次的英语学习。”
- “生成这个阶段的学习总结。”

## 工作流程

1. 语音学习先读取 `VOICE_CONTEXT.md`，再读取其中指定的当前单元。
2. 读取学习者档案、当前计划、进度、到期复习项、未解决错误和最近的每日记录。
3. 只记录对话或学习材料中真实出现的内容。
4. 将新知识放入知识库，将错误放入对应错误记录，并安排必要的复习。
5. 完成学习后更新每日记录和进度总览；仅有计划时不计为已完成。
6. 阶段结束后用可追溯的学习证据生成总结，再调整下一阶段计划。

详细的数据来源和更新约束见 [AGENTS.md](AGENTS.md) 与 [system/rules.md](system/rules.md)。
