---
layout: page
title: "💣🎬 Box Office Bombs: A Data Detective Story"
subtitle: "Unraveling the DNA of Failed Films"
cover-img: /assets/img/cover.jpg
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
  {% include plotly/rq1_metrics.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq2_actor_diversity.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq3_kmeans_centers.html %}
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

### The Diversity Deficit
Our analysis reveals some surprising patterns in casting choices and box office performance.

[PLOTLY-VISUALIZATION-2]
*Interactive visualization of cast diversity metrics vs. movie success*

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


<div class="plotly-visualization">
  {% include plotly/tropes_boxplot.html %}
</div>

## Want to Know More? 

Check out our [detailed analysis](/analysis) or dive into our [methodology](/methods).

---

*This is an ongoing investigation. Last updated: November 2024*