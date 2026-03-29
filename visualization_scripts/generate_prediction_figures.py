import argparse
import os
from typing import Dict, Tuple

import matplotlib.pyplot as plt
import pandas as pd


SCENARIO_ORDER = ["MostLikely", "EscalatoryAlternative", "DeEscalatoryAlternative"]
SCENARIO_LABELS: Dict[str, str] = {
    "MostLikely": "Most Likely",
    "EscalatoryAlternative": "Escalatory Alternative",
    "DeEscalatoryAlternative": "De-escalatory Alternative",
}
IMPACT_MAP: Dict[str, int] = {"Low": 1, "Medium": 2, "High": 3, "Critical": 4}
CONFIDENCE_COLORS: Dict[str, str] = {"High": "#2ca02c", "Medium": "#ff7f0e", "Low": "#d62728"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate weekly prediction figures from forecast objects CSV.")
    parser.add_argument("--forecast-csv", required=True, help="Path to forecast_objects CSV")
    parser.add_argument("--output-dir", required=True, help="Directory for rendered figures")
    return parser.parse_args()


def ensure_output_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def parse_probability(value: str) -> float:
    if pd.isna(value):
        return 0.0
    text = str(value).strip()
    if "-" in text:
        left, right = text.split("-", 1)
        try:
            return (float(left) + float(right)) / 2
        except ValueError:
            return 0.0
    mapping = {"High": 75.0, "Medium": 50.0, "Low": 20.0}
    return mapping.get(text, 0.0)


def scenario_summary(forecast: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for scenario in SCENARIO_ORDER:
        subset = forecast[forecast["scenario"] == scenario]
        if subset.empty:
            continue
        probability = parse_probability(subset["probability_band"].iloc[0])
        behaviors = subset["predicted_behavior"].head(3).tolist()
        triggers = subset["main_trigger"].dropna().astype(str).head(2).tolist()
        rows.append(
            {
                "scenario": scenario,
                "probability": probability,
                "behaviors": behaviors,
                "triggers": triggers,
            }
        )
    return pd.DataFrame(rows)


def save_scenario_tree(forecast: pd.DataFrame, output_dir: str) -> None:
    summary = scenario_summary(forecast)
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.axis("off")
    ax.set_title("Scenario Tree For Next 7 Days")

    root_x, root_y = 0.5, 0.88
    ax.text(
        root_x,
        root_y,
        "Weekly Forecast",
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.5", fc="#f4f4f4", ec="#555555"),
    )

    x_positions = [0.18, 0.5, 0.82]
    y = 0.36
    for x, (_, row) in zip(x_positions, summary.iterrows()):
        label = SCENARIO_LABELS.get(row["scenario"], row["scenario"])
        behaviors = "\n".join(f"- {item}" for item in row["behaviors"]) or "- No items"
        triggers = "\n".join(f"* {item}" for item in row["triggers"]) or "* No triggers"
        box_text = f"{label}\nProbability: {row['probability']:.0f}%\n\nBehaviors:\n{behaviors}\n\nTriggers:\n{triggers}"
        ax.annotate("", xy=(x, y + 0.17), xytext=(root_x, root_y - 0.05), arrowprops=dict(arrowstyle="->", lw=1.8))
        ax.text(
            x,
            y,
            box_text,
            ha="center",
            va="center",
            bbox=dict(boxstyle="round,pad=0.5", fc="#eef5ff", ec="#4a6fa5"),
            fontsize=9,
        )

    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, "scenario_tree.png"), dpi=200)
    plt.close(fig)


def probability_to_xy(value: str) -> float:
    return parse_probability(value)


def save_forecast_risk_matrix(forecast: pd.DataFrame, output_dir: str) -> None:
    plotting = forecast.copy()
    plotting["probability_value"] = plotting["probability_band"].map(probability_to_xy)
    plotting["impact_value"] = plotting["impact_level"].map(lambda x: IMPACT_MAP.get(str(x), 1))

    fig, ax = plt.subplots(figsize=(10, 7))
    for _, row in plotting.iterrows():
        ax.scatter(
            row["probability_value"],
            row["impact_value"],
            s=140,
            color=CONFIDENCE_COLORS.get(str(row["confidence"]), "#555555"),
            alpha=0.75,
        )
        label = f"{row['predicted_actor']}: {str(row['predicted_behavior'])[:42]}"
        ax.text(row["probability_value"] + 1, row["impact_value"] + 0.03, label, fontsize=8)

    ax.set_title("Forecast Risk Matrix")
    ax.set_xlabel("Probability")
    ax.set_ylabel("Impact")
    ax.set_xlim(0, 100)
    ax.set_ylim(0.7, 4.3)
    ax.set_yticks([1, 2, 3, 4])
    ax.set_yticklabels(["Low", "Medium", "High", "Critical"])
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, "forecast_risk_matrix.png"), dpi=200)
    plt.close(fig)


def signals_table(forecast: pd.DataFrame) -> pd.DataFrame:
    table = forecast.copy()
    table["signal"] = table["main_trigger"].fillna(table["predicted_behavior"])
    table["supports_which_scenario"] = table["scenario"].map(lambda x: SCENARIO_LABELS.get(x, x))
    table["current_status"] = "Watch"
    table["review_frequency"] = "Daily"
    return table[
        ["signal", "predicted_actor", "supports_which_scenario", "confidence", "main_invalidator", "current_status", "review_frequency"]
    ].rename(columns={"predicted_actor": "related_actor", "main_invalidator": "invalidator"})


def save_signals_dashboard(forecast: pd.DataFrame, output_dir: str) -> None:
    table = signals_table(forecast).head(10)
    fig, ax = plt.subplots(figsize=(16, 5))
    ax.axis("off")
    ax.set_title("Signals To Watch Dashboard")
    wrapped = table.copy()
    wrapped["signal"] = wrapped["signal"].astype(str).str.slice(0, 48)
    wrapped["invalidator"] = wrapped["invalidator"].fillna("").astype(str).str.slice(0, 40)
    mpl_table = ax.table(
        cellText=wrapped.values,
        colLabels=wrapped.columns,
        loc="center",
        cellLoc="left",
    )
    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(8)
    mpl_table.scale(1, 1.5)
    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, "signals_to_watch_dashboard.png"), dpi=200)
    plt.close(fig)


def main() -> None:
    args = parse_args()
    ensure_output_dir(args.output_dir)
    forecast = pd.read_csv(args.forecast_csv)
    save_scenario_tree(forecast, args.output_dir)
    save_forecast_risk_matrix(forecast, args.output_dir)
    save_signals_dashboard(forecast, args.output_dir)


if __name__ == "__main__":
    main()
