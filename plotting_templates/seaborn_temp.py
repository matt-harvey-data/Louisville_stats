import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data (you can replace this with your own data)
data = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [10, 15, 10, 20, 25],
    "category": ["A", "B", "A", "B", "A"]
})

# Choose plot type: 'line', 'scatter', or 'bar'
plot_type = 'line'  # Options: 'line', 'scatter', 'bar'

# Seaborn plot template
plt.figure(figsize=(8, 6))  # Figure size
title = "Seaborn Plot Title"
color_palette = "pastel"  # Color options: "muted", "bright", "pastel", etc.

if plot_type == 'line':
    sns.lineplot(data=data, x="x", y="y", hue="category", palette=color_palette)
elif plot_type == 'scatter':
    sns.scatterplot(data=data, x="x", y="y", hue="category", palette=color_palette, s=100)
elif plot_type == 'bar':
    sns.barplot(data=data, x="x", y="y", hue="category", palette=color_palette)

# Add title and show plot
plt.title(title)
plt.show()
