import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def rq1_analysis(data_path):
    # 1. Initialize
    # Load the dataset
    df = pd.read_csv(data_path)

    # 2. Process the dataset
    # Check 0 vote_average, revenue, and budget
    print(f"Number of 0 values in each column: {(df[['vote_average', 'revenue', 'budget']] == 0).sum()}")
    print(f"Number of missing values in each column: {df[['vote_average', 'revenue', 'budget']].isnull().sum()}")

    # Remove rows if one of vote_average, revenue, and budget is 0
    df = df[(df[['vote_average', 'revenue', 'budget']] != 0).all(axis=1)]
    df.reset_index(drop=True, inplace=True)

    # Calculate profit
    df['profit'] = df['revenue'] - df['budget']
    # Calculate the ratio of revenue to budget
    df['revenue_to_budget'] = df['revenue'] / df['budget']

    # Logscale the revenue and profit columns
    df['log_revenue'] = np.log1p(df['revenue'])
    df['log_profit'] = np.log1p(df['profit'])
    df['log_revenue_to_budget'] = np.log1p(df['revenue_to_budget'])

    # 3. Analyze

    # 3.1 Initial statistical summary
    print(df[['vote_average', 'vote_count', 'revenue', 'profit']].describe())

    # 3.2 Distribution plots
    variables = ['vote_average', 'log_revenue', 'log_profit', 'log_revenue_to_budget']
    for var in variables:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[var], bins=20, kde=True)
        plt.title(f'Distribution of {var.capitalize()}')
        plt.xlabel(var.capitalize())
        plt.ylabel('Frequency')
        plt.show()

    # 3.3 Scatter plot: Vote Average vs. Vote Count
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='vote_count', y='vote_average', data=df)
    plt.title('Vote Average vs. Vote Count')
    plt.xlabel('Vote Count')
    plt.ylabel('Vote Average')
    plt.show()

    # 3.4 Scatter plot: Revenue vs. Budget
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='budget', y='revenue', data=df)
    plt.title('Revenue vs. Budget')
    plt.xlabel('Budget')
    plt.ylabel('Revenue')
    plt.show()

    # 3.5 Scatter plot: Profit vs. Budget
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='budget', y='profit', data=df)
    plt.title('Profit vs. Budget')
    plt.xlabel('Budget')
    plt.ylabel('Profit')
    plt.show()

    # 3.6 Scatter plot: Average Rating vs. Revenue
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='vote_average', y='revenue', data=df, alpha=0.7)
    plt.title('Average Rating vs. Revenue')
    plt.xlabel('Average Rating')
    plt.ylabel('Revenue')
    plt.yscale('log')  # Optional: Apply log scale if revenue has a wide range
    plt.show()

    # 3.7 Correlation matrix
    corr_columns = ['vote_average', 'vote_count', 'revenue', 'budget', 'profit']
    corr_matrix = df[corr_columns].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()