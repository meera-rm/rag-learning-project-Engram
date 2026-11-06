---
title: pandas-practice-drills
topic: python-data
source_type: my-notes
source_file: STUDYNOTEs/concepts/pandas-practice-drills.md
---

# Pandas Practice Drills

Generic, standalone exercises — not tied to any specific assignment or dataset. Use any small CSV, or build a toy one (5–10 fake rows, one obvious null, one obvious duplicate) so you know the "answer" going in before repeating on a real CSV.

## Reading & inspecting
1. Read a CSV, print the shape, column names, and dtypes.
2. Read a CSV, display only 5 columns of your choice with `.head()`.
3. Read a CSV, print the first 5 rows and the last 5 rows.
4. Read a CSV, print one column as a plain list and as a Series — note the difference in output.

## Null / missing checks
5. Print null count per column with one line (`.isna().sum()`).
6. Print which rows have a null in a specific column (`df[df["col"].isna()]`).
7. Print percent null per column, sorted highest to lowest.
8. Check for "hidden" missing values — empty strings or whitespace-only — separately from real nulls.

## Duplicates
9. Print how many fully-duplicate rows exist (`.duplicated().sum()`), then display them.
10. Find duplicates based on just one or two columns, not the whole row (`.duplicated(subset=[...])`).
11. Drop duplicates, keeping the first occurrence, and print how many rows were removed.

## Cleaning
12. Fill nulls in a numeric column with the column mean; fill nulls in a text column with `"unknown"`.
13. Strip whitespace and lowercase every value in a text column.
14. Drop any column that's more than 50% null.
15. Convert a column of strings like `"$1,200"` into a proper float column.

## Small report writing
16. Build a 5-column summary table: column name, dtype, null count, unique count, sample value.
17. Group by one categorical column and print count + mean of a numeric column per group.
18. Print the 3 most common values in a column with their counts and percentages.
19. Write a function `quick_report(df)` that combines 16–18 into one printed report, called on any DataFrame.
