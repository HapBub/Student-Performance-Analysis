"""
visualizer.py
Handles visualizations for the Student Performance Factors dataset.
"""
import pandas as pd
import matplotlib.pyplot as plt

class StudentVisualizer:
    """Creates visualizations for the Student Performance Factors dataset."""

    def __init__(self, data: pd.DataFrame) -> None:
        """Initialise the visualizer with a cleaned DataFrame."""
        self._data = data

    def plot_correlation(self) -> None:
        """
        Plot a horizontal bar chart of correlations with Exam_Score.

        Bars are colored green for positive and red for negative correlation.
        """
        num_data = self._data.select_dtypes(include="number")
        corr = num_data.corr()["Exam_Score"].drop("Exam_Score").sort_values()

        colors = ["red" if v < 0 else "green" for v in corr.values]

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.barh(corr.index, corr.values, color=colors)
        ax.axvline(0, color="black", linewidth=0.8)
        ax.set_title("Correlation with Exam Score")
        ax.set_xlabel("Correlation coefficient")
        plt.tight_layout()
        plt.show()

    def plot_group_comparison(self, group_by: str) -> None:
        """
        Plot a bar chart of mean Exam_Score grouped by a categorical column.

        Parameters
        group_by : str
        The categorical column to group by.
        """
        grouped = (
            self._data.groupby(group_by)["Exam_Score"]
            .mean()
            .round(2)
            .sort_values(ascending=False)
        )

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(grouped.index, grouped.values, color="steelblue")
        ax.set_title(f"Average Exam Score by {group_by}")
        ax.set_xlabel(group_by)
        ax.set_ylabel("Mean Exam Score")
        ax.set_ylim(grouped.values.min() - 2, grouped.values.max() + 2)
        for i, val in enumerate(grouped.values):
            ax.text(i, val + 0.1, str(val), ha="center", fontsize=9)
        plt.tight_layout()
        plt.show()

    def plot_score_distribution(self) -> None:
        """
        Plot a histogram of Exam_Score with a mean line.
        """
        scores = self._data["Exam_Score"]
        mean_score = scores.mean()

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.hist(scores, bins=20, color="steelblue", edgecolor="white")
        ax.axvline(mean_score, color="red", linewidth=1.5, linestyle="--", label=f"Mean: {mean_score:.1f}")
        ax.set_title("Distribution of Exam Scores")
        ax.set_xlabel("Exam Score")
        ax.set_ylabel("Number of Students")
        ax.legend()
        plt.tight_layout()
        plt.show()

    def plot_bonus(self) -> None:
        """
        Plot mean Exam_Score for the 3 bonus columns (Gender,
        Learning_Disabilities, Distance_from_Home) side by side.
        """
        bonus_cols = ["Gender", "Learning_Disabilities", "Distance_from_Home"]

        fig, axes = plt.subplots(1, 3, figsize=(14, 5))
        fig.suptitle("Bonus: Additional Factors vs Exam Score", fontsize=13)

        for ax, col in zip(axes, bonus_cols):
            grouped = (
                self._data.groupby(col)["Exam_Score"]
                .mean()
                .round(2)
                .sort_values(ascending=False)
            )
            ax.bar(grouped.index, grouped.values, color="mediumpurple")
            ax.set_title(f"By {col}")
            ax.set_xlabel(col)
            ax.set_ylabel("Mean Exam Score")
            ax.set_ylim(grouped.values.min() - 2, grouped.values.max() + 2)
            for i, val in enumerate(grouped.values):
                ax.text(i, val + 0.1, str(val), ha="center", fontsize=9)

        plt.tight_layout()
        plt.show()