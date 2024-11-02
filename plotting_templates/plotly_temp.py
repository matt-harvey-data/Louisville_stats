import plotly.graph_objects as go

# Choose your plot type: 'line', 'scatter', 'bar', or 'pie'
plot_type = 'line'  # Options: 'line', 'scatter', 'bar', 'pie'

# Define data for the plots
x_values = [1, 2, 3, 4, 5]
y_values = [10, 15, 10, 20, 25]

# Plot customization options
color = "skyblue"  # Color for lines, bars, or scatter markers
marker_size = 10   # Marker size for scatter plot

# Create plot based on selected type
fig = go.Figure()

if plot_type == 'line':
    fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines+markers', line=dict(color=color, width=2),
                             marker=dict(size=marker_size), name="Line Plot"))

elif plot_type == 'scatter':
    fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='markers', marker=dict(color=color, size=marker_size),
                             name="Scatter Plot"))

elif plot_type == 'bar':
    fig.add_trace(go.Bar(x=x_values, y=y_values, marker=dict(color=color), name="Bar Chart"))

elif plot_type == 'pie':
    fig = go.Figure(data=[go.Pie(labels=x_values, values=y_values, hole=.3, marker=dict(colors=[color, "#FF69B4", "#FFD700", "#ADFF2F", "#FF6347"]))])

# Title and labels
fig.update_layout(
    title="Plot Title Here",
    xaxis_title="X-axis Label Here",
    yaxis_title="Y-axis Label Here",
    showlegend=True,
    width=800,
    height=500
)

# Display the plot
fig.show()
