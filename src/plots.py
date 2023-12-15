import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys


class Plot:
    def __init__(self) -> None:
        pass

    def plot_bar(self, x, y, xlabel,ylabel,title,palette=None) -> None:
        plt.figure(figsize=(12, 6))
        sns.barplot(x=x, y=y, palette="viridis")

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.show()

    def plot_count(self, df: pd.DataFrame, column: str) -> None:
        """Plot the count of the column.

        Args:
            df (pd.DataFrame): Dataframe to be plotted.
            column (str): column to be plotted.
        """
        plt.figure(figsize=(12, 7))
        sns.countplot(data=df, x=column)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()


    def plot_heatmap(self, df: pd.DataFrame, title: str, cbar=False) -> None:
        """Plot Heat map of the dataset.

        Args:
            df (pd.DataFrame): Dataframe to be plotted.
            title (str): title of chart.
        """
        # num_cols = df.select_dtypes(include=np.number).columns
        plt.figure(figsize=(12, 7))
        sns.heatmap(df, annot=True, cmap='viridis', vmin=0,
                    vmax=1, fmt='.2f', linewidths=.7, cbar=cbar)
        plt.title(title, size=18, fontweight='bold')
        plt.show()

    def plot_box(self, df: pd.DataFrame, x_col: str, title: str) -> None:
        """Plot box chart of the column.

        Args:
            df (pd.DataFrame): Dataframe to be plotted.
            x_col (str): column to be plotted.
            title (str): title of chart.
        """
        plt.figure(figsize=(12, 7))
        sns.boxplot(data=df, x=x_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.show()

    def plot_box_multi(self, df: pd.DataFrame, x_col: str, y_col: str, title: str) -> None:
        """Plot the box chart for multiple column.

        Args:
            df (pd.DataFrame): Dataframe to be plotted.
            column (str): column to be plotted.
        """
        plt.figure(figsize=(12, 7))
        sns.boxplot(data=df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()

    def plot_scatter(self, df: pd.DataFrame, x_col: str, y_col: str, title: str, hue: str, style: str) -> None:
        """Plot Scatter chart of the data.

        Args:
            df (pd.DataFrame): Dataframe to be plotted.
            column (str): column to be plotted.
        """
        plt.figure(figsize=(12, 7))
        sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, style=style)
        plt.title(title, size=20)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()

    def plot_pie(self, data, title, label) -> None:
        """Plot pie chart of the data.

        Args:
            data (list): Data to be plotted.
            labels (list): labels of the data.
            colors (list): colors of the data.
        """
        plt.figure(figsize=(8, 8))
        plt.pie(x=data, labels=label, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("Set3"))

        plt.title(title)
        plt.show()

    def plot_hist(self, df: pd.DataFrame, column: str, title: str) -> None:
        """Plot histogram of the data.

        Args:
            df (pd.DataFrame): Dataframe to be plotted.
            column (str): column to be plotted.
        """
        plt.figure(figsize=(12, 7))
        sns.histplot(data=df, x=column, kde=True)
        plt.title(title, size=20)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.show()