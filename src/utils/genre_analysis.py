import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ..utils.visualization_utils import setup_visualization, create_genre_colors


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
        data=df_genres.sample(n=min(10000, len(df_genres))),
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
    sample_size = min(2000, len(df_genres))
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
