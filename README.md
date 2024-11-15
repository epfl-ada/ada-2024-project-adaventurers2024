# Decoding Box-Office Bombs

## Abstract

In this project, we aim to explore the underlying reasons for a movie's failure by examining several key factors, including ratings, number of reviews, revenue, and the influence of demographics. We will investigate how actor diversity, director-actor collaborations, and narrative structures affect a movie's performance across different countries and languages. In particular, we analyze the role of character tropes and thematic content, assessing their impact on both critical acclaim and box office success. By exploring how combinations of common tropes resonate with audiences, and observing trends in thematic content over time, we aim to uncover patterns that contribute to or detract from movie success.

<!-- ## Research Questions

1. [Metrics ] What metrics (e.g., low ratings, limited number of ratings, revenue vs budget) best indicate movie failure?
2. [Actor   ] How do actor demographics and lack of diversity impact audience disengagement and contribute to box office underperformance?
3. [Director] What role do director-actor collaborations play in a movie's failure, and are there specific patterns in these partnerships that correlate with unsuccessful films?
4. [Director] Is thematic consistency in director filmographies a predictor of failure/success?
5. [Genre   ] How does genre choice influence a movie's failure, particularly in different cultural contexts?
6. [Timing  ] How does poor release timing (e.g., season, holiday periods) affect a movie's likelihood of failing?
7. [Tropes  ] How do overused or poorly executed character tropes contribute to a movie's box office failure?
8. [Tropes  ] How has the thematic content of movie plots evolved, and what themes have historically failed to resonate with audiences?
9. [Tropes  ] How does portraying controversial social issues or outdated themes affect a movie's acceptance and potential failure across demographics? -->

## Research Questions

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

7. How do overused or poorly executed character **tropes** contribute to a movie's box office failure?

8. How has the **thematic content** of movie plots evolved, and what themes have historically failed to resonate with audiences?

9. How does portraying **controversial topics** affect a movie's acceptance and potential failure across demographics?

## Datasets

| Dataset                                                          | Description                                                                                                           |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| [CMU Movie Summary Corpus](http://www.cs.cmu.edu/~ark/personas/) | 42K movie plot summaries from Wikipedia with metadata including box office, genre, characters, and actor demographics |

### Proposed Additional Datasets

| Dataset                                                                                                             | Description                                                                            |
| ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [IMDb Non-Commercial Datasets](https://developer.imdb.com/non-commercial-datasets/)                                 | Movie and TV show data including titles, ratings, crew, cast, episodes (updated daily) |
| [TV Tropes Dataset](https://github.com/dhruvilgala/tvtropes)                                                        | 30K narrative tropes with 1.9M examples, linked to IMDb and Goodreads metadata         |
| [TMDB Movies Dataset 2024 (Kaggle)](https://www.kaggle.com/datasets/asaniczka/tmdb-movies-dataset-2023-930k-movies) | 1M movies with metadata including cast, crew, budget, revenue, and popularity metrics  |
| Deirector information scraped from Wikipedia 																		  | This table contains director names, birthdates, filmography, the number of Academy Award nominations received for Best Director, and whether the director was awarded the Palme d'Or. For directors awarded the Palme d'Or, the date of the award will also be recorded.  |


## Methods

Team meeting via Zoom at 6:30 PM on Wednesday, 13/11/2024.

**RQ3**
Career Pattern Analysis: The first phase of analysis focuses on identifying patterns in directors' careers by examining the number and timing of films they directed over their active years. Success and productivity will be quantified by counting the total number of films each director has directed, as well as calculating the frequency of films released per year. This information is synthesized into a "career profile" for each director, which visually represents the frequency of their directorial work throughout their career. Additionally, clustering techniques such as the K-Nearest Neighbors (KNN) algorithm will be employed to classify directors based on their career trajectories. The silhouette score will be used to evaluate the quality of the clusters, helping to determine distinct career patterns. Cluster centroids and medoids will be visualized to illustrate the typical patterns or trends found within each group.
Director-Actor Collaboration Analysis: The second phase examines patterns in director-actor collaborations, analyzing the extent and consistency of directors’ relationships with actors. For each director, the analysis will compute the number of unique actors with whom they have collaborated over their careers. The consistency of collaborations is quantified by dividing the total number of unique actor collaborations by the number of films directed, producing a “consistency score” that reflects the director's tendency to either work with a diverse cast or with recurring collaborators. Furthermore, a "collaboration profile" is constructed for each director, which categorizes directors based on their collaboration patterns. As before, clustering analysis will be applied to these profiles. The number of awards and nominations associated with each cluster is compared to identify potential correlations between collaboration patterns and critical success. 

**RQ4**
Genre Participation and Career Profiles: To explore the extent to which directing in one genre may conflict with directing in others, we analyze directors' genre participation proportions. Using a heatmap, we visualize these correlations, revealing distinct career profiles based on directors’ genre preferences or specialization patterns. A clustering approach is then applied to further identify groups with similar genre profiles. The distribution of directors’ birth years across clusters is assessed to identify any generational trends or shifts in genre preferences.
Thematic Consistency and Critical Success: We measure thematic consistency by evaluating the presence of recurring tropes across directors' filmographies, excluding those with fewer than three films to ensure robust data. Thematic consistency is quantified by dividing the number of unique tropes by the total number of films, while the dominance of specific tropes is assessed by finding the most frequent trope and dividing its count by the number of films directed. The study then investigates whether a high or low thematic consistency correlates with critical success, measured through Academy Award nominations and Palme d’Or wins, to determine if thematic focus or diversity is associated with greater acclaim in the film industry.



### Data Processing

### ADA

### Potiential Methods to Handle RQ

## Proposed Timeline

| Deliverable                       | Expected Date |
| --------------------------------- | ------------- |
| Data preprocessing (AZ & AO & JX) | 12/11/2024    |
| Gantt Chart (RW)                  | 12/11/2024    |
| Data analysis (Everyone)          | 14/11/2024    |
| Setup Web (RL)                    | 22/11/2024    |
| Group visualizations (Everyone)   | 13/12/2024    |
| Storytelling (Everyone)           | 19/12/2024    |

## Organization within the team

?? A list of internal milestones up until project Milestone P3. ??

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
