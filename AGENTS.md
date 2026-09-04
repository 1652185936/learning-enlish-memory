# Repository Instructions

## Purpose

This repository is the durable source of truth for one learner's English-learning history. Use it to continue learning from verified evidence instead of starting from zero in each conversation.

## Sources of truth

| Information | Source |
|---|---|
| Stable goals, level, preferences, and constraints | `profile/learner.md` |
| Current targets and study rhythm | `plans/` |
| What actually happened in a study session | `progress/daily/` |
| Derived totals and current skill picture | `progress/dashboard.md` |
| Reusable language knowledge | `knowledge/` |
| Unresolved recurring errors | `mistakes/` |
| Due dates, review outcomes, and mastered items | `review/` |
| Repository behavior and formats | `system/` |

## Non-negotiable rules

1. Never invent study time, scores, completed exercises, proficiency, mistakes, or mastery.
2. Use `Asia/Dubai` for dates and time. Use ISO dates: `YYYY-MM-DD`.
3. Keep one daily file per date at `progress/daily/YYYY/YYYY-MM-DD.md`.
4. A planned activity is not a completed activity. Only confirmed completion changes totals.
5. Preserve historical evidence. If an old record is wrong, append a clearly dated correction instead of silently rewriting history.
6. Use stable error IDs such as `ERR-VOC-20260904-01`; never reuse an ID for another item.
7. Prefer small, relevant updates. Preserve unrelated content and user-authored notes.
8. Link summaries and claims back to daily records or other concrete evidence whenever possible.
9. If required information is missing, write `待确认` or ask the learner. Do not guess.

## Update workflows

### Save today's learning

1. Read the current profile, plans, dashboard, due reviews, active mistakes, and recent daily records.
2. Create or update today's one daily file from `system/templates/daily.md`.
3. Record only facts confirmed in the conversation or supplied evidence.
4. Update relevant knowledge and mistake files.
5. Schedule reviews when needed, then update the dashboard from confirmed data.

### Plan today's learning

1. Prioritize overdue reviews.
2. Then address active mistakes and the current weekly goal.
3. Create a daily entry with `status: planned` if a saved plan is requested.
4. Do not increase completed-session or duration totals until completion is confirmed.

### Produce a stage summary

1. Use the stage-summary template.
2. Link the relevant daily evidence.
3. Separate measured improvement from learner self-assessment.
4. Update the next plan only after recording remaining weak points.

When the learner explicitly asks to save, record, or update this repository, the request authorizes the corresponding repository change. Otherwise, inspect and advise without mutating records.
