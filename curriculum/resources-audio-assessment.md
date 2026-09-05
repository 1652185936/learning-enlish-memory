# Interchange音频与测评资源映射

- 最近核验：2026-09-05
- 用途：让计划、语音教学和学习记录能够准确引用本地原始资源，而不把版权材料复制进仓库。

## Classroom Audio

音频文件名已直接编码级别、单元、学生书印刷页、练习号、活动类型和Part。例如：

`IC5_L0_Unit 01 Pg 002 Ex 01 Conversation Pt A.mp3`

使用时应以文件名为准，不重新编造轨号。

| 级别 | 归档文件 | 真实可播放MP3 | 总时长 | 覆盖 |
|---|---|---:|---:|---|
| Intro | `Interchange Intro Level Classroom Audio_20190814_193143.zip` | 186 | 219.582分钟 | U1-16及8次PC |
| Level 1 | `Interchange 1 Level Classroom Audio.zip` | 152 | 约174.2分钟 | U1-16及8次PC |
| Level 2 | `Interchange 2 Level Classroom Audio.zip` | 158 | 约211.6分钟 | U1-16及有声PC项目 |
| Level 3 | `Interchange 3 Level Classroom Audio.zip` | 141 | 约191.2分钟 | U1-16及8组PC；9个PC音频文件（U11-12分为Part A/B） |

Level 3 ZIP另含一个280字节的`__MACOSX/._...mp3`元数据文件，不应播放或计数。

### Intro每单元音频数量

| 单元 | MP3数 | 文件名前缀 | 学生书印刷页 |
|---|---:|---|---:|
| 1 | 16 | `IC5_L0_Unit 01` | 2-7 |
| 2 | 12 | `IC5_L0_Unit 02` | 8-13 |
| 3 | 12 | `IC5_L0_Unit 03` | 16-21 |
| 4 | 11 | `IC5_L0_Unit 04` | 22-27 |
| 5 | 12 | `IC5_L0_Unit 05` | 30-35 |
| 6 | 10 | `IC5_L0_Unit 06` | 36-41 |
| 7 | 10 | `IC5_L0_Unit 07` | 44-49 |
| 8 | 9 | `IC5_L0_Unit 08` | 50-55 |
| 9 | 9 | `IC5_L0_Unit 09` | 58-63 |
| 10 | 10 | `IC5_L0_Unit 10` | 64-69 |
| 11 | 11 | `IC5_L0_Unit 11` | 72-77 |
| 12 | 11 | `IC5_L0_Unit 12` | 78-83 |
| 13 | 10 | `IC5_L0_Unit 13` | 86-91 |
| 14 | 12 | `IC5_L0_Unit 14` | 92-97 |
| 15 | 11 | `IC5_L0_Unit 15` | 100-105 |
| 16 | 12 | `IC5_L0_Unit 16` | 106-111 |

另有8个双单元Progress Check MP3，文件名前缀为`IC5_L0_Unit 01-02 PC`至`IC5_L0_Unit 15-16 PC`。

## Assessment Program

每个级别的ZIP有94个实际文件：46 PDF、36 DOC、12 MP3。

| 检查点 | 使用材料 | 建议时长 | 记录要求 |
|---|---|---:|---|
| 每个单元第4课 | Oral Question Bank中该单元题目 | 10-15分钟 | 保存首次回答、提示程度及五维评分 |
| 每两个单元 | 对应Written Quiz的可执行非听力部分；另做已核验Progress Check内容卡 | 约35分钟 | 保存已答项目首次结果；Assessment听力跳过、不评分 |
| Units 1-8结束 | Half-book Test 1-8 A当前可执行的非听力部分 | 以实际为准 | 保存“已答得分/已答总分”；听力跳过；B卷留作延迟复测 |
| Units 9-16结束 | Half-book Test 9-16 A当前可执行的非听力部分 | 以实际为准 | 保存“已答得分/已答总分”；听力跳过；B卷留作延迟复测 |

### 口试评分

按照官方Scoring Sheet分别记录：

1. 理解；
2. 流利度；
3. 语法；
4. 词汇；
5. 发音。

每项0-5。总分只能来自真实口试，不得由教师印象补写。

### 音轨编号警告

Assessment中MP3文件名与脚本纸面轨号不是同一编号：

- U1-2 Written Quiz：文件名`Track01`，脚本写Track 2；之后依次相差1。
- U15-16 Written Quiz：文件名`Track08`，脚本写Track 9。
- U1-8 Test A/B：文件名`Track09/10`，脚本写Track 10/11。
- U9-16 Test A/B：文件名`Track11/12`，脚本写Track 12/13。

永远按“级别 + 测评名称 + 同一文件夹”配对。

## 语音模式如何使用

1. 先读`VOICE_CONTEXT.md`、当前单元文件和该单元的[听力内容卡](interchange-intro-5e/listening/README.md)。
2. 每项教材听力必须先选定已核验的`listening_ref`；不要求学习者查找、打开、播放或上传本地MP3。
3. AI语音只能按内容卡中已核验的内容顺序和固定事实重现，不得根据单元主题自行编造姓名、数字、事件或答案。
4. 第一遍不显示答案；先记录主旨和细节结果。第二遍与第一遍结果分开。
5. 最后才用内容卡中已核验的教师书脚本或答案订正。
6. 统一记录`audio_mode: source_grounded_ai`和`listening_ref`；这不等于播放了出版社原录音，也不计为原版录音成绩。没有已核验引用时不执行、不评分。

Assessment的12个MP3目前只有[配对元数据索引](interchange-intro-5e/listening/assessment-audio-index.md)，没有公开可呈现的内容卡。因此Written Quiz与Half-book Test的听力项目统一保持`audio_mode: none`；不得用课堂单元卡或自由生成内容代替。

## 第四版Video Resource Book

现有四本Video Resource Book均为©2012第四版，且目录中没有视频文件。可使用其中的背景词汇、预测、脚本改编和角色扮演，但不能：

- 把它们称为第五版视频；
- 沿用为第五版学生书精确页码或答案；
- 把阅读脚本或AI朗读计为真实视频理解成绩。
