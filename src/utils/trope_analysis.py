import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import math

from pathlib import Path
from plotly.subplots import make_subplots
from src.utils.plot_settings import (
    COLORS,
    COMMON_LAYOUT,
    AXIS_STYLE,
    BAR_STYLE,
    get_title_style,
    create_hover_template, 
    get_subplot_settings
)

OUTPUT_PATH = 'data/preprocessed/'

def get_unique_genres(df_tropes_filtered):
    unique_str_genres = df_tropes_filtered['genres'].unique()
    unique_genres = set()

    for str_genres in unique_str_genres:
        for genre in str_genres.split(","):
            unique_genres.add(genre.strip())

    ordered_genres = ['All'] + sorted([genre for genre in unique_genres if genre != 'All'])
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
            showactive=True,
            active=0,
        ),
        dict(
            type="buttons",
            buttons=[],
            x=1.13,
            xanchor='left',
            yanchor='top',
            showactive=True,
            active=-1,
        )
    ]
    default_title = f"Top {k} tropes with the highest ratio of low-rated movies for All Genres"
    valid_buttons = []

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
                **BAR_STYLE
            )
        )

        title = f"Top {k} tropes with the highest ratio of low-rated movies for genre {genre}"

        valid_buttons.append(
            dict(
                label=genre,
                method="update",
                args=[
                    {"visible": []}, 
                    {"title": default_title if genre == "All" else title}
                ],
            )
        )

    midpoint = math.ceil(len(valid_buttons) / 2)
    updatemenus[0]['buttons'] = valid_buttons[:midpoint]
    updatemenus[1]['buttons'] = valid_buttons[midpoint:]

    for i in range(len(valid_buttons)):
        column = i // midpoint
        button_index = i % midpoint

        visibility = [False] * len(valid_buttons)
        visibility[i] = True

        updatemenus[column]['buttons'][button_index]['args'] = [
        {
            "visible": visibility
        },
        {
            "title": default_title if valid_buttons[i]['label'] == "All" else f"Top {k} tropes with the highest ratio of low-rated movies for genre {valid_buttons[i]['label']}",
            "annotations": [dict(
                text="Choose a genre:",
                x=1.13,
                xref="paper",
                y=1.1,
                yref="paper",
                align="right",
                showarrow=False,
                font=dict(
                    family='Arial, sans-serif',
                    size=14,
                    color='#1F1F1F'
                )
            )],
            "updatemenus[0].active": button_index if column == 0 else -1,  # Reset other column
            "updatemenus[1].active": button_index if column == 1 else -1   # Reset other column
        }
    ]


    fig.update_layout(
        **COMMON_LAYOUT,
        updatemenus=updatemenus,
        showlegend=False,
        title=default_title,
        yaxis=dict(
            automargin=True,
            showline=True,
            autorange="reversed",
            **AXIS_STYLE
        ),
        xaxis_title='Ratio of low-rated movies to high-rated movies',
        yaxis_title='Tropes',
        annotations=[dict(
            text="Choose a genre:",
            x=1.13,
            xref="paper",
            y=1.1,
            yref="paper",
            align="right",
            showarrow=False,
            font=dict(
                family='Arial, sans-serif',
                size=14,
                color='#1F1F1F'
            )
        )]
    )

    fig.show()
    fig.write_html(f'{OUTPUT_PATH}rq6_tropes.html', full_html=False, include_plotlyjs='cdn')


def rq8(df_cmu_tropes, threshold=6.0, min_trope_occurrences=100):
    print(f"Initial shape: {df_cmu_tropes.shape}")

    df_low_rated_movies = df_cmu_tropes[df_cmu_tropes["vote_average"] <= threshold]
    df_low_rated_movies = df_low_rated_movies.groupby("trope").filter(lambda x: len(x) > min_trope_occurrences)

    print(f"Number of rows after filtering: {df_low_rated_movies.shape}")

    # Get the full range of years and tropes
    all_years = range(df_low_rated_movies["release_year"].min(), df_low_rated_movies["release_year"].max() + 1)
    tropes = sorted(df_low_rated_movies["trope"].unique())
    
    # Create complete year-trope combinations and merge with actual data for counts
    year_trope_combinations = pd.DataFrame([(year, trope) for year in all_years for trope in tropes], columns=["release_year", "trope"])
    
    # Process counts with zero-filling
    trope_counts = df_low_rated_movies.groupby(["release_year", "trope"]).size().reset_index(name="count")
    trope_counts = pd.merge(year_trope_combinations, trope_counts, 
                           on=["release_year", "trope"], 
                           how="left").fillna(0)

    max_count = trope_counts["count"].max()
    
    # Process average scores with zero-filling
    tropes_avg_scores = df_low_rated_movies.groupby(["release_year", "trope"])["vote_average"].mean().reset_index()
    tropes_avg_scores = pd.merge(
                                year_trope_combinations,
                                tropes_avg_scores, 
                                on=["release_year", "trope"], 
                                how="left").fillna(0)

    max_avg_score = tropes_avg_scores["vote_average"].max()

    num_tropes = len(tropes)
    num_rows = (num_tropes + 2) // 3

    subplot_settings = get_subplot_settings(num_rows, tropes)
    
    # Create subplots for counts
    fig_counts = make_subplots(**subplot_settings)

    # Add individual line plots for counts
    for idx, trope in enumerate(tropes):
        row = idx // 3 + 1
        col = idx % 3 + 1
        
        trope_data = trope_counts[trope_counts["trope"] == trope].sort_values("release_year")
        
        fig_counts.add_trace(
            go.Scatter(
                x=trope_data["release_year"],
                y=trope_data["count"],
                name=trope,
                showlegend=False,
                mode='lines',
                line=dict(
                    color=COLORS[idx % len(COLORS)],
                    width=2
                ),
                hovertemplate=create_hover_template("Year", "Count", "d")
            ),
            row=row,
            col=col
        )

    fig_counts.update_layout(
        height=300 * num_rows,
        width=1200,
        title=get_title_style("Evolution of Tropes Use Over Time"),
        showlegend=False,
        title_x=0.5,
        **COMMON_LAYOUT
    )
    
    # Create subplots for average scores
    fig_avg_scores = make_subplots(**subplot_settings)

    # Add individual line plots for average scores
    for idx, trope in enumerate(tropes):
        row = idx // 3 + 1
        col = idx % 3 + 1
        
        trope_data = tropes_avg_scores[tropes_avg_scores["trope"] == trope].sort_values("release_year")
        
        fig_avg_scores.add_trace(
            go.Scatter(
                x=trope_data["release_year"],
                y=trope_data["vote_average"],
                name=trope,
                showlegend=False,
                mode='lines',
                line=dict(
                    color=COLORS[idx % len(COLORS)],
                    width=2
                ),
                hovertemplate=create_hover_template("Year", "Average Score")
            ),
            row=row,
            col=col
        )

    # Update layout for average scores
    fig_avg_scores.update_layout(
        height=300 * num_rows,
        width=1200,
        title=get_title_style("Evolution of Tropes Average Scores Over Time"),
        showlegend=False,
        title_x=0.5,
        **COMMON_LAYOUT
    )

    # Update axes styling
    for fig in [fig_counts, fig_avg_scores]:
        fig.update_xaxes(
            title_text="Release Year",
            dtick=20,
            title_standoff=15,
            **AXIS_STYLE
        )
    
    fig_counts.update_yaxes(
        title_text="Number of Movies",
        range=[0, max_count * 1.1],
        **AXIS_STYLE
    )

    fig_avg_scores.update_yaxes(
        title_text="Average Score", 
        range=[0, max_avg_score * 1.1],
        **AXIS_STYLE
    )

    fig_counts.show()
    fig_counts.write_html(f'{OUTPUT_PATH}rq8_tropes_counts.html', include_plotlyjs='cdn', full_html=False)

    fig_avg_scores.show()
    fig_avg_scores.write_html(f'{OUTPUT_PATH}rq8_tropes_avg_scores.html', include_plotlyjs='cdn', full_html=False)
