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

<div class="viz-container">
    <div class="plotly-visualization">
        {% include plotly/rq4_1_genre_profit_distribution.html %}
    </div>
    <div class="plotly-visualization">
        {% include plotly/rq4_2_genre_rating_distribution.html %}
    </div>
</div>

The first clue in our investigation of Hollywood failures lies in the stark contrast between profit distributions and ratings across genres. Looking at the profit distribution chart, we immediately notice the treacherous terrain of high-stakes genres like Adventure and Animation. These genres display alarmingly wide error bars stretching deep into negative territory - silent witnesses to some of cinema's most spectacular financial disasters. When these movies fail, they don't just disappoint; they create financial sinkholes that can swallow entire studio budgets.

Digging deeper into the ratings distribution, we uncover a puzzling paradox. Animation and Family films consistently achieve critical acclaim, clustering above the 6.0 rating mark. Yet this critical success offers no immunity against financial failure. The evidence suggests that some of the industry's most painful losses came wrapped in glowing reviews - a reminder that audience appreciation doesn't always translate into box office success. This disconnect between critical reception and financial performance reveals a fundamental flaw in the assumption that good movies naturally find their audience.

Perhaps most telling is the fate of genres like Documentaries and Westerns. Despite maintaining respectable average ratings, these genres show a systematic pattern of financial underperformance. Their profit distributions tell a story of chronic struggle, rarely breaking into significant positive territory. Meanwhile, Action films present an interesting counter-narrative - their middling ratings don't prevent them from achieving financial stability. This pattern suggests that certain genres are structurally disadvantaged in the modern marketplace, regardless of their artistic merit. The data points to an uncomfortable truth: in Hollywood's high-stakes game, quality and commercial success often operate in entirely separate dimensions.

_Case File Note: Our investigation reveals that no genre is truly safe from failure - even those with the strongest critical foundations can crumble at the box office._

#### The ROI Riddle: Where Movies Go to Lose Money 💸

<div class="row">
    <div class="col-sm-12 col-md-8">
        {% include plotly/rq4_5_roi_analysis.html %}
    </div>
    <div class="col-sm-12 col-md-4">
        A closer examination of the ROI distribution chart reveals a troubling pattern across genres. Documentaries stand out with their extreme variance, showing ROI swings from -216% to a staggering 9900%. This volatility tells a story of a genre where financial outcomes are wildly unpredictable. Horror films follow a similar pattern, with their error bars stretching far into both positive and negative territories, suggesting an industry segment where financial planning becomes more art than science.
    </div>
</div>

<div class="row">
    <div class="col-sm-12 col-md-4">
        The relationship between budget categories and financial outcomes presents perhaps the most counterintuitive finding in our investigation. While Very High budget films command the largest absolute profits, their ROI tells a drastically different story. These blockbusters barely achieve a 1x return on investment, with their error bars suggesting frequent dips into negative territory. The data paints a picture of an inverse relationship: as budgets climb, ROI potential consistently diminishes, creating a tension between absolute returns and investment efficiency.
    </div>
    <div class="col-sm-12 col-md-8">
        {% include plotly/rq4_6_budget_analysis.html %}
    </div>
</div>

Looking at both plots together reveals the full scope of Hollywood's risk paradox. Very Low budget productions show the highest ROI potential (reaching over 10x returns) but minimal absolute profits, while Very High budget films display the opposite pattern - substantial absolute profits but anemic ROI figures. This creates a cruel dilemma for studios: chase higher absolute profits at the cost of efficiency, or maintain better ROI while accepting limited profit potential. The data suggests that the safest path - balancing ROI and absolute profits - lies somewhere in the middle budget categories, though even these show significant potential for failure.

_Case File Note: The evidence points to a fundamental inefficiency in Hollywood's business model - the more money invested, the harder it becomes to generate proportional returns, creating a perfect storm for spectacular financial failures._

#### The Success-Failure Paradox: When Genres Betray Their Promise 🎭

<div class="viz-container">
    <div class="plotly-visualization">
        {% include plotly/rq4_7_success_rates.html %}
    </div>
    <div class="plotly-visualization">
        {% include plotly/rq4_8_failure_rates.html %}
    </div>
</div>

<div class="section-divider"></div>

The failure rate chart reveals a disturbing truth about Hollywood's riskiest genres. Thrillers emerge as the industry's most treacherous territory, with a startling 4.5% of productions ending in catastrophic losses (defined as losing over 50% of their investment). This is closely followed by Science Fiction films at 4%, painting a picture of genres where ambition and disaster walk hand in hand. These aren't just statistics - they represent hundreds of millions in lost investments and countless careers derailed.

Looking at the success rate chart might initially seem to offer hope, with Adventure and Science Fiction films showing impressive peaks of around 13% success (defined as achieving over 100% ROI). However, this apparent silver lining reveals a darker truth when viewed alongside the failure rates. The very genres that promise the highest rewards also harbor the highest risks of catastrophic failure. It's a classic case of double-edged sword economics, where the path to potential triumph is littered with financial casualties.

The intersection of these two metrics exposes the full scope of Hollywood's genre-based risk landscape. While genres like Animation and TV Movies show admirably low failure rates (under 1%), they also demonstrate limited success potential, rarely breaking past the 5% success rate threshold. This creates a cruel dynamic where playing it safe leads to stagnation, while pursuing bigger returns inevitably increases exposure to catastrophic failure. The data suggests that in Hollywood's high-stakes game, there are no truly safe harbors - only varying degrees of risk and compromise.

_Case File Note: The evidence points to a fundamental truth in Hollywood - genres that promise the highest returns are often the same ones that harbor the greatest potential for devastating failure. This isn't just coincidence; it's the DNA of the industry's risk structure._

<!-- ## Part II: The Deeper Patterns -->

#### The Heat Map of Hollywood Heartbreak 🎯

<div class="row">
    <div class="col-sm-12 col-md-4">
        The performance heat map before us reads like a crime scene analysis of Hollywood's financial casualties. The dark purple bands stretching across the left side of the visualization tell a sobering story - every genre, without exception, has its share of total losses and severe failures. This isn't just data; it's a graveyard of creative ambitions and financial investments. The deepest purple zones, particularly prominent in TV Movies and Westerns, represent areas where movies go to die, rarely emerging from the red zone of financial loss.
    </div>
    <div class="col-sm-12 col-md-8">
        {% include plotly/rq4_9_success_matrix.html %}
    </div>
</div>

#### The Heat Map of Hollywood Heartbreak 🎯

Moving towards the center, we encounter what might be called "Hollywood's Purgatory" - the break-even zone. Here, the colors begin to warm slightly, but the predominant purple tones reveal an uncomfortable truth: most films barely manage to recoup their investments. This vast middle ground isn't merely a neutral zone; it represents thousands of projects that failed to achieve their financial potential, languishing in what industry veterans darkly call "development hell." The transition from deep purple to lighter shades in this region maps the thin line between failure and mere survival.

The right side of the heat map provides the most striking contrast - and perhaps the most painful insight into the industry's brutal economics. Those rare yellow hotspots in Adventure, Fantasy, and Science Fiction genres represent the elusive blockbuster territory, but their very brightness serves to highlight the darkness surrounding them. These aren't just success stories; they're statistical anomalies that tantalize studios into continued risk-taking, even as the surrounding purple zones warn of the far more common outcome - financial disaster. The pattern is particularly cruel in genres like Thrillers, where the extreme color variation from deep purple to bright yellow illustrates the genre's tendency to either soar or crash spectacularly, with little middle ground.

_Case File Note: The heat map reveals Hollywood's darkest secret - in the pursuit of those rare yellow zones of success, the industry has normalized a landscape dominated by failure. The purple vastness isn't just a background; it's the industry's default state._

#### The Popularity Puzzle: A Beautiful Mess 📊

<div class="viz-container">
    <div class="plotly-visualization">
        {% include plotly/rq4_3_genre_performance_popularity.html %}
    </div>
    <div class="plotly-visualization">
        {% include plotly/rq4_4_genre_performance_profit.html %}
    </div>
</div>

The scatter plots before us reveal the brutal democracy of audience reception, where failure leaves its most visible scars. The left plot's apparent chaos isn't random noise - it's a map of creative casualties. In the low-vote regions (below 100 votes), we see the industry's killing fields: films that didn't just fail financially, but failed to even capture enough attention to generate significant audience response. These data points represent countless projects that died in obscurity, their ratings scattered across the spectrum like debris after a storm.

The right plot, coded by profit, exposes an even darker truth. The lighter shades dominating the lower-vote regions tell a story of financial bloodletting - movies that not only failed to find their audience but hemorrhaged money in the process. As we move rightward along the vote count axis, we see how profitability (darker colors) tends to cluster in the upper regions of the rating scale, but the path there is littered with failures. The most painful revelation comes from those rare high-vote, low-rating examples - massive marketing campaigns that drew audiences to critically panned films, resulting in spectacular financial disasters.

What's particularly fascinating is how these plots capture the industry's cruel mathematics. The funnel shape that emerges as vote counts increase isn't just a statistical phenomenon - it's the visualization of audience consensus crushing creative ambitions. While individual opinions may vary wildly for obscure films, increased exposure tends to push ratings toward a harsh middle ground. This convergence effect is especially brutal for genres like Horror and Comedy, where we can see their distinctive patterns dissolve into the general mass as vote counts rise, suggesting that even genre-specific appeal offers little protection against the broader market's judgment.

_Case File Note: These scatter plots aren't just data visualizations - they're obituaries for thousands of creative ventures that failed to thread the needle between artistic merit and commercial viability. The pattern suggests that while quality doesn't guarantee success, its absence almost certainly ensures failure._

<div class="section-divider">
    🎬
</div>

### Part V: The Temporal Dimension

#### Seasonal Patterns in Movie Failures: When Timing Meets Trouble 📊

<div class="plotly-visualization full-width">
    {% include plotly/rq5_1_seasonal_analysis.html %}
</div>

The seasonal performance charts reveal a complex temporal landscape where timing can either salvage a troubled project or doom a promising one. Winter emerges as perhaps the most treacherous season, with mean profits hovering cautiously around the $0-9M mark. But the real story lies in those dramatic error bars stretching from $-9M to $99M - a range that represents countless holiday releases that aimed for Oscar glory but found only financial ruin. The winter months create a particularly cruel paradox: while audiences are most available during the holiday season, they're also most selective with their entertainment choices.

Spring presents itself as a season of extremes, displaying the highest average profits but accompanied by the widest profit variance. This isn't just statistical noise - it's the visualization of an industry-wide gamble. The spring release window has become a high-stakes poker game where studios push their chips all in, hoping to capture audiences emerging from their winter hibernation. The ROI statistics for spring tell an equally volatile story, with those towering error bars representing both spectacular successes and catastrophic failures that often occur within weeks of each other.

Summer, traditionally Hollywood's golden season, reveals a troubling pattern when we examine all four metrics simultaneously. While average profits remain stable, the combination of lower ROI and steadily climbing ratings suggests an industry caught in a spending trap. Studios pour ever-larger budgets into summer blockbusters, chasing audiences with spectacular effects and marketing campaigns, yet the return on these massive investments continues to shrink. The performance metrics chart shows this disconnect most clearly - as ratings climb through the summer, profits fail to keep pace.

Fall emerges as a season of missed opportunities and modest consolations. The relatively stable profit margins and ROI figures might suggest a "safe" release window, but this stability comes at the cost of limited upside potential. What's particularly striking is how the average rating line continues its upward trend through fall, even as profits decline from their spring peaks. This disconnect between critical reception and financial performance paints a picture of a season where good movies go to die quietly - earning critical acclaim but failing to translate that success into box office results.

_Case File Note: The seasonal data exposes how timing has become both weapon and weakness in Hollywood's arsenal. Each season presents its own path to failure, whether through winter's selective audiences, spring's high-stakes gambling, summer's budget bloat, or fall's quiet disappointments._

#### Monthly Deep Dive: The Anatomy of Movie Failures 📈

<div class="plotly-visualization full-width">
    {% include plotly/rq5_2_monthly_analysis.html %}
</div>

The monthly profit statistics reveal a cruel calendar where timing can be as decisive as quality. The notorious "January dump" shows up clearly in our data, with the month posting a devastating combination of the year's lowest high success rate (2.3%) and highest severe loss rate (0.8%). This isn't just a bad month - it's a graveyard shift where studios often abandon their troubled projects, creating a self-fulfilling prophecy of failure. The profit variance bars for January tell an especially grim story, stretching deep into negative territory with rare upward breaks.

Summer's data exposes what might be called the "blockbuster paradox." June and July show impressive high success rates of 8-8.2%, but these peaks come with a dangerous caveat - they're matched by significant severe loss rates around 1%. The monthly ROI trends heat map reveals the full picture: while success rates peak, the deep red zones in the "Severe Loss" column remain stubbornly present. This suggests that summer's higher box office potential comes at the cost of higher risk exposure, creating a high-wire act where the difference between triumph and disaster often comes down to opening weekend performance.

The transitional months tell their own story of industry vulnerability. March and September emerge as particularly treacherous, showing moderate success rates but disproportionately high failure rates (1.2-1.9% severe losses). The monthly success metrics graph reveals how these shoulder seasons create false hope - the success rate line climbing hopefully before plummeting, creating what industry insiders might call "trap months" where studios are lured into releases that seem promising but often end in financial disaster.

December presents perhaps the most fascinating case study in risk versus reward. The month shows an impressive 8.1% high success rate, but the ROI trends reveal a complex underlying reality. The heat map shows significant percentages across all performance categories, from severe losses to high success, suggesting December is less a "good" month than a highly volatile one. This volatility is further confirmed by the widest profit variance bars of any month, stretching from deep losses to spectacular gains. It's a month that perfectly encapsulates Hollywood's gambling nature - where the biggest winners and losers are often decided within the same few weeks.

_Case File Note: The monthly data exposes how Hollywood's calendar isn't just a scheduling tool - it's a risk management battlefield where timing mistakes can doom even promising projects. Each month presents its own unique combination of threats and opportunities, creating a complex temporal maze that studios must navigate to avoid financial disaster._

#### Historical Failure Patterns: A Century of Cinema Risk 📽️

<div class="container">
    <div class="row justify-content-center">
        <div class="col-auto">
    {% include plotly/rq5_4_seasonal_success_patterns.html %}
        </div>
    </div>
</div>

The heat map before us isn't just data - it's a century-long autopsy of Hollywood's learning curve. The deep red zones of the 1880s-1910s reveal an industry essentially operating blind, with success rates hovering near zero across all seasons. This wasn't just failure - it was systematic failure, with hundreds of productions venturing into an untested market with no playbook for success. The sparse number of movies (0-5 per season) tells a story of an industry where survival, not success, was the primary metric.

The middle decades (1920s-1960s) document Hollywood's painful education in risk management. The gradual warming of colors from deep red to lighter shades tracks the industry's growing sophistication, but the persistent winter weakness (staying below 2% success rate until the 1970s) reveals how deeply seasonal vulnerabilities were embedded in the industry's DNA. The fall season's emergence as a viable release window (reaching 4.9% in the 1960s) wasn't just a scheduling shift - it was the industry's first successful attempt to engineer its way around seasonal failure patterns.

The modern era (1970s-2010s) presents a fascinating paradox. While overall success rates reached unprecedented heights (peaking at 12.6% in 2010s spring), the sheer volume of releases (564 fall movies in the 2000s alone) created a new kind of risk landscape. The data suggests that higher success rates came with a cruel twist - more absolute failures than ever before. The brightening blues of the 2010s might look like triumph, but they mask an industry where the sheer scale of production meant that even improved success rates translated to hundreds of failed projects.

What's particularly striking is how the seasonal patterns, while less severe, have never truly disappeared. Even in the 2010s, with all our modern analytics and market research, winter releases still underperform spring by 2.5 percentage points (10.1% vs 12.6%). The persistence of these patterns across decades suggests something fundamental about audience behavior that even a century of industry evolution hasn't been able to fully overcome. The modern era hasn't eliminated failure - it's just made it more expensive and more frequent in absolute terms.

_Case File Note: The historical data reveals that while Hollywood has gotten better at success, it has never truly solved the problem of failure. Instead, it has simply scaled up both success and failure to unprecedented levels, creating a modern industry where the sheer volume of production ensures a steady stream of casualties regardless of improved success rates._

<div class="section-divider"></div>

### Part VI: The Tropes of Trouble

#### The Tropes of Failure: When Narrative Patterns Predict Disaster 📜

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.

<div class="container-fluid">
    <div class="row">
        <div class="col-12">
            {% include plotly/rq6_tropes.html %}
        </div>
    </div>
</div>

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.

<div class="container">
  {% include plotly/rq7_tropes_boxplot.html %}
</div>

### 🎭 **The "Unhappy Ending" Curse**: Consistently low ratings across years

Different tropes have been used in movies over the years, and some have consistently led to negative reception by audiences. Analyzing the frequency of these tropes across genres reveals interesting patterns. For example, the "Unhappy Ending" trope is prevalent in Drama and Romance films, while the "Love Triangle" trope is common in Romance and Comedy genres. By examining the distribution of these tropes across genres, we can identify which narrative elements are associated with negative audience reactions and box office failures.

Analyzing the average score of low-rated tropes across different periods reveals interesting trends. While some tropes have consistently low ratings over time, others show significant variation. For example, the "Unhappy Ending" trope has maintained a low average score of around 5.5 since the 1920s, indicating a consistent negative reception from audiences. In contrast, the "Love Triangle" trope experienced a notable decline in average rating from the 1920s to the 1980s, followed by a slight recovery in the 1990s and 2000s. This suggests changing audience preferences and storytelling trends over the decades.

<div class="container">
  {% include plotly/rq8_tropes_avg_scores.html %}
</div>

### Combinations of tropes that lead to failure

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.

<div class="text-center">
    <img src="https://media0.giphy.com/media/l2JdYkTPVG9gRbvhK/giphy.gif?cid=6c09b952uf8lcok55y8ans5raxds0t2l0erufs0nsao0mpcf&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="Detective Gif" class="gif">
    <figcaption class="mt-2 text-muted">Your caption text here</figcaption>
</div>

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.

<div class="container">
    <div class="row justify-content-center">
        <div class="col-10">
            {% include plotly/rq7_movie_clusters.html %}
        </div>
    </div>
</div>

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.

<div class="container">
    <div class="row justify-content-center">
        <div class="col-10">
            {% include plotly/rq7_worst_clusters.html %}
        </div>
    </div>
</div>

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.

<div class="container">
    <div class="row justify-content-center">
        <div class="col-10">
            {% include plotly/rq7_trope_network.html %}
        </div>
    </div>
</div>

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.

<div class="container">
    <div class="row justify-content-center">
        <div class="col-10">
            {% include plotly/rq7_trope_combinations.html %}
        </div>
    </div>
</div>

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.

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
                <h5 class="fw-bold mb-2">Rizhong Lin</h5>
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
