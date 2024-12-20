import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def rq2_display_correlation_heatmap(file_path):
    """
    Displays a correlation heatmap for diversity metrics and revenue/average rating.

    Parameters:
    - file_path (str): Path to the JSON file containing the dataset.

    Returns:
    - None
    """
    movies_df = pd.read_json(file_path)
    correlation_matrix = movies_df.drop(columns=["wikipedia_movie_id"]).corr()
    heatmap_fig = px.imshow(
        correlation_matrix,
        text_auto=True,
        title="Correlation Between Diversity Metrics and Revenue/Average Rating",
        color_continuous_scale="Viridis",
    )
    heatmap_fig.update_layout(
        template="plotly_white", title_x=0.5, width=700, height=700
    )
    heatmap_fig.show()

def rq2_display_diversity_boxplots(file_path):
    """
    Displays boxplots for revenue and average rating grouped by diversity groups.

    Parameters:
    - file_path (str): Path to the JSON file containing the dataset.

    Returns:
    - None
    """
    movies_df = pd.read_json(file_path)

    # Define diversity groups for each diversity factor
    for factor in ["age_diversity", "gender_diversity", "height_diversity", "ethnicity_diversity"]:
        movies_df[f"{factor}_group"] = pd.qcut(
            movies_df[factor], q=4, labels=["Low", "Medium", "High", "Very High"]
        )

    # Revenue Boxplot
    revenue_box_fig = px.box(
        movies_df.melt(
            id_vars=["revenue"], 
            value_vars=[f"{factor}_group" for factor in ["age_diversity", "gender_diversity", "height_diversity", "ethnicity_diversity"]],
            var_name="Diversity Factor", 
            value_name="Group"
        ),
        x="Group",
        y="revenue",
        color="Diversity Factor",
        title="Revenue by Diversity Groups",
        labels={"Group": "Diversity Group", "revenue": "Revenue"},
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    revenue_box_fig.update_layout(
        template="plotly_white", title_x=0.5,
        xaxis=dict(categoryorder="array", categoryarray=["Low", "Medium", "High", "Very High"])
    )
    revenue_box_fig.show()

    # Average Rating Boxplot
    rating_box_fig = px.box(
        movies_df.melt(
            id_vars=["average_rating"], 
            value_vars=[f"{factor}_group" for factor in ["age_diversity", "gender_diversity", "height_diversity", "ethnicity_diversity"]],
            var_name="Diversity Factor", 
            value_name="Group"
        ),
        x="Group",
        y="average_rating",
        color="Diversity Factor",
        title="Average Rating by Diversity Groups",
        labels={"Group": "Diversity Group", "average_rating": "Average Rating"},
        color_discrete_sequence=px.colors.qualitative.Set2,
    )
    rating_box_fig.update_layout(
        template="plotly_white", title_x=0.5,
        xaxis=dict(categoryorder="array", categoryarray=["Low", "Medium", "High", "Very High"])
    )
    rating_box_fig.show()

def rq2_display_diversity_radar_charts(file_path):
    """
    Displays radar charts comparing diversity metrics for high vs low revenue
    and high vs low average ratings.

    Parameters:
    - file_path (str): Path to the JSON file containing the dataset.

    Returns:
    - None
    """
    movies_df = pd.read_json(file_path)

    # Create revenue groups for radar chart
    movies_df["revenue_group"] = pd.qcut(
        movies_df["revenue"], q=2, labels=["Low Revenue", "High Revenue"]
    )

    # Create average rating groups for radar chart
    movies_df["average_rating_group"] = pd.qcut(
        movies_df["average_rating"], q=2, labels=["Low Rating", "High Rating"]
    )

    numeric_columns = ["age_diversity", "gender_diversity", "height_diversity", "ethnicity_diversity"]

    # Radar Chart for Revenue
    radar_data = movies_df.groupby("revenue_group")[numeric_columns].mean().reset_index()
    radar_fig = go.Figure()
    for _, row in radar_data.iterrows():
        radar_fig.add_trace(
            go.Scatterpolar(
                r=row[numeric_columns].values,
                theta=numeric_columns,
                fill="toself",
                name=row["revenue_group"],
            )
        )
    radar_fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        title="Diversity Radar Chart: High vs Low Revenue",
        template="plotly_white",
        title_x=0.5,
    )
    radar_fig.show()

    # Radar Chart for Average Rating
    rating_data = movies_df.groupby("average_rating_group")[numeric_columns].mean().reset_index()
    rating_radar_fig = go.Figure()
    for _, row in rating_data.iterrows():
        rating_radar_fig.add_trace(
            go.Scatterpolar(
                r=row[numeric_columns].values,
                theta=numeric_columns,
                fill="toself",
                name=row["average_rating_group"],
            )
        )
    rating_radar_fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
        title="Diversity Radar Chart: High vs Low Average Rating",
        template="plotly_white",
        title_x=0.5,
    )
    rating_radar_fig.show()
