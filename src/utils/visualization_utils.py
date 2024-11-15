import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def setup_visualization():
    """Set up global visualization parameters."""
    plt.style.use("seaborn-v0_8")
    plt.rcParams["figure.figsize"] = [12, 6]
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["figure.autolayout"] = True

    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)


def create_genre_colors(unique_genres):
    """Create consistent color palette for genres."""
    return dict(zip(unique_genres, sns.color_palette("husl", len(unique_genres))))
