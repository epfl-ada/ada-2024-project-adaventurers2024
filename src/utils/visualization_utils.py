import matplotlib.pyplot as plt
import seaborn as sns

def setup_visualization():
    """Set up global visualization parameters."""
    plt.style.use('seaborn-v0_8')
    plt.rcParams['figure.figsize'] = [12, 6]
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['figure.autolayout'] = True

def create_genre_colors(unique_genres):
    """Create consistent color palette for genres."""
    return dict(zip(unique_genres, sns.color_palette("husl", len(unique_genres))))