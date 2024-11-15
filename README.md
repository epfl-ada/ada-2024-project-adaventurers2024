# Decoding Box-Office Bombs 🎬💣

## Abstract

In this project, we aim to explore the underlying reasons for a movie's failure by examining several key factors, including ratings, number of reviews, revenue, and the influence of demographics. We will investigate how actor diversity, director-actor collaborations, and narrative structures affect a movie's performance across different countries and languages. In particular, we analyze the role of character tropes and thematic content, assessing their impact on both critical acclaim and box office success. By exploring how combinations of common tropes resonate with audiences, and observing trends in thematic content over time, we aim to uncover patterns that contribute to or detract from movie success.

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

To create our main dataset, we inspected the CMU Movie Corpus Dataset and identified gaps in the data, such as revenue data and missing budgets. To address this, we merged it with the TMDB dataset using movie titles and release years as common identifiers, despite varying date formats. The resulting dataset includes 49,516 movies with 27 columns, covering fields like vote average, budget, and IMDb ids. The IMDb id is important because it serves as a unique identifier for a movie, enabling us to merge it with the Tropes dataset. Additionally, we created a file linking directors and actors to movies, using data from IMDb and CMU, to support cast and crew analysis.

To reproduce these preprocessed files, place the necessary datasets in the `data` folder, navigate to `src/scripts`, and run:

```
python preprocess_data.py
```

### 2. Exploratory Data Analysis

We first calculated key financial metrics. Return on Investment (ROI) was computed as $\text{ROI} = \frac{\text{revenue} - \text{budget}}{\text{budget}}$, and absolute profit was calculated as $\text{revenue} - \text{budget}$. To handle extreme values in ROI, we capped positive returns at 5000% and removed cases where losses exceeded 99%, as these often represented data anomalies. We defined movie failure as losing more than 50% of its investment ($\text{ROI}<-0.5$) and success as achieving more than 100% ROI ($\text{ROI}>1$), as the first step in understanding the financial performance of movies.

### 3. Potential methods to handle research questions

#### Metrics for Movie Failure (RQ1)

Current analysis examines metric distributions (ratings, revenue, profit ratios) through histograms and kernel density estimation, investigates relationships through scatter plots of audience metrics versus financial performance, and quantifies correlations between vote_average, vote_count, revenue, budget, and profit through matrix analysis. Future work could develop a composite failure score combining financial and reception metrics, employ clustering and machine learning for pattern identification, and incorporate regional market variations to create a more comprehensive prediction framework.

#### Impact of Actors' Demographic Diversity on Movie Failure (RQ2)

To address how actors' demographics diversity impacts movie failure, we plan to use multiple regression analysis to quantify the impact of gender diversity, ethnic diversity, and age diversity on failure metrics (revenue and average rating), expressed mathematically as

$\text{Failure Metric} = \beta_0 + \beta_1 \times \text{Gender Diversity} + \beta_2 \times \text{Ethnic Diversity} + \beta_3 \times \text{Age Diversity} + \epsilon$.

Clustering algorithms (e.g., k-means) will group movies based on diversity metrics, identifying clusters linked to high failure rates. For visualization, we will use interactive parallel coordinates plots to simultaneously visualize multiple diversity metrics alongside failure indicators and identify trends or patterns across movies. The interactivity will enable filtering and highlighting specific movie samples.

#### Impact of Directors' Filmography on Film Failure (RQ3)

This research question investigates the relationship between a director’s filmography and film failure. A filmography can be characterized through the genres to which its films belong, i.e. a success profile can be constructed for each director by averaging revenues/ratings of each of their film by genre. The first phase of the analysis is to assemble such profiles. The next step is to perform clustering on these profiles in order to identify patterns in film failure relating to the type of directors’ filmographies. Clustering techniques such as the K-Nearest Neighbours (KNN) algorithm (implemented in scikit learn) are employed to classify directors based on their filmographies. The silhouette score is used to evaluate the quality of the clusters, helping to determine distinct career patterns. Cluster centroids and medoids are displayed to illustrate the typical patterns or trends found within each group.

#### Genre Influence on Movie Failure (RQ4)

Current analysis uses violin plots for profit distributions, scatter plots for rating-popularity relationships, ROI analysis, and 5-year moving averages for genre evolution. Further refinements could include: regional market segmentation to compare genre performance across cultures, developing a composite risk score combining financial and critical metrics, analyzing genre hybridization effects on failure rates, and identifying genre-specific budget thresholds for optimal risk-return profiles. This would create a more comprehensive understanding of how genres perform in different contexts and market conditions.

#### Release Timing Impact on Failure (RQ5)

Current analysis employs violin plots for seasonal and monthly distributions, temporal trend analysis, and success/failure rate tracking. Potential enhancements include: analyzing holiday-specific effects, creating a competition index based on concurrent releases, examining genre-timing interactions, studying regional variations in optimal release windows, and developing a predictive model incorporating marketing spend and critical reviews. This would provide deeper insights into how timing decisions impact movie performance across different contexts.

#### Tropes Negative Reception (RQ6, RQ7)

To investigate the relationship between narrative tropes and audience reception, we established a rating threshold of 6.0 on a 10-point scale to distinguish between low and high-rated films. Given the vast number of tropes, our first step was to identify the 20 most common tropes in low-rated movies and show them in a bar plot. Then, we analyze tropes within specific genres, we focused on Horror, Adventure, and Comedy films for this initial analysis. We calculated a ratio of trope occurrence in low-rated films compared to high-rated films. The results were visualized using bar plots showing the top 10 tropes that might contribute to negative audience reception. Next steps include completing the plots for all genres and analyzing combinations of tropes.

## Proposed Timeline

| Deliverable                     | Expected Date |
| ------------------------------- | ------------- |
| Data preprocessing (AO & JX)    | 13/11/2024    |
| Data analysis (Everyone)        | 14/11/2024    |
| Setup Web (RL)                  | 22/11/2024    |
| Group visualizations (Everyone) | 13/12/2024    |
| Storytelling (Everyone)         | 19/12/2024    |

## Organization within the team

- JX: Questions 1, 2
- RL: Questions 4, 5
- RW: Questions 3
- AZ: Questions 6, 7
- AO: Questions 6, 7

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
│   │       README.txt
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
│           .gitattributes
│           film_imdb_match.csv
│           film_tropes.csv
│           genderedness_filtered.csv
│           lit_goodreads_match.csv
│           lit_tropes.csv
│           tropes.csv
│           tv_imdb_match.csv
│           tv_tropes.csv
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
