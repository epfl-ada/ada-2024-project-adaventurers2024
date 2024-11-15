import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import statsmodels.api as sm

def director_analysis(data_path):
    # Load the dataset
    df = pd.read_csv(data_path)

    # Parse 'genres_x' into lists
    df['genres_list'] = df['genres_x'].fillna('').apply(lambda x: x.split(',') if x != '\\N' else [])

    # Function to parse 'genres_y' strings
    def parse_genres_y(s):
        try:
            if pd.isnull(s) or s == '\\N':
                return []
            s = s.replace('""', '"').replace('\\', '')
            genres_dict = json.loads(s)
            return list(genres_dict.values())
        except json.JSONDecodeError:
            return []

    # Apply the function to 'genres_y'
    df['genres_y_list'] = df['genres_y'].apply(parse_genres_y)

    # Combine the two genre lists
    df['all_genres'] = df['genres_list'] + df['genres_y_list']

    # Convert to numeric types
    df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
    df['average_rating'] = pd.to_numeric(df['average_rating'], errors='coerce')

    # Explode the genres
    df_exploded = df.explode('all_genres')

    # Remove rows with empty genres
    df_exploded = df_exploded[df_exploded['all_genres'].notna() & (df_exploded['all_genres'] != '')]

    # Group by director and genre
    grouped = df_exploded.groupby(['director_name', 'all_genres'])

    # Compute the metrics
    result = grouped.agg(
        num_movies=('movie_id', 'nunique'),
        avg_revenue=('revenue', 'mean'),
        avg_rating=('average_rating', 'mean')
    ).reset_index()

    # Number of genres per director
    director_genre_counts = result.groupby('director_name').agg(
        num_genres=('all_genres', 'nunique'),
        total_movies=('num_movies', 'sum'),
        overall_avg_revenue=('avg_revenue', 'mean'),
        overall_avg_rating=('avg_rating', 'mean')
    ).reset_index()

    # Correlation analysis
    correlation_revenue = director_genre_counts['num_genres'].corr(director_genre_counts['overall_avg_revenue'])
    correlation_rating = director_genre_counts['num_genres'].corr(director_genre_counts['overall_avg_rating'])

    print(f"Correlation between number of genres and average revenue: {correlation_revenue}")
    print(f"Correlation between number of genres and average rating: {correlation_rating}")

    # Display the result
    print(director_genre_counts)

    # Visualization for Revenue
    plt.figure(figsize=(10, 6))
    plt.scatter(director_genre_counts['num_genres'], director_genre_counts['overall_avg_revenue'])
    plt.xlabel('Number of Genres')
    plt.ylabel('Overall Average Revenue')
    plt.title('Number of Genres vs. Average Revenue')
    plt.grid(True)
    plt.show()

    # Visualization for Rating
    plt.figure(figsize=(10, 6))
    plt.scatter(director_genre_counts['num_genres'], director_genre_counts['overall_avg_rating'])
    plt.xlabel('Number of Genres')
    plt.ylabel('Overall Average Rating')
    plt.title('Number of Genres vs. Average Rating')
    plt.grid(True)
    plt.show()

    # Regression Analysis for Revenue
    X = director_genre_counts[['num_genres']]
    y_revenue = director_genre_counts['overall_avg_revenue']
    X_with_const = sm.add_constant(X)
    model_revenue = sm.OLS(y_revenue, X_with_const).fit()
    print(model_revenue.summary())

    # Regression Analysis for Rating
    y_rating = director_genre_counts['overall_avg_rating']
    model_rating = sm.OLS(y_rating, X_with_const).fit()
    print(model_rating.summary())