---
title: pandas-practice-drills-notebook
topic: python-data
source_type: my-notes
source_file: STUDYNOTEs/pandas-practice-drills.ipynb
---

# Pandas Practice Drills

Companion notebook to `concepts/pandas-practice-drills.md`. Same 19 exercises, one markdown
cell per question with an empty code cell underneath for your solution.

## How to use this notebook

1. **Build a toy DataFrame first**, in the setup cell below, before touching a real CSV.
   5–10 fake rows with one obvious null and one obvious duplicate, so you know the "answer"
   going in.
2. **Work top to bottom** within a section — later drills in "Cleaning" and "Report writing"
   assume the toy frame from setup still exists.
3. **Re-run against a real CSV** once each drill works on the toy data — swap `df` for a
   `pd.read_csv(...)` call and see what breaks.
4. Don't peek at `pandas-cheatsheet` until you're stuck for a few minutes on a drill.

## Setup — build a toy dataset

Create a small DataFrame by hand here (5–10 rows, a mix of numeric and text columns, at least one null and one duplicate row). Every drill below reuses this `df` unless you point it at a real CSV instead.

```python
import pandas as pd
import numpy as np

# df = pd.DataFrame({...})
```

## Reading & inspecting

### 1. Read a CSV, print the shape, column names, and dtypes.

```python
import pandas as pd
csv_file10="inspection_10.csv"
df=pd.read_csv(csv_file10)
```

### 2. Read a CSV, display only 5 columns of your choice with `.head()`.

```python
df=pd.read_csv(csv_file10)
df.head(5)
```

### 3. Read a CSV, print the first 5 rows and the last 5 rows.

```python
csv_file20="inspection_sample_20.csv"
df=pd.read_csv(csv_file20)
df.head()
df.tail()
```

### 4. Read a CSV, print one column as a plain list and as a Series — note the difference in output.

```python
df=pd.read_csv(csv_file20)
df["priority"].tolist()
print(df["priority"])
```

## Null / missing checks

### 5. Print null count per column with one line (`.isna().sum()`).

```python
print(df.isna().sum())
```

### 6. Print which rows have a null in a specific column (`df[df["col"].isna()]`).

```python
print(df[df["text_clear"].isna()])
```

### 7. Print percent null per column, sorted highest to lowest.

```python
print((df.isnull().mean() * 100).sort_values(ascending=False))
```

### 8. Check for "hidden" missing values — empty strings or whitespace-only — separately from real nulls.

```python
null_count=0
whitespace_ct=0
for col in df.columns:
    null_count = df[col].isna().sum()

    whitespace_count = (
        df[col]
        .astype(str)
        .str.strip()
        .eq("")
        .sum()
    )

    print(col, "nulls:", null_count, "empty/whitespace:", whitespace_count)
```

## Duplicates

### 9. Print how many fully-duplicate rows exist (`.duplicated().sum()`), then display them.

```python
print(df.duplicated().sum())
```

### 10. Find duplicates based on just one or two columns, not the whole row (`.duplicated(subset=[...])`).

```python
print(df.duplicated(subset=["subject","body","priority"]))
```

### 11. Drop duplicates, keeping the first occurrence, and print how many rows were removed.

```python
before=len(df)
print(df.drop_duplicates(keep="first"))
after=len(df)
num_rows=before-after
print(before,after,before,num_rows )
```

## Cleaning

### 12. Fill nulls in a numeric column with the column mean; fill nulls in a text column with `"unknown"`.

```python
df["text_clear"]=df["text_clear"].fillna("unknown")
df["body"]=df["body"].fillna(df["body"].mean())
```

### 13. Strip whitespace and lowercase every value in a text column.

```python
print(df["body"]
      .str.strip()
      .str.lower())
```

### 14. Drop any column that's more than 50% null.

```python
null_percent = df.isnull().mean()

columns_to_drop = null_percent[null_percent > 0.5].index

df = df.drop(columns=columns_to_drop)

print("Dropped columns:", columns_to_drop.tolist())
```

### 15. Convert a column of strings like `"$1,200"` into a proper float column.

```python
df[amount]= (df[amount]
             .str.replace("$","",regex=False)
             .str.replace(",","",regex=False)
             .astype(float)
)
```

## Small report writing

### 16. Build a 5-column summary table: column name, dtype, null count, unique count, sample value.

```python
cols=["column name","dtype","null count","unique count","sample value"]
df[cols].describe()
```

### 17. Group by one categorical column and print count + mean of a numeric column per group.

```python
table = pd.DataFrame({

    "region": ["East", "North", "South", "West"],

    "count": [25, 18, 30, 22],

    "mean": [120.5, 98.2, 135.7, 110.4]

})

print(table)
#df.groupby("category")["numeric_col"].agg(["count", "mean"])
df.groupby("region")["sales"].agg(["count", "mean"])
```

### 18. Print the 3 most common values in a column with their counts and percentages.

```python
top3 = df["column"].value_counts().head(3).reset_index()

top3.columns = ["value", "count"]

top3["percentage"] = top3["count"] / len(df) * 100

print(top3)
```

### 19. Write a function `quick_report(df)` that combines the previous 3 drills into one printed report, called on any DataFrame.

```python
def quick_report(df, numeric_cols, group_col, value_col):

    

    # 1. Summary statistics for numeric columns

    print("=== SUMMARY STATISTICS ===")

    print(df[numeric_cols].describe())

    

    # 2. Count + mean by categorical group

    print("\n=== GROUP SUMMARY ===")

    group_summary = (

        df.groupby(group_col)[numeric_cols[0]]

          .agg(["count", "mean"])

          .reset_index()

    )

    print(group_summary)

    

    # 3. Top 3 most common values

    print("\n=== TOP 3 VALUES ===")

    top3 = df[value_col].value_counts().head(3).reset_index()

    top3.columns = ["value", "count"]

    top3["percentage"] = (

        top3["count"] / df[value_col].count() * 100

    )

    print(top3)
```

```python
quick_report(

    df,

    numeric_cols=["sales", "profit", "quantity", "price", "discount"],

    group_col="region",

    value_col="product"

)
```
