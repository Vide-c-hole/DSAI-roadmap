"""
Pandas Fundamentals - Practice Exercises
=========================================

Complete each exercise by replacing `pass` with your solution.
Run with Claude Code: "Run pandas exercise 1"

Difficulty: Beginner → Intermediate
Prerequisites: Python basics, NumPy basics
"""

import pandas as pd
import numpy as np

# =============================================================================
# EXERCISE 1: DataFrame Creation
# =============================================================================
"""
Create a DataFrame from different data sources.

Tasks:
1.1 Create a DataFrame from a dictionary with columns: 'name', 'age', 'city'
    Data: [('Alice', 25, 'NYC'), ('Bob', 30, 'LA'), ('Charlie', 35, 'Chicago')]

1.2 Create a DataFrame from a list of dictionaries

1.3 Create a DataFrame with a custom index (use names as index)
"""

def create_dataframe_from_dict():
    """Return a DataFrame with name, age, city columns"""
    pass

def create_dataframe_from_list_of_dicts():
    """Return a DataFrame from list of dicts"""
    data = [
        {'product': 'Widget', 'price': 25.99, 'quantity': 100},
        {'product': 'Gadget', 'price': 49.99, 'quantity': 50},
        {'product': 'Gizmo', 'price': 15.99, 'quantity': 200}
    ]
    pass

def create_dataframe_with_index():
    """Return a DataFrame with names as the index"""
    pass


# =============================================================================
# EXERCISE 2: Selection and Filtering
# =============================================================================
"""
Practice selecting rows and columns from DataFrames.

Use this sample DataFrame:
    df = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales'],
        'salary': [75000, 50000, 80000, 60000, 55000],
        'years': [3, 5, 7, 2, 4]
    })
"""

def get_sample_df():
    return pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'department': ['Engineering', 'Sales', 'Engineering', 'HR', 'Sales'],
        'salary': [75000, 50000, 80000, 60000, 55000],
        'years': [3, 5, 7, 2, 4]
    })

def select_single_column(df):
    """Return just the 'name' column as a Series"""
    pass

def select_multiple_columns(df):
    """Return 'name' and 'salary' columns as a DataFrame"""
    pass

def filter_by_condition(df):
    """Return rows where salary > 60000"""
    pass

def filter_multiple_conditions(df):
    """Return Engineering employees with salary > 70000"""
    pass

def filter_using_isin(df):
    """Return employees in Engineering OR Sales departments"""
    pass


# =============================================================================
# EXERCISE 3: GroupBy Operations
# =============================================================================
"""
Aggregate data using groupby.

Tasks:
3.1 Calculate average salary by department
3.2 Count employees per department
3.3 Get multiple aggregations (mean, max, count) by department
"""

def avg_salary_by_department(df):
    """Return a Series with average salary per department"""
    pass

def count_by_department(df):
    """Return count of employees per department"""
    pass

def multiple_aggregations(df):
    """Return DataFrame with mean salary, max salary, and count per department"""
    pass


# =============================================================================
# EXERCISE 4: Handling Missing Data
# =============================================================================
"""
Practice handling NaN values.

Sample data with missing values:
    df = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 2, 3, np.nan, 5],
        'C': [1, 2, 3, 4, 5]
    })
"""

def get_missing_data_df():
    return pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 2, 3, np.nan, 5],
        'C': [1, 2, 3, 4, 5]
    })

def count_missing_values(df):
    """Return count of missing values per column"""
    pass

def fill_missing_with_mean(df):
    """Fill missing values in column 'A' with the column mean"""
    pass

def drop_rows_with_missing(df):
    """Return DataFrame with rows containing any NaN dropped"""
    pass


# =============================================================================
# EXERCISE 5: Merge and Join
# =============================================================================
"""
Combine DataFrames using merge operations.

employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'dept_id': [10, 20, 10, 30]
})

departments = pd.DataFrame({
    'dept_id': [10, 20, 40],
    'dept_name': ['Engineering', 'Sales', 'Marketing']
})
"""

def get_employees_df():
    return pd.DataFrame({
        'emp_id': [1, 2, 3, 4],
        'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'dept_id': [10, 20, 10, 30]
    })

def get_departments_df():
    return pd.DataFrame({
        'dept_id': [10, 20, 40],
        'dept_name': ['Engineering', 'Sales', 'Marketing']
    })

def inner_merge(employees, departments):
    """Return inner merge on dept_id (only matching rows)"""
    pass

def left_merge(employees, departments):
    """Return left merge (all employees, matching departments)"""
    pass

def outer_merge(employees, departments):
    """Return outer merge (all rows from both)"""
    pass


# =============================================================================
# EXERCISE 6: Pivot Tables
# =============================================================================
"""
Create pivot tables for data summarization.

sales = pd.DataFrame({
    'date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'product': ['Widget', 'Gadget', 'Widget', 'Gadget'],
    'region': ['North', 'North', 'South', 'South'],
    'revenue': [100, 150, 200, 250]
})
"""

def get_sales_df():
    return pd.DataFrame({
        'date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
        'product': ['Widget', 'Gadget', 'Widget', 'Gadget'],
        'region': ['North', 'North', 'South', 'South'],
        'revenue': [100, 150, 200, 250]
    })

def create_pivot_table(df):
    """
    Create pivot table:
    - Rows: product
    - Columns: region
    - Values: sum of revenue
    """
    pass

def pivot_with_multiple_aggs(df):
    """
    Create pivot table with both sum and mean of revenue
    by product (rows) and region (columns)
    """
    pass


# =============================================================================
# EXERCISE 7: Apply and Transform
# =============================================================================
"""
Apply custom functions to DataFrames.
"""

def apply_function_to_column(df):
    """
    Given df with 'salary' column, add a new column 'salary_tier':
    - 'Low' if salary < 55000
    - 'Medium' if 55000 <= salary < 75000
    - 'High' if salary >= 75000
    """
    pass

def apply_function_to_row(df):
    """
    Add column 'years_salary_ratio' = years / (salary / 10000)
    Use apply with axis=1
    """
    pass


# =============================================================================
# EXERCISE 8: String Operations
# =============================================================================
"""
Practice pandas string methods.

names = pd.DataFrame({
    'full_name': ['JOHN SMITH', 'jane doe', 'Bob Johnson', 'ALICE WONG']
})
"""

def get_names_df():
    return pd.DataFrame({
        'full_name': ['JOHN SMITH', 'jane doe', 'Bob Johnson', 'ALICE WONG']
    })

def convert_to_title_case(df):
    """Convert full_name to title case (e.g., 'John Smith')"""
    pass

def extract_first_name(df):
    """Add column 'first_name' with just the first name"""
    pass

def filter_names_containing(df, substring):
    """Return rows where full_name contains the substring (case insensitive)"""
    pass


# =============================================================================
# TEST RUNNER
# =============================================================================
if __name__ == "__main__":
    print("Pandas Exercises - Run with Claude Code")
    print("=" * 50)
    print("\nExample: 'Run pandas exercise 1'")
    print("\nExercises:")
    print("1. DataFrame Creation")
    print("2. Selection and Filtering")
    print("3. GroupBy Operations")
    print("4. Handling Missing Data")
    print("5. Merge and Join")
    print("6. Pivot Tables")
    print("7. Apply and Transform")
    print("8. String Operations")
