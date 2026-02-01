"""
ETL (Extract, Transform, Load) - Practice Exercises
====================================================

Learn to build data pipelines: reading various formats,
cleaning/transforming data, and outputting clean datasets.

Run with Claude Code: "Run ETL exercise 1"

Prerequisites: Python basics, Pandas basics
"""

import pandas as pd
import json
import os
from pathlib import Path

# =============================================================================
# EXERCISE 1: Reading Different File Formats
# =============================================================================
"""
Practice reading data from CSV, JSON, and Excel files.
"""

def read_csv_with_options(filepath):
    """
    Read a CSV file with these requirements:
    - Skip the first 2 rows (metadata/headers)
    - Use the 3rd row as column names
    - Parse 'date' column as datetime
    - Handle missing values represented as 'N/A', 'NA', or '-'

    Return: DataFrame
    """
    pass

def read_json_nested(filepath):
    """
    Read a JSON file with nested structure like:
    {
        "data": {
            "records": [
                {"id": 1, "value": 100},
                {"id": 2, "value": 200}
            ]
        }
    }

    Return: DataFrame with 'id' and 'value' columns
    """
    pass

def read_multiple_csv_files(folder_path):
    """
    Read all CSV files in a folder and concatenate them.
    Add a 'source_file' column indicating which file each row came from.

    Return: Single concatenated DataFrame
    """
    pass


# =============================================================================
# EXERCISE 2: Data Cleaning
# =============================================================================
"""
Clean messy data to prepare for analysis.

Sample messy data:
    df = pd.DataFrame({
        'name': ['John Smith', 'JANE DOE', 'bob wilson', '  Alice  ', None],
        'email': ['john@email.com', 'JANE@EMAIL.COM', 'invalid', 'alice@email.com', 'bob@email.com'],
        'phone': ['123-456-7890', '(234) 567-8901', '345.678.9012', '456-789-0123', None],
        'salary': ['$50,000', '60000', '$75,000.00', '80k', None],
        'date': ['2024-01-15', '01/20/2024', 'Jan 25, 2024', '2024-02-01', None]
    })
"""

def get_messy_df():
    return pd.DataFrame({
        'name': ['John Smith', 'JANE DOE', 'bob wilson', '  Alice  ', None],
        'email': ['john@email.com', 'JANE@EMAIL.COM', 'invalid', 'alice@email.com', 'bob@email.com'],
        'phone': ['123-456-7890', '(234) 567-8901', '345.678.9012', '456-789-0123', None],
        'salary': ['$50,000', '60000', '$75,000.00', '80k', None],
        'date': ['2024-01-15', '01/20/2024', 'Jan 25, 2024', '2024-02-01', None]
    })

def clean_names(df):
    """
    Clean the 'name' column:
    - Strip whitespace
    - Convert to title case
    - Replace None with 'Unknown'

    Return: DataFrame with cleaned names
    """
    pass

def standardize_phone_numbers(df):
    """
    Standardize phone numbers to format: XXX-XXX-XXXX
    Remove all non-numeric characters, then format.
    Handle None values.

    Return: DataFrame with standardized phones
    """
    pass

def parse_salary_to_numeric(df):
    """
    Convert salary strings to numeric:
    - Remove '$' and ','
    - Handle 'k' suffix (e.g., '80k' -> 80000)
    - Convert to float
    - Handle None values

    Return: DataFrame with numeric salary column
    """
    pass

def validate_email(df):
    """
    Add 'email_valid' boolean column:
    - True if email contains '@' and '.'
    - False otherwise

    Return: DataFrame with email_valid column
    """
    pass


# =============================================================================
# EXERCISE 3: Data Transformation
# =============================================================================
"""
Transform data structures and derive new features.
"""

def unpivot_wide_to_long(df):
    """
    Transform wide format to long format.

    Input (wide):
        product | jan_sales | feb_sales | mar_sales
        Widget  | 100       | 150       | 200
        Gadget  | 80        | 90        | 100

    Output (long):
        product | month | sales
        Widget  | jan   | 100
        Widget  | feb   | 150
        ...

    Use pd.melt()
    """
    pass

def pivot_long_to_wide(df):
    """
    Transform long format to wide format (opposite of above).
    Use pd.pivot()
    """
    pass

def create_date_features(df):
    """
    Given a DataFrame with 'date' column (datetime):
    Add columns: year, month, day_of_week, is_weekend, quarter

    Return: DataFrame with new date feature columns
    """
    pass

def bin_numeric_column(df, column, bins, labels):
    """
    Create binned/categorical version of numeric column.

    Example: bin 'age' into ['Young', 'Middle', 'Senior']

    Return: DataFrame with new binned column
    """
    pass


# =============================================================================
# EXERCISE 4: Deduplication
# =============================================================================
"""
Handle duplicate records appropriately.

Sample data with duplicates:
    df = pd.DataFrame({
        'customer_id': [1, 2, 1, 3, 2, 1],
        'order_date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-01', '2024-01-02', '2024-01-01'],
        'amount': [100, 200, 150, 300, 200, 100]
    })
"""

def get_duplicate_df():
    return pd.DataFrame({
        'customer_id': [1, 2, 1, 3, 2, 1],
        'order_date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-01', '2024-01-02', '2024-01-01'],
        'amount': [100, 200, 150, 300, 200, 100]
    })

def find_duplicates(df, subset_columns):
    """
    Find and return all duplicate rows based on subset of columns.
    Include all occurrences (not just first/last).
    """
    pass

def remove_duplicates_keep_latest(df, id_column, date_column):
    """
    Remove duplicates, keeping the row with the latest date for each ID.
    """
    pass

def aggregate_duplicates(df, group_columns, agg_column, agg_func='sum'):
    """
    Instead of removing duplicates, aggregate them.
    Sum the 'amount' for duplicate customer_id + order_date combinations.
    """
    pass


# =============================================================================
# EXERCISE 5: Building a Complete ETL Pipeline
# =============================================================================
"""
Combine everything into a complete ETL pipeline.
"""

def etl_pipeline(input_path, output_path):
    """
    Build a complete ETL pipeline:

    EXTRACT:
    - Read CSV file from input_path

    TRANSFORM:
    - Clean column names (lowercase, replace spaces with underscores)
    - Remove completely empty rows
    - Fill missing numeric values with column median
    - Fill missing string values with 'Unknown'
    - Remove duplicate rows
    - Add 'processed_date' column with current date

    LOAD:
    - Save cleaned data to output_path as CSV
    - Return summary dict: {
        'rows_input': int,
        'rows_output': int,
        'rows_removed': int,
        'columns': list
      }
    """
    pass

def etl_with_validation(input_path, output_path, schema):
    """
    ETL pipeline with schema validation.

    schema = {
        'required_columns': ['id', 'name', 'value'],
        'column_types': {'id': 'int', 'value': 'float'},
        'not_null': ['id', 'name']
    }

    Raise ValueError if validation fails.
    Return success message and row counts if passes.
    """
    pass


# =============================================================================
# TEST RUNNER
# =============================================================================
if __name__ == "__main__":
    print("ETL Exercises - Run with Claude Code")
    print("=" * 50)
    print("\nExample: 'Run ETL exercise 1'")
    print("\nExercises:")
    print("1. Reading Different File Formats")
    print("2. Data Cleaning")
    print("3. Data Transformation")
    print("4. Deduplication")
    print("5. Building a Complete ETL Pipeline")
