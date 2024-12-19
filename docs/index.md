---
layout: page
title: "🎬 Box Office Bombs 💣: A Data Detective Story"
subtitle: "Unraveling the 🧬 DNA of Failed Films"
cover-img: /assets/img/cover.jpeg
---

# Welcome to the Movie Morgue 🔍

Ever wondered why some movies crash and burn at the box office? Like how 'John Carter' lost Disney $200 million, or how 'Cats' became the stuff of Hollywood nightmares? We're not just talking about obvious flops - we're conducting a forensic analysis of over 42,000 films to uncover the hidden patterns behind cinematic disasters.

## The Case File 📁

Our investigation digs deep, from forgotten B-movies to high-budget catastrophes. Using state-of-the-art data analysis and visualization techniques, we're cracking open the vault on:

- 💰 **The Money Trail**: Following the financial failures - from modest mishaps to billion-dollar blunders
- 🎭 **The Cast Chronicles**: Identifying patterns in star power and ensemble dynamics
- 📅 **The Timing Trap**: Uncovering how release dates can make or break a film's success
- 📖 **The Plot Patterns**: Discovering which story elements are red flags for disaster

Join us as we piece together the clues and uncover the formula for box office failure. Whether you're a film buff, data enthusiast, or just curious about Hollywood's biggest misses, this investigation will change how you see the movie industry.

Let the autopsy begin... 🎬

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

### Genre Face-Off: Ratings vs. Revenue 🎭

Let's decode what our data reveals about the tricky balance between critical success and box office triumph:

- 🎯 **The High Rollers**: Adventure and Animation top the profit charts, but watch out - those massive error bars show you could hit the jackpot or lose big. It's Hollywood's version of high-stakes poker.

- 🏆 **Critical Darlings**: Animation and Family films consistently score high ratings (6.0+/10), proving quality can sell. But there's a twist - some critically acclaimed genres barely break even.

- 💸 **The Underdogs**: Documentaries and Westerns earn critics' respect but struggle at the box office. Meanwhile, Action films keep cashing in despite average ratings.

Moral of the story? In Hollywood's game of chance, critical acclaim doesn't always translate to commercial success. The safest bet might be targeting that sweet spot where art meets entertainment.

*Tip: Notice how the gray zones (5th-95th percentiles) tell the real story of risk in each genre...*

<div class="plotly-visualization">
  {% include plotly/rq4_1_genre_profit_distribution.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq4_2_genre_rating_distribution.html %}
</div>

### The Popularity Puzzle: A Beautiful Mess 📊

These scatterplots might look like a Jackson Pollock painting at first glance, but there's method in the madness:

- 🎨 **Genre Rainbow**: The first plot is deliberately chaotic - every genre competing for space, creating a dazzling but messy spectrum. It's Hollywood in its true form: a beautiful chaos where Drama mingles with Horror, and Romance crosses paths with Sci-Fi.

- 📈 **The Convergence**: Despite the genre chaos, a clear pattern emerges - as votes increase (moving right), ratings tend to stabilize. It's like watching a messy party eventually find its rhythm.

- 💰 **Follow the Money**: The second plot strips away the genre confusion, using color for profit instead. Now we see a cleaner story - successful movies (darker dots) clustering in the popular, well-rated zone, while financial flops scatter across the board.

*Tip: Sometimes the messiest data tells the most honest story about how complex the movie industry really is.*

<div class="plotly-visualization">
  {% include plotly/rq4_3_genre_performance_popularity.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq4_4_genre_performance_profit.html %}
</div>

### The ROI Riddle: Where Movies Go to Lose Money 💸

The return-on-investment story reveals some surprising truths about Hollywood's failures:

- 📉 **The Budget Trap**: Look at those "Very High" budget films - their ROI is dismally low (barely 1x) despite massive profits. The old saying "you have to spend money to lose money" seems eerily true here.

- 🎯 **Sweet Spot or Danger Zone?**: The wild variance in Documentary ROI (900%!) suggests a fascinating pattern - when they fail, they fail small, but when they hit, they hit big. It's the opposite of blockbuster economics.

- ⚠️ **Warning Signs**:
  - Higher budgets consistently show lower ROI spreads
  - Horror and Documentary films maintain better ROI despite smaller budgets
  - Genre failures are more devastating in high-budget categories

*Bottom line: In Hollywood, the biggest failures often come wrapped in the biggest budgets. Sometimes, spending less means risking less.*

<div class="plotly-visualization">
  {% include plotly/rq4_5_roi_analysis.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq4_6_budget_analysis.html %}
</div>

### The Success-Failure Paradox: When Genres Betray Their Promise 🎭

These charts reveal some fascinating contradictions about genre performance:

- 🎢 **High Risk, High Reward**: Adventure and Sci-Fi top the success rate chart (~13%), but look closer - they also carry significant failure rates (3-4%). It's Hollywood's version of "go big or go home."

- 🔍 **The Thriller Paradox**: Most intriguing case study here - Thrillers show strong success potential (11%) but lead the failure rate chart (4.5%). They're essentially Hollywood's most volatile investment.

- 🎯 **The Safe Havens**: 
  - Animation/TV Movies have low failure rates (<1%)
  - Documentaries rarely fail catastrophically
  - But here's the catch - their success rates are also among the lowest

*The real story? The genres most likely to succeed are often the ones most likely to fail spectacularly. Playing it safe might mean avoiding disaster, but it also means limiting potential breakout success.*

<div class="plotly-visualization">
  {% include plotly/rq4_7_success_rates.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq4_8_failure_rates.html %}
</div>

### The Heat Map of Hollywood Heartbreak 🎯

This heat map tells the brutal truth about movie performance across genres:

- 🔥 **The Purple Valley**: That dark purple sea on the left? It's the graveyard of movie investments, showing how rare catastrophic failures are across all genres. But they do happen, and when they do...

- 🌟 **The Golden Zone**: Notice those bright yellow spots for Adventure, Fantasy, and Sci-Fi around the "Break Even" mark? That's where the magic happens - but it's a narrow band of success.

- 💀 **Dead Zones**:
  - TV Movies and Documentaries show consistently dark colors across all metrics
  - Thrillers show stronger colors in both extremes - supporting our earlier "volatile investment" theory
  - Westerns barely register on the success metrics - explaining their near-extinction

*In Hollywood's landscape, mediocrity is the norm (purple), breakthrough success is rare (yellow), and total failure is uncommon but devastating when it happens.*

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