# IRAN_vs_US

This repository is a structured analysis workspace for the ongoing Iran-U.S.-Israel war. It is designed to turn raw reporting into a repeatable research pipeline: collect daily war briefs, synthesize weekly behavior patterns, generate scenario-based forecasts, review forecast errors, and then visualize the evolving conflict.

The project contains four linked instruction layers in `instructions/`, plus background files in `fundamentals/` and the accumulated daily chronology in `news/`. The value of the repository is not just the collected information, but the workflow discipline: each stage has a defined input set, output format, and place in the sequence.

## Table of Contents

- [Repository Purpose](#repository-purpose)
- [Workflow Order](#workflow-order)
- [Outputs](#outputs)
- [Figure Rendering](#figure-rendering)
- [Repository Structure](#repository-structure)
- [Thank You](#thank-you-)

## Repository Purpose

The repository supports four connected tasks:

- daily war-news collection
- weekly pattern analysis
- weekly 7-day prediction
- forecast review and self-correction
- visualization data extraction and figure generation

The workflow is meant to be iterative. Daily briefs build the weekly evidence base. Weekly forecasts are later scored against reality. The lessons from that review feed back into the next weekly forecast cycle. Visualization sits on top of the coded daily and weekly outputs.

## Workflow Order

Run the workflow in this order:

1. Daily news collection
2. Weekly pattern analysis and prediction
3. Weekly prediction review and lessons update
4. Visualization data collection and figure generation
5. Figure rendering from visualization CSV files

The order matters because each stage depends on the outputs of the earlier stages.

| Stage                                  | Run This Instruction                                                              | Main Inputs                                                                                                                                  | Main Outputs                                                                                                                                                                                   |
| -------------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Daily collection                       | `instructions/daily_war_news_collection_instruction.md`                           | official statements for the target date, Reuters/AP, other high-confidence same-day reporting                                                | `news/daily_war_news_brief_YYYY-MM-DD.md`                                                                                                                                                      |
| Weekly pattern analysis and prediction | `instructions/weekly_pattern_analysis_and_prediction_instruction.md`              | last 7 daily briefs, recent continuity briefs, `fundamentals/`, prior weekly outputs and lessons when they exist                             | `pattern_analysis_YYYY-MM-DD_to_YYYY-MM-DD.md`, `prediction_YYYY-MM-DD_to_YYYY-MM-DD.md`                                                                                                       |
| Weekly review and self-correction      | `instructions/weekly_prediction_review_and_lessons_instruction.md`                | the relevant prediction file, the supporting pattern analysis file, the 7 daily briefs from the forecast window, prior lessons if they exist | `prediction_scorecard_YYYY-MM-DD_to_YYYY-MM-DD.md`, updated `prediction_lessons_master.md`                                                                                                     |
| Visualization                          | `instructions/visualization_data_collection_and_figure_generation_instruction.md` | relevant daily briefs, weekly analysis, prediction, scorecard, lessons, and `fundamentals/` when needed                                      | `visual_coding_YYYY-MM-DD_to_YYYY-MM-DD.csv`, `weekly_actor_summary_YYYY-MM-DD_to_YYYY-MM-DD.csv`, `forecast_objects_YYYY-MM-DD_to_YYYY-MM-DD.csv`, `figure_notes_YYYY-MM-DD_to_YYYY-MM-DD.md` |
| Figure rendering                       | Python scripts in `visualization_scripts/`                                        | visualization CSV outputs from the prior step                                                                                                | rendered `.png` figures for pattern analysis and prediction                                                                                                                                    |

### Minimal Run Logic

1. If a day is missing, create its daily brief first.
2. Once 7 consecutive daily briefs exist, run weekly pattern analysis and prediction.
3. After the forecast week ends and its 7 daily briefs exist, run weekly review and update the lessons file.
4. After the analytical files exist, run the visualization instruction to generate the CSV datasets.
5. Run the Python scripts in `visualization_scripts/` to render the figures from those CSV files.

## Outputs

- Daily brief: `news/daily_war_news_brief_YYYY-MM-DD.md`
- Weekly pattern analysis: `pattern_analysis_YYYY-MM-DD_to_YYYY-MM-DD.md`
- Weekly prediction: `prediction_YYYY-MM-DD_to_YYYY-MM-DD.md`
- Weekly scorecard: `prediction_scorecard_YYYY-MM-DD_to_YYYY-MM-DD.md`
- Rolling lessons: `prediction_lessons_master.md`
- Visualization coding: `visual_coding_YYYY-MM-DD_to_YYYY-MM-DD.csv`
- Weekly actor summary: `weekly_actor_summary_YYYY-MM-DD_to_YYYY-MM-DD.csv`
- Forecast objects: `forecast_objects_YYYY-MM-DD_to_YYYY-MM-DD.csv`
- Figure notes: `figure_notes_YYYY-MM-DD_to_YYYY-MM-DD.md`
- Pattern figures: rendered `.png` files from coding and summary CSVs
- Prediction figures: rendered `.png` files from forecast object CSVs

## Figure Rendering

The visualization instruction creates the structured CSV and notes files. The final figures are rendered afterward by the Python scripts in `visualization_scripts/`.

### Scripts Folder

- `visualization_scripts/generate_pattern_figures.py`
- `visualization_scripts/generate_prediction_figures.py`
- `visualization_scripts/requirements.txt`

### Install Dependencies

From the repository root:

```bash
python -m pip install -r visualization_scripts/requirements.txt
```

### Render Pattern Figures

Run this after these files already exist:

- `visual_coding_YYYY-MM-DD_to_YYYY-MM-DD.csv`
- `weekly_actor_summary_YYYY-MM-DD_to_YYYY-MM-DD.csv`

Command:

```bash
python visualization_scripts/generate_pattern_figures.py \
  --coding-csv visual_coding_YYYY-MM-DD_to_YYYY-MM-DD.csv \
  --summary-csv weekly_actor_summary_YYYY-MM-DD_to_YYYY-MM-DD.csv \
  --output-dir figures/pattern_YYYY-MM-DD_to_YYYY-MM-DD
```

Outputs:

- `escalation_intensity.png`
- `actor_behavior_heatmaps.png`
- `geographic_conflict_map.png`
- `trigger_response_flow.png`

### Render Prediction Figures

Run this after this file already exists:

- `forecast_objects_YYYY-MM-DD_to_YYYY-MM-DD.csv`

Command:

```bash
python visualization_scripts/generate_prediction_figures.py \
  --forecast-csv forecast_objects_YYYY-MM-DD_to_YYYY-MM-DD.csv \
  --output-dir figures/prediction_YYYY-MM-DD_to_YYYY-MM-DD
```

Outputs:

- `scenario_tree.png`
- `forecast_risk_matrix.png`
- `signals_to_watch_dashboard.png`

### Final Order After Visualization Data Collection

1. Run `instructions/visualization_data_collection_and_figure_generation_instruction.md`
2. Generate:
   - `visual_coding_...csv`
   - `weekly_actor_summary_...csv`
   - `forecast_objects_...csv`
   - `figure_notes_...md`
3. Run `generate_pattern_figures.py`
4. Run `generate_prediction_figures.py`
5. Save the resulting images under `figures/`

## Repository Structure

- `instructions/`
  - contains the operational instruction files for each stage of the workflow
- `visualization_scripts/`
  - contains the Python scripts used to render figures from the visualization CSV outputs
- `news/`
  - contains the daily chronological war briefs
- `fundamentals/`
  - contains longer-term background files used as structural context
- repository root
  - contains weekly analysis, prediction, review, lessons, and visualization data files as they are created

---

## Thank You <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Hand%20gestures/Folded%20Hands.png" alt="Folded Hands" width="20" height="20" />

Thank you for using and extending this workflow. The repository is built to support disciplined, source-based conflict analysis rather than one-off summaries, and its quality depends on keeping each stage consistent and well-attributed.

**How you can contribute:**

- Improve daily brief sourcing quality and attribution discipline
- Refine weekly pattern and forecast methodology
- Strengthen the review and lessons framework with better calibration rules
- Expand the visualization layer carefully without overstating the data
- Improve documentation and workflow clarity

We look forward to improving the analysis process over time.
