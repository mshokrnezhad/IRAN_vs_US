import argparse
import os
from typing import Dict, List

import matplotlib.pyplot as plt
import pandas as pd


ACTOR_ORDER = ["US", "Israel", "Iran", "Hezbollah", "IraqiPartnerForces", "Houthis"]
METRIC_COLUMNS = [
    ("military_activity_score", "Military"),
    ("diplomatic_activity_score", "Diplomacy"),
    ("proxy_activity_score", "Proxy"),
    ("infrastructure_coercion_score", "Infrastructure"),
    ("maritime_pressure_score", "Maritime"),
]

THEATER_COORDS: Dict[str, tuple] = {
    "Iran": (4.8, 7.2),
    "Israel": (2.0, 5.2),
    "Lebanon": (1.5, 5.8),
    "Iraq": (3.6, 6.0),
    "YemenRedSea": (1.0, 2.0),
    "GulfHormuz": (5.7, 4.4),
    "MultiTheater": (7.8, 6.2),
    "Diplomatic": (7.5, 2.1),
}

ACTOR_COLORS: Dict[str, str] = {
    "US": "#1f77b4",
    "Israel": "#ff7f0e",
    "Iran": "#2ca02c",
    "Hezbollah": "#d62728",
    "IraqiPartnerForces": "#9467bd",
    "Houthis": "#8c564b",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate weekly pattern figures from visualization CSVs.")
    parser.add_argument("--coding-csv", required=True, help="Path to visual_coding CSV")
    parser.add_argument("--summary-csv", required=True, help="Path to weekly_actor_summary CSV")
    parser.add_argument("--output-dir", required=True, help="Directory for rendered figures")
    return parser.parse_args()


def ensure_output_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def save_escalation_intensity(coding: pd.DataFrame, output_dir: str) -> None:
    scored = coding.copy()
    scored["EscalationPressure"] = (
        scored["military_activity_score"] * 2
        + scored["infrastructure_coercion_score"] * 2
        + scored["maritime_pressure_score"] * 2
        + scored["proxy_activity_score"] * 1.5
        + scored["rhetorical_escalation_score"] * 1
    )
    daily = (
        scored.groupby("date", as_index=False)[["EscalationPressure", "diplomatic_activity_score"]]
        .sum()
        .rename(columns={"diplomatic_activity_score": "DiplomaticActivity"})
        .sort_values("date")
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(daily["date"], daily["EscalationPressure"], marker="o", linewidth=2, label="EscalationPressure")
    ax.plot(daily["date"], daily["DiplomaticActivity"], marker="s", linewidth=2, label="DiplomaticActivity")
    ax.set_title("Escalation Intensity Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Index Value")
    ax.tick_params(axis="x", rotation=45)
    ax.legend()
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, "escalation_intensity.png"), dpi=200)
    plt.close(fig)


def save_actor_behavior_heatmaps(coding: pd.DataFrame, output_dir: str) -> None:
    dates = sorted(coding["date"].dropna().unique().tolist())
    fig, axes = plt.subplots(len(METRIC_COLUMNS), 1, figsize=(12, 12), constrained_layout=True)
    if len(METRIC_COLUMNS) == 1:
        axes = [axes]

    for ax, (column, title) in zip(axes, METRIC_COLUMNS):
        pivot = (
            coding.pivot_table(index="actor", columns="date", values=column, aggfunc="mean")
            .reindex(ACTOR_ORDER)
            .reindex(columns=dates)
            .fillna(0)
        )
        image = ax.imshow(pivot.values, aspect="auto", vmin=0, vmax=3)
        ax.set_title(f"{title} Heatmap")
        ax.set_yticks(range(len(pivot.index)))
        ax.set_yticklabels(pivot.index)
        ax.set_xticks(range(len(pivot.columns)))
        ax.set_xticklabels(pivot.columns, rotation=45, ha="right")
        fig.colorbar(image, ax=ax, fraction=0.02, pad=0.02)

    fig.savefig(os.path.join(output_dir, "actor_behavior_heatmaps.png"), dpi=200)
    plt.close(fig)


def save_geographic_conflict_map(summary: pd.DataFrame, output_dir: str) -> None:
    plotted = summary.copy()
    plotted["plot_x"] = plotted["primary_theater"].map(lambda x: THEATER_COORDS.get(x, THEATER_COORDS["MultiTheater"])[0])
    plotted["plot_y"] = plotted["primary_theater"].map(lambda x: THEATER_COORDS.get(x, THEATER_COORDS["MultiTheater"])[1])
    plotted["size"] = (
        plotted["avg_military_activity"].fillna(0)
        + plotted["avg_infrastructure_coercion"].fillna(0)
        + plotted["avg_maritime_pressure"].fillna(0)
        + 1
    ) * 110

    fig, ax = plt.subplots(figsize=(10, 7))
    ax.set_title("Geographic Conflict Map (Theater-Level)")
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 8)
    ax.set_xticks([])
    ax.set_yticks([])

    for theater, (x, y) in THEATER_COORDS.items():
        ax.text(x, y, theater, ha="center", va="center", fontsize=9, alpha=0.45)

    for _, row in plotted.iterrows():
        actor = row["actor"]
        ax.scatter(
            row["plot_x"],
            row["plot_y"],
            s=row["size"],
            color=ACTOR_COLORS.get(actor, "#333333"),
            alpha=0.7,
        )
        ax.text(row["plot_x"], row["plot_y"] + 0.28, actor, ha="center", va="bottom", fontsize=9)

    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, "geographic_conflict_map.png"), dpi=200)
    plt.close(fig)


def select_trigger_rows(coding: pd.DataFrame) -> List[pd.Series]:
    working = coding.copy()
    working["weight"] = (
        working["military_activity_score"].fillna(0)
        + working["infrastructure_coercion_score"].fillna(0)
        + working["maritime_pressure_score"].fillna(0)
    )
    working = working[
        working["key_trigger"].fillna("").str.strip().ne("")
        & working["key_response"].fillna("").str.strip().ne("")
    ]
    working = working.sort_values(["weight", "date"], ascending=[False, True])
    return [row for _, row in working.head(5).iterrows()]


def save_trigger_response_flow(coding: pd.DataFrame, output_dir: str) -> None:
    rows = select_trigger_rows(coding)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_title("Trigger-Response Flow")
    ax.axis("off")

    if not rows:
        ax.text(0.5, 0.5, "No trigger-response data available", ha="center", va="center", fontsize=12)
    else:
        y_positions = list(reversed([0.14 + i * 0.18 for i in range(len(rows))]))
        for y, row in zip(y_positions, rows):
            trigger_text = f"{row['date']} | {row['actor']} trigger\n{row['key_trigger']}"
            response_text = f"{row['date']} | {row['actor']} response\n{row['key_response']}"
            ax.text(
                0.18,
                y,
                trigger_text,
                ha="center",
                va="center",
                bbox=dict(boxstyle="round,pad=0.4", fc="#eef3ff", ec="#4a6fa5"),
            )
            ax.text(
                0.82,
                y,
                response_text,
                ha="center",
                va="center",
                bbox=dict(boxstyle="round,pad=0.4", fc="#fff1e8", ec="#c97b3b"),
            )
            ax.annotate("", xy=(0.67, y), xytext=(0.33, y), arrowprops=dict(arrowstyle="->", lw=1.8))

    fig.tight_layout()
    fig.savefig(os.path.join(output_dir, "trigger_response_flow.png"), dpi=200)
    plt.close(fig)


def main() -> None:
    args = parse_args()
    ensure_output_dir(args.output_dir)
    coding = pd.read_csv(args.coding_csv)
    summary = pd.read_csv(args.summary_csv)

    save_escalation_intensity(coding, args.output_dir)
    save_actor_behavior_heatmaps(coding, args.output_dir)
    save_geographic_conflict_map(summary, args.output_dir)
    save_trigger_response_flow(coding, args.output_dir)


if __name__ == "__main__":
    main()
