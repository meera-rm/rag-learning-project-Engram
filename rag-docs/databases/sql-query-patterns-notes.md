---
title: SQL query patterns — study notes
topic: databases
source_type: my-notes
note_kind: study-notes
---

# SQL Query Patterns — Study Notes

Practical patterns that come up again and again in SQL practice and interviews. Examples use two tables:

```sql
staff(id, name, pay, team_id, boss_id, hire_date)
teams(id, name)
```

## Self-join: comparing a row with a related row in the same table

A table that points to itself (each employee has a `boss_id`) is queried by joining it to a second copy of itself with different aliases.

```sql
-- staff who earn more than their manager
SELECT e.name AS employee, e.pay, m.name AS manager, m.pay AS manager_salary
FROM staff e
JOIN staff m ON e.boss_id = m.id
WHERE e.pay > m.pay;
```

Think of `e` and `m` as two separate tables that happen to hold the same data.

## Anti-join: rows with no match

"Find X that has no Y" — two common forms:

```sql
-- LEFT JOIN and keep the rows where the right side is missing
SELECT d.name
FROM teams d
LEFT JOIN staff e ON e.team_id = d.id
WHERE e.id IS NULL;

-- NOT EXISTS (often the clearest)
SELECT d.name
FROM teams d
WHERE NOT EXISTS (SELECT 1 FROM staff e WHERE e.team_id = d.id);
```

Avoid `NOT IN (subquery)` when the subquery can return NULL — a single NULL makes the whole condition unknown, so no rows come back.

## Nth highest value

```sql
-- 2nd highest pay, handling ties and "no such row"
SELECT MAX(pay) AS second_highest
FROM staff
WHERE pay < (SELECT MAX(pay) FROM staff);

-- general Nth with a window function (N = 3)
SELECT DISTINCT pay
FROM (SELECT pay, DENSE_RANK() OVER (ORDER BY pay DESC) AS rnk FROM staff) t
WHERE rnk = 3;
```

`DENSE_RANK` is the usual choice because tied salaries share a rank and no rank numbers are skipped.

## Top N per group

```sql
-- top 2 earners in each department
SELECT *
FROM (
  SELECT e.*, ROW_NUMBER() OVER (PARTITION BY team_id ORDER BY pay DESC) AS rn
  FROM staff e
) t
WHERE rn <= 2;
```

`PARTITION BY` restarts the numbering for each department. Use `RANK`/`DENSE_RANK` instead of `ROW_NUMBER` if ties should all be included.

## Comparing with a group average

```sql
-- staff paid above their department's average
SELECT name, pay, team_id
FROM (
  SELECT e.*, AVG(pay) OVER (PARTITION BY team_id) AS team_avg
  FROM staff e
) t
WHERE pay > team_avg;
```

The window function keeps every row and attaches the group average, which avoids a separate subquery per row.

## Filtering on aggregates

```sql
-- teams with more than 5 people and an average pay over 50,000
SELECT team_id, COUNT(*) AS headcount, AVG(pay) AS avg_salary
FROM staff
GROUP BY team_id
HAVING COUNT(*) > 5 AND AVG(pay) > 50000;
```

`WHERE` filters rows before grouping; `HAVING` filters groups after aggregation.

## Gaps between consecutive rows (LAG / LEAD)

```sql
-- pay difference to the previous hire in the same department
SELECT name, team_id, hire_date, pay,
       pay - LAG(pay) OVER (PARTITION BY team_id ORDER BY hire_date) AS diff_from_prev
FROM staff;
```

`LAG` looks at the previous row, `LEAD` at the next, inside the window's order.

## Duplicates

```sql
-- find duplicate names
SELECT name, COUNT(*) FROM staff GROUP BY name HAVING COUNT(*) > 1;

-- keep one row per name, delete the rest (keep the lowest id)
DELETE FROM staff
WHERE id IN (
  SELECT id FROM (
    SELECT id, ROW_NUMBER() OVER (PARTITION BY name ORDER BY id) AS rn FROM staff
  ) t WHERE rn > 1
);
```

## Conditional aggregation (pivot-style)

```sql
SELECT team_id,
       SUM(CASE WHEN pay >= 80000 THEN 1 ELSE 0 END) AS high_earners,
       SUM(CASE WHEN pay <  80000 THEN 1 ELSE 0 END) AS others
FROM staff
GROUP BY team_id;
```

`CASE` inside an aggregate turns rows into columns without a special PIVOT feature.

## Tricky cases to remember

| Situation | What to watch |
| --- | --- |
| `COUNT(*)` vs `COUNT(col)` | `COUNT(col)` skips NULLs |
| `NULL = NULL` | Not true — use `IS NULL` |
| `NOT IN` with NULLs | Returns nothing; prefer `NOT EXISTS` |
| `LEFT JOIN` + `WHERE right.col = x` | Turns it back into an inner join — move the condition into `ON` |
| Ties | Decide between `ROW_NUMBER`, `RANK`, `DENSE_RANK` on purpose |
| Integer division | `5/2` may give `2`; cast to decimal |

## Reading order of a query

SQL is written `SELECT … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT`, but it is **evaluated** roughly as `FROM/JOIN → WHERE → GROUP BY → HAVING → window functions → SELECT → DISTINCT → ORDER BY → LIMIT`. That explains why a column alias defined in `SELECT` usually can't be used in `WHERE`, and why window functions can't go in `WHERE` (wrap them in a subquery).
