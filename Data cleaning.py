import pandas as pd

data = {
    "Emp ID": [101, 102, 103, 103, 104, 105],
    "Name": ["Ravi ", "Sita", None, "Amit", "Neha", "Rahul"],
    "Age": [25, None, -30, 40, 200, 35],
    "Department": ["IT", "HR", "IT ", "hr", "Finance", None],
    "Salary": [50000, None, 60000, 0, 8000000, 45000],
    "Join Date": ["2021-01-10", "2020/05/20", "invalid", "2019-03-15", "2018-07-01", "2022-02-30"]
}

df = pd.DataFrame(data)

#clean column names
df.columns = df.columns.str.lower().str.replace(" ","_")

#handle missing values
df["name"] = df["name"].fillna("Unknown")
df["age"] = df["age"].fillna(df["age"].median())
df["department"] = df["department"].fillna(df["department"].mode()[0])
df["salary"] = df["salary"].fillna(df["salary"].median())
df.drop_duplicates(subset="emp_id", inplace=True)

#fixed invalid values
df = df[(df["age"] >= 18) & (df["age"] <= 60)]

#Standardize Text Data
df["department"] = df["department"].str.lower().str.strip()

#handle Outliers (Salary)
Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)
IQR = Q3 - Q1
df = df[(df["salary"] >= Q1 - 1.5*IQR) &
        (df["salary"] <= Q3 + 1.5*IQR)]

#fix Date Column
df["join_date"] = pd.to_datetime(df["join_date"], errors="coerce")



print(df.info())

