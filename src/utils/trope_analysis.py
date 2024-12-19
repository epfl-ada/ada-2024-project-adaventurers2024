import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

from pathlib import Path

OUTPUT_PATH = 'data/preprocessed/'

def get_unique_genres(df_tropes_filtered):
    unique_str_genres = df_tropes_filtered['genres'].unique()
    unique_genres = set()

    for str_genres in unique_str_genres:
        for genre in str_genres.split(","):
            unique_genres.add(genre.strip())

    ordered_genres = ['All'] + sorted([genre for genre in unique_genres if genre != 'All'])

    print(f"{len(ordered_genres)} unique genres: {ordered_genres}")
    return ordered_genres


def rq6(df_cmu_tropes, threshold=6.0, k=10, min_votes=100):
    df_tropes_filtered = df_cmu_tropes[
        (df_cmu_tropes[["vote_average", "revenue"]] != 0).all(axis=1)
    ]

    df_tropes_filtered = df_tropes_filtered[df_tropes_filtered['vote_count'] > min_votes]
    df_tropes_filtered = df_tropes_filtered.sort_values(by="vote_average")
    df_tropes_filtered.reset_index(drop=True, inplace=True)
    print(f"Number of unique tropes: {df_tropes_filtered['trope'].nunique()}")
    print(f"Number of unique movies: {df_tropes_filtered['imdb_id'].nunique()}")
    print(f"Shape of the filtered dataset: {df_tropes_filtered.shape}")

    # If the output path does not exist, we create it
    Path(OUTPUT_PATH).mkdir(parents=True, exist_ok=True)

    # Get the unique genres and the top k tropes with the highest ratio of low-rated movies
    unique_genres = get_unique_genres(df_tropes_filtered)

    df_low_rated_tropes = df_tropes_filtered[df_tropes_filtered['vote_average'] < threshold]
    df_high_rated_tropes = df_tropes_filtered[df_tropes_filtered['vote_average'] >= threshold]

    # Define the figure and the updatemenus
    fig = go.Figure()
    updatemenus=[
        dict(
            type="buttons",
            buttons=[],
            x=1.05,
            xanchor='left',
            yanchor='top',
        )
    ]
    default_title = f"Top {k} tropes with the highest ratio of low-rated movies for All Genres"

    # Iterate over the unique genres and get the top k tropes with the highest ratio of low-rated movies
    for index, genre in enumerate(unique_genres):
        if genre == "All":
            plot_title = f"Top {k} tropes for all genres"
            df_lr_genre_tropes = df_low_rated_tropes
            df_hr_genre_tropes = df_high_rated_tropes
        else:
            plot_title = f"Top {k} tropes for genre {genre}"
            df_lr_genre_tropes = df_low_rated_tropes[df_low_rated_tropes['genres'].str.contains(genre)]
            df_hr_genre_tropes = df_high_rated_tropes[df_high_rated_tropes['genres'].str.contains(genre)]

        low_rated_tropes = df_lr_genre_tropes.trope.value_counts().to_dict()
        high_rated_tropes = df_hr_genre_tropes.trope.value_counts().to_dict()

        trope_ratios = {}
        for trope in low_rated_tropes:
            low_count = low_rated_tropes[trope]
            high_count = high_rated_tropes.get(trope, 0)

            if low_count >= 5:
                ratio = low_count / (high_count + 1)
                trope_ratios[trope] = ratio

        if len(trope_ratios) < k:
            continue

        sorted_tropes = sorted(trope_ratios.items(), key=lambda x: x[1], reverse=True)[:k]
        df = pd.DataFrame(sorted_tropes, columns=["trope", "ratio"])
        print(f"Genre {genre} has {len(sorted_tropes)} tropes with a ratio of low-rated movies to high-rated movies")

        fig.add_trace(
            go.Bar(
                x=df['ratio'],
                y=df['trope'],
                name=genre,
                orientation='h',
                visible=False if genre != "All" else True,
                marker=dict(color='rgba(11, 127, 1271, 0.7)'),
            )
        )

        title = f"Top {k} tropes with the highest ratio of low-rated movies for genre {genre}"

        updatemenus[0]['buttons'].append(
            dict(
                label=genre,
                method="update",
                args=[
                    {"visible": []}, 
                    {
                        "title": default_title if genre == "All" else title, 
                        "annotations": [dict(text="Choose a genre:", x=1.1, xref="paper", y=1.1, yref="paper", align="right", showarrow=False)]
                    }
                ],
            )
        )

    for i in range(len(updatemenus[0]['buttons'])):
        updatemenus[0]['buttons'][i]['args'][0]['visible'] = [False] * len(unique_genres)
        updatemenus[0]['buttons'][i]['args'][0]['visible'][i] = True

    fig.update_layout(
        updatemenus=updatemenus,
        showlegend=False,
        title=default_title,
        yaxis=dict(
            automargin=True,
            showline=True,
            showgrid=False,
            autorange="reversed",
        ),
        xaxis_title='Ratio of low-rated movies to high-rated movies',
        yaxis_title='Tropes',
        annotations=[dict(text="Choose a genre:", x=1.1, xref="paper", y=1.1, yref="paper", align="right", showarrow=False)]
    )

    fig.show()
    # fig.write_html(f'{OUTPUT_PATH}rq6_tropes.html', full_html=False, include_plotlyjs='cdn')


def rq7(df_cmu_tropes, show_plotly_charts=True):
    # Filter all tropes that appear in less than 15 movies
    df_cmu_tropes_filtered = df_cmu_tropes.groupby('trope').filter(lambda x: len(x) >= 15)

    # Get the top 10 tropes with the lowest average rating
    worst_tropes = df_cmu_tropes_filtered[['trope', 'vote_average']].groupby('trope').mean().sort_values(by='vote_average', ascending=True).head(10)

    # Create a boxplot with the top 10 tropes with the lowest average rating

    if show_plotly_charts:
        fig = px.box(
            df_cmu_tropes_filtered[df_cmu_tropes_filtered['trope'].isin(worst_tropes.index)],
            y='trope',
            x='vote_average',
            title='Top 10 tropes with lowest average rating',
            color='trope',
        )
        fig.update_layout(
            xaxis_title='Average rating',
            yaxis_title='Tropes',
            legend_title='Tropes',
            title_x=0.5,
            yaxis=dict(
                automargin=True,
                showline=True,
                showgrid=False,
            )
        )
        fig.show()
        fig.write_html(f'{OUTPUT_PATH}rq7_tropes_boxplot.html', include_plotlyjs='cdn', full_html=False)
    else:
        plt.figure(figsize=(8, 5))
        sns.boxplot(
            data=df_cmu_tropes_filtered[df_cmu_tropes_filtered['trope'].isin(worst_tropes.index)],
            x='vote_average',
            y='trope',
            palette='viridis',
        )
        plt.xlabel('Average rating')
        plt.ylabel('Tropes')

        plt.title('Top 10 tropes with lowest average rating')
        plt.show()


def rq8(df_cmu_tropes, threshold=6.0, min_trope_occurrences=100):
    print(f"Initial shape: {df_cmu_tropes.shape}")

    df_low_rated_movies = df_cmu_tropes[df_cmu_tropes["vote_average"] <= threshold]
    df_low_rated_movies = df_low_rated_movies.groupby("trope").filter(lambda x: len(x) > min_trope_occurrences)

    print(f"Number of rows after filtering: {df_low_rated_movies.shape}")

    trope_counts = df_low_rated_movies.groupby(["release_year", "trope"]).size().reset_index(name="count")
    tropes_avg_scores = df_low_rated_movies.groupby(["release_year", "trope"])["vote_average"].mean().reset_index()

    fig_counts = px.line(
        trope_counts,
        x="release_year",
        y="count",
        color="trope",
        title="Evolution of tropes use over time",
        labels={"count": "Number of movies using trope", "release_year": "Release year"},
    )
    fig_counts.update_layout(
        legend_title="Tropes",
        title_x=0.5,
    )

    fig_avg_scores = px.line(
        tropes_avg_scores,
        x="release_year",
        y="vote_average",
        color="trope",
        title="Evolution of tropes average scores over time",
        labels={"vote_average": "Average score", "release_year": "Release year"},
    )
    fig_avg_scores.update_layout(
        legend_title="Tropes",
        title_x=0.5,
    )

    fig_counts.show()
    fig_counts.write_html(f'{OUTPUT_PATH}rq8_tropes_counts.html', include_plotlyjs='cdn', full_html=False)

    fig_avg_scores.show()
    fig_avg_scores.write_html(f'{OUTPUT_PATH}rq8_tropes_avg_scores.html', include_plotlyjs='cdn', full_html=False)
