from plotnine import ggplot, aes, geom_line, geom_point, geom_bar, labs, theme_minimal
import pandas as pd

# Sample data (replace with your data)
data = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [10, 15, 10, 20, 25],
    "category": ["A", "B", "A", "B", "A"]
})

# Choose plot type: 'line', 'scatter', or 'bar'
plot_type = 'line'  # Options: 'line', 'scatter', 'bar'

# Base plot
if plot_type == 'line':
    plot = (ggplot(data, aes(x="x", y="y", color="category")) +
            geom_line(size=1) +
            geom_point(size=3))
elif plot_type == 'scatter':
    plot = ggplot(data, aes(x="x", y="y", color="category")) + geom_point(size=5)
elif plot_type == 'bar':
    plot = ggplot(data, aes(x="x", y="y", fill="category")) + geom_bar(stat="identity", position="dodge")

# Add title and labels
plot += labs(title="Plotnine Plot Title", x="X-axis Label", y="Y-axis Label") + theme_minimal()

# Display plot
print(plot)
