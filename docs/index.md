---
layout: page
title: "🎬 Box Office Bombs 💣: A Data Detective Story"
subtitle: "Unraveling the 🧬 DNA of Failed Films"
cover-img: /assets/img/cover.jpeg
---

# Welcome to the Movie Morgue 🔍

Ever wondered why some movies crash and burn at the box office? We're not just talking about obvious flops - we're diving deep into the DNA of over 42,000 films to conduct a proper cinematic autopsy. 

## The Case File 📁

Our investigation covers everything from ill-fated release dates to questionable casting choices. Using state-of-the-art data analysis, we're examining:

- 💰 **The Money Trail**: How much cash went up in smoke?
- 🎭 **The Usual Suspects**: Are certain actors and directors repeat offenders?
- 📅 **The Timeline**: Does releasing your vampire romance during Christmas spell doom?
- 📖 **The Plot Thickens**: Which story tropes should come with a warning label?

## Key Evidence 🔍

<div class="plotly-visualization">
  {% include plotly/rq2_actor_diversity.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq4_1_genre_profit_distribution.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq4_2_genre_rating_distribution.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq4_3_genre_performance_popularity.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq4_4_genre_performance_profit.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq4_5_roi_analysis.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq4_6_budget_analysis.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq4_7_success_rates.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq4_8_failure_rates.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq4_9_success_matrix.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq5_1_seasonal_analysis.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq5_2_monthly_analysis.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq5_4_seasonal_success_patterns.html %}
</div>

*Interactive visualization showing the relationship between budget and ROI*

[PLOTLY-VISUALIZATION-1]
*Metrics*
<div class="plotly-visualization">
  {% include plotly/rq1_metrics_distribution.html %}
</div>

We begin our exploration of the metrics associated with movie failures by analyzing three key indicators: average vote, revenue, and ROI (Return on Investment). The first step is to uncover patterns and relationships between these metrics to better understand the causes of poor movie performance. 

The scatterplot mattrix provides an overview of the relationships between three metrics. Along the diagonal, histograms display the distributions of each metric. Movie ratings are approximately normally distributed, with most falling between 6 and 7, peaking near 6.5. Revenue, however, is heavily skewed to the right, with the majority of movies earning less than $50 million, though a few outliers exceed $150 million. ROI follows a similar trend, with most values concentrated below 2, indicating that a majority of films generate modest returns relative to their costs.

The off-diagonal scatter plots reveal the pairwise correlations between these metrics, supplemented by trendlines to illustrate general patterns. Movies with higher ratings tend to earn more revenue, as shown by a slight positive correlation, though the relationship is not particularly strong. For example, a cluster of films rated between 6 and 7 generates revenues in the $20–50 million range. Similarly, there is a moderate positive correlation between ratings and ROI, suggesting that higher-rated movies are more likely to achieve better financial returns. Films with a vote_average near 7 often exhibit an ROI between 1 and 2. Interestingly, the relationship between revenue and ROI is weak but positive, indicating that high-grossing films are not necessarily the most profitable. Many movies with revenues above $100 million have ROIs under 2, reflecting high production and marketing costs.

Overall, the plot underscores that while better ratings slightly correlate with higher revenue and ROI, these relationships are nuanced, with significant variability and a concentration of movies in lower revenue and ROI ranges.

### The Diversity Deficit
Our analysis reveals some surprising patterns in casting choices and box office performance.

[PLOTLY-VISUALIZATION-2]
*Interactive visualization of cast diversity metrics vs. movie failure*

### The Director's Curse
Some directors seem to have a knack for picking problematic projects...

[PLOTLY-VISUALIZATION-3]
*Interactive visualization of director track records*

### Genre Graveyards
Certain genres are more likely to fail in specific seasons...

[PLOTLY-VISUALIZATION-4]
*Interactive visualization of genre performance by release timing*

## Behind the Investigation 🕵️

This project is part of the Applied Data Analysis course at EPFL. We've analyzed:
- 42,000+ movie plots from Wikipedia
- Cast and crew data from IMDb
- 30,000+ narrative tropes
- Box office numbers that would make studio executives cry

[PLOTLY-VISUALIZATION-5]
*Interactive visualization of trope combinations and their impact on ratings*

Questions:
### 6. Which tropes consistently lead to negative reception by genre?

### 7. What plots are the most common in movies that fail?

<div class="plotly-visualization">
  {% include plotly/rq7_tropes_boxplot.html %}
</div>

### 8. How have low-rated tropes evolved over time, and what trends can be observed in their average ratings across different periods?

<div class="plotly-visualization">
  {% include plotly/rq8_tropes_counts.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq8_tropes_avg_scores.html %}
</div>

## Want to Know More? 

Check out our [detailed analysis](/analysis) or dive into our [methodology](/methods).

---

*This is an ongoing investigation. Last updated: November 2024*