import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_seasonal_distributions(df):
    """Plot profit and rating distributions by season."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Profit by Season
    sns.violinplot(data=df, x='release_season', y='profit_scaled', 
                   ax=ax1, palette='viridis')
    ax1.set_yscale('symlog', linthresh=1)
    ax1.set_title('Movie Profits Distribution by Season', pad=20)
    ax1.set_ylabel('Profit (Millions USD, Log Scale)')
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(True, alpha=0.3)

    # Ratings by Season
    sns.violinplot(data=df, x='release_season', y='vote_average', 
                   ax=ax2, palette='viridis')
    ax2.set_title('Movie Rating Distribution by Season', pad=20)
    ax2.set_ylabel('Average Rating (0-10)')
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(True, alpha=0.3)
    for y in [5, 6, 7]:
        ax2.axhline(y=y, color='gray', linestyle='--', alpha=0.3)

    plt.tight_layout()
    plt.show()

    # Print statistics
    seasonal_stats = df.groupby('release_season').agg({
        'profit_scaled': ['mean', 'median'],
        'vote_average': ['mean', 'count'],
        'roi_clean': ['mean', 'median']
    }).round(2)
    
    print("\nSummary Statistics by Season:")
    print(seasonal_stats)
    
    return seasonal_stats

def analyze_monthly_performance(df):
    """Analyze and visualize monthly performance patterns."""
    # Distribution plots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))

    # Profit Distribution
    sns.violinplot(data=df, x='release_month', y='profit_scaled', 
                   ax=ax1, palette='viridis')
    ax1.set_yscale('symlog', linthresh=1)
    ax1.set_title('Movie Profits Distribution by Release Month', pad=20)
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Profit (Millions USD, Log Scale)')
    ax1.grid(True, alpha=0.3)

    # Rating Distribution
    sns.violinplot(data=df, x='release_month', y='vote_average', 
                   ax=ax2, palette='viridis')
    ax2.set_title('Movie Rating Distribution by Release Month', pad=20)
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Average Rating (0-10)')
    ax2.grid(True, alpha=0.3)
    for y in [5, 6, 7]:
        ax2.axhline(y=y, color='gray', linestyle='--', alpha=0.3)

    plt.tight_layout()
    plt.show()

def analyze_monthly_roi(df):
    """Analyze ROI patterns by month."""
    # ROI Distribution
    plt.figure(figsize=(14, 6))
    sns.violinplot(data=df[df['roi_clean'].notna()], 
                   x='release_month', y='roi_clean', 
                   palette='viridis')
    plt.title('ROI Distribution by Release Month', pad=20)
    plt.ylabel('Return on Investment (ROI)')
    plt.xlabel('Month')
    plt.yscale('symlog', linthresh=0.1)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

    # Calculate monthly performance rates
    monthly_performance = {}
    for month in range(1, 13):
        month_data = df[df['release_month'] == month]['roi_clean']
        rates = {
            'Severe Loss (>70%)': (month_data < -0.7).mean(),
            'Significant Loss (>50%)': (month_data < -0.5).mean(),
            'Break Even': (month_data > 0).mean(),
            'Successful (>100%)': (month_data > 1).mean(),
            'Very Successful (>200%)': (month_data > 2).mean()
        }
        monthly_performance[month] = rates

    return pd.DataFrame(monthly_performance).T.round(3) * 100

def plot_monthly_success_rates(monthly_perf_df):
    """Plot monthly success and failure rates."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Success rates
    monthly_perf_df['Successful (>100%)'].plot(kind='bar', ax=ax1, 
                                             color=sns.color_palette('viridis', 12))
    ax1.set_title('Success Rate by Month (>100% ROI)', pad=20)
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Success Rate (%)')
    plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')
    ax1.grid(True, alpha=0.3)

    # Failure rates
    monthly_perf_df['Significant Loss (>50%)'].plot(kind='bar', ax=ax2, 
                                                  color=sns.color_palette('viridis', 12))
    ax2.set_title('Failure Rate by Month (>50% Loss)', pad=20)
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Failure Rate (%)')
    plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

def analyze_monthly_statistics(df, monthly_perf_df):
    """Calculate and print detailed monthly statistics."""
    month_names = {
        1: 'January', 2: 'February', 3: 'March', 4: 'April',
        5: 'May', 6: 'June', 7: 'July', 8: 'August',
        9: 'September', 10: 'October', 11: 'November', 12: 'December'
    }

    # ROI statistics
    monthly_roi_stats = df.groupby('release_month')['roi_clean'].agg([
        'count', 'mean', 'median',
        lambda x: x.quantile(0.25),
        lambda x: x.quantile(0.75),
        lambda x: x.std()
    ]).round(3)
    monthly_roi_stats.columns = ['Count', 'Mean ROI', 'Median ROI', 
                               '25th Percentile', '75th Percentile', 'Std Dev']
    monthly_roi_stats.index = [month_names[m] for m in monthly_roi_stats.index]

    # Best and worst months
    best_months = monthly_perf_df['Successful (>100%)'].nlargest(3)
    worst_months = monthly_perf_df['Significant Loss (>50%)'].nlargest(3)

    # Risk-adjusted performance
    monthly_perf_df['Risk-Adjusted Performance'] = (
        monthly_perf_df['Successful (>100%)'] / 
        monthly_perf_df['Significant Loss (>50%)']
    ).round(2)

    return {
        'roi_stats': monthly_roi_stats,
        'best_months': best_months,
        'worst_months': worst_months,
        'risk_adjusted': monthly_perf_df['Risk-Adjusted Performance'].sort_values(ascending=False)
    }

def analyze_temporal_trends(df):
    """Analyze and visualize performance trends over time."""
    df['release_year'] = pd.to_numeric(df['release_year'])
    yearly_performance = df.groupby('release_year').agg(
        success_rate=('roi_clean', lambda x: (x > 1).mean()),
        failure_rate=('roi_clean', lambda x: (x < -0.5).mean()),
        movie_count=('roi_clean', 'count')
    )

    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Plot rates
    line1 = ax1.plot(yearly_performance.index, yearly_performance['success_rate'] * 100, 
                     color='forestgreen', linewidth=2, label='Success Rate (>100% ROI)')
    line2 = ax1.plot(yearly_performance.index, yearly_performance['failure_rate'] * 100, 
                     color='crimson', linewidth=2, label='Failure Rate (>50% Loss)')
    ax1.set_xlabel('Release Year')
    ax1.set_ylabel('Rate (%)', color='black')
    ax1.tick_params(axis='y', labelcolor='black')
    ax1.grid(True, alpha=0.3)

    # Add movie count
    ax2 = ax1.twinx()
    bars = ax2.bar(yearly_performance.index, yearly_performance['movie_count'], 
                   alpha=0.2, color='royalblue', label='Number of Movies')
    ax2.set_ylabel('Number of Movies', color='royalblue')
    ax2.tick_params(axis='y', labelcolor='royalblue')

    # Legend
    lines = line1 + line2 + [bars]
    labels = [l.get_label() for l in line1 + line2] + ['Number of Movies']
    ax1.legend(lines, labels, loc='upper left')

    plt.title('Movie Success, Failure Rates and Volume Over Time', pad=20)
    plt.tight_layout()
    plt.show()

    return yearly_performance

def run_timing_analysis(df):
    """Run complete timing analysis pipeline."""
    results = {}
    
    # Seasonal analysis
    results['seasonal_stats'] = plot_seasonal_distributions(df)
    
    # Monthly analysis
    analyze_monthly_performance(df)
    monthly_perf_df = analyze_monthly_roi(df)
    plot_monthly_success_rates(monthly_perf_df)
    results['monthly_stats'] = analyze_monthly_statistics(df, monthly_perf_df)
    
    # Temporal analysis
    results['yearly_performance'] = analyze_temporal_trends(df)
    
    return results