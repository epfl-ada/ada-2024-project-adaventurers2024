import pandas as pd
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
