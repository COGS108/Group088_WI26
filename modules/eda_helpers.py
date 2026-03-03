import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_relationship(df, x, y, hue=None, title=None, log_scale=False):
    """Scatter plot with regression line for hypothesis testing."""
    if log_scale:
        plot_data = df.copy()
        plot_data[x] = plot_data[x] + 1
        plot_data[y] = plot_data[y] + 1
        sns.scatterplot(data=plot_data, x=plot_data[x], y=plot_data[y], hue=hue)
        plt.xscale("log")
        plt.yscale("log")
    else:
        sns.regplot(data=df, x=x, y=y)
    
    plt.title(title or f"{y} vs {x}")
    plt.grid(True, linestyle="--")
    plt.show()

def plot_distribution(df, column, title):
    """Distribution plot for skewed data."""
    sns.histplot(df[column], kde=True, bins=30)
    plt.axvline(df[column].median(), color="red", linestyle="--", label=f"Median: {df[column].median():.2f}")
    plt.title(title)
    plt.legend()
    plt.show()