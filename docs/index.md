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

<style>
.viz-container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    margin: 20px 0;
}

@media (max-width: 768px) {
    .viz-container {
        grid-template-columns: 1fr;
    }
}

.section-divider {
    margin: 40px 0;
    border-top: 2px solid #eee;
    text-align: center;
}

.full-width {
    grid-column: 1 / -1;
    width: 100%;
    margin: 20px 0;
}
</style>

### Part IV: The Genre Gamble

#### Genre Face-Off: The Anatomy of Box Office Disasters 🎭

Let's decode what our data reveals about where and why movies fail financially:

- 🎯 **The High-Risk Zones**: Adventure and Animation show the widest loss margins in their failure cases - when these big-budget genres fail, they fail spectacularly. Those massive error bars aren't just statistics; they're financial bloodbaths.

- 🏆 **The Critics' Curse**: High ratings offer no safety net. Animation and Family films maintain strong ratings (6.0+/10) but can still bomb catastrophically. Some of the biggest financial disasters came with critical acclaim attached.

- 💸 **The Genre Trap**: Documentaries and Westerns face chronic failure patterns - consistent critical respect but systematic financial underperformance. Meanwhile, Action films demonstrate how mediocre ratings don't necessarily predict financial failure.

*Key Failure Pattern: Critical acclaim and financial disaster aren't mutually exclusive - some genres are structurally prone to failure regardless of quality.*

<div class="viz-container">
    <div class="plotly-visualization">
        {% include plotly/rq4_1_genre_profit_distribution.html %}
    </div>
    <div class="plotly-visualization">
        {% include plotly/rq4_2_genre_rating_distribution.html %}
    </div>
</div>

#### The ROI Riddle: Where Movies Go to Lose Money 💸

The return-on-investment patterns reveal Hollywood's hidden risk landscape:

- 📉 **The Budget Paradox**: "Very High" budget films show dismally low ROI (barely 1x) despite massive profits. More money, more problems?

- 🎯 **The Documentary Gambit**: 900% ROI variance tells a fascinating story - minimal losses, occasional massive wins. It's anti-blockbuster economics in action.

- ⚠️ **Risk Indicators**:
  - Higher budgets = tighter ROI spreads
  - Horror/Documentary maintain better ROI despite smaller budgets
  - High-budget failures hit hardest

*Key Pattern: The biggest financial disasters often come wrapped in the biggest budgets.*

<div class="viz-container">
    <div class="plotly-visualization">
        {% include plotly/rq4_5_roi_analysis.html %}
    </div>
    <div class="plotly-visualization">
        {% include plotly/rq4_6_budget_analysis.html %}
    </div>
</div>

#### The Success-Failure Paradox: When Genres Betray Their Promise 🎭

Our data reveals some fascinating contradictions in genre performance:

- 🎢 **The Volatility Champions**: Adventure and Sci-Fi lead with ~13% success rates but carry 3-4% failure rates. Welcome to Hollywood's "go big or go home" genres.

- 🔍 **The Thriller Enigma**: Leading 11% success potential paired with 4.5% failure rate makes Thrillers Hollywood's most volatile investment.

- 🎯 **The Conservative Players**: 
  - Animation/TV Movies: Low failure rates (<1%)
  - Documentaries: Rare catastrophic failures
  - The catch? Limited breakout potential

*The Pattern: Genre success often comes packaged with proportional risk of spectacular failure.*

<div class="viz-container">
    <div class="plotly-visualization">
        {% include plotly/rq4_7_success_rates.html %}
    </div>
    <div class="plotly-visualization">
        {% include plotly/rq4_8_failure_rates.html %}
    </div>
</div>

<div class="section-divider">
    ⭐️
</div>

<!-- ## Part II: The Deeper Patterns -->

#### The Heat Map of Hollywood Heartbreak 🎯

Let's decode the performance matrix that reveals the true anatomy of success and failure:

- 🔥 **The Purple Valley**: That dominant purple zone isn't just a color - it's the baseline of Hollywood performance, showing how most movies cluster around modest outcomes.

- 🌟 **Success Hotspots**: The bright yellow patches in Adventure, Fantasy, and Sci-Fi reveal the narrow band where blockbusters live. Like finding gold, it's rare but valuable.

- 💀 **Genre Graveyards**:
  - TV Movies/Documentaries: Consistently dark colors show limited upside
  - Thrillers: Color extremes confirm their high-risk profile
  - Westerns: Fading colors tell the story of a genre in decline

*Pattern Recognition: Success in Hollywood follows a power law - mediocrity is common, excellence is rare, and total failure leaves lasting scars.*

<div class="plotly-visualization full-width">
    {% include plotly/rq4_9_success_matrix.html %}
</div>

#### The Popularity Puzzle: A Beautiful Mess 📊

Now that we understand the basic patterns, let's explore how audience reception shapes success:

- 🎨 **The Genre Spectrum**: Our first scatter plot looks chaotic because it is - it's the true face of Hollywood's constant genre experimentation.

- 📈 **The Convergence Effect**: Watch how ratings stabilize as vote counts increase. It's like watching audience opinions find their true north.

- 💰 **The Money Trail**: When we switch to profit coloring, the chaos resolves into clear patterns - successful movies cluster in the high-rating, high-popularity zone.

*Key Insight: Popularity and quality aren't just metrics - they're the twin engines of sustainable success.*

<div class="viz-container">
    <div class="plotly-visualization">
        {% include plotly/rq4_3_genre_performance_popularity.html %}
    </div>
    <div class="plotly-visualization">
        {% include plotly/rq4_4_genre_performance_profit.html %}
    </div>
</div>

<div class="section-divider">
    🎬
</div>

## Part IV: The Temporal Dimension

### Seasonal Patterns in Movie Failures: When Timing Meets Trouble 📊

Beyond genre and popularity, timing proves crucial in the success equation:

- 🌨️ **The Winter Challenge**: 
  - $0-9M mean profit range reveals seasonal struggles
  - High ROI volatility suggests increased risk
  - Critical acclaim doesn't guarantee winter warmth

- 🌸 **Spring's Double Edge**:
  - Peak average profits come with significant variance
  - Perfect example of high risk/high reward dynamics

- 🌞 **Summer Complexities**:
  - Traditional "blockbuster season" shows surprising vulnerability
  - ROI swings from -5 to +10 tell a story of extremes
  - Higher production costs create pressure

*The Calendar Effect: Each season brings its unique risk profile.*

<div class="plotly-visualization full-width">
    {% include plotly/rq5_1_seasonal_analysis.html %}
</div>

### Monthly Deep Dive: The Anatomy of Movie Failures 📈

Let's zoom in to see exactly when movies are most vulnerable:

- 🥶 **January's Risk Trifecta**:
  - 2.3% high success rate (lowest)
  - 0.8% severe loss rate (highest)
  - Consistently poor ROI metrics
  - Hollywood's notorious "dump month"

- 🌞 **The Summer Paradox**:
  - June-July: 8-8.2% peak success rates
  - Accompanied by 0.8-1% severe loss rates
  - Maximum profit variance

*Monthly Insight: Success and failure peaks often align, creating seasonal risk hotspots.*

<div class="plotly-visualization full-width">
    {% include plotly/rq5_2_monthly_analysis.html %}
</div>

### Historical Failure Patterns: A Century of Cinema Risk 📽️

Our final visualization shows how these patterns evolved over 100+ years:

- 🌅 **1880s-1910s: The Pioneer's Curse**:
  - Near-zero success rates
  - High-risk experimental period
  - Industry fundamentals still forming

- 📈 **1920s-1960s: The Learning Years**:
  - Steady success rate improvement
  - Winter remained the challenging season
  - Fall emergence as a viable release window

- 💡 **1970s-2010s: The Modern Era**:
  - Volume and success rates reached new heights
  - Spring 1970s breakthrough (7.2% success)
  - Winter finally caught up (10.1% in 2010s)

*Historical Perspective: While success rates have improved, fundamental seasonal patterns persist.*

<div class="plotly-visualization full-width">
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