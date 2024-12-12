import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# set the default font size to 14 and font family to 'Arial'
import plotly.io as pio

pio.templates.default = "plotly_white"
pio.templates[pio.templates.default].layout.font.size = 14
pio.templates[pio.templates.default].layout.font.family = "Arial"


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


def rgb_to_hex(rgb_tuple):
    """Convert RGB tuple to hex color string."""
    return "#{:02x}{:02x}{:02x}".format(
        int(rgb_tuple[0] * 255), int(rgb_tuple[1] * 255), int(rgb_tuple[2] * 255)
    )


def hex_to_rgb(hex_string):
    """Convert hex color string to RGB tuple."""
    return tuple(int(hex_string.lstrip("#")[i : i + 2], 16) / 255 for i in (0, 2, 4))


def prepare_color_map(genre_colors):
    """Convert RGB tuple colors to hex strings."""
    return {genre: rgb_to_hex(color) for genre, color in genre_colors.items()}
