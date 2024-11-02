import matplotlib.pyplot as plt

# Choose your plot type: 'line', 'scatter', 'bar', or 'pie'
plot_type = 'line'  # Options: 'line', 'scatter', 'bar', 'pie'

# Define data for the plots
x_values = [1, 2, 3, 4, 5]  # x-axis data for line, scatter, or bar plot
y_values = [10, 15, 10, 20, 25]  # y-axis data for line, scatter, or bar plot

# Define figure size (width, height in inches)
plt.figure(figsize=(8, 6))

# Title and labels
plt.title("Plot Title Here")  # Add plot title
plt.xlabel("X-axis Label Here")  # Label for x-axis (if applicable)
plt.ylabel("Y-axis Label Here")  # Label for y-axis (if applicable)

# Plot customization options
color = "skyblue"          # Color for line or bar plot
marker = "o"               # Marker type for scatter or line plot
line_style = "-"           # Line style for line plot (e.g., '-', '--', '-.', ':')
explode = (0.1, 0, 0, 0, 0)  # Explode setting for pie chart (if applicable)

# Select plot type
if plot_type == 'line':
    plt.plot(x_values, y_values, color=color, marker=marker, linestyle=line_style, linewidth=2)
elif plot_type == 'scatter':
    plt.scatter(x_values, y_values, color=color, marker=marker, s=100)  # s is marker size
elif plot_type == 'bar':
    plt.bar(x_values, y_values, color=color)
elif plot_type == 'pie':
    plt.pie(y_values, labels=x_values, colors=[color], explode=explode, autopct='%1.1f%%')

# Show grid (optional)
plt.grid(True)

# Display plot
plt.show()
