import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def actor_analysis(data_path, ethnicity_mapping_path):
    # 1. Load the dataset
    df_movie_actors = pd.read_csv(data_path)

    # Display the first few rows
    print("First few rows of the dataset:")
    display(df_movie_actors.head())

    # 2. Data cleaning

    # 2.1 Remove duplicates
    num_duplicates = df_movie_actors.duplicated().sum()
    print(f"\nNumber of duplicate rows: {num_duplicates}")

    # Remove duplicates
    df_movie_actors.drop_duplicates(inplace=True)

    # 2.2 Handle missing values
    print("\nMissing values per column:")
    missing_values = df_movie_actors.isnull().sum()
    print(missing_values)

    # Drop rows with missing critical data
    df_movie_actors.dropna(
        subset=[
            "actor_gender",
            "actor_age_at_movie_release",
            "revenue",
            "average_rating",
            "num_votes",
        ],
        inplace=True,
    )

    # Reset index after dropping rows
    df_movie_actors.reset_index(drop=True, inplace=True)

    # 3. Ethnicity mapping

    # Map 'actor_ethnicity_freebase_id' to ethnicity names
    ethnicity_mapping_df = pd.read_csv(
        ethnicity_mapping_path
    )  # Ensure this file exists
    # Create mapping dictionary
    ethnicity_mapping = pd.Series(
        ethnicity_mapping_df["itemLabel"].values,
        index=ethnicity_mapping_df["freebase_id"],
    ).to_dict()
    # Map ethnicity IDs to names
    df_movie_actors["actor_ethnicity"] = df_movie_actors[
        "actor_ethnicity_freebase_id"
    ].map(ethnicity_mapping)

    # Check for missing ethnicity mappings
    missing_ethnicities = df_movie_actors[df_movie_actors["actor_ethnicity"].isnull()][
        "actor_ethnicity_freebase_id"
    ].unique()
    print("\nMissing ethnicity mappings:", missing_ethnicities)

    # 4. Data exploration

    # 4.1 Overview of actor demographics
    # Gender distribution
    gender_counts = df_movie_actors["actor_gender"].value_counts()
    print("\nGender distribution of actors:")
    print(gender_counts)

    # Plot gender distribution
    plt.figure(figsize=(6, 4))
    sns.countplot(x="actor_gender", data=df_movie_actors)
    plt.title("Actor Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.show()

    # 4.2 Age distribution of actors
    # Histogram of actor ages at movie release
    plt.figure(figsize=(8, 6))
    sns.histplot(df_movie_actors["actor_age_at_movie_release"], bins=30, kde=True)
    plt.title("Age Distribution of Actors at Movie Release")
    plt.xlim(0, 100)
    plt.xlabel("Age")
    plt.ylabel("Number of Actors")
    plt.show()

    # 4.3 Ethnicity diversity
    # Count unique ethnicities
    num_ethnicities = df_movie_actors["actor_ethnicity"].nunique()
    print(f"\nNumber of unique ethnicities: {num_ethnicities}")

    # Display counts
    ethnicity_counts = df_movie_actors["actor_ethnicity"].value_counts()
    print("\nEthnicity distribution of actors:")
    print(ethnicity_counts.head())
    # Plot ethnicity distribution (top 10)
    plt.figure(figsize=(12, 6))
    sns.countplot(
        y="actor_ethnicity", data=df_movie_actors, order=ethnicity_counts.index[:10]
    )
    plt.title("Top 10 Actor Ethnicities")
    plt.xlabel("Count")
    plt.ylabel("Ethnicity")
    plt.show()

    # 5. Assessing diversity per movie

    # Group data by movie
    grouped = df_movie_actors.groupby("movie_name")

    # 5.1 Compute diversity metrics
    def compute_diversity_metrics(group):
        # Count unique actors for each movie
        num_actors = group["actor_name"].nunique()
        
        # Count unique female actors
        num_female = group[group["actor_gender"] == "F"]["actor_name"].nunique()
        
        # Count unique male actors
        num_male = group[group["actor_gender"] == "M"]["actor_name"].nunique()
        
        # Calculate gender diversity (proportion of female actors)
        gender_diversity = num_female / num_actors if num_actors else np.nan
        
        # Calculate other metrics
        num_ethnicities = group["actor_ethnicity"].nunique()
        age_std = group["actor_age_at_movie_release"].std()
        revenue = group["revenue"].mean()
        average_rating = group["average_rating"].mean()
        num_votes = group["num_votes"].sum()
        
        return pd.Series(
            {
                "num_actors": num_actors,
                "num_male": num_male,
                "num_female": num_female,
                "gender_diversity": gender_diversity,
                "num_ethnicities": num_ethnicities,
                "age_std": age_std,
                "revenue": revenue,
                "average_rating": average_rating,
                "num_votes": num_votes,
            }
        )

    # Apply the function to each movie group
    movie_metrics = grouped.apply(compute_diversity_metrics).reset_index()

    # Display the metrics
    print("\nDiversity metrics for movies:")
    display(movie_metrics.head())

    # 6. Analyzing the impact on ratings and revenue

    # 6.1 Correlation Analysis
    # Select relevant columns for correlation
    corr_columns = [
        "gender_diversity",
        "num_ethnicities",
        "age_std",
        "revenue",
        "average_rating",
    ]
    corr_matrix = movie_metrics[corr_columns].corr()

    # Display the correlation matrix
    print("\nCorrelation Matrix:")
    print(corr_matrix)

    # 6.2 Visualize correlations
    # Heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix Heatmap")
    plt.show()

    # 6.3 Scatter plots

    # 6.3.1 Gender Diversity vs. Revenue
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="gender_diversity", y="revenue", data=movie_metrics)
    plt.title("Gender Diversity vs. Revenue")
    plt.xlabel("Gender Diversity (Proportion of Female Actors)")
    plt.ylabel("Revenue")
    plt.ylim(0, 1.5e9)  # Limit y-axis for better visualization
    plt.show()

    # 6.3.2 Gender Diversity vs. Average Rating
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="gender_diversity", y="average_rating", data=movie_metrics)
    plt.title("Gender Diversity vs. Average Rating")
    plt.xlabel("Gender Diversity (Proportion of Female Actors)")
    plt.ylabel("Average Rating")
    plt.show()

    # 6.3.3 Ethnic Diversity vs. Revenue
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="num_ethnicities", y="revenue", data=movie_metrics)
    plt.title("Ethnic Diversity vs. Revenue")
    plt.xlabel("Number of Unique Ethnicities")
    plt.ylabel("Revenue")
    plt.ylim(0, 1.5e9) 
    plt.show()

    # 6.3.4 Ethnic Diversity vs. Average Rating
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="num_ethnicities", y="average_rating", data=movie_metrics)
    plt.title("Ethnic Diversity vs. Average Rating")
    plt.xlabel("Number of Unique Ethnicities")
    plt.ylabel("Average Rating")
    plt.show()

    # 6.3.5 Age Diversity vs. Revenue
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="age_std", y="revenue", data=movie_metrics)
    plt.title("Age Diversity (Std Dev) vs. Revenue")
    plt.xlabel("Age Standard Deviation")
    plt.ylabel("Revenue")
    plt.show()

    # 6.3.6 Age Diversity vs. Average Rating
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="age_std", y="average_rating", data=movie_metrics)
    plt.title("Age Diversity (Std Dev) vs. Average Rating")
    plt.xlabel("Age Standard Deviation")
    plt.ylabel("Average Rating")
    plt.show()

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
