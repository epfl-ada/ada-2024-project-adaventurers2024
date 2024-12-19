import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

from ..utils.visualization_utils import (
    create_genre_colors,
    hex_to_rgb,
    prepare_color_map,
)


def plot_seasonal_distributions(df):
    """Plot profit and rating distributions by season."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Profit by Season
    sns.violinplot(
        data=df,
        x="release_season",
        y="profit_scaled",
        ax=ax1,
        palette="viridis",
        hue="release_season",
        legend=False,
    )
    ax1.set_yscale("symlog", linthresh=1)
    ax1.set_title("Movie Profits Distribution by Season", pad=20)
    ax1.set_ylabel("Profit (Millions USD, Log Scale)")
    ax1.tick_params(axis="x", rotation=45)
    ax1.grid(True, alpha=0.3)

    # Ratings by Season
    sns.violinplot(
        data=df,
        x="release_season",
        y="vote_average",
        ax=ax2,
        palette="viridis",
        hue="release_season",
        legend=False,
    )
    ax2.set_title("Movie Rating Distribution by Season", pad=20)
    ax2.set_ylabel("Average Rating (0-10)")
    ax2.tick_params(axis="x", rotation=45)
    ax2.grid(True, alpha=0.3)
    for y in [5, 6, 7]:
        ax2.axhline(y=y, color="gray", linestyle="--", alpha=0.3)

    plt.tight_layout()
    plt.show()

    # Print statistics
    seasonal_stats = (
        df.groupby("release_season")
        .agg(
            {
                "profit_scaled": ["mean", "median"],
                "vote_average": ["mean", "count"],
                "roi_clean": ["mean", "median"],
            }
        )
        .round(2)
    )

    print("\nSummary Statistics by Season:")
    print(seasonal_stats)

    return seasonal_stats


def analyze_monthly_performance(df):
    """Analyze and visualize monthly performance patterns."""
    # Distribution plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))

    # Profit Distribution
    sns.violinplot(
        data=df,
        x="release_month",
        y="profit_scaled",
        ax=ax1,
        palette="viridis",
        hue="release_month",
        legend=False,
    )
    ax1.set_yscale("symlog", linthresh=1)
    ax1.set_title("Movie Profits Distribution by Release Month", pad=20)
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Profit (Millions USD, Log Scale)")
    ax1.grid(True, alpha=0.3)

    # Rating Distribution
    sns.violinplot(
        data=df,
        x="release_month",
        y="vote_average",
        ax=ax2,
        palette="viridis",
        hue="release_month",
        legend=False,
    )
    ax2.set_title("Movie Rating Distribution by Release Month", pad=20)
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Average Rating (0-10)")
    ax2.grid(True, alpha=0.3)
    for y in [5, 6, 7]:
        ax2.axhline(y=y, color="gray", linestyle="--", alpha=0.3)

    plt.tight_layout()
    plt.show()


def analyze_monthly_roi(df):
    """Analyze ROI patterns by month."""
    # ROI Distribution
    plt.figure(figsize=(14, 6))
    sns.violinplot(
        data=df[df["roi_clean"].notna()],
        x="release_month",
        y="roi_clean",
        palette="viridis",
        hue="release_month",
        legend=False,
    )
    plt.title("ROI Distribution by Release Month", pad=20)
    plt.ylabel("Return on Investment (ROI)")
    plt.xlabel("Month")
    plt.yscale("symlog", linthresh=0.1)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Calculate monthly performance rates
    monthly_performance = {}
    for month in range(1, 13):
        month_data = df[df["release_month"] == month]["roi_clean"]
        rates = {
            "Severe Loss (>70%)": (month_data < -0.7).mean(),
            "Significant Loss (>50%)": (month_data < -0.5).mean(),
            "Break Even": (month_data > 0).mean(),
            "Successful (>100%)": (month_data > 1).mean(),
            "Very Successful (>200%)": (month_data > 2).mean(),
        }
        monthly_performance[month] = rates

    return pd.DataFrame(monthly_performance).T.round(3) * 100


def plot_monthly_success_rates(monthly_perf_df):
    """Plot monthly success and failure rates."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Success rates
    monthly_perf_df["Successful (>100%)"].plot(
        kind="bar", ax=ax1, color=sns.color_palette("viridis", 12)
    )
    ax1.set_title("Success Rate by Month (>100% ROI)", pad=20)
    ax1.set_xlabel("Month")
    ax1.set_ylabel("Success Rate (%)")
    plt.setp(ax1.get_xticklabels(), rotation=45, ha="right")
    ax1.grid(True, alpha=0.3)

    # Failure rates
    monthly_perf_df["Significant Loss (>50%)"].plot(
        kind="bar", ax=ax2, color=sns.color_palette("viridis", 12)
    )
    ax2.set_title("Failure Rate by Month (>50% Loss)", pad=20)
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Failure Rate (%)")
    plt.setp(ax2.get_xticklabels(), rotation=45, ha="right")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()


def analyze_monthly_statistics(df, monthly_perf_df):
    """Calculate and print detailed monthly statistics."""
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    # ROI statistics
    monthly_roi_stats = (
        df.groupby("release_month")["roi_clean"]
        .agg(
            [
                "count",
                "mean",
                "median",
                lambda x: x.quantile(0.25),
                lambda x: x.quantile(0.75),
                lambda x: x.std(),
            ]
        )
        .round(3)
    )
    monthly_roi_stats.columns = [
        "Count",
        "Mean ROI",
        "Median ROI",
        "25th Percentile",
        "75th Percentile",
        "Std Dev",
    ]
    monthly_roi_stats.index = [month_names[m] for m in monthly_roi_stats.index]

    # Best and worst months
    best_months = monthly_perf_df["Successful (>100%)"].nlargest(3)
    worst_months = monthly_perf_df["Significant Loss (>50%)"].nlargest(3)

    # Risk-adjusted performance
    monthly_perf_df["Risk-Adjusted Performance"] = (
        monthly_perf_df["Successful (>100%)"]
        / monthly_perf_df["Significant Loss (>50%)"]
    ).round(2)

    return {
        "roi_stats": monthly_roi_stats,
        "best_months": best_months,
        "worst_months": worst_months,
        "risk_adjusted": monthly_perf_df["Risk-Adjusted Performance"].sort_values(
            ascending=False
        ),
    }


def analyze_temporal_trends(df):
    """Analyze and visualize performance trends over time."""
    df["release_year"] = pd.to_numeric(df["release_year"])
    yearly_performance = df.groupby("release_year").agg(
        success_rate=("roi_clean", lambda x: (x > 1).mean()),
        failure_rate=("roi_clean", lambda x: (x < -0.5).mean()),
        movie_count=("roi_clean", "count"),
    )

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot rates
    line1 = ax1.plot(
        yearly_performance.index,
        yearly_performance["success_rate"] * 100,
        color="forestgreen",
        linewidth=2,
        label="Success Rate (>100% ROI)",
    )
    line2 = ax1.plot(
        yearly_performance.index,
        yearly_performance["failure_rate"] * 100,
        color="crimson",
        linewidth=2,
        label="Failure Rate (>50% Loss)",
    )
    ax1.set_xlabel("Release Year")
    ax1.set_ylabel("Rate (%)", color="black")
    ax1.tick_params(axis="y", labelcolor="black")
    ax1.grid(True, alpha=0.3)

    # Add movie count
    ax2 = ax1.twinx()
    bars = ax2.bar(
        yearly_performance.index,
        yearly_performance["movie_count"],
        alpha=0.2,
        color="royalblue",
        label="Number of Movies",
    )
    ax2.set_ylabel("Number of Movies", color="royalblue")
    ax2.tick_params(axis="y", labelcolor="royalblue")

    # Legend
    lines = line1 + line2 + [bars]
    labels = [l.get_label() for l in line1 + line2] + ["Number of Movies"]
    ax1.legend(lines, labels, loc="upper left")

    plt.title("Movie Success, Failure Rates and Volume Over Time", pad=20)
    plt.tight_layout()
    plt.show()

    return yearly_performance


def run_timing_analysis(df):
    """Run complete timing analysis pipeline."""
    results = {}

    # Seasonal analysis
    results["seasonal_stats"] = plot_seasonal_distributions(df)

    # Monthly analysis
    analyze_monthly_performance(df)
    monthly_perf_df = analyze_monthly_roi(df)
    plot_monthly_success_rates(monthly_perf_df)
    results["monthly_stats"] = analyze_monthly_statistics(df, monthly_perf_df)

    # Temporal analysis
    results["yearly_performance"] = analyze_temporal_trends(df)

    return results


def create_interactive_seasonal_distributions(df):
    """Create interactive seasonal distribution plots with statistical characteristics."""
    # Create combined figure with subplots
    fig = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=(
            "Profit Statistics by Season",
            "Rating Statistics by Season",
            "ROI Statistics by Season",
            "Performance Metrics by Season",
        ),
        specs=[
            [{}, {}],
            [{}, {"secondary_y": True}],
        ],  # Enable secondary y-axis for last subplot
    )

    seasons = ["Winter", "Spring", "Summer", "Fall"]
    colors = px.colors.qualitative.Set3

    # Calculate statistics for each metric
    seasonal_stats = {
        "profit": df.groupby("release_season")["profit_scaled"]
        .agg(
            [
                ("mean", "mean"),
                ("std", "std"),
                ("median", "median"),
                ("percentile_25", lambda x: x.quantile(0.25)),
                ("percentile_75", lambda x: x.quantile(0.75)),
            ]
        )
        .round(2),
        "rating": df.groupby("release_season")["vote_average"]
        .agg(
            [
                ("mean", "mean"),
                ("std", "std"),
                ("median", "median"),
                ("percentile_25", lambda x: x.quantile(0.25)),
                ("percentile_75", lambda x: x.quantile(0.75)),
            ]
        )
        .round(2),
        "roi": df.groupby("release_season")["roi_clean"]
        .agg(
            [
                ("mean", "mean"),
                ("std", "std"),
                ("median", "median"),
                ("percentile_25", lambda x: x.quantile(0.25)),
                ("percentile_75", lambda x: x.quantile(0.75)),
            ]
        )
        .round(2),
    }

    # Function to transform values for log scale while handling negative values
    def log_transform(x):
        return np.sign(x) * np.log10(np.abs(x) + 1)

    # Transform profit statistics for log scale
    profit_stats_log = seasonal_stats["profit"].copy()
    for col in ["mean", "std", "median", "percentile_25", "percentile_75"]:
        profit_stats_log[f"{col}_log"] = log_transform(profit_stats_log[col])

    # Function to add statistical traces
    def add_stat_traces(
        stats, row, col, metric_name, value_prefix="", legend_group="", log_scale=False
    ):
        if log_scale:
            y_values = stats["mean_log"].values
            error_y_values = stats["std_log"].values
            percentile_75_values = stats["percentile_75_log"].values
            percentile_25_values = stats["percentile_25_log"].values
            median_values = stats["median_log"].values
            # Original values for hover text
            hover_values = stats["mean"].values
            hover_std = stats["std"].values
            hover_75 = stats["percentile_75"].values
            hover_25 = stats["percentile_25"].values
            hover_median = stats["median"].values
        else:
            y_values = stats["mean"].values
            error_y_values = stats["std"].values
            percentile_75_values = stats["percentile_75"].values
            percentile_25_values = stats["percentile_25"].values
            median_values = stats["median"].values
            hover_values = y_values
            hover_std = error_y_values
            hover_75 = percentile_75_values
            hover_25 = percentile_25_values
            hover_median = median_values

        sample_sizes = df.groupby("release_season").size().values

        # Add mean with error bars
        fig.add_trace(
            go.Bar(
                name=f"Mean {metric_name}",
                x=stats.index,
                y=y_values,
                error_y=dict(type="data", array=error_y_values, visible=True),
                marker_color=colors[0],
                legendgroup=legend_group,
                hovertemplate="<b>Season:</b> %{x}<br>"
                + f"<b>Mean {metric_name}:</b> {value_prefix}%{{customdata[0]:.2f}}<br>"
                + f"<b>Std Dev:</b> {value_prefix}%{{customdata[1]:.2f}}<br>"
                + "<b>Sample Size:</b> %{customdata[2]}<extra></extra>",
                customdata=np.vstack((hover_values, hover_std, sample_sizes)).T,
            ),
            row=row,
            col=col,
        )

        # Add quartile ranges
        fig.add_trace(
            go.Scatter(
                name="Interquartile Range",
                x=stats.index,
                y=percentile_75_values,
                mode="lines",
                line=dict(width=0),
                legendgroup=legend_group,
                showlegend=False,
                customdata=hover_75,
                hovertemplate=f"<b>75th Percentile:</b> {value_prefix}%{{customdata:.2f}}<extra></extra>",
            ),
            row=row,
            col=col,
        )

        fig.add_trace(
            go.Scatter(
                name="Interquartile Range",
                x=stats.index,
                y=percentile_25_values,
                mode="lines",
                fill="tonexty",
                line=dict(width=0),
                fillcolor="rgba(128, 128, 128, 0.2)",
                legendgroup=legend_group,
                showlegend=True,
                customdata=hover_25,
                hovertemplate=f"<b>25th Percentile:</b> {value_prefix}%{{customdata:.2f}}<extra></extra>",
            ),
            row=row,
            col=col,
        )

        # Add median line
        fig.add_trace(
            go.Scatter(
                name="Median",
                x=stats.index,
                y=median_values,
                mode="markers",
                marker=dict(symbol="line-ns", size=20, color="black"),
                legendgroup=legend_group,
                showlegend=True,
                customdata=hover_median,
                hovertemplate=f"<b>Median:</b> {value_prefix}%{{customdata:.2f}}<extra></extra>",
            ),
            row=row,
            col=col,
        )

    # Add statistical traces for each metric with separate legend groups
    add_stat_traces(profit_stats_log, 1, 1, "Profit", "$", "profit", log_scale=True)
    add_stat_traces(seasonal_stats["rating"], 1, 2, "Rating", "", "rating")
    add_stat_traces(seasonal_stats["roi"], 2, 1, "ROI", "", "roi")

    # Success Metrics with dual y-axis
    seasonal_metrics = (
        df.groupby("release_season")
        .agg(
            {
                "profit_scaled": "mean",
                "vote_average": "mean",
                "roi_clean": lambda x: (x > 1).mean() * 100,  # Success rate
            }
        )
        .round(2)
    )

    # Add profit bars
    fig.add_trace(
        go.Bar(
            name="Average Profit",
            x=seasons,
            y=seasonal_metrics["profit_scaled"],
            marker_color=colors[0],
            legendgroup="performance",
            hovertemplate="<b>Season:</b> %{x}<br>"
            + "<b>Average Profit:</b> $%{y:.2f}M<br>"
            + "<extra></extra>",
        ),
        row=2,
        col=2,
        secondary_y=False,
    )

    # Add rating line
    fig.add_trace(
        go.Scatter(
            name="Average Rating",
            x=seasons,
            y=seasonal_metrics["vote_average"],
            mode="lines+markers",
            marker_color=colors[2],
            line_color=colors[2],
            legendgroup="performance",
            hovertemplate="<b>Season:</b> %{x}<br>"
            + "<b>Average Rating:</b> %{y:.2f}<br>"
            + "<extra></extra>",
        ),
        row=2,
        col=2,
        secondary_y=True,
    )

    # Update layout
    fig.update_layout(
        height=800,
        showlegend=True,
        title_text="Seasonal Movie Performance Analysis",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5,
            traceorder="grouped",
        ),
    )

    # Create custom tick values and labels for the profit y-axis
    tick_values = [-2, -1, 0, 1, 2, 3]
    tick_labels = [
        f"${'-' if v < 0 else ''}{10 ** abs(v) - 1:.0f}M" for v in tick_values
    ]

    # Update axes
    fig.update_yaxes(
        title_text="Profit (Millions USD, log scale)",
        row=1,
        col=1,
        tickmode="array",
        tickvals=tick_values,
        ticktext=tick_labels,
    )
    fig.update_yaxes(title_text="Rating (0-10)", row=1, col=2)
    fig.update_yaxes(title_text="ROI", row=2, col=1)
    fig.update_yaxes(
        title_text="Profit (Millions USD)", secondary_y=False, row=2, col=2
    )
    fig.update_yaxes(title_text="Average Rating", secondary_y=True, row=2, col=2)

    return fig, seasonal_metrics


def create_interactive_monthly_performance(df):
    """Create interactive monthly performance analysis with statistical characteristics."""
    # Create figure with subplots
    fig = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=(
            "Monthly Profit Statistics",
            "Monthly Rating Statistics",
            "Monthly ROI Trends",
            "Monthly Success Metrics",
        ),
        specs=[[{}, {}], [{"type": "heatmap"}, {"secondary_y": True}]],
        vertical_spacing=0.15,
        horizontal_spacing=0.12,
    )

    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    # Calculate monthly statistics
    monthly_stats = {
        "profit": df.groupby("release_month")["profit_scaled"]
        .agg(
            [
                ("mean", "mean"),
                ("std", "std"),
                ("median", "median"),
                ("percentile_25", lambda x: x.quantile(0.25)),
                ("percentile_75", lambda x: x.quantile(0.75)),
            ]
        )
        .round(2),
        "rating": df.groupby("release_month")["vote_average"]
        .agg(
            [
                ("mean", "mean"),
                ("std", "std"),
                ("median", "median"),
                ("percentile_25", lambda x: x.quantile(0.25)),
                ("percentile_75", lambda x: x.quantile(0.75)),
            ]
        )
        .round(2),
    }

    # Function to transform values for log scale while handling negative values
    def log_transform(x):
        return np.sign(x) * np.log10(np.abs(x) + 1)

    # Transform profit statistics for log scale
    profit_stats_log = monthly_stats["profit"].copy()
    for col in ["mean", "std", "median", "percentile_25", "percentile_75"]:
        profit_stats_log[f"{col}_log"] = log_transform(profit_stats_log[col])

    # Function to add statistical traces
    def add_stat_traces(
        stats, row, col, metric_name, value_prefix="", legend_group="", log_scale=False
    ):
        x_values = [month_names[i] for i in range(1, 13)]

        if log_scale:
            y_values = stats["mean_log"].values
            error_values = stats["std_log"].values
            percentile_75_values = stats["percentile_75_log"].values
            percentile_25_values = stats["percentile_25_log"].values
            median_values = stats["median_log"].values
            # Original values for hover text
            hover_values = stats["mean"].values
            hover_std = stats["std"].values
            hover_75 = stats["percentile_75"].values
            hover_25 = stats["percentile_25"].values
            hover_median = stats["median"].values
        else:
            y_values = stats["mean"].values
            error_values = stats["std"].values
            percentile_75_values = stats["percentile_75"].values
            percentile_25_values = stats["percentile_25"].values
            median_values = stats["median"].values
            hover_values = y_values
            hover_std = error_values
            hover_75 = percentile_75_values
            hover_25 = percentile_25_values
            hover_median = median_values

        sample_sizes = df.groupby("release_month").size().values

        # Add mean with error bars
        fig.add_trace(
            go.Bar(
                name=f"Mean {metric_name}",
                x=x_values,
                y=y_values,
                error_y=dict(type="data", array=error_values, visible=True),
                legendgroup=legend_group,
                hovertemplate="<b>Month:</b> %{x}<br>"
                + f"<b>Mean {metric_name}:</b> {value_prefix}%{{customdata[0]:.2f}}<br>"
                + f"<b>Std Dev:</b> {value_prefix}%{{customdata[1]:.2f}}<br>"
                + "<b>Sample Size:</b> %{customdata[2]}<extra></extra>",
                customdata=np.vstack((hover_values, hover_std, sample_sizes)).T,
            ),
            row=row,
            col=col,
        )

        # Add quartile ranges
        fig.add_trace(
            go.Scatter(
                name="Interquartile Range",
                x=x_values,
                y=percentile_75_values,
                mode="lines",
                line=dict(width=0),
                legendgroup=legend_group,
                showlegend=False,
                customdata=hover_75,
                hovertemplate=f"<b>75th Percentile:</b> {value_prefix}%{{customdata:.2f}}<extra></extra>",
            ),
            row=row,
            col=col,
        )

        fig.add_trace(
            go.Scatter(
                name="Interquartile Range",
                x=x_values,
                y=percentile_25_values,
                mode="lines",
                fill="tonexty",
                line=dict(width=0),
                fillcolor="rgba(128, 128, 128, 0.2)",
                legendgroup=legend_group,
                showlegend=True,
                customdata=hover_25,
                hovertemplate=f"<b>25th Percentile:</b> {value_prefix}%{{customdata:.2f}}<extra></extra>",
            ),
            row=row,
            col=col,
        )

        # Add median line
        fig.add_trace(
            go.Scatter(
                name="Median",
                x=x_values,
                y=median_values,
                mode="markers",
                marker=dict(symbol="line-ns", size=20, color="black"),
                legendgroup=legend_group,
                showlegend=True,
                customdata=hover_median,
                hovertemplate=f"<b>Median:</b> {value_prefix}%{{customdata:.2f}}<extra></extra>",
            ),
            row=row,
            col=col,
        )

    # Add statistical traces for profit and rating
    add_stat_traces(profit_stats_log, 1, 1, "Profit", "$", "profit", log_scale=True)
    add_stat_traces(monthly_stats["rating"], 1, 2, "Rating", "", "rating")

    # Monthly ROI Heatmap
    roi_metrics = pd.DataFrame(
        {
            "Severe Loss": [
                (df[df["release_month"] == m]["roi_clean"] < -0.7).mean() * 100
                for m in range(1, 13)
            ],
            "Moderate Loss": [
                (df[df["release_month"] == m]["roi_clean"].between(-0.7, -0.3)).mean()
                * 100
                for m in range(1, 13)
            ],
            "Break Even": [
                (df[df["release_month"] == m]["roi_clean"].between(-0.3, 0.3)).mean()
                * 100
                for m in range(1, 13)
            ],
            "Moderate Success": [
                (df[df["release_month"] == m]["roi_clean"].between(0.3, 1)).mean() * 100
                for m in range(1, 13)
            ],
            "High Success": [
                (df[df["release_month"] == m]["roi_clean"] > 1).mean() * 100
                for m in range(1, 13)
            ],
        },
        index=[month_names[m] for m in range(1, 13)],
    )

    fig.add_trace(
        go.Heatmap(
            z=roi_metrics.values,
            x=roi_metrics.columns,
            y=roi_metrics.index,
            colorscale="RdYlBu",
            text=np.round(roi_metrics.values, 1),
            texttemplate="%{text}%",
            textfont={"size": 10},
            hoverongaps=False,
        ),
        row=2,
        col=1,
    )

    # Monthly Success Metrics
    success_metrics = pd.DataFrame(
        {
            "Month": [month_names[m] for m in range(1, 13)],
            "Success_Rate": [
                (df[df["release_month"] == m]["roi_clean"] > 1).mean() * 100
                for m in range(1, 13)
            ],
            "Movie_Count": [len(df[df["release_month"] == m]) for m in range(1, 13)],
        }
    )

    # Add success rate line
    fig.add_trace(
        go.Scatter(
            x=success_metrics["Month"],
            y=success_metrics["Success_Rate"],
            name="Success Rate",
            line=dict(color="green", width=2),
            legendgroup="performance",
            hovertemplate="Month: %{x}<br>Success Rate: %{y:.1f}%<extra></extra>",
        ),
        row=2,
        col=2,
        secondary_y=False,
    )

    # Add movie count bars
    fig.add_trace(
        go.Bar(
            x=success_metrics["Month"],
            y=success_metrics["Movie_Count"],
            name="Movie Count",
            marker_color="rgba(55, 83, 109, 0.3)",
            legendgroup="performance",
            hovertemplate="Month: %{x}<br>Movies: %{y}<extra></extra>",
        ),
        row=2,
        col=2,
        secondary_y=True,
    )

    # Update layout
    fig.update_layout(
        height=1000,
        title_text="Monthly Movie Performance Analysis",
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5,
            traceorder="grouped",
        ),
    )

    # Create custom tick values and labels for the profit y-axis
    tick_values = [-2, -1, 0, 1, 2, 3]
    tick_labels = [
        f"${'-' if v < 0 else ''}{10 ** abs(v) - 1:.0f}M" for v in tick_values
    ]

    # Update axes
    fig.update_xaxes(tickangle=45)
    fig.update_yaxes(
        title_text="Profit (Millions USD, log scale)",
        row=1,
        col=1,
        tickmode="array",
        tickvals=tick_values,
        ticktext=tick_labels,
    )
    fig.update_yaxes(title_text="Rating (0-10)", row=1, col=2)
    fig.update_yaxes(title_text="Success Rate (%)", secondary_y=False, row=2, col=2)
    fig.update_yaxes(title_text="Number of Movies", secondary_y=True, row=2, col=2)

    return fig, monthly_stats, roi_metrics


def create_interactive_temporal_trends(df):
    """Create interactive temporal trend analysis with statistical characteristics."""
    # Create figure with subplots
    fig = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=(
            "ROI Statistics Over Time",
            "Movie Volume and Success Metrics",
            "Seasonal Success Patterns by Decade",
            "Performance Metrics Evolution",
        ),
        specs=[
            [{}, {"secondary_y": True}],
            [{"type": "heatmap"}, {"secondary_y": True}],
        ],
        vertical_spacing=0.15,
        horizontal_spacing=0.12,
    )

    # Calculate yearly statistics
    yearly_stats = {
        "roi": df.groupby("release_year")["roi_clean"].agg(
            [
                ("mean", "mean"),
                ("std", "std"),
                ("median", "median"),
                ("percentile_25", lambda x: x.quantile(0.25)),
                ("percentile_75", lambda x: x.quantile(0.75)),
                ("success_rate", lambda x: (x > 1).mean() * 100),
                ("failure_rate", lambda x: (x < -0.5).mean() * 100),
            ]
        ),
        "profit": df.groupby("release_year")["profit_scaled"].agg(
            [
                ("mean", "mean"),
                ("std", "std"),
                ("median", "median"),
                ("percentile_25", lambda x: x.quantile(0.25)),
                ("percentile_75", lambda x: x.quantile(0.75)),
            ]
        ),
        "rating": df.groupby("release_year")["vote_average"].agg(
            [
                ("mean", "mean"),
                ("std", "std"),
                ("median", "median"),
                ("percentile_25", lambda x: x.quantile(0.25)),
                ("percentile_75", lambda x: x.quantile(0.75)),
            ]
        ),
    }

    # Calculate movie counts
    movie_counts = df.groupby("release_year").size()

    def add_stat_traces(
        stats,
        row,
        col,
        metric_name,
        value_prefix="",
        legend_group="",
        secondary_y=False,
    ):
        """Add statistical traces for a given metric."""
        # Add mean with error bars
        fig.add_trace(
            go.Bar(
                name=f"Mean {metric_name}",
                x=stats.index,
                y=stats["mean"],
                error_y=dict(type="data", array=stats["std"], visible=True),
                legendgroup=legend_group,
                hovertemplate="<b>Year:</b> %{x}<br>"
                + f"<b>Mean {metric_name}:</b> {value_prefix}%{{y:.2f}}<br>"
                + f"<b>Std Dev:</b> {value_prefix}%{{error_y.array:.2f}}<extra></extra>",
            ),
            row=row,
            col=col,
            secondary_y=secondary_y,
        )

        # Add quartile ranges
        fig.add_trace(
            go.Scatter(
                name="Interquartile Range",
                x=stats.index,
                y=stats["percentile_75"],
                mode="lines",
                line=dict(width=0),
                legendgroup=legend_group,
                showlegend=False,
                hovertemplate=f"<b>75th Percentile:</b> {value_prefix}%{{y:.2f}}<extra></extra>",
            ),
            row=row,
            col=col,
            secondary_y=secondary_y,
        )

        fig.add_trace(
            go.Scatter(
                name="Interquartile Range",
                x=stats.index,
                y=stats["percentile_25"],
                mode="lines",
                fill="tonexty",
                line=dict(width=0),
                fillcolor="rgba(128, 128, 128, 0.2)",
                legendgroup=legend_group,
                showlegend=True,
                hovertemplate=f"<b>25th Percentile:</b> {value_prefix}%{{y:.2f}}<extra></extra>",
            ),
            row=row,
            col=col,
            secondary_y=secondary_y,
        )

        # Add median line
        fig.add_trace(
            go.Scatter(
                name="Median",
                x=stats.index,
                y=stats["median"],
                mode="markers",
                marker=dict(symbol="line-ns", size=20, color="black"),
                legendgroup=legend_group,
                showlegend=True,
                hovertemplate=f"<b>Median:</b> {value_prefix}%{{y:.2f}}<extra></extra>",
            ),
            row=row,
            col=col,
            secondary_y=secondary_y,
        )

    # 1. ROI Statistics Plot
    add_stat_traces(yearly_stats["roi"], 1, 1, "ROI", "", "roi")

    # 2. Movie Volume and Success Metrics
    fig.add_trace(
        go.Scatter(
            x=yearly_stats["roi"].index,
            y=yearly_stats["roi"]["success_rate"],
            name="Success Rate",
            line=dict(color="green", width=2),
            legendgroup="success",
            hovertemplate="<b>Year:</b> %{x}<br><b>Success Rate:</b> %{y:.1f}%<extra></extra>",
        ),
        row=1,
        col=2,
    )

    fig.add_trace(
        go.Bar(
            x=yearly_stats["roi"].index,
            y=movie_counts,
            name="Movie Count",
            marker_color="rgba(55, 83, 109, 0.3)",
            legendgroup="success",
            hovertemplate="<b>Year:</b> %{x}<br><b>Movies:</b> %{y}<extra></extra>",
        ),
        row=1,
        col=2,
        secondary_y=True,
    )

    # 3. Improved Seasonal Patterns Heatmap
    # Create decade bins and calculate success rates
    df["decade"] = (df["release_year"] // 10) * 10
    season_order = ["Winter", "Spring", "Summer", "Fall"]

    seasonal_evolution = df.pivot_table(
        index="decade",
        columns="release_season",
        values="roi_clean",
        aggfunc=lambda x: (x > 1).mean() * 100,
        fill_value=0,
    ).round(1)

    seasonal_evolution = seasonal_evolution[season_order]

    # Calculate movie counts for annotations
    movie_counts_seasonal = df.pivot_table(
        index="decade",
        columns="release_season",
        values="roi_clean",
        aggfunc="count",
        fill_value=0,
    )

    # Create custom text matrix
    text_matrix = np.array(
        [
            [
                f"{seasonal_evolution.iloc[i, j]:.1f}%\n({movie_counts_seasonal.iloc[i, j]:.0f})"
                for j in range(len(season_order))
            ]
            for i in range(len(seasonal_evolution))
        ]
    )

    fig.add_trace(
        go.Heatmap(
            z=seasonal_evolution.values,
            x=season_order,
            y=[f"{int(year)}s" for year in seasonal_evolution.index],
            colorscale="RdYlBu",
            text=text_matrix,
            texttemplate="%{text}",
            textfont={"size": 10},
            colorbar=dict(
                title="Success Rate (%)", titleside="right", ticksuffix="%", x=1.15
            ),
            hoverongaps=False,
            hovertemplate="<b>Decade:</b> %{y}<br>"
            + "<b>Season:</b> %{x}<br>"
            + "<b>Success Rate:</b> %{z:.1f}%<extra></extra>",
        ),
        row=2,
        col=1,
    )

    # 4. Performance Metrics Evolution
    add_stat_traces(yearly_stats["profit"], 2, 2, "Profit", "$", "profit")
    add_stat_traces(
        yearly_stats["rating"], 2, 2, "Rating", "", "rating", secondary_y=True
    )

    # Update layout
    fig.update_layout(
        height=1000,
        title_text="Temporal Trends in Movie Performance",
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.2,
            xanchor="center",
            x=0.5,
            traceorder="grouped",
        ),
    )

    # Update axes
    fig.update_xaxes(title_text="Year", row=1, col=1)
    fig.update_xaxes(title_text="Year", row=1, col=2)
    fig.update_xaxes(title_text="Year", row=2, col=2)

    fig.update_yaxes(title_text="Return on Investment", row=1, col=1)
    fig.update_yaxes(title_text="Success Rate (%)", row=1, col=2)
    fig.update_yaxes(title_text="Number of Movies", secondary_y=True, row=1, col=2)
    fig.update_yaxes(title_text="Profit (Millions USD)", row=2, col=2)
    fig.update_yaxes(title_text="Rating", secondary_y=True, row=2, col=2)

    # Add annotation explaining success rate
    fig.add_annotation(
        text="Success rate: ROI > 100%<br>Numbers show: success rate % (movie count)",
        xref="paper",
        yref="paper",
        x=0.25,  # Positioned above the heatmap
        y=0.5,
        showarrow=False,
        font=dict(size=10),
        xanchor="center",
        yanchor="bottom",
    )

    return fig, yearly_stats, seasonal_evolution


def create_seasonal_success_heatmap(df):
    """Create a clear heatmap visualization of seasonal success patterns."""

    # Create decade bins for pooling
    df["decade"] = (df["release_year"] // 10) * 10

    # Calculate success rates by decade and season
    seasonal_evolution = df.pivot_table(
        index="decade",
        columns="release_season",
        values="roi_clean",
        aggfunc=lambda x: (x > 1).mean() * 100,  # Success rate percentage
        fill_value=0,
    ).round(1)

    # Sort seasons in chronological order
    season_order = ["Winter", "Spring", "Summer", "Fall"]
    seasonal_evolution = seasonal_evolution[season_order]

    # Calculate number of movies for annotations
    movie_counts = df.pivot_table(
        index="decade",
        columns="release_season",
        values="roi_clean",
        aggfunc="count",
        fill_value=0,
    )

    # Create custom text for annotations
    text_matrix = np.array(
        [
            [
                f"{seasonal_evolution.iloc[i, j]:.1f}%\n({movie_counts.iloc[i, j]:.0f} movies)"
                for j in range(len(season_order))
            ]
            for i in range(len(seasonal_evolution))
        ]
    )

    # Create figure
    fig = go.Figure()

    # Add heatmap
    fig.add_trace(
        go.Heatmap(
            z=seasonal_evolution.values,
            x=season_order,
            y=[f"{int(year)}s" for year in seasonal_evolution.index],
            colorscale="RdYlBu",
            text=text_matrix,
            texttemplate="%{text}",
            textfont={"size": 10},
            showscale=True,
            colorbar=dict(
                title="Success Rate (%)", titleside="right", ticksuffix="%", x=1.15
            ),
            hoverongaps=False,
            hovertemplate="<b>Decade:</b> %{y}<br>"
            + "<b>Season:</b> %{x}<br>"
            + "<b>Success Rate:</b> %{z:.1f}%<extra></extra>",
        )
    )

    # Update layout
    fig.update_layout(
        title=dict(
            text="Movie Success Rates by Season and Decade",
            x=0.5,
            y=0.95,
            xanchor="center",
            yanchor="top",
            font=dict(size=20),
        ),
        xaxis=dict(
            title="Season",
            tickangle=0,
            side="bottom",
            tickfont=dict(size=12),
            titlefont=dict(size=14),
        ),
        yaxis=dict(
            title="Decade",
            autorange="reversed",  # To show earliest decades at bottom
            tickfont=dict(size=12),
            titlefont=dict(size=14),
        ),
        width=900,
        height=600,
        margin=dict(
            t=100, r=150, b=50, l=100
        ),  # Adjust margins to accommodate colorbar
        paper_bgcolor="white",
        plot_bgcolor="white",
    )

    # Add a subtitle with explanation
    fig.add_annotation(
        text="Values show success rate % (number of movies); Success defined as ROI > 100%",
        xref="paper",
        yref="paper",
        x=0.5,
        y=1.05,
        showarrow=False,
        font=dict(size=12),
        xanchor="center",
    )

    return fig, seasonal_evolution


def analyze_seasonal_patterns(df):
    """Perform statistical analysis of seasonal patterns."""

    # Calculate overall statistics by season
    seasonal_stats = (
        df.groupby("release_season")
        .agg(
            {
                "roi_clean": [
                    ("success_rate", lambda x: (x > 1).mean() * 100),
                    ("mean_roi", "mean"),
                    ("movie_count", "count"),
                ]
            }
        )
        .round(2)
    )

    # Flatten column names
    seasonal_stats.columns = ["Success Rate (%)", "Mean ROI", "Movie Count"]

    # Sort seasons chronologically
    season_order = ["Winter", "Spring", "Summer", "Fall"]
    seasonal_stats = seasonal_stats.reindex(season_order)

    return seasonal_stats


def run_seasonal_success_analysis(df):
    """Run complete seasonal success pattern analysis."""

    # Create visualization
    fig, seasonal_evolution = create_seasonal_success_heatmap(df)

    # Calculate statistics
    seasonal_stats = analyze_seasonal_patterns(df)

    # Save the plot
    fig.write_html(
        "seasonal_success_patterns.html", full_html=False, include_plotlyjs="cdn"
    )

    return {"figure": fig, "evolution": seasonal_evolution, "stats": seasonal_stats}


def run_interactive_timing_analysis(df):
    """Run complete interactive timing analysis pipeline."""

    results = {}

    # Seasonal analysis
    seasonal_fig, seasonal_stats = create_interactive_seasonal_distributions(df)
    seasonal_fig.write_html(
        "seasonal_analysis.html", full_html=False, include_plotlyjs="cdn"
    )
    results["seasonal_stats"] = seasonal_stats

    # Monthly analysis
    monthly_fig, monthly_stats, monthly_roi = create_interactive_monthly_performance(df)
    monthly_fig.write_html(
        "monthly_analysis.html", full_html=False, include_plotlyjs="cdn"
    )
    results["monthly_stats"] = monthly_stats
    results["monthly_roi"] = monthly_roi

    # # Temporal analysis
    # temporal_fig, yearly_stats, seasonal_evolution = create_interactive_temporal_trends(df)
    # temporal_fig.write_html("temporal_trends.html",full_html=False, include_plotlyjs='cdn')
    # results["yearly_stats"] = yearly_stats
    # results["seasonal_evolution"] = seasonal_evolution

    # Heatmap of seasonal success patterns
    seasonal_success = run_seasonal_success_analysis(df)
    results["seasonal_success"] = seasonal_success

    return results
