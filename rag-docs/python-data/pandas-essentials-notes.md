---
title: pandas essentials — study notes
topic: python-data
source_type: my-notes
note_kind: study-notes
---

# pandas Essentials — Study Notes

## Core objects

- **Series**: one labelled column.
- **DataFrame**: a table of Series sharing an index.

## Reading and writing

```python
df = pd.read_csv("sales.csv", parse_dates=["order_date"])
df = pd.read_json("events.json")
df = pd.read_excel("budget.xlsx", sheet_name="2025")
df.to_csv("clean.csv", index=False)
df.to_parquet("clean.parquet")      # compact, keeps types
```

## Viewing

`df.head()`, `df.tail()`, `df.shape`, `df.columns`, `df.dtypes`, `df.info()`, `df.describe()`, `df["region"].value_counts()`.

## Selecting

| Goal | Code |
| --- | --- |
| One column | `df["price"]` |
| Several columns | `df[["name", "price"]]` |
| Rows by label | `df.loc[5]`, `df.loc[df["price"] > 10, ["name", "price"]]` |
| Rows by position | `df.iloc[0:5]` |

`loc` uses labels (end inclusive); `iloc` uses integer positions (end exclusive).

## Filtering

```python
df[(df["region"] == "West") & (df["price"] > 10)]   # use & | ~ and brackets
df[df["region"].isin(["West", "East"])]
df.query("price > 10 and region == 'West'")
df[df["name"].str.contains("pro", case=False)]
```

## Changing values

```python
df["status"] = df["status"].replace({"Y": "yes", "N": "no"})
df["price"] = df["price"].astype(float)
df["total"] = df["price"] * df["qty"]
df = df.rename(columns={"qty": "quantity"})
df = df.drop(columns=["notes"])
```

## Sorting

`df.sort_values("price", ascending=False)`, `df.sort_values(["region", "price"])`, `df.sort_index()`.

## Missing data

```python
df.isna().sum()
df.dropna(subset=["price"])
df["price"].fillna(df["price"].median())
df["temp"].interpolate()     # fill gaps in ordered data from neighbours
df.ffill()                   # carry the last value forward
```

## Duplicates

`df.drop_duplicates()`, or by key with `subset=[...]` and `keep="first"/"last"`.

## Combining tables

```python
pd.merge(orders, customers, on="customer_id", how="left")   # SQL-style join
pd.concat([jan, feb], ignore_index=True)                    # stack rows
```

`how` = `inner`, `left`, `right`, `outer`. Check row counts after a merge — duplicate keys multiply rows.

## Grouping and aggregation

```python
df.groupby("region")["total"].sum()
df.groupby(["region", "product"]).agg(revenue=("total", "sum"), orders=("order_id", "count"))
df.pivot_table(index="region", columns="month", values="total", aggfunc="sum")
```

## Dates and time series

```python
df["order_date"] = pd.to_datetime(df["order_date"])
df["month"] = df["order_date"].dt.to_period("M")
daily = df.set_index("order_date")["total"].resample("D").sum()
weekly = df.set_index("order_date")["total"].resample("W").mean()
```

`resample` groups by time buckets; `rolling(7).mean()` gives moving averages.

## Statistics helpers

`cumsum`, `cumprod` (compounding growth), `pct_change`, `std`, `var`, `corr`, `cov`, `quantile`.

## Memory and speed

- `df.memory_usage(deep=True)` shows real memory use.
- Convert repeated text to `category`; downcast numbers (`int64` → `int32`) where safe.
- Read only the needed columns: `pd.read_csv(..., usecols=[...])`.
- Prefer vectorised operations over `apply` with Python functions and over row loops.
- For data that doesn't fit in memory, read in chunks (`chunksize=`) or use tools such as Polars, DuckDB or PySpark.
