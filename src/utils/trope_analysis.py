import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def rq6(df_cmu_tropes, k=20, vote_threshold=6):
    """
    Plot the top k tropes in movies with a vote average lower or equal than the threshold
    """
    print(
        "Number of movies with tropes before filtering: ",
        df_cmu_tropes["id"].unique().shape[0],
    )

    # Filtering movies witg zero votes or no revenue
    df_movies_filtered = df_cmu_tropes[
        (df_cmu_tropes[["vote_average", "vote_count", "revenue"]] != 0).all(axis=1)
    ]

    # Filter movies with an average score lower than the threshold
    df_low_rated_movies = df_movies_filtered[
        df_movies_filtered["vote_average"] <= vote_threshold
    ]
    df_low_rated_movies.reset_index(drop=True, inplace=True)
    print(
        "Number of movies with low rating and non-zero votes: ",
        df_low_rated_movies["id"].unique().shape[0],
    )
    print(
        "Number of tropes in low rated movies: ", df_low_rated_movies["trope"].shape[0]
    )
    print(
        "Number of unique tropes in low rated movies: ",
        df_low_rated_movies["trope"].unique().shape[0],
    )

    print("Vote average statistics:")
    print(df_low_rated_movies["vote_average"].describe())

    # Get the top k tropes for low rated movies
    df_top_tropes_lr_movies = (
        df_low_rated_movies["trope"].value_counts().reset_index().head(k)
    )
    df_top_tropes_lr_movies.columns = ["trope", "count"]

    plt.figure(figsize=(8, 6))
    sns.barplot(
        data=df_top_tropes_lr_movies, x="count", y="trope", hue="trope", dodge=False
    )
    plt.title(
        f"Top {k} tropes in movies with a vote average of {vote_threshold} or lower"
    )
    plt.ylabel("Tropes")
    plt.xlabel("Number of movies")
    plt.show()


def rq7(df_cmu_tropes, movie_genre, vote_threshold=6):
    """
    Plot the top 10 tropes more common in low-rated films of a specific genre
    """
    df_genre_tropes = df_cmu_tropes[df_cmu_tropes["genres"].str.contains(movie_genre)]
    df_genre_tropes = df_genre_tropes[df_genre_tropes["vote_count"] > 100]

    print(
        f"There are {len(df_genre_tropes.id.unique())} {movie_genre.lower()} films in the dataset"
    )

    df_low_rated_tropes = df_genre_tropes[
        df_genre_tropes["vote_average"] <= vote_threshold
    ]
    df_high_rated_tropes = df_genre_tropes[
        df_genre_tropes["vote_average"] > vote_threshold
    ]

    print(f"Films with low ratings: {len(df_low_rated_tropes.id.unique())}")
    print(f"Films with high ratings: {len(df_high_rated_tropes.id.unique())}")

    low_rated_tropes = df_low_rated_tropes.trope.value_counts()
    high_rated_tropes = df_high_rated_tropes.trope.value_counts()

    low_rated_dict = low_rated_tropes.to_dict()
    high_rated_dict = high_rated_tropes.to_dict()

    trope_ratios = {}
    for trope in low_rated_dict:
        low_count = low_rated_dict[trope]
        high_count = high_rated_dict.get(trope, 0)

        if low_count >= 5:
            ratio = low_count / (high_count + 1)
            trope_ratios[trope] = ratio

    sorted_tropes = sorted(trope_ratios.items(), key=lambda x: x[1], reverse=True)

    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=[x[1] for x in sorted_tropes[:10]],
        y=[x[0] for x in sorted_tropes[:10]],
        palette="viridis",
    )
    plt.title(f"Top 10 tropes more common in low-rated {movie_genre.lower()} films")
    plt.xlabel("Ratio low:high rated")
    plt.ylabel("Tropes")
    plt.show()
