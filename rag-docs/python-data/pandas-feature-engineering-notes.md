---
title: Feature engineering with pandas — study notes
topic: python-data
source_type: my-notes
note_kind: study-notes
---

# Feature Engineering with pandas — Study Notes

Feature engineering turns raw columns into inputs a model can learn from. The steps below are a typical order of work.

## 1. Look at distributions (box plots)

A box plot shows the median, the middle 50 % (the box, from Q1 to Q3) and points beyond the whiskers that may be outliers.

```python
import matplotlib.pyplot as plt
df.boxplot(column="price", by="category")
plt.show()
```

Use it to spot skewed columns and suspicious values before modelling.

## 2. Correlation

```python
corr = df.select_dtypes("number").corr()           # correlation matrix
corr["target"].sort_values(ascending=False)        # how each feature relates to the target
```

- Values range from -1 to 1; near 0 means no **linear** relationship (there may still be a non-linear one).
- Two features that are highly correlated with **each other** (e.g. > 0.9) carry similar information — consider dropping one.
- Correlation is not causation.

A heatmap (e.g. `seaborn.heatmap(corr, annot=True)`) makes the matrix easy to scan.

## 3. Outliers with the IQR rule

```python
q1, q3 = df["price"].quantile([0.25, 0.75])
iqr = q3 - q1
low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
outliers = df[(df["price"] < low) | (df["price"] > high)]
df["price_capped"] = df["price"].clip(low, high)    # cap instead of deleting
```

Decide per case: remove data-entry errors, but keep (or cap) real extreme values.

## 4. Missing values

- Drop rows only when few are missing and they're random: `df.dropna(subset=["age"])`.
- Fill numbers with the median (robust to outliers), categories with the mode or `"Unknown"`.
- Add a flag column (`df["age_missing"] = df["age"].isna()`) — sometimes "missing" is itself informative.
- Compute fill values on the **training data only**, then apply them to test data, to avoid leakage.

## 5. Binning

Turn a continuous number into ranges:

```python
df["age_group"] = pd.cut(df["age"], bins=[0, 18, 35, 60, 120], labels=["child", "young", "adult", "senior"])
df["income_band"] = pd.qcut(df["income"], q=4, labels=["Q1", "Q2", "Q3", "Q4"])   # equal-sized groups
```

`cut` uses fixed edges; `qcut` uses quantiles so each bin has about the same count.

## 6. Encoding categories

Models need numbers.

| Method | Code | When |
| --- | --- | --- |
| Label/ordinal encoding | `df["size"].map({"S": 0, "M": 1, "L": 2})` | Categories with a natural order |
| One-hot encoding | `pd.get_dummies(df, columns=["city"])` | No order, few categories |
| Category codes | `df["city"].astype("category").cat.codes` | Quick ids; tree models tolerate it |

Plain integer codes on unordered categories can mislead linear models into thinking "city 3 > city 1".

## 7. New features

- Ratios: `price_per_sqft = price / sqft`.
- Date parts: `df["dow"] = df["date"].dt.dayofweek`, month, is_weekend.
- Aggregates: average spend per customer via `groupby().transform("mean")`.
- Log transform for skewed values: `np.log1p(df["income"])`.

## 8. Sorting, saving and reloading

- Sort by time before creating lag features or splitting train/test chronologically.
- Save the processed data (`to_parquet` keeps types; `to_csv` is universal) so you don't repeat cleaning every run.

## Checklist

Distributions → correlations → outliers → missing values → binning/encoding → new features → save. Fit any statistics (medians, bins, encoders) on training data only.
