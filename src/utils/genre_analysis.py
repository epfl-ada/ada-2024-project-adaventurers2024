import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

from ..utils.visualization_utils import (
    setup_visualization,
    create_genre_colors,
    prepare_color_map,
)


def prepare_data(df_path):
    """Prepare dataset with all necessary metrics."""
    df = pd.read_csv(df_path)

    # Financial metrics
    df["profit"] = df["revenue"] - df["budget"]
    df["roi"] = (df["revenue"] - df["budget"]) / df["budget"]
    df["profit_scaled"] = df["profit"] / 1e6

    # Temporal data
    df["release_date"] = pd.to_datetime(df["release_date"])
    df["release_month"] = df["release_date"].dt.month
    df["release_season"] = pd.cut(
        df["release_date"].dt.month,
        bins=[0, 3, 6, 9, 12],
        labels=["Winter", "Spring", "Summer", "Fall"],
    )

    # Genre processing
    df["genres"] = df["genres"].fillna("")
    df["genres"] = df["genres"].str.split(", ")
    df_genres = df.explode("genres")
    df_genres = df_genres[df_genres["genres"] != ""]

    return df, df_genres


def plot_genre_distributions(df_genres, genre_colors):
    """Plot basic genre distributions for profits and ratings."""
    # Profit distribution
    plt.figure(figsize=(12, 6))
    sns.violinplot(
        data=df_genres,
        x="genres",
        y="profit_scaled",
        hue="genres",
        palette=genre_colors,
        legend=False,
    )
    plt.yscale("symlog", linthresh=1)
    plt.xticks(rotation=45, ha="right")
    plt.title("Movie Profits Distribution by Genre", pad=20)
    plt.ylabel("Profit (Millions USD, Log Scale)")
    plt.xlabel("Genre")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Rating distribution
    plt.figure(figsize=(12, 9))
    ax = sns.violinplot(
        data=df_genres,
        x="genres",
        y="vote_average",
        hue="genres",
        palette=genre_colors,
        legend=False,
    )
    plt.xticks(rotation=45, ha="right")
    plt.title("Movie Rating Distribution by Genre", pad=20)
    plt.ylabel("Average Rating (0-10)")
    plt.xlabel("Genre")
    plt.grid(True, alpha=0.3)

    for y in [5, 6, 7]:
        ax.axhline(y=y, color="gray", linestyle="--", alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_genre_performance(df_genres, genre_colors):
    """Plot genre performance analysis."""
    # Rating vs. Popularity
    plt.figure(figsize=(12, 6))
    sns.scatterplot(
        data=df_genres.sample(n=min(20000, len(df_genres))),
        x="vote_count",
        y="vote_average",
        hue="genres",
        alpha=0.6,
        palette=genre_colors,
    )
    plt.xscale("log")
    plt.title("Rating vs. Popularity by Genre", pad=20)
    plt.xlabel("Number of Votes (Log Scale)")
    plt.ylabel("Average Rating (0-10)")
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", title="Genre")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Profit-based analysis
    plt.figure(figsize=(12, 6))
    sample_size = min(20000, len(df_genres))
    df_genres_sample = df_genres.sample(n=sample_size, random_state=42)
    scatter = plt.scatter(
        df_genres_sample["vote_count"],
        df_genres_sample["vote_average"],
        c=df_genres_sample["profit_scaled"],
        s=30,
        alpha=0.6,
        cmap="RdYlBu",
    )
    plt.xscale("log")
    plt.title("Rating vs. Popularity by Profit", pad=20)
    plt.xlabel("Number of Votes (Log Scale)")
    plt.ylabel("Average Rating (0-10)")
    plt.grid(True, alpha=0.3)
    plt.colorbar(scatter, label="Profit (Millions USD)")
    plt.tight_layout()
    plt.show()


def analyze_temporal_trends(df_genres, genre_colors, unique_genres):
    """Analyze and plot temporal trends."""
    plt.figure(figsize=(12, 6))
    for genre in unique_genres:
        genre_data = df_genres[df_genres["genres"] == genre]
        if len(genre_data) > 0:
            yearly_avg = genre_data.groupby("release_year")["vote_average"].mean()
            moving_avg = yearly_avg.rolling(window=5, min_periods=1).mean()
            plt.plot(
                moving_avg.index,
                moving_avg.values,
                label=genre,
                color=genre_colors[genre],
                alpha=0.7,
                linewidth=2,
            )

    plt.title(
        "Average Movie Ratings by Genre Over Time (5-Year Moving Average)", pad=20
    )
    plt.xlabel("Release Year")
    plt.ylabel("Average Rating (0-10)")
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left", title="Genre")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def analyze_roi(df, df_genres, genre_colors):
    """Analyze and visualize ROI distributions."""

    def clean_roi(x):
        if np.isinf(x) or np.isnan(x) or x < -0.99:
            return np.nan
        if x > 50:  # Cap at 5000%
            return 50
        return x

    # Clean ROI data
    df["roi_clean"] = df["roi"].apply(clean_roi)
    df_genres["roi_clean"] = df_genres["roi"].apply(clean_roi)

    print("\nOverall ROI Statistics (cleaned):")
    print(df["roi_clean"].describe())

    # ROI Distribution Visualization
    plt.figure(figsize=(12, 6))
    sns.violinplot(
        data=df_genres[df_genres["roi_clean"].notna()],
        x="genres",
        y="roi_clean",
        palette=genre_colors,
        hue="genres",
    )
    plt.yscale("symlog", linthresh=0.1)
    plt.xticks(rotation=45, ha="right")
    plt.title("Movie ROI Distribution by Genre (capped at 5000%)", pad=20)
    plt.ylabel("Return on Investment (ROI)")
    plt.xlabel("Genre")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    return df, df_genres


def analyze_budget_categories(df):
    """Analyze ROI performance by budget categories."""
    df_with_budget = df[df["budget"] > 0].copy()
    df_with_budget["budget_category"] = pd.qcut(
        df_with_budget["budget"],
        q=5,
        labels=["Very Low", "Low", "Medium", "High", "Very High"],
    )

    # Print statistics
    print("\nROI Statistics by Budget Category (excluding zero budgets):")
    budget_roi = (
        df_with_budget.groupby("budget_category")
        .agg(
            {"roi_clean": ["count", "mean", "median"], "budget": ["mean", "min", "max"]}
        )
        .round(2)
    )
    print(budget_roi)

    # Visualize
    plt.figure(figsize=(12, 6))
    sns.violinplot(
        data=df_with_budget,
        x="budget_category",
        y="roi_clean",
        palette="viridis",
        hue="budget_category",
    )
    plt.yscale("symlog", linthresh=0.1)
    plt.title("ROI Distribution by Budget Category", pad=20)
    plt.ylabel("Return on Investment (ROI)")
    plt.xlabel("Budget Category")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    return budget_roi


def analyze_success_failure_rates(df_genres, genre_colors, unique_genres):
    """Analyze success and failure rates by genre."""
    performance_thresholds = {
        "Total Loss (>90%)": -0.9,
        "Severe Loss (>70%)": -0.7,
        "Significant Loss (>50%)": -0.5,
        "Moderate Loss (>30%)": -0.3,
        "Minor Loss (>0%)": 0,
        "Break Even": 0,
        "Modest Success (>50%)": 0.5,
        "Successful (>100%)": 1.0,
        "Very Successful (>200%)": 2.0,
        "Blockbuster (>500%)": 5.0,
    }

    # Calculate rates
    performance_rates = {}
    for genre in unique_genres:
        genre_data = df_genres[df_genres["genres"] == genre]["roi_clean"]
        rates = {}
        for threshold_name, threshold in performance_thresholds.items():
            if "Loss" in threshold_name:
                rate = (genre_data < threshold).mean()
            else:
                rate = (genre_data > threshold).mean()
            rates[threshold_name] = rate
        performance_rates[genre] = rates

    performance_df = pd.DataFrame(performance_rates).T.round(3) * 100
    print("\nPerformance Rates by Genre:")
    print(performance_df)

    # Visualize success and failure rates
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 6))

    # Success rates
    success_series = performance_df["Successful (>100%)"].sort_values(ascending=False)
    colors_success = [genre_colors[genre] for genre in success_series.index]
    success_series.plot(kind="bar", color=colors_success, ax=ax1)
    ax1.set_title("Success Rate: Movies Achieving >100% ROI", pad=20)
    ax1.set_xlabel("Genre")
    ax1.set_ylabel("Success Rate (%)")
    plt.setp(ax1.get_xticklabels(), rotation=45, ha="right")
    ax1.grid(True, alpha=0.3)

    # Failure rates
    failure_series = performance_df["Significant Loss (>50%)"].sort_values(
        ascending=False
    )
    colors_failure = [genre_colors[genre] for genre in failure_series.index]
    failure_series.plot(kind="bar", color=colors_failure, ax=ax2)
    ax2.set_title("Failure Rate: Movies with >50% Loss", pad=20)
    ax2.set_xlabel("Genre")
    ax2.set_ylabel("Failure Rate (%)")
    plt.setp(ax2.get_xticklabels(), rotation=45, ha="right")
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    return performance_df


def get_summary_statistics(df_genres):
    """Calculate and return summary statistics by genre."""
    summary_stats = (
        df_genres.groupby("genres")
        .agg(
            {
                "profit_scaled": ["mean", "median"],
                "vote_average": ["mean", "count"],
                "roi_clean": ["mean", "median"],
            }
        )
        .round(2)
    )

    print("\nSummary Statistics by Genre:")
    print(summary_stats)

    return summary_stats


def run_complete_analysis(df_path):
    """Run complete genre analysis pipeline."""
    # Setup
    setup_visualization()
    df, df_genres = prepare_data(df_path)
    unique_genres = sorted(df_genres["genres"].unique())
    genre_colors = create_genre_colors(unique_genres)

    # Run analyses
    plot_genre_distributions(df_genres, genre_colors)
    plot_genre_performance(df_genres, genre_colors)
    analyze_temporal_trends(df_genres, genre_colors, unique_genres)
    df, df_genres = analyze_roi(df, df_genres, genre_colors)
    budget_stats = analyze_budget_categories(df)
    performance_stats = analyze_success_failure_rates(
        df_genres, genre_colors, unique_genres
    )
    summary_stats = get_summary_statistics(df_genres)

    return {
        "df": df,
        "df_genres": df_genres,
        "budget_stats": budget_stats,
        "performance_stats": performance_stats,
        "summary_stats": summary_stats,
    }


def create_interactive_genre_distributions(df_genres, genre_colors):
    """Create interactive plots for genre distributions with summary statistics."""
    color_map = prepare_color_map(genre_colors)

    # Calculate summary statistics for profit
    profit_stats = (
        df_genres.groupby("genres")["profit_scaled"]
        .agg(
            [
                ("mean", "mean"),
                ("std", "std"),
                ("median", "median"),
                ("percentile_5", lambda x: x.quantile(0.05)),
                ("percentile_95", lambda x: x.quantile(0.95)),
            ]
        )
        .round(2)
    )

    # Function to transform values for log scale while handling negative values
    def log_transform(x):
        return np.sign(x) * np.log10(np.abs(x) + 1)

    # Transform all profit statistics
    for col in ["mean", "std", "median", "percentile_5", "percentile_95"]:
        profit_stats[f"{col}_log"] = log_transform(profit_stats[col])

    # Profit distribution plot
    profit_fig = go.Figure()

    # Add error bars for std deviation
    profit_fig.add_trace(
        go.Bar(
            name="Mean Profit",
            x=profit_stats.index,
            y=profit_stats["mean_log"],
            error_y=dict(type="data", array=profit_stats["std_log"], visible=True),
            marker_color=list(color_map.values()),
            hovertemplate="<b>Genre:</b> %{x}<br>"
            + "<b>Mean:</b> $%{customdata[0]:.2f}M<br>"
            + "<b>Std Dev:</b> $%{customdata[1]:.2f}M<extra></extra>",
            customdata=np.stack((profit_stats["mean"], profit_stats["std"]), axis=1),
        )
    )

    # Add percentile ranges
    profit_fig.add_trace(
        go.Scatter(
            name="5th-95th Percentile",
            x=profit_stats.index,
            y=profit_stats["percentile_95_log"],
            mode="lines",
            line=dict(width=0),
            showlegend=False,
            hovertemplate="<b>95th Percentile:</b> $%{customdata:.2f}M<extra></extra>",
            customdata=profit_stats["percentile_95"],
        )
    )

    profit_fig.add_trace(
        go.Scatter(
            name="5th-95th Percentile",
            x=profit_stats.index,
            y=profit_stats["percentile_5_log"],
            mode="lines",
            fill="tonexty",
            line=dict(width=0),
            fillcolor="rgba(128, 128, 128, 0.2)",
            hovertemplate="<b>5th Percentile:</b> $%{customdata:.2f}M<extra></extra>",
            customdata=profit_stats["percentile_5"],
        )
    )

    # Add median line
    profit_fig.add_trace(
        go.Scatter(
            name="Median",
            x=profit_stats.index,
            y=profit_stats["median_log"],
            mode="markers",
            marker=dict(symbol="line-ns", size=20, color="black"),
            hovertemplate="<b>Median:</b> $%{customdata:.2f}M<extra></extra>",
            customdata=profit_stats["median"],
        )
    )

    # Create custom tick values and labels for the y-axis
    tick_values = [-3, -2, -1, 0, 1, 2, 3]
    tick_labels = [
        f"${'-' if v < 0 else ''}{10 ** abs(v) - 1:.0f}M" for v in tick_values
    ]

    profit_fig.update_layout(
        title="Movie Profits Distribution by Genre",
        xaxis_title="Genre",
        yaxis_title="Profit (Millions USD, log scale)",
        showlegend=True,
        xaxis_tickangle=-45,
        hovermode="closest",
        yaxis=dict(tickmode="array", tickvals=tick_values, ticktext=tick_labels),
    )

    # Calculate summary statistics for ratings
    rating_stats = (
        df_genres.groupby("genres")["vote_average"]
        .agg(
            [
                ("mean", "mean"),
                ("std", "std"),
                ("median", "median"),
                ("percentile_5", lambda x: x.quantile(0.05)),
                ("percentile_95", lambda x: x.quantile(0.95)),
            ]
        )
        .round(2)
    )

    # Rating distribution plot
    rating_fig = go.Figure()

    # Add error bars for std deviation
    rating_fig.add_trace(
        go.Bar(
            name="Mean Rating",
            x=rating_stats.index,
            y=rating_stats["mean"],
            error_y=dict(type="data", array=rating_stats["std"], visible=True),
            marker_color=list(color_map.values()),
            hovertemplate="<b>Genre:</b> %{x}<br>"
            + "<b>Mean:</b> %{y:.2f}<br>"
            + "<b>Std Dev:</b> %{error_y.array:.2f}<extra></extra>",
        )
    )

    # Add percentile ranges
    rating_fig.add_trace(
        go.Scatter(
            name="5th-95th Percentile",
            x=rating_stats.index,
            y=rating_stats["percentile_95"],
            mode="lines",
            line=dict(width=0),
            showlegend=False,
            hovertemplate="<b>95th Percentile:</b> %{y:.2f}<extra></extra>",
        )
    )

    rating_fig.add_trace(
        go.Scatter(
            name="5th-95th Percentile",
            x=rating_stats.index,
            y=rating_stats["percentile_5"],
            mode="lines",
            fill="tonexty",
            line=dict(width=0),
            fillcolor="rgba(128, 128, 128, 0.2)",
            hovertemplate="<b>5th Percentile:</b> %{y:.2f}<extra></extra>",
        )
    )

    # Add median line
    rating_fig.add_trace(
        go.Scatter(
            name="Median",
            x=rating_stats.index,
            y=rating_stats["median"],
            mode="markers",
            marker=dict(symbol="line-ns", size=20, color="black"),
            hovertemplate="<b>Median:</b> %{y:.2f}<extra></extra>",
        )
    )

    rating_fig.update_layout(
        title="Movie Rating Distribution by Genre",
        xaxis_title="Genre",
        yaxis_title="Average Rating (0-10)",
        showlegend=True,
        xaxis_tickangle=-45,
        hovermode="closest",
    )

    # Set y-axis range for ratings
    rating_fig.update_yaxes(range=[1, 8])

    profit_fig.write_html(
        "genre_profit_distribution.html", full_html=False, include_plotlyjs="cdn"
    )
    rating_fig.write_html(
        "genre_rating_distribution.html", full_html=False, include_plotlyjs="cdn"
    )

    return profit_fig, rating_fig


def create_interactive_performance_analysis(df_genres, genre_colors):
    """Create interactive scatter plots for performance analysis."""
    plot_df = df_genres.sample(n=min(20000, len(df_genres))).copy()

    # Transform profit values for sizing and better color scaling
    max_abs_profit = max(
        abs(plot_df["profit_scaled"].min()), abs(plot_df["profit_scaled"].max())
    )

    fig = px.scatter(
        plot_df,
        x="vote_count",
        y="vote_average",
        color="profit_scaled",
        color_continuous_scale="RdYlBu",  # Red-Yellow-Blue scale
        range_color=[-max_abs_profit, max_abs_profit],  # Symmetric color scale
        hover_data={
            "title": True,
            "release_year": True,
            "budget": ":,.0f",
            "revenue": ":,.0f",
            "profit_scaled": ":.1f",
        },
        title="Rating vs. Popularity by Profit",
        labels={
            "vote_count": "Number of Votes",
            "vote_average": "Average Rating (0-10)",
            "profit_scaled": "Profit (Millions USD)",
            "budget": "Budget (USD)",
            "revenue": "Revenue (USD)",
        },
    )

    fig.update_traces(
        marker=dict(size=8),
        hovertemplate="<b>%{customdata[0]}</b><br>"
        + "Year: %{customdata[1]}<br>"
        + "Budget: $%{customdata[2]:,.0f}<br>"
        + "Revenue: $%{customdata[3]:,.0f}<br>"
        + "Profit: $%{customdata[4]:.1f}M<br>"
        + "Rating: %{y:.1f}<br>"
        + "Votes: %{x:,}<extra></extra>",
    )

    fig.update_xaxes(type="log")
    fig.update_layout(
        hovermode="closest", coloraxis_colorbar_title="Profit (Millions USD)"
    )

    fig.write_html("performance_analysis.html", full_html=False, include_plotlyjs="cdn")


def create_interactive_temporal_analysis(df_genres, genre_colors, unique_genres):
    """Create interactive temporal trend analysis."""
    color_map = prepare_color_map(genre_colors)
    fig = go.Figure()

    for genre in unique_genres:
        genre_data = df_genres[df_genres["genres"] == genre]
        if len(genre_data) > 0:
            # Calculate yearly statistics
            yearly_stats = (
                genre_data.groupby("release_year")
                .agg(
                    {
                        "vote_average": ["mean", "std", "count"],
                        "vote_count": "mean",
                        "profit_scaled": ["mean", "std"],
                    }
                )
                .round(2)
            )

            # Rename columns for easier access
            yearly_stats.columns = [
                "rating_mean",
                "rating_std",
                "movie_count",
                "vote_count_mean",
                "profit_mean",
                "profit_std",
            ]

            # Calculate moving averages for all metrics
            moving_stats = yearly_stats.rolling(window=5, min_periods=1).mean()

            # Create hover text with all information
            hover_text = [
                f"<b>{genre}</b><br>"
                + f"Year: {year}<br>"
                + f"Rating: {moving_stats['rating_mean'][year]:.2f} ± {yearly_stats['rating_std'][year]:.2f}<br>"
                + f"Movies: {yearly_stats['movie_count'][year]:.0f}<br>"
                + f"Votes per movie: {yearly_stats['vote_count_mean'][year]:.0f}<br>"
                + f"Profit: ${moving_stats['profit_mean'][year]:.1f}M ± ${yearly_stats['profit_std'][year]:.1f}M"
                for year in moving_stats.index
            ]

            fig.add_trace(
                go.Scatter(
                    x=moving_stats.index,
                    y=moving_stats["rating_mean"],
                    name=genre,
                    line=dict(color=color_map[genre]),
                    hovertemplate="%{text}<extra></extra>",
                    text=hover_text,
                    customdata=np.stack(
                        (
                            yearly_stats["movie_count"],
                            yearly_stats["vote_count_mean"],
                            moving_stats["profit_mean"],
                            yearly_stats["rating_std"],
                        ),
                        axis=1,
                    ),
                )
            )

    fig.update_layout(
        title="Genre Rating Trends Over Time (5-Year Moving Average)",
        xaxis_title="Release Year",
        yaxis_title="Average Rating",
        hovermode="closest",
        yaxis=dict(range=[1, 7.5]),  # Adjust this range based on your data
        showlegend=True,
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=1.02),
        margin=dict(r=200),
    )

    fig.write_html("temporal_trends.html", full_html=False, include_plotlyjs="cdn")

    return fig


def create_interactive_roi_analysis(df_genres, genre_colors):
    """Create interactive ROI analysis visualization with summary statistics."""
    color_map = prepare_color_map(genre_colors)

    # Calculate summary statistics
    roi_stats = (
        df_genres[df_genres["roi_clean"].notna()]
        .groupby("genres")["roi_clean"]
        .agg(
            [
                ("mean", "mean"),
                ("std", "std"),
                ("median", "median"),
                ("percentile_25", lambda x: x.quantile(0.25)),
                ("percentile_75", lambda x: x.quantile(0.75)),
            ]
        )
        .round(2)
    )

    # Function to transform values for better visualization while handling negative values
    def transform_value(x):
        return np.sign(x) * np.log10(np.abs(x) + 1)

    # Transform all ROI statistics
    for col in ["mean", "std", "median", "percentile_25", "percentile_75"]:
        roi_stats[f"{col}_transformed"] = transform_value(roi_stats[col])

    # Create figure
    fig = go.Figure()

    # Add error bars for std deviation
    fig.add_trace(
        go.Bar(
            name="Mean ROI",
            x=roi_stats.index,
            y=roi_stats["mean_transformed"],
            error_y=dict(type="data", array=roi_stats["std_transformed"], visible=True),
            marker_color=list(color_map.values()),
            hovertemplate="<b>Genre:</b> %{x}<br>"
            + "<b>Mean ROI:</b> %{customdata[0]:.2f}<br>"
            + "<b>Std Dev:</b> %{customdata[1]:.2f}<br>"
            + "<b>Sample Size:</b> %{customdata[2]}<extra></extra>",
            customdata=np.stack(
                (
                    roi_stats["mean"],
                    roi_stats["std"],
                    df_genres[df_genres["roi_clean"].notna()].groupby("genres").size(),
                ),
                axis=1,
            ),
        )
    )

    # Add quartile ranges
    fig.add_trace(
        go.Scatter(
            name="Interquartile Range",
            x=roi_stats.index,
            y=roi_stats["percentile_75_transformed"],
            mode="lines",
            line=dict(width=0),
            showlegend=False,
            hovertemplate="<b>75th Percentile:</b> %{customdata:.2f}<extra></extra>",
            customdata=roi_stats["percentile_75"],
        )
    )

    fig.add_trace(
        go.Scatter(
            name="Interquartile Range",
            x=roi_stats.index,
            y=roi_stats["percentile_25_transformed"],
            mode="lines",
            fill="tonexty",
            line=dict(width=0),
            fillcolor="rgba(128, 128, 128, 0.2)",
            hovertemplate="<b>25th Percentile:</b> %{customdata:.2f}<extra></extra>",
            customdata=roi_stats["percentile_25"],
        )
    )

    # Add median line
    fig.add_trace(
        go.Scatter(
            name="Median",
            x=roi_stats.index,
            y=roi_stats["median_transformed"],
            mode="markers",
            marker=dict(symbol="line-ns", size=20, color="black"),
            hovertemplate="<b>Median:</b> %{customdata:.2f}<extra></extra>",
            customdata=roi_stats["median"],
        )
    )

    # Create custom tick values and labels for the y-axis
    tick_values = [-2, -1, -0.5, 0, 0.5, 1, 2]
    tick_labels = [
        f"{'-' if v < 0 else ''}{(10 ** abs(v) - 1) * 100:.0f}%" for v in tick_values
    ]

    # Update layout
    fig.update_layout(
        title="ROI Distribution by Genre",
        xaxis_title="Genre",
        yaxis_title="Return on Investment (transformed scale)",
        showlegend=True,
        xaxis_tickangle=-45,
        hovermode="closest",
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=1.02),
        margin=dict(r=200),
        yaxis=dict(tickmode="array", tickvals=tick_values, ticktext=tick_labels),
    )

    fig.write_html("roi_analysis.html", full_html=False, include_plotlyjs="cdn")

    return fig


def create_interactive_budget_analysis(df, genre_colors):
    """Create interactive budget analysis visualization."""
    df_with_budget = df[df["budget"] > 0].copy()
    df_with_budget["budget_category"] = pd.qcut(
        df_with_budget["budget"],
        q=5,
        labels=["Very Low", "Low", "Medium", "High", "Very High"],
    )

    fig = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=("ROI by Budget Category", "Profit by Budget Category"),
    )

    # Calculate statistics for ROI
    roi_stats = (
        df_with_budget.groupby("budget_category")["roi_clean"]
        .agg(
            [
                ("mean", "mean"),
                ("std", "std"),
                ("median", "median"),
                ("percentile_25", lambda x: x.quantile(0.25)),
                ("percentile_75", lambda x: x.quantile(0.75)),
            ]
        )
        .round(2)
    )

    # Calculate statistics for Profit
    profit_stats = (
        df_with_budget.groupby("budget_category")["profit_scaled"]
        .agg(
            [
                ("mean", "mean"),
                ("std", "std"),
                ("median", "median"),
                ("percentile_25", lambda x: x.quantile(0.25)),
                ("percentile_75", lambda x: x.quantile(0.75)),
            ]
        )
        .round(2)
    )

    # ROI Analysis
    fig.add_trace(
        go.Bar(
            name="Mean ROI",
            x=roi_stats.index,
            y=roi_stats["mean"],
            error_y=dict(type="data", array=roi_stats["std"], visible=True),
            hovertemplate="<b>Budget Category:</b> %{x}<br>"
            + "<b>Mean ROI:</b> %{y:.2f}<br>"
            + "<b>Std Dev:</b> %{error_y.array:.2f}<br>"
            + "<b>Sample Size:</b> %{customdata}<extra></extra>",
            customdata=df_with_budget.groupby("budget_category").size(),
        ),
        row=1,
        col=1,
    )

    # Add ROI quartile ranges
    fig.add_trace(
        go.Scatter(
            name="ROI IQR",
            x=roi_stats.index,
            y=roi_stats["percentile_75"],
            mode="lines",
            line=dict(width=0),
            showlegend=False,
            hovertemplate="<b>75th Percentile:</b> %{y:.2f}<extra></extra>",
        ),
        row=1,
        col=1,
    )

    fig.add_trace(
        go.Scatter(
            name="ROI IQR",
            x=roi_stats.index,
            y=roi_stats["percentile_25"],
            mode="lines",
            fill="tonexty",
            line=dict(width=0),
            fillcolor="rgba(128, 128, 128, 0.2)",
            hovertemplate="<b>25th Percentile:</b> %{y:.2f}<extra></extra>",
        ),
        row=1,
        col=1,
    )

    # Add ROI median line
    fig.add_trace(
        go.Scatter(
            name="ROI Median",
            x=roi_stats.index,
            y=roi_stats["median"],
            mode="markers",
            marker=dict(symbol="line-ns", size=20, color="black"),
            hovertemplate="<b>Median:</b> %{y:.2f}<extra></extra>",
        ),
        row=1,
        col=1,
    )

    # Profit Analysis
    fig.add_trace(
        go.Bar(
            name="Mean Profit",
            x=profit_stats.index,
            y=profit_stats["mean"],
            error_y=dict(type="data", array=profit_stats["std"], visible=True),
            hovertemplate="<b>Budget Category:</b> %{x}<br>"
            + "<b>Mean Profit:</b> $%{y:.2f}M<br>"
            + "<b>Std Dev:</b> $%{error_y.array:.2f}M<br>"
            + "<b>Sample Size:</b> %{customdata}<extra></extra>",
            customdata=df_with_budget.groupby("budget_category").size(),
        ),
        row=1,
        col=2,
    )

    # Add Profit quartile ranges
    fig.add_trace(
        go.Scatter(
            name="Profit IQR",
            x=profit_stats.index,
            y=profit_stats["percentile_75"],
            mode="lines",
            line=dict(width=0),
            showlegend=False,
            hovertemplate="<b>75th Percentile:</b> $%{y:.2f}M<extra></extra>",
        ),
        row=1,
        col=2,
    )

    fig.add_trace(
        go.Scatter(
            name="Profit IQR",
            x=profit_stats.index,
            y=profit_stats["percentile_25"],
            mode="lines",
            fill="tonexty",
            line=dict(width=0),
            fillcolor="rgba(128, 128, 128, 0.2)",
            hovertemplate="<b>25th Percentile:</b> $%{y:.2f}M<extra></extra>",
        ),
        row=1,
        col=2,
    )

    # Add Profit median line
    fig.add_trace(
        go.Scatter(
            name="Profit Median",
            x=profit_stats.index,
            y=profit_stats["median"],
            mode="markers",
            marker=dict(symbol="line-ns", size=20, color="black"),
            hovertemplate="<b>Median:</b> $%{y:.2f}M<extra></extra>",
        ),
        row=1,
        col=2,
    )

    fig.update_layout(
        height=600,
        title_text="Budget Category Analysis",
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )

    # Update y-axis titles
    fig.update_yaxes(title_text="Return on Investment", row=1, col=1)
    fig.update_yaxes(title_text="Profit (Millions USD)", row=1, col=2)

    fig.write_html("budget_analysis.html", full_html=False, include_plotlyjs="cdn")

    return fig


def create_interactive_success_matrix(performance_df):
    """Create interactive success rate matrix visualization."""
    fig = px.imshow(
        performance_df,
        title="Performance Rates by Genre (%)",
        labels=dict(x="Performance Metric", y="Genre", color="Rate (%)"),
        aspect="auto",
    )

    fig.update_layout(xaxis_tickangle=-45, height=800)
    fig.write_html("success_matrix.html", full_html=False, include_plotlyjs="cdn")


def create_interactive_plot_genre_performance(df_genres, genre_colors):
    """Create interactive genre performance analysis plots."""
    color_map = prepare_color_map(genre_colors)
    
    # Filter out zero profit entries
    df_genres = df_genres[df_genres['profit_scaled'] != 0]

    # Rating vs. Popularity
    fig1 = px.scatter(
        df_genres.sample(n=min(50000, len(df_genres))),
        x="vote_count",
        y="vote_average",
        color="genres",
        color_discrete_map=color_map,
        title="Rating vs. Popularity by Genre",
        labels={
            "vote_count": "Number of Votes",
            "vote_average": "Average Rating (0-10)",
            "genres": "Genre",
        },
        hover_data=["title", "release_year"],
    )

    fig1.update_xaxes(type="log")
    fig1.update_layout(hovermode="closest")
    fig1.write_html("genre_performance_popularity.html", full_html=False, include_plotlyjs="cdn")

    # Profit-based analysis
    sample_size = min(50000, len(df_genres))
    df_genres_sample = df_genres.sample(n=sample_size, random_state=42)

    fig2 = px.scatter(
        df_genres_sample,
        x="vote_count",
        y="vote_average",
        color="profit_scaled",
        title="Rating vs. Popularity by Profit",
        labels={
            "vote_count": "Number of Votes",
            "vote_average": "Average Rating (0-10)",
            "profit_scaled": "Profit (Millions USD)",
        },
        hover_data=["title", "genres", "release_year"],
    )

    fig2.update_xaxes(type="log")
    fig2.update_layout(hovermode="closest")
    # set the color scale to log scale with visible non-light colors
    fig2.update_coloraxes(colorscale="emrld", cmin=-5, cmax=5)
    fig2.write_html(
        "genre_performance_profit.html", full_html=False, include_plotlyjs="cdn"
    )


def create_interactive_success_failure_analysis(
    df_genres, genre_colors, performance_df
):
    """Create interactive success and failure rate visualizations."""
    color_map = prepare_color_map(genre_colors)

    # Success rates
    success_series = performance_df["Successful (>100%)"].sort_values(ascending=False)

    fig1 = go.Figure(
        go.Bar(
            x=success_series.index,
            y=success_series.values,
            marker_color=[color_map[genre] for genre in success_series.index],
        )
    )

    fig1.update_layout(
        title="Success Rate: Movies Achieving >100% ROI",
        xaxis_title="Genre",
        yaxis_title="Success Rate (%)",
        xaxis_tickangle=-45,
        showlegend=False,
    )
    fig1.write_html("success_rates.html", full_html=False, include_plotlyjs="cdn")

    # Failure rates
    failure_series = performance_df["Significant Loss (>50%)"].sort_values(
        ascending=False
    )

    fig2 = go.Figure(
        go.Bar(
            x=failure_series.index,
            y=failure_series.values,
            marker_color=[color_map[genre] for genre in failure_series.index],
        )
    )

    fig2.update_layout(
        title="Failure Rate: Movies with >50% Loss",
        xaxis_title="Genre",
        yaxis_title="Failure Rate (%)",
        xaxis_tickangle=-45,
        showlegend=False,
    )
    fig2.write_html("failure_rates.html", full_html=False, include_plotlyjs="cdn")


from scipy import stats


def create_interactive_summary_statistics(df_genres):
    """Create interactive summary statistics visualization."""
    # Calculate summary statistics
    summary_stats = (
        df_genres.groupby("genres")
        .agg(
            {
                "profit_scaled": ["mean", "std"],
                "vote_average": ["mean", "count"],
                "roi_clean": ["mean", "std", "median"],
            }
        )
        .round(2)
    )

    # Create subplots for different metric groups
    fig = make_subplots(
        rows=3,
        cols=1,
        subplot_titles=(
            "Average Profit by Genre (Millions USD)",
            "Rating Metrics by Genre",
            "ROI Statistics by Genre",
        ),
        vertical_spacing=0.12,
        specs=[[{"type": "bar"}], [{"secondary_y": True}], [{"type": "bar"}]],
    )

    # Colors for different metrics
    colors = px.colors.qualitative.Set2

    # Add profit metrics
    fig.add_trace(
        go.Bar(
            name="Mean Profit",
            x=summary_stats.index,
            y=summary_stats[("profit_scaled", "mean")],
            error_y=dict(
                type="data", array=summary_stats[("profit_scaled", "std")], visible=True
            ),
            marker_color=colors[0],
            hovertemplate="<b>Genre:</b> %{x}<br>"
            + "<b>Mean Profit:</b> $%{y:.2f}M<br>"
            + "<b>Std Dev:</b> $%{error_y.array:.2f}M<extra></extra>",
        ),
        row=1,
        col=1,
    )

    # Add rating metrics with dual y-axis
    fig.add_trace(
        go.Bar(
            name="Average Rating",
            x=summary_stats.index,
            y=summary_stats[("vote_average", "mean")],
            marker_color=colors[2],
            hovertemplate="<b>Genre:</b> %{x}<br>"
            + "<b>Average Rating:</b> %{y:.2f}<extra></extra>",
        ),
        row=2,
        col=1,
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(
            name="Movie Count",
            x=summary_stats.index,
            y=summary_stats[("vote_average", "count")],
            marker_color=colors[3],
            mode="lines+markers",
            hovertemplate="<b>Genre:</b> %{x}<br>"
            + "<b>Number of Movies:</b> %{y}<extra></extra>",
        ),
        row=2,
        col=1,
        secondary_y=True,
    )

    # Add ROI metrics
    fig.add_trace(
        go.Bar(
            name="Mean ROI",
            x=summary_stats.index,
            y=summary_stats[("roi_clean", "mean")],
            error_y=dict(
                type="data", array=summary_stats[("roi_clean", "std")], visible=True
            ),
            marker_color=colors[4],
            hovertemplate="<b>Genre:</b> %{x}<br>"
            + "<b>Mean ROI:</b> %{y:.2f}<br>"
            + "<b>Std Dev:</b> %{error_y.array:.2f}<extra></extra>",
        ),
        row=3,
        col=1,
    )

    fig.add_trace(
        go.Bar(
            name="Median ROI",
            x=summary_stats.index,
            y=summary_stats[("roi_clean", "median")],
            marker_color=colors[5],
            hovertemplate="<b>Genre:</b> %{x}<br>"
            + "<b>Median ROI:</b> %{y:.2f}<extra></extra>",
        ),
        row=3,
        col=1,
    )

    # Update layout
    fig.update_layout(
        height=1200,
        title_text="Genre Performance Statistics",
        showlegend=True,
        barmode="group",
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=1.02),
        margin=dict(r=200),
    )

    # Update axes
    fig.update_xaxes(tickangle=-45)

    # Update y-axis titles and ranges
    fig.update_yaxes(title_text="Profit (Millions USD)", row=1, col=1)

    # Update second subplot y-axes with fixed range for ratings
    fig.update_yaxes(
        title_text="Average Rating",
        range=[4.4, 6.2],  # Set fixed range for ratings
        row=2,
        col=1,
        secondary_y=False,
    )
    fig.update_yaxes(title_text="Number of Movies", row=2, col=1, secondary_y=True)

    fig.update_yaxes(title_text="ROI", row=3, col=1)

    fig.write_html("summary_statistics.html", full_html=False, include_plotlyjs="cdn")

    return fig


def run_complete_interactive_analysis(df_path):
    """Run complete interactive analysis pipeline."""
    # Setup
    df, df_genres = prepare_data(df_path)
    unique_genres = sorted(df_genres["genres"].unique())
    genre_colors = create_genre_colors(unique_genres)

    # Run analyses and generate interactive visualizations
    create_interactive_genre_distributions(df_genres, genre_colors)
    create_interactive_plot_genre_performance(df_genres, genre_colors)
    create_interactive_temporal_analysis(df_genres, genre_colors, unique_genres)

    # ROI Analysis
    df, df_genres = analyze_roi(df, df_genres, genre_colors)
    create_interactive_roi_analysis(df_genres, genre_colors)

    # Budget Analysis
    create_interactive_budget_analysis(df, genre_colors)

    # Success/Failure Analysis
    performance_stats = analyze_success_failure_rates(
        df_genres, genre_colors, unique_genres
    )
    create_interactive_success_failure_analysis(
        df_genres, genre_colors, performance_stats
    )
    create_interactive_success_matrix(performance_stats)

    # Summary Statistics
    create_interactive_summary_statistics(df_genres)

    return {"df": df, "df_genres": df_genres, "performance_stats": performance_stats}
