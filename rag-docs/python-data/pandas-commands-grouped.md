---
title: pandas-commands-grouped
topic: python-data
source_type: my-notes
source_file: pandas-commands-grouped.md
---

# 🐼 pandas Commands — Grouped Reference

> Built from the 19 pages under **Cornell Note taking Method → aitanner → notes** in Notion (pandas 3.0 user-guide pages you saved).
> Every command that showed up across those pages is pulled together here **by what it does**. When the same command appeared on several pages (for example `fillna` on Basics, Missing Data, Time Deltas and Cookbook), it's listed once, with all its variants side by side.
> All examples run on **one small support-ticket dataset** (defined once below) and were tested on pandas 3.0.

---

## Contents

0. [Source pages → sections](#0-source-pages--sections)
1. [One-page cheat sheet](#1-one-page-cheat-sheet)
2. [Shared example data](#2-shared-example-data)
3. [Create objects](#3-create-objects)
4. [Inspect & summarize](#4-inspect--summarize)
5. [Select & filter](#5-select--filter)
6. [Add, change, rename, drop columns & labels](#6-add-change-rename-drop-columns--labels)
7. [Missing data (NaN / NA / NaT)](#7-missing-data-nan--na--nat)
8. [Duplicates](#8-duplicates)
9. [Data types & conversion](#9-data-types--conversion)
10. [Math, stats, comparison & binning](#10-math-stats-comparison--binning)
11. [Applying functions: `pipe` / `apply` / `agg` / `transform` / `map`](#11-applying-functions)
12. [Text: the `.str` accessor](#12-text-the-str-accessor)
13. [Dates & times: `Timestamp`, `.dt`, offsets, time zones, `Period`](#13-dates--times)
14. [Time deltas](#14-time-deltas)
15. [GroupBy (split → apply → combine)](#15-groupby)
16. [Window functions: `rolling` / `expanding` / `ewm`](#16-window-functions)
17. [Resampling time series](#17-resampling)
18. [Reshape: pivot, melt, stack, dummies, explode, crosstab](#18-reshape)
19. [Combine: concat, merge, join, merge_asof, compare](#19-combine)
20. [Iterating (and why to avoid it)](#20-iterating)
21. [Read & write files / databases (IO)](#21-io)
22. [Plotting](#22-plotting)
23. [Table styling (`.style`)](#23-table-styling)
24. [Options & display settings](#24-options--display-settings)
25. [Same command, many places](#25-same-command-many-places)
26. [Parameters that mean the same thing everywhere](#26-shared-parameters)
27. [Look-alike commands that are NOT the same](#27-look-alikes)
28. [Top resources with reasoning](#28-top-resources-with-reasoning)

---

## 0. Source pages → sections

| # | Notion page | Feeds sections |
|---|---|---|
| 1 | Essential basic functionality | 4, 6, 9, 10, 11, 12, 13, 20 |
| 2 | Indexing and selecting data | 5, 6, 8 |
| 3 | IO tools (text, CSV, HDF5, …) | 21 |
| 4 | Merge, join, concatenate and compare | 19 |
| 5 | Reshaping and pivot tables | 10 (`cut`), 18 |
| 6 | Working with text data | 12 |
| 7 | Working with text data *(duplicate of #6 — same content, safe to delete one)* | 12 |
| 8 | Working with missing data | 7 |
| 9 | Duplicate Labels | 8 |
| 10 | Nullable integer data type | 7, 9 |
| 11 | Nullable Boolean data type | 7, 9 |
| 12 | Group by: split-apply-combine | 15 |
| 13 | Chart visualization | 22 |
| 14 | Table Visualization | 23 |
| 15 | Windowing operations | 16 |
| 16 | Time series / date functionality | 13, 17 |
| 17 | Time deltas | 14 |
| 18 | Options and settings | 24 |
| 19 | Cookbook | 5, 6, 15, 18, 21 (recipes) |

---

## 1. One-page cheat sheet

| Task | Command(s) | SQL / PySpark mental model |
|---|---|---|
| Peek | `df.head()` · `df.tail(3)` · `df.sample(5)` | `LIMIT` |
| Shape & types | `df.shape` · `df.dtypes` · `df.info()` | `DESCRIBE` |
| Summary stats | `df.describe(include="all")` | — |
| Count values | `s.value_counts()` · `df.value_counts([cols])` · `s.nunique()` | `GROUP BY … COUNT(*)` |
| Pick columns | `df["a"]` · `df[["a","b"]]` | `SELECT a, b` |
| Pick by label | `df.loc[rows, cols]` *(end inclusive)* | — |
| Pick by position | `df.iloc[0:5, 0:3]` *(end exclusive)* | — |
| One cell fast | `df.at[label, col]` · `df.iat[i, j]` | — |
| Filter rows | `df[mask]` · `df.loc[mask, cols]` · `df.query("a > 1")` | `WHERE` |
| Membership | `s.isin([...])` · `~s.isin([...])` | `IN` / `NOT IN` |
| Conditional value | `np.where(cond, a, b)` · `np.select(conds, choices)` · `s.where()` / `s.mask()` | `CASE WHEN` / `F.when` |
| New column | `df["c"] = …` · `df.assign(c=…)` | `withColumn` |
| Rename / drop | `df.rename(columns={…})` · `df.drop(columns=[…])` | `withColumnRenamed` / `drop` |
| Index | `df.set_index("k")` · `df.reset_index()` · `df.reindex([...])` | — |
| Missing | `isna` · `dropna` · `fillna` · `ffill/bfill` · `interpolate` · `replace` | `COALESCE` / `fillna` |
| Duplicates | `duplicated` · `drop_duplicates(subset, keep)` | `DISTINCT` / `dropDuplicates` |
| Types | `astype` · `to_numeric` · `to_datetime` · `convert_dtypes` · `select_dtypes` | `CAST` |
| Sort / top-N | `sort_values` · `sort_index` · `nlargest` · `nsmallest` | `ORDER BY … LIMIT` |
| Bin | `pd.cut` (fixed edges) · `pd.qcut` (quantiles) | `CASE` / `ntile` |
| Text | `s.str.strip/lower/contains/replace/split/get_dummies` | `TRIM/LOWER/LIKE/REGEXP_REPLACE` |
| Dates | `s.dt.date/hour/day_name()/to_period()` · `pd.offsets.*` | `date_trunc` / `date_format` |
| Group | `df.groupby(k).agg(name=(col, func))` | `GROUP BY` |
| Group → same shape | `groupby(k)[c].transform("mean")` | window `AVG() OVER (PARTITION BY k)` |
| Moving window | `rolling(3)` · `expanding()` · `ewm(span=3)` | `ROWS BETWEEN 2 PRECEDING` |
| Time buckets | `resample("D")` · `pd.Grouper(key, freq)` | `date_trunc` + `GROUP BY` |
| Wide ↔ long | `pivot` · `pivot_table` · `melt` · `stack/unstack` | `PIVOT` / `UNPIVOT` (`stack()` in Spark) |
| One-hot | `pd.get_dummies` · `s.str.get_dummies("|")` | — |
| List → rows | `explode` | `explode` |
| Stack tables | `pd.concat([a, b])` | `UNION ALL` |
| Join | `a.merge(b, on, how)` · `a.join(b)` | `JOIN` |
| Nearest-time join | `pd.merge_asof` | as-of join |
| Read / write | `pd.read_*` ↔ `df.to_*` (csv, json, parquet, excel, sql, pickle…) | `spark.read` / `df.write` |
| Display | `pd.set_option("display.max_columns", None)` · `pd.option_context(...)` | — |

---

## 2. Shared example data

Every example below uses this frame. Run it once first.

```python
import numpy as np
import pandas as pd

tickets = pd.DataFrame(
    {
        "ticket_id": [101, 102, 103, 104, 105, 106, 107, 108],
        "team": ["billing", "tech", "tech", "billing", "sales", "tech", "billing", None],
        "priority": ["high", "low", "high", "medium", "low", "high", "low", "medium"],
        "opened": pd.to_datetime([
            "2026-01-03 09:15", "2026-01-03 11:40", "2026-01-04 08:05", "2026-01-05 14:30",
            "2026-01-05 16:10", "2026-01-06 10:00", "2026-01-07 13:45", "2026-01-07 15:20",
        ]),
        "hours_to_close": [4.5, 30.0, np.nan, 12.0, 2.0, 48.0, 6.5, np.nan],
        "tags": ["refund|urgent", "login", "outage|urgent", "invoice", "demo", "outage", "refund", "login|sso"],
        "customer": [" Acme Corp", "globex ", "Initech", "acme corp", "Umbrella", "Globex", "Initech ", "umbrella"],
    }
)
```

> Real-world shape: one row per support ticket, messy customer names, a missing team, missing close times, and multi-value tags — the same mess you clean in a bronze → silver step.

---

## 3. Create objects

| Command | What it makes | Seen in |
|---|---|---|
| `pd.Series(data, index=, name=, dtype=)` | 1-D labeled array | Basics, Indexing, Text, Missing |
| `pd.DataFrame(dict / 2-D array, index=, columns=)` | 2-D table | every page |
| `pd.Index([...], name=, dtype=)` | Labels object (rows/columns) | Indexing |
| `pd.MultiIndex.from_tuples / from_arrays / from_product` | Hierarchical labels | Basics, Reshaping, GroupBy, Merge |
| `pd.array([...], dtype="Int64" / "boolean" / "string")` | Nullable extension array | Nullable int/bool, Missing |
| `pd.Categorical(values, categories=, ordered=)` | Fixed set of labels | Reshaping, GroupBy |
| `pd.date_range` · `pd.bdate_range` · `pd.period_range` · `pd.timedelta_range` | Ranges of times | Time series, Time deltas |
| `pd.Timestamp` · `pd.Period` · `pd.Timedelta` | Single time values | Time series, Time deltas |
| `df.copy()` | Independent copy | Basics, Indexing |

```python
s = pd.Series([4.5, 30.0, None], index=["a", "b", "c"], name="hours")
labels = pd.Index(["x", "y"], name="key")
nullable_ints = pd.array([1, None, 3], dtype="Int64")              # keeps ints, missing = <NA>
mi = pd.MultiIndex.from_product([["tech", "billing"], ["high", "low"]], names=["team", "priority"])
days = pd.date_range("2026-01-01", periods=7, freq="D")
workdays = pd.bdate_range("2026-01-01", periods=5)                  # skips weekends
sizes = pd.Categorical(["low", "high", "low"], categories=["low", "medium", "high"], ordered=True)
```

---

## 4. Inspect & summarize

| Command | Use | Seen in |
|---|---|---|
| `head(n)` · `tail(n)` | First/last n rows (default 5) | Basics, Cookbook, GroupBy |
| `shape` · `dtypes` · `columns` · `index` · `empty` | Metadata | Basics, Indexing |
| `info()` | Columns, non-null counts, dtypes, memory | Options |
| `describe(percentiles=, include=, exclude=)` | Summary stats (numeric by default; `include="all"` for everything) | Basics, GroupBy |
| `value_counts()` (Series or DataFrame; `subset=`) | Frequency table | Basics, IO |
| `nunique()` · `unique()` · `mode()` | Distinct count / values / most common | Basics, GroupBy |
| `memory_usage()` | Bytes per column | Options (`display.memory_usage`) |

```python
tickets.head(3)
tickets.shape                     # (8, 7)
tickets.dtypes
tickets.info()
tickets.describe()                # numeric columns
tickets.describe(include="all")   # every column
tickets["priority"].value_counts()
tickets.value_counts(["team", "priority"])          # combinations
tickets["team"].nunique(), tickets["team"].unique()
tickets["priority"].mode()
tickets.empty
```

---

## 5. Select & filter

### 5.1 The four indexers

| Indexer | Selects by | Slice end | Raises | Seen in |
|---|---|---|---|---|
| `df[...]` | column name(s); a slice selects **rows**; a boolean mask filters rows | — | `KeyError` | Indexing, Duplicates |
| `df.loc[rows, cols]` | **labels** (or boolean mask / callable) | **inclusive** | `KeyError` | Indexing, Cookbook, Missing |
| `df.iloc[rows, cols]` | **integer positions** (or boolean *array*) | exclusive | `IndexError` | Indexing, Cookbook |
| `df.at[label, col]` · `df.iat[i, j]` | one scalar, fastest | — | — | Indexing |

### 5.2 Filtering tools

| Command | Use | Seen in |
|---|---|---|
| `df[mask]` with `&` `|` `~` (wrap each condition in `( )`) | Boolean filter | Indexing, Cookbook |
| `s.isin(list or dict)` · `index.isin()` | Membership | Indexing, Cookbook |
| `df.query("a < b and c in ['x', 'y']")` · `@var` for Python variables | SQL-like string filter | Indexing |
| `s.where(cond, other)` | Keep where True, replace elsewhere (same shape) | Indexing, Missing, Cookbook |
| `s.mask(cond, other)` | Replace where True (inverse of `where`) | Indexing |
| `np.where(cond, a, b)` · `np.select(conds, choices, default)` | Build values from conditions | Indexing, Cookbook |
| `df.loc[lambda d: …]` | Filter inside a method chain | Indexing |
| `df.get(key, default)` | Dict-style safe get | Indexing |
| `df.xs(key, level=)` | Cross-section of a MultiIndex | Indexing, Cookbook |
| `df.sample(n= / frac=, replace=, weights=, random_state=)` | Random rows | Indexing |
| `df.nlargest(n, col)` · `df.nsmallest(n, col)` | Top/bottom N | Basics |
| `df.truncate(before=, after=)` | Slice a sorted index | Time series |
| `idx.get_loc()` · `idx.get_indexer()` | Label → position | Indexing |

```python
tickets["team"]                                  # Series
tickets[["team", "priority"]]                    # DataFrame
tickets.loc[0:2, "team":"priority"]              # labels, END INCLUDED (rows 0,1,2)
tickets.iloc[0:2, 0:3]                           # positions, end excluded (rows 0,1)
tickets.at[0, "team"], tickets.iat[0, 1]

slow_high = tickets[(tickets["priority"] == "high") & (tickets["hours_to_close"] > 10)]
not_tech = tickets[~tickets["team"].isin(["tech"])]
q = tickets.query("priority == 'high' and hours_to_close > 10")
limit = 10
q2 = tickets.query("hours_to_close > @limit")    # @ = Python variable

capped = tickets["hours_to_close"].mask(tickets["hours_to_close"] > 24, 24)
kept = tickets["hours_to_close"].where(tickets["hours_to_close"] < 24)   # others -> NaN
chained = tickets.loc[lambda d: d["hours_to_close"] > 10, ["ticket_id", "hours_to_close"]]
tickets.get("not_a_column", default="missing")
tickets.sample(n=3, random_state=1)
tickets.nlargest(3, "hours_to_close")
```

> ⚠️ pandas 3 uses **Copy-on-Write**: `df[df.a > 1]["b"] = 0` (chained assignment) never changes `df`. Always write `df.loc[df.a > 1, "b"] = 0`.

---

## 6. Add, change, rename, drop columns & labels

| Command | Use | Seen in |
|---|---|---|
| `df["new"] = …` · `df.loc[mask, "col"] = …` | Create / conditional update | Indexing, Cookbook |
| `df.assign(new=…, other=lambda d: …)` | Add columns inside a chain | Basics, Reshaping |
| `df.insert(pos, name, value)` | Add at a position | Basics |
| `df.rename(columns={…}, index={…})` · `rename(str.upper)` | Rename labels | Basics, GroupBy, Duplicates |
| `df.rename_axis(...)` · `idx.set_names` · `idx.rename` | Rename index **names** (not labels) | Basics, Indexing |
| `df.drop(columns=[…])` · `df.drop([rows], axis=0)` | Remove labels | Basics |
| `df.set_index(col or [cols])` · `df.reset_index(drop=)` | Column ↔ index | Indexing, Merge, Cookbook |
| `df.reindex(labels / index= / columns=, method=, fill_value=)` | Conform to new labels (adds NaN for new ones) | Basics, Indexing, Missing |
| `df.reindex_like(other)` · `a.align(b, join=)` | Match another object's labels | Basics |
| `df.sort_values(by, ascending=)` · `df.sort_index()` | Order rows | Basics, Cookbook, Indexing |
| `df.T` / `df.transpose()` | Swap rows/columns | Basics |
| `df.columns = df.columns.str.strip().str.lower()` | Clean all column names | Text |

```python
t = tickets.copy()
t["sla_breached"] = t["hours_to_close"] > 24
t = t.assign(
    opened_day=t["opened"].dt.day_name(),
    hours_x2=lambda d: d["hours_to_close"] * 2,
)
t["speed"] = np.where(t["hours_to_close"] > 24, "slow", "fast")
t["level"] = np.select(
    [t["priority"].eq("high"), t["priority"].eq("medium")], [3, 2], default=1
)
t.loc[t["team"].isna(), "team"] = "unassigned"
t.insert(1, "source", "email")
t = t.rename(columns={"hours_to_close": "hrs"}).drop(columns=["hours_x2"])
t = t.set_index("ticket_id").sort_index(ascending=False).reset_index()
t.reindex(columns=["ticket_id", "team", "new_col"])          # new_col filled with NaN
t.sort_values(["team", "hrs"], ascending=[True, False])
```

---

## 7. Missing data (NaN / NA / NaT)

### 7.1 Which "missing" you get

| Sentinel | Used by | Compare with `==`? |
|---|---|---|
| `np.nan` | float, `str` dtype, object | `nan == nan` → `False` |
| `pd.NaT` | datetime, timedelta, period | `NaT == NaT` → `False` |
| `pd.NA` | nullable `Int64`, `Float64`, `boolean`, `string`, pyarrow | `NA == NA` → `<NA>` (3-valued logic) |

**Always test with `isna()` / `notna()`**, never `== np.nan`.

### 7.2 Commands

| Command | Use | Seen in |
|---|---|---|
| `isna()` · `notna()` (also `pd.isna(x)`) | Detect | Missing, Basics |
| `dropna(axis=, how="any"/"all", subset=, thresh=)` | Remove rows/cols | Missing, GroupBy |
| `fillna(value / dict / Series)` | Fill with value(s) | Missing, Basics, Time deltas, Nullable bool |
| `ffill(limit=)` · `bfill()` | Carry last/next value | Missing, Basics, Cookbook |
| `interpolate(method="linear"/"time"/"values"/…, limit=, limit_direction=, limit_area=)` | Estimate from neighbors | Missing, Basics |
| `replace(to_replace, value, regex=)` | Swap values (incl. to/from NaN) | Missing |
| `convert_dtypes()` | Switch to nullable dtypes that keep ints as ints | Missing |
| `combine_first(other)` | Fill holes from another frame | Basics, Merge |
| `add(other, fill_value=0)` | Arithmetic treating one-sided NaN as 0 | Basics |
| `sum(skipna=False)` · `cumsum(skipna=False)` | Let NaN propagate | Basics, Missing |
| `mask.fillna(True)` | Decide how `NA` behaves in a boolean filter | Nullable bool |

```python
tickets.isna().sum()                                     # missing per column
tickets.dropna(subset=["hours_to_close"])
tickets.dropna(axis=1)                                   # drop columns with any NaN
h = tickets["hours_to_close"]
h.fillna(h.median())
tickets.fillna({"team": "unassigned", "hours_to_close": 0})
h.ffill(), h.bfill(), h.interpolate()
tickets.replace({"priority": {"medium": "med"}})
tickets.replace(r"^\s+|\s+$", "", regex=True)            # trim strings everywhere
tickets.convert_dtypes().dtypes                          # Int64 / string / boolean / Float64
pd.Series([1, None], dtype="Int64")                      # 1, <NA>  (stays integer)

primary = pd.Series([1.0, np.nan, 3.0])
backup = pd.Series([9.0, 2.0, 9.0])
primary.combine_first(backup)                            # 1, 2, 3
```

> Engineering tip: decide **why** a value is missing before filling. Fill close-time with 0 and your SLA dashboard says tickets were closed instantly.

---

## 8. Duplicates

| Command | Use | Seen in |
|---|---|---|
| `df.duplicated(subset=, keep="first"/"last"/False)` | Boolean flag per row | Indexing |
| `df.drop_duplicates(subset=, keep=)` | Remove duplicate rows | Indexing |
| `df.index.duplicated(keep=)` → `df[~mask]` | Duplicate **labels** | Indexing, Duplicates |
| `df.index.is_unique` · `df.columns.is_unique` | Quick check | Duplicates |
| `df.groupby(level=0).first()` / `.mean()` | Resolve duplicate labels by rule | Duplicates |
| `df.set_flags(allows_duplicate_labels=False)` · `df.flags` | Make pandas raise if duplicates appear later | Duplicates |

```python
clean_customer = tickets["customer"].str.strip().str.lower()
clean_customer.duplicated()
deduped = tickets.assign(customer=clean_customer).drop_duplicates(subset=["customer"], keep="last")
tickets.duplicated(subset=["team"], keep=False)          # True for EVERY member of a dup group

s = pd.Series([1, 2, 3], index=["a", "a", "b"])
s.index.is_unique                                        # False
s[~s.index.duplicated()]                                 # keep first label
s.groupby(level=0).sum()                                 # or combine them

guarded = deduped.set_flags(allows_duplicate_labels=False)   # later ops that create dup labels raise
```

---

## 9. Data types & conversion

| Command | Use | Seen in |
|---|---|---|
| `astype(dtype or {col: dtype})` | Cast | Basics, Text, Nullable int, Time deltas |
| `convert_dtypes()` | Best nullable dtypes automatically | Missing |
| `pd.to_numeric(s, errors="coerce")` | Text → numbers, bad → NaN | IO |
| `pd.to_datetime(s, format=, errors=, dayfirst=, unit=, utc=)` | Text/epoch → datetime | IO, Time series, Reshaping |
| `pd.to_timedelta(s, unit=)` | Text/numbers → durations | Time deltas |
| `dtype="category"` · `pd.CategoricalDtype(cats, ordered=True)` | Low-cardinality labels | IO, GroupBy |
| `dtype="str"` (default, NaN) vs `"string"` (pd.NA) | Text dtypes in pandas 3 | Text |
| `"Int64"` · `"Float64"` · `"boolean"` (capitalised = nullable) | Keep ints/bools with missing values | Nullable int/bool |
| `select_dtypes(include=, exclude=)` | Pick columns by type | Basics, Text |
| `to_numpy(dtype=)` · `.array` | Get the underlying values (avoid `.values`) | Basics |
| `infer_objects()` | Re-infer object columns | Basics |

```python
tickets["hours_to_close"].astype("Float64")
priority_type = pd.CategoricalDtype(["low", "medium", "high"], ordered=True)
pri = tickets["priority"].astype(priority_type)
pri.sort_values()                                     # low < medium < high, not alphabetical
pri > "low"                                           # ordered comparisons work

pd.to_numeric(pd.Series(["1", "2", "x"]), errors="coerce")        # 1, 2, NaN
pd.to_datetime(pd.Series(["2026-01-03", "bad"]), errors="coerce") # 2026-01-03, NaT
pd.to_datetime(pd.Series(["03/01/2026"]), dayfirst=True)          # 3 Jan
pd.to_datetime([1767225600], unit="s")                            # epoch seconds
pd.to_timedelta(["1 days", "4h"])

tickets.select_dtypes(include="number")
tickets.select_dtypes(exclude=["number", "datetime"])
tickets["hours_to_close"].to_numpy()
```

---

## 10. Math, stats, comparison & binning

| Group | Commands | Seen in |
|---|---|---|
| Reductions | `sum mean median min max std var count prod quantile` (all take `axis=`, `skipna=`, `numeric_only=`) | Basics, Missing, GroupBy, Time deltas |
| Cumulative | `cumsum cumprod cummax cummin` | Basics, Missing, GroupBy |
| Row-to-row | `diff()` · `pct_change()` · `shift(n)` · `rank()` | GroupBy, Time series, Cookbook |
| Position of extreme | `idxmin()` · `idxmax()` | Basics, Time deltas, Cookbook |
| Flexible arithmetic | `add sub mul div floordiv mod pow` + `radd…` (`axis=`, `fill_value=`, `level=`) · `divmod()` | Basics |
| Flexible comparison | `eq ne lt gt le ge` | Basics |
| Boolean reduce | `any()` · `all()` · `empty` | Basics, Indexing |
| Equality | `a.equals(b)` (treats NaN==NaN) | Basics |
| Rounding/limits | `round(n)` · `clip(lower, upper)` · `abs()` | Options, Time deltas |
| Correlation | `corr(method=)` · `cov()` · `corrwith()` | Cookbook, Window |
| Binning | `pd.cut(x, bins, labels=)` (fixed edges) · `pd.qcut(x, q)` (equal-size groups) | Basics, Reshaping, Cookbook |
| Encoding | `pd.factorize(x)` → codes, uniques | Reshaping |

```python
h = tickets["hours_to_close"]
h.sum(), h.mean(), h.median(), h.std(), h.quantile(0.9)
h.sum(skipna=False)                       # NaN because some values are missing
h.cumsum(), h.diff(), h.shift(1), h.rank()
h.idxmax()                                # row label of the slowest ticket
h.add(1, fill_value=0)
h.gt(10)
h.clip(upper=24).round(0)
(tickets[["hours_to_close"]] > 0).all()
h.equals(h.copy())                        # True even with NaNs

pd.cut(h, bins=[0, 8, 24, np.inf], labels=["same day", "next day", "slow"])
pd.qcut(h, q=2, labels=["fast half", "slow half"])
codes, uniques = pd.factorize(tickets["priority"])
tickets[["ticket_id", "hours_to_close"]].corr()
```

---

## 11. Applying functions

These five come up on Basics, GroupBy, Window, Time series, Missing, Cookbook — **same names, same rules**.

| Command | Function receives | Output shape | Use when |
|---|---|---|---|
| `df.pipe(f, *args)` | the whole DataFrame | whatever `f` returns | Chain your own table-level steps |
| `df.apply(f, axis=0/1)` | each column (0) or row (1) as a Series | reduced or same | Custom logic per column/row (slow on rows) |
| `df.agg(func / [funcs] / {col: funcs})` (`aggregate`) | each column | **reduced** (one value per col/func) | Summaries |
| `df.transform(func / [funcs] / {col: func})` | each column | **same shape** as input | Normalising, filling, ranking |
| `s.map(dict / Series / func)` · `df.map(func)` | each **element** | same shape | Lookups, value recoding |

```python
def flag_sla(df, limit):
    return df.assign(sla_breached=df["hours_to_close"] > limit)

tickets.pipe(flag_sla, limit=24)

tickets[["ticket_id", "hours_to_close"]].apply(lambda col: col.max() - col.min())
tickets.apply(lambda row: f"{row['team']}-{row['priority']}", axis=1)

tickets["priority"].map({"low": 1, "medium": 2, "high": 3})        # lookup table
tickets[["hours_to_close"]].map(lambda v: round(v) if pd.notna(v) else v)   # DataFrame.map (was applymap)

tickets["hours_to_close"].agg(["min", "max", "mean"])
tickets.agg({"hours_to_close": ["mean", "max"], "ticket_id": "count"})

tickets["hours_to_close"].transform(lambda x: x / x.max())          # same length as input
tickets[["hours_to_close"]].transform(["abs", "sqrt"])
```

---

## 12. Text: the `.str` accessor

Works on Series **and** on `df.columns` / any Index. Missing values are skipped automatically.

| Group | Commands | Seen in |
|---|---|---|
| Case & spaces | `lower upper title capitalize swapcase strip lstrip rstrip` | Text, Basics |
| Length & slicing | `len()` · `str[0]` · `str[1:3]` · `str.get(i)` · `slice()` | Text |
| Search (→ bool) | `contains(pat, case=, regex=, na=)` · `match` (anchored at start) · `fullmatch` (whole string) · `startswith` · `endswith` | Text, Indexing |
| Replace | `replace(pat, repl, regex=, case=)` · `removeprefix` · `removesuffix` | Text, Basics |
| Split | `split(sep, n=, expand=)` · `rsplit` | Text, Reshaping, Basics |
| Join | `cat(others, sep=, na_rep=, join=)` | Text |
| Extract | `extract(r"(group)")` · `extractall` · `findall` *(not in your saved copy — the page skips that section)* | — |
| Count/test | `count(pat)` · `isdigit` · `isalpha` · … | Text |
| Indicators | `str.get_dummies(sep="|")` | Text, Reshaping |

```python
c = tickets["customer"]
c.str.strip().str.lower().str.title()          # " Acme Corp" -> "Acme Corp"
c.str.contains("acme", case=False)
c.str.strip().str.startswith("G")
c.str.len()

tags = tickets["tags"]
tags.str.split("|")                            # lists
tags.str.split("|", expand=True)               # one column per piece
tags.str.split("|").str[0]                     # first tag
tags.str.get_dummies(sep="|")                  # one-hot per tag
tags.str.contains("urgent")

c.str.strip().str.replace(r"\s+corp$", "", case=False, regex=True)
pd.Series(["$1,200", "$75"]).str.replace("$", "", regex=False).str.replace(",", "")
c.str.strip().str.cat(sep=", ")                # one combined string
pd.Series(["TKT-101", "TKT-202"]).str.extract(r"TKT-(\d+)")

messy = pd.DataFrame(columns=[" Ticket ID ", "Team Name "])
messy.columns = messy.columns.str.strip().str.lower().str.replace(" ", "_")
```

> `str.match` vs `str.contains` vs `str.fullmatch` = `re.match` vs `re.search` vs `re.fullmatch`.

---

## 13. Dates & times

### 13.1 Commands

| Group | Commands | Seen in |
|---|---|---|
| Create | `pd.Timestamp` · `pd.to_datetime` · `pd.date_range(start, end, periods, freq)` · `pd.bdate_range` · `pd.DatetimeIndex` | Time series, Basics |
| `.dt` parts | `date time year month day hour minute second dayofweek day_name() month_name() quarter is_month_end isocalendar()` | Basics, Time series |
| `.dt` transforms | `strftime(fmt)` · `normalize()` · `floor/ceil/round(freq)` · `to_period(freq)` | Basics, Time series |
| Time zones | `tz_localize(tz)` (attach) · `tz_convert(tz)` (move) · `tz=` in constructors · `utc=True` in `to_datetime` | Basics, Time series, IO |
| Offsets | `pd.offsets.Day/BDay/Hour/Minute/Week(weekday=)/MonthEnd/MonthBegin/QuarterEnd/YearEnd/BusinessHour/CustomBusinessDay` · `pd.DateOffset(months=2)` · `rollforward/rollback` | Time series, Time deltas |
| Frequency aliases | `"D" "B" "h" "min" "s" "W-MON" "MS" "ME" "QS" "QE" "YS" "YE"` | Time series, Window |
| Index slicing | `ts.loc["2026-01"]` · `ts.loc["2026-01-04":"2026-01-06"]` · `between_time` · `at_time` · `truncate` | Time series |
| Shift | `shift(n)` · `shift(freq="1D")` | Time series, Cookbook |
| Periods | `pd.Period` · `pd.period_range` · `to_period()` / `to_timestamp()` · `asfreq` | Time series |
| Holidays | `USFederalHolidayCalendar` · `CustomBusinessDay(calendar=)` | Time series |

```python
o = tickets["opened"]
o.dt.date, o.dt.hour, o.dt.day_name(), o.dt.month
o.dt.strftime("%Y-%m-%d")
o.dt.floor("D")
o.dt.to_period("W")
o.dt.tz_localize("America/New_York").dt.tz_convert("UTC")

pd.Timestamp("2026-01-02") + pd.offsets.BDay(2)          # skips the weekend -> Tue 6 Jan
pd.Timestamp("2026-01-15") + pd.offsets.MonthEnd(0)       # snap to month end
pd.Timestamp("2026-01-15") + pd.DateOffset(months=2)
pd.date_range("2026-01-01", periods=4, freq="W-MON")

ts = tickets.set_index("opened")["hours_to_close"]
ts.loc["2026-01-05"]                                      # every row on that day
ts.loc["2026-01-04":"2026-01-06"]
ts.between_time("09:00", "12:00")
ts.truncate(before="2026-01-04")
ts.shift(1)

pd.Period("2026-01", freq="M").asfreq("D", how="end")     # 2026-01-31
pd.period_range("2026-01", periods=3, freq="M")
```

> `tz_localize` says *"these times were recorded in X"*; `tz_convert` says *"show the same instant in Y"*. Localize once, convert as often as you like.

---

## 14. Time deltas

| Command | Use | Seen in |
|---|---|---|
| `pd.Timedelta("1 days 2 hours")` · `pd.Timedelta(hours=4.5)` · `pd.Timedelta(1, unit="D")` | One duration | Time deltas, Time series |
| `pd.to_timedelta(values, unit=)` | Many durations | Time deltas |
| `datetime - datetime` · `datetime + timedelta` | Durations & shifted times | Time deltas |
| `.dt.days` · `.dt.seconds` · `.dt.total_seconds()` · `.dt.components` | Parts | Time deltas, Basics |
| `td / pd.Timedelta(hours=1)` · `td // pd.Timedelta(days=1)` · `td.astype("timedelta64[s]")` | Convert units | Time deltas |
| `pd.timedelta_range` · `pd.TimedeltaIndex` | Ranges / index | Time deltas |
| `fillna(pd.Timedelta(0))` · `mean/median/sum` | Missing & stats | Time deltas |

```python
closed = tickets["opened"] + pd.to_timedelta(tickets["hours_to_close"], unit="h")
dur = closed - tickets["opened"]
dur / pd.Timedelta(hours=1)          # back to hours as floats
dur.dt.total_seconds()
dur.dt.components                    # days, hours, minutes, … as columns
dur.fillna(pd.Timedelta(0))
dur.mean(), dur.max()
pd.timedelta_range("0 days", periods=3, freq="12h")
```

---

## 15. GroupBy

### 15.1 The three patterns

| Pattern | Returns | Commands | SQL analogue |
|---|---|---|---|
| **Aggregate** | one row per group | `sum mean count size nunique min max first last describe` · `agg(...)` | `GROUP BY` |
| **Transform** | same rows as input | `transform(...)` · `cumsum cumcount rank diff shift` · `ffill` | window `OVER (PARTITION BY …)` |
| **Filter** | subset of rows | `filter(func)` · `head(n)` · `tail(n)` · `nth(n)` | `QUALIFY` / `HAVING` |

### 15.2 Commands

| Command | Use | Seen in |
|---|---|---|
| `df.groupby(by, as_index=, sort=, dropna=, observed=, group_keys=)` | Make groups (`by` = column(s), Series, function, `level=`, `pd.Grouper`) | GroupBy, Duplicates, Cookbook |
| `g.agg(new=("col", "func"), …)` (named aggregation) · `pd.NamedAgg` | Clean output column names | GroupBy, Cookbook |
| `g.agg({"col": ["sum", "mean"]})` | Different funcs per column | GroupBy |
| `g.size()` vs `g.count()` | Rows per group vs non-null per column | GroupBy |
| `g.groups` · `len(g)` · `g.get_group(key)` · `for name, grp in g` | Inspect groups | GroupBy |
| `g.apply(f)` · `g.pipe(f)` | Free-form per group / whole-groupby step | GroupBy, Cookbook |
| `g.ngroup()` · `g.cumcount()` | Number groups / rows in group | GroupBy |
| `g.rolling(n)` · `g.expanding()` · `g.resample(freq)` | Windows per group | GroupBy, Window |
| `pd.Grouper(key=, freq=, level=)` | Group by time buckets | GroupBy, Reshaping |
| `groupby(...).boxplot()` | Plot per group | GroupBy, Charts |

```python
g = tickets.groupby("team")                      # team=None row is dropped (dropna=True)
g.size()
g["hours_to_close"].mean()
summary = g.agg(
    tickets=("ticket_id", "count"),
    avg_hours=("hours_to_close", "mean"),
    worst=("hours_to_close", "max"),
)
tickets.groupby(["team", "priority"], dropna=False).size()     # keep the None team
tickets.groupby("team", as_index=False)["hours_to_close"].sum()  # flat output, no index

t = tickets.copy()
t["team_avg"] = t.groupby("team")["hours_to_close"].transform("mean")
t["vs_team"] = t["hours_to_close"] - t["team_avg"]
t["nth_in_team"] = t.groupby("team").cumcount()
t["team_rank"] = t.groupby("team")["hours_to_close"].rank(ascending=False)

busy = tickets.groupby("team").filter(lambda d: len(d) >= 3)    # only teams with 3+ tickets
first_per_team = tickets.sort_values("opened").groupby("team").head(1)
tickets.groupby("team").get_group("tech")
spread = g["hours_to_close"].apply(lambda s: s.max() - s.min())
daily_counts = tickets.groupby(pd.Grouper(key="opened", freq="D")).size()
for team, rows in g:
    pass  # rows is a DataFrame for that team
```

---

## 16. Window functions

| Command | Window | Seen in |
|---|---|---|
| `rolling(window=n or "2D", min_periods=, center=, closed=, win_type=)` | Fixed size or time span, sliding | Window, GroupBy, Cookbook, Basics |
| `expanding(min_periods=)` | From the start to now | Window, GroupBy |
| `ewm(span= / com= / halflife= / alpha=, adjust=)` | Exponentially weighted | Window |
| then `.mean() .sum() .std() .min() .max() .count() .median() .quantile() .corr() .cov()` | Aggregation | Window |
| `.agg([...])` · `.apply(f, raw=True)` | Many / custom aggregations | Window, Cookbook |
| `FixedForwardWindowIndexer` · `VariableOffsetWindowIndexer` · `BaseIndexer` | Forward-looking / custom windows | Window |

```python
daily = tickets.set_index("opened")["hours_to_close"].resample("D").mean()
daily.rolling(window=3, min_periods=1).mean()        # 3-day moving average
daily.rolling(3, center=True, min_periods=1).mean()
daily.expanding().max()                              # worst so far
daily.ewm(span=3).mean()                             # recent days weigh more
daily.rolling(3, min_periods=1).agg(["mean", "max"])

ts = tickets.set_index("opened")["hours_to_close"]
ts.rolling("2D").sum()                               # time-based window (index must be sorted)
```

> `min_periods` defaults to the window size for count windows → early rows are NaN. Set `min_periods=1` for dashboards.

---

## 17. Resampling

| Command | Use | Seen in |
|---|---|---|
| `ts.resample("D").sum()/mean()/count()/ohlc()/agg({...})` | Downsample into time buckets | Time series, Time deltas, Cookbook |
| `resample(..., on="col")` / `level=` | Use a column instead of the index | Time series |
| `closed="left"/"right"` · `label="left"/"right"` · `origin=` · `offset=` | Bucket edges | Time series |
| `resample("12h").ffill()/bfill()/asfreq()/interpolate()` | Upsample | Time series |
| `df.groupby(key).resample(freq)` | Per-group buckets | GroupBy |
| `asfreq(freq)` | Re-index to a frequency without aggregating | Time series |

```python
by_time = tickets.set_index("opened")
by_time.resample("D")["ticket_id"].count()
by_time.resample("D").agg({"ticket_id": "count", "hours_to_close": "mean"})
tickets.resample("D", on="opened")["ticket_id"].count()          # no set_index needed
by_time.resample("W-MON", label="left", closed="left")["ticket_id"].count()
by_time["hours_to_close"].resample("D").ohlc()
daily.resample("12h").ffill()                                     # upsample
```

---

## 18. Reshape

| Command | Direction | Seen in |
|---|---|---|
| `df.pivot(index, columns, values)` | long → wide (keys must be unique) | Reshaping |
| `pd.pivot_table(df, index, columns, values, aggfunc, fill_value, margins)` | long → wide **with aggregation** | Reshaping, Cookbook |
| `df.melt(id_vars, value_vars, var_name, value_name)` | wide → long | Reshaping, Basics |
| `pd.wide_to_long(df, stubnames, i, j)` | wide → long for `A1970, A1980…` columns | Reshaping |
| `stack(level)` · `unstack(level, fill_value)` | columns ↔ inner index level | Reshaping, GroupBy, Cookbook |
| `pd.get_dummies(df / s, prefix=, columns=, drop_first=, dtype=)` · `pd.from_dummies` | Category ↔ indicator columns | Reshaping, Text |
| `explode(col)` | List-cells → rows | Reshaping |
| `pd.crosstab(a, b, values=, aggfunc=, normalize=, margins=)` | Frequency table | Reshaping |
| `T` | Transpose | Basics |

```python
counts = tickets.pivot_table(
    index="team", columns="priority", values="ticket_id",
    aggfunc="count", fill_value=0, margins=True,
)
hours_wide = tickets.pivot(index="ticket_id", columns="priority", values="hours_to_close")
long = (
    counts.reset_index()
    .melt(id_vars="team", var_name="priority", value_name="n")
)
stacked = counts.stack()            # priority becomes an inner index level
stacked.unstack()                   # and back

pd.get_dummies(tickets["priority"], prefix="p", dtype=int)
pd.from_dummies(pd.get_dummies(tickets["priority"]))
one_tag_per_row = tickets.assign(tag=tickets["tags"].str.split("|")).explode("tag")
pd.crosstab(tickets["team"], tickets["priority"], normalize="index")   # row %
```

> Rule of thumb: duplicates in your `index × columns` pairs → `pivot` raises, `pivot_table` aggregates.

---

## 19. Combine

| Command | Like | Key params | Seen in |
|---|---|---|---|
| `pd.concat([a, b], axis=0/1, ignore_index=, keys=, join="outer"/"inner")` | `UNION ALL` (axis 0) / side-by-side (axis 1) | `keys` adds an outer level | Merge, Text, Cookbook, IO |
| `a.merge(b, on= / left_on= right_on= / left_index=, how=, suffixes=, indicator=, validate=)` | `JOIN` on columns | `how`: left, right, inner, outer, cross | Merge, Cookbook |
| `a.join(b, on=, how=, lsuffix=, rsuffix=)` | `JOIN` on the **index** of `b` | default `how="left"` | Merge, Reshaping |
| `pd.merge_ordered(a, b, fill_method="ffill", left_by=)` | Ordered outer join with fill | | Merge |
| `pd.merge_asof(a, b, on=, by=, tolerance=, direction=)` | Nearest earlier match (both sorted) | | Merge |
| `a.compare(b, align_axis=, keep_shape=, keep_equal=)` | Diff two same-shape frames | | Merge |
| `a.combine_first(b)` · `a.combine(b, func)` | Patch holes / element-wise combine | | Basics, Merge |
| `a.update(b)` | In-place overwrite with non-NA values | | Basics |

```python
teams = pd.DataFrame({"team": ["billing", "tech", "sales", "legal"], "manager": ["Ana", "Raj", "Lee", "Kim"]})

enriched = tickets.merge(teams, on="team", how="left", validate="many_to_one", indicator=True)
enriched["_merge"].value_counts()          # left_only = tickets with no team match
pd.merge(tickets, teams, on="team", how="outer")

renamed = teams.rename(columns={"team": "team_name"})
tickets.merge(renamed, left_on="team", right_on="team_name", how="inner")

tickets.set_index("team").join(teams.set_index("team"), how="inner")

week1 = tickets.head(4)
week2 = tickets.tail(4)
pd.concat([week1, week2], ignore_index=True)
pd.concat({"week1": week1, "week2": week2}, names=["batch"])      # labeled sources
pd.concat([tickets[["ticket_id"]], tickets[["team"]]], axis=1)

shifts = pd.DataFrame({
    "start": pd.to_datetime(["2026-01-03 08:00", "2026-01-05 00:00"]),
    "on_call": ["Ana", "Raj"],
})
pd.merge_asof(tickets.sort_values("opened"), shifts, left_on="opened", right_on="start")

before = tickets.loc[:2, ["priority", "hours_to_close"]]
after = before.copy()
after.loc[1, "priority"] = "high"
before.compare(after)                       # only the changed cells
```

> `validate="one_to_one"/"one_to_many"/"many_to_one"` turns silent row explosions into errors — use it in pipelines.

---

## 20. Iterating

| Command | Yields | Seen in |
|---|---|---|
| `for col in df` | column names | Basics |
| `df.items()` | `(column, Series)` | Basics |
| `df.iterrows()` | `(index, row Series)` — slow, **loses dtypes** | Basics, Cookbook |
| `df.itertuples(index=, name=)` | namedtuples — faster, keeps dtypes | Basics |
| `for name, grp in df.groupby(k)` | group key + sub-frame | GroupBy |
| `for chunk in pd.read_csv(path, chunksize=n)` | DataFrame chunks | IO |

```python
for col, series in tickets.items():
    pass
for idx, row in tickets.head(2).iterrows():
    pass
for row in tickets.head(2).itertuples(index=False):
    row.team, row.priority
```

> Reach for vectorised code, `.map`, `.apply`, or `groupby` first. Never modify the object you're iterating over.

---

## 21. IO

### 21.1 Reader ↔ writer pairs

| Format | Read | Write | Key options | Needs |
|---|---|---|---|---|
| CSV / text | `pd.read_csv` · `pd.read_fwf` · `pd.read_table` | `to_csv` | `sep usecols dtype parse_dates index_col na_values keep_default_na thousands chunksize nrows skiprows comment encoding on_bad_lines dtype_backend` | — |
| JSON | `pd.read_json` · `pd.json_normalize` | `to_json` | `orient` (`records`, `split`, `index`, `columns`, `values`, `table`) · `lines=True` · `date_format="iso"` | — |
| Excel / ODS | `pd.read_excel` · `pd.ExcelFile` | `to_excel` · `pd.ExcelWriter` | `sheet_name` (`None` = all sheets) · `usecols="A,C:E"` · `engine` | openpyxl / xlsxwriter |
| Parquet | `pd.read_parquet` | `to_parquet` | `columns` · `engine="pyarrow"` · `partition_cols` · `index=False` | pyarrow |
| Feather / ORC | `pd.read_feather` · `pd.read_orc` | `to_feather` · `to_orc` | | pyarrow |
| SQL | `pd.read_sql` · `read_sql_query` · `read_sql_table` | `to_sql` | `con` · `if_exists` · `index` · `chunksize` · `dtype` | SQLAlchemy (or `sqlite3`) |
| Pickle | `pd.read_pickle` | `to_pickle` | `compression` | — |
| HDF5 | `pd.read_hdf` · `pd.HDFStore` | `to_hdf` | `format="table"` · `where` | PyTables |
| HTML | `pd.read_html` (returns a **list**) | `to_html` | `match` · `attrs` · `extract_links` | lxml / bs4 |
| XML | `pd.read_xml` | `to_xml` | `xpath` | lxml |
| LaTeX | — | `df.style.to_latex()` | | jinja2 |
| Stata / SAS / SPSS | `read_stata` · `read_sas` · `read_spss` | `to_stata` | | — |
| Iceberg | `pd.read_iceberg` | `to_iceberg` | `catalog_name` | pyiceberg |
| Clipboard | `pd.read_clipboard` | `to_clipboard` | | — |
| Remote | any reader with `s3://`, `https://` + `storage_options=` | | | fsspec / s3fs |

### 21.2 Examples

```python
import sqlite3
import tempfile
from io import StringIO

out = tempfile.mkdtemp()

tickets.to_csv(f"{out}/tickets.csv", index=False)
back = pd.read_csv(
    f"{out}/tickets.csv",
    parse_dates=["opened"],
    dtype={"team": "string", "ticket_id": "Int64"},
    usecols=["ticket_id", "team", "opened", "hours_to_close"],
    na_values=["", "NA"],
)
pd.read_csv(StringIO("a;b\n1;2\n3;4"), sep=";")
for chunk in pd.read_csv(f"{out}/tickets.csv", chunksize=3):
    pass                                                    # process big files piece by piece

tickets.to_json(f"{out}/tickets.jsonl", orient="records", lines=True, date_format="iso")
pd.read_json(f"{out}/tickets.jsonl", lines=True)
pd.json_normalize([{"id": 1, "customer": {"name": "Acme", "tier": "gold"}}])   # customer.name, customer.tier

tickets.to_parquet(f"{out}/tickets.parquet", index=False)
pd.read_parquet(f"{out}/tickets.parquet", columns=["ticket_id", "team"])

tickets.to_pickle(f"{out}/tickets.pkl.gz")                  # compression inferred from .gz
pd.read_pickle(f"{out}/tickets.pkl.gz")

with pd.ExcelWriter(f"{out}/report.xlsx") as writer:
    tickets.to_excel(writer, sheet_name="tickets", index=False)
    tickets.groupby("team").size().to_excel(writer, sheet_name="by_team")
all_sheets = pd.read_excel(f"{out}/report.xlsx", sheet_name=None)   # dict of DataFrames

con = sqlite3.connect(":memory:")
tickets.to_sql("tickets", con, index=False)
pd.read_sql_query("SELECT team, COUNT(*) AS n FROM tickets GROUP BY team", con)
con.close()

tables = pd.read_html(StringIO(tickets.head(2).to_html()))      # list of DataFrames
```

> Pipeline habit: land raw files with everything as text (`dtype=str`) in bronze, then cast with `to_numeric` / `to_datetime(errors="coerce")` and count the coerced NaNs in silver.

---

## 22. Plotting

All use matplotlib under the hood (`pd.set_option("plotting.backend", …)` to switch).

| Command | Chart | Seen in |
|---|---|---|
| `df.plot()` · `df.plot(x=, y=, kind=)` | Line (default) | Charts, Missing, GroupBy |
| `plot.bar()` · `plot.barh(stacked=True)` | Bars | Charts |
| `plot.hist(bins=, alpha=)` · `df.hist()` | Histogram | Charts |
| `plot.box()` · `df.boxplot(by=)` · `groupby(k).boxplot()` | Box | Charts, GroupBy, Cookbook |
| `plot.area()` · `plot.scatter(x, y, c=, s=)` · `plot.hexbin()` · `plot.pie()` · `plot.kde()` | Other kinds | Charts |
| `pandas.plotting.scatter_matrix` · `andrews_curves` · `parallel_coordinates` · `lag_plot` · `autocorrelation_plot` · `bootstrap_plot` · `radviz` · `table` | Diagnostic plots | Charts |
| common args: `title xlabel ylabel legend logy secondary_y subplots layout figsize colormap yerr table ax` | Formatting | Charts |

```python
import matplotlib
matplotlib.use("Agg")                     # headless; drop this line in Jupyter

tickets["priority"].value_counts().plot.bar(title="Tickets by priority")
tickets["hours_to_close"].plot.hist(bins=5)
tickets.boxplot(column="hours_to_close", by="team")
daily.plot(title="Avg hours to close", ylabel="hours")
tickets.plot.scatter(x="ticket_id", y="hours_to_close")
```

---

## 23. Table styling

`df.style` returns a **Styler** (for notebooks, HTML, Excel, LaTeX — it doesn't change the data).

| Command | Use | Seen in |
|---|---|---|
| `format(fmt / {col: fmt}, precision=, na_rep=, thousands=)` · `format_index()` | Display formatting | Table viz |
| `highlight_max / highlight_min / highlight_null / highlight_between / highlight_quantile` | Built-in highlights | Table viz |
| `background_gradient(cmap=)` · `text_gradient()` · `bar(subset=, color=)` | Heatmap / in-cell bars | Table viz |
| `map(func)` (cell) · `apply(func, axis=)` (column/row/table) · `apply_index()` | Custom CSS per cell | Table viz |
| `set_properties(**css, subset=)` · `set_table_styles([...])` · `set_td_classes()` · `set_caption()` · `set_tooltips()` | CSS & captions | Table viz |
| `hide(axis=, subset=)` · `concat(other_styler)` · `relabel_index()` | Layout | Table viz |
| `to_html()` · `to_excel()` · `to_latex()` · `export()` / `use()` | Output & reuse | Table viz, IO |

```python
styled = (
    tickets[["ticket_id", "team", "hours_to_close"]]
    .style.format({"hours_to_close": "{:.1f}"}, na_rep="—")
    .highlight_null(color="lightyellow")
    .highlight_max(subset=["hours_to_close"], color="salmon")
    .bar(subset=["hours_to_close"], color="#9ecae1")
    .set_caption("Ticket close times")
    .hide(axis="index")
)
html = styled.to_html()
```

---

## 24. Options & display settings

| Command | Use | Seen in |
|---|---|---|
| `pd.get_option(name)` · `pd.set_option(name, value)` · `pd.options.display.max_rows = n` | Read/change | Options, Basics |
| `pd.reset_option(name or "^display")` | Back to default | Options |
| `pd.describe_option(name)` | Docs for options | Options |
| `with pd.option_context(name, value, …):` | Temporary change | Options |
| `pd.set_eng_float_format(accuracy=, use_eng_prefix=)` | Engineering notation | Options |

Most used: `display.max_rows`, `display.min_rows`, `display.max_columns`, `display.max_colwidth`, `display.precision`, `display.width`, `display.expand_frame_repr`, `display.float_format`, `mode.chained_assignment`, `compute.use_numexpr`, `compute.use_bottleneck`, `plotting.backend`.

```python
pd.set_option("display.max_columns", None)       # show every column
pd.set_option("display.precision", 2)
with pd.option_context("display.max_rows", 5, "display.max_colwidth", 20):
    print(tickets)
pd.reset_option("^display")
```

---

## 25. Same command, many places

These names show up on several of your pages because they work on **many object types with the same syntax**. Learn once, reuse everywhere.

| Command | DataFrame / Series | GroupBy | Rolling / Expanding / EWM | Resampler | Index | Styler |
|---|---|---|---|---|---|---|
| `agg` / `aggregate` | ✅ | ✅ | ✅ | ✅ | — | — |
| `apply` | ✅ | ✅ | ✅ (not EWM) | ✅ | — | ✅ (CSS) |
| `transform` | ✅ | ✅ | — | ✅ | — | — |
| `pipe` | ✅ | ✅ | ✅ (not EWM) | ✅ | — | ✅ |
| `map` | ✅ (element) | — | — | — | ✅ | ✅ (CSS) |
| `sum mean min max std count` | ✅ | ✅ | ✅ | ✅ | `min`/`max` only | — |
| `first` / `last` | — *(the offset version was removed in pandas 3; use `.loc["2026-01"]`)* | ✅ | ✅ (rolling) | ✅ | — | — |
| `head` / `tail` | ✅ | ✅ (per group) | — | — | — | — |
| `ffill` / `bfill` | ✅ | ✅ (within group) | — | ✅ (upsample) | — | — |
| `shift` / `diff` / `cumsum` / `rank` | ✅ | ✅ (within group) | — | — | — | — |
| `fillna` | ✅ | — | — | — | ✅ | — |
| `isin` | ✅ | — | — | — | ✅ (`level=`) | — |
| `plot` / `boxplot` / `hist` | ✅ | ✅ | — | — | — | — |
| `.str` / `.dt` | Series | — | — | — | ✅ | — |
| `rename` | ✅ | — | — | — | ✅ | — |
| `to_*` writers | ✅ | — | — | — | — | `to_html/excel/latex` |

---

## 26. Shared parameters

The same keyword means the same thing across commands.

| Parameter | Meaning | Appears in |
|---|---|---|
| `axis=0` / `"index"` | operate **down** rows (per column) | stats, `apply`, `dropna`, `drop`, `concat`, `sample`, `where` |
| `axis=1` / `"columns"` | operate **across** columns (per row) | same |
| `subset=` | limit to these columns | `dropna`, `duplicated`, `drop_duplicates`, `value_counts`, Styler methods |
| `keep="first"/"last"/False` | which duplicate survives | `duplicated`, `drop_duplicates`, `index.duplicated`, `nlargest` |
| `how=` | join type / NaN rule | `merge`, `join` (`left/right/inner/outer/cross`), `dropna` (`any/all`) |
| `on=` / `left_on=` / `right_on=` | join keys | `merge`, `join`, `merge_asof`, `resample` (`on=` column) |
| `ignore_index=True` | rebuild 0..n-1 index | `concat`, `melt`, `explode`, `sort_values`, `drop_duplicates` |
| `as_index=False` | keep group keys as columns | `groupby` |
| `dropna=` | include/exclude NaN keys | `groupby`, `value_counts`, `crosstab`, `pivot_table`, `nunique` |
| `skipna=` | ignore NaN in reductions | `sum`, `mean`, `cumsum`, `idxmax`… |
| `numeric_only=True` | skip non-numeric columns | stats, `groupby` aggregations, `corr` |
| `fill_value=` | value for missing combos | `add/sub/…`, `reindex`, `unstack`, `pivot_table` |
| `errors="coerce"/"raise"/"ignore"` | bad input handling | `to_numeric`, `to_datetime`, `to_timedelta`, `astype` (`raise/ignore`), `drop` |
| `regex=` | treat pattern as regex | `replace`, `str.replace`, `str.contains`, `filter` |
| `na=` / `na_rep=` | value used for missing | `str.contains(na=)`, `str.cat(na_rep=)`, `to_csv(na_rep=)`, `format(na_rep=)` |
| `freq=` | time step | `date_range`, `resample`, `shift`, `Grouper`, `to_period`, `asfreq` |
| `min_periods=` | minimum non-NaN values | `rolling`, `expanding`, `ewm`, `corr` |
| `level=` | which MultiIndex level | `groupby`, `xs`, `stack/unstack`, `sum`, `isin`, `sub` |
| `random_state=` | reproducible randomness | `sample` |
| `observed=` | only categories that appear | `groupby`, `pivot_table`, `crosstab` (`dropna=`) |
| `dtype_backend="numpy_nullable"/"pyarrow"` | nullable/Arrow dtypes on load | `read_csv`, `read_json`, `read_parquet`, `read_sql` |

---

## 27. Look-alikes

| These… | …differ like this |
|---|---|
| `loc` vs `iloc` vs `[]` | labels (end **inclusive**) vs positions (end exclusive) vs columns / row slice / mask |
| `at`/`iat` vs `loc`/`iloc` | scalar-only, faster |
| `apply` vs `map` vs `transform` vs `agg` | row/column function vs element-wise vs same-shape vs reduced |
| `replace` vs `str.replace` | whole-cell value swap (any dtype) vs substring/regex inside text |
| `where` vs `mask` vs `np.where` | keep-if-True vs replace-if-True vs build new array from scratch |
| `fillna` vs `ffill`/`bfill` vs `interpolate` | constant vs carry neighbour vs estimate |
| `dropna()` vs `groupby(dropna=)` | remove rows vs keep/drop NaN **group keys** |
| `size()` vs `count()` | rows per group incl. NaN vs non-NaN per column |
| `pivot` vs `pivot_table` vs `crosstab` | reshape only vs reshape + aggregate vs count two factors |
| `merge` vs `join` vs `concat` | column keys vs index keys vs stack/glue |
| `stack` vs `melt` | moves a column **level** to index vs turns columns into rows with `variable/value` |
| `cut` vs `qcut` | your bin edges vs equal-count bins |
| `get_dummies` vs `str.get_dummies` | one category per cell vs delimited multi-values per cell |
| `str.match` vs `str.contains` vs `str.fullmatch` | anchored at start vs anywhere vs whole string |
| `NaN` vs `NA` vs `NaT` vs `None` | float/str vs nullable dtypes vs datetimes vs object; test all with `isna()` |
| `"int64"` vs `"Int64"` | NumPy (no missing) vs nullable (supports `<NA>`) |
| `"str"` vs `"string"` | pandas 3 default text (NaN) vs `pd.NA`-based text |
| `tz_localize` vs `tz_convert` | attach a zone vs change the zone |
| `resample` vs `groupby(pd.Grouper(freq=))` vs `rolling("2D")` | calendar buckets vs same buckets alongside other keys vs sliding windows |
| `.values` vs `.to_numpy()` vs `.array` | legacy/ambiguous vs NumPy array vs pandas ExtensionArray |
| `drop_duplicates` vs `index.duplicated` | duplicate **rows** vs duplicate **labels** |
| `equals` vs `==` | whole-object check (NaN==NaN) vs element-wise (NaN≠NaN) |

---

## 28. Top resources with reasoning

| # | Resource | Why it's worth your time |
|---|---|---|
| 1 | **pandas User Guide** (pandas.pydata.org/docs/user_guide) — the pages you saved | The source of every command here. Use the per-method API reference links when you need every parameter. |
| 2 | **pandas "10 minutes to pandas"** | Fastest refresher of sections 3–6 and 15–19 in one sitting. |
| 3 | **pandas Comparison with SQL** (docs → Getting started → Comparison with other tools) | Maps `SELECT/WHERE/GROUP BY/JOIN/UNION` to pandas one-to-one — matches how you already think as a data engineer. |
| 4 | **Official Cheat Sheet PDF** (pandas.pydata.org/Pandas_Cheat_Sheet.pdf) | Two-page visual of reshape/combine/group — good for desk reference beside this file. |
| 5 | **Wes McKinney — *Python for Data Analysis*, 3rd ed.** (free at wesmckinney.com/book) | Written by the pandas creator; best long-form explanation of indexing, groupby, time series. |
| 6 | **Matt Harrison — *Effective Pandas*** | Teaches method chaining with `assign/pipe/query`, the style used in this file; great for clean pipeline code. |
| 7 | **Kaggle Learn: Pandas** (kaggle.com/learn/pandas) | Short hands-on exercises to practise selection, groupby, merge with instant feedback. |
| 8 | **PySpark pandas API / Spark DataFrame docs** | Most commands here have a Spark twin (`groupBy().agg`, `withColumn`, window `over`); useful when the same logic has to scale on Databricks/Glue. |
| 9 | **AWS SDK for pandas (awswrangler)** | Adds `wr.s3.read_parquet`, `wr.athena.read_sql_query`, `wr.s3.to_parquet(dataset=True)` — the IO section extended to S3/Glue/Athena, handy for AWS cert labs. |

**Suggested practice loop:** load a real CSV (your `ticket-data` page is a good candidate) → run sections 4 → 7 → 8 → 9 to clean it → 15 & 18 to summarise → 19 to enrich → 21 to write Parquet.
