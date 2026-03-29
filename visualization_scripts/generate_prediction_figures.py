import argparse
import os
from typing import Dict, Tuple

import matplotlib.pyplot as plt
import pandas as pd
import textwrap
from matplotlib.lines import Line2D


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
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.axis("off")
    ax.set_title("Scenario Tree For Next 7 Days", fontsize=16, pad=20)

    root_x, root_y = 0.5, 0.92
    ax.text(
        root_x,
        root_y,
        "Weekly Forecast",
        ha="center",
        va="center",
        fontsize=14,
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.8", fc="#f8fafc", ec="#475569", lw=2),
    )

    x_positions = [0.16, 0.5, 0.84]
    y = 0.40
    for x, (_, row) in zip(x_positions, summary.iterrows()):
        label = SCENARIO_LABELS.get(row["scenario"], row["scenario"])
        
        # Wrap the behaviors and triggers so they don't stretch too wide
        wrapped_behaviors = []
        for item in row["behaviors"]:
            wrapped = "\n  ".join(textwrap.wrap(str(item), width=45))
            wrapped_behaviors.append(f"• {wrapped}")
        behaviors_str = "\n".join(wrapped_behaviors) if wrapped_behaviors else "• No items"
        
        wrapped_triggers = []
        for item in row["triggers"]:
            wrapped = "\n  ".join(textwrap.wrap(str(item), width=45))
            wrapped_triggers.append(f"► {wrapped}")
        triggers_str = "\n".join(wrapped_triggers) if wrapped_triggers else "► No triggers"
        
        box_text = f"{label}\nProbability: {row['probability']:.0f}%\n\nBehaviors:\n{behaviors_str}\n\nTriggers:\n{triggers_str}"
        
        ax.annotate(
            "", 
            xy=(x, y + 0.28), 
            xytext=(root_x, root_y - 0.05), 
            arrowprops=dict(arrowstyle="->", lw=2.5, color="#64748b")
        )
        
        ax.text(
            x,
            y,
            box_text,
            ha="center",
            va="center",
            bbox=dict(boxstyle="round,pad=0.8", fc="#f1f5f9", ec="#3b82f6", lw=1.5),
            fontsize=10.5,
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

    # Group by coordinates to combine text for overlapping points
    grouped = {}
    for _, row in plotting.iterrows():
        key = (row["probability_value"], row["impact_value"])
        if key not in grouped:
            grouped[key] = []
        grouped[key].append(row)

    fig = plt.figure(figsize=(12, 14))
    # Create two subplots: one for the matrix (top), one for the legend/text (bottom)
    gs = fig.add_gridspec(2, 1, height_ratios=[1, 1.2], hspace=0.15)
    ax_matrix = fig.add_subplot(gs[0])
    ax_text = fig.add_subplot(gs[1])
    
    ax_text.axis('off')

    marker_idx = 1
    legend_texts = []

    for (base_x, base_y), rows in grouped.items():
        # Calculate how many items are at this coordinate to center them
        num_items = len(rows)
        total_width = (num_items - 1) * 4.0
        start_x = base_x - (total_width / 2)
        
        for i, row in enumerate(rows):
            # Spread dots horizontally if they share the exact same coordinate
            dot_x = start_x + (i * 4.0)
            dot_y = base_y
            
            color = CONFIDENCE_COLORS.get(str(row["confidence"]), "#555555")
            ax_matrix.scatter(
                dot_x,
                dot_y,
                s=500,
                color=color,
                edgecolor="white",
                linewidth=2.0,
                alpha=0.9,
                zorder=3
            )
            
            # Put the marker number inside the dot
            ax_matrix.text(
                dot_x,
                dot_y,
                str(marker_idx),
                color="white",
                fontsize=12,
                fontweight="bold",
                ha="center",
                va="center",
                zorder=4
            )
            
            behavior_text = "\n    ".join(textwrap.wrap(str(row['predicted_behavior']), width=85))
            legend_texts.append(f"[{marker_idx}] {row['predicted_actor']}: {behavior_text}")
            
            marker_idx += 1

    ax_matrix.set_title("Forecast Risk Matrix", fontsize=16, pad=15)
    ax_matrix.set_xlabel("Probability (%)", fontsize=12)
    ax_matrix.set_ylabel("Impact Level", fontsize=12)
    ax_matrix.set_xlim(0, 105)
    ax_matrix.set_ylim(0.5, 4.5)
    ax_matrix.set_yticks([1, 2, 3, 4])
    ax_matrix.set_yticklabels(["Low", "Medium", "High", "Critical"])
    ax_matrix.grid(alpha=0.4, linestyle="--", zorder=1)
    
    # Add confidence legend to the matrix plot
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='High Confidence', markerfacecolor=CONFIDENCE_COLORS['High'], markersize=10),
        Line2D([0], [0], marker='o', color='w', label='Medium Confidence', markerfacecolor=CONFIDENCE_COLORS['Medium'], markersize=10),
        Line2D([0], [0], marker='o', color='w', label='Low Confidence', markerfacecolor=CONFIDENCE_COLORS['Low'], markersize=10),
    ]
    ax_matrix.legend(handles=legend_elements, loc='upper left', framealpha=0.95, fontsize=10)

    # Render the text in the right sidebar
    full_text = "\n\n".join(legend_texts)
    
    # Add a title for the sidebar
    ax_text.text(
        0.02, 
        1.0, 
        "Forecast Details", 
        fontsize=16,
        fontweight="bold",
        va="top",
        ha="left",
        transform=ax_text.transAxes
    )
    
    ax_text.text(
        0.02, 
        0.92, 
        full_text, 
        fontsize=12,
        va="top",
        ha="left",
        transform=ax_text.transAxes
    )

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
    fig, ax = plt.subplots(figsize=(14, 12))
    ax.axis("off")
    wrapped = table.copy()
    
    # Wrap text cleanly instead of slicing
    wrapped["signal"] = wrapped["signal"].apply(lambda x: "\n".join(textwrap.wrap(str(x), width=30)))
    wrapped["invalidator"] = wrapped["invalidator"].fillna("").apply(lambda x: "\n".join(textwrap.wrap(str(x), width=25)))
    wrapped["supports_which_scenario"] = wrapped["supports_which_scenario"].apply(lambda x: "\n".join(textwrap.wrap(str(x), width=15)))
    
    # Format column names
    col_labels = ["\n".join(textwrap.wrap(col.replace("_", " ").title(), width=12)) for col in wrapped.columns]
    
    mpl_table = ax.table(
        cellText=wrapped.values,
        colLabels=col_labels,
        loc="center",
        cellLoc="left",
    )
    
    # Adjust column widths to give more space to the text-heavy columns
    col_widths = {
        0: 0.28,  # Signal
        1: 0.10,  # Related Actor
        2: 0.15,  # Supports Which Scenario
        3: 0.10,  # Confidence
        4: 0.28,  # Invalidator
        5: 0.08,  # Current Status
        6: 0.08   # Review Frequency
    }
    for col, width in col_widths.items():
        for row in range(len(wrapped) + 1):
            cell = mpl_table.get_celld().get((row, col))
            if cell:
                cell.set_width(width)
                
    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(10)
    mpl_table.scale(1, 6.0)  # Scale height to fit wrapped text
    
    # Style headers
    for (row, col), cell in mpl_table.get_celld().items():
        if row == 0:
            cell.set_text_props(weight='bold', color='white')
            cell.set_facecolor('#334155')
        else:
            # Alternate row colors
            if row % 2 == 0:
                cell.set_facecolor('#f8fafc')
            else:
                cell.set_facecolor('#ffffff')
                
        # Add some padding
        cell.set_edgecolor('#cbd5e1')
        
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
