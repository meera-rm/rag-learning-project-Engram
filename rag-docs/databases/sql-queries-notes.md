---
title: Classic SQL interview queries — study notes
topic: databases
source_type: my-notes
note_kind: study-notes
---

# Classic SQL Interview Queries — Study Notes

A checklist of problem types that keep appearing in SQL interviews, each with the idea behind the solution. Table and column names are generic.

## Highest / Nth highest value

**Idea:** rank values with `DENSE_RANK() OVER (ORDER BY value DESC)` and pick rank N, or use `MAX` with a `<` subquery for the 2nd highest. Return NULL (not an empty result) when there is no Nth value by wrapping in an outer `SELECT MAX(...)`.

## Find duplicates

**Idea:** `GROUP BY` the columns that define "the same", then `HAVING COUNT(*) > 1`.

```sql
SELECT email, COUNT(*) FROM users GROUP BY email HAVING COUNT(*) > 1;
```

## Delete duplicates, keep one

**Idea:** number rows inside each duplicate group with `ROW_NUMBER() OVER (PARTITION BY dup_cols ORDER BY id)` and delete where the number is greater than 1.

## Earns more than their manager

**Idea:** self-join the employee table to itself on `e.boss_id = m.id`, then compare salaries.

## Consecutive values (e.g. a value appearing 3 times in a row)

**Idea:** compare each row with the next rows using `LEAD(value, 1)` and `LEAD(value, 2)` ordered by id, or use the "gaps and islands" trick: `id - ROW_NUMBER() OVER (PARTITION BY value ORDER BY id)` is constant across a consecutive run, so group by it.

## Running total

```sql
SELECT order_date, amount,
       SUM(amount) OVER (ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total
FROM orders;
```

## Rolling average (e.g. 7 days)

```sql
SELECT day, revenue,
       AVG(revenue) OVER (ORDER BY day ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS avg_7d
FROM daily_revenue;
```

`ROWS` counts physical rows; if days can be missing, fill the calendar first or use a date-range frame where supported.

## Gaps in ids or dates

**Idea:** use `LEAD(id) OVER (ORDER BY id)` and keep rows where the next id is more than 1 greater; the gap is from `id + 1` to `next_id - 1`. For dates, join to a generated calendar table and find dates with no matching row.

## Active users (e.g. logged in on N consecutive days)

**Idea:** distinct user-days, then gaps-and-islands: `day - ROW_NUMBER() OVER (PARTITION BY user ORDER BY day)` groups consecutive days; keep groups with `COUNT(*) >= N`.

## Year-over-year growth

```sql
SELECT year, revenue,
       ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY year)) / LAG(revenue) OVER (ORDER BY year), 1) AS yoy_pct
FROM yearly_revenue;
```

## Median

**Idea:** many databases have `PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY value)`. Without it, number the rows in both directions (`ROW_NUMBER` ascending and descending) and average the middle one or two rows.

## Most frequent item

**Idea:** `GROUP BY item ORDER BY COUNT(*) DESC LIMIT 1` — or use `RANK()` over the counts to return all items tied for first.

## Random sample

**Idea:** `ORDER BY RANDOM() LIMIT n` (or `RAND()`), fine for small tables; large tables use built-in sampling (`TABLESAMPLE`) because sorting everything is expensive.

## Text search

**Idea:** `LIKE '%word%'` works but can't use a normal index when the pattern starts with `%`; full-text search indexes are the scalable option.

## Pagination

**Idea:** `LIMIT/OFFSET` is simple but slow for deep pages; **keyset pagination** (`WHERE id > last_seen_id ORDER BY id LIMIT 20`) stays fast.

## Hierarchy (org chart, categories)

**Idea:** a **recursive CTE**: start from the root rows, then repeatedly join children to the rows found so far.

```sql
WITH RECURSIVE chain AS (
  SELECT id, name, boss_id, 1 AS level FROM staff WHERE boss_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.boss_id, c.level + 1
  FROM staff e JOIN chain c ON e.boss_id = c.id
)
SELECT * FROM chain ORDER BY level;
```

## First value in each group

**Idea:** `FIRST_VALUE(col) OVER (PARTITION BY grp ORDER BY ts)`, or `ROW_NUMBER() = 1` per group.

## Existence check

**Idea:** `EXISTS (SELECT 1 …)` stops at the first match, which is cheaper than counting all matches with `COUNT(*) > 0`.

## Upsert (insert or update)

**Idea:** insert, and if the key already exists, update instead — `INSERT … ON CONFLICT (key) DO UPDATE` (PostgreSQL), `INSERT … ON DUPLICATE KEY UPDATE` (MySQL), or `MERGE` (SQL Server, Oracle, standard SQL).

## Mutual relationships (e.g. friends both ways)

**Idea:** self-join a relationship table on swapped columns: `a.user1 = b.user2 AND a.user2 = b.user1`.

## How to approach any of these in an interview

1. Restate the question and confirm edge cases (ties? NULLs? empty result?).
2. Name the pattern: self-join, anti-join, window function, gaps-and-islands, recursive CTE.
3. Write the simplest correct version first, then improve.
4. Mention performance: indexes on join and filter columns, avoiding deep `OFFSET`, `EXISTS` vs `COUNT`.
