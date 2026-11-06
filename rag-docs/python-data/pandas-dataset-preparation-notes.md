---
title: Preparing a dataset with pandas — study notes
topic: python-data
source_type: my-notes
note_kind: study-notes
---

# Preparing a Dataset with pandas — Study Notes

Steps for turning a raw table into something clean enough to analyse or train on.

## 1. Inspect before changing anything

```python
df.shape            # rows, columns
df.info()           # column types and non-null counts
df.head()           # first rows
df.describe()       # numeric summaries
df.isna().sum()     # missing values per column
df.nunique()        # distinct values per column
```

Look for wrong types (numbers stored as text), unexpected nulls, and columns with one value only.

## 2. Stable IDs with hashing

If rows have no reliable id, build one from the content so the same row always gets the same id, across runs and machines:

```python
import hashlib

def stable_id(row):
    key = f"{row['title']}|{row['author']}|{row['date']}"
    return hashlib.sha256(key.encode()).hexdigest()[:12]

df["row_id"] = df.apply(stable_id, axis=1)
```

Python's built-in `hash()` is **not** suitable — it changes between runs for strings.

## 3. Duplicates

```python
df.duplicated().sum()                                   # exact duplicates
df = df.drop_duplicates()
df = df.drop_duplicates(subset=["email"], keep="first") # duplicates by key
```

Decide what "the same record" means before dropping anything.

## 4. Multi-value columns with `explode`

A column holding lists (e.g. `tags = ["sql", "python"]`) is hard to count. `explode` gives one row per element:

```python
df["tags"] = df["tags"].str.split(",")       # if stored as "sql,python"
tags = df.explode("tags")
tags["tags"] = tags["tags"].str.strip().str.lower()
tags["tags"].value_counts()
```

## 5. Cross-tabulation

`pd.crosstab` counts combinations of two categories; `normalize` turns counts into proportions:

```python
pd.crosstab(df["level"], df["passed"])                    # counts
pd.crosstab(df["level"], df["passed"], normalize="index") # share per row
```

`normalize="index"` makes each row sum to 1 — e.g. pass rate per level.

## 6. Sampling

```python
df.sample(n=100, random_state=42)        # fixed sample size
df.sample(frac=0.1, random_state=42)     # 10 %
df.groupby("level").sample(n=20, random_state=42)  # stratified sample
```

Setting `random_state` makes the sample reproducible.

## Checklist

1. Inspect shape, types, nulls.
2. Fix types and obvious errors.
3. Add stable ids.
4. Remove duplicates by a clear rule.
5. Explode list columns before counting.
6. Summarise with `value_counts`, `groupby`, `crosstab`.
7. Sample reproducibly.
