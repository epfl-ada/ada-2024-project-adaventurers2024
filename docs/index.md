---
layout: page
title: "🎬 Box Office Bombs 💣: A Data Detective Story"
subtitle: "Unraveling the 🧬 DNA of Failed Films"
cover-img: /assets/img/cover.jpeg
---

<style>
html, body {
    max-width: 100%;
    overflow-x: hidden;
}

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

- 42,000+ movie plots
- Cast and crew data from IMDb
- 30,000+ narrative tropes

## Key Evidence 🔍

Hey there, movie fans! Come join us to discover why some movies fail. We've been looking at Hollywood's past and found lots of movies that didn't succeed. As we looked closer, we found some interesting clues - like movies that came out at the wrong time (imagine opening your movie the same day as a new superhero film!), or movies that had stories people just didn't want to watch.

But wait, there's more to this story! It's like a puzzle we need to solve! So grab some popcorn and join us as we figure out why some movies fail.

<div class="text-center">
    <img src="https://media4.giphy.com/media/NS7gPxeumewkWDOIxi/giphy.gif?cid=6c09b952mg94u2g7aq1pcnj1sxdidnzdsm6as1z4c55nx3bs&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="Detective Gif" class="gif">
    <figcaption class="mt-2 text-muted">From the movie: <em>Detective Pikachu</em></figcaption>
</div>

<div class="section-divider"></div>

### Part I: The Evidence of Failure: Metrics

Let us start our investigation with three primary suspects: Average Vote, Revenue, and ROI (Return on Investment). The scatterplot matrix serves as our evidence board, showing how these three metrics interact.

<div class="container">
    <div class="row justify-content-center">
        <div class="col-auto">
            {% include plotly/rq1_metrics_distribution.html %}
        </div>
    </div>
</div>

The diagonal histograms give us their basic profiles. Average Vote is fairly stable, with most ratings clustering between 6 and 7, and two peaks around 6.3 and 7.3. Revenue is more erratic—most films make under $50 million, but a small number break well beyond $150 million. ROI, like revenue, is also skewed; most films’ returns are modest, clustering below 2.

Comparing these metrics pairwise provides further clues. Movies with lower ratings tend to have worse returns, though this link is not strong. For instance, films rated below 5 commonly have a negative ROI. A similar mild trend appears between revenue and ROI. Some low-revenue movies tend to generate low profits.

In short, lower ratings may lead films toward worse revenue and ROI, but they don’t solve the mystery on their own. These metrics serve as useful signals rather than direct culprits. They hint at trouble, but they don’t tell us who’s really pulling the strings behind a movie’s downfall. To crack the case, we’ll need to dig deeper into the forces at play behind the scenes. Follow me as we investigate the true causes lurking beneath these surface indicators.

<div class="section-divider"></div>

### Part II: The Cast Check: Actor Demographics
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

<div class="section-divider"></div>

### Part III: The Director's Enigma: Director Filmographies

<div class="text-center">
    <img src="https://media2.giphy.com/media/eQabXVbbLW63K/200.gif?cid=6c09b952h6xy4fkwj27ehe3n3g9bm294agh7j44b1s6pdrp0&ep=v1_gifs_search&rid=200.gif&ct=g" alt="Director Gif" class="gif">
    <figcaption class="mt-2 text-muted">From the animated series: <em>Peanuts</em></figcaption>
</div>

Next, we turn our attention to directors. Is thematic consistency or variety in their filmography related to poor performance?

<div class="row">
    <div class="col-sm-12 col-md-4 d-flex align-items-center">
        The Sankey diagram compares the number of genres directors work with to their films’ ratings and average revenue. Directors who stick to just one genre generally cluster in lower rating categories, 5.5–6.0. This suggests that overly rigid thematic focus may limit a film’s appeal. In contrast, directors who explore a moderate range of genres—around 6 to 13—tend to produce films with higher ratings (above 6.4). 
        <br><br>
        Revenue patterns follow a similar trend. Directors who either confine themselves to very few genres (e.g., 1) or attempt too many (e.g., 18) show lower average revenues (lower than $30 million). Those who maintain a middle ground, exploring a moderate but not overwhelming range of genres, tend to see better financial returns. 
    </div>
    <div class="col-sm-12 col-md-8">
        {% include plotly/rq3_genres_to_ratings.html %}
    </div>
</div>

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
    <div class="col-sm-12 col-md-4 d-flex align-items-center">
        A closer examination of the ROI distribution chart reveals a troubling pattern across genres. Documentaries stand out with their extreme variance, showing ROI swings from -216% to a staggering 9900%. This volatility tells a story of a genre where financial outcomes are wildly unpredictable. Horror films follow a similar pattern, with their error bars stretching far into both positive and negative territories, suggesting an industry segment where financial planning becomes more art than science.
    </div>
</div>

The relationship between budget categories and financial outcomes presents perhaps the most counterintuitive finding in our investigation. While Very High budget films command the largest absolute profits, their ROI tells a drastically different story. These blockbusters barely achieve a 1x return on investment, with their error bars suggesting frequent dips into negative territory. The data paints a picture of an inverse relationship: as budgets climb, ROI potential consistently diminishes, creating a tension between absolute returns and investment efficiency.

<div class="plotly-visualization" style="width: 100%;">
  {% include plotly/rq4_6_budget_analysis.html %}
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

The failure rate chart reveals a disturbing truth about Hollywood's riskiest genres. Thrillers emerge as the industry's most treacherous territory, with a startling 4.5% of productions ending in catastrophic losses (defined as losing over 50% of their investment). This is closely followed by Science Fiction films at 4%, painting a picture of genres where ambition and disaster walk hand in hand. These aren't just statistics - they represent hundreds of millions in lost investments and countless careers derailed.

Looking at the success rate chart might initially seem to offer hope, with Adventure and Science Fiction films showing impressive peaks of around 13% success (defined as achieving over 100% ROI). However, this apparent silver lining reveals a darker truth when viewed alongside the failure rates. The very genres that promise the highest rewards also harbor the highest risks of catastrophic failure. It's a classic case of double-edged sword economics, where the path to potential triumph is littered with financial casualties.

The intersection of these two metrics exposes the full scope of Hollywood's genre-based risk landscape. While genres like Animation and TV Movies show admirably low failure rates (under 1%), they also demonstrate limited success potential, rarely breaking past the 5% success rate threshold. This creates a cruel dynamic where playing it safe leads to stagnation, while pursuing bigger returns inevitably increases exposure to catastrophic failure. The data suggests that in Hollywood's high-stakes game, there are no truly safe harbors - only varying degrees of risk and compromise.

_Case File Note: The evidence points to a fundamental truth in Hollywood - genres that promise the highest returns are often the same ones that harbor the greatest potential for devastating failure. This isn't just coincidence; it's the DNA of the industry's risk structure._

<!-- ## Part II: The Deeper Patterns -->

#### The Heat Map of Hollywood Heartbreak 🎯

The performance heat map before us reads like a crime scene analysis of Hollywood's financial casualties. The dark purple bands stretching across the left side of the visualization tell a sobering story - every genre, without exception, has its share of total losses and severe failures. This isn't just data; it's a graveyard of creative ambitions and financial investments. The deepest purple zones, particularly prominent in TV Movies and Westerns, represent areas where movies go to die, rarely emerging from the red zone of financial loss.

<div class="row">
    <div class="col-sm-12 col-md-4 d-flex align-items-center">
        Moving towards the center, we encounter what might be called "Hollywood's Purgatory" - the break-even zone. Here, the colors begin to warm slightly, but the predominant purple tones reveal an uncomfortable truth: most films barely manage to recoup their investments. This vast middle ground isn't merely a neutral zone; it represents thousands of projects that failed to achieve their financial potential, languishing in what industry veterans darkly call "development hell." The transition from deep purple to lighter shades in this region maps the thin line between failure and mere survival.
    </div>
    <div class="col-sm-12 col-md-8">
        {% include plotly/rq4_9_success_matrix.html %}
    </div>
</div>

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

<div class="section-divider"></div>

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

In our search for what makes movies fail, we've found something interesting: tropes. Think of tropes as storytelling patterns that keep showing up in movies - like when the hero gets rescued at the last minute, or when there's a mad scientist character, or even when characters travel through time and mess things up. While tropes aren't necessarily good or bad on their own, how they're used can make or break a movie. We suspect certain tropes might be behind negative audience reactions and box office failures.

#### The Tropes of Failure: When Narrative Patterns Predict Disaster 📜

To understand what's going on, we first need to find which tropes show up most often in movies people don't like. We're looking at movies that got scores lower than 6.0 and were rated by at least 100 people (after all, we need enough people to have watched the movie to be sure). But here's something interesting - just because we find a trope in bad movies doesn't automatically make it bad. Maybe it appears in lots of good movies too! That's why we look at how often it shows up in low rated movies compared to high rated ones. The higher this ratio, the more likely the trope is connected to low ratings. Let's examine our first piece of evidence in the chart below:

<div class="container-fluid">
    <div class="row">
        <div class="col-12">
            {% include plotly/rq6_tropes.html %}
        </div>
    </div>
</div>

Our investigation shows three main suspects across all genres: "NotScreenedForCritics" which is typically seen as a red flag for poor quality, "ActionDressRip" which is used as a visual appealing element but can be seen as very dramatic, and "HellOnEarth" which is a trope that many horror movies overuse to show apocalyctic scenarios. When we look at just drama movies, we found some other interesting patterns like "BTeamSequel" (when they make a sequel without the original stars), "DisneyVillainDeath" (when the villain dies dramatically), and "BlondBrunetteRedHead" (when they put three hair colors characters together). The chart above shows even more examples from different types of movies.

But which tropes get the worst ratings? Let's look at the top 10 tropes with the lowest ratings in our files:

<div class="container">
  {% include plotly/rq7_tropes_boxplot.html %}
</div>

Looking at this box plot which shows the median, the interquartile range and the distribution of the average rating for the top 10 tropes identified in movies. The plot reveals that these tropes usually get ratings between 4 and 6. "BMovie" and "SlasherFilm" have some unusual cases - "BMovie" sometimes gets really low scores below 2.5, while in the case of "SlasherFilm" sometimes it is love or sometimes is hate it by the audience. "MonsterMisogyny" seems to be our biggest troublemaker, getting the lowest typical ratings, probably because audiences don't like movies that show harmful ideas about violence against women.

### Tropes working together: Combinations of tropes that lead to failure

But wait - what happens when these tropes combine forces? To solve this mystery, we used k-means clustering to group movies based on their tropes. It's like finding out which ingredients often get used in the same recipe.

<div class="container">
    <div class="row justify-content-center">
        <div class="col-10">
            {% include plotly/rq7_movie_clusters.html %}
        </div>
    </div>
</div>

Interestingly, the clustering reveals that many movies share common trope patterns, and we can also observe some regions where certain cluster dominates like the cluster 19 and 20. The t-SNE plot allow us to visualize these clusters in a 2D space, where each point represents a movie and the color represents the cluster to which it belongs.

We are interested in the clusters with the lowest average ratings as they represents the tropes that were not well received by the audience. Thus, let's check out which groups of movies got the worst ratings:

<div class="container">
    <div class="row justify-content-center">
        <div class="col-10">
            {% include plotly/rq7_worst_clusters.html %}
        </div>
    </div>
</div>

Clearly clusters 9, 13 and 20 highlight in these top, they are our prime suspects. We also can see some movies stand alone at the edges, showing that sometimes even unusual combinations of tropes can lead to bad ratings.

To have a better look of these combinations, the following bar chart reveals the most frequently trope combinations in our worst-rated movie clusters. The combination of "HorrorFilms + ShoutOut + AssholeVictim" appears most frequently, followed by other horror-related combinations involving B-movies, SciFiHorror and slasher films movies. This suggests that certain horror movie formulas, particularly those that rely heavily on traditional tropes, tend to be perceived as repetitive or unoriginal by audiences, leading to poor ratings. Beyond horror, we see recurring patterns in other genres: dirty cop narratives, recursive or self-referential storytelling (as shown by "AlliterativeTitle + RecursiveCanon + RecursiveFiction"), and psychological thrillers with specific social themes. The presence of "BigBad + FilmsOfThe1980s + TheDragon" suggests that dated villain archetypes from the 1980s may not do well with modern audiences. These combinations point to potential narrative fatigue, where audiences may be responding negatively to overly familiar or poorly executed trope patterns

<div class="container">
    <div class="row justify-content-center">
        <div class="col-10">
            {% include plotly/rq7_trope_combinations.html %}
        </div>
    </div>
</div>

Finally, let's look at how these tropes connect to each other:

<div class="container">
    <div class="row justify-content-center">
        <div class="col-10">
            {% include plotly/rq7_trope_network.html %}
        </div>
    </div>
</div>

Our network visualization reveals the connection between tropes in poorly-rated movies, with "HorrorFilms" emerging as the central node with the largest size, indicating its high frequency. The thickness of the connecting lines reveals particularly strong co-occurrences between certain tropes, highlighting common but potentially problematic narrative combinations in these lower-rated films. We can notice strong connections between horror-related tropes, forming a dense cluster that includes "SlasherFilm," "BMovie," and "SciFiHorror." This central cluster connects to more specific tropes like "FinalGirl," "DeathBySex," and "TooDumbToLive," suggesting that these narrative elements frequently appear together in poorly-received films. Moreover, there's another interesting pattern in our evidence: "FilmsOfThe1980s" connecting with "TheDragon" and "BigBad" shows a combination that probably are too simple or outdated for audiences that prefer more complex and original narratives. 

<div class="text-center">
    <img src="https://media0.giphy.com/media/l2JdYkTPVG9gRbvhK/giphy.gif?cid=6c09b952uf8lcok55y8ans5raxds0t2l0erufs0nsao0mpcf&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="Detective Gif" class="gif">
    <figcaption class="mt-2 text-muted">From the animated series: <em>The Simpsons</em></figcaption>
</div>

### 🎭 The Historical Record: Tropes with consistently low ratings across years

Our next clue in the investigation is to look at how tropes have performed over time. Particularly, we're interested in tropes that have consistently led to negative audience reception and are the ones that are in the following plot. We decided to look back through time to see the average ratings of these tropes over the years.

<div class="container">
  {% include plotly/rq8_tropes_avg_scores.html %}
</div>

These tropes show average ratings fluctuating between 4 and 6. Moreover, in the early years of this analysis, we noticed that "ChekhovsGun" and "OhCrap" are actually gotten better over time, having scores around 5.5 recently. Looks like filmmakers have figured out how to use better these tropes. However, "HorrorFilms" and "BMovie" have stayed pretty much the same over the years, usually getting between 4 and 5 stars. And here's something funny - "FilmsOfThe1980s" did best during... you guessed it, the 1980s! Thus, it seems that some tropes might have a better reception over time, probably because they are used in a more creative and innovative way. While other tropes, like horror films, might have a more consistent performance, suggesting that audiences have certain expectations for these tropes.

_Case File Note: This section of our investigation reveals that while individual tropes like "NotScreenedForCritics" and "MonsterMisogyny" are red flags for low ratings, the most dangerous patterns emerge when some tropes combine, particularly the combination of horror films. This genre has a tendency to group certain tropes (like "SlasherFilm" + "BMovie" + "SciFiHorror"), a pattern that consistently leads to poor audience reception and suggests filmmakers should focus on new ideas that avoid trying to combine these narrative formulas._

<div class="section-divider"></div>

## Conclusion 🎬

#### Closed: The Anatomy of Box Office Failure 🎬
After an exhaustive investigation into over 42,000 films, examining everything from cast diversity to seasonal patterns, we can finally close this case file on Hollywood's biggest failures. The evidence points to a complex web of factors that can doom a film to box office disaster.

#### The Final Report 📋
Our investigation has uncovered several key patterns that serve as warning signs for potential box office bombs:

1. The Cast Conundrum 👥

While cast diversity itself isn't a primary culprit, our investigation found that extremes in any direction can be problematic:

Very high age and ethnic diversity correlates with lower median earnings
Low gender diversity may result in lower audience ratings
The sweet spot appears to be moderate diversity across all metrics

2. The Director's Dilemma 🎥

Our evidence points to a clear pattern in directorial careers:

Directors who stick to a single genre show consistently lower ratings (5.5-6.0)
Those who spread themselves too thin across many genres see diminished returns
The optimal range appears to be 6-13 genres, suggesting that calculated versatility trumps both rigid specialization and excessive experimentation

3. The Genre Trap 🎭
We've discovered that certain genres are particularly susceptible to catastrophic failure. Thrillers and Science Fiction films show the highest failure rates (4.5% and 4% respectively), while carrying the cruel irony of also offering the highest potential returns. The evidence suggests that these genres don't just fail – they fail greatly, creating a high-stakes gambling scenario for studios.
4. The Temporal Curse ⏰
Our analysis of release timing revealed a treacherous calendar landscape:

Winter emerges as the season of extremes, where holiday releases either soar or crash
January stands as the deadliest month, with the highest severe loss rate (0.8%)
Summer blockbuster season shows itself to be a double-edged sword, with high success rates (8-8.2%) matched by significant failure rates

5. The Trope Trap 📖

Perhaps our most damning evidence comes from the analysis of narrative patterns:

Certain combinations of tropes, particularly in horror films, act as reliable predictors of failure
The "NotScreenedForCritics" trope emerges as a consistent red flag
Historical analysis shows some tropes, like "HorrorFilms" and "BMovie," have maintained their negative impact across decades

#### The Verdict 🔨

After examining all the evidence, we can conclude that box office failures rarely result from a single fatal flaw. Instead, they emerge from a perfect storm of risk factors: poor timing, problematic genre choices, overused tropes, and suboptimal creative decisions. The data suggests that many of Hollywood's biggest failures could have been predicted – and potentially prevented – by paying attention to these warning signs.

#### Case Status: CLOSED 📁
While we've identified the primary factors contributing to box office failures, the entertainment industry remains an inherently risky business. No amount of data analysis can completely eliminate the possibility of failure, but understanding these patterns can help minimize the risk of creating the next legendary box office bomb.
Remember: In Hollywood, as in any mystery, the clues are always there if you know where to look.
Filed by: ADAdventurers
Date: December 20, 2024
Case Number: BOB-2024-001

<div class="section-divider"></div>
<section class="container py-5">
    <h2 class="text-center mb-5 fw-bold">About Our Detective Team</h2>
    <div class="row text-center g-4">
        <div class="col">
            <div class="p-3 h-100 border-0 shadow-sm rounded">
                <div class="emoji-large">🕵️‍♂️</div>
                <h5 class="fw-bold mb-2">Jianan Xu</h5>
            </div>
        </div>
        <div class="col">
            <div class="p-3 h-100 border-0 shadow-sm rounded">
                <div class="emoji-large">🕵️‍♂️</div>
                <h5 class="fw-bold mb-2">Rizhong Lin</h5>
            </div>
        </div>
        <div class="col">
            <div class="p-3 h-100 border-0 shadow-sm rounded">
                <div class="emoji-large">🕵️‍♂️</div>
                <h5 class="fw-bold mb-2">Angel Zenteno</h5>
            </div>
        </div>
        <div class="col">
            <div class="p-3 h-100 border-0 shadow-sm rounded">
                <div class="emoji-large">🕵️‍♀️</div>
                <h5 class="fw-bold mb-2">Adriana Orellana</h5>
            </div>
        </div>
        <div class="col">
            <div class="p-3 h-100 border-0 shadow-sm rounded">
                <div class="emoji-large">🕵️‍♂️</div>
                <h5 class="fw-bold mb-2">Raph Wegmann</h5>
            </div>
        </div>
    </div>
</section>

<div class="section-divider"></div>

## Want to Know More?

Check out our [detailed analysis](https://github.com/epfl-ada/ada-2024-project-adaventurers2024/blob/main/results.ipynb) or dive into our [methodology](https://github.com/epfl-ada/ada-2024-project-adaventurers2024/tree/main).
