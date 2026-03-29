# Visualization Data Collection And Figure Generation Instruction

## Purpose

Use this instruction when the goal is to:

- collect or derive structured data from the daily briefs, weekly pattern analyses, predictions, and forecast reviews
- generate consistent data tables for visualization
- draw the approved first-generation figures for pattern analysis and prediction

This instruction is for disciplined visual analysis. It should not invent precision beyond the evidence in the briefs.

## Current Figure Set

For now, support only these figures:

### Pattern Analysis Figures

- `Escalation intensity over time`
- `Actor behavior heatmap`
- `Geographic conflict map`
- `Trigger-response flow diagram` when the week has a clear escalation loop

### Prediction Figures

- `Scenario tree for next 7 days`
- `Forecast risk matrix`
- `Signals to watch dashboard`

Do not prioritize other figures unless the dataset becomes more standardized.

## Rendering Scripts

After the CSV and notes files are created, render the final figures with:

- `visualization_scripts/generate_pattern_figures.py`
- `visualization_scripts/generate_prediction_figures.py`

Dependencies file:

- `visualization_scripts/requirements.txt`

Install:

```bash
python -m pip install -r visualization_scripts/requirements.txt
```

## Evidence Inputs

Use these inputs in this order:

1. The relevant daily briefs in `/home/masoud/Desktop/Projects/IRAN_vs_US/news`
2. The most recent weekly pattern analysis file, if it exists
3. The relevant prediction file, if it exists
4. The relevant prediction scorecard file, if it exists
5. The rolling lessons file, if it exists
6. The fundamentals files in `/home/masoud/Desktop/Projects/IRAN_vs_US/fundamentals`

For weekly pattern figures, the daily briefs are the primary evidence base.

For prediction figures, the prediction file and its supporting pattern analysis are the primary evidence base.

## Output Files

For each weekly visualization cycle, generate these data files:

- `visual_coding_YYYY-MM-DD_to_YYYY-MM-DD.csv`
- `weekly_actor_summary_YYYY-MM-DD_to_YYYY-MM-DD.csv`
- `forecast_objects_YYYY-MM-DD_to_YYYY-MM-DD.csv`
- `figure_notes_YYYY-MM-DD_to_YYYY-MM-DD.md`

Use:

- the analysis window for `visual_coding_...` and `weekly_actor_summary_...`
- the forecast window for `forecast_objects_...`
- the analysis window for `figure_notes_...` unless it is a forecast-only figure package

Example:

- analysis window: `2026-03-22` to `2026-03-28`
- forecast window: `2026-03-29` to `2026-04-04`

Then create:

- `visual_coding_2026-03-22_to_2026-03-28.csv`
- `weekly_actor_summary_2026-03-22_to_2026-03-28.csv`
- `forecast_objects_2026-03-29_to_2026-04-04.csv`
- `figure_notes_2026-03-22_to_2026-03-28.md`

Then render the figures from those files.

## Actor Set

Use these actor labels:

- `US`
- `Israel`
- `Iran`
- `Hezbollah`
- `IraqiPartnerForces`
- `Houthis`

Only add another actor if it had material and repeated relevance in the source window.

## Core Data Layers

Build the visualization package in three layers:

1. `daily coded signals`
2. `weekly actor summaries`
3. `weekly forecast objects`

## Layer 1: Daily Coded Signals

Create one row per `date x actor`.

### Required Columns

```text
date
actor
military_activity_score
diplomatic_activity_score
proxy_activity_score
infrastructure_coercion_score
maritime_pressure_score
rhetorical_escalation_score
confidence_of_coding
dominant_posture
key_trigger
key_response
main_theater
notes
```

### Field Definitions

`date`
- The date of the daily brief.

`actor`
- One of the standard actor labels.

`military_activity_score`
- 0 to 3

`diplomatic_activity_score`
- 0 to 3

`proxy_activity_score`
- 0 to 3

`infrastructure_coercion_score`
- 0 to 3

`maritime_pressure_score`
- 0 to 3

`rhetorical_escalation_score`
- 0 to 3

`confidence_of_coding`
- `High`
- `Medium`
- `Low`

`dominant_posture`
- `Escalating`
- `Deterring`
- `Retaliating`
- `Holding`
- `Negotiating`
- `Pressuring`
- `Mixed`

`key_trigger`
- Short phrase naming the main thing the actor reacted to that day.

`key_response`
- Short phrase naming the actor’s main response that day.

`main_theater`
- `Iran`
- `Israel`
- `Lebanon`
- `Iraq`
- `YemenRedSea`
- `GulfHormuz`
- `MultiTheater`
- `Diplomatic`

`notes`
- One short sentence only.

## Layer 2: Weekly Actor Summaries

Create one row per `week x actor`.

### Required Columns

```text
week_start
week_end
actor
avg_military_activity
avg_diplomatic_activity
avg_proxy_activity
avg_infrastructure_coercion
avg_maritime_pressure
avg_rhetorical_escalation
dominant_weekly_posture
primary_theater
trend_vs_prior_week
key_pattern
main_constraint
main_incentive
```

### Weekly Summary Rules

`trend_vs_prior_week`
- `Higher`
- `Lower`
- `Stable`
- `Mixed`

`key_pattern`
- One clear sentence such as:
  - `Using diplomacy to delay escalation`
  - `Expanding target categories`
  - `Maintaining pressure through proxies`
  - `Combining maritime coercion with selective access`

`main_constraint`
- State the single most relevant limit observed in the week.

`main_incentive`
- State the single most relevant driver observed in the week.

## Layer 3: Weekly Forecast Objects

Create one row per forecasted development.

### Required Columns

```text
forecast_window_start
forecast_window_end
scenario
predicted_actor
predicted_behavior
probability_band
impact_level
confidence
supporting_pattern
main_trigger
main_invalidator
theater
status_after_review
```

### Forecast Object Rules

`scenario`
- `MostLikely`
- `EscalatoryAlternative`
- `DeEscalatoryAlternative`

`predicted_behavior`
- Must be concrete and observable.

Good examples:

- `Israel likely continues strikes on military and infrastructure targets in Iran`
- `Iran likely maintains maritime coercion without fully reopening shipping`
- `Houthis may widen Red Sea pressure`
- `US likely increases pressure while avoiding declared ground combat`

`probability_band`
- `High`
- `Medium`
- `Low`

or a range such as:

- `70-85`
- `40-60`
- `15-30`

Use one convention consistently within the same forecast package.

`impact_level`
- `Low`
- `Medium`
- `High`
- `Critical`

`confidence`
- `High`
- `Medium`
- `Low`

`status_after_review`
- Leave blank until a review exists.
- Then fill with:
  - `Correct`
  - `PartiallyCorrect`
  - `Wrong`
  - `MissedDevelopment`
  - `RightDirectionWrongMechanism`

## Scoring Rubric

Use only this simple 0 to 3 scoring scale:

- `0` = absent or negligible
- `1` = limited, symbolic, or mostly rhetorical
- `2` = clear and relevant
- `3` = major, repeated, or strategically important

Do not use more granular scales such as 0 to 10.

## Coding Rules By Category

### Military Activity

Score based on:

- strike tempo
- missile or drone launches
- interceptions
- major deployments
- cross-border attacks

### Diplomatic Activity

Score based on:

- talks
- mediation attempts
- official calls
- U.N. or multilateral diplomatic steps
- public de-escalation proposals

Do not reduce escalation automatically just because diplomacy exists.

### Proxy Activity

Score based on:

- proxy attacks
- proxy mobilization
- proxy signaling
- proxy restraint after prior activity

### Infrastructure Coercion

Score based on:

- attacks or threats against energy, ports, airports, power, water, desalination, communications, industrial, or nuclear-linked sites

### Maritime Pressure

Score based on:

- Hormuz pressure
- Bab el-Mandeb / Red Sea pressure
- shipping restrictions
- selective access
- naval threats

### Rhetorical Escalation

Score based on:

- official threat intensity
- ultimata
- explicit retaliation warnings
- statements expanding war aims

Do not let rhetoric outweigh action if the two conflict.

## Figure Mapping

## 1. Escalation Intensity Over Time

### Purpose

Show the weekly or daily trend of conflict pressure.

### Use Data From

- `visual_coding_...csv`

### Recommended Construction

Create two lines:

- `EscalationPressure`
- `DiplomaticActivity`

Do not collapse diplomacy into escalation unless the diplomacy is plainly coercive.

### Recommended EscalationPressure Formula

```text
EscalationPressure =
(military_activity_score * 2)
+ (infrastructure_coercion_score * 2)
+ (maritime_pressure_score * 2)
+ (proxy_activity_score * 1.5)
+ (rhetorical_escalation_score * 1)
```

Do not claim the score is objective truth. It is a comparative analytical index.

## 2. Actor Behavior Heatmap

### Purpose

Compare actors across time and behavior categories.

### Use Data From

- `visual_coding_...csv`
- `weekly_actor_summary_...csv`

### Recommended Construction

Prefer separate heatmaps for:

- military
- diplomacy
- proxy activity
- infrastructure coercion
- maritime pressure

Do not compress everything into a single opaque score if category separation is still informative.

## 3. Geographic Conflict Map

### Purpose

Show the main theaters, cross-theater effects, and strategic chokepoints.

### Use Data From

- `visual_coding_...csv`
- `weekly_actor_summary_...csv`
- `figure_notes_...md`

### Mapping Rule

Treat this as a `theater map`, not a precise coordinate strike map.

Preferred theater labels:

- Tehran / central Iran
- Israel
- southern Lebanon / Beirut
- Iraq
- Yemen / Red Sea
- Strait of Hormuz / Gulf

Use arrows only for clear cross-theater trigger-response relationships.

## 4. Trigger-Response Flow Diagram

### Purpose

Explain escalation logic rather than event count.

### Use Data From

- `key_trigger`
- `key_response`
- weekly summary patterns

### Rule

Only create this figure when the week has a visible escalation or restraint loop.

Example:

- `Israeli strike expansion -> Iranian retaliation threat -> proxy activation risk -> U.S. deployment signal -> maritime pressure`

## 5. Scenario Tree

### Purpose

Show the next 7 days as structured alternatives rather than one deterministic call.

### Use Data From

- `forecast_objects_...csv`
- prediction file

### Rule

The tree must contain:

- `MostLikely`
- `EscalatoryAlternative`
- `DeEscalatoryAlternative`

Scenario probabilities must sum to 100%.

## 6. Forecast Risk Matrix

### Purpose

Separate most likely outcomes from most dangerous outcomes.

### Use Data From

- `forecast_objects_...csv`

### Rule

Plot:

- x-axis = `probability_band`
- y-axis = `impact_level`

Each point must be a concrete forecast object, not a vague narrative.

## 7. Signals To Watch Dashboard

### Purpose

Provide a monitoring interface for the next week.

### Use Data From

- `forecast_objects_...csv`
- prediction file

### Required Columns

```text
signal
related_actor
why_it_matters
supports_which_scenario
current_status
review_frequency
```

### Good Signals

- Israeli target-category expansion
- U.S. ground-force language shift
- Iranian shipping-access policy change
- Hezbollah tempo shift
- Houthi maritime threat language
- formalization of mediation venue
- sanctions escalation or restraint

## Figure Placement Rules

### In Pattern Analysis Files

Prefer:

- escalation intensity chart
- actor behavior heatmap
- geographic conflict map
- trigger-response flow when especially useful

### In Prediction Files

Prefer:

- scenario tree
- forecast risk matrix
- signals to watch dashboard

## Figure Notes File

For each visualization cycle, create `figure_notes_YYYY-MM-DD_to_YYYY-MM-DD.md` with:

```md
# Figure Notes - YYYY-MM-DD to YYYY-MM-DD

## Scope
- Analysis or forecast window

## Data Inputs
- Files used

## Coding Assumptions
- Any subjective coding calls

## Figure List
### Escalation Intensity
- What it shows
- Main finding

### Actor Behavior Heatmap
- What it shows
- Main finding

### Geographic Conflict Map
- What it shows
- Main finding

### Trigger-Response Flow
- What it shows
- Main finding

### Scenario Tree
- What it shows
- Main finding

### Forecast Risk Matrix
- What it shows
- Main finding

### Signals Dashboard
- What it shows
- Main finding

## Evidence Limits
- What the figures do not prove
```

## Honesty And Attribution Rules

- Do not visualize disputed claims as if they are settled fact.
- If the underlying evidence is mixed, reflect that in labels or notes.
- If location precision is low, map the theater, not an invented point.
- If a score is judgment-based, say so.
- If an actor claim lacks independent verification, do not encode it as a major observed action without qualification.

## Trigger Format For Use

Interpret the task as:

`Collect visualization data and generate figures using visualization_data_collection_and_figure_generation_instruction.md`

Then:

1. Read the relevant briefs and analysis files
2. Build `visual_coding_...csv`
3. Build `weekly_actor_summary_...csv`
4. Build `forecast_objects_...csv` when forecasting is involved
5. Save `figure_notes_...md`
6. Render the pattern figures:

```bash
python visualization_scripts/generate_pattern_figures.py \
  --coding-csv visual_coding_YYYY-MM-DD_to_YYYY-MM-DD.csv \
  --summary-csv weekly_actor_summary_YYYY-MM-DD_to_YYYY-MM-DD.csv \
  --output-dir figures/pattern_YYYY-MM-DD_to_YYYY-MM-DD
```

7. Render the prediction figures:

```bash
python visualization_scripts/generate_prediction_figures.py \
  --forecast-csv forecast_objects_YYYY-MM-DD_to_YYYY-MM-DD.csv \
  --output-dir figures/prediction_YYYY-MM-DD_to_YYYY-MM-DD
```

## Minimum Quality Standard

Do not finalize unless:

- the coding table covers every day in the selected window
- every actor included has a reason to be included
- the scores use the 0 to 3 rubric consistently
- the figure set matches the actual available data quality
- figure notes explain the key assumptions and limits
