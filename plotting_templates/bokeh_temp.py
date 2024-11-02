from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.transform import dodge
from bokeh.models import ColumnDataSource, LabelSet
import numpy as np
from math import pi

# Initialize Bokeh in a notebook
output_notebook()

# Select plot type: 'line', 'scatter', 'bar', or 'pie'
plot_type = 'line'  # Options: 'line', 'scatter', 'bar', 'pie'

# Define data
x_values = [1, 2, 3, 4, 5]
y_values = [10, 15, 10, 20, 25]

# Figure settings
plot = figure(title="Plot Title Here", width=600, height=400, x_axis_label="X-axis Label Here", y_axis_label="Y-axis Label Here")

# Plot options
color = "skyblue"  # Color for line, scatter, or bar plot
line_width = 2
size = 10          # Marker size for scatter plot
bar_width = 0.8    # Width of bars in bar chart

# Define plots based on type
if plot_type == 'line':
    plot.line(x_values, y_values, line_width=line_width, color=color, legend_label="Line Plot")
    plot.circle(x_values, y_values, size=size, color=color, legend_label="Line Points")
    
elif plot_type == 'scatter':
    plot.scatter(x_values, y_values, size=size, color=color, marker="circle", legend_label="Scatter Plot")

elif plot_type == 'bar':
    # Prepare data for bar chart
    source = ColumnDataSource(data=dict(x=[str(i) for i in x_values], y=y_values))
    plot.vbar(x=dodge('x', 0, range=plot.x_range), top='y', width=bar_width, source=source, color=color, legend_label="Bar Chart")

elif plot_type == 'pie':
    # Prepare data for pie chart
    angles = [y / sum(y_values) * 2 * pi for y in y_values]
    start_angles = np.cumsum([0] + angles[:-1])
    end_angles = np.cumsum(angles)
    colors = ["#AEC6E0", "#FF69B4", "#FFD700", "#ADFF2F", "#FF6347"]  # Custom color palette
    
    # Plot each wedge as a pie slice
    for i in range(len(y_values)):
        plot.wedge(x=0, y=0, radius=0.4, start_angle=start_angles[i], end_angle=end_angles[i],
                   color=colors[i % len(colors)], legend_label=f"Slice {i+1}")

# Display plot
plot.legend.location = "top_left"
plot.legend.title = "Legend"
show(plot)
