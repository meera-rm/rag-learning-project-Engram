---
title: SQL-Interview-Questions
topic: databases
source_type: interview-questions
source_file: STUDYNOTEs/SQL-Interview-Questions.md
---

# SQL Interview Questions — Complete Collection

Every interview question found in this folder, organised and answered. Concepts are explained in depth in the companion file **SQL-Complete-Notes.md**; this file is the question bank.

## Contents

| Section | Source | Count |
|---------|--------|-------|
| **A** | 100 Questions — Basic → Optimization (Vinay Kumar Panika set) | 100 |
| **B** | 50 Rapid-Fire Questions | 50 |
| **C** | Real Interview Questions (10–20 LPA package) | 30 |
| **D** | 350 Practice Questions with Working Solutions (Kartik Mungole set) | 350 |
| **E** | Questions embedded in the SQL Complete Notes pages | ~40 |
| **F** | Interview strategy and quick-revision sheet | — |

All queries in Section D are written against the practice schema documented at the end of **SQL-Complete-Notes.md** (§68).

---

# SECTION A — 100 QUESTIONS (BASIC → OPTIMIZATION)

## A1. Basic Level (Q1–Q25)

**Q1. What is SQL?**
SQL (Structured Query Language) is a standard programming language used to interact with relational databases. It is used to store, retrieve, update and delete data, and to create and modify database structures such as tables, views and indexes.
```sql
SELECT * FROM Employees;
```

**Q2. What is a Database?**
An organized collection of data stored and managed electronically. It allows users to efficiently store, retrieve, update and manage data. Example: a customer database on an e-commerce website storing name, email, contact number and purchase history.

**Q3. What are the types of SQL commands?**
Five families:
1. **DDL** (Data Definition Language) — defines the structure: `CREATE`, `ALTER`, `DROP`, `TRUNCATE`
2. **DML** (Data Manipulation Language) — manages stored data: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
3. **DCL** (Data Control Language) — controls access: `GRANT`, `REVOKE`
4. **TCL** (Transaction Control Language) — manages transactions: `COMMIT`, `ROLLBACK`, `SAVEPOINT`
5. **DQL** (Data Query Language) — retrieves data: `SELECT`

**Q4. What is a Primary Key?**
A column or combination of columns that uniquely identifies each row. Does not allow NULL, must be unique, only one per table.

**Q5. What is a Foreign Key?**
A column (or combination) in one table that refers to the Primary Key in another table, creating a relationship and enforcing referential integrity. Can contain duplicates and NULLs.

**Q6. What is a UNIQUE Key?**
A constraint ensuring all values in a column are distinct across all rows. Prevents duplicates but allows NULL (usually one). Multiple UNIQUE keys per table are allowed.

**Q7. Difference between Primary Key and UNIQUE Key?**

| Primary Key | UNIQUE Key |
|-------------|------------|
| Uniquely identifies each row | Ensures values in the column are unique |
| Does not allow NULL | Allows one NULL (in most databases) |
| Only one per table | Multiple allowed |
| Creates a unique clustered index | Creates a unique non-clustered index |
| Used to identify a record | Used to enforce uniqueness without being the primary identifier |

**Q8. What is the NOT NULL constraint?**
Ensures a column cannot have NULL values — every row must have a value there. Prevents insertion of NULL, ensures mandatory fields have data, can be applied to one or more columns.

**Q9. What is the Default Constraint?**
Provides a default value when no value is specified during insert. Helps avoid NULLs; can apply to any data type.
```sql
CREATE TABLE Employees (EmpID INT, Salary DECIMAL(10,2) DEFAULT 5000);
```

**Q10. Difference between DELETE, TRUNCATE and DROP?**

| Command | Function | Can Rollback | Affects Structure | Speed |
|---------|----------|--------------|-------------------|-------|
| DELETE | Removes specific rows based on a WHERE condition | Yes (with COMMIT/ROLLBACK) | No | Slow (row-by-row) |
| TRUNCATE | Removes all rows without a condition | No | No | Faster than DELETE |
| DROP | Deletes the entire table including data and structure | No | Yes (removes table structure) | Fastest |

**Q11. Difference between WHERE and HAVING?**

| Clause | Purpose | Used With | Filter Type | Execution Order |
|--------|---------|-----------|-------------|-----------------|
| WHERE | Filters rows before grouping | SELECT, UPDATE, DELETE | Row-level | Applied before GROUP BY |
| HAVING | Filters groups after grouping | SELECT with GROUP BY | Group-level | Applied after GROUP BY |

**Q12. What are Joins in SQL?**
Joins combine data from two or more tables based on a related column. Types: INNER, LEFT, RIGHT, FULL, SELF, CROSS.

**Q13. What is INNER JOIN?**
Combines rows from two or more tables based on a matching condition, returning only records where the condition is true in both tables.
```sql
SELECT e.Name, d.DepartmentName
FROM Employees e
INNER JOIN Departments d ON e.DepartmentID = d.DepartmentID;
```

**Q14. What is LEFT JOIN?**
Returns all records from the left table and matching records from the right. Non-matching right-side columns show NULL.

**Q15. What is RIGHT JOIN?**
Returns all records from the right table and matching records from the left. Non-matching left-side columns show NULL.

**Q16. What is FULL JOIN?**
Combines LEFT and RIGHT JOIN — returns all records from both tables, with NULLs where there is no match. Useful to find unmatched records on both sides.

**Q17. What is Self Join?**
A table joined with itself to compare rows within the same table. Requires table aliases. Used for hierarchical relationships.
```sql
SELECT e.Name AS Employee, m.Name AS Manager
FROM Employees e
JOIN Employees m ON e.ManagerID = m.EmpID;
```

**Q18. What is Cross Join?**
Returns the Cartesian product — every row of table 1 combined with every row of table 2. No condition required. Result rows = Rows(T1) × Rows(T2).

**Q19. What is UNION and UNION ALL?**
Both combine result sets of two or more SELECT statements. UNION removes duplicates; UNION ALL keeps them.

**Q20. Difference between UNION and UNION ALL?**

| Criteria | UNION | UNION ALL |
|----------|-------|-----------|
| Duplicates | Removes duplicate rows | Includes all duplicate rows |
| Performance | Slower (duplicate removal) | Faster |
| Sorting | Sorts the result set | Does not sort |
| Usage | When duplicates are not required | When duplicates must be preserved |

**Q21. What is Normalization?**
The process of organizing data to reduce redundancy and improve data integrity by dividing large tables into smaller related tables. Forms: 1NF (atomic values), 2NF (no partial dependency), 3NF (no transitive dependency), BCNF (every determinant is a candidate key).

**Q22. What is Denormalization?**
Combining tables or adding redundant data to improve read performance at the cost of redundancy. Opposite of normalization. Used in data warehouses and reporting systems.

**Q23. Difference between CHAR and VARCHAR?**
CHAR is fixed-length and pads with spaces; VARCHAR is variable-length and uses only what it needs plus a length byte or two. CHAR is faster for consistent-length data (PIN codes); VARCHAR suits varying data (names, addresses).

**Q24. Difference between SQL and MySQL?**
SQL is a *language* (a standard developed by ANSI, used across many databases). MySQL is a *software* — an RDBMS developed by Oracle Corporation that uses SQL.

**Q25. What is Auto Increment in SQL?**
A property that automatically generates a unique sequential number when a new row is inserted, typically used for primary keys. Starts at 1 by default and increments by 1.
```sql
CREATE TABLE Employees (EmployeeID INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(50));
```

---

## A2. Intermediate Level (Q26–Q50)

**Q26. What is a Subquery?**
A query nested inside another query, used to fetch data the main query uses as a condition. Also called an inner/nested query. Executes before the main query. Types: single-row, multiple-row, correlated.

**Q27. What is a Nested Query?**
A query written inside another query to retrieve data based on the inner query's result. The inner query executes first and passes its result to the outer query. Can be used with WHERE, HAVING and FROM.

**Q28. What is a Correlated Subquery?**
A subquery that depends on values from the outer query, executing repeatedly for each row of the outer query — which makes it slower. It cannot be executed independently.
```sql
SELECT * FROM Employees e1
WHERE Salary > (SELECT AVG(Salary) FROM Employees e2 WHERE e2.DepartmentID = e1.DepartmentID);
```

**Q29. What is GROUP BY in SQL?**
Groups rows with the same values into summary rows, typically used with aggregate functions (COUNT, SUM, AVG, MAX, MIN). Used after WHERE and before ORDER BY.

**Q30. Difference between GROUP BY and ORDER BY?**
GROUP BY groups rows into summary rows and works with aggregate functions; ORDER BY sorts the final result and needs no aggregates. GROUP BY comes before ORDER BY.

**Q31. What is the use of LIMIT in SQL?**
Restricts the number of rows returned. Commonly used for Top N records and pagination.
```sql
SELECT * FROM Employees ORDER BY Salary DESC LIMIT 3;
```

**Q32. How to find the Second Highest Salary?**
```sql
SELECT MAX(Salary) FROM Employees
WHERE Salary < (SELECT MAX(Salary) FROM Employees);
```
The inner query gets the highest salary; the outer query finds the highest salary below it.

**Q33. How to find Duplicate Records in a table?**
```sql
SELECT Name, COUNT(*)
FROM Employees
GROUP BY Name
HAVING COUNT(*) > 1;
```
GROUP BY groups the same names; HAVING COUNT(*) > 1 keeps only duplicates.

**Q34. What is a CTE (Common Table Expression)?**
A temporary result set defined within the execution of a single SQL statement, using the WITH clause.
```sql
WITH IT_Employees AS (
    SELECT * FROM Employees WHERE Department = 'IT'
)
SELECT * FROM IT_Employees WHERE Salary > 50000;
```

**Q35. What is a Temporary Table?**
A table used to store temporary data during a session. Automatically deleted when the session ends. Prefixed with `#` in SQL Server, `TEMPORARY` in MySQL.

**Q36. What is a Window Function?**
A function that performs calculations across a set of table rows related to the current row without collapsing the result into a single value. Works with `OVER()`. Used for ranking, running totals and moving averages.

Types: `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `NTILE(n)`, `SUM()`, `AVG()`, `MAX()`/`MIN()`, `LEAD()`, `LAG()`.

| Function | Purpose | Duplicates | Skips Numbers | Example Usage |
|----------|---------|------------|---------------|---------------|
| ROW_NUMBER | Unique Rank | No | No | Employee ranking |
| RANK | Rank with skips | Yes | Yes | Competition rank |
| DENSE_RANK | Rank without skips | Yes | No | Class rank |
| NTILE | Divide rows | No | No | Quartiles |
| SUM | Running total | No | No | Salary analysis |
| AVG | Running average | No | No | Salary average |
| LEAD | Next row value | No | No | Price trends |
| LAG | Previous row value | No | No | Sales trends |

**Q37. Difference between ROW_NUMBER(), RANK() and DENSE_RANK()?**

| Function | Purpose | Duplicates | Skips Numbers | Example |
|----------|---------|------------|---------------|---------|
| ROW_NUMBER() | Assigns unique sequential numbers to each row | No | No | 1, 2, 3, 4 |
| RANK() | Assigns the same rank to equal values | Yes | Yes | 1, 2, 2, 4 |
| DENSE_RANK() | Assigns rank without skipping numbers | Yes | No | 1, 2, 2, 3 |

**Q38. What is the CASE Statement?**
Applies conditional logic in SQL queries, similar to IF-ELSE.
```sql
SELECT Name, Salary,
       CASE WHEN Salary >= 70000 THEN 'High'
            WHEN Salary >= 40000 THEN 'Medium'
            ELSE 'Low' END AS Level
FROM Employee;
```

**Q39. What is COALESCE?**
Returns the first non-null value from a list of expressions. Used to handle NULLs; accepts multiple expressions.
```sql
SELECT COALESCE(phone, mobile, 'No contact') FROM Customers;
```

**Q40. What is the NVL Function?**
Replaces NULL values with a specified value (Oracle). MySQL equivalent: `IFNULL()`. SQL Server: `ISNULL()`.
```sql
SELECT NVL(Salary, 0) FROM Employees;
```

**Q41. What is Indexing?**
Creating a lookup structure that improves the speed of data retrieval. Speeds up SELECT, automatically maintained, can cover one or more columns — but slows down INSERT/UPDATE/DELETE.

**Q42. What is a Clustered Index?**
Sorts and stores the data physically in the table based on the indexed column. Only one per table. Automatically created on the Primary Key. Faster for retrieval.

**Q43. What is a Non-Clustered Index?**
Creates a separate structure from the table data, storing pointers to the actual rows. Multiple allowed per table. Does not affect the physical order of data.

**Q44. Difference between Clustered and Non-Clustered Index?**

| Clustered Index | Non-Clustered Index |
|-----------------|---------------------|
| Stores data physically sorted | Stores pointers to data |
| Only one per table | Multiple allowed |
| Faster for data retrieval | Slower than clustered |
| Automatically created on Primary Key | Manually created on any column |
| Affects physical order of table | Does not affect physical order |

**Q45. What is a View?**
A virtual table based on the result of a SQL query. Does not store data physically, simplifies complex queries, provides data security, and can be used like a table in SELECT queries.

**Q46. Difference between View and Table?**

| View | Table |
|------|-------|
| Virtual table | Physical table |
| Does not store data physically | Stores data physically |
| Based on SQL queries | Contains raw data |
| Provides security by restricting columns | No restriction unless applied |
| Automatically updates when base data changes | Needs manual updates |

**Q47. What is a Stored Procedure?**
A group of predefined SQL statements stored in the database that can be executed multiple times. Improves code reusability and performance, supports input/output parameters, and provides security by hiding SQL code.

**Q48. Difference between Function and Stored Procedure?**

| Function | Stored Procedure |
|----------|------------------|
| Returns a single value or table | May or may not return a value |
| Can be used in SELECT statements | Cannot be used in SELECT statements |
| Allows only input parameters | Allows input and output parameters |
| Cannot modify database state | Can modify database state (INSERT/UPDATE/DELETE) |
| Always returns a value | Does not always return a value |

**Q49. What is a Trigger?**
An automatic action executed when a specified event occurs in a table. Executes on INSERT/UPDATE/DELETE, used for data validation and logging, cannot be called manually, improves data integrity.

**Q50. What is a Cursor?**
A database object used to retrieve, manipulate and navigate row-by-row through a result set. Slower than set-based operations; not recommended for large datasets.

---

## A3. Advanced Level (Q51–Q75)

**Q51. What is the ACID Property?**

| Property | Description |
|----------|-------------|
| **A** — Atomicity | The transaction is all or nothing. If one part fails, the entire transaction fails and the database remains unchanged. |
| **C** — Consistency | The database must be in a consistent state before and after the transaction. |
| **I** — Isolation | Transactions execute independently, without interfering with each other. |
| **D** — Durability | Once committed, changes are permanent, even if the system crashes. |

**Q52. What is a Transaction?**
A group of SQL operations executed as a single unit to perform a specific task. Follows ACID properties. Commands: `BEGIN TRANSACTION`, `COMMIT`, `ROLLBACK`, `SAVEPOINT`.

**Q53. Difference between COMMIT and ROLLBACK?**

| COMMIT | ROLLBACK |
|--------|----------|
| Saves the transaction's changes permanently | Undoes all changes made by the transaction |
| Once executed, changes cannot be undone | Restores the database to its previous state |
| Used when all operations are successful | Used when an error occurs |
| Improves data durability | Helps maintain data consistency |

**Q54. What is a Savepoint?**
Temporarily saves a transaction at a specific point, allowing rollback of only part of the transaction. Enables partial rollback and better error handling.
```sql
SAVEPOINT sp1;
ROLLBACK TO sp1;
```

**Q55. Difference between IN and EXISTS?**

| IN | EXISTS |
|----|--------|
| Compares values from the main query with a list of values | Checks if a subquery returns any rows |
| Works with static values or subqueries | Only works with subqueries |
| Slower with large datasets | Faster for large datasets |
| Returns all matching rows | Stops checking after finding the first match |

**Q56. Difference between DELETE and TRUNCATE?**

| DELETE | TRUNCATE |
|--------|----------|
| Removes specific rows based on a WHERE condition | Removes all rows without any condition |
| Can be rolled back inside a transaction | Cannot be rolled back once executed |
| Slower — logs each row deletion | Faster — does not log individual row deletions |
| Maintains table structure and identity values | Resets identity column values to the initial seed |

**Q57. What is Index Fragmentation?**
When the logical order of index pages does not match the physical order of data on disk, making retrieval slower.
- **Internal Fragmentation** — unused space inside index pages due to deletions or updates.
- **External Fragmentation** — index pages stored in non-sequential order.
Fix with `OPTIMIZE TABLE` (MySQL), `ALTER INDEX REBUILD` (SQL Server), `REINDEX` (PostgreSQL).

**Q58. Difference between RANK() and DENSE_RANK()?**

| RANK() | DENSE_RANK() |
|--------|--------------|
| Assigns a unique rank but skips the next rank when there are duplicates | Assigns rank without skipping ranks for duplicates |
| Gaps are created in the ranking sequence | No gaps |
| Slower than DENSE_RANK() | Faster because it doesn't skip |

**Q59. How to fetch common records from two tables?**
Use INNER JOIN:
```sql
SELECT a.* FROM TableA a INNER JOIN TableB b ON a.id = b.id;
```

**Q60. Difference between UNION and JOIN?**

| UNION | JOIN |
|-------|------|
| Combines result sets vertically (rows) | Combines result sets horizontally (columns) |
| Removes duplicates by default | Does not remove duplicates |
| Tables must have the same number of columns and data types | Tables can have different numbers of columns |
| Used when tables have similar data | Used when tables have related data through a common column |

**Q61. What is a Pivot Table?**
Transforms row data into column data to give a summary report. Converts rows into columns, used for summary reports and data analysis, commonly used with SUM(), AVG(), COUNT().
```sql
SELECT region,
       SUM(CASE WHEN month='Jan' THEN amount ELSE 0 END) AS Jan,
       SUM(CASE WHEN month='Feb' THEN amount ELSE 0 END) AS Feb
FROM sales GROUP BY region;
```

**Q62. What is Case Sensitivity in SQL?**
Whether the database treats uppercase and lowercase letters as different.
- **Column names:** most databases are not case-sensitive (MySQL, SQL Server).
- **Table names:** depends on the database and operating system.
- **String values:** MySQL is case-insensitive by default.
Use `BINARY` in MySQL for case-sensitive matching:
```sql
SELECT * FROM Employee WHERE BINARY Name = 'Vinay';
```

**Q63. How to find the Nth Highest Salary?**
Method 1 — LIMIT with OFFSET (MySQL):
```sql
SELECT DISTINCT Salary FROM Employees ORDER BY Salary DESC LIMIT 1 OFFSET 2;  -- 3rd highest
```
- `ORDER BY Salary DESC` sorts descending
- `OFFSET 2` skips the top 2
- `LIMIT 1` selects the next one
Always use DISTINCT to remove duplicate salaries.

**Q64. How to get the First 3 Maximum Salaries?**
```sql
SELECT DISTINCT Salary FROM Employees ORDER BY Salary DESC LIMIT 3;
```

**Q65. Difference between DROP, DELETE and TRUNCATE?**

| Command | Purpose | Can Rollback | Speed | Structure Affected | Condition-Based |
|---------|---------|--------------|-------|--------------------|-----------------|
| DROP | Deletes the entire table with its structure | No | Fastest | Yes (removes structure) | No |
| DELETE | Removes specific rows based on condition | Yes (within a transaction) | Slow | No | Yes (with WHERE) |
| TRUNCATE | Removes all rows from the table | No | Fast | No (keeps structure) | No |

**Q66. How to calculate Age from Date of Birth?**
Method 1 — DATEDIFF (MySQL), accurate:
```sql
SELECT Name, FLOOR(DATEDIFF(CURDATE(), DOB) / 365.25) AS Age FROM Employees;
```
Method 2 — YEAR (MySQL), simple:
```sql
SELECT Name, YEAR(CURDATE()) - YEAR(DOB) AS Age FROM Employees;
```

**Q67. What is a Recursive Query?**
A query that refers to itself to perform repetitive operations until a condition is met. Used for hierarchical data (employee-manager relationships, org structures). Implemented with CTEs; recursion continues until the termination condition is satisfied.

**Q68. Difference between Temporary Table and CTE?**

| Temporary Table | CTE |
|-----------------|-----|
| Stores data physically in temporary memory | Stores data logically without physical storage |
| Needs to be explicitly created and dropped | Automatically disappears after query execution |
| Can be used multiple times within a session | Can be used only within the same query |
| Supports indexing and DDL operations | Does not support indexing or DDL |
| Slower for small datasets | Faster for small datasets |

**Q69. How to find Odd and Even records?**
Method 1 — MOD (MySQL):
```sql
SELECT * FROM Employee WHERE MOD(EmpID, 2) = 0;   -- Even
SELECT * FROM Employee WHERE MOD(EmpID, 2) = 1;   -- Odd
```
Method 2 — ROW_NUMBER (SQL Server, PostgreSQL):
```sql
SELECT * FROM (SELECT *, ROW_NUMBER() OVER (ORDER BY EmpID) rn FROM Employee) t
WHERE rn % 2 = 0;
```

**Q70. What is JSON in SQL?**
Used to store, retrieve and manipulate data in a structured, text-based format inside relational databases. Stores key-value pairs, lightweight, good for semi-structured data. Supported in MySQL, SQL Server and PostgreSQL.

**Q71. What is XML in SQL?**
Used to store, retrieve and manipulate structured data in a text-based hierarchical format using tags. Commonly used for data exchange between applications. Supported in SQL Server, MySQL and Oracle.

**Q72. How to handle NULL values?**
1. `IS NULL` — check if a column contains NULL
2. `IS NOT NULL` — check if it doesn't
3. `COALESCE()` — replace NULL with a default value
4. `IFNULL()` (MySQL) — replace NULL with a specified value
5. `NULLIF()` — returns NULL if two expressions are equal

**Q73. What is Dynamic SQL?**
Constructing and executing SQL statements at runtime instead of writing static queries. Allows flexible query creation, used in stored procedures — but increases security risks if not handled properly. Always use parameterized queries to prevent SQL injection.

**Q74. How to calculate Percentage in SQL?**
Using arithmetic expressions with aggregate functions:
```sql
SELECT DepartmentID,
       COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Employees) AS Percentage
FROM Employees GROUP BY DepartmentID;
```

**Q75. How to find Employees who earn more than their Manager?**
Use a self join:
```sql
SELECT e.Name AS Employee, e.Salary AS EmployeeSalary,
       m.Name AS Manager, m.Salary AS ManagerSalary
FROM Employees e
JOIN Employees m ON e.ManagerID = m.EmpID
WHERE e.Salary > m.Salary;
```

---

## A4. Real-Time Scenarios (Q76–Q90)

**Q76. How to find Duplicate Emails in the Employee Table?**
```sql
SELECT Email, COUNT(Email) FROM Employees GROUP BY Email HAVING COUNT(Email) > 1;
```

**Q77. How to get the Highest Salary in each Department?**
```sql
SELECT DepartmentID, MAX(Salary) FROM Employees GROUP BY DepartmentID;
```

**Q78. How to find Employees joined in the last 3 months?**
```sql
SELECT * FROM Employees WHERE DATEDIFF(CURDATE(), JoinDate) <= 90;
-- or
SELECT * FROM Employees WHERE JoinDate >= DATE_ADD(CURDATE(), INTERVAL -3 MONTH);
```

**Q79. How to Display the First 5 Records?**
```sql
SELECT * FROM Employees LIMIT 5;          -- MySQL
SELECT TOP 5 * FROM Employees;            -- SQL Server
```

**Q80. How to find the Number of Employees in each Department?**
```sql
SELECT DepartmentID, COUNT(*) FROM Employees GROUP BY DepartmentID;
```

**Q81. How to find the Last 3 Records?**
```sql
SELECT * FROM Employees ORDER BY EmpID DESC LIMIT 3;   -- MySQL
-- SQL Server / PostgreSQL with ROW_NUMBER:
SELECT * FROM (SELECT *, ROW_NUMBER() OVER (ORDER BY EmpID DESC) rn FROM Employees) t
WHERE rn <= 3;
```

**Q82. How to find Employees without Managers?**
```sql
SELECT * FROM Employees WHERE ManagerID IS NULL;
-- or with a LEFT JOIN
SELECT e.* FROM Employees e
LEFT JOIN Employees m ON e.ManagerID = m.EmpID
WHERE m.EmpID IS NULL;
```

**Q83. How to find First Names starting with 'A'?**
```sql
SELECT * FROM Employees WHERE FirstName LIKE 'A%';
```
`%` represents any number of characters after 'A'.

**Q84. How to fetch Alternate Rows from a table?**
```sql
-- MySQL, MOD
SELECT * FROM Employee WHERE MOD(EmpID, 2) = 1;   -- odd rows
SELECT * FROM Employee WHERE MOD(EmpID, 2) = 0;   -- even rows

-- SQL Server / PostgreSQL, ROW_NUMBER
SELECT * FROM (SELECT *, ROW_NUMBER() OVER (ORDER BY EmpID) rn FROM Employee) t
WHERE rn % 2 = 1;
```

**Q85. How to swap two columns in SQL?**
Use UPDATE with a temporary variable technique:
```sql
UPDATE Employees
SET ColumnA = ColumnB, ColumnB = ColumnA;   -- works in MySQL
-- Safer, explicit temp-variable form:
UPDATE Employees SET ColumnA = ColumnA + ColumnB;
UPDATE Employees SET ColumnB = ColumnA - ColumnB;
UPDATE Employees SET ColumnA = ColumnA - ColumnB;
```

**Q86. How to display Duplicate Records with their Count?**
```sql
SELECT Name, COUNT(*) AS Occurrences
FROM Employees GROUP BY Name HAVING COUNT(*) > 1;
```

**Q87. How to find the Highest Salary without using MAX()?**
```sql
-- Method 1: ORDER BY with LIMIT
SELECT Salary FROM Employees ORDER BY Salary DESC LIMIT 1;
-- Method 2: Subquery
SELECT Salary FROM Employees e1
WHERE 0 = (SELECT COUNT(*) FROM Employees e2 WHERE e2.Salary > e1.Salary);
-- Method 3: NOT IN
SELECT Salary FROM Employees
WHERE Salary NOT IN (SELECT Salary FROM Employees WHERE Salary < ALL (...));
```

**Q88. How to fetch common records from two tables without JOIN?**
```sql
-- Method 1: IN
SELECT col FROM Table1 WHERE col IN (SELECT col FROM Table2);
-- Method 2: INTERSECT (SQL Server, PostgreSQL, Oracle)
SELECT col FROM Table1 INTERSECT SELECT col FROM Table2;
```

**Q89. How to delete Duplicate Records from a table?**
```sql
-- Method 1: ROW_NUMBER (SQL Server, PostgreSQL)
WITH cte AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY Name, Email ORDER BY EmpID) rn FROM Employees
)
DELETE FROM cte WHERE rn > 1;

-- Method 2: GROUP BY with MIN (MySQL)
DELETE FROM Employees
WHERE EmpID NOT IN (SELECT MIN(EmpID) FROM (SELECT * FROM Employees) t GROUP BY Name, Email);

-- Method 3: DISTINCT into a temporary table, then swap
```
Always back up data before deleting duplicates.

**Q90. How to find the Department with the highest Employee Count?**
```sql
SELECT DepartmentID, COUNT(*) AS cnt
FROM Employees GROUP BY DepartmentID ORDER BY cnt DESC LIMIT 1;
```

---

## A5. Optimization Techniques (Q91–Q100)

**Q91. How to Optimize SQL Queries?**
1. **Use indexes** on columns in WHERE, JOIN and ORDER BY.
2. **Avoid `SELECT *`** — select only required columns.
3. **Use joins efficiently** — INNER JOIN instead of OUTER JOIN where possible.
4. **Use EXISTS instead of IN** — EXISTS performs better with large datasets.
5. **Use LIMIT or TOP** — fetch only required rows.
6. **Avoid functions in the WHERE clause.** Instead of `WHERE YEAR(order_date) = 2024`, use `WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31'`.
7. **Optimize subqueries** — use JOIN instead of subqueries where possible.
8. **Partition large tables.**
9. **Use CTEs and temp tables** to store intermediate results.
10. **Analyze the execution plan** with EXPLAIN or Query Plan.

**Q92. What is a Query Execution Plan?**
A detailed roadmap used by the database engine to execute SQL queries efficiently. Shows how data will be retrieved, the order of operations (joins, scans, sorting), and information about indexes and filtering methods.
```sql
EXPLAIN SELECT ...;        -- MySQL / PostgreSQL
SET SHOWPLAN_ALL ON;       -- SQL Server
```
Use it to identify bottlenecks, check whether indexes or table scans are used, and understand how joins and filters are applied.

**Q93. How to Improve Query Performance?**
Same core list as Q91, plus: use WHERE instead of HAVING to filter rows early, limit results, use appropriate data types, and analyze execution plans with EXPLAIN or SHOWPLAN.

**Q94. What is Indexing?**
A technique to improve the speed of data retrieval by creating a lookup table for faster access — like a book index. Types: Primary Index, Unique Index, Clustered Index (one per table, sorts data physically), Non-Clustered Index (multiple allowed, stores pointers). Improves reads but increases the cost of INSERT/UPDATE/DELETE.

**Q95. What is Table Partitioning?**
Dividing large tables into smaller, more manageable pieces without changing the table structure. Improves query performance on large datasets and simplifies data management. Types: Range, List, Hash, Composite.

**Q96. How to Avoid Deadlocks?**
1. Access tables in the same order across transactions.
2. Minimize lock time — keep transactions short.
3. Use lower isolation levels (READ COMMITTED instead of SERIALIZABLE).
4. Avoid user interaction inside transactions.
5. Use NOLOCK / READ UNCOMMITTED for read-only operations.
6. Proper indexing to minimize the number of rows locked.
7. Break large transactions into smaller batches.

**Q97. What is the use of EXISTS?**
Checks whether a subquery returns any rows. Returns TRUE if at least one row is returned, FALSE otherwise. Faster than IN for large datasets.

**Q98. What is Query Optimization?**
The process of improving the efficiency and performance of SQL queries to retrieve data faster with minimal system resources. Reduces execution time, improves performance, minimizes CPU/memory/IO. Performed automatically by the Query Optimizer in most RDBMS, plus your own rewrites.

**Q99. Difference between Stored Procedure and Function?**

| Stored Procedure | Function |
|------------------|----------|
| Can return multiple values | Returns only one value (scalar or table) |
| Can perform DML (INSERT, UPDATE, DELETE) | Cannot perform DML |
| Supports input and output parameters | Only supports input parameters |
| Can call functions inside it | Cannot call stored procedures inside it |
| Used for business logic and complex operations | Used for calculations and returning values |

**Q100. Difference between OLTP and OLAP?**

| OLTP | OLAP |
|------|------|
| Used for day-to-day transactional operations | Used for data analysis and reporting |
| Focuses on data consistency and speed | Focuses on data aggregation and analysis |
| Stores detailed transactional data | Stores historical and summarized data |
| Supports INSERT, UPDATE, DELETE | Supports SELECT with complex queries |
| Small amounts of data per transaction | Large amounts processed at once |
| Example: banking systems, e-commerce websites | Example: data warehouses, BI tools |

---

# SECTION B — 50 RAPID-FIRE QUESTIONS

Short, definitional questions — the kind asked in the first ten minutes of a screening call.

**Q1. What is SQL?**
SQL stands for Structured Query Language. It is a programming language used for managing and manipulating relational databases.

**Q2. What is a database?**
An organized collection of data stored and accessed electronically. It provides a way to store, organize and retrieve large amounts of data efficiently.

**Q3. What is a primary key?**
A column or combination of columns that uniquely identifies each row in a table. It enforces the **entity integrity** rule in a relational database.

**Q4. What is a foreign key?**
A column or combination of columns that establishes a link between data in two tables. It ensures **referential integrity** by enforcing relationships between tables.

**Q5. Difference between a primary key and a unique key?**
A primary key uniquely identifies a row and must have a unique, non-NULL value. A unique key ensures a column (or combination) has unique values but does not necessarily identify the row, and typically allows a NULL.

**Q6. What is normalization?**
The process of organizing data in a database to minimize redundancy and dependency, by breaking a table into smaller tables and establishing relationships between them.

**Q7. What are the different types of normalization?**
- First Normal Form (1NF)
- Second Normal Form (2NF)
- Third Normal Form (3NF)
- Boyce-Codd Normal Form (BCNF)
- Fourth Normal Form (4NF)
- Fifth Normal Form (5NF) or Project-Join Normal Form (PJNF)

**Q8. What is a join in SQL?**
An operation used to combine rows from two or more tables based on related columns, allowing you to retrieve data from multiple tables simultaneously.

**Q9. Difference between DELETE and TRUNCATE?**
DELETE removes specific rows based on a condition, can be rolled back, and generates individual delete operations for each row. TRUNCATE removes all rows, cannot be rolled back, and is faster because it deallocates data pages instead of logging individual row deletions.

**Q10. Difference between UNION and UNION ALL?**
Both combine result sets of two or more SELECT statements. UNION removes duplicate rows from the combined result; UNION ALL includes all rows, including duplicates.

**Q11. Difference between the HAVING clause and the WHERE clause?**
WHERE filters rows based on a condition **before** the data is grouped or aggregated — it operates on individual rows. HAVING filters grouped rows **after** the data is grouped or aggregated using GROUP BY.

**Q12. What is a transaction in SQL?**
A sequence of SQL statements executed as a single logical unit of work. It ensures data consistency and integrity by either committing all changes or rolling them back if an error occurs.

**Q13. Difference between a clustered and a non-clustered index?**
A clustered index determines the physical order of data in a table — it changes how data is stored on disk, and a table can have only one. A non-clustered index does not affect the physical order; it is stored separately and contains a pointer to the actual data. A table can have multiple non-clustered indexes.

**Q14. What is ACID in the context of database transactions?**
ACID stands for Atomicity, Consistency, Isolation and Durability — a set of properties that guarantee reliable processing of database transactions.
- **Atomicity** ensures a transaction is treated as a single unit of work — either all or none of the changes are applied.
- **Consistency** ensures a transaction brings the database from one valid state to another.
- **Isolation** ensures concurrent transactions do not interfere with each other.
- **Durability** ensures that once a transaction is committed, its changes are permanent and survive system failures.

**Q15. What is a deadlock?**
When two or more transactions are waiting for each other to release resources, creating a circular dependency. None of the transactions can proceed, and the system may become unresponsive.

**Q16. Difference between a database and a schema?**
A database is a container holding multiple objects — tables, views, indexes, procedures — representing a logical grouping of related data. A schema is a container *within* a database that holds objects and defines their ownership, providing a way to organize and manage database objects.

**Q17. Difference between a temporary table and a table variable?**
A temporary table is created and exists only for the duration of a session or transaction; it can be explicitly dropped or is automatically dropped when the session/transaction ends. A table variable stores a table-like structure **in memory**, has limited scope within a batch, stored procedure or function, and is automatically deallocated when that scope ends.

**Q18. What is the purpose of the GROUP BY clause?**
To group rows based on one or more columns. Typically used with aggregate functions (SUM, AVG, COUNT, etc.) to perform calculations on grouped data.

**Q19. Difference between CHAR and VARCHAR data types?**
CHAR is a fixed-length string data type; VARCHAR is a variable-length string data type.

**Q20. What is a stored procedure?**
A set of SQL statements stored in the database that can be executed repeatedly. It provides code reusability and better performance.

**Q21. What is a subquery?**
A query nested inside another query, used to retrieve data based on the result of the inner query.

**Q22. What is a view?**
A virtual table based on the result of a SQL statement. It allows users to retrieve and manipulate data as if it were a real table.

**Q23. Difference between a cross join and an inner join?**
A cross join (Cartesian product) returns the combination of all rows from two or more tables. An inner join returns only the matching rows based on a join condition.

**Q24. What is the purpose of the COMMIT statement?**
To save changes made in a transaction permanently. It ends the transaction and makes the changes visible to other users.

**Q25. What is the purpose of the ROLLBACK statement?**
To undo changes made in a transaction, reverting the database to its previous state before the transaction started.

**Q26. What is the purpose of the NULL value in SQL?**
NULL represents the absence of a value, or an unknown value. It is different from zero and from an empty string, and requires special handling in queries (`IS NULL`, not `= NULL`).

**Q27. Difference between a view and a materialized view?**
A materialized view is a **physical copy** of the view's result set stored in the database and updated periodically. It improves query performance at the cost of data freshness.

**Q28. What is a correlated subquery?**
A subquery that refers to a column from the outer query. It executes once for each row processed by the outer query.

**Q29. What is the purpose of the DISTINCT keyword?**
To retrieve unique values from a column or combination of columns in a SELECT statement.

**Q30. Difference between the CHAR and VARCHAR data types?** *(asked twice in the original set)*
CHAR stores fixed-length character strings; VARCHAR stores variable-length character strings. The storage size of CHAR is constant, while VARCHAR adjusts dynamically.

**Q31. Difference between the IN and EXISTS operators?**
The IN operator checks for a value within a set of values or the result of a subquery. The EXISTS operator checks for the **existence** of rows returned by a subquery.

**Q32. What is the purpose of the TRIGGER statement?**
To associate a set of SQL statements with a specific event in the database. It executes automatically when the event occurs.

**Q33. Difference between a unique constraint and a unique index?**
A unique constraint ensures the uniqueness of values in one or more columns. A unique index enforces the uniqueness **and also improves query performance**.

**Q34. What is the purpose of the TOP or LIMIT clause?**
To limit the number of rows returned by a query — `TOP` in SQL Server, `LIMIT` in MySQL. Often used with an ORDER BY clause.

**Q35. Difference between the UNION and JOIN operators?**
UNION combines the result sets of two or more SELECT statements **vertically**. JOIN combines columns from two or more tables **horizontally** based on a join condition.

**Q36. What is a data warehouse?**
A large, centralized repository that stores and manages data from various sources. It is designed for efficient reporting, analysis and business intelligence.

**Q37. Difference between a primary key and a candidate key?**
A primary key is a **chosen** candidate key that uniquely identifies a row. A candidate key is a set of one or more columns that could potentially become the primary key.

**Q38. What is the purpose of the GRANT statement?**
To grant specific permissions or privileges to users or roles in a database.

**Q39. What is a correlated update?**
An UPDATE statement that refers to a column from the same table in a subquery. It updates values based on the subquery's result for each row.

**Q40. What is the purpose of the CASE statement?**
To perform conditional logic in SQL queries, returning different values based on specified conditions.

**Q41. What is the purpose of the COALESCE function?**
Returns the first non-null expression from a list of expressions. Often used to handle null values effectively.

**Q42. What is the purpose of the ROW_NUMBER() function?**
Assigns a unique incremental number to each row in the result set. Commonly used for pagination or ranking.

**Q43. Difference between a natural join and an inner join?**
A natural join is an inner join that matches rows based on columns with the **same name** in the joined tables — the columns are determined automatically by the database.

**Q44. What is the purpose of the CASCADE DELETE constraint?**
To automatically delete related rows in child tables when a row in the parent table is deleted.

**Q45. What is the purpose of the ALL keyword in SQL?**
`ALL` compares a value against **every** value returned by a subquery — the condition is true only if it holds for all of them. (`> ALL` is equivalent to greater than the maximum.)

**Q46. Difference between the EXISTS and NOT EXISTS operators?**
EXISTS returns true if a subquery returns **any** rows; NOT EXISTS returns true if a subquery returns **no** rows.

**Q47. What is the purpose of the CROSS APPLY operator?**
Used to invoke a table-valued function for each row of a table expression, returning the combined result set. (SQL Server's equivalent of PostgreSQL's `LATERAL`.)

**Q48. What is a self-join?**
A join operation where a table is joined with itself. Useful when you want to compare rows within the same table based on related columns. It requires table aliases.

**Q49. What is an ALIAS command?**
ALIAS is a name that can be given to any table or column. This alias name can be referred to in the WHERE clause to identify a particular table or column.

**Q50. Why are SQL functions used?**
- To perform some calculations on the data
- To modify individual data items
- To manipulate the output
- To format dates and numbers
- To convert data types

---

# SECTION C — REAL INTERVIEW QUESTIONS (10–20 LPA PACKAGE)

## C1. SQL Questions (Q1–Q20)

**Q1. Write a query to find employees with the second highest salary.**
```sql
SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```
The inner query finds the highest salary; the outer query then finds the maximum salary less than that.

> **Tip:** to handle ties or retrieve multiple employees with the same second-highest salary, use `DENSE_RANK()` with a CTE.

**Q2. Explain the difference between INNER JOIN and OUTER JOIN with examples.**

INNER JOIN — returns only matching records from both tables:
```sql
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;
```
Output: only employees who belong to a department.

LEFT OUTER JOIN — all records from the left table, matching from the right; NULL if no match:
```sql
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id;
```
Output: all employees, with department info where available.

RIGHT OUTER JOIN — all records from the right table, matching from the left.
FULL OUTER JOIN — all records from both tables, matching where possible.

**Key difference:** INNER JOIN = intersection (matched data only). OUTER JOIN = union + NULLs (matched + unmatched data).

**Q3. Write a query to fetch the second-highest salary from an employee table.**
```sql
-- Option 1: DISTINCT + ORDER BY + LIMIT (MySQL/PostgreSQL)
SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;

-- Option 2: subquery (generic SQL)
SELECT MAX(salary) FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

**Q4. How do you use GROUP BY and HAVING together?**
Use GROUP BY to group data and HAVING to filter aggregated results (unlike WHERE, which filters raw rows).
```sql
SELECT department_id, COUNT(*) AS emp_count
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5;
```

**Q5. Write a query to find employees earning more than their managers.**
Assuming `employees(emp_id, name, salary, manager_id)`:
```sql
SELECT e.name AS employee_name, e.salary,
       m.name AS manager_name, m.salary AS manager_salary
FROM employees e
JOIN employees m ON e.manager_id = m.emp_id
WHERE e.salary > m.salary;
```
A self-join matches employees (`e`) with their managers (`m`), then filters where the employee's salary exceeds the manager's.

**Q6. What is a window function? Provide examples of ROW_NUMBER and RANK.**
A window function performs calculations across a set of table rows related to the current row — without collapsing rows like GROUP BY.
```sql
FUNCTION_NAME() OVER (PARTITION BY column ORDER BY column)
```
```sql
-- ROW_NUMBER: unique sequential number within a partition
SELECT name, department, salary,
       ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS row_num
FROM employees;

-- RANK: same rank for equal values, then skips
SELECT name, department, salary,
       RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_num
FROM employees;
```
If 2 employees have the same salary, both get rank 1 and the next gets rank 3.

**Q7. Write a query to fetch the top 3 performing products based on sales.**
```sql
SELECT product_id, product_name, total_sales
FROM sales_data
ORDER BY total_sales DESC
LIMIT 3;

-- Alternative using RANK() if ties matter:
SELECT product_id, product_name, total_sales
FROM (
  SELECT *, RANK() OVER (ORDER BY total_sales DESC) AS rank_num
  FROM sales_data
) ranked_sales
WHERE rank_num <= 3;
```

**Q8. Explain the difference between UNION and UNION ALL.**

| Feature | UNION | UNION ALL |
|---------|-------|-----------|
| Duplicates | Removes duplicates | Keeps all rows, including duplicates |
| Performance | Slower (because of sorting) | Faster (no de-duplication) |
| Use case | When you want distinct rows | When duplicates are meaningful |

```sql
SELECT city FROM customers UNION SELECT city FROM vendors;      -- unique list
SELECT city FROM customers UNION ALL SELECT city FROM vendors;  -- all, with duplicates
```

**Q9. How do you use a CASE statement?**
```sql
SELECT name, salary,
       CASE
           WHEN salary >= 100000 THEN 'High'
           WHEN salary >= 50000  THEN 'Medium'
           ELSE 'Low'
       END AS salary_category
FROM employees;
```
Works inside SELECT, WHERE, ORDER BY, etc.

**Q10. Write a query to calculate the cumulative sum of sales.**
```sql
SELECT order_date, product_id, sales_amount,
       SUM(sales_amount) OVER (PARTITION BY product_id ORDER BY order_date)
       AS cumulative_sales
FROM sales;
```
PARTITION BY groups by product; ORDER BY ensures the accumulation follows chronological order.

**Q11. What is a CTE, and how is it used?**
A CTE (Common Table Expression) is a temporary, named result set you can reference within a SQL query. It improves readability and simplifies complex subqueries or recursive logic.
```sql
WITH HighEarners AS (
    SELECT emp_id, name, salary
    FROM employees
    WHERE salary > 100000
)
SELECT * FROM HighEarners;
```
Benefits: reusable and readable; allows recursion (hierarchical data); avoids repeating subqueries.

**Q12. Write a query to identify customers who have made transactions above $5,000 multiple times.**
```sql
SELECT customer_id, COUNT(*) AS high_value_txns
FROM transactions
WHERE transaction_amount > 5000
GROUP BY customer_id
HAVING COUNT(*) > 1;
```

**Q13. Explain the difference between DELETE and TRUNCATE.**

| Feature | DELETE | TRUNCATE |
|---------|--------|----------|
| Removes rows | Yes (can use a WHERE condition) | Yes (removes all rows) |
| WHERE supported? | Yes | No |
| Logging | Logs each deleted row (slower) | Minimal logging (faster) |
| Rollback | Can be rolled back (within a transaction) | Can be rolled back in some RDBMS |
| Identity reset | Retains identity | Resets identity (in most DBs) |
| Use case | Partial deletion or audit trail needed | Full data wipe without audit needed |

**Q14. How do you optimize SQL queries for better performance?**
1. **Use SELECT with only required columns**
   ```sql
   -- Bad
   SELECT * FROM orders;
   -- Good
   SELECT order_id, customer_id FROM orders;
   ```
2. **Create proper indexes** — index frequently used columns in JOIN, WHERE, ORDER BY.
3. **Avoid functions on indexed columns**
   ```sql
   -- Slower (cannot use index)
   WHERE YEAR(order_date) = 2024
   -- Better
   WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31'
   ```
4. **Use EXISTS instead of IN** for subqueries
   ```sql
   SELECT name FROM customers c
   WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id);
   ```
5. **Avoid unnecessary joins or nested subqueries.**
6. **Use appropriate data types and avoid implicit conversions.**
7. **Analyze execution plans** (`EXPLAIN` or `EXPLAIN ANALYZE`).

**Q15. Write a query to find all customers who have not made any purchases in the last 6 months.**
```sql
SELECT c.customer_id, c.name
FROM customers c
LEFT JOIN transactions t
  ON c.customer_id = t.customer_id
 AND t.transaction_date >= CURRENT_DATE - INTERVAL '6 months'
WHERE t.customer_id IS NULL;
```
LEFT JOIN includes all customers; `WHERE t.customer_id IS NULL` keeps only those with no purchase in the window.

**Q16. How do you handle NULL values in SQL?**
1. `IS NULL` / `IS NOT NULL`:
   ```sql
   SELECT * FROM employees WHERE manager_id IS NULL;
   ```
2. Replace NULL using `COALESCE()` or `IFNULL()` (MySQL):
   ```sql
   SELECT name, COALESCE(phone_number, 'Not Provided') AS contact FROM customers;
   ```
3. NULLs in aggregation — these functions ignore NULLs by default:
   ```sql
   SELECT AVG(salary) FROM employees;
   ```
4. Conditional checks:
   ```sql
   SELECT name,
          CASE WHEN salary IS NULL THEN 'Unknown' ELSE 'Known' END AS salary_status
   FROM employees;
   ```

**Q17. Write a query to transpose rows into columns.**
Using CASE:
```sql
SELECT region,
       SUM(CASE WHEN month = 'Jan' THEN sales_amount ELSE 0 END) AS Jan,
       SUM(CASE WHEN month = 'Feb' THEN sales_amount ELSE 0 END) AS Feb,
       SUM(CASE WHEN month = 'Mar' THEN sales_amount ELSE 0 END) AS Mar
FROM sales
GROUP BY region;
```
Using PIVOT (SQL Server / Oracle):
```sql
SELECT region, [Jan], [Feb], [Mar]
FROM (SELECT region, month, sales_amount FROM sales) AS src
PIVOT (SUM(sales_amount) FOR month IN ([Jan], [Feb], [Mar])) AS p;
```

**Q18. Explain indexing and how it improves query performance.**
An index is a data structure that improves the speed of data retrieval on a table, at the cost of additional space and write-time performance.

| Feature | With Index | Without Index |
|---------|-----------|---------------|
| Search performance | Fast (uses binary/tree search) | Slow (scans every row — full scan) |
| Used in | WHERE, JOIN, ORDER BY, GROUP BY | Inefficient for large datasets |
| Types | B-tree (default), Bitmap, Hash, etc. | — |

```sql
CREATE INDEX idx_customer_id ON transactions(customer_id);
-- helps: SELECT * FROM transactions WHERE customer_id = 101;
```

Important notes:
- Too many indexes can slow down INSERT/UPDATE.
- Avoid indexing columns with low cardinality (e.g. gender).
- Use composite indexes when querying multiple columns together.

**Q19. Write a query to fetch the maximum transaction amount for each customer.**
```sql
SELECT customer_id, MAX(amount) AS max_transaction
FROM transactions
GROUP BY customer_id;
```

**Q20. What is a self-join, and how is it used?**
A regular join where a table is joined with itself. Useful when rows in a table are related to other rows in the same table.

| emp_id | name | manager_id |
|--------|------|------------|
| 1 | Alice | NULL |
| 2 | Bob | 1 |
| 3 | Carol | 1 |
| 4 | David | 2 |

```sql
SELECT e.name AS employee_name, m.name AS manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.emp_id;
```
`e` is an alias for employees (as employee); `m` is another alias for the same table (as manager). The join links an employee to their manager using `manager_id = emp_id`.

---

## C2. Data Analysis / Scenario-Based Questions (Q21–Q30)

**Q21. How would you design a database to store credit card transaction data?**
Normalize the structure while keeping it scalable, secure and query-efficient.

Suggested schema:
1. **Customers Table** — `customer_id` (PK), name, email, phone, address
2. **Cards Table** — `card_id` (PK), `customer_id` (FK), card_number (masked), card_type, status, issued_date
3. **Merchants Table** — `merchant_id` (PK), name, category, location
4. **Transactions Table** — `transaction_id` (PK), `card_id` (FK), `merchant_id` (FK), transaction_date, amount, currency, status, location

Best practices:
- Mask sensitive fields (like card numbers).
- Store `card_number` encrypted or tokenized.
- Use partitioning on date fields for faster querying.
- Add indexes on `card_id`, `merchant_id`, `transaction_date`.

**Q22. Write a query to identify the most profitable regions based on transaction data.**
```sql
SELECT region, SUM(amount) AS total_revenue
FROM transactions
GROUP BY region
ORDER BY total_revenue DESC
LIMIT 3;
```
Optional: calculate profit by subtracting costs if a cost column is present.

**Q23. How would you analyze customer churn using SQL?**

**Step 1: Define churn.** Say a churned customer is one who hasn't transacted in the last 6 months.

**Step 2: Sample schema.** `customers(customer_id, name, signup_date)` and `transactions(customer_id, transaction_date, amount)`.

**Step 3: Query to identify churned customers**
```sql
SELECT c.customer_id, c.name
FROM customers c
LEFT JOIN transactions t
  ON c.customer_id = t.customer_id
 AND t.transaction_date >= CURRENT_DATE - INTERVAL '6 months'
WHERE t.transaction_id IS NULL;
```

**Step 4: Analyze churn metrics**
- Churn rate = (Churned Customers / Total Customers) × 100
- Monthly churn trend
- Compare churned vs active customers in terms of average spend

**Q24. Explain the difference between OLAP and OLTP databases.**

| Feature | OLTP (Online Transaction Processing) | OLAP (Online Analytical Processing) |
|---------|--------------------------------------|-------------------------------------|
| Purpose | Handles real-time transactional queries | Used for analytical/reporting queries |
| Operations | INSERT, UPDATE, DELETE | SELECT (aggregate, group, slice, dice) |
| Data Structure | Highly normalized (3NF) | De-normalized (star/snowflake schema) |
| Speed | Fast for read/write of single rows | Fast for complex analytical queries |
| Examples | Banking systems, e-commerce order processing | Business intelligence, dashboards, sales trends |
| Users | Clerks, DBAs | Analysts, data scientists |
| Backup/Recovery | Essential and frequent | Less frequent |

In short: OLTP = operational, fast, real-time transactions. OLAP = analytical, slow-changing, historical data.

**Q25. How would you determine the Average Revenue Per User (ARPU) from transaction data?**
ARPU = Total Revenue / Total Number of Users
```sql
SELECT SUM(amount) * 1.0 / COUNT(DISTINCT customer_id) AS ARPU
FROM transactions;
```
Multiply by 1.0 to ensure float division. Monthly ARPU:
```sql
SELECT DATE_TRUNC('month', transaction_date) AS month,
       SUM(amount) * 1.0 / COUNT(DISTINCT customer_id) AS monthly_arpu
FROM transactions
GROUP BY month
ORDER BY month;
```

**Q26. Describe a scenario where you would use a LEFT JOIN instead of an INNER JOIN.**
Use LEFT JOIN when you want all records from the left table, even if there's no matching record in the right table.

Real-life scenario — "List all customers and their transactions, even if they haven't made any":
```sql
SELECT c.customer_id, c.name, t.transaction_id, t.amount
FROM customers c
LEFT JOIN transactions t ON c.customer_id = t.customer_id;
```
This shows all customers, including those with no transactions (returning NULLs for those). Using INNER JOIN would exclude customers with zero activity.

**Q27. Write a query to calculate YoY (Year-over-Year) growth for a set of transactions.**

Step 1 — extract year-wise revenue:
```sql
SELECT EXTRACT(YEAR FROM transaction_date) AS year, SUM(amount) AS total_revenue
FROM transactions
GROUP BY EXTRACT(YEAR FROM transaction_date);
```

Step 2 — calculate YoY growth using a CTE and self-join:
```sql
WITH yearly_revenue AS (
    SELECT EXTRACT(YEAR FROM transaction_date) AS year, SUM(amount) AS total_revenue
    FROM transactions
    GROUP BY EXTRACT(YEAR FROM transaction_date)
)
SELECT curr.year AS current_year,
       curr.total_revenue,
       prev.total_revenue AS previous_year_revenue,
       ROUND(((curr.total_revenue - prev.total_revenue) / prev.total_revenue) * 100, 2)
         AS yoy_growth_percent
FROM yearly_revenue curr
LEFT JOIN yearly_revenue prev ON curr.year = prev.year + 1;
```

**Q28. How would you implement fraud detection using transactional data?**
Fraud detection involves pattern recognition, anomaly detection and rule-based filtering.

| Type | Rule |
|------|------|
| Unusual Amounts | Flag transactions > 3× the average amount of that user |
| Rapid Repeats | Detect multiple transactions from the same user within seconds |
| Location Mismatch | Transactions from different countries within a short time |
| Card Sharing | Same card used by different customers or IPs |

Example — unusually high amount per user:
```sql
WITH avg_txn AS (
    SELECT customer_id, AVG(amount) AS avg_amount
    FROM transactions
    GROUP BY customer_id
)
SELECT t.*
FROM transactions t
JOIN avg_txn a ON t.customer_id = a.customer_id
WHERE t.amount > 3 * a.avg_amount;
```

**Q29. Write a query to find customers who have used more than 2 credit cards for transactions in a given month.**
```sql
SELECT customer_id,
       TO_CHAR(transaction_date, 'YYYY-MM') AS txn_month,
       COUNT(DISTINCT card_id) AS cards_used
FROM transactions
GROUP BY customer_id, TO_CHAR(transaction_date, 'YYYY-MM')
HAVING COUNT(DISTINCT card_id) > 2;
```

**Q30. How would you approach a business problem where you need to analyze the spending patterns of premium customers?**

**Step 1: Understand the Objective**
- Clarify with stakeholders what "spending pattern" means — frequency, amount, category, channel, or timing?
- Define "premium customer" — based on credit score, card tier (Platinum, Centurion), monthly spend threshold, etc.

**Step 2: Data Collection**
- Customer table (ID, tier, demographics)
- Transactions table (amount, date, category, location)
- Cards table (card_type, limits, activation)

**Step 3: Data Cleaning & Preparation**
- Handle missing values and outliers.
- Filter to premium customers using the defined criteria.
- Enrich data (categorize merchant types or locations).

**Step 4: Exploratory Data Analysis**

| Focus Area | Example Analysis |
|------------|------------------|
| Spend Amount | Average monthly/yearly spend |
| Time Trends | Seasonality or weekly spending behavior |
| Categories | Where they spend most (Travel, Dining, Shopping) |
| Geography | City or region-wise behavior |
| Trends | Is their spend increasing/decreasing YoY? |

**Step 5: Segmentation**
- Use clustering or thresholds to group premium customers into high spenders, frequent spenders, category loyalists (e.g. only travel).
- Identify anomalies or subgroups with unique patterns.

**Step 6: Business Recommendations**
- Personalize rewards or offers based on their dominant categories.
- Enhance retention strategies for segments showing decline.
- Promote premium card upgrades based on usage patterns.

**Bonus SQL** — top 3 spending categories of premium customers monthly:
```sql
SELECT customer_id,
       DATE_TRUNC('month', transaction_date) AS txn_month,
       category,
       SUM(amount) AS total_spend
FROM transactions
WHERE customer_id IN (SELECT customer_id FROM customers WHERE tier = 'Premium')
GROUP BY customer_id, txn_month, category
ORDER BY customer_id, txn_month, total_spend DESC;
```

---

# SECTION D — 350 PRACTICE QUESTIONS WITH WORKING SOLUTIONS

> 350 real, scenario-based SQL problems with working query solutions — covering joins, aggregation, ranking, window functions, dates, subqueries, recursive CTEs, schema design, performance tuning, and the toughest senior-level interview favourites.
> **Level:** Beginner → Senior · **Topics:** 16 · **Dialect:** ANSI / PostgreSQL

## Index

| # | Section | Range |
|---|---------|-------|
| 01 | Basic Filtering & Aggregation | Q1–Q25 |
| 02 | Joins-Based Problems | Q26–Q54 |
| 03 | Duplicates, Ranking & Nth Value | Q55–Q83 |
| 04 | Window Functions in Practice | Q84–Q112 |
| 05 | Date & Time Problems | Q113–Q132 |
| 06 | GROUP BY / HAVING Puzzles | Q133–Q152 |
| 07 | Subqueries & CTEs | Q153–Q172 |
| 08 | String & Pattern Problems | Q173–Q187 |
| 09 | Real Interview Favorites / Hard | Q188–Q200 |
| 10 | Advanced Window Functions & Analytics | Q201–Q225 |
| 11 | Advanced Recursive CTEs & Hierarchies | Q226–Q245 |
| 12 | Complex JOIN Patterns | Q246–Q270 |
| 13 | Advanced Aggregation Pipelines | Q271–Q290 |
| 14 | Schema Modifications & DDL | Q291–Q315 |
| 15 | Performance Tuning & Query Optimization | Q316–Q335 |
| 16 | Senior-Level Interview Challenges | Q336–Q350 |

---

## D01 — Basic Filtering & Aggregation (Q1–Q25)

*Foundational SELECT, WHERE, GROUP BY and aggregate-function problems every SQL practitioner must master.*

**Q1. Find employees earning more than the company average salary.**
```sql
SELECT *
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

**Q2. Count the number of employees in each department.**
```sql
SELECT department_id, COUNT(*) AS total_employees
FROM employees
GROUP BY department_id;
```

**Q3. Find employees who do not have a manager assigned.**
```sql
SELECT * FROM employees WHERE manager_id IS NULL;
```

**Q4. Find all employees whose email is missing (NULL).**
```sql
SELECT * FROM employees WHERE email IS NULL;
```

**Q5. Find employees hired in the current year.**
```sql
SELECT *
FROM employees
WHERE EXTRACT(YEAR FROM join_date) = EXTRACT(YEAR FROM CURRENT_DATE);
```

**Q6. Find the top 3 highest paid employees in each department.**
```sql
SELECT *
FROM (
  SELECT e.*,
         ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rnk
  FROM employees e
) ranked
WHERE rnk <= 3;
```

**Q7. Find employees whose name starts with 'A'.**
```sql
SELECT * FROM employees WHERE name LIKE 'A%';
```

**Q8. Find employees whose name ends with 'n'.**
```sql
SELECT * FROM employees WHERE name LIKE '%n';
```

**Q9. Find the total salary expense per department.**
```sql
SELECT department_id, SUM(salary) AS total_salary
FROM employees
GROUP BY department_id;
```

**Q10. Find the highest and lowest salary in the company.**
```sql
SELECT MAX(salary) AS highest_salary, MIN(salary) AS lowest_salary FROM employees;
```

**Q11. Find employees who earn between 40000 and 80000.**
```sql
SELECT * FROM employees WHERE salary BETWEEN 40000 AND 80000;
```

**Q12. Find the number of distinct job titles in the company.**
```sql
SELECT COUNT(DISTINCT job_title) AS distinct_titles FROM employees;
```

**Q13. Find employees whose salary is not NULL and greater than zero.**
```sql
SELECT * FROM employees WHERE salary IS NOT NULL AND salary > 0;
```

**Q14. Find all employees sorted by salary in descending order.**
```sql
SELECT * FROM employees ORDER BY salary DESC;
```

**Q15. Find the second lowest salary in the employees table.**
```sql
SELECT MIN(salary) AS second_lowest
FROM employees
WHERE salary > (SELECT MIN(salary) FROM employees);
```

**Q16. Find departments having an average salary above 50000.**
```sql
SELECT department_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 50000;
```

**Q17. Find employees whose job title is either 'Manager' or 'Director'.**
```sql
SELECT * FROM employees WHERE job_title IN ('Manager','Director');
```

**Q18. Find employees who joined between two given dates.**
```sql
SELECT * FROM employees WHERE join_date BETWEEN '2023-01-01' AND '2023-12-31';
```

**Q19. Count how many employees have a salary above 100000.**
```sql
SELECT COUNT(*) AS high_earners FROM employees WHERE salary > 100000;
```

**Q20. Find the average salary rounded to two decimal places.**
```sql
SELECT ROUND(AVG(salary), 2) AS avg_salary FROM employees;
```

**Q21. List unique department IDs from the employees table.**
```sql
SELECT DISTINCT department_id FROM employees;
```

**Q22. Find employees with a salary exactly equal to the maximum salary.**
```sql
SELECT * FROM employees WHERE salary = (SELECT MAX(salary) FROM employees);
```

**Q23. Find the total number of employees in the company.**
```sql
SELECT COUNT(*) AS total_employees FROM employees;
```

**Q24. Find employees whose name contains the substring 'an'.**
```sql
SELECT * FROM employees WHERE name LIKE '%an%';
```

**Q25. Find the 5 most recently hired employees.**
```sql
SELECT * FROM employees ORDER BY join_date DESC LIMIT 5;
```

---

## D02 — Joins-Based Problems (Q26–Q54)

*Multi-table problems testing INNER, LEFT, RIGHT and SELF joins on real-world schemas.*

**Q26. Find employees who are not assigned to any department.**
```sql
SELECT e.*
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
WHERE d.department_id IS NULL;
```

**Q27. Find customers who have never placed an order.**
```sql
SELECT c.*
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

**Q28. Find products that have never been sold.**
```sql
SELECT p.*
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
WHERE oi.product_id IS NULL;
```

**Q29. Display each employee along with their manager's name.**
```sql
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

**Q30. Find departments along with their employee count, including departments with zero employees.**
```sql
SELECT d.department_name, COUNT(e.id) AS employee_count
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name;
```

**Q31. Find students enrolled in more than 2 courses.**
```sql
SELECT student_id, COUNT(course_id) AS total_courses
FROM enrollments
GROUP BY student_id
HAVING COUNT(course_id) > 2;
```

**Q32. Find orphaned order_items rows whose product no longer exists.**
```sql
SELECT oi.*
FROM order_items oi
LEFT JOIN products p ON oi.product_id = p.product_id
WHERE p.product_id IS NULL;
```

**Q33. Find pairs of employees who work in the same department.**
```sql
SELECT e1.name AS employee1, e2.name AS employee2, e1.department_id
FROM employees e1
JOIN employees e2
  ON e1.department_id = e2.department_id
 AND e1.id < e2.id;
```

**Q34. Find customers who placed orders in 2024 along with their total spend.**
```sql
SELECT c.customer_id, c.name, SUM(o.amount) AS total_spend
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE EXTRACT(YEAR FROM o.order_date) = 2024
GROUP BY c.customer_id, c.name;
```

**Q35. Find products along with the category name they belong to.**
```sql
SELECT p.product_name, c.category_name
FROM products p
JOIN categories c ON p.category_id = c.category_id;
```

**Q36. Find employees who work in departments located in 'New York'.**
```sql
SELECT e.*
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE d.location = 'New York';
```

**Q37. Find the manager with the most direct reports.**
```sql
SELECT manager_id, COUNT(*) AS direct_reports
FROM employees
WHERE manager_id IS NOT NULL
GROUP BY manager_id
ORDER BY direct_reports DESC
LIMIT 1;
```

**Q38. Find all orders along with customer name and product name.**
```sql
SELECT o.order_id, c.name AS customer, p.product_name
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id;
```

**Q39. Find employees who share the same job title as 'John'.**
```sql
SELECT e2.*
FROM employees e1
JOIN employees e2 ON e1.job_title = e2.job_title
WHERE e1.name = 'John' AND e2.name <> 'John';
```

**Q40. Find departments that have at least one employee earning above 90000.**
```sql
SELECT DISTINCT d.department_name
FROM departments d
JOIN employees e ON d.department_id = e.department_id
WHERE e.salary > 90000;
```

**Q41. Find customers who ordered every product in a given category.**
```sql
SELECT o.customer_id
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE p.category_id = 1
GROUP BY o.customer_id
HAVING COUNT(DISTINCT p.product_id) = (
  SELECT COUNT(*) FROM products WHERE category_id = 1
);
```

**Q42. Find employees and the total number of projects each is assigned to.**
```sql
SELECT e.name, COUNT(pa.project_id) AS total_projects
FROM employees e
LEFT JOIN project_assignments pa ON e.id = pa.employee_id
GROUP BY e.name;
```

**Q43. Find vendors who supply products that are currently out of stock.**
```sql
SELECT DISTINCT v.vendor_name
FROM vendors v
JOIN products p ON v.vendor_id = p.vendor_id
WHERE p.stock_quantity = 0;
```

**Q44. Find the department with the highest total salary expense.**
```sql
SELECT d.department_name, SUM(e.salary) AS total_salary
FROM departments d
JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY total_salary DESC
LIMIT 1;
```

**Q45. Find customers who have placed orders for products costing more than 500.**
```sql
SELECT DISTINCT c.customer_id, c.name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE p.price > 500;
```

**Q46. Find employees who joined before their manager.**
```sql
SELECT e.name AS employee, m.name AS manager
FROM employees e
JOIN employees m ON e.manager_id = m.id
WHERE e.join_date < m.join_date;
```

**Q47. Find all combinations of employees and departments using a cross join (for testing).**
```sql
SELECT e.name, d.department_name
FROM employees e
CROSS JOIN departments d;
```

**Q48. Find suppliers who supply more than one category of product.**
```sql
SELECT vendor_id
FROM products
GROUP BY vendor_id
HAVING COUNT(DISTINCT category_id) > 1;
```

**Q49. Find the employee count for each manager, including managers with zero reports.**
```sql
SELECT m.id, m.name, COUNT(e.id) AS reports
FROM employees m
LEFT JOIN employees e ON e.manager_id = m.id
GROUP BY m.id, m.name;
```

**Q50. Find customers whose total order amount exceeds 10000.**
```sql
SELECT c.customer_id, c.name, SUM(o.amount) AS total_spend
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING SUM(o.amount) > 10000;
```

**Q51. Find products purchased by the same customers who bought product X.**
```sql
SELECT DISTINCT oi2.product_id
FROM order_items oi1
JOIN orders o1 ON oi1.order_id = o1.order_id
JOIN orders o2 ON o1.customer_id = o2.customer_id
JOIN order_items oi2 ON o2.order_id = oi2.order_id
WHERE oi1.product_id = 'X' AND oi2.product_id <> 'X';
```

**Q52. Find employees who have never been assigned to any project.**
```sql
SELECT e.*
FROM employees e
LEFT JOIN project_assignments pa ON e.id = pa.employee_id
WHERE pa.employee_id IS NULL;
```

**Q53. Find the average order amount per customer along with customer name.**
```sql
SELECT c.name, AVG(o.amount) AS avg_order_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.name;
```

**Q54. Find departments with more managers than regular employees.**
```sql
SELECT department_id
FROM employees
GROUP BY department_id
HAVING SUM(CASE WHEN job_title='Manager' THEN 1 ELSE 0 END) >
       SUM(CASE WHEN job_title<>'Manager' THEN 1 ELSE 0 END);
```

---

## D03 — Duplicates, Ranking & Nth Value (Q55–Q83)

*The most frequently asked interview pattern: finding duplicates and Nth highest/lowest values using several techniques.*

**Q55. Find the second highest salary from the employees table.**
```sql
SELECT MAX(salary) AS SecondHighestSalary
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

**Q56. Find the third highest salary using a window function.**
```sql
SELECT salary
FROM (
  SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM employees
) ranked
WHERE rnk = 3
LIMIT 1;
```

**Q57. Find the Nth highest salary using a generic, parameterised query.**
```sql
SELECT DISTINCT salary
FROM employees e1
WHERE (N - 1) = (
  SELECT COUNT(DISTINCT salary)
  FROM employees e2
  WHERE e2.salary > e1.salary
);
```

**Q58. Find duplicate records based on the employee name.**
```sql
SELECT name, COUNT(*) AS occurrences
FROM employees
GROUP BY name
HAVING COUNT(*) > 1;
```

**Q59. Delete duplicate rows keeping only one copy.**
```sql
DELETE FROM employees
WHERE id NOT IN (
  SELECT MIN(id)
  FROM employees
  GROUP BY name, email
);
```

**Q60. Find duplicate emails along with the number of times they occur.**
```sql
SELECT email, COUNT(*) AS total
FROM employees
GROUP BY email
HAVING COUNT(*) > 1;
```

**Q61. Rank employees by salary within each department.**
```sql
SELECT name, department_id, salary,
       RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS dept_rank
FROM employees;
```

**Q62. Find ties in salary ranking using DENSE_RANK.**
```sql
SELECT name, salary,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
FROM employees;
```

**Q63. Find the lowest salary in each department.**
```sql
SELECT department_id, MIN(salary) AS lowest_salary
FROM employees
GROUP BY department_id;
```

**Q64. Find the second highest salary per department.**
```sql
SELECT department_id, salary
FROM (
  SELECT department_id, salary,
         DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rnk
  FROM employees
) ranked
WHERE rnk = 2;
```

**Q65. Find rows that are exact duplicates across all columns.**
```sql
SELECT name, email, salary, department_id, COUNT(*)
FROM employees
GROUP BY name, email, salary, department_id
HAVING COUNT(*) > 1;
```

**Q66. Find employees with a unique (non-duplicated) salary value.**
```sql
SELECT salary
FROM employees
GROUP BY salary
HAVING COUNT(*) = 1;
```

**Q67. Assign a row number to each employee ordered by hire date.**
```sql
SELECT name, join_date,
       ROW_NUMBER() OVER (ORDER BY join_date) AS hire_sequence
FROM employees;
```

**Q68. Find the top 1 highest paid employee per job title using RANK.**
```sql
SELECT *
FROM (
  SELECT *, RANK() OVER (PARTITION BY job_title ORDER BY salary DESC) AS rnk
  FROM employees
) ranked
WHERE rnk = 1;
```

**Q69. Remove duplicate customer records keeping the most recently updated one.**
```sql
DELETE FROM customers
WHERE customer_id NOT IN (
  SELECT customer_id FROM (
    SELECT customer_id,
           ROW_NUMBER() OVER (PARTITION BY email ORDER BY updated_at DESC) AS rn
    FROM customers
  ) t
  WHERE rn = 1
);
```

**Q70. Find the Nth highest order amount per customer.**
```sql
SELECT customer_id, amount
FROM (
  SELECT customer_id, amount,
         DENSE_RANK() OVER (PARTITION BY customer_id ORDER BY amount DESC) AS rnk
  FROM orders
) ranked
WHERE rnk = 2;
```

**Q71. Find duplicate phone numbers shared by multiple customers.**
```sql
SELECT phone, COUNT(*) AS total
FROM customers
GROUP BY phone
HAVING COUNT(*) > 1;
```

**Q72. Use NTILE to split employees into 4 salary quartiles.**
```sql
SELECT name, salary,
       NTILE(4) OVER (ORDER BY salary) AS quartile
FROM employees;
```

**Q73. Find the second most expensive product in each category.**
```sql
SELECT category_id, product_name, price
FROM (
  SELECT category_id, product_name, price,
         DENSE_RANK() OVER (PARTITION BY category_id ORDER BY price DESC) AS rnk
  FROM products
) ranked
WHERE rnk = 2;
```

**Q74. Find employees whose salary matches another employee's salary exactly.**
```sql
SELECT e1.name, e1.salary
FROM employees e1
JOIN employees e2
  ON e1.salary = e2.salary AND e1.id <> e2.id;
```

**Q75. Keep only the latest order per customer, deleting older duplicates of the same product.**
```sql
DELETE FROM orders
WHERE order_id NOT IN (
  SELECT order_id FROM (
    SELECT order_id,
           ROW_NUMBER() OVER (PARTITION BY customer_id, product_id ORDER BY order_date DESC) AS rn
    FROM orders
  ) t
  WHERE rn = 1
);
```

**Q76. Find the rank of a specific employee's salary within the company.**
```sql
SELECT name, salary,
       RANK() OVER (ORDER BY salary DESC) AS overall_rank
FROM employees
WHERE name = 'John';
```

**Q77. Find duplicate rows in a transactions table based on amount and date.**
```sql
SELECT amount, transaction_date, COUNT(*)
FROM transactions
GROUP BY amount, transaction_date
HAVING COUNT(*) > 1;
```

**Q78. Find the highest salary that is not unique (shared by more than one employee).**
```sql
SELECT salary
FROM employees
GROUP BY salary
HAVING COUNT(*) > 1
ORDER BY salary DESC
LIMIT 1;
```

**Q79. Find the bottom 3 performing products by total sales using ranking.**
```sql
SELECT product_id, total_sales
FROM (
  SELECT product_id, SUM(quantity * price) AS total_sales,
         RANK() OVER (ORDER BY SUM(quantity * price) ASC) AS rnk
  FROM order_items
  GROUP BY product_id
) ranked
WHERE rnk <= 3;
```

**Q80. Find duplicate combinations of student and course in an enrollments table.**
```sql
SELECT student_id, course_id, COUNT(*)
FROM enrollments
GROUP BY student_id, course_id
HAVING COUNT(*) > 1;
```

**Q81. Find the percentile rank of each employee's salary.**
```sql
SELECT name, salary,
       PERCENT_RANK() OVER (ORDER BY salary) AS percentile_rank
FROM employees;
```

**Q82. Find employees who have the same salary as the department's average.**
```sql
SELECT e.*
FROM employees e
JOIN (
  SELECT department_id, AVG(salary) AS avg_salary
  FROM employees
  GROUP BY department_id
) d ON e.department_id = d.department_id AND e.salary = d.avg_salary;
```

**Q83. Keep only the first occurrence of each duplicate invoice number.**
```sql
DELETE FROM invoices
WHERE invoice_id NOT IN (
  SELECT MIN(invoice_id)
  FROM invoices
  GROUP BY invoice_number
);
```

---

## D04 — Window Functions in Practice (Q84–Q112)

*Running totals, moving averages, gaps-and-islands, and other analytics-style problems solved with OVER().*

**Q84. Calculate a running total of sales ordered by date.**
```sql
SELECT sale_date, amount,
       SUM(amount) OVER (ORDER BY sale_date) AS running_total
FROM sales;
```

**Q85. Calculate a 3-order moving average of order amounts per customer.**
```sql
SELECT customer_id, order_date, amount,
       AVG(amount) OVER (
         PARTITION BY customer_id
         ORDER BY order_date
         ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
       ) AS moving_avg
FROM orders;
```

**Q86. Find the difference between each order amount and the previous order amount for the same customer.**
```sql
SELECT customer_id, order_date, amount,
       amount - LAG(amount) OVER (PARTITION BY customer_id ORDER BY order_date) AS diff
FROM orders;
```

**Q87. Find the first and last order date for each customer.**
```sql
SELECT customer_id,
       MIN(order_date) AS first_order,
       MAX(order_date) AS last_order
FROM orders
GROUP BY customer_id;
```

**Q88. Find the cumulative distribution of employee salaries.**
```sql
SELECT name, salary,
       CUME_DIST() OVER (ORDER BY salary) AS cum_dist
FROM employees;
```

**Q89. Calculate year-over-year revenue growth.**
```sql
SELECT year, revenue,
       revenue - LAG(revenue) OVER (ORDER BY year) AS yoy_growth
FROM annual_revenue;
```

**Q90. Find the running count of orders placed by each customer.**
```sql
SELECT customer_id, order_date,
       COUNT(*) OVER (PARTITION BY customer_id ORDER BY order_date) AS order_sequence
FROM orders;
```

**Q91. Find the next order amount for each customer using LEAD.**
```sql
SELECT customer_id, order_date, amount,
       LEAD(amount) OVER (PARTITION BY customer_id ORDER BY order_date) AS next_amount
FROM orders;
```

**Q92. Find the highest salary so far for each employee ordered by date of raise.**
```sql
SELECT employee_id, raise_date, salary,
       MAX(salary) OVER (PARTITION BY employee_id ORDER BY raise_date) AS highest_so_far
FROM salary_history;
```

**Q93. Calculate the percentage contribution of each product's sales to the total sales.**
```sql
SELECT product_id, total_sales,
       ROUND(100.0 * total_sales / SUM(total_sales) OVER (), 2) AS pct_of_total
FROM (
  SELECT product_id, SUM(quantity * price) AS total_sales
  FROM order_items
  GROUP BY product_id
) t;
```

**Q94. Find the 3rd highest salary per department using NTH_VALUE.**
```sql
SELECT department_id,
       NTH_VALUE(salary, 3) OVER (
         PARTITION BY department_id ORDER BY salary DESC
         ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
       ) AS third_highest
FROM employees;
```

**Q95. Find the running maximum stock price per day.**
```sql
SELECT trade_date, price,
       MAX(price) OVER (ORDER BY trade_date) AS running_max
FROM stock_prices;
```

**Q96. Identify the rank of each customer based on total spend, without gaps.**
```sql
SELECT customer_id, total_spend,
       DENSE_RANK() OVER (ORDER BY total_spend DESC) AS spend_rank
FROM (
  SELECT customer_id, SUM(amount) AS total_spend
  FROM orders
  GROUP BY customer_id
) t;
```

**Q97. Find each employee's salary compared to the department average using window functions.**
```sql
SELECT name, department_id, salary,
       salary - AVG(salary) OVER (PARTITION BY department_id) AS diff_from_avg
FROM employees;
```

**Q98. Calculate the running total of expenses reset at the start of every month.**
```sql
SELECT expense_date, amount,
       SUM(amount) OVER (
         PARTITION BY DATE_TRUNC('month', expense_date)
         ORDER BY expense_date
       ) AS monthly_running_total
FROM expenses;
```

**Q99. Find the previous and next salary of each employee ordered by salary.**
```sql
SELECT name, salary,
       LAG(salary)  OVER (ORDER BY salary) AS prev_salary,
       LEAD(salary) OVER (ORDER BY salary) AS next_salary
FROM employees;
```

**Q100. Find the percentage change in monthly sales.**
```sql
SELECT month, total_sales,
       ROUND(100.0 * (total_sales - LAG(total_sales) OVER (ORDER BY month))
             / LAG(total_sales) OVER (ORDER BY month), 2) AS pct_change
FROM monthly_sales;
```

**Q101. Identify the first purchase made by each customer using window functions.**
```sql
SELECT *
FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rn
  FROM orders
) t
WHERE rn = 1;
```

**Q102. Find a 7-day rolling average of daily website visits.**
```sql
SELECT visit_date, visits,
       AVG(visits) OVER (
         ORDER BY visit_date
         ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
       ) AS rolling_7day_avg
FROM daily_visits;
```

**Q103. Find the gap in days between consecutive orders for each customer.**
```sql
SELECT customer_id, order_date,
       order_date - LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS days_gap
FROM orders;
```

**Q104. Rank products within each category by total revenue and keep only the top 2.**
```sql
SELECT *
FROM (
  SELECT category_id, product_id, total_revenue,
         RANK() OVER (PARTITION BY category_id ORDER BY total_revenue DESC) AS rnk
  FROM (
    SELECT p.category_id, oi.product_id, SUM(oi.quantity * oi.price) AS total_revenue
    FROM order_items oi
    JOIN products p ON oi.product_id = p.product_id
    GROUP BY p.category_id, oi.product_id
  ) rev
) ranked
WHERE rnk <= 2;
```

**Q105. Find the salary growth of each employee compared to their first recorded salary.**
```sql
SELECT employee_id, raise_date, salary,
       salary - FIRST_VALUE(salary) OVER (
         PARTITION BY employee_id ORDER BY raise_date
       ) AS growth_since_start
FROM salary_history;
```

**Q106. Find the median order amount using PERCENTILE_CONT.**
```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY amount) AS median_amount
FROM orders;
```

**Q107. Find customers whose spending increased in every consecutive quarter.**
```sql
SELECT customer_id
FROM (
  SELECT customer_id, quarter, amount,
         LAG(amount) OVER (PARTITION BY customer_id ORDER BY quarter) AS prev_amount
  FROM quarterly_spend
) t
GROUP BY customer_id
HAVING SUM(CASE WHEN amount <= prev_amount THEN 1 ELSE 0 END) = 0;
```

**Q108. Find the average time gap between orders for each customer.**
```sql
SELECT customer_id, AVG(gap_days) AS avg_gap
FROM (
  SELECT customer_id,
         order_date - LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS gap_days
  FROM orders
) t
GROUP BY customer_id;
```

**Q109. Find the top performing salesperson for each month.**
```sql
SELECT *
FROM (
  SELECT month, salesperson_id, total_sales,
         RANK() OVER (PARTITION BY month ORDER BY total_sales DESC) AS rnk
  FROM monthly_sales_by_rep
) ranked
WHERE rnk = 1;
```

**Q110. Find the cumulative number of new customers acquired each month.**
```sql
SELECT signup_month, new_customers,
       SUM(new_customers) OVER (ORDER BY signup_month) AS cumulative_customers
FROM (
  SELECT DATE_TRUNC('month', signup_date) AS signup_month, COUNT(*) AS new_customers
  FROM customers
  GROUP BY DATE_TRUNC('month', signup_date)
) t;
```

**Q111. Calculate the variance of each employee's salary from the company average.**
```sql
SELECT name, salary,
       salary - AVG(salary) OVER () AS variance_from_company_avg
FROM employees;
```

**Q112. Find the last value of stock price in each trading day partitioned by stock symbol.**
```sql
SELECT symbol, trade_date, price,
       LAST_VALUE(price) OVER (
         PARTITION BY symbol, trade_date ORDER BY trade_time
         ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
       ) AS closing_price
FROM stock_prices;
```

---

## D05 — Date & Time Problems (Q113–Q132)

*Handling temporal data: streaks, gaps, age calculations and time-bucketed aggregations.*

**Q113. Find employees who joined in the last 6 months.**
```sql
SELECT * FROM employees WHERE join_date >= CURRENT_DATE - INTERVAL '6 months';
```

**Q114. Find customers who logged in on consecutive days (a login streak).**
```sql
SELECT customer_id, login_date,
       login_date - ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY login_date)::INT
       AS streak_group
FROM logins;
```

**Q115. Find missing dates in a sequence of daily sales records.**
```sql
SELECT d.calendar_date
FROM calendar d
LEFT JOIN sales s ON d.calendar_date = s.sale_date
WHERE s.sale_date IS NULL
  AND d.calendar_date BETWEEN (SELECT MIN(sale_date) FROM sales)
                          AND (SELECT MAX(sale_date) FROM sales);
```

**Q116. Calculate each employee's age from their date of birth.**
```sql
SELECT name, dob,
       EXTRACT(YEAR FROM AGE(CURRENT_DATE, dob)) AS age
FROM employees;
```

**Q117. Find orders placed on weekends.**
```sql
SELECT * FROM orders WHERE EXTRACT(DOW FROM order_date) IN (0, 6);
```

**Q118. Find the number of monthly active users.**
```sql
SELECT DATE_TRUNC('month', activity_date) AS month,
       COUNT(DISTINCT user_id) AS active_users
FROM user_activity
GROUP BY DATE_TRUNC('month', activity_date);
```

**Q119. Find customers who have not placed an order in the last 90 days.**
```sql
SELECT c.*
FROM customers c
WHERE c.customer_id NOT IN (
  SELECT customer_id FROM orders
  WHERE order_date >= CURRENT_DATE - INTERVAL '90 days'
);
```

**Q120. Find the number of days between an employee's hire date and today.**
```sql
SELECT name, join_date, CURRENT_DATE - join_date AS days_employed
FROM employees;
```

**Q121. Find the busiest day of the week for orders.**
```sql
SELECT TO_CHAR(order_date,'Day') AS day_of_week, COUNT(*) AS total_orders
FROM orders
GROUP BY TO_CHAR(order_date,'Day')
ORDER BY total_orders DESC
LIMIT 1;
```

**Q122. Find employees whose work anniversary is this month.**
```sql
SELECT * FROM employees
WHERE EXTRACT(MONTH FROM join_date) = EXTRACT(MONTH FROM CURRENT_DATE);
```

**Q123. Find the total sales for each quarter of the year.**
```sql
SELECT EXTRACT(QUARTER FROM sale_date) AS quarter, SUM(amount) AS total_sales
FROM sales
GROUP BY EXTRACT(QUARTER FROM sale_date);
```

**Q124. Find the longest streak of consecutive days a user was active.**
```sql
SELECT user_id, MAX(streak_length) AS longest_streak
FROM (
  SELECT user_id, COUNT(*) AS streak_length
  FROM (
    SELECT user_id, activity_date,
           activity_date - ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY activity_date)::INT AS grp
    FROM user_activity
  ) t
  GROUP BY user_id, grp
) streaks
GROUP BY user_id;
```

**Q125. Find the average number of days between consecutive purchases for each customer.**
```sql
SELECT customer_id, AVG(days_between) AS avg_days_between
FROM (
  SELECT customer_id,
         order_date - LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS days_between
  FROM orders
) t
GROUP BY customer_id;
```

**Q126. Find all orders placed in the last 24 hours.**
```sql
SELECT * FROM orders WHERE order_timestamp >= NOW() - INTERVAL '24 hours';
```

**Q127. Find the month with the highest revenue.**
```sql
SELECT DATE_TRUNC('month', sale_date) AS month, SUM(amount) AS total_revenue
FROM sales
GROUP BY DATE_TRUNC('month', sale_date)
ORDER BY total_revenue DESC
LIMIT 1;
```

**Q128. Find employees who have completed exactly 5 years of service.**
```sql
SELECT * FROM employees WHERE join_date = CURRENT_DATE - INTERVAL '5 years';
```

**Q129. Convert a UTC timestamp column to a specific time zone.**
```sql
SELECT order_id, order_timestamp AT TIME ZONE 'UTC' AT TIME ZONE 'Asia/Kolkata' AS local_time
FROM orders;
```

**Q130. Find users who signed up but never logged in within 7 days.**
```sql
SELECT u.*
FROM users u
LEFT JOIN logins l ON u.user_id = l.user_id
  AND l.login_date BETWEEN u.signup_date AND u.signup_date + INTERVAL '7 days'
WHERE l.user_id IS NULL;
```

**Q131. Find the number of new customers acquired each week.**
```sql
SELECT DATE_TRUNC('week', signup_date) AS week, COUNT(*) AS new_customers
FROM customers
GROUP BY DATE_TRUNC('week', signup_date);
```

**Q132. Find orders that took more than 5 days to be shipped after being placed.**
```sql
SELECT * FROM orders WHERE shipped_date - order_date > 5;
```

---

## D06 — GROUP BY / HAVING Puzzles (Q133–Q152)

*Aggregation edge cases that frequently trip up candidates in real interviews.*

**Q133. Find departments having more than 5 employees.**
```sql
SELECT department_id, COUNT(*) AS num_employees
FROM employees
GROUP BY department_id
HAVING COUNT(*) > 5;
```

**Q134. Find products ordered by more than 10 distinct customers.**
```sql
SELECT oi.product_id, COUNT(DISTINCT o.customer_id) AS distinct_customers
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
GROUP BY oi.product_id
HAVING COUNT(DISTINCT o.customer_id) > 10;
```

**Q135. Find departments whose average salary is above the company average.**
```sql
SELECT department_id, AVG(salary) AS dept_avg
FROM employees
GROUP BY department_id
HAVING AVG(salary) > (SELECT AVG(salary) FROM employees);
```

**Q136. Find categories that have zero sales.**
```sql
SELECT c.category_id, c.category_name
FROM categories c
LEFT JOIN products p ON c.category_id = p.category_id
LEFT JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY c.category_id, c.category_name
HAVING SUM(oi.quantity) IS NULL;
```

**Q137. Find customers who have placed orders worth more than 5000 in total.**
```sql
SELECT customer_id, SUM(amount) AS total_spent
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 5000;
```

**Q138. Find job titles held by more than one employee.**
```sql
SELECT job_title, COUNT(*) AS total
FROM employees
GROUP BY job_title
HAVING COUNT(*) > 1;
```

**Q139. Find departments where the maximum salary is less than 60000.**
```sql
SELECT department_id, MAX(salary) AS max_salary
FROM employees
GROUP BY department_id
HAVING MAX(salary) < 60000;
```

**Q140. Find students who have failed more than 2 subjects.**
```sql
SELECT student_id, COUNT(*) AS failed_subjects
FROM results
WHERE grade = 'F'
GROUP BY student_id
HAVING COUNT(*) > 2;
```

**Q141. Find customers who ordered the same product more than 3 times.**
```sql
SELECT customer_id, product_id, COUNT(*) AS times_ordered
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
GROUP BY customer_id, product_id
HAVING COUNT(*) > 3;
```

**Q142. Find departments with a total headcount between 10 and 20.**
```sql
SELECT department_id, COUNT(*) AS headcount
FROM employees
GROUP BY department_id
HAVING COUNT(*) BETWEEN 10 AND 20;
```

**Q143. Find vendors supplying products with an average price above 1000.**
```sql
SELECT vendor_id, AVG(price) AS avg_price
FROM products
GROUP BY vendor_id
HAVING AVG(price) > 1000;
```

**Q144. Find months where total sales dropped below 10000.**
```sql
SELECT DATE_TRUNC('month', sale_date) AS month, SUM(amount) AS total_sales
FROM sales
GROUP BY DATE_TRUNC('month', sale_date)
HAVING SUM(amount) < 10000;
```

**Q145. Find employees grouped by job title having a combined salary above 500000.**
```sql
SELECT job_title, SUM(salary) AS total_salary
FROM employees
GROUP BY job_title
HAVING SUM(salary) > 500000;
```

**Q146. Find product categories with fewer than 5 products listed.**
```sql
SELECT category_id, COUNT(*) AS total_products
FROM products
GROUP BY category_id
HAVING COUNT(*) < 5;
```

**Q147. Find customers with orders in more than 3 different months.**
```sql
SELECT customer_id, COUNT(DISTINCT DATE_TRUNC('month', order_date)) AS active_months
FROM orders
GROUP BY customer_id
HAVING COUNT(DISTINCT DATE_TRUNC('month', order_date)) > 3;
```

**Q148. Find regions where total revenue exceeds 1 million.**
```sql
SELECT region, SUM(amount) AS total_revenue
FROM sales
GROUP BY region
HAVING SUM(amount) > 1000000;
```

**Q149. Find suppliers providing only a single product.**
```sql
SELECT vendor_id, COUNT(*) AS total_products
FROM products
GROUP BY vendor_id
HAVING COUNT(*) = 1;
```

**Q150. Find departments where the salary range (max-min) exceeds 50000.**
```sql
SELECT department_id, MAX(salary) - MIN(salary) AS salary_range
FROM employees
GROUP BY department_id
HAVING MAX(salary) - MIN(salary) > 50000;
```

**Q151. Find customers whose average order value is below 100.**
```sql
SELECT customer_id, AVG(amount) AS avg_order_value
FROM orders
GROUP BY customer_id
HAVING AVG(amount) < 100;
```

**Q152. Find employees grouped by department who collectively worked more than 1000 overtime hours.**
```sql
SELECT department_id, SUM(overtime_hours) AS total_overtime
FROM employees
GROUP BY department_id
HAVING SUM(overtime_hours) > 1000;
```

---

## D07 — Subqueries & CTEs (Q153–Q172)

*Correlated subqueries, recursive CTEs for hierarchies, and statistical queries like median and mode.*

**Q153. Find employees who earn more than their manager.**
```sql
SELECT e.name AS Employee, e.salary, m.name AS Manager, m.salary AS ManagerSalary
FROM employees e
JOIN employees m ON e.manager_id = m.id
WHERE e.salary > m.salary;
```

**Q154. Build the full organizational hierarchy using a recursive CTE.**
```sql
WITH RECURSIVE org_chart AS (
  SELECT id, name, manager_id, 1 AS level
  FROM employees
  WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id, oc.level + 1
  FROM employees e
  JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT * FROM org_chart ORDER BY level;
```

**Q155. Find the median salary in the employees table.**
```sql
SELECT AVG(salary) AS median_salary
FROM (
  SELECT salary
  FROM employees
  ORDER BY salary
  LIMIT 2 - (SELECT COUNT(*) FROM employees) % 2
  OFFSET (SELECT (COUNT(*) - 1) / 2 FROM employees)
) AS median_subquery;
```

**Q156. Find the mode (most frequently occurring salary).**
```sql
SELECT salary
FROM employees
GROUP BY salary
ORDER BY COUNT(*) DESC
LIMIT 1;
```

**Q157. Find each employee's level/depth in the reporting hierarchy.**
```sql
WITH RECURSIVE hierarchy AS (
  SELECT id, name, manager_id, 0 AS depth
  FROM employees
  WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id, h.depth + 1
  FROM employees e
  JOIN hierarchy h ON e.manager_id = h.id
)
SELECT * FROM hierarchy;
```

**Q158. Find customers whose total spend is greater than the average spend across all customers.**
```sql
SELECT customer_id, total_spend
FROM (
  SELECT customer_id, SUM(amount) AS total_spend
  FROM orders
  GROUP BY customer_id
) c
WHERE total_spend > (
  SELECT AVG(total_spend) FROM (
    SELECT SUM(amount) AS total_spend FROM orders GROUP BY customer_id
  ) avg_sub
);
```

**Q159. Use a CTE to simplify a multi-step sales summary report.**
```sql
WITH monthly_totals AS (
  SELECT DATE_TRUNC('month', sale_date) AS month, SUM(amount) AS total
  FROM sales
  GROUP BY DATE_TRUNC('month', sale_date)
)
SELECT month, total,
       total - LAG(total) OVER (ORDER BY month) AS month_over_month_change
FROM monthly_totals;
```

**Q160. Find products priced above the average price within their own category (correlated subquery).**
```sql
SELECT p1.*
FROM products p1
WHERE p1.price > (
  SELECT AVG(p2.price)
  FROM products p2
  WHERE p2.category_id = p1.category_id
);
```

**Q161. Find the total number of direct and indirect reports for each manager using a recursive CTE.**
```sql
WITH RECURSIVE reports AS (
  SELECT id, manager_id FROM employees
  WHERE manager_id IS NOT NULL
  UNION ALL
  SELECT e.id, r.manager_id
  FROM employees e
  JOIN reports r ON e.manager_id = r.id
)
SELECT manager_id, COUNT(*) AS total_reports
FROM reports
GROUP BY manager_id;
```

**Q162. Find employees who do not appear in the project_assignments table using NOT EXISTS.**
```sql
SELECT *
FROM employees e
WHERE NOT EXISTS (
  SELECT 1 FROM project_assignments pa WHERE pa.employee_id = e.id
);
```

**Q163. Find customers who bought a product also bought by customer 'Alice'.**
```sql
SELECT DISTINCT o2.customer_id
FROM orders o1
JOIN order_items oi1 ON o1.order_id = oi1.order_id
JOIN order_items oi2 ON oi1.product_id = oi2.product_id
JOIN orders o2 ON oi2.order_id = o2.order_id
WHERE o1.customer_id = (SELECT customer_id FROM customers WHERE name = 'Alice')
  AND o2.customer_id <> o1.customer_id;
```

**Q164. Use a CTE to find the top spender in each region.**
```sql
WITH regional_spend AS (
  SELECT region, customer_id, SUM(amount) AS total_spend,
         RANK() OVER (PARTITION BY region ORDER BY SUM(amount) DESC) AS rnk
  FROM orders o
  JOIN customers c ON o.customer_id = c.customer_id
  GROUP BY region, customer_id
)
SELECT * FROM regional_spend WHERE rnk = 1;
```

**Q165. Find the percentage of employees earning above the median salary.**
```sql
WITH median_calc AS (
  SELECT AVG(salary) AS median_salary
  FROM (
    SELECT salary FROM employees ORDER BY salary
    LIMIT 2 - (SELECT COUNT(*) FROM employees) % 2
    OFFSET (SELECT (COUNT(*) - 1) / 2 FROM employees)
  ) sub
)
SELECT 100.0 * COUNT(*) / (SELECT COUNT(*) FROM employees) AS pct_above_median
FROM employees, median_calc
WHERE employees.salary > median_calc.median_salary;
```

**Q166. Find all subordinates (direct and indirect) of a given manager using a recursive CTE.**
```sql
WITH RECURSIVE subordinates AS (
  SELECT id, name, manager_id
  FROM employees
  WHERE manager_id = 101
  UNION ALL
  SELECT e.id, e.name, e.manager_id
  FROM employees e
  JOIN subordinates s ON e.manager_id = s.id
)
SELECT * FROM subordinates;
```

**Q167. Find departments where every employee earns above 50000 using NOT EXISTS.**
```sql
SELECT DISTINCT department_id
FROM employees e1
WHERE NOT EXISTS (
  SELECT 1 FROM employees e2
  WHERE e2.department_id = e1.department_id AND e2.salary <= 50000
);
```

**Q168. Find the cumulative count of orders using a CTE combined with a window function.**
```sql
WITH daily_orders AS (
  SELECT order_date, COUNT(*) AS daily_count
  FROM orders
  GROUP BY order_date
)
SELECT order_date, daily_count,
       SUM(daily_count) OVER (ORDER BY order_date) AS cumulative_orders
FROM daily_orders;
```

**Q169. Find products that have never appeared together in the same order.**
```sql
SELECT p1.product_id AS product_a, p2.product_id AS product_b
FROM products p1
CROSS JOIN products p2
WHERE p1.product_id < p2.product_id
  AND NOT EXISTS (
    SELECT 1 FROM order_items oi1
    JOIN order_items oi2 ON oi1.order_id = oi2.order_id
    WHERE oi1.product_id = p1.product_id AND oi2.product_id = p2.product_id
  );
```

**Q170. Find the average tenure (in years) of employees per department using a CTE.**
```sql
WITH tenure AS (
  SELECT department_id,
         EXTRACT(YEAR FROM AGE(CURRENT_DATE, join_date)) AS years_employed
  FROM employees
)
SELECT department_id, AVG(years_employed) AS avg_tenure
FROM tenure
GROUP BY department_id;
```

**Q171. Find employees earning the maximum salary within their reporting chain (their own subtree) using recursion.**
```sql
WITH RECURSIVE chain AS (
  SELECT id, name, manager_id, salary, id AS root_manager
  FROM employees
  WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id, e.salary, c.root_manager
  FROM employees e
  JOIN chain c ON e.manager_id = c.id
)
SELECT root_manager, MAX(salary) AS max_salary_in_tree
FROM chain
GROUP BY root_manager;
```

**Q172. Find customers whose most recent order amount is greater than their average order amount.**
```sql
WITH customer_orders AS (
  SELECT customer_id, amount, order_date,
         AVG(amount) OVER (PARTITION BY customer_id) AS avg_amount,
         ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rn
  FROM orders
)
SELECT customer_id, amount, avg_amount
FROM customer_orders
WHERE rn = 1 AND amount > avg_amount;
```

---

## D08 — String & Pattern Problems (Q173–Q187)

*Text manipulation: extracting, transforming, and matching string-based data.*

**Q173. Find employees with duplicate names (case-insensitive).**
```sql
SELECT LOWER(name) AS name_lower, COUNT(*)
FROM employees
GROUP BY LOWER(name)
HAVING COUNT(*) > 1;
```

**Q174. Extract the domain name from each employee's email address.**
```sql
SELECT email, SUBSTRING(email FROM POSITION('@' IN email) + 1) AS domain
FROM employees;
```

**Q175. Find employees whose name contains only alphabetic characters.**
```sql
SELECT * FROM employees WHERE name ~ '^[A-Za-z ]+$';
```

**Q176. Concatenate first and last name into a single full name column.**
```sql
SELECT first_name || ' ' || last_name AS full_name FROM employees;
```

**Q177. Find the employee with the longest name.**
```sql
SELECT name, LENGTH(name) AS name_length
FROM employees
ORDER BY LENGTH(name) DESC
LIMIT 1;
```

**Q178. Find the employee with the shortest name.**
```sql
SELECT name, LENGTH(name) AS name_length
FROM employees
ORDER BY LENGTH(name) ASC
LIMIT 1;
```

**Q179. Convert all employee names to uppercase.**
```sql
SELECT UPPER(name) AS name_upper FROM employees;
```

**Q180. Find employees whose email does not contain '@'.**
```sql
SELECT * FROM employees WHERE email NOT LIKE '%@%';
```

**Q181. Find the count of vowels in each employee's name.**
```sql
SELECT name,
       LENGTH(name) -
       LENGTH(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(
         LOWER(name),
         'a',''),'e',''),'i',''),'o',''),'u','')) AS vowel_count
FROM employees;
```

**Q182. Find customers whose phone number does not match a 10-digit numeric pattern.**
```sql
SELECT * FROM customers WHERE phone !~ '^[0-9]{10}$';
```

**Q183. Trim leading and trailing spaces from product names.**
```sql
SELECT TRIM(product_name) AS cleaned_name FROM products;
```

**Q184. Find the position of the substring 'mail' within each email address.**
```sql
SELECT email, POSITION('mail' IN email) AS position_in_string FROM employees;
```

**Q185. Replace all spaces in product names with underscores.**
```sql
SELECT product_name, REPLACE(product_name,' ','_') AS slug FROM products;
```

**Q186. Find employees whose name has more than one word.**
```sql
SELECT * FROM employees WHERE name LIKE '% %';
```

**Q187. Reverse each customer's name.**
```sql
SELECT name, REVERSE(name) AS reversed_name FROM customers;
```

---

## D09 — Real Interview Favorites / Hard (Q188–Q200)

*Tricky, high-frequency interview puzzles: gaps-and-islands, pivoting, and complex existence checks.*

**Q188. Find the 3 consecutive numbers that are missing from an ID sequence.**
```sql
SELECT id + 1 AS missing_start
FROM sequence_table s1
WHERE NOT EXISTS (SELECT 1 FROM sequence_table s2 WHERE s2.id = s1.id + 1)
  AND NOT EXISTS (SELECT 1 FROM sequence_table s3 WHERE s3.id = s1.id + 2)
  AND NOT EXISTS (SELECT 1 FROM sequence_table s4 WHERE s4.id = s1.id + 3);
```

**Q189. Pivot monthly sales rows into columns (one column per month).**
```sql
SELECT product_id,
       SUM(CASE WHEN month = 'Jan' THEN amount END) AS Jan,
       SUM(CASE WHEN month = 'Feb' THEN amount END) AS Feb,
       SUM(CASE WHEN month = 'Mar' THEN amount END) AS Mar
FROM monthly_sales
GROUP BY product_id;
```

**Q190. Unpivot columns (Jan, Feb, Mar) back into rows.**
```sql
SELECT product_id,'Jan' AS month, jan_sales AS amount
FROM sales_wide
UNION ALL
SELECT product_id,'Feb', feb_sales FROM sales_wide
UNION ALL
SELECT product_id,'Mar', mar_sales FROM sales_wide;
```

**Q191. Find employees who never took a single day of leave.**
```sql
SELECT e.*
FROM employees e
LEFT JOIN leave_records l ON e.id = l.employee_id
WHERE l.employee_id IS NULL;
```

**Q192. Find the top N products per category using window functions.**
```sql
SELECT *
FROM (
  SELECT p.category_id, p.product_name, s.total_sales,
         ROW_NUMBER() OVER (PARTITION BY p.category_id ORDER BY s.total_sales DESC) AS rnk
  FROM products p
  JOIN (
    SELECT product_id, SUM(quantity * price) AS total_sales
    FROM order_items
    GROUP BY product_id
  ) s ON p.product_id = s.product_id
) ranked
WHERE rnk <= 3;
```

**Q193. Find customers who bought every single product in a given category.**
```sql
SELECT o.customer_id
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE p.category_id = 5
GROUP BY o.customer_id
HAVING COUNT(DISTINCT p.product_id) = (
  SELECT COUNT(*) FROM products WHERE category_id = 5
);
```

**Q194. Find consecutive groups of dates (islands) where a machine was continuously active.**
```sql
SELECT machine_id, MIN(active_date) AS island_start, MAX(active_date) AS island_end
FROM (
  SELECT machine_id, active_date,
         active_date - ROW_NUMBER() OVER (PARTITION BY machine_id ORDER BY active_date)::INT AS grp
  FROM machine_activity
) t
GROUP BY machine_id, grp;
```

**Q195. Find the longest consecutive run of login days for any single user.**
```sql
SELECT user_id, COUNT(*) AS streak_length
FROM (
  SELECT user_id, login_date,
         login_date - ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date)::INT AS grp
  FROM logins
) t
GROUP BY user_id, grp
ORDER BY streak_length DESC
LIMIT 1;
```

**Q196. Transpose a table of exam scores so each subject becomes its own column per student.**
```sql
SELECT student_id,
       MAX(CASE WHEN subject = 'Math'    THEN score END) AS Math,
       MAX(CASE WHEN subject = 'Science' THEN score END) AS Science,
       MAX(CASE WHEN subject = 'English' THEN score END) AS English
FROM exam_scores
GROUP BY student_id;
```

**Q197. Find employees who have an identical set of skills as another employee.**
```sql
SELECT e1.employee_id, e2.employee_id AS matching_employee
FROM employee_skills e1
JOIN employee_skills e2
  ON e1.skill_id = e2.skill_id AND e1.employee_id <> e2.employee_id
GROUP BY e1.employee_id, e2.employee_id
HAVING COUNT(*) = (SELECT COUNT(*) FROM employee_skills WHERE employee_id = e1.employee_id)
   AND COUNT(*) = (SELECT COUNT(*) FROM employee_skills WHERE employee_id = e2.employee_id);
```

**Q198. Find the three most recently registered customers in each country.**
```sql
SELECT *
FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY country ORDER BY signup_date DESC) AS rnk
  FROM customers
) ranked
WHERE rnk <= 3;
```

**Q199. Find products whose sales dropped for two consecutive months in a row.**
```sql
SELECT product_id, month
FROM (
  SELECT product_id, month, total_sales,
         LAG(total_sales, 1) OVER (PARTITION BY product_id ORDER BY month) AS prev1,
         LAG(total_sales, 2) OVER (PARTITION BY product_id ORDER BY month) AS prev2
  FROM monthly_product_sales
) t
WHERE total_sales < prev1 AND prev1 < prev2;
```

**Q200. Find the employee-manager pair with the largest salary gap.**
```sql
SELECT e.name AS employee, m.name AS manager, (m.salary - e.salary) AS salary_gap
FROM employees e
JOIN employees m ON e.manager_id = m.id
ORDER BY salary_gap DESC
LIMIT 1;
```

---

## D10 — Advanced Window Functions & Analytics (Q201–Q225)

*Deeper OVER() patterns: weighted averages, centered windows, cohort ratios, and multi-period comparisons.*

**Q201. Calculate a weighted moving average of sales using quantity as the weight.**
```sql
SELECT sale_date,
       SUM(amount * quantity) OVER (ORDER BY sale_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)
       / NULLIF(SUM(quantity) OVER (ORDER BY sale_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 0)
       AS weighted_moving_avg
FROM sales;
```

**Q202. Find the rank of each order within its own month by amount.**
```sql
SELECT order_id, order_date, amount,
       RANK() OVER (PARTITION BY DATE_TRUNC('month', order_date) ORDER BY amount DESC) AS month_rank
FROM orders;
```

**Q203. Compute the difference between each order and the customer's first order amount.**
```sql
SELECT customer_id, order_date, amount,
       amount - FIRST_VALUE(amount) OVER (
         PARTITION BY customer_id ORDER BY order_date
       ) AS diff_from_first
FROM orders;
```

**Q204. Find a running total of revenue per product that resets at the start of each year.**
```sql
SELECT product_id, sale_date, amount,
       SUM(amount) OVER (
         PARTITION BY product_id, EXTRACT(YEAR FROM sale_date)
         ORDER BY sale_date
       ) AS yearly_running_total
FROM product_sales;
```

**Q205. Compute the ratio of each employee's salary to the maximum salary in their department.**
```sql
SELECT name, department_id, salary,
       ROUND(salary::NUMERIC / MAX(salary) OVER (PARTITION BY department_id), 2) AS pct_of_dept_max
FROM employees;
```

**Q206. Find the second and third highest salaries in a single query using DENSE_RANK.**
```sql
SELECT salary, rnk
FROM (
  SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM employees
) ranked
WHERE rnk IN (2, 3);
```

**Q207. Compute a centered 5-day moving average of daily sales (2 preceding, 2 following).**
```sql
SELECT sale_date, amount,
       AVG(amount) OVER (
         ORDER BY sale_date
         ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING
       ) AS centered_avg
FROM sales;
```

**Q208. Find the first order date on which a customer's running total exceeded 1000.**
```sql
SELECT customer_id, order_date, running_total
FROM (
  SELECT customer_id, order_date,
         SUM(amount) OVER (PARTITION BY customer_id ORDER BY order_date) AS running_total,
         ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rn
  FROM orders
) t
WHERE running_total > 1000
QUALIFY ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) = 1;
```

**Q209. Compute a 2-period lag of stock prices for each symbol.**
```sql
SELECT symbol, trade_date, price,
       LAG(price, 2) OVER (PARTITION BY symbol ORDER BY trade_date) AS price_2_days_ago
FROM stock_prices;
```

**Q210. Find each customer's spend-rank change between the current and previous month.**
```sql
WITH monthly_rank AS (
  SELECT customer_id, month, SUM(amount) AS total,
         RANK() OVER (PARTITION BY month ORDER BY SUM(amount) DESC) AS rnk
  FROM monthly_customer_spend
  GROUP BY customer_id, month
)
SELECT customer_id, month, rnk,
       rnk - LAG(rnk) OVER (PARTITION BY customer_id ORDER BY month) AS rank_change
FROM monthly_rank;
```

**Q211. Compute the cumulative count of distinct products purchased by each customer over time.**
```sql
SELECT customer_id, order_date, product_id,
       COUNT(DISTINCT product_id) OVER (
         PARTITION BY customer_id ORDER BY order_date
         ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS distinct_products_so_far
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id;
```

**Q212. Find the employee in each department whose salary is closest to the department median.**
```sql
WITH dept_median AS (
  SELECT department_id,
         PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) AS median_salary
  FROM employees
  GROUP BY department_id
)
SELECT e.name, e.department_id, e.salary
FROM employees e
JOIN dept_median d ON e.department_id = d.department_id
QUALIFY ROW_NUMBER() OVER (
  PARTITION BY e.department_id ORDER BY ABS(e.salary - d.median_salary)
) = 1;
```

**Q213. Compute the z-score of each employee's salary within the company.**
```sql
SELECT name, salary,
       (salary - AVG(salary) OVER ()) / NULLIF(STDDEV(salary) OVER (), 0) AS z_score
FROM employees;
```

**Q214. Find the first and last order amount per customer using an unbounded window frame.**
```sql
SELECT DISTINCT customer_id,
       FIRST_VALUE(amount) OVER (
         PARTITION BY customer_id ORDER BY order_date
         ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
       ) AS first_amount,
       LAST_VALUE(amount) OVER (
         PARTITION BY customer_id ORDER BY order_date
         ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
       ) AS last_amount
FROM orders;
```

**Q215. Compute a 30-day trailing sum of daily revenue.**
```sql
SELECT sale_date, amount,
       SUM(amount) OVER (
         ORDER BY sale_date
         RANGE BETWEEN INTERVAL '29 days' PRECEDING AND CURRENT ROW
       ) AS trailing_30day_sum
FROM daily_revenue;
```

**Q216. Rank customers into deciles (10 buckets) based on lifetime spend.**
```sql
SELECT customer_id, total_spend,
       NTILE(10) OVER (ORDER BY total_spend) AS spend_decile
FROM (
  SELECT customer_id, SUM(amount) AS total_spend
  FROM orders
  GROUP BY customer_id
) t;
```

**Q217. Find the difference between each employee's salary and the next lower salary in the company.**
```sql
SELECT name, salary,
       salary - LEAD(salary) OVER (ORDER BY salary DESC) AS gap_to_next_lower
FROM employees;
```

**Q218. Compute each department's share of total company headcount.**
```sql
SELECT department_id, COUNT(*) AS headcount,
       ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS pct_of_company
FROM employees
GROUP BY department_id;
```

**Q219. Find products whose sales rank improved from Q1 to Q2.**
```sql
WITH quarter_rank AS (
  SELECT product_id, quarter, total_sales,
         RANK() OVER (PARTITION BY quarter ORDER BY total_sales DESC) AS rnk
  FROM quarterly_product_sales
)
SELECT q1.product_id, q1.rnk AS q1_rank, q2.rnk AS q2_rank
FROM quarter_rank q1
JOIN quarter_rank q2 ON q1.product_id = q2.product_id
WHERE q1.quarter = 'Q1' AND q2.quarter = 'Q2' AND q2.rnk < q1.rnk;
```

**Q220. Compute a running average of order amount that excludes the current row.**
```sql
SELECT customer_id, order_date, amount,
       AVG(amount) OVER (
         PARTITION BY customer_id ORDER BY order_date
         ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
       ) AS avg_excluding_current
FROM orders;
```

**Q221. Compare ROW_NUMBER, RANK and DENSE_RANK side by side for the top earners.**
```sql
SELECT name, salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num,
       RANK()       OVER (ORDER BY salary DESC) AS rnk,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rnk
FROM employees;
```

**Q222. Compute, for each employee, the count of employees earning a higher salary (inverse rank).**
```sql
SELECT name, salary,
       COUNT(*) OVER (ORDER BY salary DESC ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING)
       AS higher_earners
FROM employees;
```

**Q223. Find the largest single-day drop in stock price for each symbol.**
```sql
SELECT symbol, trade_date,
       price - LAG(price) OVER (PARTITION BY symbol ORDER BY trade_date) AS daily_change
FROM stock_prices
QUALIFY daily_change = MIN(price - LAG(price) OVER (PARTITION BY symbol ORDER BY trade_date))
  OVER (PARTITION BY symbol);
```

**Q224. Compute a 3-month rolling customer retention rate.**
```sql
SELECT month,
       COUNT(DISTINCT CASE WHEN active_this_month AND active_last_month THEN customer_id END)::NUMERIC
       / NULLIF(COUNT(DISTINCT CASE WHEN active_last_month THEN customer_id END), 0) AS retention_rate
FROM customer_month_activity
GROUP BY month;
```

**Q225. Find login gaps larger than 30 days between consecutive logins per user.**
```sql
SELECT user_id, login_date,
       login_date - LAG(login_date) OVER (PARTITION BY user_id ORDER BY login_date) AS gap_days
FROM logins
QUALIFY gap_days > 30;
```

---

## D11 — Advanced Recursive CTEs & Hierarchies (Q226–Q245)

*Multi-level trees, bill-of-materials explosions, path strings, and cycle-safe recursion.*

**Q226. Generate a series of dates between two dates using a recursive CTE.**
```sql
WITH RECURSIVE date_series AS (
  SELECT DATE '2024-01-01' AS d
  UNION ALL
  SELECT d + 1 FROM date_series WHERE d + 1 <= DATE '2024-01-31'
)
SELECT d FROM date_series;
```

**Q227. Build a materialized path string for each node in an org chart.**
```sql
WITH RECURSIVE paths AS (
  SELECT id, name, manager_id, name::TEXT AS path
  FROM employees
  WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id, p.path || ' > ' || e.name
  FROM employees e
  JOIN paths p ON e.manager_id = p.id
)
SELECT * FROM paths ORDER BY path;
```

**Q228. Explode a bill-of-materials to find all sub-components of a product.**
```sql
WITH RECURSIVE bom AS (
  SELECT parent_product_id, component_id, quantity, 1 AS level
  FROM product_components
  WHERE parent_product_id = 500
  UNION ALL
  SELECT pc.parent_product_id, pc.component_id, pc.quantity, b.level + 1
  FROM product_components pc
  JOIN bom b ON pc.parent_product_id = b.component_id
)
SELECT * FROM bom ORDER BY level;
```

**Q229. Detect a cycle in a manager-report relationship using a recursive CTE guard.**
```sql
WITH RECURSIVE chain AS (
  SELECT id, manager_id, ARRAY[id] AS visited, FALSE AS is_cycle
  FROM employees
  UNION ALL
  SELECT e.id, c.manager_id, c.visited || e.id, e.id = ANY(c.visited)
  FROM employees e
  JOIN chain c ON e.manager_id = c.id
  WHERE NOT c.is_cycle
)
SELECT DISTINCT id FROM chain WHERE is_cycle;
```

**Q230. Find the total budget of a department including all of its child departments.**
```sql
WITH RECURSIVE dept_tree AS (
  SELECT department_id, parent_department_id, budget
  FROM departments
  WHERE department_id = 10
  UNION ALL
  SELECT d.department_id, d.parent_department_id, d.budget
  FROM departments d
  JOIN dept_tree t ON d.parent_department_id = t.department_id
)
SELECT SUM(budget) AS total_budget FROM dept_tree;
```

**Q231. Compute the number of direct reports at each level of the hierarchy.**
```sql
WITH RECURSIVE levels AS (
  SELECT id, manager_id, 0 AS lvl
  FROM employees
  WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.manager_id, l.lvl + 1
  FROM employees e
  JOIN levels l ON e.manager_id = l.id
)
SELECT lvl, COUNT(*) AS employees_at_level
FROM levels
GROUP BY lvl
ORDER BY lvl;
```

**Q232. Find the shortest reporting-chain path between two employees.**
```sql
WITH RECURSIVE path AS (
  SELECT id, manager_id, ARRAY[id] AS chain, 0 AS steps
  FROM employees
  WHERE id = 55
  UNION ALL
  SELECT e.id, e.manager_id, p.chain || e.id, p.steps + 1
  FROM employees e
  JOIN path p ON e.id = p.manager_id
)
SELECT * FROM path WHERE id = 1 ORDER BY steps LIMIT 1;
```

**Q233. Generate a numbered sequence from 1 to 100 without a numbers table.**
```sql
WITH RECURSIVE seq AS (
  SELECT 1 AS n
  UNION ALL
  SELECT n + 1 FROM seq WHERE n < 100
)
SELECT n FROM seq;
```

**Q234. Find all categories and their nested sub-categories using a recursive CTE.**
```sql
WITH RECURSIVE cat_tree AS (
  SELECT category_id, category_name, parent_category_id, 1 AS depth
  FROM categories
  WHERE parent_category_id IS NULL
  UNION ALL
  SELECT c.category_id, c.category_name, c.parent_category_id, ct.depth + 1
  FROM categories c
  JOIN cat_tree ct ON c.parent_category_id = ct.category_id
)
SELECT * FROM cat_tree ORDER BY depth, category_name;
```

**Q235. Compute the total headcount under each director, including all indirect reports.**
```sql
WITH RECURSIVE org AS (
  SELECT id, manager_id, id AS director_id
  FROM employees
  WHERE job_title = 'Director'
  UNION ALL
  SELECT e.id, e.manager_id, o.director_id
  FROM employees e
  JOIN org o ON e.manager_id = o.id
)
SELECT director_id, COUNT(*) AS total_headcount
FROM org
GROUP BY director_id;
```

**Q236. Find the maximum depth of the organizational hierarchy.**
```sql
WITH RECURSIVE depth AS (
  SELECT id, manager_id, 1 AS lvl
  FROM employees
  WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.manager_id, d.lvl + 1
  FROM employees e
  JOIN depth d ON e.manager_id = d.id
)
SELECT MAX(lvl) AS max_depth FROM depth;
```

**Q237. Compute a running Fibonacci-style forecast sequence using a recursive CTE.**
```sql
WITH RECURSIVE fib AS (
  SELECT 1 AS a, 1 AS b, 1 AS step
  UNION ALL
  SELECT b, a + b, step + 1 FROM fib WHERE step < 20
)
SELECT step, a AS fib_value FROM fib;
```

**Q238. Find all leaf-level employees (those with no direct reports).**
```sql
SELECT e.*
FROM employees e
WHERE NOT EXISTS (SELECT 1 FROM employees x WHERE x.manager_id = e.id);
```

**Q239. Compute the total sales rolled up through a product category tree.**
```sql
WITH RECURSIVE cat_tree AS (
  SELECT category_id, parent_category_id FROM categories
  WHERE category_id = 1
  UNION ALL
  SELECT c.category_id, c.parent_category_id
  FROM categories c
  JOIN cat_tree ct ON c.parent_category_id = ct.category_id
)
SELECT SUM(oi.quantity * oi.price) AS rolled_up_sales
FROM cat_tree ct
JOIN products p ON p.category_id = ct.category_id
JOIN order_items oi ON oi.product_id = p.product_id;
```

**Q240. Find employees who are more than 3 levels deep in the reporting hierarchy.**
```sql
WITH RECURSIVE hierarchy AS (
  SELECT id, manager_id, 0 AS depth
  FROM employees
  WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.manager_id, h.depth + 1
  FROM employees e
  JOIN hierarchy h ON e.manager_id = h.id
)
SELECT e.*
FROM employees e
JOIN hierarchy h ON e.id = h.id
WHERE h.depth > 3;
```

**Q241. Traverse a friend-of-friend social graph up to 2 hops using recursion.**
```sql
WITH RECURSIVE network AS (
  SELECT user_id, friend_id, 1 AS hops
  FROM friendships
  WHERE user_id = 1
  UNION ALL
  SELECT n.user_id, f.friend_id, n.hops + 1
  FROM friendships f
  JOIN network n ON f.user_id = n.friend_id
  WHERE n.hops < 2
)
SELECT DISTINCT friend_id FROM network;
```

**Q242. Find all ancestor categories of a given leaf category (walking upward).**
```sql
WITH RECURSIVE ancestors AS (
  SELECT category_id, parent_category_id
  FROM categories
  WHERE category_id = 42
  UNION ALL
  SELECT c.category_id, c.parent_category_id
  FROM categories c
  JOIN ancestors a ON c.category_id = a.parent_category_id
)
SELECT * FROM ancestors;
```

**Q243. Compute the cumulative project budget across a multi-level project/sub-project tree.**
```sql
WITH RECURSIVE proj_tree AS (
  SELECT project_id, parent_project_id, budget
  FROM projects
  WHERE parent_project_id IS NULL
  UNION ALL
  SELECT p.project_id, p.parent_project_id, p.budget
  FROM projects p
  JOIN proj_tree t ON p.parent_project_id = t.project_id
)
SELECT SUM(budget) AS total_budget FROM proj_tree;
```

**Q244. Find the reporting chain (top to bottom) as a single readable string for one employee.**
```sql
WITH RECURSIVE chain AS (
  SELECT id, name, manager_id, name::TEXT AS path
  FROM employees
  WHERE id = 5
  UNION ALL
  SELECT e.id, e.name, e.manager_id, e.name || ' -> ' || c.path
  FROM employees e
  JOIN chain c ON e.id = c.manager_id
)
SELECT path FROM chain ORDER BY LENGTH(path) DESC LIMIT 1;
```

**Q245. Flatten a threaded comments table into ordered conversation order using recursion.**
```sql
WITH RECURSIVE thread AS (
  SELECT comment_id, parent_comment_id, comment_text, 1 AS depth,
         LPAD(comment_id::TEXT, 5, '0') AS sort_path
  FROM comments
  WHERE parent_comment_id IS NULL
  UNION ALL
  SELECT c.comment_id, c.parent_comment_id, c.comment_text, t.depth + 1,
         t.sort_path || '.' || LPAD(c.comment_id::TEXT, 5, '0')
  FROM comments c
  JOIN thread t ON c.parent_comment_id = t.comment_id
)
SELECT * FROM thread ORDER BY sort_path;
```

---

## D12 — Complex JOIN Patterns (Q246–Q270)

*Multi-key joins, anti-joins, lateral joins, self-joins, and set-based comparisons across tables.*

**Q246. Find customers who bought product A but never bought product B.**
```sql
SELECT DISTINCT o.customer_id
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
WHERE oi.product_id = 'A'
  AND o.customer_id NOT IN (
    SELECT o2.customer_id
    FROM orders o2
    JOIN order_items oi2 ON o2.order_id = oi2.order_id
    WHERE oi2.product_id = 'B'
  );
```

**Q247. Join two tables on multiple columns to find matching shipment records.**
```sql
SELECT s.*
FROM shipments s
JOIN manifests m
  ON s.order_id     = m.order_id
 AND s.warehouse_id = m.warehouse_id
 AND s.ship_date    = m.ship_date;
```

**Q248. Use a LATERAL join to get each customer's 3 most recent orders.**
```sql
SELECT c.customer_id, c.name, recent.*
FROM customers c
CROSS JOIN LATERAL (
  SELECT order_id, order_date, amount
  FROM orders o
  WHERE o.customer_id = c.customer_id
  ORDER BY order_date DESC
  LIMIT 3
) recent;
```

**Q249. Find employees and departments using a FULL OUTER JOIN to spot mismatches both ways.**
```sql
SELECT e.name, d.department_name
FROM employees e
FULL OUTER JOIN departments d ON e.department_id = d.department_id
WHERE e.id IS NULL OR d.department_id IS NULL;
```

**Q250. Find pairs of orders from the same customer placed within 1 hour of each other.**
```sql
SELECT o1.order_id AS order1, o2.order_id AS order2, o1.customer_id
FROM orders o1
JOIN orders o2
  ON o1.customer_id = o2.customer_id
 AND o1.order_id < o2.order_id
 AND ABS(EXTRACT(EPOCH FROM (o1.order_timestamp - o2.order_timestamp))) <= 3600;
```

**Q251. Find products that appear in every warehouse's inventory (a relational-division join).**
```sql
SELECT product_id
FROM inventory
GROUP BY product_id
HAVING COUNT(DISTINCT warehouse_id) = (SELECT COUNT(*) FROM warehouses);
```

**Q252. Join a sales fact table to a date dimension to label each sale with its fiscal quarter.**
```sql
SELECT s.sale_id, s.amount, d.fiscal_quarter, d.fiscal_year
FROM sales s
JOIN date_dim d ON s.sale_date = d.calendar_date;
```

**Q253. Find customers whose shipping address differs from their billing address.**
```sql
SELECT c.customer_id, a1.address AS billing, a2.address AS shipping
FROM customers c
JOIN addresses a1 ON c.customer_id = a1.customer_id AND a1.type = 'billing'
JOIN addresses a2 ON c.customer_id = a2.customer_id AND a2.type = 'shipping'
WHERE a1.address <> a2.address;
```

**Q254. Find the closest warehouse to each customer using a LATERAL join with distance calculation.**
```sql
SELECT c.customer_id, nearest.warehouse_id, nearest.distance
FROM customers c
CROSS JOIN LATERAL (
  SELECT w.warehouse_id,
         SQRT(POWER(w.lat - c.lat, 2) + POWER(w.lon - c.lon, 2)) AS distance
  FROM warehouses w
  ORDER BY distance ASC
  LIMIT 1
) nearest;
```

**Q255. Find employees assigned to a project but missing from the timesheets table (anti-join).**
```sql
SELECT pa.employee_id, pa.project_id
FROM project_assignments pa
WHERE NOT EXISTS (
  SELECT 1 FROM timesheets t
  WHERE t.employee_id = pa.employee_id AND t.project_id = pa.project_id
);
```

**Q256. Join three tables to compute each salesperson's commission for the month.**
```sql
SELECT r.rep_name, SUM(o.amount) AS total_sales,
       SUM(o.amount) * c.commission_rate AS commission
FROM sales_reps r
JOIN orders o ON r.rep_id = o.rep_id
JOIN commission_rates c ON r.rep_id = c.rep_id
WHERE DATE_TRUNC('month', o.order_date) = DATE_TRUNC('month', CURRENT_DATE)
GROUP BY r.rep_name, c.commission_rate;
```

**Q257. Find customers who have orders in EVERY month of the current year (relational division).**
```sql
SELECT customer_id
FROM orders
WHERE EXTRACT(YEAR FROM order_date) = EXTRACT(YEAR FROM CURRENT_DATE)
GROUP BY customer_id
HAVING COUNT(DISTINCT EXTRACT(MONTH FROM order_date)) = 12;
```

**Q258. Find overlapping date-range bookings for the same meeting room using a range join.**
```sql
SELECT b1.booking_id AS booking1, b2.booking_id AS booking2
FROM bookings b1
JOIN bookings b2
  ON b1.room_id = b2.room_id
 AND b1.booking_id < b2.booking_id
 AND b1.start_time < b2.end_time
 AND b2.start_time < b1.end_time;
```

**Q259. Join employees to their most recent performance review using a LATERAL subquery.**
```sql
SELECT e.name, r.review_date, r.rating
FROM employees e
CROSS JOIN LATERAL (
  SELECT review_date, rating
  FROM performance_reviews pr
  WHERE pr.employee_id = e.id
  ORDER BY review_date DESC
  LIMIT 1
) r;
```

**Q260. Find products sold in one store but not in another, using an anti-join on a multi-column key.**
```sql
SELECT p.product_id
FROM store_inventory p
WHERE p.store_id = 'A'
  AND NOT EXISTS (
    SELECT 1 FROM store_inventory q
    WHERE q.store_id = 'B' AND q.product_id = p.product_id
  );
```

**Q261. Join a transactions table to itself to find refund transactions matching an original sale.**
```sql
SELECT t1.transaction_id AS sale_id, t2.transaction_id AS refund_id
FROM transactions t1
JOIN transactions t2
  ON t1.order_id = t2.order_id
 AND t1.type = 'sale' AND t2.type = 'refund'
 AND t1.amount = -t2.amount;
```

**Q262. Find employees working on projects outside their own department.**
```sql
SELECT e.name, pr.project_name, pr.department_id AS project_department
FROM employees e
JOIN project_assignments pa ON e.id = pa.employee_id
JOIN projects pr ON pa.project_id = pr.project_id
WHERE e.department_id <> pr.department_id;
```

**Q263. Find the best-selling product in each store using a LATERAL join with TOP-1 semantics.**
```sql
SELECT s.store_id, top_product.product_id, top_product.total_qty
FROM stores s
CROSS JOIN LATERAL (
  SELECT product_id, SUM(quantity) AS total_qty
  FROM store_sales ss
  WHERE ss.store_id = s.store_id
  GROUP BY product_id
  ORDER BY total_qty DESC
  LIMIT 1
) top_product;
```

**Q264. Find pairs of products frequently bought together (market-basket self-join).**
```sql
SELECT oi1.product_id AS product_a, oi2.product_id AS product_b, COUNT(*) AS times_together
FROM order_items oi1
JOIN order_items oi2
  ON oi1.order_id = oi2.order_id AND oi1.product_id < oi2.product_id
GROUP BY oi1.product_id, oi2.product_id
ORDER BY times_together DESC;
```

**Q265. Join employees with their department and a lookup of the department's building floor.**
```sql
SELECT e.name, d.department_name, f.floor_number
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN building_floors f ON d.location = f.location;
```

**Q266. Find customers whose order history exactly matches another customer's order history.**
```sql
SELECT o1.customer_id, o2.customer_id AS matching_customer
FROM (SELECT DISTINCT customer_id, product_id
      FROM order_items oi JOIN orders o ON oi.order_id = o.order_id) o1
JOIN (SELECT DISTINCT customer_id, product_id
      FROM order_items oi JOIN orders o ON oi.order_id = o.order_id) o2
  ON o1.product_id = o2.product_id AND o1.customer_id < o2.customer_id
GROUP BY o1.customer_id, o2.customer_id
HAVING COUNT(*) = (SELECT COUNT(*) FROM order_items oi JOIN orders o ON oi.order_id = o.order_id
                   WHERE o.customer_id = o1.customer_id)
   AND COUNT(*) = (SELECT COUNT(*) FROM order_items oi JOIN orders o ON oi.order_id = o.order_id
                   WHERE o.customer_id = o2.customer_id);
```

**Q267. Find managers who share at least one direct report's department with another manager.**
```sql
SELECT DISTINCT m1.id AS manager1, m2.id AS manager2, e1.department_id
FROM employees e1
JOIN employees m1 ON e1.manager_id = m1.id
JOIN employees e2 ON e1.department_id = e2.department_id AND e1.manager_id <> e2.manager_id
JOIN employees m2 ON e2.manager_id = m2.id
WHERE m1.id < m2.id;
```

**Q268. Join orders to a currency-rates table to convert every order amount to USD as of the order date.**
```sql
SELECT o.order_id, o.amount, o.currency, o.amount * r.usd_rate AS amount_usd
FROM orders o
JOIN currency_rates r
  ON o.currency = r.currency AND o.order_date = r.rate_date;
```

**Q269. Find employees who share the exact same set of project assignments as another employee.**
```sql
SELECT pa1.employee_id, pa2.employee_id AS matching_employee
FROM project_assignments pa1
JOIN project_assignments pa2
  ON pa1.project_id = pa2.project_id AND pa1.employee_id < pa2.employee_id
GROUP BY pa1.employee_id, pa2.employee_id
HAVING COUNT(*) = (SELECT COUNT(*) FROM project_assignments WHERE employee_id = pa1.employee_id)
   AND COUNT(*) = (SELECT COUNT(*) FROM project_assignments WHERE employee_id = pa2.employee_id);
```

**Q270. Join a returns table back to the original order_items to compute the net quantity sold per product.**
```sql
SELECT oi.product_id,
       SUM(oi.quantity) - COALESCE(SUM(r.quantity_returned), 0) AS net_quantity_sold
FROM order_items oi
LEFT JOIN returns r
  ON oi.order_id = r.order_id AND oi.product_id = r.product_id
GROUP BY oi.product_id;
```

---

## D13 — Advanced Aggregation Pipelines (Q271–Q290)

*Multi-stage GROUP BY pipelines, conditional aggregation, rollups, and cube-style summaries.*

**Q271. Build a sales summary with subtotals per region and a grand total using ROLLUP.**
```sql
SELECT region, product_category, SUM(amount) AS total_sales
FROM sales
GROUP BY ROLLUP (region, product_category);
```

**Q272. Build a cross-tabulation of headcount by department and job title using CUBE.**
```sql
SELECT department_id, job_title, COUNT(*) AS headcount
FROM employees
GROUP BY CUBE (department_id, job_title);
```

**Q273. Compute conditional aggregates: total revenue split by online vs in-store channel per month.**
```sql
SELECT DATE_TRUNC('month', sale_date) AS month,
       SUM(CASE WHEN channel = 'online'   THEN amount ELSE 0 END) AS online_revenue,
       SUM(CASE WHEN channel = 'in_store' THEN amount ELSE 0 END) AS in_store_revenue
FROM sales
GROUP BY DATE_TRUNC('month', sale_date);
```

**Q274. Find the funnel conversion rate from signup to first purchase using staged aggregation.**
```sql
WITH signups    AS (SELECT COUNT(*) AS total_signups FROM customers),
     purchasers AS (SELECT COUNT(DISTINCT customer_id) AS total_purchasers FROM orders)
SELECT p.total_purchasers, s.total_signups,
       ROUND(100.0 * p.total_purchasers / s.total_signups, 2) AS conversion_rate
FROM signups s, purchasers p;
```

**Q275. Compute a multi-level aggregation pipeline: daily totals, then monthly averages of those daily totals.**
```sql
WITH daily AS (
  SELECT sale_date, SUM(amount) AS daily_total
  FROM sales
  GROUP BY sale_date
)
SELECT DATE_TRUNC('month', sale_date) AS month, AVG(daily_total) AS avg_daily_sales
FROM daily
GROUP BY DATE_TRUNC('month', sale_date);
```

**Q276. Find the top 3 revenue-generating categories, with all others rolled into an 'Other' bucket.**
```sql
WITH cat_totals AS (
  SELECT category_name, SUM(amount) AS total,
         RANK() OVER (ORDER BY SUM(amount) DESC) AS rnk
  FROM sales s JOIN categories c ON s.category_id = c.category_id
  GROUP BY category_name
)
SELECT CASE WHEN rnk <= 3 THEN category_name ELSE 'Other' END AS category,
       SUM(total) AS total
FROM cat_totals
GROUP BY CASE WHEN rnk <= 3 THEN category_name ELSE 'Other' END;
```

**Q277. Compute distinct customer counts per channel using FILTER-style conditional counting.**
```sql
SELECT COUNT(*) FILTER (WHERE channel = 'online')   AS online_customers,
       COUNT(*) FILTER (WHERE channel = 'in_store') AS in_store_customers
FROM (SELECT DISTINCT customer_id, channel FROM orders) t;
```

**Q278. Build a summary table showing min, max, avg and stddev of order amount per customer segment.**
```sql
SELECT segment,
       MIN(amount) AS min_amount,
       MAX(amount) AS max_amount,
       ROUND(AVG(amount), 2)    AS avg_amount,
       ROUND(STDDEV(amount), 2) AS stddev_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY segment;
```

**Q279. Compute year-over-year comparison of quarterly revenue in a single pivoted result set.**
```sql
SELECT quarter,
       SUM(CASE WHEN year = 2024 THEN revenue END) AS revenue_2024,
       SUM(CASE WHEN year = 2025 THEN revenue END) AS revenue_2025
FROM quarterly_revenue
GROUP BY quarter
ORDER BY quarter;
```

**Q280. Find the average basket size (items per order) segmented by customer loyalty tier.**
```sql
SELECT c.loyalty_tier, AVG(item_count) AS avg_basket_size
FROM (
  SELECT order_id, customer_id, COUNT(*) AS item_count
  FROM order_items oi JOIN orders o ON oi.order_id = o.order_id
  GROUP BY order_id, customer_id
) basket
JOIN customers c ON basket.customer_id = c.customer_id
GROUP BY c.loyalty_tier;
```

**Q281. Compute a two-stage aggregation: total per employee per project, then average per department.**
```sql
WITH emp_project_hours AS (
  SELECT e.department_id, t.employee_id, SUM(t.hours) AS total_hours
  FROM timesheets t
  JOIN employees e ON t.employee_id = e.id
  GROUP BY e.department_id, t.employee_id
)
SELECT department_id, AVG(total_hours) AS avg_hours_per_employee
FROM emp_project_hours
GROUP BY department_id;
```

**Q282. Find the percentage of total revenue contributed by each sales channel.**
```sql
SELECT channel, SUM(amount) AS channel_revenue,
       ROUND(100.0 * SUM(amount) / SUM(SUM(amount)) OVER (), 2) AS pct_of_total
FROM sales
GROUP BY channel;
```

**Q283. Build a GROUPING SETS report combining totals by region alone, by product alone, and by both.**
```sql
SELECT region, product_category, SUM(amount) AS total_sales
FROM sales
GROUP BY GROUPING SETS ((region), (product_category), (region, product_category));
```

**Q284. Compute a customer cohort retention matrix (signup month vs activity month).**
```sql
SELECT DATE_TRUNC('month', c.signup_date) AS cohort_month,
       DATE_TRUNC('month', o.order_date)  AS activity_month,
       COUNT(DISTINCT o.customer_id) AS active_customers
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY DATE_TRUNC('month', c.signup_date), DATE_TRUNC('month', o.order_date)
ORDER BY cohort_month, activity_month;
```

**Q285. Find the incremental revenue contribution of each new product launched this year versus last year's baseline.**
```sql
SELECT p.product_id,
       SUM(CASE WHEN EXTRACT(YEAR FROM o.order_date) = EXTRACT(YEAR FROM CURRENT_DATE)
                THEN oi.quantity*oi.price ELSE 0 END) AS this_year,
       SUM(CASE WHEN EXTRACT(YEAR FROM o.order_date) = EXTRACT(YEAR FROM CURRENT_DATE) - 1
                THEN oi.quantity*oi.price ELSE 0 END) AS last_year
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
JOIN orders o ON oi.order_id = o.order_id
GROUP BY p.product_id;
```

**Q286. Compute an aging report bucketing outstanding invoices into 0-30, 31-60, 61-90 and 90+ days.**
```sql
SELECT
  CASE
    WHEN CURRENT_DATE - due_date <= 30 THEN '0-30'
    WHEN CURRENT_DATE - due_date <= 60 THEN '31-60'
    WHEN CURRENT_DATE - due_date <= 90 THEN '61-90'
    ELSE '90+'
  END AS aging_bucket,
  SUM(amount_due) AS total_due
FROM invoices
WHERE paid = FALSE
GROUP BY 1;
```

**Q287. Compute the percentage of orders that are first-time versus repeat purchases, per month.**
```sql
WITH first_orders AS (
  SELECT customer_id, MIN(order_date) AS first_order_date
  FROM orders
  GROUP BY customer_id
)
SELECT DATE_TRUNC('month', o.order_date) AS month,
       COUNT(*) FILTER (WHERE o.order_date =  f.first_order_date) AS first_time_orders,
       COUNT(*) FILTER (WHERE o.order_date <> f.first_order_date) AS repeat_orders
FROM orders o
JOIN first_orders f ON o.customer_id = f.customer_id
GROUP BY DATE_TRUNC('month', o.order_date);
```

**Q288. Build a summary of average discount percentage applied, grouped by product category and customer tier.**
```sql
SELECT p.category_id, c.loyalty_tier,
       ROUND(AVG(100.0 * (p.price - oi.price) / NULLIF(p.price, 0)), 2) AS avg_discount_pct
FROM order_items oi
JOIN products p  ON oi.product_id = p.product_id
JOIN orders o    ON oi.order_id = o.order_id
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY p.category_id, c.loyalty_tier;
```

**Q289. Compute total, average and median order value together in a single aggregation query.**
```sql
SELECT COUNT(*) AS total_orders,
       SUM(amount) AS total_revenue,
       ROUND(AVG(amount), 2) AS avg_order_value,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY amount) AS median_order_value
FROM orders;
```

**Q290. Find the percentage of employees in each department who received a raise in the last 12 months.**
```sql
SELECT e.department_id,
       ROUND(100.0 * COUNT(DISTINCT sh.employee_id) / COUNT(DISTINCT e.id), 2) AS pct_received_raise
FROM employees e
LEFT JOIN salary_history sh
  ON e.id = sh.employee_id AND sh.raise_date >= CURRENT_DATE - INTERVAL '12 months'
GROUP BY e.department_id;
```

---

## D14 — Schema Modifications & DDL (Q291–Q315)

*ALTER, CREATE, constraints, indexes, views, and other data-definition tasks a senior engineer is expected to know.*

**Q291. Create a new table for storing customer addresses with proper primary and foreign keys.**
```sql
CREATE TABLE addresses (
  address_id   SERIAL PRIMARY KEY,
  customer_id  INT NOT NULL REFERENCES customers(customer_id),
  address_line VARCHAR(255) NOT NULL,
  city         VARCHAR(100),
  country      VARCHAR(100),
  type         VARCHAR(20) CHECK (type IN ('billing','shipping'))
);
```

**Q292. Add a new NOT NULL column with a default value to an existing large table.**
```sql
ALTER TABLE employees
ADD COLUMN is_active BOOLEAN NOT NULL DEFAULT TRUE;
```

**Q293. Rename a column without breaking existing views that reference it.**
```sql
ALTER TABLE customers
RENAME COLUMN phone TO phone_number;
```

**Q294. Add a foreign key constraint to an existing column after cleaning up orphaned rows.**
```sql
DELETE FROM orders
WHERE customer_id NOT IN (SELECT customer_id FROM customers);

ALTER TABLE orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (customer_id) REFERENCES customers(customer_id);
```

**Q295. Create a composite index to speed up a common two-column filter.**
```sql
CREATE INDEX idx_orders_customer_date
ON orders (customer_id, order_date);
```

**Q296. Create a partial index that only covers active (non-deleted) rows.**
```sql
CREATE INDEX idx_active_employees
ON employees (department_id)
WHERE is_active = TRUE;
```

**Q297. Add a CHECK constraint to enforce that salary is always positive.**
```sql
ALTER TABLE employees
ADD CONSTRAINT chk_salary_positive CHECK (salary > 0);
```

**Q298. Create a view that exposes only non-sensitive employee columns.**
```sql
CREATE VIEW employee_directory AS
SELECT id, name, department_id, job_title, email
FROM employees;
```

**Q299. Create a materialized view for a slow-to-compute monthly sales summary and refresh it.**
```sql
CREATE MATERIALIZED VIEW monthly_sales_summary AS
SELECT DATE_TRUNC('month', sale_date) AS month, SUM(amount) AS total_sales
FROM sales
GROUP BY DATE_TRUNC('month', sale_date);

REFRESH MATERIALIZED VIEW monthly_sales_summary;
```

**Q300. Alter a column's data type from VARCHAR(50) to VARCHAR(255).**
```sql
ALTER TABLE products
ALTER COLUMN product_name TYPE VARCHAR(255);
```

**Q301. Add a unique constraint on a column that should never have duplicate values.**
```sql
ALTER TABLE employees
ADD CONSTRAINT uq_employee_email UNIQUE (email);
```

**Q302. Drop a column that is no longer used by the application.**
```sql
ALTER TABLE products
DROP COLUMN legacy_sku;
```

**Q303. Create a table partitioned by range on the order_date column.**
```sql
CREATE TABLE orders (
  order_id    SERIAL,
  customer_id INT,
  order_date  DATE NOT NULL,
  amount      DECIMAL(10,2)
) PARTITION BY RANGE (order_date);

CREATE TABLE orders_2025 PARTITION OF orders
FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');
```

**Q304. Create a sequence and use it to backfill an existing ID column.**
```sql
CREATE SEQUENCE invoice_seq START 10000;

UPDATE invoices
SET invoice_number = nextval('invoice_seq')
WHERE invoice_number IS NULL;
```

**Q305. Add a self-referencing foreign key to support a manager hierarchy.**
```sql
ALTER TABLE employees
ADD CONSTRAINT fk_manager
FOREIGN KEY (manager_id) REFERENCES employees(id);
```

**Q306. Create a table with a generated (computed) column for total line-item value.**
```sql
CREATE TABLE order_items (
  order_id   INT,
  product_id INT,
  quantity   INT,
  price      DECIMAL(10,2),
  line_total DECIMAL(10,2) GENERATED ALWAYS AS (quantity * price) STORED
);
```

**Q307. Rename a table safely while keeping a backward-compatible view under the old name.**
```sql
ALTER TABLE clients RENAME TO customers;
CREATE VIEW clients AS SELECT * FROM customers;
```

**Q308. Add an ON DELETE CASCADE behavior to an existing foreign key.**
```sql
ALTER TABLE order_items
DROP CONSTRAINT fk_order_items_order,
ADD CONSTRAINT fk_order_items_order
FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE;
```

**Q309. Create a lookup table for status codes and migrate an existing free-text status column to reference it.**
```sql
CREATE TABLE order_statuses (
  status_id   SERIAL PRIMARY KEY,
  status_name VARCHAR(30) UNIQUE NOT NULL
);

INSERT INTO order_statuses (status_name)
SELECT DISTINCT status FROM orders;

ALTER TABLE orders ADD COLUMN status_id INT REFERENCES order_statuses(status_id);

UPDATE orders o
SET status_id = s.status_id
FROM order_statuses s
WHERE o.status = s.status_name;
```

**Q310. Create a trigger that automatically updates an updated_at timestamp on row modification.**
```sql
CREATE OR REPLACE FUNCTION set_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_customers_updated_at
BEFORE UPDATE ON customers
FOR EACH ROW EXECUTE FUNCTION set_updated_at();
```

**Q311. Add a composite primary key to a many-to-many junction table.**
```sql
ALTER TABLE enrollments
ADD CONSTRAINT pk_enrollments PRIMARY KEY (student_id, course_id);
```

**Q312. Create a schema and move a set of reporting tables into it.**
```sql
CREATE SCHEMA reporting;
ALTER TABLE monthly_sales_summary SET SCHEMA reporting;
```

**Q313. Add a default expression that auto-populates a created_at column with the current timestamp.**
```sql
ALTER TABLE orders
ADD COLUMN created_at TIMESTAMP NOT NULL DEFAULT NOW();
```

**Q314. Safely drop a table only if no foreign keys reference it.**
```sql
DROP TABLE IF EXISTS temp_staging_orders;
```

**Q315. Add a table-level exclusion constraint to prevent overlapping room bookings.**
```sql
ALTER TABLE bookings
ADD CONSTRAINT no_overlapping_bookings
EXCLUDE USING gist (
  room_id WITH =,
  tsrange(start_time, end_time) WITH &&
);
```

---

## D15 — Performance Tuning & Query Optimization (Q316–Q335)

*Reading execution plans, indexing strategy, and rewriting slow queries for large tables.*

**Q316. Use EXPLAIN ANALYZE to inspect how a slow customer-order query is being executed.**
```sql
EXPLAIN ANALYZE
SELECT c.name, SUM(o.amount)
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.name;
```

**Q317. Rewrite a NOT IN subquery as a NOT EXISTS to avoid NULL-related performance traps.**
```sql
-- Slow / risky with NULLs:
-- SELECT * FROM customers WHERE customer_id NOT IN (SELECT customer_id FROM orders);

-- Faster and NULL-safe:
SELECT c.*
FROM customers c
WHERE NOT EXISTS (
  SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id
);
```

**Q318. Rewrite a query that applies a function to an indexed column so the index can still be used.**
```sql
-- Prevents index usage:
-- SELECT * FROM orders WHERE EXTRACT(YEAR FROM order_date) = 2025;

-- Index-friendly range scan instead:
SELECT *
FROM orders
WHERE order_date >= '2025-01-01' AND order_date < '2026-01-01';
```

**Q319. Add a covering index so a common SELECT can be satisfied entirely from the index.**
```sql
CREATE INDEX idx_orders_covering
ON orders (customer_id, order_date) INCLUDE (amount);
```

**Q320. Rewrite a correlated subquery used for existence checks into a JOIN for large tables.**
```sql
-- Correlated subquery (can be slow row-by-row):
-- SELECT * FROM employees e WHERE EXISTS (SELECT 1 FROM project_assignments p WHERE p.employee_id = e.id);

-- Semi-join rewrite:
SELECT DISTINCT e.*
FROM employees e
JOIN project_assignments p ON p.employee_id = e.id;
```

**Q321. Use a CTE with MATERIALIZED hint to avoid re-computing an expensive aggregation multiple times.**
```sql
WITH monthly_totals AS MATERIALIZED (
  SELECT DATE_TRUNC('month', sale_date) AS month, SUM(amount) AS total
  FROM sales
  GROUP BY DATE_TRUNC('month', sale_date)
)
SELECT * FROM monthly_totals WHERE total > 100000
UNION ALL
SELECT * FROM monthly_totals WHERE total < 1000;
```

**Q322. Batch a large DELETE into smaller chunks to avoid long lock times.**
```sql
DELETE FROM logs
WHERE ctid IN (
  SELECT ctid FROM logs
  WHERE log_date < CURRENT_DATE - INTERVAL '1 year'
  LIMIT 10000
);
-- Repeat in a loop until zero rows are affected.
```

**Q323. Identify unused indexes that can be dropped to speed up writes.**
```sql
SELECT relname AS table_name, indexrelname AS index_name, idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0
ORDER BY relname;
```

**Q324. Rewrite a query using multiple OR conditions on the same column as an IN list.**
```sql
-- Harder to optimize:
-- SELECT * FROM orders WHERE status = 'pending' OR status = 'processing' OR status = 'shipped';

-- Cleaner and equally indexable:
SELECT *
FROM orders
WHERE status IN ('pending', 'processing', 'shipped');
```

**Q325. Use a window function instead of a self-join to avoid a quadratic execution plan.**
```sql
-- Slower self-join approach:
-- SELECT a.*, (SELECT MAX(amount) FROM orders b WHERE b.customer_id = a.customer_id) FROM orders a;

-- Single-pass window function instead:
SELECT customer_id, amount,
       MAX(amount) OVER (PARTITION BY customer_id) AS max_amount
FROM orders;
```

**Q326. Estimate table and index bloat to decide when a VACUUM/REINDEX is needed.**
```sql
SELECT relname, n_dead_tup, n_live_tup,
       ROUND(100.0 * n_dead_tup / NULLIF(n_live_tup + n_dead_tup, 0), 2) AS dead_pct
FROM pg_stat_user_tables
ORDER BY dead_pct DESC;
```

**Q327. Analyze a query plan to confirm a sequential scan is being replaced by an index scan after adding an index.**
```sql
CREATE INDEX idx_customers_email ON customers (email);

EXPLAIN ANALYZE
SELECT * FROM customers WHERE email = 'alice@example.com';
```

**Q328. Rewrite a SELECT * query to only fetch needed columns for a high-traffic endpoint.**
```sql
-- Avoid over-fetching:
-- SELECT * FROM products WHERE category_id = 3;

-- Fetch only what the endpoint needs:
SELECT product_id, product_name, price
FROM products
WHERE category_id = 3;
```

**Q329. Use LIMIT with an indexed ORDER BY to efficiently paginate a large orders table (keyset pagination).**
```sql
SELECT order_id, order_date, amount
FROM orders
WHERE order_date < '2025-06-01'
ORDER BY order_date DESC
LIMIT 20;
```

**Q330. Use EXPLAIN to compare a query before and after adding a partial index for frequently filtered active rows.**
```sql
CREATE INDEX idx_active_orders ON orders (order_date) WHERE status = 'active';

EXPLAIN ANALYZE
SELECT * FROM orders WHERE status = 'active' ORDER BY order_date DESC LIMIT 50;
```

**Q331. Break a single massive multi-join query into staged temp tables for readability and speed.**
```sql
CREATE TEMP TABLE tmp_customer_orders AS
SELECT customer_id, SUM(amount) AS total_spend
FROM orders
GROUP BY customer_id;

SELECT c.name, t.total_spend
FROM customers c
JOIN tmp_customer_orders t ON c.customer_id = t.customer_id
WHERE t.total_spend > 5000;
```

**Q332. Use ANALYZE to refresh table statistics after a large bulk load so the planner picks good plans.**
```sql
COPY orders FROM '/data/orders_bulk.csv' WITH (FORMAT csv, HEADER true);
ANALYZE orders;
```

**Q333. Detect and resolve a query that is blocked waiting on a lock from another session.**
```sql
SELECT blocked.pid AS blocked_pid, blocking.pid AS blocking_pid, blocked.query AS blocked_query
FROM pg_stat_activity blocked
JOIN pg_locks bl ON blocked.pid = bl.pid AND NOT bl.granted
JOIN pg_locks kl ON bl.locktype = kl.locktype AND bl.relation = kl.relation AND kl.granted
JOIN pg_stat_activity blocking ON kl.pid = blocking.pid
WHERE blocked.pid <> blocking.pid;
```

**Q334. Rewrite a query that uses DISTINCT to mask a join fan-out bug, replacing it with a pre-aggregated subquery.**
```sql
-- Masking symptom, not the cause:
-- SELECT DISTINCT c.customer_id, c.name FROM customers c JOIN orders o ON c.customer_id = o.customer_id;

-- Pre-aggregate before joining to avoid the fan-out entirely:
SELECT c.customer_id, c.name, o.order_count
FROM customers c
JOIN (
  SELECT customer_id, COUNT(*) AS order_count
  FROM orders
  GROUP BY customer_id
) o ON c.customer_id = o.customer_id;
```

**Q335. Use a hash-friendly equality rewrite to replace a slow range-based join condition where possible.**
```sql
-- Range join can be costly at scale:
-- SELECT * FROM events e JOIN sessions s ON e.event_time BETWEEN s.start_time AND s.end_time;

-- Pre-bucket into a shared key when granularity allows an equality join:
SELECT *
FROM events e
JOIN sessions s ON DATE_TRUNC('hour', e.event_time) = DATE_TRUNC('hour', s.start_time);
```

---

## D16 — Senior-Level Interview Challenges (Q336–Q350)

*Capstone problems that combine window functions, recursion, joins and aggregation in a single query.*

**Q336. Find the top 2 highest-paid employees per department, tie-broken by earliest join date, and show the department average alongside.**
```sql
SELECT *
FROM (
  SELECT e.*, d.avg_salary,
         ROW_NUMBER() OVER (
           PARTITION BY e.department_id
           ORDER BY e.salary DESC, e.join_date ASC
         ) AS rnk
  FROM employees e
  JOIN (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
  ) d ON e.department_id = d.department_id
) ranked
WHERE rnk <= 2;
```

**Q337. Build a full customer RFM (Recency, Frequency, Monetary) segmentation in one query.**
```sql
WITH rfm AS (
  SELECT customer_id,
         CURRENT_DATE - MAX(order_date) AS recency_days,
         COUNT(*)   AS frequency,
         SUM(amount) AS monetary
  FROM orders
  GROUP BY customer_id
),
scored AS (
  SELECT customer_id,
         NTILE(5) OVER (ORDER BY recency_days ASC) AS r_score,
         NTILE(5) OVER (ORDER BY frequency DESC)   AS f_score,
         NTILE(5) OVER (ORDER BY monetary DESC)    AS m_score
  FROM rfm
)
SELECT *, (r_score + f_score + m_score) AS rfm_total
FROM scored
ORDER BY rfm_total DESC;
```

**Q338. Find, for each department, the longest gap in months between any two consecutive employee hires.**
```sql
WITH hire_gaps AS (
  SELECT department_id, join_date,
         join_date - LAG(join_date) OVER (PARTITION BY department_id ORDER BY join_date) AS gap
  FROM employees
)
SELECT department_id, MAX(gap) AS longest_hiring_gap
FROM hire_gaps
GROUP BY department_id;
```

**Q339. Combine a recursive CTE and window function to rank each employee's salary among their entire management chain.**
```sql
WITH RECURSIVE chain AS (
  SELECT id, name, manager_id, salary, id AS root
  FROM employees
  WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id, e.salary, c.root
  FROM employees e
  JOIN chain c ON e.manager_id = c.id
)
SELECT id, name, root, salary,
       RANK() OVER (PARTITION BY root ORDER BY salary DESC) AS rank_in_chain
FROM chain;
```

**Q340. Find customers whose order frequency in the last 90 days has doubled compared to the previous 90 days.**
```sql
WITH periods AS (
  SELECT customer_id,
         COUNT(*) FILTER (WHERE order_date >= CURRENT_DATE - INTERVAL '90 days') AS recent_count,
         COUNT(*) FILTER (WHERE order_date >= CURRENT_DATE - INTERVAL '180 days'
                            AND order_date <  CURRENT_DATE - INTERVAL '90 days') AS prior_count
  FROM orders
  GROUP BY customer_id
)
SELECT customer_id, recent_count, prior_count
FROM periods
WHERE prior_count > 0 AND recent_count >= 2 * prior_count;
```

**Q341. Compute a full gaps-and-islands report of active subscription periods per user, merging overlapping ranges.**
```sql
WITH ordered AS (
  SELECT user_id, start_date, end_date,
         MAX(end_date) OVER (
           PARTITION BY user_id ORDER BY start_date
           ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
         ) AS prev_max_end
  FROM subscriptions
),
flagged AS (
  SELECT *, CASE WHEN start_date > prev_max_end OR prev_max_end IS NULL THEN 1 ELSE 0 END
            AS is_new_island
  FROM ordered
),
grouped AS (
  SELECT *, SUM(is_new_island) OVER (PARTITION BY user_id ORDER BY start_date) AS island_id
  FROM flagged
)
SELECT user_id, island_id, MIN(start_date) AS period_start, MAX(end_date) AS period_end
FROM grouped
GROUP BY user_id, island_id;
```

**Q342. Find the single day with the largest week-over-week percentage change in total revenue.**
```sql
WITH daily AS (
  SELECT sale_date, SUM(amount) AS total
  FROM sales
  GROUP BY sale_date
),
wow AS (
  SELECT sale_date, total,
         LAG(total, 7) OVER (ORDER BY sale_date) AS total_last_week
  FROM daily
)
SELECT sale_date, total, total_last_week,
       ROUND(100.0 * (total - total_last_week) / NULLIF(total_last_week, 0), 2) AS pct_change
FROM wow
ORDER BY ABS(pct_change) DESC
LIMIT 1;
```

**Q343. Design a query to detect potential duplicate customer accounts using fuzzy matching on name and phone.**
```sql
SELECT c1.customer_id AS customer_a, c2.customer_id AS customer_b
FROM customers c1
JOIN customers c2
  ON c1.customer_id < c2.customer_id
 AND (
   SOUNDEX(c1.name) = SOUNDEX(c2.name)
   OR c1.phone = c2.phone
 )
WHERE c1.email <> c2.email;
```

**Q344. Build a query that identifies employees eligible for a 'long service' award: 5+ years tenure, no more than 1 manager change, and above-median department performance.**
```sql
WITH tenure AS (
  SELECT id, department_id,
         EXTRACT(YEAR FROM AGE(CURRENT_DATE, join_date)) AS years_service
  FROM employees
),
mgr_changes AS (
  SELECT employee_id, COUNT(*) AS changes
  FROM manager_change_log
  GROUP BY employee_id
),
dept_perf AS (
  SELECT department_id,
         PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY performance_score) AS median_score
  FROM performance_reviews pr
  JOIN employees e ON pr.employee_id = e.id
  GROUP BY department_id
)
SELECT e.id, e.name
FROM employees e
JOIN tenure t ON e.id = t.id
LEFT JOIN mgr_changes m ON e.id = m.employee_id
JOIN dept_perf dp ON e.department_id = dp.department_id
JOIN performance_reviews pr ON pr.employee_id = e.id
WHERE t.years_service >= 5
  AND COALESCE(m.changes, 0) <= 1
  AND pr.performance_score > dp.median_score;
```

**Q345. Find the shortest path (fewest hops) between two products based on a 'frequently bought together' graph, using recursive CTEs.**
```sql
WITH RECURSIVE graph AS (
  SELECT product_a AS start_product, product_b AS current_product,
         ARRAY[product_a, product_b] AS path, 1 AS hops
  FROM product_pairs
  WHERE product_a = 'P100'
  UNION ALL
  SELECT g.start_product, pp.product_b, g.path || pp.product_b, g.hops + 1
  FROM product_pairs pp
  JOIN graph g ON pp.product_a = g.current_product
  WHERE NOT pp.product_b = ANY(g.path) AND g.hops < 5
)
SELECT * FROM graph WHERE current_product = 'P250' ORDER BY hops LIMIT 1;
```

**Q346. Compute a complete customer lifetime value (CLV) forecast combining historical average order value, purchase frequency, and estimated retention.**
```sql
WITH customer_stats AS (
  SELECT customer_id,
         AVG(amount) AS avg_order_value,
         COUNT(*)::NUMERIC
         / NULLIF(EXTRACT(YEAR FROM AGE(MAX(order_date), MIN(order_date))) + 1, 0)
         AS orders_per_year
  FROM orders
  GROUP BY customer_id
)
SELECT customer_id, avg_order_value, orders_per_year,
       ROUND(avg_order_value * orders_per_year * 3, 2) AS estimated_3yr_clv
FROM customer_stats
ORDER BY estimated_3yr_clv DESC;
```

**Q347. Write a single query to reconcile two ledgers (system A and system B) and report unmatched transactions on both sides.**
```sql
SELECT 'missing_in_b' AS discrepancy, a.transaction_id, a.amount
FROM ledger_a a
WHERE NOT EXISTS (SELECT 1 FROM ledger_b b
                  WHERE b.transaction_id = a.transaction_id AND b.amount = a.amount)
UNION ALL
SELECT 'missing_in_a' AS discrepancy, b.transaction_id, b.amount
FROM ledger_b b
WHERE NOT EXISTS (SELECT 1 FROM ledger_a a
                  WHERE a.transaction_id = b.transaction_id AND a.amount = b.amount);
```

**Q348. Design a query that flags potential salary-band inversions across an entire multi-level reporting chain.**
```sql
WITH RECURSIVE chain AS (
  SELECT id, name, manager_id, salary
  FROM employees
  WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id, e.salary
  FROM employees e
  JOIN chain c ON e.manager_id = c.id
)
SELECT e.id AS employee_id, e.name AS employee, e.salary AS employee_salary,
       m.id AS manager_id,  m.name AS manager,  m.salary AS manager_salary
FROM employees e
JOIN employees m ON e.manager_id = m.id
WHERE e.salary > m.salary;
```

**Q349. Build a single report combining top product per category, category revenue share, and month-over-month growth.**
```sql
WITH cat_month AS (
  SELECT p.category_id, DATE_TRUNC('month', o.order_date) AS month,
         SUM(oi.quantity * oi.price) AS revenue
  FROM order_items oi
  JOIN orders o   ON oi.order_id = o.order_id
  JOIN products p ON oi.product_id = p.product_id
  GROUP BY p.category_id, DATE_TRUNC('month', o.order_date)
),
growth AS (
  SELECT category_id, month, revenue,
         revenue - LAG(revenue) OVER (PARTITION BY category_id ORDER BY month) AS mom_growth,
         ROUND(100.0 * revenue / SUM(revenue) OVER (PARTITION BY month), 2) AS pct_share
  FROM cat_month
)
SELECT * FROM growth ORDER BY month, category_id;
```

**Q350. Design a single query that detects employees whose salary, title and department changed simultaneously in a way that looks like a data-entry error rather than a real promotion.**
```sql
WITH changes AS (
  SELECT employee_id, change_date,
         salary - LAG(salary) OVER (PARTITION BY employee_id ORDER BY change_date) AS salary_delta,
         title <> LAG(title) OVER (PARTITION BY employee_id ORDER BY change_date) AS title_changed,
         department_id <> LAG(department_id) OVER (PARTITION BY employee_id ORDER BY change_date) AS dept_changed
  FROM employee_change_log
)
SELECT *
FROM changes
WHERE salary_delta < 0 AND title_changed AND dept_changed;
```

---

# SECTION E — QUESTIONS FROM THE "SQL COMPLETE NOTES" PAGES

These are the interview questions printed on each page of the 10-page illustrated notes series. Answers are in **SQL-Complete-Notes.md** at the section noted.

## E1. DDL & DML Commands (Page 2)
1. What is the difference between DROP, TRUNCATE and DELETE? *(§8)*
2. What is the difference between DDL, DML, DCL, TCL and DQL? *(§4)*
3. How will you add a new column in an existing table? *(§7)*
4. Can we rollback after a TRUNCATE command? Why or why not? *(§8 — no in most RDBMS; TRUNCATE is DDL and deallocates pages rather than logging row deletions)*

## E2. DCL, TCL & Constraints (Page 3)

**DCL**
1. What is GRANT and REVOKE? *(§4)*
2. How do you give SELECT privilege on a table? — `GRANT SELECT ON Student TO john;`
3. How can you revoke all privileges from a user? — `REVOKE ALL PRIVILEGES ON <object> FROM <user>;`

**TCL**
4. What is the difference between COMMIT and ROLLBACK? *(§57)*
5. What is SAVEPOINT and how is it used? *(§57)*
6. Can we COMMIT a partial transaction? *(No — COMMIT commits everything since the transaction began. For partial undo use SAVEPOINT + ROLLBACK TO.)*

**Constraints**
7. What is the difference between PRIMARY KEY and UNIQUE? *(§10)*
8. When would you use a CHECK constraint? *(§9 — when values must satisfy a business rule, e.g. `age >= 18`)*
9. Can a table have multiple FOREIGN KEYs? *(Yes — one per relationship to a parent table.)*

**General**
10. What is the ACID property? *(§56)*
11. Why are constraints important in database design? *(§9 — they enforce data quality at the database level, where it cannot be bypassed by an application bug.)*
12. Give an example of a parent–child relationship in SQL. *(§10 — Department (parent) → Student (child) via `dept_id`.)*

**Key takeaway:** DCL secures data, TCL manages transactions, constraints ensure integrity.

## E3. SQL Functions (Page 4)
1. What is the difference between `COUNT(*)` and `COUNT(column)`? *(§25 — `COUNT(*)` counts all rows; `COUNT(column)` counts non-NULL values only.)*
2. How does `COUNT(column)` behave with NULL values? *(It skips them.)*
3. What is the difference between `WHERE 'IT'` and `Department = 'IT'`? *(The first is not a valid predicate; a filter must compare a column to a value.)*
4. How does `DATEDIFF()` work? Give an example. *(§29 — returns the difference between two dates: `DATEDIFF('2025-05-28','2025-05-01')` → 27.)*
5. How can you get the last 3 characters of a string? *(`RIGHT(name, 3)`, or `SUBSTRING(name, LENGTH(name)-2, 3)`.)*

**Key takeaway:** functions make SQL powerful and expressive — master them to write clean, efficient queries.

## E4. Filtering, Sorting & Clauses (Page 5)
1. What is the difference between WHERE and HAVING? *(§27)*
2. Explain the use of BETWEEN, IN and LIKE with examples. *(§20)*
3. How do you handle NULL values in SQL? *(§16)*
4. Why is ORDER BY applied after the WHERE clause? *(§24 — WHERE filters the rows first; ORDER BY sorts the final result set, so it runs near the end.)*

**Key takeaway:** use filtering, sorting and clauses to get the exact results you need — fast and accurate.

## E5. Joins in SQL (Page 6)
1. What is the difference between INNER JOIN and LEFT JOIN? *(§30)*
2. What is the result of a CROSS JOIN? *(§32 — the Cartesian product: every row of A paired with every row of B.)*
3. When would you use a SELF JOIN? Give an example. *(§31 — hierarchical data, e.g. employee → manager.)*
4. Explain the difference between WHERE and ON in JOINs. *(§30 — `ON` filters before the join; `WHERE` filters after, which can silently convert an outer join into an inner join.)*

**Common mistakes / tips:** always specify the join condition using ON; missing ON leads to a CROSS JOIN (a huge result); be careful with duplicate rows (one-to-many); use table aliases for readability.

## E6. GROUP BY, HAVING & CASE (Page 7)
1. What is the difference between WHERE and HAVING? Give an example. *(§27)*
2. Write a query to find departments with more than 2 employees.
   ```sql
   SELECT Dept, COUNT(*) FROM Employee GROUP BY Dept HAVING COUNT(*) > 2;
   ```
3. Write a query to show employee name, salary and salary level (High/Medium/Low) using CASE WHEN. *(§28)*
4. Write a query to find the department with the highest average salary.
   ```sql
   SELECT Dept, AVG(Salary) AS avg_sal
   FROM Employee GROUP BY Dept ORDER BY avg_sal DESC LIMIT 1;
   ```

**Best practices:** every non-aggregated column in SELECT must appear in GROUP BY; WHERE filters rows, HAVING filters groups; use meaningful aliases; CASE is powerful inside SELECT, ORDER BY and aggregate expressions.

## E7. Subqueries, CTEs & Set Operators (Page 8)
1. What is a subquery? What are the types of subqueries, with examples? *(§35)*
2. What is the difference between EXISTS and IN? When would you use each? *(§37 — EXISTS for existence checks, IN for value comparison.)*
3. What is a CTE? Write a query using a CTE to find the top 3 highest paid employees in each department. *(§39, §43)*
4. Explain UNION, UNION ALL, INTERSECT and EXCEPT with examples. What is the difference between UNION and UNION ALL? *(§33)*

**Common mistakes:** mismatched column count in UNION/INTERSECT; using UNION when duplicates are required; forgetting the correlated reference in a correlated subquery (`e2.col = e1.col`); using a subquery in the SELECT list that returns multiple rows; ORDER BY inside a subquery without LIMIT/FETCH (may not work in all DBs); placing ORDER BY before UNION instead of at the end.

## E8. Views, Indexes & Window Functions (Page 9)
1. What is the difference between a VIEW and a TABLE? Give one example. *(§48)*
2. What is an INDEX? How does it improve query performance? Explain with an example. *(§49)*
3. Explain the difference between ROW_NUMBER(), RANK() and DENSE_RANK() with an example. *(§43)*
4. What is the use of LEAD() and LAG() functions? Give one practical example. *(§44)*

**Best practices:** use indexes on frequently searched, joined or filtered columns; do not over-index (it slows writes); use views to simplify complex or repeated queries and to control data access; window functions are powerful for ranking, running totals and moving averages.

**Key takeaway:** use Views for simplicity, Indexes for speed, and Window Functions for deep analysis.

## E9. Interview Master Sheet (Page 10) — 23 rapid questions with hints

| # | Question | Hint |
|---|----------|------|
| 1 | What is SQL? | Language to communicate with RDBMS |
| 2 | What are different types of SQL commands? | DDL, DML, DCL, TCL, DQL |
| 3 | Difference between DBMS and RDBMS? | Relational, tables, keys, relations |
| 4 | DELETE vs TRUNCATE vs DROP? | Delete: rows \| Truncate: all rows \| Drop: table |
| 5 | WHERE vs HAVING? | WHERE: rows filter \| HAVING: group filter |
| 6 | CHAR vs VARCHAR? | CHAR: fixed length \| VARCHAR: variable length |
| 7 | What is NULL? | Unknown / missing value (not 0 or ' ') |
| 8 | Primary Key vs Foreign Key? | PK: unique & not null \| FK: references another key |
| 9 | What is a JOIN? | Combines rows from two tables |
| 10 | Subquery vs Correlated Subquery? | Independent subquery vs row-dependent |
| 11 | What is a Subquery? | Query inside another query |
| 12 | What is a View? | Virtual table based on a query |
| 13 | What are Window Functions? | OVER(), PARTITION BY, RANK(), SUM() OVER |
| 14 | What is Normalization? | Organising data to reduce redundancy |
| 15 | What is Indexing? | Speeds up search; created on columns |
| 16 | What is the ACID property? | Atomicity, Consistency, Isolation, Durability |
| 17 | What is a CTE? | Common Table Expression (WITH clause) |
| 18 | What is a Transaction? | Unit of work (COMMIT / ROLLBACK) |
| 19 | What is the use of GROUP BY? | Groups rows to apply aggregate functions |
| 20 | What is DISTINCT? | Returns unique rows |
| 21 | What is UNION vs UNION ALL? | UNION: unique \| UNION ALL: keeps duplicates |
| 22 | What is a Constraint? | Rules for data integrity (PK, FK, UNIQUE) |
| 23 | What is a Sequence? | Generates unique numbers |

**Common interview scenarios (write smart queries):**

| Scenario | Approach |
|----------|----------|
| Find the second highest salary | Use `ORDER BY` with `LIMIT`/`OFFSET` |
| Find duplicate rows in a table | `GROUP BY` + `HAVING COUNT(*) > 1` |
| Find running total of salary by dept | `SUM() OVER (PARTITION BY ... ORDER BY ...)` |
| Find Nth highest salary | `LIMIT`/`OFFSET` or `DENSE_RANK()` |
| Delete duplicate rows keeping one | `ROW_NUMBER() OVER (PARTITION BY ...)` |
| Top N salaries in each department | `RANK()` / `DENSE_RANK()` by partition |

**Sample interview tasks:**
1. List all employees with their department name.
2. Find employees whose salary is greater than the average salary in their department.
3. Find the number of employees in each department.
4. Show departments having more than 5 employees.
5. Find the top 3 expensive products in each category.

---

# SECTION F — INTERVIEW STRATEGY & QUICK REVISION

## Interview pro tips

- **Think out loud, explain your steps.** Interviewers score your reasoning, not just the final query.
- **Start with a simple solution, then optimize.** A working query you then improve beats a clever query that doesn't run.
- **Ask clarifying questions if unsure.** "Should ties be included in the top 3?" is a *good* question — it shows you think about edge cases.
- **Handle edge cases:** NULLs, duplicates, empty result sets, ties.
- **Write readable, maintainable queries.** Use aliases and CTEs; format consistently.
- **Test with small data, then scale.**
- **Stay calm, be confident.**

## The five patterns that cover most SQL interviews

If you have limited time, drill these until they are automatic:

1. **Nth highest / Top N per group** — `DENSE_RANK()` or `ROW_NUMBER()` inside a subquery, filtered outside. Know the LIMIT/OFFSET version too, and know why `WHERE rnk = 2` fails without the subquery.
2. **Finding duplicates and deleting them** — `GROUP BY ... HAVING COUNT(*) > 1` to find; `ROW_NUMBER()` keeping `rn = 1` to delete.
3. **Anti-join** — "customers with no orders", "products never sold". `LEFT JOIN ... WHERE right.key IS NULL`, or `NOT EXISTS`.
4. **Self join on a hierarchy** — employees vs managers. Know why you need `LEFT JOIN` to keep the CEO, and the `a.id < b.id` trick for pairs.
5. **Running totals and period-over-period** — `SUM() OVER (PARTITION BY ... ORDER BY ...)` and `LAG()`.

## Concept questions that come up almost every time

- DELETE vs TRUNCATE vs DROP
- WHERE vs HAVING
- INNER vs LEFT JOIN
- UNION vs UNION ALL
- ROW_NUMBER vs RANK vs DENSE_RANK
- Primary Key vs Unique Key
- Clustered vs Non-clustered index
- ACID properties
- Normalization forms
- What indexes cost you (writes, space)

## Common mistakes to avoid

- Using `= NULL` instead of `IS NULL`.
- Forgetting that `NOT IN` returns nothing if the subquery contains a NULL — use `NOT EXISTS`.
- Putting a filter on the right table in the `WHERE` of a `LEFT JOIN`, silently making it an inner join.
- Forgetting the `ON` clause and producing a Cartesian product.
- Trying to filter a window function in `WHERE` instead of wrapping it in a subquery.
- Using `LAST_VALUE` without an explicit frame.
- Non-aggregated columns in `SELECT` that aren't in `GROUP BY`.
- `ORDER BY` inside a `UNION` branch instead of at the end.
- Integer division (`100 / 3` = 33) when you wanted a percentage — use `100.0`.
- Reaching for `DISTINCT` to hide a join fan-out instead of fixing the join.

## Final mantra

**Write → Test → Optimize → Repeat → Excel.**

---

*Compiled from: sqlnotes.pdf (100 questions), sqlnotes2.pdf (50 questions), sqlnotes4.pdf (30 real interview questions), sql350questions.pdf (350 practice questions), the CTE deep-dive PDF, and the 10-page "SQL Complete Notes" screenshot series.*
