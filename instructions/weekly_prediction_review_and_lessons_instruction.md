# Weekly Prediction Review And Lessons Instruction

## Purpose

Use this instruction after a forecast week has ended and the daily briefs for that forecast window already exist.

The goal is to:

- compare the weekly prediction against what actually happened
- score the prediction in a disciplined way
- identify forecasting mistakes and calibration issues
- create one weekly scorecard file
- append distilled lessons to one rolling master lessons file

This instruction is for forecast evaluation and self-correction.

## Output Files

For each review cycle, create or update these outputs:

- create one new file: `prediction_scorecard_YYYY-MM-DD_to_YYYY-MM-DD.md`
- update one rolling file: `prediction_lessons_master.md`

The scorecard file should match the forecast window being reviewed.

Example:

- if the forecast covered `2026-03-29` to `2026-04-04`
- create `prediction_scorecard_2026-03-29_to_2026-04-04.md`
- then append new distilled lessons to `prediction_lessons_master.md`

## Required Inputs

Always read:

1. The prediction file for the reviewed week
2. The pattern analysis file that informed that prediction
3. All 7 daily briefs covering the reviewed forecast window
4. Any existing `prediction_lessons_master.md`
5. The previous week's scorecard when useful for continuity

## Main Evaluation Principle

Score predictions against observable behavior, not against broad narrative impressions.

Good evaluation targets:

- whether attacks happened or did not happen
- whether maritime disruption widened, narrowed, or stayed stable
- whether mediation advanced, stalled, or collapsed
- whether new fronts opened
- whether force posture changed
- whether proxies activated, restrained, or shifted tempo

Bad evaluation targets:

- `we were directionally insightful overall`
- `the week felt escalatory`

## Evaluation Categories

Every major prediction should be classified into one of these:

- `Correct`
- `Partially Correct`
- `Wrong`
- `Missed Development`
- `Right Direction / Wrong Mechanism`

Use `Missed Development` for important developments that were not forecast at all.

Use `Right Direction / Wrong Mechanism` when the general direction was right but the actor, tool, theater, or pathway was wrong.

## Review Method

1. Break the prediction into discrete forecast claims.
2. Match each claim against the 7 daily briefs from the forecast window.
3. Judge the claim based on evidence, not hindsight framing.
4. Separate timing errors from logic errors.
5. Separate actor misreads from scenario misreads.
6. Identify which signals were over-weighted and under-weighted.
7. Convert mistakes into reusable lessons.

## Required Weekly Scorecard Output Format

Use this structure:

```md
# Prediction Scorecard - YYYY-MM-DD to YYYY-MM-DD

## Scope
- Forecast window reviewed: YYYY-MM-DD to YYYY-MM-DD
- Prediction file reviewed: `prediction_...`
- Pattern analysis file reviewed: `pattern_analysis_...`

## Executive Summary
- 4-8 bullets on what the forecast got right, wrong, and missed

## Forecast Quality Snapshot
| Category | Count | Notes |
|----------|-------|-------|
| Correct | X | |
| Partially Correct | X | |
| Wrong | X | |
| Missed Development | X | |
| Right Direction / Wrong Mechanism | X | |

## Detailed Scorecard
| Forecast Claim | Result | Evidence From Week | Why It Scored This Way |
|----------------|--------|--------------------|------------------------|

## Actor-By-Actor Review
### United States
- What was forecast
- What happened
- What was missed

### Israel
- What was forecast
- What happened
- What was missed

### Iran
- What was forecast
- What happened
- What was missed

### Hezbollah
- What was forecast
- What happened
- What was missed

### Iraqi Partner Forces
- What was forecast
- What happened
- What was missed

### Ansar Allah / Houthis
- What was forecast
- What happened
- What was missed

## Scenario Review
| Scenario | Original Probability | Outcome | Assessment |
|----------|----------------------|---------|------------|
| Most likely | XX% | | |
| Escalatory alternative | XX% | | |
| De-escalatory / negotiation alternative | XX% | | |

## Missed Developments
- Important developments not forecast at all

## Why The Forecast Missed
- Over-weighted signals
- Under-weighted signals
- Timing errors
- Actor-control errors
- Propaganda traps
- Structural misunderstandings

## Calibration Notes
- Which confidence calls were too high
- Which confidence calls were too low
- Which actor was hardest to estimate correctly

## Improvements For Next Forecast
- Concrete methodological fixes for the next cycle

## Source Base
- Prediction file
- Pattern analysis file
- Daily briefs from the reviewed week
```

## Rolling Lessons File Rules

The rolling lessons file is not a duplicate of weekly scorecards.

Append only distilled, reusable lessons.

Good lessons:

- `Do not treat public negotiation claims by Washington as strong evidence of actual progress unless Tehran behavior also changes.`
- `When Israel expands target categories late in the week, the next week should assume higher risk of cross-theater spillover unless mediation materially advances.`

Bad lessons:

- `This week was complicated.`
- `Need better forecasting.`

## Required Rolling Lessons Output Format

If the file does not exist, create:

```md
# Prediction Lessons Master

## How To Use
- Read this file before writing each new weekly pattern analysis and prediction.
- Append new lessons only when they are specific and reusable.
- Do not repeat the same lesson in slightly different wording.

## Lessons
### YYYY-MM-DD to YYYY-MM-DD
- Lesson
- Lesson
```

If it already exists:

- append a new dated subsection under `## Lessons`
- keep prior lessons unchanged unless a new lesson explicitly corrects or replaces an older one

## Lesson Categories To Extract

When appending lessons, look for:

- escalation-bias errors
- de-escalation-bias errors
- actor-mirroring errors
- proxy-autonomy errors
- rhetoric-vs-behavior errors
- timing-window errors
- capability-assessment errors
- negotiation-signal errors
- maritime-risk errors
- domestic-politics weighting errors

## Self-Correction Rules

- If the forecast was wrong for the right reason but bad timing, record that as a timing lesson, not a full logic failure.
- If the forecast relied too heavily on one side's official messaging, record that as a source-weighting lesson.
- If a proxy actor moved more independently than expected, record that explicitly.
- If a development was visible in the week before but ignored, record that as a missed-indicator lesson.
- If an uncertainty was stated clearly in the prediction and the forecast still failed because the uncertainty resolved the other way, note that separately from overconfidence.

## Trigger Format For Use

Interpret the task as:

`Review the weekly prediction using weekly_prediction_review_and_lessons_instruction.md`

Then:

1. Read the prediction file
2. Read the supporting pattern analysis file
3. Read the 7 daily briefs from the forecast window
4. Create the weekly scorecard file
5. Create or append the rolling lessons file

## Minimum Quality Standard

Do not finalize unless:

- every major forecast claim has been scored
- missed developments are listed explicitly
- reasons for error are separated from outcomes
- the rolling lessons entry contains only reusable lessons
- the next forecast cycle would genuinely improve if it read the appended lessons
