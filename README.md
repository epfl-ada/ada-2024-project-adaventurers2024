# Decoding Box-Office Bombs 🎬💣

## Abstract

In this project, we aim to explore the underlying reasons for a movie's failure by examining several key factors, including ratings, number of reviews, revenue, and the influence of demographics. We will investigate how actor diversity, director-actor collaborations, and narrative structures affect a movie's performance across different countries and languages. In particular, we analyze the role of character tropes and thematic content, assessing their impact on both critical acclaim and box office success. By exploring how combinations of common tropes resonate with audiences, and observing trends in thematic content over time, we aim to uncover patterns that contribute to or detract from movie success.

## Research Questions

Our research questions are organized around four main categories, which are designed to address the following sub-questions:

### 📊 Metrics & Performance

1. What **metrics** (e.g., low ratings, limited number of ratings, revenue vs budget) best indicate movie failure?

### 👥 Cast & Crew Analysis

2. How do **actor demographics** and lack of diversity impact audience disengagement and contribute to box office underperformance?

3. What role do **director-actor collaborations** play in a movie's failure, and are there specific patterns in these partnerships that correlate with unsuccessful films?

4. Is thematic consistency in **director filmographies** a predictor of failure/success?

### 🎬 Genre & Market Factors

5. How does **genre choice** influence a movie's failure, particularly in different cultural contexts?

6. How does poor **release timing** (e.g., season, holiday periods) affect a movie's likelihood of failing?

### 📖 Narrative & Thematic Elements

7. Which **trope combinations** consistently lead to negative reception by genre?

8. What recurring **plot patterns** appear most frequently in critically panned films?

## Datasets

For this project, our main dataset is the [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/), which contains 42K movie plot summaries from Wikipedia with metadata including genre, characters, and actor demographics. To complement this dataset, we will utilize additional datasets to enhance our analysis.

### Proposed Additional Datasets

| Dataset                                                                                                             | Description                                                                            |
| ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [IMDb Non-Commercial Datasets](https://developer.imdb.com/non-commercial-datasets/)                                 | Movie and TV show data including titles, ratings, crew, cast, episodes (updated daily) |
| [TV Tropes Dataset](https://github.com/dhruvilgala/tvtropes)                                                        | 30K narrative tropes with 1.9M examples, linked to IMDb and Goodreads metadata         |
| [TMDB Movies Dataset 2024 (Kaggle)](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies) | 1M movies with metadata including cast, crew, budget, revenue, and popularity metrics  |
| Deirector information scraped from Wikipedia 																		  | This table contains director names, birthdates, filmography, the number of Academy Award nominations received for Best Director, and whether the director was awarded the Palme d'Or. For directors awarded the Palme d'Or, the date of the award will also be recorded.  |


## Methods

### 1. Data Preprocessing


### Data Processing
=======
To create our main dataset that addresses our research questions, we inspected the CMU Movie Corpus Dataset and identified gaps in the data, such as revenue information for only 8,401 movies and missing budget data. To fill these gaps, we merged the TMDB dataset, which provides more complete information on revenue and other field. We used the movie title and release year as common identifiers for merging the datasets, as the release date format varied (yy-mm-dd, yy-mm, or yy). The resulting merged dataset contains 49,516 movies with 27 columns, including vote average, vote count, runtime, budget, IMDb id, and more.

The IMDb id field is important because it serves as a unique identifier for a movie, enabling us to merge them with the Tropes dataset. Since each movie can be associated with multiple tropes, the resulting merged dataframe contains more than 200k rows.

Finally, we generated a file linking directors and actors to each movie that takes into account the IMDb and CMU datasets to facilitate our cast and crew analysis.

To reproduce the preprocessed files that contain the information previously described, navigate to `src/scripts` and run the following script:

```
python preprocess_data.py
```

### 2. Exploratory Data Analysis

We first calculated key financial metrics. Return on Investment (ROI) was computed as $\text{ROI} = \frac{\text{revenue} - \text{budget}}{\text{budget}}$, and absolute profit was calculated as $\text{revenue} - \text{budget}$. To handle extreme values in ROI, we capped positive returns at 5000% and removed cases where losses exceeded 99%, as these often represented data anomalies. We defined movie failure as losing more than 50% of its investment ($\text{ROI}<-0.5$) and success as achieving more than 100% ROI.

For genre analysis, we processed the genre field by splitting multiple genres per movie and creating individual entries for each genre-movie combination. This allowed us to analyze each genre's performance independently while accounting for movies that belong to multiple genres. We examined genre performance through profit distribution, rating patterns (0-10 scale), and success/failure rates.

For release timing analysis, we extracted and categorized temporal information from release dates into seasons (Winter: Dec-Feb, Spring: Mar-May, Summer: Jun-Aug, Fall: Sep-Nov) and months. This enabled us to identify seasonal patterns in movie performance and potential risk periods for movie releases.

### 3. Potiential methods to handle research questions

#### Directors: Career Pattern Analysis (RQ3)
: The first phase of analysis focuses on identifying patterns in directors' careers by examining the number and timing of films they directed over their active years. Success and productivity will be quantified by counting the total number of films each director has directed, as well as calculating the frequency of films released per year. This information is synthesized into a "career profile" for each director, which visually represents the frequency of their directorial work throughout their career. Additionally, clustering techniques such as the K-Nearest Neighbors (KNN) algorithm will be employed to classify directors based on their career trajectories. The silhouette score will be used to evaluate the quality of the clusters, helping to determine distinct career patterns. Cluster centroids and medoids will be visualized to illustrate the typical patterns or trends found within each group.
Director-Actor Collaboration Analysis: The second phase examines patterns in director-actor collaborations, analyzing the extent and consistency of directors’ relationships with actors. For each director, the analysis will compute the number of unique actors with whom they have collaborated over their careers. The consistency of collaborations is quantified by dividing the total number of unique actor collaborations by the number of films directed, producing a “consistency score” that reflects the director's tendency to either work with a diverse cast or with recurring collaborators. Furthermore, a "collaboration profile" is constructed for each director, which categorizes directors based on their collaboration patterns. As before, clustering analysis will be applied to these profiles. The number of awards and nominations associated with each cluster is compared to identify potential correlations between collaboration patterns and critical success. 

#### Directors: Genre and Tropes (RQ4)
Genre Participation and Career Profiles: To explore the extent to which directing in one genre may conflict with directing in others, we analyze directors' genre participation proportions. Using a heatmap, we visualize these correlations, revealing distinct career profiles based on directors’ genre preferences or specialization patterns. A clustering approach is then applied to further identify groups with similar genre profiles. The distribution of directors’ birth years across clusters is assessed to identify any generational trends or shifts in genre preferences.
Thematic Consistency and Critical Success: We measure thematic consistency by evaluating the presence of recurring tropes across directors' filmographies, excluding those with fewer than three films to ensure robust data. Thematic consistency is quantified by dividing the number of unique tropes by the total number of films, while the dominance of specific tropes is assessed by finding the most frequent trope and dividing its count by the number of films directed. The study then investigates whether a high or low thematic consistency correlates with critical success, measured through Academy Award nominations and Palme d’Or wins, to determine if thematic focus or diversity is associated with greater acclaim in the film industry.

#### Genre Influence on Movie Failure (RQ5)
We employed several analytical approaches to understand genre impact on movie failure. First, we used violin plots with symmetric log scaling to visualize profit distribution across genres, capturing both the central tendency and spread of financial performance. To understand cultural reception, we analyzed the relationship between ratings and popularity (measured by vote count) using scatter plots with logarithmic scaling for vote counts. We tracked genre performance over time using 5-year moving averages to identify long-term trends in audience reception. Finally, we calculated and compared genre-specific success and failure rates to identify which genres carry the highest risk of significant financial loss.

#### Release Timing Impact on Failure (RQ6)
To investigate how release timing affects movie failure, we analyzed the distribution of profits and ratings across different temporal categories using violin plots. We compared failure rates across seasons and months to identify particularly risky release periods. To account for industry evolution, we examined the temporal trends of success and failure rates alongside movie release volume using a dual-axis visualization combining line graphs for rates and bar charts for release counts. This allowed us to identify historical patterns in optimal release timing while controlling for changes in industry output volume.
>>>>>>> cf2e8b4383507a51bed4c369cc3b9f117edbb899



## Proposed Timeline

| Deliverable                       | Expected Date |
| --------------------------------- | ------------- |
| Data preprocessing (AO & JX)      | 13/11/2024    |
| Gantt Chart (RW)                  | 13/11/2024    |
| Data analysis (Everyone)          | 14/11/2024    |
| Setup Web (RL)                    | 22/11/2024    |
| Group visualizations (Everyone)   | 13/12/2024    |
| Storytelling (Everyone)           | 19/12/2024    |

## Organization within the team

- JX: Questions 2, 3, 4
- RL: Questions 5, 6
- RW: Questions 2, 3, 4
- AZ: Questions 7, 8, 9
- AO: Questions 7, 8, 9

## Questions for TAs (optional)

!! Add here any questions you have for us related to the proposed project. !!

## Project Structure

TBD

```bash
├── data                        <- Project data files
│
├── src                         <- Source code
│   ├── data                            <- Data directory
│   ├── models                          <- Model directory
│   ├── utils                           <- Utility directory
│   ├── scripts                         <- Shell scripts
│
├── tests                       <- Tests of any kind
│
├── results.ipynb               <- a well-structured notebook showing the results
│
├── .gitignore                  <- List of files ignored by git
├── pip_requirements.txt        <- File for installing python dependencies
└── README.md
```
