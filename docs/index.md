---
layout: page
title: "🎬 Box Office Bombs 💣: A Data Detective Story"
subtitle: "Unraveling the 🧬 DNA of Failed Films"
cover-img: /assets/img/cover.jpeg
---

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

.emoji-large {
  font-size: 4rem; /* Makes emojis larger */
  line-height: 1.2;
  margin-bottom: 1rem;
}

.gif {
  width: 40%;
  margin-top: 20px;
  margin-bottom: 10px;
}

</style>

<div class="mt-5"></div>
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

## Behind the Investigation 🕵️

This project is part of the Applied Data Analysis course at EPFL. We've analyzed:
- 42,000+ movie plots from Wikipedia
- Cast and crew data from IMDb
- 30,000+ narrative tropes
- Box office numbers that would make studio executives cry


## Key Evidence 🔍

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

<div class="text-center">
    <img src="https://media4.giphy.com/media/NS7gPxeumewkWDOIxi/giphy.gif?cid=6c09b952mg94u2g7aq1pcnj1sxdidnzdsm6as1z4c55nx3bs&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="Detective Gif" class="gif">
    <figcaption class="mt-2 text-muted">Your caption text here</figcaption>
</div>

### Part I: The Evidence of Failure: Metric

Let us start our investigation with three primary suspects: Average Vote, Revenue, and ROI (Return on Investment). The scatterplot matrix serves as our evidence board, showing how these three metrics interact.

<div class="container" style="margin-right: 100px;">
  {% include plotly/rq1_metrics_distribution.html %}
</div>

The diagonal histograms give us their basic profiles. Average Vote is fairly stable, with most ratings clustering between 6 and 7, and two peaks around 6.3 and 7.3. Revenue is more erratic—most films make under $50 million, but a small number break well beyond $150 million. ROI, like revenue, is also skewed; most films’ returns are modest, clustering below 2.

Comparing these metrics pairwise provides further clues. Movies with lower ratings tend to have worse returns, though this link is not strong. For instance, films rated below 5 commonly have a negative ROI. A similar mild trend appears between revenue and ROI. Some low-revenue movies tend to generate low profits.

In short, lower ratings may lead films toward worse revenue and ROI, but they don’t solve the mystery on their own. These metrics serve as useful signals rather than direct culprits. They hint at trouble, but they don’t tell us who’s really pulling the strings behind a movie’s downfall. To crack the case, we’ll need to dig deeper into the forces at play behind the scenes. Follow me as we investigate the true causes lurking beneath these surface indicators.

### Part II: The Cast Check: Actor Diversity
Our next step is to examine the makeup of the cast—could diversity be a factor in a film’s downfall? To test this, let us measure diversity across four dimensions: age, gender, height, and ethnicity. Age and height diversity are reflected in their standard deviations (higher means more varied), while gender and ethnicity diversity are measured by Shannon’s entropy (higher means more balanced representation).

<div class="row">
    <div class="col-sm-12 col-md-6">
      {% include plotly/rq2_revenue_boxplot.html %}
    </div>
    <div class="col-sm-12 col-md-6">
      {% include plotly/rq2_rating_boxplot.html %}
    </div>
</div>

The boxplots group movies into “Low,” “Medium,” “High,” and “Very High” levels of diversity and show their distributions in terms of revenue and ratings. For revenue, we notice that movies with “Very High” age and ethnicity diversity often have lower median earnings (under $0.5 million) and show greater variability than other groups. One possible explanation is that extremely diverse age ranges or ethnic mixes might lack a focused target audience. For instance, a young cast may be more appealing to children than a highly diverse cast. On the other hand, “Low” gender diversity corresponds to lower median ratings, suggesting that when a cast leans heavily toward one gender, it may not resonate well with a broad audience.

However, when we look at the overall correlations, their strength is minimal. None of these diversity factors show more than a small (absolute value around 0.2) connection to revenue or ratings. Height diversity, for example, seems to have no clear impact at all. 

<div class="container">
    <div class="row justify-content-center">
        <div class="col-auto">
            {% include plotly/rq2_correlation_heatmap.html %}
        </div>
    </div>
</div>

The radar plots compare diversity factors between high-performing and low-performing movies. Each axis ranges from 0 to 1, showing the levels of diversity for each group. The filled areas of each group illustrate the relative contributions of each diversity factor.

<div class="row">
    <div class="col-sm-12 col-md-6">
        {% include plotly/rq2_revenue_radar_chart.html %}
    </div>
    <div class="col-sm-12 col-md-6">
        {% include plotly/rq2_rating_radar_chart.html %}
    </div>
</div>

Radar plots further confirm that while “Very High” ethnicity and age diversity or “Low” gender diversity might push metrics down slightly, the effect is small. 

In short, while casting diversity might influence a film’s performance in subtle ways, it doesn’t emerge as the main suspect for movie failures. Other factors—like acting skills or marketing strategies—may carry more weight in determining a film’s success or downfall. The investigation continues as we delve deeper into the true causes behind box-office bombs.

### Part III: The Director's Enigma

<div class="text-center">
    <img src="https://media2.giphy.com/media/eQabXVbbLW63K/200.gif?cid=6c09b952h6xy4fkwj27ehe3n3g9bm294agh7j44b1s6pdrp0&ep=v1_gifs_search&rid=200.gif&ct=g" alt="Director Gif" class="gif">
    <figcaption class="mt-2 text-muted">Your caption text here</figcaption>
</div>

Next, we turn our attention to directors. Is thematic consistency or variety in their filmography related to poor performance?

<div class="plotly-visualization">
  {% include plotly/rq3_genres_to_ratings.html %}
</div>

The Sankey diagram compares the number of genres directors work with to their films’ ratings and average revenue. Directors who stick to just one genre generally cluster in lower rating categories, 5.5–6.0. This suggests that overly rigid thematic focus may limit a film’s appeal. In contrast, directors who explore a moderate range of genres—around 6 to 13—tend to produce films with higher ratings (above 6.4). 

Revenue patterns follow a similar trend. Directors who either confine themselves to very few genres (e.g., 1) or attempt too many (e.g. 18) show lower average revenues (lower than $30 million). Those who maintain a middle ground, exploring a moderate but not overwhelming range of genres, tend to see better financial returns. 

In summary, a director’s thematic range raises a red flag. Sticking too closely to one type of film or scattering focus across too many can contribute to lower ratings and revenue. It may be because sticking to one genre feels predictable, while too many genres dilute focus, reducing appeal.

With the director’s patterns under our magnifying glass, we turn to other potential clues in our investigation. How does genre choice influence a movie's failure? And will release timing affect a movie's likelihood of failing? Let’s continue!

<div class="section-divider"></div>

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

<div class="row">
    <div class="col-sm-12 col-md-8">
        {% include plotly/rq4_5_roi_analysis.html %}
    </div>
    <div class="col-sm-12 col-md-4">
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. m Ipsum is
    </div>
</div>

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,

<div class="row">
    <div class="col-sm-12 col-md-4">
        Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s
    </div>
    <div class="col-sm-12 col-md-8">
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

<div class="section-divider"></div>

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

### Part V: The Temporal Dimension

#### Seasonal Patterns in Movie Failures: When Timing Meets Trouble 📊

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

#### Monthly Deep Dive: The Anatomy of Movie Failures 📈

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

#### Historical Failure Patterns: A Century of Cinema Risk 📽️

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

<div class="container">
    <div class="row justify-content-center">
        <div class="col-auto">
    {% include plotly/rq5_4_seasonal_success_patterns.html %}
        </div>
    </div>
</div>

*Interactive visualization showing the relationship between budget and ROI*

<div class="section-divider"></div>

### Part VI: The Tropes of Trouble

#### The Tropes of Failure: When Narrative Patterns Predict Disaster 📜

Some tropes are box office poison - let's decode the narrative DNA of failure:

<div class="plotly-visualization">
  {% include plotly/rq6_tropes.html %}
</div>

<div class="plotly-visualization">
  {% include plotly/rq7_tropes_boxplot.html %}
</div>

### 🎭 **The "Unhappy Ending" Curse**: Consistently low ratings across years

Different tropes have been used in movies over the years, and some have consistently led to negative reception by audiences. Analyzing the frequency of these tropes across genres reveals interesting patterns. For example, the "Unhappy Ending" trope is prevalent in Drama and Romance films, while the "Love Triangle" trope is common in Romance and Comedy genres. By examining the distribution of these tropes across genres, we can identify which narrative elements are associated with negative audience reactions and box office failures.

Analyzing the average score of low-rated tropes across different periods reveals interesting trends. While some tropes have consistently low ratings over time, others show significant variation. For example, the "Unhappy Ending" trope has maintained a low average score of around 5.5 since the 1920s, indicating a consistent negative reception from audiences. In contrast, the "Love Triangle" trope experienced a notable decline in average rating from the 1920s to the 1980s, followed by a slight recovery in the 1990s and 2000s. This suggests changing audience preferences and storytelling trends over the decades.

<div class="plotly-visualization">
  {% include plotly/rq8_tropes_avg_scores.html %}
</div>

### Combinations of tropes that lead to failure

<div class="text-center">
    <img src="https://media0.giphy.com/media/l2JdYkTPVG9gRbvhK/giphy.gif?cid=6c09b952uf8lcok55y8ans5raxds0t2l0erufs0nsao0mpcf&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="Detective Gif" class="gif">
    <figcaption class="mt-2 text-muted">Your caption text here</figcaption>
</div>


- Add cluster
- Add network

<div class="section-divider"></div>

## Conclusion 🎬


<div class="section-divider"></div>
<section class="container py-5">
    <h2 class="text-center mb-5 fw-bold">About Our Detective Team</h2>
    <div class="row text-center g-4">
        <div class="col">
            <div class="p-3 h-100 border-0 shadow-sm rounded">
                <div class="emoji-large">🕵️‍♂️</div>
                <h5 class="fw-bold mb-2">Jianan Xu</h5>
                <p class="text-muted fst-italic">"Logic never fails"</p>
            </div>
        </div>
        <div class="col">
            <div class="p-3 h-100 border-0 shadow-sm rounded">
                <div class="emoji-large">🕵️‍♂️</div>
                <h5 class="fw-bold mb-2">Rizhong Li</h5>
                <p class="text-muted fst-italic">"Truth hides in plain sight"</p>
            </div>
        </div>
        <div class="col">
            <div class="p-3 h-100 border-0 shadow-sm rounded">
                <div class="emoji-large">🕵️‍♂️</div>
                <h5 class="fw-bold mb-2">Angel Zenteno</h5>
                <p class="text-muted fst-italic">"Every case tells a story"</p>
            </div>
        </div>
        <div class="col">
            <div class="p-3 h-100 border-0 shadow-sm rounded">
                <div class="emoji-large">🕵️‍♀️</div>
                <h5 class="fw-bold mb-2">Adriana Orellana</h5>
                <p class="text-muted fst-italic">"Details make perfection"</p>
            </div>
        </div>
        <div class="col">
            <div class="p-3 h-100 border-0 shadow-sm rounded">
                <div class="emoji-large">🕵️‍♂️</div>
                <h5 class="fw-bold mb-2">Raph Wegmann</h5>
                <p class="text-muted fst-italic">"Mystery loves company"</p>
            </div>
        </div>
    </div>
</section>

<div class="section-divider"></div>

## Want to Know More? 

Check out our [detailed analysis](/analysis) or dive into our [methodology](/methods).
