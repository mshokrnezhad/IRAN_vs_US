# Weekly Pattern Analysis And Prediction Instruction

## Purpose

Use this instruction when the goal is to:

- analyze the behavior pattern of the main actors over the last 7 days
- combine that short-horizon evidence with longer-term fundamentals
- produce one weekly `pattern analysis` file
- produce one weekly `prediction` file for the next 7 days

This instruction is for structured forecasting, not for advocacy or certainty claims.

## Output Files

For each weekly cycle, create exactly these two files:

- `pattern_analysis_YYYY-MM-DD_to_YYYY-MM-DD.md`
- `prediction_YYYY-MM-DD_to_YYYY-MM-DD.md`

Use the first filename for the analysis window and the second filename for the forecast window.

Example:

- analysis window: `2026-03-22` to `2026-03-28`
- forecast window: `2026-03-29` to `2026-04-04`

Then create:

- `pattern_analysis_2026-03-22_to_2026-03-28.md`
- `prediction_2026-03-29_to_2026-04-04.md`

## Core Principle

Keep `pattern analysis` and `prediction` separate.

- The pattern file explains what happened, what repeated, and why it matters.
- The prediction file states what is likely next, with scenarios, probabilities, and invalidation signals.

Do not mix descriptive analysis and forward-looking prediction into a single section.

## Required Inputs

Always use these inputs in this priority order:

1. The last 7 daily briefs in `/home/masoud/Desktop/Projects/IRAN_vs_US/news`
2. The most recent 2 to 4 weeks of daily briefs for continuity when needed
3. The fundamentals files in `/home/masoud/Desktop/Projects/IRAN_vs_US/fundamentals` (must explicitly include `who_is_trump.json` for US behavioral profiling)
4. Any prior weekly pattern analysis files, if they exist
5. Any prior prediction files, if they exist
6. Any prior prediction review files or lessons file, if they exist

Treat the last 7 daily briefs as the primary evidence layer.

Treat the fundamentals files as structural context, not as same-weight recent evidence.

## Actor Set

Always assess behavior for these actors when relevant:

- United States
- Israel
- Iran
- Hezbollah
- Hashd / militias when clearly relevant
- Ansar Allah / Houthis

You may include other directly relevant actors only if there is clear evidence that they materially affected the week.

## Forecasting Discipline

Forecast observable behavior, not vague intent.

Good forecast objects:

- missile or drone attack tempo
- infrastructure targeting patterns
- maritime disruption behavior
- proxy activation or restraint
- troop movement and force posture
- negotiation posture
- sanctions or coercive economic signaling
- leadership messaging shifts
- escalation thresholds crossed or not crossed

Avoid weak forecast objects such as:

- `they will become more angry`
- `the war mood will worsen`
- `a dramatic event may happen`

## Evidence Weighting Rules

Use this weighting logic:

- recent 7-day behavior: highest weight
- recent 2 to 4 week continuity: medium weight
- structural fundamentals: medium weight for constraints and incentives, low weight for near-term timing
- prior lessons file: high weight for calibration and error reduction

If rhetoric and behavior diverge, prefer behavior.

If one side makes a threat but there is no supporting capability, preparation, or historical pattern, say so clearly.

## Pattern Analysis Method

For the analysis window:

1. Extract the most important events and signals from the 7 daily briefs.
2. Group them by actor and by behavior type.
3. Distinguish:
   - signaling
   - action
   - capability
   - constraint
   - willingness
4. Identify repeated patterns, not just one-off incidents.
5. Note where the week changed relative to the previous week.
6. Identify triggers that likely move the system toward escalation, restraint, or stalemate.
7. Identify which claims remain uncertain or propaganda-shaped.

## Required Pattern Analysis Output Format

Use this structure:

```md
# Pattern Analysis - YYYY-MM-DD to YYYY-MM-DD

## Scope
- Analysis window: YYYY-MM-DD to YYYY-MM-DD
- Forecast purpose: support a 7-day forward prediction
- Primary evidence base: daily briefs for the analysis window

## Inputs Used
- Last 7 daily briefs used
- Earlier daily briefs used for continuity
- Fundamentals files used
- Prior pattern/prediction/review files used, if any

## Executive Summary
- 4-8 bullets on the week's dominant patterns

## Weekly Baseline
- Short paragraph on the week's overall state: escalation, stalemate, coercive diplomacy, multi-front spread, etc.

## Actor Behavior Analysis
### United States
- Objectives observed
- Actions taken
- Constraints
- Pattern assessment

### Israel
- Objectives observed
- Actions taken
- Constraints
- Pattern assessment

### Iran
- Objectives observed
- Actions taken
- Constraints
- Pattern assessment

### Hezbollah
- Role this week
- Pattern assessment

### Hashd
- Role this week
- Pattern assessment

### Ansar Allah / Houthis
- Role this week
- Pattern assessment

## Cross-Actor Interaction Patterns
- How one actor's moves changed another actor's behavior
- Escalation loop or restraint loop if visible

## Constraints And Incentives
| Actor | Main Incentives | Main Constraints | What This Likely Means Next |
|------|------------------|------------------|-----------------------------|

## Pattern Confidence Assessment
| Pattern | Confidence | Why |
|---------|------------|-----|

## Indicators To Watch Next Week
- 5-10 concrete signals that would confirm or weaken the pattern assessment

## Information Gaps
- What remains unclear
- Which unknowns matter most for the forecast

## Source Base
- Cite the main daily briefs and any major supporting context files
```

## Prediction Method

After completing the pattern analysis:

1. Convert patterns into next-week expectations.
2. Incorporate behavioral insights from `who_is_trump.json` when forecasting US actions and responses.
3. Produce one `most likely` scenario and at least two alternatives:
   - `escalatory alternative`
   - `de-escalatory / negotiation alternative`
4. Assign probabilities to the scenarios.
5. Make sure scenario probabilities sum to 100%.
6. For each actor, forecast likely behavior in observable terms.
7. Include invalidators and early-warning indicators.
8. State what would prove the forecast wrong quickly.

## Required Prediction Output Format

Use this structure:

```md
# Prediction - YYYY-MM-DD to YYYY-MM-DD

## Scope
- Forecast window: YYYY-MM-DD to YYYY-MM-DD
- Analysis basis: pattern analysis from the prior 7 days

## Executive Summary
- 4-8 bullets with the highest-value forecast calls

## Scenario Table
| Scenario | Probability | Description | What Would Make It More Likely |
|----------|-------------|-------------|--------------------------------|
| Most likely | XX% | Short summary | 1-3 triggers |
| Escalatory alternative | XX% | Short summary | 1-3 triggers |
| De-escalatory / negotiation alternative | XX% | Short summary | 1-3 triggers |

## Actor-By-Actor Predictions
### United States
| Predicted Behavior | Confidence | Why | Invalidators |
|--------------------|------------|-----|--------------|

### Israel
| Predicted Behavior | Confidence | Why | Invalidators |
|--------------------|------------|-----|--------------|

### Iran
| Predicted Behavior | Confidence | Why | Invalidators |
|--------------------|------------|-----|--------------|

### Hezbollah
| Predicted Behavior | Confidence | Why | Invalidators |
|--------------------|------------|-----|--------------|

### Hashd
| Predicted Behavior | Confidence | Why | Invalidators |
|--------------------|------------|-----|--------------|

### Ansar Allah / Houthis
| Predicted Behavior | Confidence | Why | Invalidators |
|--------------------|------------|-----|--------------|

## Cross-Theater Forecast
- Maritime
- Air and missile campaign
- Proxy front activation
- Diplomacy and mediation
- Economic and sanctions signaling

## Key Triggers To Watch
- Trigger
- Why it matters
- Which scenario it supports

## Fast-Fail Signals
- Signals that would quickly show the forecast is wrong

## Confidence And Limits
- State the biggest uncertainties
- State what evidence was thin
- Distinguish forecast confidence from scenario probability

## Source Base
- Cite the pattern analysis file
- Cite the main daily briefs and any prior lessons used
```

## Confidence Rules

Use these confidence labels for specific forecast calls:

- `High`: behavior has strong recent repetition, clear capability, and no major contradictory indicators
- `Medium`: behavior is plausible and supported, but there are meaningful contradictory indicators or timing uncertainty
- `Low`: behavior is possible, but evidence is weak, mixed, or too dependent on unknown decisions

Use probabilities only for scenarios, not for every line item.

## Analytical Guardrails

- Do not present prediction as certainty.
- Do not forecast exact casualty counts unless the forecast is explicitly range-based and well-grounded.
- Do not predict dramatic decapitation, collapse, or regime-change events unless there is direct strong evidence.
- Do not assume Iranian-aligned actors are perfectly synchronized with Tehran.
- Do not assume threats will be executed just because they were spoken.
- Do not let one day dominate the weekly pattern unless that day clearly changed the strategic baseline.

## Trigger Format For Use

Interpret the task as:

`Create a weekly pattern analysis and a 7-day prediction using weekly_pattern_analysis_and_prediction_instruction.md`

Then:

1. Read the last 7 daily briefs
2. Read the most relevant fundamentals files
3. Read any existing lessons file or past weekly forecast files
4. Produce the pattern analysis file
5. Produce the prediction file

## Minimum Quality Standard

Do not finalize unless:

- the analysis uses all 7 daily briefs in the window
- the forecast includes at least 3 scenarios including the baseline
- scenario probabilities sum to 100%
- each main actor has at least one concrete forecast when relevant
- invalidators are listed
- uncertainties and evidence gaps are stated plainly
