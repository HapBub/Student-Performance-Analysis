import pandas as pd
import numpy as np
class StudentAnalyzer:
    """Performs analysis on the cleaned Student Performance Factors dataset."""

    def __init__(self, data: pd.DataFrame) -> None:
        """Initialises the analyzer with a cleaned DataFrame."""
        self._data = data

    ############################################################################################

    def correlation(self) -> pd.Series:
        """
        Computes correlation of all numerical columns with Exam_Score.

        Returns a Series sorted from strongest to weakest correlation.
        """
        num_data = self._data.select_dtypes(include="number")
        result = num_data.corr()["Exam_Score"].drop("Exam_Score").sort_values(ascending=False)
        print("Correlation with Exam_Score:")
        print(result.to_string())
        return result

    ############################################################################################

    def group_aggregation(self, group_by: str) -> pd.DataFrame:
        """
        Groups data by a categorical column and compute Exam_Score statistics.

        Parameters
        group_by : str

        The categorical column to group by.
        Returns a DataFrame with mean, median and std of Exam_Score per group.
        """

        result = (
            self._data.groupby(group_by)["Exam_Score"]
            .agg(mean="mean", median="median", std="std")
            .round(2)
            .sort_values("mean", ascending=False)
        )
        print(f"\nExam_Score by {group_by}:")
        print(result.to_string())
        return result

    #############################################################################################

    def statistical_summary(self) -> pd.DataFrame:
        """
        Computes descriptive statistics for all numerical columns.

        Returns a DataFrame with mean, median, std, min and max.
        """
        print(f"NumPy mean of Exam_Score: {np.mean(self._data['Exam_Score']):.2f}")
        num_data = self._data.select_dtypes(include="number")
        result = num_data.agg(["mean", "median", "std", "min", "max"]).round(2)
        print("Statistical Summary:")
        print(result.to_string())
        return result