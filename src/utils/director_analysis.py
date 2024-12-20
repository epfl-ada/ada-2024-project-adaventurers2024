import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import statsmodels.api as sm
import plotly.graph_objects as go

def director_analysis(data_path):
    # Load the dataset
    df = pd.read_csv(data_path)

    # Parse 'genres_x' into lists
    df["genres_list"] = (
        df["genres_x"].fillna("").apply(lambda x: x.split(",") if x != "\\N" else [])
    )

    # Function to parse 'genres_y' strings
    def parse_genres_y(s):
        try:
            if pd.isnull(s) or s == "\\N":
                return []
            s = s.replace('""', '"').replace("\\", "")
            genres_dict = json.loads(s)
            return list(genres_dict.values())
        except json.JSONDecodeError:
            return []

    # Apply the function to 'genres_y'
    df["genres_y_list"] = df["genres_y"].apply(parse_genres_y)

    # Combine the two genre lists
    df["all_genres"] = df["genres_list"] + df["genres_y_list"]

    # Convert to numeric types
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
    df["average_rating"] = pd.to_numeric(df["average_rating"], errors="coerce")

    # Explode the genres
    df_exploded = df.explode("all_genres")

    # Remove rows with empty genres
    df_exploded = df_exploded[
        df_exploded["all_genres"].notna() & (df_exploded["all_genres"] != "")
    ]

    # Group by director and genre
    grouped = df_exploded.groupby(["director_name", "all_genres"])

    # Compute the metrics
    result = grouped.agg(
        num_movies=("movie_id", "nunique"),
        avg_revenue=("revenue", "mean"),
        avg_rating=("average_rating", "mean"),
    ).reset_index()

    # Number of genres per director
    director_genre_counts = (
        result.groupby("director_name")
        .agg(
            num_genres=("all_genres", "nunique"),
            total_movies=("num_movies", "sum"),
            overall_avg_revenue=("avg_revenue", "mean"),
            overall_avg_rating=("avg_rating", "mean"),
        )
        .reset_index()
    )

    # Correlation analysis
    correlation_revenue = director_genre_counts["num_genres"].corr(
        director_genre_counts["overall_avg_revenue"]
    )
    correlation_rating = director_genre_counts["num_genres"].corr(
        director_genre_counts["overall_avg_rating"]
    )

    print(
        f"Correlation between number of genres and average revenue: {correlation_revenue}"
    )
    print(
        f"Correlation between number of genres and average rating: {correlation_rating}"
    )

    # Display the result
    print(director_genre_counts)

    # Visualization for Revenue
    plt.figure(figsize=(10, 6))
    plt.scatter(
        director_genre_counts["num_genres"],
        director_genre_counts["overall_avg_revenue"],
    )
    plt.xlabel("Number of Genres")
    plt.ylabel("Overall Average Revenue")
    plt.title("Number of Genres vs. Average Revenue")
    plt.grid(True)
    plt.show()

    # Visualization for Rating
    plt.figure(figsize=(10, 6))
    plt.scatter(
        director_genre_counts["num_genres"], director_genre_counts["overall_avg_rating"]
    )
    plt.xlabel("Number of Genres")
    plt.ylabel("Overall Average Rating")
    plt.title("Number of Genres vs. Average Rating")
    plt.grid(True)
    plt.show()

    # Regression Analysis for Revenue
    X = director_genre_counts[["num_genres"]]
    y_revenue = director_genre_counts["overall_avg_revenue"]
    X_with_const = sm.add_constant(X)
    model_revenue = sm.OLS(y_revenue, X_with_const).fit()
    print(model_revenue.summary())

    # Regression Analysis for Rating
    y_rating = director_genre_counts["overall_avg_rating"]
    model_rating = sm.OLS(y_rating, X_with_const).fit()
    print(model_rating.summary())

def rq3_display_sankey_diagram(data_path):
    """
    Generates and displays a Sankey diagram visualizing the relationship between
    the number of genres and rating groups, with line thickness representing revenue.

    Parameters:
    - data_path (str): Path to the CSV file containing the data.

    Returns:
    - None
    """
    # Load data
    data = pd.read_csv(data_path)

    # Define rating groups
    rating_groups = ["5.5-6", "6-6.5", "6.5-7", "7-7.5"]
    rating_bins = [5.5, 6.0, 6.5, 7.0, 7.5]

    # Map avg_rating to bins
    data["rating_group"] = pd.cut(data["avg_rating"], bins=rating_bins, labels=rating_groups, include_lowest=True)

    # Handle NaN in rating_group
    data = data.dropna(subset=["rating_group"])  # Drop rows with NaN in rating_group

    # Normalize line thickness for visualization
    data["line_thickness_norm"] = data["line_thickness"] / data["line_thickness"].max() * 10

    # Prepare Sankey nodes
    left_nodes = sorted(data["num_genres"].unique())  # Left side: num_genres
    right_nodes = rating_groups  # Right side: rating groups

    # Node details
    nodes = {
        "labels": [str(num) for num in left_nodes] + right_nodes,
        "x": [0.1] * len(left_nodes) + [0.9] * len(right_nodes),
        "y": list((1 - (i / len(left_nodes))) for i in range(len(left_nodes))) + list(
            (1 - (i / len(right_nodes))) for i in range(len(right_nodes))
        ),
        "color": ["blue"] * len(left_nodes) + ["green"] * len(right_nodes),
        "customdata": [f"Number of Genres: {num}" for num in left_nodes] +
                      [f"Rating Group: {group}" for group in right_nodes]
    }

    # Prepare Sankey links
    sources = [left_nodes.index(num) for num in data["num_genres"]]  # Indices for num_genres
    targets = [
        len(left_nodes) + rating_groups.index(group) for group in data["rating_group"]
    ]  # Map to grouped ratings
    values = data["line_thickness_norm"]

    # Add hover data to links
    link_customdata = [
        f"Num Genres: {row['num_genres']}<br>Avg Rating: {row['avg_rating']:.1f}<br>Avg Revenue: ${row['avg_revenue']:,}"
        for _, row in data.iterrows()
    ]

    # Create Sankey figure
    fig = go.Figure(go.Sankey(
        arrangement='snap',
        node=dict(
            label=nodes["labels"],
            x=nodes["x"],
            y=nodes["y"],
            pad=10,
            align="center",
            color=nodes["color"],
            customdata=nodes["customdata"],
            hovertemplate="Node: %{customdata}<extra></extra>"
        ),
        link=dict(
            source=sources,
            target=targets,
            value=values,
            customdata=link_customdata,
            hovertemplate="Link:<br>%{customdata}<extra></extra>"
        )
    ))

    # Update layout
    fig.update_layout(
        title_text="Sankey Diagram: Number of Directors' Genres to Ratings Groups with Revenue Thickness",
        font_size=12,
        title_x=0.5,
        height=600,
        width=1200,
        annotations=[
            dict(
                x=0.5,
                y=-0.14,
                xref="paper",
                yref="paper",
                text="Note: The thicker the link, the higher the average revenue.",
                showarrow=False,
                font=dict(size=14, color="black")
            ),
            dict(
                x=0.05,
                y=1.05,
                xref="paper",
                yref="paper",
                text="Number of Directors' Genres",
                showarrow=False,
                font=dict(size=14, color="blue")
            ),
            dict(
                x=0.95,
                y=1.05,
                xref="paper",
                yref="paper",
                text="Rating Groups",
                showarrow=False,
                font=dict(size=14, color="green")
            )
        ]
    )

    # Show plot
    fig.show()
