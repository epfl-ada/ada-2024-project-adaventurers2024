# Decoding Box-Office Bombs 🎬💣

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

Current analysis examines metric distributions (ratings, revenue, profit ratios) through histograms and kernel density estimation, investigates relationships through scatter plots of audience metrics versus financial performance, and quantifies correlations between vote_average, vote_count, revenue, budget, and profit through matrix analysis. Future work could develop a composite failure score combining financial and reception metrics, employ clustering and machine learning for pattern identification.

#### Impact of Actors' Demographic Diversity on Movie Failure (RQ2)

To address how actors' demographics diversity impacts movie failure, we plan to use multiple regression analysis to quantify the impact of gender, ethnicity, and age diversity on failure metrics (revenue and average rating), expressed mathematically as

$\text{Failure Metric} = \beta_0 + \beta_1 \times \text{Gender Diversity} + \beta_2 \times \text{Ethnic Diversity} + \beta_3 \times \text{Age Diversity} + \epsilon$.

Clustering algorithms (e.g., k-means) will group movies based on diversity metrics, identifying clusters linked to high failure rates. For visualization, we will use interactive parallel coordinates plots to simultaneously visualize multiple diversity metrics alongside failure indicators and identify trends or patterns across movies. The interactivity will enable highlighting specific movie samples.

#### Impact of Directors' Filmography on Film Failure (RQ3)

A director's filmography can be characterized by the diversity of genres in their films. A failure indicator for each director can be constructed by averaging the revenues or ratings of their films across genres. The first phase of the analysis involves assembling these profiles. The next step is to perform clustering on them to identify patterns in film failure related to directors' filmographies. Clustering techniques such as the K-Nearest Neighbours (KNN) algorithm are employed to classify directors based on their filmographies. The silhouette score is used to evaluate the quality of the clusters, helping to determine distinct career patterns. Cluster centroids and medoids are displayed to illustrate the typical patterns or trends found within each group.

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

## Proposed Timeline

| Deliverable                     | Expected Date |
| ------------------------------- | ------------- |
| Data preprocessing              | 13/11/2024    |
| Data analysis                   | 14/11/2024    |
| Setup Web                       | 22/11/2024    |
| Group visualizations            | 13/12/2024    |
| Storytelling                    | 19/12/2024    |

## Organization within the team

- Jianan Xu: Data preprocessing; data analysis, visulization, story from RQ 1, 2, and 3.
- RL: Website setup; data analysis, visulization, story from RQ 4, 5, and 6.
- RW: Data analysis for RQ 3.
- AZ: Data preprocessing; Data analysis, visulization, story from RQ 7 and 8; Website beautification.
- AO: Data preprocessing; Data analysis, visulization, story from RQ 7 and 8.

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
