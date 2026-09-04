# 字段与状态约定

## 每日记录状态

| 值 | 含义 |
|---|---|
| `planned` | 已安排，未确认开始 |
| `in_progress` | 已开始，未确认完成 |
| `completed` | 已确认完成 |
| `skipped` | 未执行 |

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
