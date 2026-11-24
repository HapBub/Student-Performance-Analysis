"""
main.py
Runs the full Student Performance analysis pipeline.

Usage: place StudentPerformanceFactors.csv in this folder, then run `python main.py`.
"""
from src.dataset import DatasetHandler
from src.analyzer import StudentAnalyzer
from src.visualizer import StudentVisualizer


def main() -> None:
    # Load and clean the data
    h = DatasetHandler("data/StudentPerformanceFactors.csv")
    h.load()
    h.select_columns()
    h.remove_duplicates()
    h.fix_dtypes()
    h.handle_missing()
    h.summary()

    # Analyze
    a = StudentAnalyzer(h.get_data())
    a.correlation()
    a.group_aggregation("Family_Income")
    a.group_aggregation("Motivation_Level")
    a.group_aggregation("School_Type")
    a.statistical_summary()

    # Visualize
    v = StudentVisualizer(h.get_data())
    v.plot_score_distribution()
    v.plot_correlation()
    v.plot_group_comparison("Family_Income")
    v.plot_group_comparison("Motivation_Level")
    v.plot_bonus()


if __name__ == "__main__":
    main()