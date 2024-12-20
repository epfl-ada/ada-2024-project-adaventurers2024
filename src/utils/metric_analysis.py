import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import statsmodels.api as sm
import os

def metric_analysis(data_path):
    # 1. Initialize
    # Load the dataset
    df = pd.read_csv(data_path)

    # 2. Process the dataset
    # Check 0 vote_average, revenue, and budget
    print(
        f"Number of 0 values in each column: {(df[['vote_average', 'revenue', 'budget']] == 0).sum()}"
    )
    print(
        f"Number of missing values in each column: {df[['vote_average', 'revenue', 'budget']].isnull().sum()}"
    )

    # Remove rows if one of vote_average, revenue, and budget is 0
    df = df[(df[["vote_average", "revenue", "budget"]] != 0).all(axis=1)]
    df.reset_index(drop=True, inplace=True)

    # Calculate profit
    df["profit"] = df["revenue"] - df["budget"]
    # Calculate the ratio of revenue to budget
    df["revenue_to_budget"] = df["revenue"] / df["budget"]

    # Logscale the revenue and profit columns
    df["log_revenue"] = np.log1p(df["revenue"])
    df["log_profit"] = np.log1p(df["profit"])
    df["log_revenue_to_budget"] = np.log1p(df["revenue_to_budget"])

    # 3. Analyze

    # 3.1 Initial statistical summary
    print(df[["vote_average", "vote_count", "revenue", "profit"]].describe())

    # 3.2 Distribution plots
    variables = ["vote_average", "log_revenue", "log_profit", "log_revenue_to_budget"]
    for var in variables:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[var], bins=20, kde=True)
        plt.title(f"Distribution of {var.capitalize()}")
        plt.xlabel(var.capitalize())
        plt.ylabel("Frequency")
        plt.show()

    # 3.3 Scatter plot: Vote Average vs. Vote Count
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="vote_count", y="vote_average", data=df)
    plt.title("Vote Average vs. Vote Count")
    plt.xlabel("Vote Count")
    plt.ylabel("Vote Average")
    plt.show()

    # 3.4 Scatter plot: Revenue vs. Budget
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="budget", y="revenue", data=df)
    plt.title("Revenue vs. Budget")
    plt.xlabel("Budget")
    plt.ylabel("Revenue")
    plt.show()

    # 3.5 Scatter plot: Profit vs. Budget
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="budget", y="profit", data=df)
    plt.title("Profit vs. Budget")
    plt.xlabel("Budget")
    plt.ylabel("Profit")
    plt.show()

    # 3.6 Scatter plot: Average Rating vs. Revenue
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x="vote_average", y="revenue", data=df, alpha=0.7)
    plt.title("Average Rating vs. Revenue")
    plt.xlabel("Average Rating")
    plt.ylabel("Revenue")
    plt.yscale("log")  # Optional: Apply log scale if revenue has a wide range
    plt.show()

    # 3.7 Correlation matrix
    corr_columns = ["vote_average", "vote_count", "revenue", "budget", "profit"]
    corr_matrix = df[corr_columns].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()

def rq1_display_pair_plot(file_path, columns_to_plot):
    """
    Generates and displays a pair plot with histograms and scatter plots for given columns from a dataset.
    
    Parameters:
    - file_path (str): Path to the JSON file containing the dataset.
    - columns_to_plot (list of str): List of column names to include in the pair plot.

    Returns:
    - None
    """
    # Load the dataset
    try:
        df = pd.read_json(file_path)
    except ValueError:
        raise ValueError(f"Could not read the file at {file_path}. Ensure the path and format are correct.")
    
    # Helper function for regression
    def add_trendline(x, y):
        """Fit an OLS trendline and return line endpoints."""
        x = np.array(x)
        y = np.array(y)
        # Handle NaN values
        x_clean = x[~np.isnan(y)]
        y_clean = y[~np.isnan(y)]
        x_with_const = sm.add_constant(x_clean)  # Add intercept
        model = sm.OLS(y_clean, x_with_const).fit()
        y_pred = model.predict(x_with_const)
        return x_clean, y_pred

    n = len(columns_to_plot)
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # Custom color palette

    # Create a subplot grid
    fig = make_subplots(
        rows=n, cols=n,
        shared_xaxes=False,
        shared_yaxes=False,
        vertical_spacing=0.05,
        horizontal_spacing=0.05
    )

    # Loop through rows and columns
    for i, col_y in enumerate(columns_to_plot):
        for j, col_x in enumerate(columns_to_plot):
            row, col = i + 1, j + 1

            if i == j:
                # Diagonal: Histogram
                fig.add_trace(
                    go.Histogram(
                        x=df[col_x],
                        nbinsx=20,
                        marker=dict(color=colors[i], line=dict(color="black", width=1)),
                        opacity=0.7,
                        name=f"{col_x} Distribution"
                    ),
                    row=row, col=col
                )
            else:
                # Off-diagonal: Scatter plot with trendline
                fig.add_trace(
                    go.Scatter(
                        x=df[col_x],
                        y=df[col_y],
                        mode='markers',
                        marker=dict(size=5, color=colors[j], opacity=0.7),
                        name=f"{col_y} vs {col_x}"
                    ),
                    row=row, col=col
                )

                # Add trendline
                x_clean, y_pred = add_trendline(df[col_x], df[col_y])
                fig.add_trace(
                    go.Scatter(
                        x=x_clean,
                        y=y_pred,
                        mode='lines',
                        line=dict(color='red', width=2),
                        name=f"Trendline: {col_y} ~ {col_x}"
                    ),
                    row=row, col=col
                )

    # Update Layout
    fig.update_layout(
        title_text="Distribution and Correlation Between Columns",
        width=880,
        height=720,
        legend=dict(
            x=1.05, y=1,
            traceorder="normal",
            font=dict(size=10),
            bgcolor="rgba(255, 255, 255, 0.5)",
            bordercolor="gray",
            borderwidth=1
        ),
        template="plotly_white",
    )

    # Update axis labels
    for i, col in enumerate(columns_to_plot):
        fig.update_xaxes(title_text=col, row=n, col=i + 1)
        fig.update_yaxes(title_text=col, row=i + 1, col=1)

    # Display the figure
    fig.show()
