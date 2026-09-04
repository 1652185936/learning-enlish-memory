# 字段与状态约定

## 每日记录状态

| 值 | 含义 |
|---|---|
| `planned` | 已安排，未确认开始 |
| `in_progress` | 已开始，未确认完成 |
| `completed` | 已确认完成 |
| `skipped` | 未执行 |

## 基线证据类型

| 值 | 含义 |
|---|---|
| `self_report` | 学习者描述的目标、场景、压力或习惯，不等同于能力测量 |
| `short_observed_sample` | 已保存的简短语言样本，只能支持对该样本本身的判断 |
| `assessment` | 在明确任务、条件和标准下取得的测评结果 |

基线信息保存在 `progress/baselines/`。若没有真实学习时长和已完成任务，基线整理不计为学习次数。

## 知识掌握状态

| 值 | 含义 |
|---|---|
| `new` | 首次确认接触 |
| `learning` | 能部分理解或使用 |
| `reviewing` | 正在通过间隔复习巩固 |
| `mastered` | 有跨日期、跨语境的稳定证据 |

## ID 格式

- 词汇错误：`ERR-VOC-YYYYMMDD-NN`
- 语法错误：`ERR-GRA-YYYYMMDD-NN`
- 口语错误：`ERR-SPK-YYYYMMDD-NN`
- 听力错误：`ERR-LIS-YYYYMMDD-NN`

同一 ID 始终指向同一问题。编号从当天 `01` 开始。

## 空值

未知但需要学习者确认的信息统一写 `待确认`。统计字段在确实没有记录时可写 `0`，不要把未知值当作零。

## 课程资料状态

| 值 | 含义 |
|---|---|
| `verified` | 已核对文件身份、相关页面和内容 |
| `partial` | 内容可用，但只覆盖整套资料的一部分 |
| `legacy-supplement` | 旧版资料，仅能按主题辅助匹配 |
| `corrupt` | 文件结构或页面损坏，不能作为可靠课程来源 |
| `missing` | 教材引用了该资源，但尚未收到文件 |

## 课程与学习状态分离

- 课程项目 ID：`IC5-L1-U01-G01`，依次表示课程、级别、单元、内容类型和编号。
- `curriculum/` 只表示教材中存在什么，不使用 `new`、`learning` 或 `mastered`。
- 单元学习状态使用 `no_evidence`、`started`、`covered`、`assessed`、`retained`。
- 只有每日记录提供的真实证据才能改变学习状态。
