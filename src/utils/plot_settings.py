COLORS = [
    '#4363d8',  # Enhanced Blue
    '#f58231',  # Vivid Orange
    '#3cb44b',  # Bright Green
    '#e6194B',  # Vivid Red
    '#911eb4',  # Rich Purple
    '#f032e6',  # Magenta
    '#46f0f1',  # Cyan
    '#f58231',  # Coral
    '#808000',  # Olive
    '#008080'   # Teal
]

# Enhanced common layout settings
COMMON_LAYOUT = {
    'plot_bgcolor': 'white',
    'paper_bgcolor': 'white',
    'margin': dict(l=80, r=20, t=100, b=50),
    'font': dict(
        family="Arial, sans-serif",
        size=13,
        color="#2F2F2F"
    )
}

# Enhanced axis styling
AXIS_STYLE = {
    'showgrid': True,
    'gridwidth': 1,
    'gridcolor': '#F0F0F0',
    'zeroline': True,
    'zerolinewidth': 2,
    'zerolinecolor': '#CCCCCC',
    'linecolor': '#2F2F2F',
    'linewidth': 2,
    'ticks': 'outside',
    'tickwidth': 2,
    'tickcolor': '#2F2F2F',
    'ticklen': 6,
    'tickfont': dict(
        family='Arial, sans-serif',
        size=14,
        color='#2F2F2F'
    )
}

# Enhanced title styling
def get_title_style(text):
    return {
        'text': text,
        'font': {
            'family': 'Arial, sans-serif',
            'color': '#1F1F1F'
        },
        'y': 0.95,  # Slightly lower position for better spacing
        'pad': dict(b=20)  # Add padding below title
    }

# Enhanced hover template
def create_hover_template(x_label="Year", y_label="Value", y_format=".2f"):
    return (
        f'<b>{x_label}</b>: %{{x}}<br>'
        f'<b>{y_label}</b>: %{{y:{y_format}}}'
        '<extra></extra>'
    )

# Enhanced subplot settings
def get_subplot_settings(num_rows, tropes):
    return {
        'rows': num_rows,
        'cols': 3,
        'subplot_titles': tropes,
        'vertical_spacing': 0.15,  # Increased spacing
        'horizontal_spacing': 0.08,  # Increased spacing
    }


BAR_STYLE = {
    'marker': dict(
        color=COLORS[0],
        line=dict(
            width=1,
            color=COLORS[0]
        ),
        opacity=0.85
    )
}

# Function to apply bar style
def apply_bar_style(fig):
    fig.update_traces(
        marker=dict(
            color=COLORS[0],
            line=dict(color=COLORS[0], width=1),
            opacity=0.85
        ),
        hoverlabel=dict(
            bgcolor='white',
            font_size=12,
            font_family='Arial, sans-serif'
        )
    )
    return fig