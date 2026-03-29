import argparse
import os
from typing import Dict, List

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.lines import Line2D
import textwrap


ACTOR_ORDER = ["US", "Israel", "Iran", "Hezbollah", "IraqiPartnerForces", "Houthis"]
METRIC_COLUMNS = [
    ("military_activity_score", "Military"),
    ("diplomatic_activity_score", "Diplomacy"),
    ("proxy_activity_score", "Proxy"),
    ("infrastructure_coercion_score", "Infrastructure"),
    ("maritime_pressure_score", "Maritime"),
]

THEATER_COORDS: Dict[str, tuple] = {
    "Iran": (7.0, 7.5),
    "Israel": (2.5, 5.5),
    "Lebanon": (2.0, 7.5),
    "Iraq": (4.5, 6.5),
    "YemenRedSea": (2.0, 2.0),
    "GulfHormuz": (7.0, 3.0),
    "MultiTheater": (9.0, 6.5),
    "Diplomatic": (9.0, 2.0),
}

ACTOR_COLORS: Dict[str, str] = {
    "US": "#1f77b4",
    "Israel": "#ff7f0e",
    "Iran": "#2ca02c",
    "Hezbollah": "#d62728",
    "IraqiPartnerForces": "#9467bd",
    "Houthis": "#8c564b",
}

ACTOR_OFFSETS: Dict[str, tuple] = {
    "US": (-1.5, 0.5),
    "Israel": (0.0, 1.0),
    "Iran": (1.5, 0.0),
    "Hezbollah": (-0.8, 0.5),
    "IraqiPartnerForces": (0.0, 1.0),
    "Houthis": (0.0, -1.0),
}

ACTOR_LABEL_OFFSETS: Dict[str, tuple] = {
    "US": (0.0, 0.5),
    "Israel": (0.0, 0.5),
    "Iran": (0.0, -0.5),
    "Hezbollah": (0.0, 0.5),
    "IraqiPartnerForces": (0.0, 0.5),
    "Houthis": (0.0, -0.5),
}

THEATER_LABEL_OFFSETS: Dict[str, tuple] = {
    "Iran": (0.0, -0.4),
    "Israel": (0.0, -0.4),
    "Lebanon": (0.0, -0.4),
    "Iraq": (0.0, -0.4),
    "YemenRedSea": (0.0, 0.4),
    "GulfHormuz": (0.0, -0.4),
    "MultiTheater": (0.0, 0.0),
    "Diplomatic": (0.0, 0.0),
}

DISPLAY_LABELS: Dict[str, str] = {
    "US": "US",
    "Israel": "Israel",
    "Iran": "Iran",
    "Hezbollah": "Hezbollah",
    "IraqiPartnerForces": "Iraqi Partner Forces",
    "Houthis": "Houthis",
    "YemenRedSea": "Yemen / Red Sea",
    "GulfHormuz": "Hormuz / Gulf",
    "MultiTheater": "Multi-Theater",
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
    date_labels = pd.to_datetime(dates).strftime("%m-%d").tolist()
    columns = 2
    rows = (len(METRIC_COLUMNS) + columns - 1) // columns
    fig, axes = plt.subplots(rows, columns, figsize=(10, 10), constrained_layout=True)
    if hasattr(axes, "flatten"):
        axes = axes.flatten()
    else:
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
        ax.set_xticklabels(date_labels, rotation=45, ha="right")
        fig.colorbar(image, ax=ax, fraction=0.02, pad=0.02)

    for ax in axes[len(METRIC_COLUMNS) :]:
        ax.axis("off")

    fig.savefig(os.path.join(output_dir, "actor_behavior_heatmaps.png"), dpi=200)
    plt.close(fig)


def relationship_specs() -> List[Dict[str, str]]:
    return [
        {"source": "Israel", "target": "Iran", "label": "strike expansion", "curve": 0.1, "label_dx": 0.6, "label_dy": 0.0},
        {"source": "Iran", "target": "GulfHormuz", "label": "selective access pressure", "curve": -0.2, "label_dx": 0.0, "label_dy": -0.5},
        {"source": "Iran", "target": "Israel", "label": "missile and drone retaliation", "curve": 0.1, "label_dx": 0.0, "label_dy": 0.4},
        {"source": "US", "target": "GulfHormuz", "label": "security and bargaining focus", "curve": 0.2, "label_dx": -0.2, "label_dy": -0.4},
        {"source": "Hezbollah", "target": "Israel", "label": "active-bounded front", "curve": -0.1, "label_dx": -0.5, "label_dy": 0.0},
        {"source": "Houthis", "target": "YemenRedSea", "label": "latent entry signal", "curve": 0.2, "label_dx": 0.6, "label_dy": 0.0},
        {"source": "IraqiPartnerForces", "target": "Iraq", "label": "reserve escalation lane", "curve": 0.2, "label_dx": 0.7, "label_dy": 0.0},
    ]


def actor_pressure_score(row: pd.Series) -> float:
    return (
        row["avg_military_activity"]
        + row["avg_infrastructure_coercion"]
        + row["avg_maritime_pressure"]
        + (row["avg_proxy_activity"] * 0.7)
    )


def save_geographic_conflict_map(summary: pd.DataFrame, output_dir: str) -> None:
    plotted = summary.copy()
    plotted["theater_x"] = plotted["primary_theater"].map(lambda x: THEATER_COORDS.get(x, THEATER_COORDS["MultiTheater"])[0])
    plotted["theater_y"] = plotted["primary_theater"].map(lambda x: THEATER_COORDS.get(x, THEATER_COORDS["MultiTheater"])[1])
    plotted["offset_x"] = plotted["actor"].map(lambda x: ACTOR_OFFSETS.get(x, (0.35, 0.35))[0])
    plotted["offset_y"] = plotted["actor"].map(lambda x: ACTOR_OFFSETS.get(x, (0.35, 0.35))[1])
    plotted["actor_x"] = plotted["theater_x"] + plotted["offset_x"]
    plotted["actor_y"] = plotted["theater_y"] + plotted["offset_y"]
    plotted["pressure_score"] = plotted.apply(actor_pressure_score, axis=1)
    plotted["node_size"] = (plotted["pressure_score"] + 1.2) * 180

    actor_lookup = plotted.set_index("actor").to_dict("index")

    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_title("Geographic Conflict Map (Theater Interaction)")
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 10)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor("#fbfbfc")

    for theater, (x, y) in THEATER_COORDS.items():
        ax.scatter(x, y, s=1200, color="#edf1f5", edgecolor="#b8c2cc", linewidth=1.2, zorder=1)
        label_dx, label_dy = THEATER_LABEL_OFFSETS.get(theater, (0.0, 0.0))
        ax.text(
            x + label_dx,
            y + label_dy,
            DISPLAY_LABELS.get(theater, theater),
            ha="center",
            va="center",
            fontsize=9,
            color="#54606c",
            zorder=2,
        )

    for spec in relationship_specs():
        source = actor_lookup.get(spec["source"])
        target_xy = THEATER_COORDS.get(spec["target"])
        if not source or not target_xy:
            continue
        line_width = 1.5 + (source["pressure_score"] * 0.32)
        ax.annotate(
            "",
            xy=target_xy,
            xytext=(source["actor_x"], source["actor_y"]),
            arrowprops=dict(
                arrowstyle="->",
                color=ACTOR_COLORS.get(spec["source"], "#333333"),
                lw=line_width,
                alpha=0.85,
                shrinkA=12,
                shrinkB=14,
                connectionstyle=f"arc3,rad={spec.get('curve', 0.0)}",
            ),
            zorder=2,
        )
        mid_x = (source["actor_x"] + target_xy[0]) / 2 + spec.get("label_dx", 0.0)
        mid_y = (source["actor_y"] + target_xy[1]) / 2 + spec.get("label_dy", 0.0)
        ax.text(
            mid_x,
            mid_y,
            spec["label"],
            fontsize=9.5,
            color=ACTOR_COLORS.get(spec["source"], "#333333"),
            ha="center",
            va="center",
            bbox=dict(boxstyle="round,pad=0.25", fc="#ffffff", ec="none", alpha=0.95),
            zorder=4,
        )

    for _, row in plotted.iterrows():
        actor = row["actor"]
        ax.scatter(
            row["actor_x"],
            row["actor_y"],
            s=row["node_size"],
            color=ACTOR_COLORS.get(actor, "#333333"),
            edgecolor="white",
            linewidth=1.6,
            alpha=0.95,
            zorder=3,
        )
        label_dx, label_dy = ACTOR_LABEL_OFFSETS.get(actor, (0.0, 0.45))
        ax.text(
            row["actor_x"] + label_dx,
            row["actor_y"] + label_dy,
            f"{DISPLAY_LABELS.get(actor, actor)}\n{row['dominant_weekly_posture']} | {row['trend_vs_prior_week']}",
            ha="center",
            va="center",
            fontsize=9.5,
            color="#1f2937",
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=ACTOR_COLORS.get(actor, "#333333"), lw=1.5, alpha=0.98),
            zorder=5,
        )

    legend_items = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor="#64748b", markeredgecolor="white", markersize=9, label="Actor node"),
        Line2D([0], [0], marker="o", color="w", markerfacecolor="#edf1f5", markeredgecolor="#b8c2cc", markersize=9, label="Theater node"),
        Line2D([0], [0], color="#334155", lw=2.0, label="Direction of weekly pressure"),
    ]
    ax.legend(handles=legend_items, loc="lower right", frameon=True, framealpha=0.95, fontsize=8)
    ax.text(
        0.02,
        0.02,
        "Node size scales with military + infrastructure + maritime pressure.\nArrow width reflects source-actor pressure intensity.",
        transform=ax.transAxes,
        ha="left",
        va="bottom",
        fontsize=8,
        color="#475569",
    )

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
    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_title("Trigger-Response Flow")
    ax.axis("off")

    if not rows:
        ax.text(0.5, 0.5, "No trigger-response data available", ha="center", va="center", fontsize=12)
    else:
        y_positions = list(reversed([0.1 + i * 0.2 for i in range(len(rows))]))
        for y, row in zip(y_positions, rows):
            wrapped_trigger = "\n".join(textwrap.wrap(str(row['key_trigger']), width=35))
            wrapped_response = "\n".join(textwrap.wrap(str(row['key_response']), width=35))
            trigger_text = f"{row['date']} | {row['actor']} trigger\n\n{wrapped_trigger}"
            response_text = f"{row['date']} | {row['actor']} response\n\n{wrapped_response}"
            ax.text(
                0.20,
                y,
                trigger_text,
                ha="center",
                va="center",
                fontsize=10,
                bbox=dict(boxstyle="round,pad=0.6", fc="#eef3ff", ec="#4a6fa5", lw=1.5),
            )
            ax.text(
                0.80,
                y,
                response_text,
                ha="center",
                va="center",
                fontsize=10,
                bbox=dict(boxstyle="round,pad=0.6", fc="#fff1e8", ec="#c97b3b", lw=1.5),
            )
            ax.annotate("", xy=(0.62, y), xytext=(0.38, y), arrowprops=dict(arrowstyle="->", lw=2.5, color="#64748b"))

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
