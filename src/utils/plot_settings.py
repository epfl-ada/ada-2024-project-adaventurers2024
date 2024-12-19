COLORS = [
    '#1f77b4',  # Blue
    '#ff7f0e',  # Orange
    '#2ca02c',  # Green
    '#d62728',  # Red
    '#9467bd',  # Purple
    '#8c564b',  # Brown
    '#e377c2',  # Pink
    '#7f7f7f',  # Gray
    '#bcbd22',  # Olive
    '#17becf'   # Cyan
]

# Common layout settings
COMMON_LAYOUT = {
    'plot_bgcolor': 'white',
}

# Axis styling settings
AXIS_STYLE = {
    'showgrid': True,
    'gridwidth': 1,
    'gridcolor': '#E5E5E5',
    'zeroline': True,
    'zerolinewidth': 1,
    'zerolinecolor': '#E5E5E5'
}

# Title styling settings
def get_title_style(text, size=20):
    return {
        'text': f"<b>{text}</b>",
        'font': {'size': size}
    }

# Function to create hover template
def create_hover_template(x_label="Year", y_label="Value", y_format=".2f"):
    return f'{x_label}: %{{x}}<br>{y_label}: %{{y:{y_format}}}<extra></extra>'

# Function to style subplots titles
def style_subplot_titles(tropes):
    return [f"Trope: {trope}" for trope in tropes]

# Common subplot settings
def get_subplot_settings(num_rows, tropes):
    return {
        'rows': num_rows,
        'cols': 3,
        'subplot_titles': style_subplot_titles(tropes),
        'vertical_spacing': 0.15,
        'horizontal_spacing': 0.05
    }