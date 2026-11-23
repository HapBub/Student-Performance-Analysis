# Student Performance Analysis

An exploratory data analysis project investigating the relationship between behavioral, motivational, and socioeconomic factors and student academic performance using Python, statistical methods, and data visualization.

## 📌 Overview

The objective of this project is to identify and examine the factors that have the strongest relationship with students' academic performance, particularly exam scores.

Using Python and several data science libraries, we explored how factors such as attendance, study habits, motivation, family income, and school type relate to academic outcomes.

The project was developed as part of the **DS120 – Programming for Data Science** course at the American University of Armenia.

## 📊 Dataset

The analysis uses the *Student Performance Factors* dataset obtained from Kaggle.

- **Number of observations:** 6,607 students
- **Number of features:** 20
- **Data types:** Numerical and categorical

The dataset includes variables such as:

- Hours studied and sleep duration
- Attendance and previous academic scores
- Motivation and peer influence
- Family income and parental involvement
- School type and tutoring sessions

Gender, distance from home, and learning disabilities were treated as additional variables and analyzed separately.

## 🛠️ Technologies & Libraries

- **Python** – Main programming language
- **Pandas** – Data manipulation and preprocessing
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualization
- **Object-Oriented Programming (OOP)** – Modular project architecture

## 🔍 Analysis & Methodology

The project is divided into three main stages:

### 1. Data Preprocessing

- Loading and inspecting the dataset
- Selecting relevant columns
- Removing duplicate observations
- Correcting data types
- Handling missing values

### 2. Statistical Analysis

- Correlation analysis to examine relationships between numerical variables
- Group aggregation to compare academic performance across categorical variables
- Statistical summaries of numerical features

### 3. Data Visualization

- Exam score distribution histogram
- Correlation bar chart
- Group comparison visualizations
- Separate visual analysis of additional variables

## 💡 Key Findings

The analysis revealed several notable patterns:

- **Attendance** showed the strongest positive correlation with exam scores (0.58).
- **Hours studied** followed with a positive correlation of 0.45.
- Previous scores and tutoring sessions also demonstrated weaker positive correlations.
- Students with higher motivation levels tended to achieve better academic results.
- Students from higher-income families showed higher average scores than those from lower-income families.
- Private school students demonstrated higher average scores than public school students.
- Exam scores followed an approximately normal distribution, with a mean of around 67.

These findings describe associations within the dataset and do not necessarily establish causal relationships.

## 📁 Project Structure

```text
Student-Performance-Analysis/
│
├── dataset.py       # Data loading and preprocessing
├── analyzer.py      # Statistical analysis and aggregation
├── visualizer.py    # Data visualization
├── main.py          # Main execution pipeline
│
├── StudentPerformanceFactors.csv
├── Report.pdf
└── README.md
```

### Code Architecture

The project follows a modular, object-oriented structure:

- **DatasetHandler:** Responsible for loading, cleaning, and preparing the dataset.
- **StudentAnalyzer:** Implements correlation analysis, group aggregation, and statistical summaries.
- **StudentVisualizer:** Generates visual representations of the analysis results.
- **main.py:** Integrates the modules and executes the complete analysis pipeline.

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed.

Install the required libraries:

```bash
pip install numpy pandas matplotlib
```

### Running the Project

1. Clone the repository:

```bash
git clone https://github.com/HapBub/Student-Performance-Analysis
```

2. Navigate to the project directory:

```bash
cd Student-Performance-Analysis
```

3. Make sure the dataset file is in the project directory.

4. Run the main script:

```bash
python main.py
```

## 📄 Project Report

For a more detailed explanation of the methodology, analysis, findings, and project development, see the Full Project Report (PDF).

## 👥 Contributors

**Davit Meliksetyan**

- Led the development of the data loading and preprocessing module.

**Serine Ananyan**

- Led the development of the data visualization module.

Both contributors collaborated on the statistical analysis and overall project architecture.

---

*Developed as part of DS120 – Programming for Data Science, American University of Armenia (May 2026).*

