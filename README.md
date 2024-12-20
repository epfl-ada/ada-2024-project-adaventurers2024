# Decoding Box-Office Bombs 🎬💣

[Website](https://epfl-ada.github.io/ada-2024-project-adaventurers2024/)

## Abstract

In this project, we aim to explore the reasons for a movie's failure by analyzing over 42,000 films, looking at everything from box office numbers to plot patterns. Using data from Wikipedia summaries, IMDb, and TV Tropes, we're investigating what really makes a movie stumble - whether it's poor timing, problematic storytelling, or casting choices. We're particularly interested in how factors like cast diversity, director's track records, and genre selections influence a film's success or failure. By analyzing numbers on movie budgets, audience ratings, and overused plot devices, we aim to uncover patterns that are problematic for films.

## Research Questions

### 📊 Metrics & Performance

1. What **metrics** (e.g., low ratings, limited number of ratings, revenue vs budget) best indicate movie failure?

### 👥 Cast & Crew Analysis

2. How do **actor demographics** and lack of diversity impact audience disengagement and contribute to box office underperformance?

3. Is thematic consistency in **director filmographies** a predictor of movie failure?

### 🎬 Genre & Market Factors

4. How does **genre choice** influence a movie's failure, particularly in different cultural contexts?

5. How does poor **release timing** (e.g., season, holiday periods) affect a movie's likelihood of failing?

### 📖 Narrative & Thematic Elements

6. What recurring **plot patterns** appear most frequently in critically panned films?

7. Which **trope combinations** consistently lead to negative reception by genre?

## Datasets

Our main dataset is the [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/), which contains 42K movie plot summaries from Wikipedia. To complement this dataset, we will utilize additional datasets to enhance our analysis.

### Proposed Additional Datasets

| Dataset                                                                                                             | Description                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [IMDb Non-Commercial](https://developer.imdb.com/non-commercial-datasets/)                                 | Movie and TV show data including titles, ratings, crew, and cast.                                                                                                                                                                                |
| [TV Tropes](https://github.com/dhruvilgala/tvtropes)                                                        | 30K narrative tropes with 1.9M examples, linked to IMDb metadata                                                                                                                                                                                           |
| [TMDB (Kaggle)](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies) | 1M movies with metadata including cast, crew, budget, and revenue.                                                                                                                                                                                   |
| Mappings of ethnicity IDs to corresponding names                                                                    | We used an SPARQL query to retrieve ethnicity IDs and their names from Wikidata |

## Methods

### 1. Data Preprocessing

To create our main dataset, we inspected the CMU Movie Corpus Dataset and identified gaps in the data, such as revenue data. To address this, we merged it with the TMDB dataset using movie titles and release years as common identifiers. The resulting dataset includes 49,516 movies. The IMDb ID column is important because it serves as a unique identifier for a movie, enabling us to merge it with the Tropes dataset. Additionally, we created a file linking directors and actors to movies, using data from IMDb and CMU, to support cast and crew analysis.

To reproduce these preprocessed files, place the necessary datasets in the `data` folder, navigate to `src/scripts`, and run:

```
python preprocess_data.py
```

### 2. Exploratory Data Analysis

We first calculated key financial metrics. Return on Investment (ROI) was computed as $\text{ROI} = \frac{\text{revenue} - \text{budget}}{\text{budget}}$, and absolute profit was calculated as $\text{revenue} - \text{budget}$. We defined movie failure as losing more than 50% of its investment ($\text{ROI}<-0.5$) and success as achieving more than 100% ROI ($\text{ROI}>1$), as the first step in understanding the financial performance of movies.

### 3. Potential methods to handle research questions

#### Metrics for Movie Failure (RQ1)

We chose average vote(i.e., rating/score), revenue, and ROI (Return on Investment) as the metrics of movie failure. We used a scatterplot matrix to uncover patterns and relationships between these metrics, displaying histograms along the diagonal to visualize their distributions. Off-diagonal scatter plots with trendlines reveal the pairwise correlations between the indicators. 

#### Impact of Actors' Demographic Diversity on Movie Failure (RQ2)

To measure actor diversity in movies, we focused on four key factors: age, gender, height, and ethnicity. We used standard deviation to quantify age and height diversity, while using Shannon's entropy to measure gender and ethnicity diversity. We then analyzed these metrics in relation to each movie's average rating and box office revenue using box plots, heatmaps, and radar charts. The box plots visualize the distribution of revenue and average rating across different diversity levels, the heatmap shows the correlations between diversity metrics and movie failure indicators, and the radar plots illustrate how different diversity factors contribute to high and low performance in terms of revenue and ratings.

#### Impact of Directors' Filmography on Film Failure (RQ3)

A director's filmography can be characterized by the diversity of genres in their films. To investigate the relationship between the number of genres explored by directors and their films' success, we create a Sankey diagram. The diagram visualizes the connections between the number of genres directors engage with and the average ratings of their films, with the thickness of the links representing the average revenue associated with these films. By analyzing the patterns in the Sankey diagram, we explore how directors' thematic diversification influences their films' critical reception and financial performance.

#### Genre Influence on Movie Failure (RQ4)

Current analysis uses violin plots for profit distributions, scatter plots for rating-popularity relationships, ROI analysis, and 5-year moving averages for genre evolution. Further refinements could include: regional market segmentation to compare genre performance across cultures, developing a composite risk score combining financial and critical metrics, analyzing genre hybridization effects on failure rates, and identifying genre-specific budget thresholds for optimal risk-return profiles. This would create a more comprehensive understanding of how genres perform in different contexts and market conditions.

#### Release Timing Impact on Failure (RQ5)

Current analysis employs violin plots for seasonal and monthly distributions, temporal trend analysis, and success/failure rate tracking. Potential enhancements include: analyzing holiday-specific effects, creating a competition index based on concurrent releases, examining genre-timing interactions, studying regional variations in optimal release windows, and developing a predictive model incorporating marketing spend and critical reviews. This would provide deeper insights into how timing decisions impact movie performance across different contexts.

#### Tropes Negative Reception (RQ6, RQ7)

To investigate the relationship between narrative tropes and audience reception, we established a rating threshold of 6.0 on a 10-point scale to distinguish between low and high-rated films. Our first step was to identify the 20 most common tropes in low-rated movies. Then, we analyze tropes within specific genres, we focused on Horror, Adventure, and Comedy films for this initial analysis. We calculated a ratio of trope occurrence in low-rated films compared to high-rated films. The results were visualized using bar plots showing tropes that might contribute to negative audience reception.

We also analyzed movies through their associated tropes, creating binary vectors for each film. Each vector has a dimension equal to the total number of unique tropes in our dataset, with 1s indicating the presence of specific tropes and 0s their absence.
Using these binary vectors, we performed k-means clustering with k=50 to identify groups of movies with similar trope patterns. We visualized the resulting clusters using t-SNE dimensionality reduction to examine relationships between movies based on their trope usage.
To understand what makes movies poorly received, we identified the 10 clusters with lowest average ratings, analyzed common trope combinations in these clusters, created a co-occurrence network to visualize how tropes appear together, and examined the evolution of trope usage and ratings over time (1920-present).
Our approach assumes that movies sharing similar tropes likely share narrative patterns, allowing us to identify potentially problematic storytelling combinations through their trope signatures.

## Team contribution

- Jianan Xu: Developed and calculated financial metrics (ROI, profit); created visualizations for movie failure metrics through scatterplots and correlation analyses; conducted actor diversity analysis using multiple metrics; contributed to director filmography analysis methodology; final document story and revision.
- Rizhong Lin: Set up project website infrastructure; analyzed genre influence through profit distributions, rating-popularity relationships and trends; studied release timing impacts using seasonal distributions and temporal trend analysis; final document story and revision.
- Raph Wegmann: Preliminary data analysis for RQ 3.
- Angel Zenteno: Data preprocessing; established trope analysis methodology and rating thresholds; conducted genre-specific trope analysis for multiple genres; implemented clustering analysis and visualizations for trope patterns; developed trope co-occurrence network; final story proofreading and revision.
- Adriana Orellana: Data preprocessing by merging movie datasets; data preprocessing; historical evolution analysis; enhanced website aesthetics and user experience; contributed to all sections by adding relevant images, GIFs, and complementary media content; unified the visual style to ensure a cohesive story; final story proofreading and revision.
  
## Project Structure

```bash
├── data                        <- Project data files
│   │   cmu_tmdb.csv
│   │   movie_actors.csv
│   │   movie_directors_actors.csv
│   │   cmu_tropes.csv
│   │   wikidata_ethnicities.csv
│   │
│   ├───cmu
│   │       character.metadata.tsv
│   │       movie.metadata.tsv
│   │       name.clusters.txt
│   │       plot_summaries.txt
│   │       tvtropes.clusters.txt
│   │
│   ├───imdb
│   │       name.basics.tsv
│   │       title.basics.tsv
│   │       title.crew.tsv
│   │       title.principals.tsv
│   │       title.ratings.tsv
│   │
│   ├───tmdb
│   │       TMDB_movie_dataset_v11.csv
│   │
│   └───tropes
│           film_imdb_match.csv
│           tropes.csv
│
├── src                         <- Source code
│   ├── utils                           <- Utility directory
│   ├── scripts                         <- Shell scripts
│
├── results.ipynb               <- a well-structured notebook showing the results
│
├── .gitignore                  <- List of files ignored by git
├── pip_requirements.txt        <- File for installing python dependencies
└── README.md
```
