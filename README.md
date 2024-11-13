# Decoding Box-Office Bombs

## Abstract

In this project, we aim to explore the underlying reasons for a movie's failure by examining several key factors, including ratings, number of reviews, revenue, and the influence of demographics. We will investigate how actor diversity, director-actor collaborations, and narrative structures affect a movie's performance across different countries and languages. In particular, we analyze the role of character tropes and thematic content, assessing their impact on both critical acclaim and box office success. By exploring how combinations of common tropes resonate with audiences, and observing trends in thematic content over time, we aim to uncover patterns that contribute to or detract from movie success.

## Research Questions

1. What metrics (e.g., low ratings, limited number of ratings, revenue vs budget) best indicate movie failure?
2. How do actor demographics and lack of diversity impact audience disengagement and contribute to box office underperformance?
3. What role do director-actor collaborations play in a movie's failure, and are there specific patterns in these partnerships that correlate with unsuccessful films?
4. Is thematic consistency in director filmographies a predictor of failure/success?
5. How do overused or poorly executed character tropes contribute to a movie's box office failure?
6. How does genre choice influence a movie's failure, particularly in different cultural contexts?
7. How does poor release timing (e.g., season, holiday periods) affect a movie's likelihood of failing?
8. How has the thematic content of movie plots evolved, and what themes have historically failed to resonate with audiences?
9. How does portraying controversial social issues or outdated themes affect a movie's acceptance and potential failure across demographics?

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

## Methods

Team meeting via Zoom at 6:30 PM on Wednesday, 13/11/2024.

## Proposed Timeline

| Deliverable              | Expected Date  |
| ------------------------ | -------------- |
| Data analysis (everyone) | 12/11/2024     |
| Data preprocessing (JX)  | 12/11/2024     |
| Gantt Chart (RW)         | 12/11/2024     |
| Setup Web                | Next milestone |
| Group visualizations     | Next milestone |
| Storytelling             | Next milestone |

## Organization within the team

?? A list of internal milestones up until project Milestone P3. ??

- JX: Questions 2, 7
- RL: Questions 8, 1
- RW: Questions 3, 6, (4)
- AZ: Questions 1, 5
- AO: Questions 1, 9

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
