# Employee Data Cleaning using Pandas

## Project Overview
This project demonstrates how to clean and preprocess real-world employee data using Python and Pandas.  
It focuses on handling missing values, incorrect entries, and inconsistent formatting to prepare the data for analysis.

## Problem Statement
Real-world datasets are often messy and contain missing or invalid values.  
This project shows practical techniques to clean such data using Pandas.

## Features
- Cleaning column names
- Handling missing values using mean, median, and mode
- Fixing invalid age and salary values
- Standardizing categorical data
- Preparing data for analysis

## Tech Stack
- Python
- Pandas
- NumPy

## Dataset Description
The dataset contains employee information such as:
- Employee ID
- Name
- Age
- Department
- Salary
- Join Date

## Data Cleaning Steps
1. Converted column names to lowercase with underscores
2. Filled missing names with "Unknown"
3. Removed invalid age values and filled missing values using median
4. Standardized department names and filled missing values using mode
5. Cleaned salary data and handled outliers
6. Prepared data for analysis

## Sample Code
```python
df.columns = df.columns.str.lower().str.replace(" ", "_")
df["name"] = df["name"].fillna("Unknown")
df["age"] = df["age"].fillna(df["age"].median())
df["department"] = df["department"].fillna(df["department"].mode()[0])
