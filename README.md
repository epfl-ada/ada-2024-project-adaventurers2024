# Decoding Box-Office Bombs 🎬💣

## Abstract

In this project, we aim to explore the underlying reasons for a movie's failure by examining several key factors, including ratings, number of reviews, revenue, and the influence of demographics. We will investigate how actor diversity, director-actor collaborations, and narrative structures affect a movie's performance across different countries and languages. In particular, we analyze the role of character tropes and thematic content, assessing their impact on both critical acclaim and box office success. By exploring how combinations of common tropes resonate with audiences, and observing trends in thematic content over time, we aim to uncover patterns that contribute to or detract from movie success.

<!-- ## Research Questions

1. [Metrics ] What metrics (e.g., low ratings, limited number of ratings, revenue vs budget) best indicate movie failure?
2. [Actor   ] How do actor demographics and lack of diversity impact audience disengagement and contribute to box office underperformance?
3. [Director] What role do director-actor collaborations play in a movie's failure, and are there specific patterns in these partnerships that correlate with unsuccessful films?
4. [Director] Is thematic consistency in director filmographies a predictor of failure/success?
5. [Genre   ] How does genre choice influence a movie's failure, particularly in different cultural contexts?
6. [Timing  ] How does poor release timing (e.g., season, holiday periods) affect a movie's likelihood of failing?
7. [Tropes  ] Which trope combinations consistently lead to negative reception by genre?
8. [Tropes  ] What recurring plot patterns appear most frequently in critically panned films?
-->

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

## Methods

### 1. Data Preprocessing

To create our main dataset that addresses our research questions, we inspected the CMU Movie Corpus Dataset and identified gaps in the data, such as revenue information for only 8,401 movies and missing budget data. To fill these gaps, we merged the TMDB dataset, which provides more complete information on revenue and other field. We used the movie title and release year as common identifiers for merging the datasets, as the release date format varied (yy-mm-dd, yy-mm, or yy). The resulting merged dataset contains 49,516 movies with 27 columns, including vote average, vote count, runtime, budget, IMDb id, and more.

The IMDb id field is important because it serves as a unique identifier for a movie, enabling us to merge them with the Tropes dataset. Since each movie can be associated with multiple tropes, the resulting merged dataframe contains more than 200k rows.

Finally, we generated a file linking directors and actors to each movie that takes into account the IMDb and CMU datasets to facilitate our cast and crew analysis.

To reproduce the preprocessed files that contain the information previously described, navigate to `src/scripts` and run the following script:

```
python preprocess_data.py
```

### 2. Exploratory Data Analysis



### 3. Potiential methods to handle research questions



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
