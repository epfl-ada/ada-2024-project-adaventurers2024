---
layout: post
title: "🎬 Decoding Box-Office Bombs"
subtitle: "A Data Science Journey Through 42,000 Failed Films"
cover-img: "/assets/img/movie-analytics-bg.png"
thumbnail-img: "/assets/img/popcorn-spill.jpg"
share-img: "/assets/img/movie-analytics-bg.png"
tags: [data-analysis, movies, EPFL]
---

<style>
.section-divider {
    text-align: center;
    margin: 40px 0;
    font-size: 24px;
    color: #666;
}

.stat-box {
    background: rgba(255,255,255,0.9);
    border-radius: 8px;
    padding: 20px;
    margin: 20px 0;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.plotly-container {
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 15px rgba(0,0,0,0.1);
    margin: 30px 0;
}

.team-section {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    margin: 40px 0;
}

.team-member {
    text-align: center;
    margin: 15px;
    flex: 0 1 200px;
}

.highlight-text {
    background: linear-gradient(120deg, #ff9a9e 0%, #fad0c4 100%);
    padding: 3px 8px;
    border-radius: 4px;
    color: #333;
}
</style>

# 🔍 The Investigation

Ever wondered why some movies fail spectacularly at the box office? We're diving deep into the data of 42,000+ films to uncover the DNA of box office bombs. Think of us as cinematic forensics experts, analyzing everything from ill-fated release dates to questionable casting choices.

<div class="section-divider">🎬</div>

## The Evidence at a Glance

<div class="stat-box">
- 📊 42,000+ movies analyzed
- 💰 Billions in box office data
- 🎭 30,000+ narrative tropes examined
- 🌍 Global release patterns studied
</div>

## The Money Trail 💸

When movies go wrong, they go wrong big. Our analysis reveals some fascinating patterns in the relationship between budgets and box office performance.

<div class="plotly-container">
{% include plotly/visualization1.html %}
</div>

## Cast & Crew: The Usual Suspects 🎭

Our data reveals surprising patterns in how cast diversity and director track records influence a movie's fate.

<div class="plotly-container">
{% include plotly/visualization2.html %}
</div>

## The Perfect Storm: Release Timing ⏰

Some release dates are deadlier than others. Here's what we found about timing and movie failures.

<div class="plotly-container">
{% include plotly/visualization3.html %}
</div>

## Plot Patterns: The Story Autopsy 📚

We've identified the most toxic combinations of plot tropes that spell disaster for films.

<div class="plotly-container">
{% include plotly/visualization4.html %}
</div>

<div class="section-divider">🎥</div>

## The Investigation Team

<div class="team-section">
<div class="team-member">
    <h3>JX</h3>
    <p>The Financial Forensics Expert</p>
</div>
<div class="team-member">
    <h3>RL</h3>
    <p>The Market Pattern Analyst</p>
</div>
<div class="team-member">
    <h3>RW</h3>
    <p>The Director Profiler</p>
</div>
<div class="team-member">
    <h3>AZ</h3>
    <p>The Plot Pattern Specialist</p>
</div>
<div class="team-member">
    <h3>AO</h3>
    <p>The Plot Pattern Specialist</p>
</div>
</div>

<div class="section-divider">🎬</div>

## Methodology & Data

This investigation combines data from multiple sources:
- Wikipedia plot summaries
- IMDb ratings and metadata
- TV Tropes narrative patterns
- Box office performance data

Our analysis employs advanced statistical methods including:
- Financial performance clustering
- Demographic analysis
- Temporal pattern recognition
- Natural language processing for plot analysis

<div class="highlight-text">
Project for the Applied Data Analysis course at EPFL, Fall 2024
</div>