import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path
from sklearn.manifold import TSNE
from sklearn.preprocessing import normalize
from matplotlib import cm
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from sklearn.manifold import TSNE
from sklearn.preprocessing import normalize
from matplotlib import cm
import plotly.express as px
import plotly.graph_objects as go
from sklearn.cluster import KMeans 
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import plotly.graph_objects as go
import networkx as nx
from collections import defaultdict

OUTPUT_PATH = "data/preprocessed/"


def get_unique_genres(df_tropes_filtered):
    unique_str_genres = df_tropes_filtered["genres"].unique()
    unique_genres = set()

    for str_genres in unique_str_genres:
        for genre in str_genres.split(","):
            unique_genres.add(genre.strip())

    unique_genres.add("All")

    print(f"{len(unique_genres)} unique genres: {unique_genres}")
    return unique_genres


def rq6(df_cmu_tropes, threshold=6.0, k=5, min_votes=100, show_plotly_charts=True):
    df_tropes_filtered = df_cmu_tropes[
        (df_cmu_tropes[["vote_average", "revenue"]] != 0).all(axis=1)
    ]

    df_tropes_filtered = df_tropes_filtered[
        df_tropes_filtered["vote_count"] > min_votes
    ]
    df_tropes_filtered = df_tropes_filtered.sort_values(by="vote_average")
    df_tropes_filtered.reset_index(drop=True, inplace=True)
    print(f"Number of unique tropes: {df_tropes_filtered['trope'].nunique()}")
    print(f"Number of unique movies: {df_tropes_filtered['imdb_id'].nunique()}")
    print(f"Shape of the filtered dataset: {df_tropes_filtered.shape}")

    # If the output path does not exist, we create it
    Path(OUTPUT_PATH).mkdir(parents=True, exist_ok=True)

    unique_genres = get_unique_genres(df_tropes_filtered)

    df_low_rated_tropes = df_tropes_filtered[
        df_tropes_filtered["vote_average"] < threshold
    ]
    df_high_rated_tropes = df_tropes_filtered[
        df_tropes_filtered["vote_average"] >= threshold
    ]

    for genre in unique_genres:
        if genre == "All":
            plot_title = f"Top {k} tropes for all genres"
            df_lr_genre_tropes = df_low_rated_tropes
            df_hr_genre_tropes = df_high_rated_tropes
        else:
            plot_title = f"Top {k} tropes for genre {genre}"
            df_lr_genre_tropes = df_low_rated_tropes[
                df_low_rated_tropes["genres"].str.contains(genre)
            ]
            df_hr_genre_tropes = df_high_rated_tropes[
                df_high_rated_tropes["genres"].str.contains(genre)
            ]

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

        sorted_tropes = sorted(trope_ratios.items(), key=lambda x: x[1], reverse=True)[
            :k
        ]
        df = pd.DataFrame(sorted_tropes, columns=["trope", "ratio"])
        print(
            f"Genre {genre} has {len(sorted_tropes)} tropes with a ratio of low-rated movies to high-rated movies"
        )

        if show_plotly_charts:
            fig = px.bar(
                df,
                x="ratio",
                y="trope",
                orientation="h",
                title=plot_title,
                color="trope",
            )
            fig.update_layout(
                xaxis_title="Ratio of low-rated movies to high-rated movies",
                yaxis_title="Tropes",
                yaxis_categoryorder="total ascending",
                legend_title="Tropes",
                title_x=0.5,
                yaxis=dict(
                    automargin=True,
                    showline=True,
                    showgrid=False,
                ),
            )
            fig.show()
            fig.write_html(
                f"{OUTPUT_PATH}rq6_{genre.lower()}_tropes.html",
                full_html=False,
                include_plotlyjs="cdn",
            )
        else:
            plt.figure(figsize=(7, 4))
            sns.barplot(
                x="ratio",
                y="trope",
                data=df,
                palette="viridis",
            )
            plt.xlabel("Ratio of low-rated movies to high-rated movies")
            plt.ylabel("Tropes")
            plt.title(plot_title)
            plt.show()


def rq7(df_cmu_tropes, show_plotly_charts=True):
    # Filter all tropes that appear in less than 15 movies
    df_cmu_tropes_filtered = df_cmu_tropes.groupby("trope").filter(
        lambda x: len(x) >= 15
    )

    # Get the top 10 tropes with the lowest average rating
    worst_tropes = (
        df_cmu_tropes_filtered[["trope", "vote_average"]]
        .groupby("trope")
        .mean()
        .sort_values(by="vote_average", ascending=True)
        .head(10)
    )

    # Create a boxplot with the top 10 tropes with the lowest average rating

    if show_plotly_charts:
        fig = px.box(
            df_cmu_tropes_filtered[
                df_cmu_tropes_filtered["trope"].isin(worst_tropes.index)
            ],
            y="trope",
            x="vote_average",
            title="Top 10 tropes with lowest average rating",
            color="trope",
        )
        fig.update_layout(
            xaxis_title="Average rating",
            yaxis_title="Tropes",
            legend_title="Tropes",
            title_x=0.5,
            yaxis=dict(
                automargin=True,
                showline=True,
                showgrid=False,
            ),
        )
        fig.show()
        fig.write_html(
            f"{OUTPUT_PATH}rq7_tropes_boxplot.html",
            include_plotlyjs="cdn",
            full_html=False,
        )
    else:
        plt.figure(figsize=(8, 5))
        sns.boxplot(
            data=df_cmu_tropes_filtered[
                df_cmu_tropes_filtered["trope"].isin(worst_tropes.index)
            ],
            x="vote_average",
            y="trope",
            palette="viridis",
        )
        plt.xlabel("Average rating")
        plt.ylabel("Tropes")

        plt.title("Top 10 tropes with lowest average rating")
        plt.show()

def cluster_movies(df_cmu_tropes, df_tropes, n_clusters, n_tropes):
    trope_to_idx = {trope_id: idx for idx, trope_id in enumerate(df_tropes["TropeID"])}
    idx_to_trope = {idx: trope_id for idx, trope_id in enumerate(df_tropes["TropeID"])}

    movie_embeddings = {}

    for i, row in df_cmu_tropes.iterrows():
        if row['id'] not in movie_embeddings:
            movie_embeddings[row['id']] = np.zeros(n_tropes)
        
        trope_id = row['trope_id']
        movie_embeddings[row['id']][trope_to_idx[trope_id]] = 1

    X = np.array(list(movie_embeddings.values()))
    X_normalized = normalize(X)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(X_normalized)

    print("Cluster labels shape:", kmeans.labels_.shape)
    print("Number of samples in each cluster:", np.bincount(kmeans.labels_))
    print("Cluster centers shape:", kmeans.cluster_centers_.shape)

    return X_normalized, kmeans, movie_embeddings

def plot_movie_clusters(X_normalized, kmeans):
    tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=1000)
    X_2d = tsne.fit_transform(X_normalized)

    tab10_colors = cm.tab10.colors

    fig = go.Figure()

    for i, cluster in enumerate(sorted(set(kmeans.labels_))):
        mask = kmeans.labels_ == cluster
        color = f'rgb({int(tab10_colors[i % 10][0]*255)},{int(tab10_colors[i % 10][1]*255)},{int(tab10_colors[i % 10][2]*255)})'
        
        fig.add_trace(go.Scatter(
            x=X_2d[mask, 0],
            y=X_2d[mask, 1],
            mode='markers',
            name=f'Cluster {cluster}',
            marker=dict(
                size=8,
                color=color
            ),
            hovertemplate="<br>".join([
                "t-SNE 1: %{x:.2f}",
                "t-SNE 2: %{y:.2f}",
                f"Cluster: {cluster}"
            ])
        ))

    fig.update_layout(
        title='Movie clusters by tropes',
        xaxis_title='First t-SNE Component',
        yaxis_title='Second t-SNE Component',
        showlegend=True,
        width=1000,
        height=800
    )

    fig.show()

def plot_worst_clusters(df_cmu_tmdb_filtered, X_normalized, kmeans, top_k):
    tsne = TSNE(n_components=2, random_state=42, perplexity=30, n_iter=1000)
    X_2d = tsne.fit_transform(X_normalized)

    cluster_avg_vote_average = df_cmu_tmdb_filtered.groupby("cluster")["vote_average"].mean()
    cluster_avg_vote_average = cluster_avg_vote_average.sort_values(ascending=True)
    worst_clusters = cluster_avg_vote_average[:top_k]

    idx = [i for i, cluster in enumerate(kmeans.labels_) if cluster in worst_clusters.index]
    X_2d_worst = X_2d[idx]

    cluster_labels = [f"Cluster {label}" for label in kmeans.labels_[idx]]
    tab10_colors = cm.tab10.colors

    fig = go.Figure()

    for i, cluster in enumerate(sorted(set(kmeans.labels_[idx]))):
        mask = kmeans.labels_[idx] == cluster
        color = f'rgb({int(tab10_colors[i][0]*255)},{int(tab10_colors[i][1]*255)},{int(tab10_colors[i][2]*255)})'
        
        fig.add_trace(go.Scatter(
            x=X_2d_worst[mask, 0],
            y=X_2d_worst[mask, 1],
            mode='markers',
            name=f'Cluster {cluster}',
            marker=dict(
                size=8,
                color=color
            ),
            hovertemplate="<br>".join([
                "t-SNE 1: %{x:.2f}",
                "t-SNE 2: %{y:.2f}",
                f"Cluster: {cluster}",
                f"Avg Rating: {worst_clusters[cluster]:.2f}"
            ])
        ))

    fig.update_layout(
        title='Top 10 Worst-Rated Clusters Visualized with t-SNE',
        xaxis_title='First t-SNE Component',
        yaxis_title='Second t-SNE Component',
        showlegend=True,
        width=1000,
        height=800
    )

    fig.show()

def compute_worst_clusters_tropes(df_cmu_tmdb_filtered, df_cmu_tropes):
    cluster_avg_vote_average = df_cmu_tmdb_filtered.groupby("cluster")["vote_average"].mean()
    worst_clusters_by_rating = cluster_avg_vote_average.sort_values(ascending=True)[:10]

    worst_clusters_tropes = {}
    for cluster in worst_clusters_by_rating.index:
        df_cmu_tropes_filtered = df_cmu_tropes[df_cmu_tropes["id"].isin(df_cmu_tmdb_filtered[df_cmu_tmdb_filtered["cluster"] == cluster]["id"])]
        counts = df_cmu_tropes_filtered["trope"].value_counts().head(10)
        worst_clusters_tropes[cluster] = counts.to_dict()

    return worst_clusters_tropes

def plot_trope_combinations(worst_clusters_tropes):
    tab10_colors = cm.tab10.colors
    color = f'rgb({int(tab10_colors[0][0]*255)},{int(tab10_colors[0][1]*255)},{int(tab10_colors[0][2]*255)})'

    def get_top_tropes(tropes_dict, n=3):
        sorted_tropes = sorted(
            [(k, v) for k, v in tropes_dict.items()],
            key=lambda x: x[1],
            reverse=True
        )
        return ' + '.join(trope for trope, _ in sorted_tropes[:n]), sum(tropes_dict.values())

    combinations = []
    weights = []
    for cluster, tropes in worst_clusters_tropes.items():
        combo, weight = get_top_tropes(tropes)
        combinations.append(combo)
        weights.append(weight)

        if len(combinations) == 10:
            break

    fig = go.Figure()

    colors = [f'rgb({int(tab10_colors[i][0]*255)},{int(tab10_colors[i][1]*255)},{int(tab10_colors[i][2]*255)})' for i in range(3)]  

    fig.add_trace(go.Bar(
        x=weights,
        y=combinations,
        orientation='h',
        marker=dict(
            color=weights,
            colorscale=colors,
        ),
        hovertemplate='Weight: %{x}<br>%{y}<extra></extra>'
    ))

    fig.update_layout(
        title={
            'text': 'Worst Trope Combinations',
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 20}
        },
        xaxis_title='Total Weight',
        yaxis_title=None,
        height=500,
        width=1000,
        margin=dict(l=20, r=20, t=60, b=40),
        yaxis={'categoryorder': 'total ascending'}
    )

    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    fig.update_yaxes(
        showgrid=False,
        automargin=True,
        tickfont={'size': 12}
    )

    fig.show()

def plot_trope_network(worst_clusters_tropes):
    cooccurrence = defaultdict(lambda: defaultdict(int))
    trope_frequencies = defaultdict(int)

    for cluster in worst_clusters_tropes.values():
        tropes = list(cluster.keys())
        for i in range(len(tropes)):
            trope1 = tropes[i]
            trope_frequencies[trope1] += cluster[trope1]
            for j in range(i + 1, len(tropes)):
                trope2 = tropes[j]
                weight = min(cluster[trope1], cluster[trope2])
                cooccurrence[trope1][trope2] += weight
                cooccurrence[trope2][trope1] += weight

    filtered_tropes = {trope: freq for trope, freq in trope_frequencies.items() if freq >= 25}

    G = nx.Graph()

    for trope, freq in filtered_tropes.items():
        G.add_node(trope, size=freq)

    for trope1, connections in cooccurrence.items():
        if trope1 in filtered_tropes:
            for trope2, weight in connections.items():
                if trope2 in filtered_tropes:
                    if weight > 0:
                        G.add_edge(trope1, trope2, weight=weight)

    isolated_nodes = list(nx.isolates(G))
    G.remove_nodes_from(isolated_nodes)
    pos = nx.spring_layout(G, k=3.0, iterations=100)

    edge_trace = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        weight = G.edges[edge]['weight']
        
        edge_trace.append(
            go.Scatter(
                x=[x0, x1, None],
                y=[y0, y1, None],
                line=dict(width=0.5 + (weight/15), color='rgba(136, 136, 136, 0.6)'),
                hoverinfo='none',
                mode='lines',
                opacity=0.5
            )
        )

    node_x = []
    node_y = []
    node_text = []
    node_size = []

    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(node)
        node_size.append(G.nodes[node]['size'])

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode='markers+text',
        hoverinfo='text',
        text=node_text,
        textposition="top center",
        marker=dict(
            showscale=True,
            size=[20 + (40 * s/max(node_size)) for s in node_size],  # Normalize to range 20-60
            color=node_size,
            colorscale='Reds',
            reversescale=False,
            colorbar=dict(
                title='Trope Frequency',
                thickness=15,
                x=0.9
            ),
            line=dict(width=2)
        )
    )

    fig = go.Figure(data=edge_trace + [node_trace],
                    layout=go.Layout(
                        title='Trope Co-occurrence Network in Movies',
                        titlefont=dict(size=16),
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20,l=5,r=5,t=40),
                        annotations=[
                            dict(
                                text="Node size represents trope frequency<br>Edge thickness represents co-occurrence strength",
                                showarrow=False,
                                xref="paper", yref="paper",
                                x=0, y=-0.1
                            )
                        ],
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        width=1200,
                        height=1000
                    ))

    fig.show()

def rq8(df_cmu_tropes, threshold=6.0, min_trope_occurrences=100):
    print(f"Initial shape: {df_cmu_tropes.shape}")

    df_low_rated_movies = df_cmu_tropes[df_cmu_tropes["vote_average"] <= threshold]
    df_low_rated_movies = df_low_rated_movies.groupby("trope").filter(
        lambda x: len(x) > min_trope_occurrences
    )

    print(f"Number of rows after filtering: {df_low_rated_movies.shape}")

    trope_counts = (
        df_low_rated_movies.groupby(["release_year", "trope"])
        .size()
        .reset_index(name="count")
    )
    tropes_avg_scores = (
        df_low_rated_movies.groupby(["release_year", "trope"])["vote_average"]
        .mean()
        .reset_index()
    )

    fig_counts = px.line(
        trope_counts,
        x="release_year",
        y="count",
        color="trope",
        title="Evolution of tropes use over time",
        labels={
            "count": "Number of movies using trope",
            "release_year": "Release year",
        },
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
    fig_counts.write_html(
        f"{OUTPUT_PATH}rq8_tropes_counts.html", include_plotlyjs="cdn", full_html=False
    )

    fig_avg_scores.show()
    fig_avg_scores.write_html(
        f"{OUTPUT_PATH}rq8_tropes_avg_scores.html",
        include_plotlyjs="cdn",
        full_html=False,
    )
