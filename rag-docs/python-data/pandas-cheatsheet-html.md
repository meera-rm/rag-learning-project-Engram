---
title: pandas-cheatsheet-html
topic: python-data
source_type: my-notes
source_file: STUDYNOTEs/pandas-cheatsheet.html
---

Ticket Data Pandas Cheatsheet

· Week 1 assignment

# Ticket Data Pandas Cheatsheet

Every pandas task actually run against the Tobias Bueck support-ticket parquet — loading, hashing stable record IDs, deduping, building `ticket_text`, missingness and language-leakage checks, the raw→English→final filter funnel, plus the sampling, dedup-vectorization and read/write patterns from the production scripts. Code and comments are taken from the actual notebooks and scripts, trimmed to the reusable pattern.

Sourced from `profiling_raw_parquet_final.ipynb`, `profiling_raw_parquet_version1.ipynb` and `parquetfiletobiprofile.ipynb` in `extra_materials/`, plus the production scripts under `homework1/sample_output/` (`task2/profile_tobi_bueck.py`, `task3/synth_tickets.py`, `task1/datasets/*.py`)

[1. Load & inspect](#load) [2. Schema table](#schema) [3. Stable record IDs](#hashing) [4. De-duplicate](#dedup) [5. Filter to English](#filter) [6. Build ticket\_text](#derive) [7. Missingness](#missing) [8. Text-length stats](#textstats) [9. Groupby & crosstab](#groupby) [10. Language leakage (regex)](#leakage) [11. Duplicate text groups](#duplicates) [12. Filter funnel](#funnel) [13. Sample export & verify](#sample) [14. Stratified sampling](#stratified) [15. Vectorized dedup with where()](#where) [16. assign() + iterrows()](#assign) [17. insert() a column by position](#insert) [18. map() + boolean mean()](#mapmean) [19. Normalize before comparing](#normalize) [20. Write CSV + Parquet outputs](#write) [Method reference](#methods)

Task 1

## Load the parquet and get a first look

**Why:** confirm the file reads cleanly and see row/column counts before anything else. Always read the raw copy fresh — don't reuse a variable from an earlier cell that may already be filtered.

``` code
import pandas as pd
from IPython.display import display

RAW = "/Users/janedoe/hw1_data/tobi_bueck/tobi_bueck_ddf1c81a.parquet"
df_raw = pd.read_parquet(RAW)

# row/column counts as a small table instead of raw prints —
# reads better in a notebook and copies cleanly into a report
summary = pd.DataFrame({
    "Metric": ["Number of rows", "Number of columns"],
    "Value": [df_raw.shape[0], df_raw.shape[1]]
})
display(summary)
display(df_raw.head())
```

Task 2

## Confirm the schema — names and dtypes together

**Why:** `df.dtypes` alone is hard to scan for 20+ columns. Building it as its own DataFrame with a running column number made it easy to reference "column 7" when writing up notes.

``` code
schema = pd.DataFrame({
    "Column Number": range(1, len(df_raw.columns) + 1),
    "Column Name": df_raw.columns,
    "Data Type": df_raw.dtypes.astype(str).values
})
display(schema)
```

Task 3

## Create a stable, content-based record ID

**Why:** the raw file has no primary key. Hashing every raw field (sorted by column name, so column order never changes the hash) gives every ticket a deterministic ID that's the same across re-runs and re-exports — needed before any dedup or sampling step downstream can refer back to a specific row.

``` code
import hashlib
import pandas as pd

# sort so hashing never depends on the column order in the file
raw_cols = sorted(df_raw.columns.tolist())

def make_content_hash(row):
    """Deterministic SHA-256 hash from all raw field values.
    Column names are sorted so column order doesn't affect the ID."""
    parts = []
    for col in raw_cols:
        value = row[col]
        # represent missing values the same way every time
        value = "<NULL>" if pd.isna(value) else str(value)
        # include the column name so "a=1,b=" can't collide with "a=1b="
        parts.append(f"{col}={value}")
    blob = "|".join(parts)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:12]

df_raw["record_id"] = df_raw.apply(make_content_hash, axis=1)

print("Rows:", len(df_raw))
print("Unique record IDs:", df_raw["record_id"].nunique())
print("Duplicate record IDs:", df_raw["record_id"].duplicated().sum())
```

Task 4

## Number exact-duplicate rows instead of dropping them

**Why:** two tickets can hash identically (truly identical raw content). Rather than silently losing one, `groupby(...).cumcount()` numbers occurrences within each identical-content group, so the first keeps the base ID and later copies get a suffix — every row stays traceable.

``` code
# cumcount: 0 for the first row in each identical-content group, 1 for the next, ...
duplicate_number = (
    df_raw.groupby(raw_cols, dropna=False, sort=False)
          .cumcount()
)
duplicate_mask = duplicate_number > 0

# only the non-first copies get a suffix appended to their base ID
df_raw.loc[duplicate_mask, "record_id"] = (
    df_raw.loc[duplicate_mask, "record_id"]
    + "_" + duplicate_number[duplicate_mask].astype(str)
)
```

Task 5

## Filter to the English subset

**Why:** the assignment's downstream labeling only covers English tickets. `.copy()` after the boolean filter matters — without it, later assignments to `df_en[...]` raise pandas's `SettingWithCopyWarning`.

``` code
print(df_raw["language"].value_counts(dropna=False))

df_en = df_raw[
    df_raw["language"].fillna("").str.strip().eq("en")
].copy()

print("Raw rows:", len(df_raw))
print("English rows:", len(df_en))
```

Task 6

## Derive `ticket_text` from subject + body

**Why:** the model input is one combined text field, not two separate columns. `fillna("")` before concatenation is required — concatenating a `NaN` string column with `+` silently turns the \*whole\* result to `NaN`, not just that one row.

``` code
df_en["ticket_text"] = (
    df_en["subject"].fillna("").astype(str).str.strip()
    + "\n"
    + df_en["body"].fillna("").astype(str).str.strip()
).str.strip()

print("ticket_text nulls:", df_en["ticket_text"].isna().sum())
display(df_en[["subject", "body", "ticket_text"]].head())
```

Task 7

## Missing vs. blank — two different checks

**Why:** `.isna()` only catches real `NaN`/`None`. A field can also be a non-null empty string (`""` or all whitespace) — invisible to `.isna()`. Both counts get reported side by side so nothing is missed.

``` code
rows = []
for col in ["subject", "body", "ticket_text"]:
    null_count = df_en[col].isna().sum()
    blank_count = (
        df_en[col].fillna("").astype(str).str.strip().eq("").sum()
    )
    rows.append({
        "Field": col,
        "Null Count": null_count,
        "Null/Blank Count": blank_count,
        "Null/Blank %": round(blank_count / len(df_en) * 100, 2)
    })
display(pd.DataFrame(rows))
```

Task 8

## Character & word counts, then describe()

**Why:** `.describe()` on the two derived count columns gives min/median/max in one call — the fastest way to spot suspiciously short tickets (an empty subject and a one-word body) worth a manual spot check.

``` code
df_en["text_char_count"] = df_en["ticket_text"].str.len()
df_en["text_word_count"] = df_en["ticket_text"].str.split().str.len()

display(
    df_en[["text_char_count", "text_word_count"]].describe().round(2)
)

# the actual rows worth a manual read
SHORT_WORD_THRESHOLD = 5
short = (
    df_en[df_en["text_word_count"] <= SHORT_WORD_THRESHOLD]
    .sort_values(["text_word_count", "record_id"])
)
print("Tickets with <=", SHORT_WORD_THRESHOLD, "words:", len(short))
```

Task 9

## Tag coverage with groupby, crosstab and value\_counts

**Why:** tickets carry up to 8 tag slots (`tag_1`…`tag_8`). Counting how many are actually filled per ticket, and cross-tabbing the primary tag against queue, surfaced how sparse and how skewed the tagging really is.

``` code
tag_cols = [f"tag_{i}" for i in range(1, 9)]
filled = df_raw[tag_cols].notna()

# distribution of "how many tags does this ticket have"
tag_count = (
    filled.sum(axis=1).value_counts().sort_index()
    .rename_axis("Tags per ticket").reset_index(name="Tickets")
)
tag_count["Share"] = (tag_count["Tickets"] / len(df_raw) * 100).round(1)

# normalize="index" turns raw counts into row-wise proportions —
# "of tickets with this tag_1, what share land in each queue"
pd.crosstab(df_raw["tag_1"], df_raw["queue"], normalize="index").round(2)
```

Task 10

## Catch mislabeled language with a regex hint

**Why:** the `language` column is self-reported by the source data and isn't fully reliable. Counting hits against a small list of common German function words flags rows worth a manual re-check inside the "English" subset instead of trusting the label blindly.

``` code
german_words = r"\b(?:und|nicht|bitte|ich|wir|ihr|sehr|geehrte|vielen|dank|mit|für)\b"

hits = df_en["ticket_text"].str.lower().str.count(german_words)
suspect = df_en[hits >= 3].sort_values("record_id")

print(
    "Flagged (>= 3 German function words):", len(suspect),
    f"({len(suspect) / len(df_en):.2%})"
)
display(suspect[["record_id", "subject", "body", "queue"]].head(10))
```

Task 11

## Duplicate ticket text, including conflicting labels

**Why:** two different raw rows can still produce the exact same `ticket_text` after cleaning. Worse, the \*same\* text sometimes gets routed to more than one queue — those are the ones worth flagging, since they can't both be right.

``` code
# how many exact-duplicate ticket_text groups exist at all
dup_groups = df_en.groupby("ticket_text").size()
dup_groups = dup_groups[dup_groups > 1]
print("Duplicate text groups:", len(dup_groups))

# of those groups, which ones disagree on the routing queue
text_queue_counts = df_en.groupby("ticket_text")["queue"].nunique()
conflicting = text_queue_counts[text_queue_counts > 1]
print("Conflicting-label duplicate groups:", len(conflicting))
```

Task 12

## Document the filter funnel

**Why:** every filtering step drops rows silently unless it's logged. Recording the row count and the delta at each stage turns "why do I have fewer rows than I started with" into a table anyone reviewing the work can check in one glance.

``` code
n_raw = len(df_raw)
n_english = len(df_en)
n_text = (df_en["ticket_text"].str.strip() != "").sum()
n_final = (
    (df_en["ticket_text"].str.strip() != "")
    & (df_en["queue"].notna())
).sum()

funnel = pd.DataFrame({
    "Stage": ["Raw", 'English (language == "en")',
              "Non-empty ticket text", "Non-empty queue"],
    "Rows": [n_raw, n_english, n_text, n_final],
    "Rows removed at step": [0, n_raw - n_english, n_english - n_text, n_text - n_final]
})
funnel["% of raw retained"] = (funnel["Rows"] / n_raw * 100).round(1)
display(funnel)
```

Task 13

## Export a sample and verify it against expectations

**Why:** a manual inspection sample (20 rows) got written to CSV for spot-checking labels. Re-reading it back and asserting the counts match what was expected while building the sample is what actually catches a bad sampling script — printing the numbers isn't enough on its own without a known target to compare against.

``` code
s = pd.read_csv("/Users/janedoe/homework1/sample_output/task2/inspection_sample_20.csv")

# each check states the expected value in a comment, so a mismatch is obvious
print(s["label_fits_text"].value_counts())          # expect Y 8, N 6, Unclear 6
print("Missing subject:", s["subject"].isna().sum())  # expect 5
print("Language OK:", (s["language_ok"] == "Y").sum()) # expect 20

# explode turns "tag1, tag2" strings into one row per tag before counting
print(
    s["issues"].fillna("").str.split(r",\s*").explode()
     .replace("", pd.NA).dropna().value_counts()
)
```

Task 14 · `task2/profile_tobi_bueck.py`

## Shuffle once, then sample round-robin per queue

**Why:** a plain random sample can accidentally skip small queues entirely. Shuffling the whole frame with `.sample(frac=1, ...)` first, then taking "1st of each queue, then 2nd of each queue" via `.groupby().cumcount()`, guarantees every queue gets covered before any queue gets a second pick.

``` code
def build_sample(df: pd.DataFrame) -> pd.DataFrame:
    """Shuffle with random_state=SEED, then take the 1st ticket of
    each queue, then the 2nd of each queue, ... until SAMPLE_N."""
    # frac=1 samples every row — this shuffles, it doesn't subset
    shuffled = df.sample(frac=1, random_state=SEED).copy()

    shuffled["_sample_order"] = range(len(shuffled))
    # position of each row within its queue, after shuffling
    shuffled["_queue_round"] = shuffled.groupby(LABEL_COL, sort=False).cumcount()

    # sort by round first: everyone's "round 0" pick comes before anyone's "round 1"
    round_robin = shuffled.sort_values(["_queue_round", "_sample_order"])
    return round_robin.head(SAMPLE_N)[SAMPLE_COLS].copy()
```

Task 15 · `task2/profile_tobi_bueck.py`

## Vectorized dedup suffix with `Series.where()`

**Why:** the notebook version used `.loc[mask, col] = ...` to suffix duplicate IDs. The script version does the same thing in one vectorized expression — `Series.where(cond, other)` keeps the original value where `cond` is true, and substitutes `other` where it's false — the inverse of `Series.mask()`.

``` code
base = raw.apply(content_hash, axis=1)
dup_number = base.groupby(base, sort=False).cumcount()

# where dup_number == 0 (first occurrence): keep base unchanged.
# where dup_number != 0 (a later copy): substitute the suffixed version.
record_id = base.where(dup_number == 0, base + "_" + dup_number.astype(str))
```

Task 16 · `task2/profile_tobi_bueck.py`

## Attach a throwaway column with `assign()`, then walk rows with `iterrows()`

**Why:** `.assign(_w=words)` attaches the precomputed word-count Series under a temporary name without mutating `df` itself, so it can be filtered and sorted in one chained expression. `.iterrows()` is the right (if slower) tool here — only 15 rows, building a list of report dicts for JSON output, not a bulk column transform.

``` code
# suspiciously short texts (<= SHORT_WORDS words)
short = df.assign(_w=words)[words <= SHORT_WORDS].sort_values(["_w", "record_id"])

rep["short_texts"] = {
    "threshold_words": SHORT_WORDS,
    "count": len(short),
    # .iterrows() gives (index, row) pairs — used here to build plain
    # dicts for a JSON report, not for a bulk numeric transform
    "examples": [
        {"record_id": r.record_id, LABEL_COL: str(r[LABEL_COL]), "text": r.ticket_text}
        for _, r in short.head(15).iterrows()
    ],
}
```

Task 17 · `task2/profile_tobi_bueck.py`

## Insert a derived column at a fixed position

**Why:** a plain `df["record_id"] = ...` assignment tacks the new column onto the end. `.insert(0, name, values)` puts it first, so `record_id` is always the leftmost column in every exported CSV — easier to scan and to join on later.

``` code
raw = pd.read_parquet(RAW)
df = raw.copy()

# position 0 = first column, not appended at the end
df.insert(0, "record_id", derive_ids(raw))
assert df["record_id"].is_unique, "record_id is not unique"
df["ticket_text"] = build_text(df)
```

Task 18 · `task3/synth_tickets.py`, `task2/profile_tobi_bueck.py`

## `Series.map()` for per-cell cleaning, `.mean()` on a boolean mask for a proportion

**Why:** `.map(fn)` applies a plain Python function element-by-element — the right tool for a custom `clean()` function with no vectorized `.str` equivalent. Separately, `.mean()` on a boolean Series is a one-line trick for "what fraction is True" — `True`/`False` average out to exactly the proportion of missing values.

``` code
# custom cleaning function, applied cell-by-cell — not vectorizable
# the way .str.strip() or .str.lower() are
en["subject_c"], en["body_c"] = en["subject"].map(clean), en["body"].map(clean)

# is_missing(df[c]) returns a bool Series; .mean() over True/False
# values IS the proportion of True (missing) values — no separate
# .sum() / len() division needed
def missing_table(df: pd.DataFrame, cols: list) -> dict:
    return {
        c: {
            "count": int(is_missing(df[c]).sum()),
            "proportion": round(float(is_missing(df[c]).mean()), 4),
        }
        for c in cols
    }
```

Task 19 · `task2/profile_tobi_bueck.py`

## Normalize case and whitespace before comparing duplicates

**Why:** two tickets with the exact same words but different capitalization or double-spacing won't match under a strict `.duplicated()`. Lowercasing and collapsing whitespace with `.str.replace(regex=True)` first gives a second, looser duplicate count — the gap between the two numbers is how much near-duplication the strict check was missing.

``` code
# regex=True is required — without it, "\s+" is matched as a literal
# three-character string instead of "one or more whitespace chars"
norm = (
    df["ticket_text"]
    .str.lower()
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

rep["duplicates"]["redundant_rows_after_case_whitespace_normalisation"] = (
    int(norm.duplicated().sum())
)
```

Task 20 · `task1/datasets/*.py`, `_common.py`

## Write CSV + Parquet together, and convert a HF dataset to pandas

**Why:** every download script writes both formats side by side — CSV for readability, Parquet for the faster, typed reads the profiling notebooks actually use. `.to_pandas()` is the bridge from a HuggingFace `datasets.Dataset` object into a regular DataFrame, so every pandas method above becomes available immediately after.

``` code
# HuggingFace dataset -> plain pandas DataFrame
df = load_dataset(REPO, revision=commit, split="train").to_pandas()

# index=False on both — the row number isn't meaningful data,
# re-reading either file should reproduce the same columns
df.to_csv(dest / f"{tag}.csv", index=False, encoding="utf-8")
df.to_parquet(dest / f"{tag}.parquet", index=False, engine="pyarrow")

# the reproducible-sample helper does the same pairing for a subset
sample = df.sample(min(n, len(df)), random_state=seed)
sample.to_csv(out, index=False, encoding="utf-8")
sample.to_parquet(out.with_suffix(".parquet"), index=False)
```

## Method quick reference

| Method                                    | What it did here                                                                                                                         |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `.fillna("").astype(str).str.strip()`     | The standard three-step guard before any string op, so a NaN never silently poisons a concatenation or comparison.                       |
| `.copy()`                                 | After every boolean-mask filter (`df[df.x == y].copy()`), to avoid `SettingWithCopyWarning` on later column assignments.                 |
| `.groupby(cols).cumcount()`               | Numbered duplicate rows within identical-content groups instead of dropping them.                                                        |
| `.value_counts(dropna=False)`             | Language and tag distributions, including how many rows are actually null.                                                               |
| `pd.crosstab(a, b, normalize="index")`    | Row-wise proportions of tag\_1 against queue — "of this tag, what share go where."                                                       |
| `.str.count(pattern)`                     | Counted regex hits per row to flag likely-German text inside the English subset.                                                         |
| `.duplicated(subset=[...])`               | Flagged exact-duplicate ticket\_text rows.                                                                                               |
| `.explode()`                              | Split a comma-joined "issues" string into one row per tag before `value_counts()`.                                                       |
| `.describe().round(2)`                    | Min/median/max of char and word counts in one call, to spot outliers fast.                                                               |
| `.apply(fn, axis=1)`                      | Ran the SHA-256 hash function row-wise to build `record_id`.                                                                             |
| `.sample(frac=1, random_state=)`          | Shuffled the full frame reproducibly before round-robin sampling across queues.                                                          |
| `Series.where(cond, other)`               | Vectorized alternative to `.loc[mask, col] = ...` — kept the base hash where `cond` holds, substituted the suffixed one where it didn't. |
| `.assign(col=values)`                     | Attached a temporary word-count column for one chained filter + sort, without mutating `df`.                                             |
| `.iterrows()`                             | Walked 15 short-ticket rows to build plain dicts for a JSON report — not a bulk transform.                                               |
| `.insert(pos, name, values)`              | Placed `record_id` as column 0 instead of appending it at the end.                                                                       |
| `Series.map(fn)`                          | Applied a custom `clean()` function cell-by-cell where no vectorized `.str` method existed.                                              |
| `bool_series.mean()`                      | One-line proportion trick: the mean of a True/False Series is exactly the share that's True.                                             |
| `.str.replace(pattern, repl, regex=True)` | Collapsed whitespace and case before a second, looser duplicate check.                                                                   |
| `.to_csv() / .to_parquet()`               | Wrote every dataset in both formats — CSV to read by eye, Parquet for the notebooks' actual reads.                                       |
| `.to_pandas()`                            | Converted a HuggingFace `datasets.Dataset` into a DataFrame right after downloading it.                                                  |

Pulled from three related notebooks in `extra_materials/` that iterate on the same profiling task — the patterns above are the ones that survived into the final version. `task2_conversation_notes.md` and `task3_report_write copy.md` have the written-up findings this analysis fed into.
