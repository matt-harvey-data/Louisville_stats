from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Sample data
data = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [10, 15, 10, 20, 25],
    "category": ["A", "B", "A", "B", "A"]
})

# Initialize the Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Dash Plotly Template"),
    
    dcc.Dropdown(
        id='plot-type-dropdown',
        options=[
            {'label': 'Line', 'value': 'line'},
            {'label': 'Scatter', 'value': 'scatter'},
            {'label': 'Bar', 'value': 'bar'}
        ],
        value='line'  # Default plot type
    ),
    
    dcc.Graph(id='plot-output')
])

# Callback for updating plot based on dropdown selection
@app.callback(
    Output('plot-output', 'figure'),
    Input('plot-type-dropdown', 'value')
)
def update_plot(plot_type):
    if plot_type == 'line':
        fig = px.line(data, x='x', y='y', color='category', title="Line Plot")
    elif plot_type == 'scatter':
        fig = px.scatter(data, x='x', y='y', color='category', title="Scatter Plot")
    elif plot_type == 'bar':
        fig = px.bar(data, x='x', y='y', color='category', title="Bar Plot", barmode='group')
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
