"""
dataset.py
Loads and cleans the Student Performance Factors dataset.
"""
import pandas as pd

# Splitting the dataset into 2 key parts:
# 1) Main columns - crucial for extracting useful knowledge from the data,
# 2) Bonus columns - provide additional, but less essential insights about the data
MAIN_COLUMNS = [
    "Hours_Studied", "Attendance", "Parental_Involvement",
    "Access_to_Resources", "Extracurricular_Activities", "Sleep_Hours",
    "Previous_Scores", "Motivation_Level", "Internet_Access",
    "Tutoring_Sessions", "Family_Income", "Teacher_Quality",
    "School_Type", "Peer_Influence", "Physical_Activity",
    "Parental_Education_Level", "Exam_Score",
]

BONUS_COLUMNS = ["Distance_from_Home", "Gender", "Learning_Disabilities"]


class DatasetHandler:
    """
    The first main class of the project.

    1) Loads the dataset,
    2) Selects relevant columns,
    3) Removes duplicates,
    4) Fixes data types,
    5) Handles missing values.
    """

    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self._data = None  # protected attribute holding the DataFrame

    #############################################################################################

    def load(self) -> None:
        """Load the dataset from a CSV file and report the number of rows and columns."""
        self._data = pd.read_csv(self.filepath)
        print(f"Loaded {self._data.shape[0]:,} rows x {self._data.shape[1]} columns.")

    #############################################################################################

    def select_columns(self) -> None:
        """
        Keep only the relevant columns for the analysis.

        MAIN_COLUMNS are used for the core analysis.
        BONUS_COLUMNS are kept separately for bonus visualizations.
        """
        # .copy() avoids pandas' SettingWithCopyWarning in later steps
        self._data = self._data[MAIN_COLUMNS + BONUS_COLUMNS].copy()
        print(f"Selected {len(MAIN_COLUMNS)} main columns + {len(BONUS_COLUMNS)} bonus columns.")

    #############################################################################################

    def remove_duplicates(self) -> None:
        """Remove duplicate rows from the dataset."""
        before = len(self._data)
        self._data.drop_duplicates(inplace=True)
        self._data.reset_index(drop=True, inplace=True)
        print(f"Duplicates removed: {before - len(self._data)}")

    #############################################################################################

    def fix_dtypes(self) -> None:
        """
        Ensure numerical columns have a numeric dtype.

        Values that cannot be converted become NaN and are filled later
        by handle_missing().
        """
        numeric_cols = [
            "Hours_Studied", "Attendance", "Sleep_Hours",
            "Previous_Scores", "Tutoring_Sessions",
            "Physical_Activity", "Exam_Score",
        ]
        for col in numeric_cols:
            self._data[col] = pd.to_numeric(self._data[col], errors="coerce")
        print(f"Dtypes fixed for: {numeric_cols}")

    #############################################################################################

    def handle_missing(self) -> None:
        """
        Fill missing values in each column.

        Strategy:
        - Numerical columns -> median
        - Categorical columns -> mode (the most frequent value)
        """
        cols_with_missing = self._data.columns[self._data.isnull().any()].tolist()

        if not cols_with_missing:
            print("No missing values found.")
            return

        for col in cols_with_missing:
            n_missing = self._data[col].isnull().sum()
            if pd.api.types.is_numeric_dtype(self._data[col]):
                fill_val = self._data[col].median()
                strategy = "median"
            else:
                fill_val = self._data[col].mode()[0]
                strategy = "mode"
            self._data[col] = self._data[col].fillna(fill_val)
            print(f"  '{col}': filled {n_missing} missing values with {strategy} ({fill_val!r})")

    #############################################################################################

    def summary(self) -> None:
        """Print an overview of the current DataFrame."""
        df = self._data

        print("\n" + "=" * 45)
        print("DATASET SUMMARY")
        print("=" * 45)

        print(f"  Shape      : {df.shape[0]:,} rows x {df.shape[1]} columns")
        print(f"  Missing    : {df.isnull().sum().sum()}")

        print("\n  Columns:")
        for col in df.columns:
            dtype = str(df[col].dtype)
            n_unique = df[col].nunique()
            print(f"    {col:<30} {dtype:<10} {n_unique} unique values")

        print("\n  Numerical statistics:")
        print(df.describe().to_string())

        print("=" * 45 + "\n")

    #############################################################################################

    def get_data(self) -> pd.DataFrame:
        """Return a copy of the current DataFrame."""
        return self._data.copy()