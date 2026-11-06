---
title: SQL-Complete-Notes
topic: databases
source_type: my-notes
source_file: STUDYNOTEs/SQL-Complete-Notes.md
---

# SQL Complete Notes — Beginner to Advanced

A single, step-by-step guide compiled from every file in this folder (handwritten class notes, the "SQL Complete Notes" 10-page series, the ctesql.pdf CTE deep-dive, and the concept sections of the interview PDFs).

Interview questions live in a separate file: **SQL-Interview-Questions.md**

---

## Table of Contents

**Part 1 — Foundations**
1. What is Data, a Database, a DBMS, an RDBMS
2. What is SQL (and how SQL differs from MySQL)
3. How SQL Actually Runs Your Query
4. The Five Families of SQL Commands (DDL, DML, DQL, DCL, TCL)
5. Data Types

**Part 2 — Building and Changing Tables (DDL)**
6. CREATE TABLE
7. ALTER TABLE
8. DROP vs TRUNCATE vs DELETE
9. Constraints (the rules that protect your data)
10. Keys: Primary, Foreign, Unique, Candidate
11. Normalization and Denormalization

**Part 3 — Working with Data (DML + DQL)**
12. INSERT
13. SELECT
14. UPDATE
15. DELETE
16. NULL values
17. WHERE and the comparison operators
18. AND, OR, NOT
19. DISTINCT
20. BETWEEN, IN, LIKE and wildcards
21. ORDER BY
22. LIMIT / TOP / FETCH FIRST
23. Aliases (AS)
24. SQL Query Execution Order — the single most important diagram

**Part 4 — Summarizing Data**
25. Aggregate functions
26. GROUP BY
27. HAVING (and WHERE vs HAVING)
28. CASE WHEN
29. String, Numeric and Date functions

**Part 5 — Combining Tables**
30. Joins — the whole family
31. Self Join
32. Cross Join
33. UNION, UNION ALL, INTERSECT, EXCEPT
34. LATERAL joins and anti-joins

**Part 6 — Query Building Blocks**
35. Subqueries
36. Correlated subqueries
37. EXISTS vs IN
38. ANY and ALL
39. CTEs (Common Table Expressions) — full deep dive
40. Recursive CTEs
41. Temporary tables and table variables

**Part 7 — Analytics**
42. Window functions
43. ROW_NUMBER vs RANK vs DENSE_RANK
44. Running totals, moving averages, LEAD/LAG
45. NTILE, PERCENT_RANK, CUME_DIST, FIRST_VALUE/LAST_VALUE/NTH_VALUE
46. Pivot and Unpivot
47. Gaps and Islands

**Part 8 — Objects and Programmability**
48. Views and Materialized Views
49. Indexes
50. Stored Procedures and Functions
51. Triggers
52. Cursors
53. Sequences and Auto Increment
54. Dynamic SQL
55. JSON and XML in SQL

**Part 9 — Transactions and Reliability**
56. Transactions and the ACID properties
57. COMMIT, ROLLBACK, SAVEPOINT
58. Deadlocks
59. Isolation levels

**Part 10 — Performance**
60. What indexing really does
61. Query execution plans
62. Query optimization rules
63. Table partitioning
64. Index fragmentation
65. OLTP vs OLAP

**Part 11 — Reference**
66. Types of errors in SQL
67. Cheat sheet
68. Practice schema used throughout

---

# PART 1 — FOUNDATIONS

## 1. What is Data, a Database, a DBMS, an RDBMS

**Data** is raw facts — a name, an age, a salary amount. On its own it means little.

**Database** — an organized collection of data stored electronically so that it can be easily accessed, managed and updated.

> Think of it as a digital filing cabinet where data is stored in a structured way.

Example: a customer database on an e-commerce site stores each customer's name, email, contact number and purchase history.

**DBMS (Database Management System)** — the *software* that lets you create, store, manage and retrieve data from a database. You never talk to the raw files on disk; you talk to the DBMS.

```
   You  ───►   DBMS   ───►   Database (files on disk)
```

Examples of DBMS: MySQL, PostgreSQL, Oracle, SQL Server, SQLite.

### Types of DBMS

**1. Relational DBMS (RDBMS)** — data is stored in **tables** made of rows and columns, and tables are related to each other.

| Roll No | Name  | Class |
|---------|-------|-------|
| 1       | Jai   | 5th   |
| 2       | Amar  | 7th   |
| 3       | Anuj  | 5th   |
| 4       | Ram   | 8th   |

Examples: MySQL, PostgreSQL, Oracle, SQL Server.

**2. Non-Relational DBMS (NoSQL)** — data is stored as key–value pairs, documents, graphs etc., not in fixed tables.

```json
{
  "RollNo": 1,
  "Class": "5th",
  "Name": "Jai"
}
```

Examples: MongoDB, Redis.

### Vocabulary you must lock in now

| Term | Means |
|------|-------|
| Table | A grid of data (also called a *relation*) |
| Row | One record. Also called a **tuple** |
| Column | One field/attribute of every record. Also called an **attribute** |
| Field | One cell — one column's value in one row |

```
Database  →  Table  →  Row (one record)  →  Column (one field)
```

Example table `Employee`:

| ID | Name | Age | Dept | Salary |
|----|------|-----|------|--------|
| 1  | Abhi | 22  | IT   | 50000  |
| 2  | Ravi | 23  | HR   | 45000  |
| 3  | Sita | 21  | IT   | 52000  |

---

## 2. What is SQL (and how SQL differs from MySQL)

**SQL** stands for **Structured Query Language**. It is the standard language used to communicate with relational databases — to store, retrieve, update and delete data, and to create and modify database structures such as tables, views and indexes.

```sql
SELECT * FROM Employees;
```
That query retrieves every record from the `Employees` table.

### SQL vs MySQL — a very common point of confusion

| | SQL | MySQL |
|---|---|---|
| What it is | A **language** | A **software** (an RDBMS) |
| Definition | Structured Query Language, used to manage and manipulate databases | A relational database management system that *uses* SQL |
| Usage | Used to write queries that interact with databases | Used to store, manage and retrieve data |
| Developer | Standard language developed by ANSI | Developed by Oracle Corporation |
| Platform | Universal — used by MySQL, Oracle, SQL Server, PostgreSQL… | Specific to MySQL |

> **Remember:** *SQL is the language. MySQL is the software that uses SQL.*

### Case sensitivity

- SQL **keywords** are case-insensitive: `SELECT` and `select` both work. By convention we write them in UPPERCASE.
- **Column names** — usually not case-sensitive (MySQL, SQL Server).
- **Table names** — depends on the database and the operating system. On Linux MySQL table names *are* case-sensitive; on Windows they are not.
- **String values** — MySQL compares strings case-insensitively by default.

To force a case-sensitive comparison in MySQL, use `BINARY`:

```sql
SELECT * FROM Employee WHERE BINARY Name = 'Vinay';
```

Given rows `(101, 'Vinay')` and `(102, 'VINAY')`, a normal `WHERE Name = 'Vinay'` returns both. With `BINARY`, only row 101 comes back.

Every statement ends with a semicolon `;`.

---

## 3. How SQL Actually Runs Your Query

```
        SQL Query
            │
            ▼
  Query Language Processor   ◄── Parser + Optimizer
            │
            ▼
       DBMS Engine           ◄── File Manager + Transaction Manager
            │
            ▼
    Physical Database
```

- **Parsing** — the query statement is broken into tokens and checked for valid syntax.
- **Optimising** — the optimizer picks the best algorithm / access path to execute the query.
- **DBMS Engine** — the file manager finds the data on disk; the transaction manager keeps the operation safe and consistent.
- **Physical Database** — the actual bytes on disk.

You never choose *how* the data is fetched. You describe *what* you want; the optimizer decides how. That is why SQL is called a **declarative** language — and why understanding indexes and execution plans (Part 10) matters so much.

---

## 4. The Five Families of SQL Commands

Every SQL command belongs to one of five groups. Interviewers ask this constantly.

| Family | Full name | What it does | Commands |
|--------|-----------|--------------|----------|
| **DDL** | Data Definition Language | Defines/changes the **structure** of the database | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DML** | Data Manipulation Language | Manages the **data** inside the structure | `INSERT`, `UPDATE`, `DELETE` |
| **DQL** | Data Query Language | **Retrieves** data | `SELECT` |
| **DCL** | Data Control Language | Controls **access** and permissions | `GRANT`, `REVOKE` |
| **TCL** | Transaction Control Language | Manages **transactions** | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

Memory hooks:
- **DDL → structure**-related commands.
- **DML → data**-related commands.
- **CRUD** = Create (INSERT), Read (SELECT), Update (UPDATE), Delete (DELETE).
- CREATE → makes · ALTER → changes · DROP → deletes · TRUNCATE → empties.

Note that `SELECT` is sometimes listed under DML and sometimes given its own family, DQL. Both answers are accepted; say DQL and mention that some books group it with DML.

### ALTER vs UPDATE — they sound similar and are completely different

| ALTER | UPDATE |
|-------|--------|
| It is a **DDL** command | It is a **DML** command |
| Used for adding, deleting and modifying **attributes (columns)** of a table | Used for updating the **data** in an existing table |
| Changes are made to the **table structure** | Changes are made to the **data** |
| By default, all values in the tuple are initialized as NULL when a new column is added with ALTER | It sets the specified value into the tuple |

---

## 5. Data Types

Data types tell the database what kind of value a column can hold, and how much space to reserve.

### The common ones

| Category | Types | Notes |
|----------|-------|-------|
| Whole numbers | `INT`, `BIGINT`, `SMALLINT`, `TINYINT` | Use `INT` for IDs and counts |
| Decimals | `DECIMAL(p,s)`, `NUMERIC(p,s)`, `FLOAT`, `DOUBLE` | Use `DECIMAL` for money — `FLOAT` has rounding errors |
| Text | `CHAR(n)`, `VARCHAR(n)`, `TEXT` | See the CHAR vs VARCHAR table below |
| Dates & times | `DATE`, `TIME`, `DATETIME`, `TIMESTAMP` | `TIMESTAMP` usually stores time-zone-aware instants |
| True/False | `BOOLEAN` / `BIT` | |
| Semi-structured | `JSON`, `XML` | See Part 8 |

### CHAR vs VARCHAR

| Criteria | CHAR | VARCHAR |
|----------|------|---------|
| Full form | Character | Variable Character |
| Storage | Fixed-length | Variable-length |
| Memory usage | Always uses the specified length, even if fewer characters are stored | Uses only the space required for the actual data, plus one or two bytes for length |
| Performance | Faster for fixed-size data | Slower for varying data sizes |
| Padding | Pads extra spaces to match the fixed length | Does not pad spaces |
| Use case | When data length is consistent (PIN codes, gender, country codes) | When data length varies (names, addresses) |

```sql
CREATE TABLE Person (
    Name    CHAR(10),      -- always takes 10 bytes
    Address VARCHAR(200)   -- takes only what it needs
);
```

---

# PART 2 — BUILDING AND CHANGING TABLES (DDL)

## 6. CREATE TABLE

`CREATE` is a DDL command used to create databases and tables.

**Syntax**
```sql
CREATE TABLE tablename (
    column1 datatype,
    column2 datatype,
    ...
);
```

**Example**
```sql
CREATE TABLE User (
    FirstName VARCHAR(50),
    LastName  VARCHAR(50),
    Email_id  VARCHAR(100),
    Password  VARCHAR(50)
);
```

Result — an empty table with this shape:

| FirstName | LastName | Email_id | Password |
|-----------|----------|----------|----------|

A more realistic example with types and a key:

```sql
CREATE TABLE Student (
    id     INT,
    name   VARCHAR(50),
    age    INT,
    course VARCHAR(50)
);
```

---

## 7. ALTER TABLE

`ALTER` modifies an **existing table's structure**.

```sql
-- Add a column
ALTER TABLE table_name ADD column_name datatype;
ALTER TABLE Student ADD email VARCHAR(50);

-- Change a column's datatype
ALTER TABLE table_name MODIFY column_name datatype;    -- MySQL/Oracle
ALTER TABLE Student MODIFY age INT;

ALTER TABLE table_name ALTER COLUMN col TYPE datatype;  -- PostgreSQL
ALTER TABLE products ALTER COLUMN product_name TYPE VARCHAR(255);

-- Remove a column
ALTER TABLE table_name DROP COLUMN column_name;
ALTER TABLE Student DROP COLUMN email;

-- Rename a column
ALTER TABLE customers RENAME COLUMN phone TO phone_number;

-- Rename a table
ALTER TABLE clients RENAME TO customers;
```

Adding a NOT NULL column to a table that already has rows requires a default, otherwise existing rows would violate the constraint:

```sql
ALTER TABLE employees
ADD COLUMN is_active BOOLEAN NOT NULL DEFAULT TRUE;
```

Adding a timestamp that fills itself in:
```sql
ALTER TABLE orders
ADD COLUMN created_at TIMESTAMP NOT NULL DEFAULT NOW();
```

A trick for renaming a table without breaking code that still uses the old name — rename it, then leave a view behind under the old name:
```sql
ALTER TABLE clients RENAME TO customers;
CREATE VIEW clients AS SELECT * FROM customers;
```

---

## 8. DROP vs TRUNCATE vs DELETE

This is one of the most-asked interview questions in existence. Learn the table.

```sql
DROP TABLE table_name;          -- deletes the table and its structure
TRUNCATE TABLE table_name;      -- deletes all rows, keeps the empty table
DELETE FROM table_name WHERE condition;   -- deletes chosen rows
```

| Feature | DELETE | TRUNCATE | DROP |
|---------|--------|----------|------|
| Family | DML | DDL | DDL |
| Removes data | Yes — specific rows | Yes — all rows | Yes — the whole table |
| `WHERE` clause | Yes | No | No |
| Table structure | Remains | Remains | **Removed** |
| Rollback | Yes (inside a transaction) | No (in most RDBMS) | No |
| Logging | Logs each deleted row | Minimal logging | — |
| Speed | Slow (row-by-row) | Fast | Fastest |
| Identity / auto-increment | Retains current value | Resets to the initial seed | Gone with the table |
| Use case | Partial deletion, audit trail needed | Full data wipe, no audit needed | Remove the object entirely |

**Once a table is dropped, the data cannot be recovered.** Be careful.

Rules of thumb:
- Use `DELETE` to remove specific rows with a condition.
- Use `TRUNCATE` to empty a table quickly when you do not need rollback.
- Use `DROP` to remove both the data and the table structure.

---

## 9. Constraints — the rules that protect your data

**Constraints are the rules and restrictions applied to the data in a table.** They are also called **Integrity Constraints**, because their job is to keep the data correct.

```
                     Constraints
    ┌────────┬────────┬─────────┬────────┬──────────┬───────────┬────────┐
  CHECK   UNIQUE   DEFAULT   INDEX   NOT NULL  PRIMARY KEY  FOREIGN KEY
```

| Constraint | Meaning | Syntax (mini) | Example |
|-----------|---------|---------------|---------|
| **NOT NULL** | Column cannot have a NULL value | `col_name DATA_TYPE NOT NULL` | `age INT NOT NULL` |
| **UNIQUE** | All values in the column must be unique | `col_name DATA_TYPE UNIQUE` | `email VARCHAR(100) UNIQUE` |
| **PRIMARY KEY** | Uniquely identifies each row | `col_name DATA_TYPE PRIMARY KEY` | `id INT PRIMARY KEY` |
| **FOREIGN KEY** | Maintains a link between two tables | `col DATA_TYPE FOREIGN KEY REFERENCES parent_table(col)` | `dept_id INT FOREIGN KEY REFERENCES Department(dept_id)` |
| **CHECK** | Ensures values satisfy a condition | `CONSTRAINT chk_name CHECK (condition)` | `age INT CHECK (age >= 18)` |
| **DEFAULT** | Sets a default value if none is provided | `col_name DATA_TYPE DEFAULT default_value` | `status VARCHAR(10) DEFAULT 'Active'` |
| **AUTO_INCREMENT / IDENTITY** | Auto-generates a unique numeric value | `col_name INT AUTO_INCREMENT` | `id INT AUTO_INCREMENT` |
| **INDEX** | Speeds up the read process | `CREATE INDEX ix ON t(col)` | see Part 10 |

### NOT NULL in detail
Ensures a column cannot contain NULL — it enforces that every row must have a value there.
- Prevents insertion of NULL values
- Ensures mandatory fields have data
- Can be applied to one or more columns

```sql
CREATE TABLE Employees (
    Name  VARCHAR(50) NOT NULL,   -- must always have a value
    Email VARCHAR(100)            -- may be NULL
);
```

### DEFAULT in detail
Provides a default value for a column when no value is supplied during insert.
- Automatically assigns a default if no value is given
- Helps avoid NULLs in specific columns
- Can be applied to any data type

```sql
CREATE TABLE Employees (
    EmpID  INT,
    Salary DECIMAL(10,2) DEFAULT 5000
);
INSERT INTO Employees (EmpID) VALUES (1);   -- Salary becomes 5000
```

### Adding constraints after the fact

```sql
-- CHECK
ALTER TABLE employees
ADD CONSTRAINT chk_salary_positive CHECK (salary > 0);

-- UNIQUE
ALTER TABLE employees
ADD CONSTRAINT uq_employee_email UNIQUE (email);

-- FOREIGN KEY (clean up orphans first, or it will fail)
DELETE FROM orders
WHERE customer_id NOT IN (SELECT customer_id FROM customers);

ALTER TABLE orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (customer_id) REFERENCES customers(customer_id);

-- Composite primary key on a junction table
ALTER TABLE enrollments
ADD CONSTRAINT pk_enrollments PRIMARY KEY (student_id, course_id);

-- Self-referencing FK for a manager hierarchy
ALTER TABLE employees
ADD CONSTRAINT fk_manager
FOREIGN KEY (manager_id) REFERENCES employees(id);
```

### ON DELETE CASCADE
The `CASCADE DELETE` constraint automatically deletes related rows in child tables when a row in the parent table is deleted.

```sql
ALTER TABLE order_items
DROP CONSTRAINT fk_order_items_order,
ADD CONSTRAINT fk_order_items_order
FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE;
```

Constraints improve data quality. Always design them in from the start — retrofitting them onto dirty data is painful.

---

## 10. Keys: Primary, Foreign, Unique, Candidate

### Primary Key
A column (or combination of columns) that **uniquely identifies each row** in a table.

- Uniquely identifies each record
- Cannot have duplicate values
- **Cannot contain NULL values**
- Only **one** primary key is allowed per table
- Automatically creates a unique **clustered** index

```sql
CREATE TABLE tablename (
    column1 datatype,
    column2 datatype,
    PRIMARY KEY (column1)
);
```

Worked example:

| Roll No | Name | Address |
|---------|------|---------|
| 1 | Atul | Delhi |
| 2 | Abhi | Mumbai |
| 3 | Zayn | Delhi |

Name and Address are not unique (two people live in Delhi). Roll No **is** unique — so Roll No is the primary key.

### Foreign Key
A column (or combination) in one table that **refers to the Primary Key in another table**. It creates the relationship between two tables and enforces **referential integrity**.

- Establishes a relationship between two tables
- **Can contain duplicate values**
- **Can accept NULL values** (and multiple NULLs)
- Helps maintain data consistency

```sql
CREATE TABLE tablename (
    column1 datatype,
    column2 datatype,
    FOREIGN KEY (column1) REFERENCES ParentTable(PrimaryKeyColumn)
);
```

Worked example — Student (child) → Department (parent):

**Student (Child Table)**

| id (PK) | name | dept_id (FK) | age |
|---------|------|--------------|-----|
| 1 | Abhi | 10 | 22 |
| 2 | Ravi | 20 | 23 |
| 3 | Sita | 10 | 21 |

**Department (Parent Table)**

| dept_id (PK) | dept_name |
|--------------|-----------|
| 10 | IT |
| 20 | HR |
| 30 | Finance |

`Student.dept_id → Department.dept_id` is the foreign key relationship.

A second worked example from the class notes — Student table + Result table. If you want to check Roll No. 3's marks in Maths, you need the two tables linked, so you add Roll No to the Result table where it acts as a foreign key:

| Maths | Science | English | Roll No. |
|-------|---------|---------|----------|
| 10% | 80% | 70% | 1 |
| 90% | 60% | 20% | 2 |
| 70% | 30% | 21% | 3 |

### UNIQUE Key
A constraint that ensures all values in a column (or combination) are **distinct across all rows**. It prevents duplicates but **allows NULL** (usually one NULL).

- Ensures uniqueness of each record in the column
- Allows one NULL value (depending on the database)
- Multiple UNIQUE keys can be defined in a table
- Creates a unique **non-clustered** index

### Primary Key vs UNIQUE Key

| Primary Key | UNIQUE Key |
|-------------|------------|
| Uniquely identifies each row in a table | Ensures all values in the column are unique |
| Does **not** allow NULL values | Allows one NULL value (in most databases) |
| Only **one** primary key per table | **Multiple** UNIQUE keys can be defined |
| Automatically creates a unique **clustered** index | Creates a unique **non-clustered** index |
| Used to uniquely *identify* a record | Used to *enforce uniqueness* without being the primary identifier |

### Unique constraint vs unique index
A unique **constraint** ensures uniqueness of values in one or more columns. A unique **index** enforces the uniqueness *and* improves query performance. In practice most engines implement the constraint using an index.

### Candidate Key
A set of one or more columns that **could potentially become the primary key** — each candidate key can uniquely identify rows.

A table can have **multiple candidate keys but only one primary key.** The primary key is simply the candidate key you *chose*.

Quick summary:

| Key | Description |
|-----|-------------|
| Primary Key | Uniquely identifies each row in a table. Cannot be NULL or duplicate. |
| Foreign Key | References the primary key of another table to maintain a relationship. |
| Candidate Key | A column (or set) that can uniquely identify rows. The primary key is one of them. |

### Database vs Schema
A **database** is a container that holds multiple objects — tables, views, indexes, procedures. It represents a logical grouping of related data.

A **schema** is a container *within* a database that holds objects and defines their ownership. It organizes and manages database objects.

```sql
CREATE SCHEMA reporting;
ALTER TABLE monthly_sales_summary SET SCHEMA reporting;
```

---

## 11. Normalization and Denormalization

### Normalization
**Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity.** It works by dividing large tables into smaller related tables and defining relationships between them.

Why bother:
- Reduces data redundancy
- Improves data consistency
- Simplifies data maintenance
- Increases data integrity

**The normal forms:**

1. **1NF (First Normal Form)** — eliminates duplicate columns and ensures each column contains **atomic** (indivisible) values.
2. **2NF (Second Normal Form)** — no **partial dependency**; every non-key attribute is fully dependent on the whole primary key.
3. **3NF (Third Normal Form)** — removes **transitive dependencies**, where non-key columns depend on other non-key columns.
4. **BCNF (Boyce-Codd Normal Form)** — ensures that every determinant is a candidate key.
5. **4NF (Fourth Normal Form)** — removes multi-valued dependencies.
6. **5NF (Fifth Normal Form / Project-Join Normal Form, PJNF)** — removes join dependencies.

**Worked example**

Unnormalized table — the department name and location repeat on every employee row:

| EmployeeID | EmployeeName | Department | DepartmentLocation |
|------------|--------------|------------|--------------------|
| 101 | Vinay | IT | Bangalore |
| 102 | Awadhesh | IT | Bangalore |

Normalized (1NF & 2NF) — split into two tables:

**Employee Table**

| EmployeeID | EmployeeName | DepartmentID |
|------------|--------------|--------------|
| 101 | Vinay | 1 |
| 102 | Awadhesh | 1 |

**Department Table**

| DepartmentID | DepartmentName | Location |
|--------------|----------------|----------|
| 1 | IT | Bangalore |

Now if the IT department moves office, you change **one** row instead of thousands.

### Denormalization
**Denormalization is the process of combining tables or adding redundant data to improve read performance at the cost of data redundancy.** It is the opposite of normalization, used when fast data retrieval matters more than tight data integrity.

- Improves data retrieval speed
- Increases data redundancy
- Reduces the number of joins required
- Used in data warehouses and reporting systems

Denormalized version of the example above:

| EmployeeID | EmployeeName | DepartmentName |
|------------|--------------|----------------|
| 101 | Vinay | IT |
| 102 | Awadhesh | HR |

`DepartmentName` is stored directly in the Employee table, making retrieval faster but increasing redundancy.

---

# PART 3 — WORKING WITH DATA (DML + DQL)

## 12. INSERT

Used to insert data into tables.

**Syntax**
```sql
INSERT INTO tableName (column1, column2, ...)
VALUES (value1, value2, ...);
```

> **Note:** there must be the same number of values as the number of columns specified.

**Example**
```sql
INSERT INTO USER (FirstName, LastName, Email_id, Password)
VALUES ('Jai', 'Sharma', 'abc@gmail.com', 'abc#123');
```

| FirstName | LastName | Email_id | Password |
|-----------|----------|----------|----------|
| Jai | Sharma | abc@gmail.com | abc#123 |

**Inserting multiple records (rows / tuples) at once**
```sql
INSERT INTO USER (FirstName, LastName, Email_id, Password)
VALUES ('Jai',  'Sharma', 'abc@gmail.com', '123'),
       ('Jaya', 'Sharma', 'xyz@gmail.com', 'abc');
```

Starting from this table:

| FirstName | LastName | Age |
|-----------|----------|-----|
| Jai | Kumar | 10 |
| Jaya | Singh | 15 |
| Amit | Sharma | 20 |

```sql
INSERT INTO user (FirstName, LastName, Age) VALUES ('abc', 'xyz', 25);
```

| FirstName | LastName | Age |
|-----------|----------|-----|
| Jai | Kumar | 10 |
| Jaya | Singh | 15 |
| Amit | Sharma | 20 |
| abc | xyz | 25 |

---

## 13. SELECT

Used to retrieve data from a table.

**Syntax**
```sql
SELECT column1, column2
FROM tableName;
```

To select the complete table, use `*` (star):
```sql
SELECT *
FROM tableName;
```

**Example** — table `USER`:

| FirstName | LastName | Password |
|-----------|----------|----------|
| Jai | Kumar | 123 |
| Jaya | Singh | abc |
| Amit | Sharma | xyz |

```sql
SELECT FirstName FROM USER;
```

Output:

| FirstName |
|-----------|
| Jai |
| Jaya |
| Amit |

> In production code, **avoid `SELECT *`** — name the columns you need. It reduces network traffic and lets indexes cover the query (see Part 10).

---

## 14. UPDATE

Used to modify existing data in a table.

**Syntax**
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE some_column = some_value;
```

`SET` specifies the column and the value to update.

**Example** — table `Users`:

| FirstName | LastName | Age |
|-----------|----------|-----|
| Jai | Kumar | 10 |
| Jaya | Singh | 15 |
| Amit | Sharma | 20 |

```sql
UPDATE USERS
SET age = age + 1;
```

Output:

| FirstName | LastName | Age |
|-----------|----------|-----|
| Jai | Kumar | 11 |
| Jaya | Singh | 16 |
| Amit | Sharma | 21 |

> **Warning:** an `UPDATE` without a `WHERE` clause updates **every row**, as it did here. That was intentional in this example — usually it is a bug.

---

## 15. DELETE

Used to remove existing records from a table.

**Syntax**
```sql
DELETE FROM tablename WHERE condition;
```

> **Note:** this operation is not reversible once committed, so be careful when using DELETE statements.

```sql
DELETE FROM Student WHERE id = 1;
```

Without a `WHERE` clause it will delete **all records**.

---

## 16. NULL Values

`NULL` is used to represent **missing or unknown data**.

> **Note:** NULL is different from zero and from an empty string. NULL is "we don't know", not "nothing".

Insert a NULL:
```sql
INSERT INTO tablename (column1, column2, ...)
VALUES (value1, NULL, ...);
```

### Checking for NULL

You cannot use `= NULL`. NULL is never equal to anything, not even to another NULL. Use `IS NULL` / `IS NOT NULL`:

```sql
SELECT column1, column2
FROM table_name
WHERE column2 IS NULL;

SELECT column1, column2
FROM table_name
WHERE column1 IS NOT NULL;
```

### Five ways to handle NULLs

1. **IS NULL** — check if a column contains NULL.
   ```sql
   SELECT * FROM employees WHERE manager_id IS NULL;
   ```
2. **IS NOT NULL** — check if a column does not contain NULL.
3. **COALESCE()** — returns the first non-NULL value from a list of expressions.
   ```sql
   SELECT name, COALESCE(phone_number, 'Not Provided') AS contact
   FROM customers;
   ```
   - Returns the first non-null value
   - Used to handle NULL values
   - Can accept multiple expressions
4. **IFNULL() (MySQL) / NVL() (Oracle) / ISNULL() (SQL Server)** — replaces NULL with a specified value.
   ```sql
   SELECT NVL(Salary, 0) FROM Employees;      -- Oracle
   SELECT IFNULL(Salary, 0) FROM Employees;   -- MySQL
   ```
5. **NULLIF()** — returns NULL if two expressions are equal. Handy for avoiding divide-by-zero:
   ```sql
   SELECT total / NULLIF(count_value, 0) FROM t;
   ```

### NULL handling in aggregates — an interview favourite

- `COUNT(*)` counts **all rows**, including those with NULLs.
- `COUNT(column)` counts **only non-NULL values** in that column.
- `SUM()`, `AVG()`, `MAX()`, `MIN()` **ignore NULLs**.
- If all values are NULL, `SUM` and `AVG` return NULL (not 0).

```sql
SELECT name,
       CASE WHEN salary IS NULL THEN 'Unknown' ELSE 'Known' END AS salary_status
FROM employees;
```

**Remember: NULL ≠ 0, NULL ≠ '' (empty string), NULL ≠ FALSE.**

---

## 17. WHERE and the comparison operators

`WHERE` filters rows in a table based on a specified condition.

**Syntax**
```sql
SELECT column_name
FROM table_name
WHERE condition;
```

**Example** — table `USER`:

| FirstName | LastName | Age |
|-----------|----------|-----|
| Jai | Kumar | 19 |
| Jaya | Singh | 20 |
| Amit | Sharma | 21 |

```sql
SELECT FirstName, LastName
FROM USER
WHERE Age > 20;
```

Output:

| FirstName | LastName |
|-----------|----------|
| Amit | Sharma |

### Common operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `=` | Equal | `age = 22` |
| `>` | Greater than | `salary > 50000` |
| `<` | Less than | `age < 30` |
| `>=` | Greater than or equal | `salary >= 40000` |
| `<=` | Less than or equal | `age <= 25` |
| `!=` or `<>` | Not equal | `dept != 'HR'` |

`WHERE` also works with `UPDATE` and `DELETE`, not just `SELECT`.

---

## 18. AND, OR, NOT

These three combine conditions in a WHERE clause to create more complex filtering.

**AND** — returns true if **both** conditions are true, false otherwise.
```sql
WHERE condition1 AND condition2;
WHERE age > 20 AND dept = 'IT'
```

**OR** — returns true if **either** condition is true; false only if both are false.
```sql
WHERE condition1 OR condition2;
WHERE salary > 50000 OR dept = 'HR'
```

**NOT** — returns the opposite of a condition.
```sql
WHERE NOT condition;
WHERE NOT (dept = 'HR')
```

Use parentheses when mixing AND with OR — `AND` binds tighter than `OR`, and forgetting that is a classic bug:

```sql
-- These mean different things!
WHERE a = 1 OR a = 2 AND b = 3
WHERE (a = 1 OR a = 2) AND b = 3
```

---

## 19. DISTINCT

`DISTINCT` returns only **unique values** from a specified column in a table.

**Syntax**
```sql
SELECT DISTINCT column_name
FROM table_name;
```

**Example** — table `USER`:

| FirstName | LastName | Password |
|-----------|----------|----------|
| Jai | Kumar | 123 |
| Jaya | Singh | 123 |
| Amit | Sharma | xyz |

```sql
SELECT DISTINCT Password FROM USER;
```

Output:

| Password |
|----------|
| 123 |
| xyz |

`DISTINCT` across multiple columns removes duplicate *combinations*, not duplicates per column.

> A caution you will meet again in Part 10: if you find yourself adding `DISTINCT` to fix duplicate rows appearing after a JOIN, you probably have a join fan-out bug. `DISTINCT` hides the symptom; pre-aggregating fixes the cause.

---

## 20. BETWEEN, IN, LIKE and wildcards

### BETWEEN
Filters data based on a range of values. **Inclusive of both ends.**
```sql
SELECT column1, column2
FROM table_name
WHERE column_name BETWEEN value1 AND value2;

SELECT * FROM employees WHERE salary BETWEEN 40000 AND 80000;
WHERE age BETWEEN 20 AND 30
```

### IN
Specifies multiple values in a WHERE clause for filtering data — much cleaner than a chain of ORs.
```sql
SELECT column1, column2
FROM table_name
WHERE column_name IN (value1, value2);

SELECT * FROM employees WHERE job_title IN ('Manager','Director');
WHERE dept IN ('IT','HR','Finance')
```

### LIKE and wildcards
**Wildcards** are special characters used with the `LIKE` operator to search for a specific pattern in a column.

- The **percent sign `%`** represents zero, one, or multiple characters.
- The **underscore `_`** represents one single character.

```sql
SELECT column1, column2
FROM table_name
WHERE column_name LIKE pattern;
```

| Pattern | Matches |
|---------|---------|
| `'A%'` | Names starting with A |
| `'%n'` | Names ending with n |
| `'%an%'` | Names containing "an" anywhere |
| `'%an_'` | "an" followed by exactly one more character |
| `'% %'` | Values containing a space (i.e. more than one word) |

```sql
SELECT * FROM employees WHERE name LIKE 'A%';    -- starts with 'A'
SELECT * FROM employees WHERE email NOT LIKE '%@%';  -- invalid emails
```

---

## 21. ORDER BY

Sorts the result of a query in ascending or descending order.

**Syntax**
```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;
```

- **ASC** — sorts the result in ascending order (this is the default).
- **DESC** — sorts the result in descending order.

**Example** — table `User`:

| FirstName | LastName | Age |
|-----------|----------|-----|
| Jai | Kumar | 49 |
| Jaya | Singh | 20 |
| Amit | Sharma | 21 |

```sql
SELECT * FROM user ORDER BY Age;
```

Output:

| FirstName | LastName | Age |
|-----------|----------|-----|
| Jaya | Singh | 20 |
| Amit | Sharma | 21 |
| Jai | Kumar | 49 |

Multi-column sort:
```sql
SELECT name, salary
FROM Employee
ORDER BY salary DESC, name ASC;
```

### GROUP BY vs ORDER BY

| GROUP BY | ORDER BY |
|----------|----------|
| Groups rows based on the same values in one or more columns | Sorts the result set in ascending or descending order |
| Almost always used with aggregate functions like COUNT(), SUM(), AVG() | Does not require aggregate functions |
| Comes **before** ORDER BY in the statement | Always comes **after** GROUP BY |
| Groups the result into summary rows | Sorts the entire result set |
| Example: group sales by product category | Example: sort sales from highest to lowest amount |

---

## 22. LIMIT / TOP / FETCH FIRST

Restricts the number of rows returned by a query. The syntax varies by database — use the one your DB supports.

```sql
-- MySQL / PostgreSQL / SQLite
SELECT * FROM Employee LIMIT 5;

-- SQL Server
SELECT TOP 5 * FROM Employee;

-- Oracle / PostgreSQL (ANSI standard)
SELECT * FROM Employee FETCH FIRST 5 ROWS ONLY;
```

Combined with `ORDER BY`, this is how you get "Top N":

```sql
-- Top 3 highest salaries
SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 3;
```

`OFFSET` skips rows — this is the basis of pagination and of "Nth highest" queries:

```sql
-- 3rd highest salary: skip the top 2, take the next 1
SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 2;
```

`LIMIT` is commonly used for **Top N records** and **pagination**.

---

## 23. Aliases (AS)

An **alias** is a temporary name given to a table or a column in a query. Aliases make results readable and queries easier to write.

**Syntax**
```sql
SELECT column_name AS alias_name
FROM table_name;
```

**Column alias**
```sql
SELECT name   AS employee_name,
       salary AS monthly_salary
FROM Employee;
```

**Table alias**
```sql
SELECT e.name, e.dept
FROM Employee e
WHERE e.salary > 50000;
```

Table aliases are **required** for self joins (Part 5), where the same table appears twice and you must tell the two copies apart. The alias name can be referenced in the WHERE clause to identify a particular table or column.

---

## 24. SQL Query Execution Order — the single most important diagram

You *write* a query in one order. The database *runs* it in a different order. Knowing the real order explains most beginner confusion — for instance, why you cannot use a `SELECT` alias in a `WHERE` clause, and why `HAVING` can use aggregates but `WHERE` cannot.

**Written order:**
```
SELECT → FROM → JOIN → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT
```

**Actual execution order:**
```
FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
  1      2       3         4         5        6         7        8
```

Step by step:

1. **FROM** — specify the tables from which data is fetched.
2. **JOIN** — combine data from tables based on a common field.
3. **WHERE** — filter individual **rows** based on the given condition.
4. **GROUP BY** — group records based on your requirement.
5. **HAVING** — filter the **groups**.
6. **SELECT** — retrieve the columns (this is where aliases are created).
7. **ORDER BY** — sort the data in ascending or descending order.
8. **LIMIT** — specify how many rows are returned.

**Consequences you can now explain:**
- `WHERE` runs *before* grouping → it cannot see aggregate values → `WHERE COUNT(*) > 2` is an error. Use `HAVING`.
- `SELECT` runs *after* `WHERE` → an alias defined in SELECT cannot be used in WHERE.
- `ORDER BY` runs *after* `SELECT` → an alias defined in SELECT **can** be used in ORDER BY.

**Simple query-writing flow to follow when composing a query:**
```
SELECT      FROM       WHERE     ORDER BY   LIMIT/TOP
choose  →  choose  →  filter  →   sort   →  limit rows
columns    table(s)    rows      results    (optional)
```

### Worked examples: execution order on one table

Every example below uses this table. I ran each query in SQLite and pasted the real results. Two of them
are marked, because SQLite accepts things that standard SQL and PostgreSQL reject.

```sql
CREATE TABLE employees (id INT PRIMARY KEY, name VARCHAR(50), dept VARCHAR(20), salary INT);
INSERT INTO employees VALUES
 (1,'Ann','IT',60000),(2,'Bo','IT',50000),(3,'Cy','IT',70000),
 (4,'Di','HR',45000),(5,'Ed','HR',48000),(6,'Flo','Ops',52000);
```

| id | name | dept | salary |
|---|---|---|---|
| 1 | Ann | IT | 60000 |
| 2 | Bo | IT | 50000 |
| 3 | Cy | IT | 70000 |
| 4 | Di | HR | 45000 |
| 5 | Ed | HR | 48000 |
| 6 | Flo | Ops | 52000 |

**1. `WHERE` can't use an aggregate** (it runs before grouping, so there are no groups yet)
```sql
SELECT dept, COUNT(*) FROM employees WHERE COUNT(*) > 2 GROUP BY dept;
-- error: misuse of aggregate: COUNT()
```

**2. `HAVING` is the fix** (it runs after the groups exist)
```sql
SELECT dept, COUNT(*) AS n FROM employees GROUP BY dept HAVING COUNT(*) > 2;
-- IT | 3
```

**3. An alias works in `ORDER BY`** (`SELECT` already ran)
```sql
SELECT name, salary * 12 AS yearly FROM employees ORDER BY yearly DESC;
-- Cy 840000, Ann 720000, Flo 624000, Bo 600000, Ed 576000, Di 540000
```

**4. In `WHERE`, repeat the expression** (`SELECT` hasn't run yet, so the alias doesn't exist)
```sql
SELECT name, salary * 12 AS yearly FROM employees WHERE salary * 12 > 600000;
-- Ann 720000, Cy 840000, Flo 624000
```

**5. Alias in `WHERE`: SQLite is lenient.** Standard SQL, PostgreSQL and SQL Server reject it
(`column "yearly" does not exist`). SQLite accepts it, so never judge legality from SQLite alone.
```sql
SELECT name, salary * 12 AS yearly FROM employees WHERE yearly > 600000;
-- SQLite: Ann 720000, Cy 840000, Flo 624000
```

**6. `WHERE` and `HAVING` together.** `WHERE` filters rows before grouping; `HAVING` filters groups after.
```sql
SELECT dept, AVG(salary) AS avg_sal
FROM employees
WHERE salary > 46000
GROUP BY dept
HAVING AVG(salary) > 50000
ORDER BY avg_sal DESC;
-- IT | 60000.0
-- Ops | 52000.0
```
Follow it in order: `WHERE` removes Di (45000). `GROUP BY` makes IT, HR (Ed only) and Ops. `HAVING`
drops HR (48000). `ORDER BY avg_sal` works because `SELECT` already created the alias.

**7. `WHERE` changes what gets counted**
```sql
SELECT dept, COUNT(*) AS n FROM employees WHERE salary > 50000 GROUP BY dept;
-- IT | 2        (Bo, at exactly 50000, is removed before counting)
-- Ops | 1       (HR disappears: nobody there earns over 50000)
```

**8. `DISTINCT`, `ORDER BY` and `LIMIT` in order**
```sql
SELECT DISTINCT dept FROM employees ORDER BY dept DESC LIMIT 2;
-- Ops
-- IT
```

**9. Alias in `HAVING`: SQLite and MySQL are lenient.** PostgreSQL and the standard reject it. The safe
form uses the aggregate itself.
```sql
SELECT dept, COUNT(*) AS n FROM employees GROUP BY dept HAVING n > 2;       -- SQLite only
SELECT dept, COUNT(*) AS n FROM employees GROUP BY dept HAVING COUNT(*) > 2; -- works everywhere
```

### From a sentence to a query: words to clauses

| Phrase in the problem statement | Clause |
|---|---|
| a condition on each row ("employees earning...", "in IT") | `WHERE` |
| "for each X" | `GROUP BY X` |
| a condition on a group's total ("departments with at least 2...") | `HAVING` |
| "highest / lowest first" | `ORDER BY ... DESC / ASC` |
| "the top N" | `LIMIT N` |

The wording that decides `WHERE` or `HAVING` is **when** the condition applies. "Of the employees who earn
more than 46,000, the average" filters people **before** averaging, so `WHERE`. "Departments whose average is
above 50,000" filters groups **after** averaging, so `HAVING`.

**The rule for `GROUP BY`:** every column in the `SELECT` list must be either in the `GROUP BY` or inside an
aggregate (`MAX`, `COUNT`, `AVG`...). After grouping there is one row per group, so a plain column like `name`
has several values and the database can't pick one. Standard SQL and PostgreSQL give an error; SQLite
silently shows a value from the max row, which isn't portable.

**Written order of the clauses:** `SELECT`, `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`, `LIMIT`.
A query always needs `FROM`. Text values use **single** quotes (`'IT'`); standard SQL reads double quotes as a
column name.

### Practice: three problem statements, solved clause by clause

**1. "List each department with its number of employees, but only departments with at least 2 employees,
largest first."**

My notes, clause by clause: *each department* → `GROUP BY dept`; *count* → `COUNT(*)`;
*at least 2* → `HAVING COUNT(*) >= 2`; *largest first* → `ORDER BY ... DESC`.
```sql
SELECT dept, COUNT(*) AS n
FROM employees
GROUP BY dept
HAVING COUNT(*) >= 2
ORDER BY n DESC;
-- IT | 3
-- HR | 2          (Ops has 1 employee, so HAVING drops it)
```
`HAVING` must use the aggregate (`COUNT(*) >= 2`), not the alias `n`, to work everywhere.

**2. "Show the names and salaries of employees in IT who earn more than 55,000, highest salary first."**

My notes: *names and salaries* → `SELECT name, salary`; *employees* → `FROM employees`;
*in IT who earn more than 55,000* → `WHERE salary > 55000 AND dept = 'IT'`; *highest first* →
`ORDER BY salary DESC`. No grouping is needed, because each row is one employee.
```sql
SELECT name, salary
FROM employees
WHERE salary > 55000 AND dept = 'IT'
ORDER BY salary DESC;
-- Cy  | 70000
-- Ann | 60000
```

**3. "For each department, show the highest salary among employees earning less than 70,000."**

My notes: *highest salary* → `MAX(salary)`; *among employees earning less than 70,000* → a condition on
**people**, so `WHERE salary < 70000`; *for each department* → `GROUP BY dept`. Don't put `name` in the `SELECT`
list: it isn't in the `GROUP BY` and isn't aggregated.
```sql
SELECT dept, MAX(salary) AS max_salary
FROM employees
WHERE salary < 70000
GROUP BY dept;
-- HR  | 48000
-- IT  | 60000
-- Ops | 52000
```
If the `70000` test were in `HAVING MAX(salary) < 70000` instead, Cy's 70000 would already be IT's max and
**IT would disappear completely**. `WHERE` removes the person and keeps IT at 60000; `HAVING` removes the
whole department. To see the name of the highest earner as well you need a subquery or a window function,
which come later in the notes.

---

# PART 4 — SUMMARIZING DATA

## 25. Aggregate Functions

Aggregate functions **work on multiple rows and return a single value**.

| Function | Description | Syntax | Example | Result |
|----------|-------------|--------|---------|--------|
| `COUNT(*)` | Counts number of rows | `SELECT COUNT(*) FROM Employee;` | `SELECT COUNT(*) FROM Employee;` | Total number of employees |
| `SUM()` | Returns sum of numeric values | `SELECT SUM(Salary) FROM Employee;` | `SELECT SUM(Salary) FROM Employee;` | Total salary |
| `AVG()` | Returns average of numeric values | `SELECT AVG(Salary) FROM Employee;` | `SELECT AVG(Salary) FROM Employee;` | Average salary |
| `MAX()` | Returns maximum value | `SELECT MAX(Salary) FROM Employee;` | `SELECT MAX(Salary) FROM Employee;` | Highest salary |
| `MIN()` | Returns minimum value | `SELECT MIN(Salary) FROM Employee;` | `SELECT MIN(Salary) FROM Employee;` | Lowest salary |

Others you will meet: `STDDEV()`, `VARIANCE()`, `GROUP_CONCAT()` (MySQL) / `STRING_AGG()` (Postgres).

Recall the NULL rules from §16: `COUNT(*)` counts every row; `COUNT(column)` counts only non-NULL values; `SUM`/`AVG`/`MAX`/`MIN` ignore NULLs entirely.

Combined example:
```sql
SELECT UPPER(Name)  AS Name_Upper,
       COUNT(*)     AS Total_Employees,
       AVG(Salary)  AS Avg_Salary,
       MAX(Salary)  AS Max_Salary
FROM Employee
WHERE Department = 'IT';
```

---

## 26. GROUP BY

`GROUP BY` groups rows that have the same values into **summary rows**, like "find the number of customers in each city". It is typically used with aggregate functions to perform a calculation on each group.

- Groups data based on one or more columns
- Used to summarize data
- Always used **after** the WHERE clause and **before** the ORDER BY clause

**Syntax**
```sql
SELECT column1, AGG_FUNC(column2)
FROM table_name
GROUP BY column1, column2, ...;
```

**Example — total salary per department**
```sql
SELECT Dept,
       COUNT(*)    AS Total_Employees,
       SUM(Salary) AS Total_Salary,
       AVG(Salary) AS Avg_Salary
FROM Employee
GROUP BY Dept;
```

| Dept | Total_Employees | Total_Salary | Avg_Salary |
|------|-----------------|--------------|------------|
| IT | 3 | 147000 | 49000.00 |
| HR | 2 | 97000 | 48500.00 |
| Finance | 2 | 69000 | 34500.00 |

**Raw rows vs grouped summary** — this is the mental picture to keep:

Raw rows (`Employee`):

| ID | Name | Dept | Salary |
|----|------|------|--------|
| 1 | Abhi | IT | 50000 |
| 2 | Ravi | IT | 45000 |
| 3 | Sita | HR | 52000 |
| 4 | Neha | HR | 45000 |
| 5 | Omar | Finance | 30000 |
| 6 | Priya | Finance | 39000 |

`GROUP BY Dept` →

| Dept | Emp_Count | Total_Salary | Avg_Salary |
|------|-----------|--------------|------------|
| Finance | 2 | 69000 | 34500.00 |
| HR | 2 | 97000 | 48500.00 |
| IT | 2 | 95000 | 47500.00 |

**The golden rule:** every non-aggregated column in the SELECT list must appear in the GROUP BY clause.

More examples:
```sql
-- Total sales per product category
SELECT category, SUM(amount) AS total_sales
FROM Sales
GROUP BY category;

-- Number of employees in each department
SELECT DepartmentID, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY DepartmentID;

-- Highest salary in each department
SELECT DepartmentID, MAX(Salary) AS HighestSalary
FROM Employees
GROUP BY DepartmentID;
```

---

## 27. HAVING (and WHERE vs HAVING)

`HAVING` filters **groups** based on the value of an aggregate function. It works **after** GROUP BY. You cannot use aggregate functions in WHERE.

**Syntax**
```sql
SELECT column1, AGG_FUNC(column2)
FROM table_name
GROUP BY column1
HAVING condition;
```

**Example — departments with more than 2 employees**
```sql
SELECT Dept, COUNT(*) AS Total_Employees
FROM Employee
GROUP BY Dept
HAVING COUNT(*) > 2;
```

### WHERE vs HAVING — the classic comparison

| Aspect | WHERE (Row Filter) | HAVING (Group Filter) |
|--------|--------------------|-----------------------|
| When applied | Filters rows **before** grouping | Filters groups **after** grouping |
| Aggregate functions | **Cannot** use aggregate functions | **Can** use aggregate functions |
| Works on | Individual rows | Groups |
| Used with | `SELECT`, `UPDATE`, `DELETE` | `SELECT` with `GROUP BY` |
| Performance | Improves performance (filters early) | Slightly slower (runs after grouping) |
| Usage | Used with or without GROUP BY | Used only with GROUP BY |
| Execution order | Applied **before** GROUP BY | Applied **after** GROUP BY |

Both together:
```sql
SELECT department_id, COUNT(*) AS emp_count
FROM employees
WHERE salary > 30000          -- 1. filter rows first
GROUP BY department_id        -- 2. then group
HAVING COUNT(*) > 5;          -- 3. then filter groups
```

Performance tip: filter as much as you can in `WHERE` — filtering rows early means fewer rows to group.

---

## 28. CASE WHEN

The `CASE` statement applies conditional logic inside SQL, similar to IF/ELSE in other languages. It returns a different value based on the conditions you specify.

**Syntax**
```sql
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ...
    ELSE resultN
END AS alias
```

**Example — salary level**
```sql
SELECT Name, Salary,
       CASE
           WHEN Salary >= 70000 THEN 'High'
           WHEN Salary >= 40000 THEN 'Medium'
           ELSE 'Low'
       END AS Salary_Level
FROM Employee;
```

Another example with three tiers:
```sql
SELECT name, salary,
       CASE
           WHEN salary >= 100000 THEN 'High'
           WHEN salary >= 50000  THEN 'Medium'
           ELSE 'Low'
       END AS salary_category
FROM employees;
```

CASE works inside `SELECT`, `WHERE`, `ORDER BY` and inside aggregate expressions — that last one is how you build pivots (§46) and conditional counts:

```sql
-- Conditional aggregation: revenue split by channel, one row per month
SELECT DATE_TRUNC('month', sale_date) AS month,
       SUM(CASE WHEN channel = 'online'   THEN amount ELSE 0 END) AS online_revenue,
       SUM(CASE WHEN channel = 'in_store' THEN amount ELSE 0 END) AS in_store_revenue
FROM sales
GROUP BY DATE_TRUNC('month', sale_date);
```

CASE is also how you write an aging report:
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

---

## 29. String, Numeric and Date Functions

**Functions are predefined formulas in SQL that perform a specific operation and return a value.**

Why SQL functions are used:
- To perform calculations on the data
- To modify individual data items
- To manipulate the output
- To format dates and numbers
- To convert data types

### A. String functions

| Function | Description | Syntax | Example | Result |
|----------|-------------|--------|---------|--------|
| `UPPER()` | Converts string to upper case | `SELECT UPPER(Name) FROM Employee;` | `SELECT UPPER('abhi');` | `ABHI` |
| `LOWER()` | Converts string to lower case | `SELECT LOWER(Name) FROM Employee;` | `SELECT LOWER('ABHI');` | `abhi` |
| `LENGTH()` / `LEN()` | Returns length of string | `SELECT LENGTH(Name) FROM Employee;` | `SELECT LENGTH('tajamul');` | `8` |
| `CONCAT()` | Joins two or more strings | `SELECT CONCAT(FirstName,' ',LastName) FROM Employee;` | `SELECT CONCAT('Abhi',' ','Khan');` | `Abhi Khan` |
| `SUBSTRING()` | Extracts part of a string | `SELECT SUBSTRING(Name, start, length) FROM Employee;` | `SELECT SUBSTRING('tajamul',1,4);` | `taja` |

Also common: `TRIM()`, `REPLACE()`, `INITCAP()`, `REVERSE()`, `POSITION()`/`INSTR()`, `LPAD()`/`RPAD()`.

Useful string patterns:
```sql
-- Concatenate (PostgreSQL || operator)
SELECT first_name || ' ' || last_name AS full_name FROM employees;

-- Extract the domain from an email
SELECT email, SUBSTRING(email FROM POSITION('@' IN email) + 1) AS domain
FROM employees;

-- Position of a substring
SELECT email, POSITION('mail' IN email) AS position_in_string FROM employees;

-- Trim whitespace
SELECT TRIM(product_name) AS cleaned_name FROM products;

-- Replace spaces with underscores
SELECT product_name, REPLACE(product_name,' ','_') AS slug FROM products;

-- Reverse a string
SELECT name, REVERSE(name) AS reversed_name FROM customers;

-- Longest / shortest name
SELECT name, LENGTH(name) AS name_length FROM employees ORDER BY LENGTH(name) DESC LIMIT 1;

-- Count the vowels in each name (a neat trick: length minus length-without-vowels)
SELECT name,
       LENGTH(name) -
       LENGTH(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(
         LOWER(name),'a',''),'e',''),'i',''),'o',''),'u','')) AS vowel_count
FROM employees;

-- Regex matching (PostgreSQL)
SELECT * FROM employees WHERE name ~ '^[A-Za-z ]+$';        -- letters only
SELECT * FROM customers WHERE phone !~ '^[0-9]{10}$';        -- not a 10-digit number

-- Case-insensitive duplicate names
SELECT LOWER(name) AS name_lower, COUNT(*)
FROM employees
GROUP BY LOWER(name)
HAVING COUNT(*) > 1;
```

### B. Numeric functions

| Function | Description | Example | Result |
|----------|-------------|---------|--------|
| `ROUND()` | Rounds to n decimal places | `SELECT ROUND(123.456, 2);` | `123.46` |
| `CEIL()` / `CEILING()` | Rounds up to nearest integer | `SELECT CEIL(45.2);` | `46` |
| `FLOOR()` | Rounds down to nearest integer | `SELECT FLOOR(45.8);` | `45` |
| `ABS()` | Returns absolute value | `SELECT ABS(-25);` | `25` |

Also: `POWER()`, `MOD()`, `CAST()`, `CONVERT()`.

`MOD()` is how you find odd and even records:
```sql
SELECT * FROM Employee WHERE MOD(EmpID, 2) = 0;   -- even
SELECT * FROM Employee WHERE MOD(EmpID, 2) = 1;   -- odd
```
`MOD(EmpID, 2)` returns the remainder when EmpID is divided by 2. Remainder 0 → even, remainder 1 → odd.

### C. Date functions

| Function | Description | Example | Result (sample) |
|----------|-------------|---------|-----------------|
| `NOW()` / `CURRENT_TIMESTAMP` | Returns current date & time | `SELECT NOW();` | `2025-05-28 14:30:25` |
| `CURDATE()` / `CURRENT_DATE` | Returns current date | `SELECT CURDATE();` | `2025-05-28` |
| `DATEDIFF()` | Returns difference in days between two dates | `SELECT DATEDIFF('2025-05-28','2025-05-01');` | `27` |
| `DATEADD()` / `DATE_ADD()` | Adds an interval to a date | `SELECT DATEADD(DAY, 7, '2025-05-28');` | `2025-06-04` |

Also: `EXTRACT()`, `DATE_TRUNC()`, `TO_CHAR()`, `FORMAT()`, `AGE()`.

**Calculating age from date of birth**

Method 1 — using DATEDIFF (MySQL), accurate:
```sql
SELECT Name, FLOOR(DATEDIFF(CURDATE(), DOB) / 365.25) AS Age
FROM Employees;
```
- `CURDATE()` returns the current date
- `DATEDIFF()` gives the difference in days
- `FLOOR()` converts the result to whole years

Method 2 — using YEAR (MySQL), simple year-based:
```sql
SELECT Name, YEAR(CURDATE()) - YEAR(DOB) AS Age FROM Employees;
```

PostgreSQL:
```sql
SELECT name, dob, EXTRACT(YEAR FROM AGE(CURRENT_DATE, dob)) AS age FROM employees;
```

**Other common date patterns**
```sql
-- Joined in the last 6 months
SELECT * FROM employees WHERE join_date >= CURRENT_DATE - INTERVAL '6 months';

-- Joined in the last 3 months (MySQL, two ways)
SELECT * FROM Employees WHERE DATEDIFF(CURDATE(), JoinDate) <= 90;
SELECT * FROM Employees WHERE JoinDate >= DATE_ADD(CURDATE(), INTERVAL -3 MONTH);

-- Hired this calendar year
SELECT * FROM employees
WHERE EXTRACT(YEAR FROM join_date) = EXTRACT(YEAR FROM CURRENT_DATE);

-- Orders placed on weekends (0 = Sunday, 6 = Saturday)
SELECT * FROM orders WHERE EXTRACT(DOW FROM order_date) IN (0, 6);

-- Work anniversary this month
SELECT * FROM employees
WHERE EXTRACT(MONTH FROM join_date) = EXTRACT(MONTH FROM CURRENT_DATE);

-- Bucket by month / week / quarter
SELECT DATE_TRUNC('month', activity_date) AS month, COUNT(DISTINCT user_id) AS active_users
FROM user_activity
GROUP BY DATE_TRUNC('month', activity_date);

SELECT DATE_TRUNC('week', signup_date) AS week, COUNT(*) AS new_customers
FROM customers GROUP BY DATE_TRUNC('week', signup_date);

SELECT EXTRACT(QUARTER FROM sale_date) AS quarter, SUM(amount) AS total_sales
FROM sales GROUP BY EXTRACT(QUARTER FROM sale_date);

-- Busiest day of the week
SELECT TO_CHAR(order_date,'Day') AS day_of_week, COUNT(*) AS total_orders
FROM orders
GROUP BY TO_CHAR(order_date,'Day')
ORDER BY total_orders DESC
LIMIT 1;

-- Last 24 hours
SELECT * FROM orders WHERE order_timestamp >= NOW() - INTERVAL '24 hours';

-- Days between hire date and today
SELECT name, join_date, CURRENT_DATE - join_date AS days_employed FROM employees;

-- Shipping took more than 5 days
SELECT * FROM orders WHERE shipped_date - order_date > 5;

-- Convert a UTC timestamp to another time zone
SELECT order_id, order_timestamp AT TIME ZONE 'UTC' AT TIME ZONE 'Asia/Kolkata' AS local_time
FROM orders;
```

### D. Functions can be nested
```sql
SELECT UPPER(SUBSTRING(Name, 1, 3)) FROM Employee;
SELECT ROUND(AVG(Salary), 2) FROM Employee;
```

### E. Calculating a percentage
```sql
-- Percentage of employees in each department
SELECT DepartmentID,
       COUNT(*) * 100.0 / (SELECT COUNT(*) FROM Employees) AS Percentage
FROM Employees
GROUP BY DepartmentID;
```
Multiply by `100.0` (not `100`) to force floating-point division — integer division would truncate the result to 0.

---

# PART 5 — COMBINING TABLES

## 30. Joins — the whole family

**Joins combine rows from two or more tables based on a related column between them.** They let you access information from multiple tables at once — and they are what makes normalization (§11) practical: you split data into clean tables, then join them back together when you need them.

### The six types

1. **INNER JOIN** — returns only matching rows from both tables.
2. **LEFT JOIN** — all rows from the left table + matching rows from the right.
3. **RIGHT JOIN** — all rows from the right table + matching rows from the left.
4. **FULL JOIN** — all rows from both tables (matching and non-matching).
5. **SELF JOIN** — joins a table with itself.
6. **CROSS JOIN** — the Cartesian product of both tables (all possible combinations).

### Visual intuition

```
INNER JOIN        (○●○)   Only matching rows
LEFT JOIN         (●●○)   All from left + match
RIGHT JOIN        (○●●)   All from right + match
FULL OUTER JOIN   (●●●)   All from both sides
CROSS JOIN        (:::)   All combinations
```

### Sample data used below

**Customers (C)**

| id | name | city |
|----|------|------|
| 1 | Abhi | Delhi |
| 2 | Ravi | Mumbai |
| 3 | Sita | Pune |

**Orders (O)**

| id | customer_id | amount |
|----|-------------|--------|
| 101 | 1 | 2500 |
| 102 | 1 | 1500 |
| 103 | 3 | 3000 |
| 104 | 4 | 4000 |

---

### INNER JOIN

Combines rows from two or more tables based on a matching condition. Returns **only** those records where the condition is true in both tables.

- Returns matching rows from both tables
- Ignores unmatched rows
- The most commonly used type of join

```sql
SELECT column_name
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```

```sql
SELECT * FROM Customers C
INNER JOIN Orders O ON C.id = O.customer_id;
```

Output:

| C.id | C.name | O.id | O.amount |
|------|--------|------|----------|
| 1 | Abhi | 101 | 2500 |
| 1 | Abhi | 102 | 1500 |
| 3 | Sita | 103 | 3000 |

Notice Ravi (no orders) and order 104 (no matching customer) both disappear. That is the definition of an inner join: the **intersection**.

Realistic use:
```sql
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;
```
Returns employee names alongside their department names where DepartmentID exists in both tables.

---

### LEFT JOIN (LEFT OUTER JOIN)

Returns **all records from the left table** and the matching records from the right table. If there is no match, the result contains NULL values from the right table.

```sql
SELECT column_name
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
```

```sql
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id;
```
Returns all employee names; where no department is assigned, `department_name` shows NULL.

**When to use LEFT JOIN instead of INNER JOIN:** when you want all records from the left table even if there is no matching record on the right.

> Real scenario — "List all customers and their transactions, even if they haven't made any."
> ```sql
> SELECT c.customer_id, c.name, t.transaction_id, t.amount
> FROM customers c
> LEFT JOIN transactions t ON c.customer_id = t.customer_id;
> ```
> An INNER JOIN would silently exclude customers with zero activity — which is exactly the group you often care about.

**The LEFT JOIN + IS NULL anti-join pattern** — this is one of the most valuable patterns in SQL. It finds rows in the left table that have *no* match on the right:

```sql
-- Employees not assigned to any department
SELECT e.*
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
WHERE d.department_id IS NULL;

-- Customers who never placed an order
SELECT c.*
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- Products never sold
SELECT p.*
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
WHERE oi.product_id IS NULL;

-- Orphaned order_items whose product no longer exists
SELECT oi.*
FROM order_items oi
LEFT JOIN products p ON oi.product_id = p.product_id
WHERE p.product_id IS NULL;

-- Employees who never took a day of leave
SELECT e.*
FROM employees e
LEFT JOIN leave_records l ON e.id = l.employee_id
WHERE l.employee_id IS NULL;

-- Customers with no purchase in the last 6 months
-- (note the date condition goes in the ON clause, not WHERE — see the tip below)
SELECT c.customer_id, c.name
FROM customers c
LEFT JOIN transactions t
  ON c.customer_id = t.customer_id
 AND t.transaction_date >= CURRENT_DATE - INTERVAL '6 months'
WHERE t.customer_id IS NULL;
```

> **Critical tip — WHERE vs ON in an outer join.** In a LEFT JOIN, a condition in `ON` filters *before* the join (rows still survive with NULLs); a condition in `WHERE` filters *after* the join and will silently turn your LEFT JOIN back into an INNER JOIN. In the churn query above, moving `t.transaction_date >= ...` into WHERE would break it completely.

---

### RIGHT JOIN (RIGHT OUTER JOIN)

Returns **all records from the right table** and the matching records from the left table. If there is no match, the result contains NULL values from the left table.

```sql
SELECT column_name
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;
```

```sql
SELECT e.EmployeeName, d.DepartmentName
FROM Employees e
RIGHT JOIN Departments d ON e.DepartmentID = d.DepartmentID;
```
Returns all department names; if no employee is assigned to a department, the employee name shows NULL.

RIGHT JOIN is just a LEFT JOIN with the tables swapped. Most teams standardise on LEFT JOIN for readability.

---

### FULL JOIN (FULL OUTER JOIN)

Combines the results of both LEFT JOIN and RIGHT JOIN. Returns **all records from both tables**, with matching rows where available and NULLs where there is no match.

- Returns all rows from both tables
- Displays NULL where there is no match
- Useful to find unmatched records **on both sides**

```sql
SELECT column_name
FROM table1
FULL OUTER JOIN table2
ON table1.column_name = table2.column_name;
```

To spot mismatches in both directions at once:
```sql
SELECT e.name, d.department_name
FROM employees e
FULL OUTER JOIN departments d ON e.department_id = d.department_id
WHERE e.id IS NULL OR d.department_id IS NULL;
```

Note: MySQL has no `FULL OUTER JOIN`. Emulate it with `LEFT JOIN UNION RIGHT JOIN`.

### INNER JOIN vs OUTER JOIN — the one-line summary
- **INNER JOIN** = intersection (matched data only)
- **OUTER JOIN** = union + NULLs (matched + unmatched data)

---

### Natural join
A **natural join** is an inner join that matches rows based on columns with the **same name** in the joined tables. The database determines the join columns automatically.

```sql
SELECT * FROM employees NATURAL JOIN departments;
```
Convenient, but fragile — if someone adds a same-named column later, your query silently changes meaning. Prefer explicit `ON`.

---

## 31. Self Join

A **self join** is a join where a table is joined **with itself** to compare rows within the same table. Use it when a table contains a hierarchical relationship, or when you need to compare rows in the same table.

- Joins a table with itself
- **Requires table aliases** to differentiate the two instances
- Used to compare rows within the same table

```sql
SELECT a.column, b.column
FROM table1 a
JOIN table1 b ON a.common_field = b.common_field;
```

**Example — employees and their managers**

| emp_id | name | manager_id |
|--------|------|------------|
| 1 | Alice | NULL |
| 2 | Bob | 1 |
| 3 | Carol | 1 |
| 4 | David | 2 |

Here `manager_id` refers to the `emp_id` of another employee.

```sql
SELECT e.name AS employee_name,
       m.name AS manager_name
FROM employees e
LEFT JOIN employees m
  ON e.manager_id = m.emp_id;
```
- `e` is an alias for employees acting **as the employee**
- `m` is another alias for the same table acting **as the manager**
- The join links an employee to their manager using `manager_id = emp_id`

Using `LEFT JOIN` keeps the CEO (whose `manager_id` is NULL) in the result with a NULL manager. An INNER JOIN would drop them.

**Example — employees who earn more than their manager**

| EmpID | Name | Salary | ManagerID |
|-------|------|--------|-----------|
| 101 | Vinay | 50000 | NULL |
| 102 | Nevendra | 40000 | 101 |
| 103 | Awadhesh | 60000 | 101 |
| 104 | Rituraj | 45000 | 102 |

```sql
SELECT e.Name   AS Employee,
       e.Salary AS EmployeeSalary,
       m.Name   AS Manager,
       m.Salary AS ManagerSalary
FROM Employees e
JOIN Employees m ON e.ManagerID = m.EmpID
WHERE e.Salary > m.Salary;
```

Output:

| Employee | EmployeeSalary | Manager | ManagerSalary |
|----------|----------------|---------|---------------|
| Awadhesh | 60000 | Vinay | 50000 |

**Other self-join patterns**
```sql
-- Pairs of employees in the same department (a.id < b.id avoids duplicate pairs & self-pairs)
SELECT e1.name AS employee1, e2.name AS employee2, e1.department_id
FROM employees e1
JOIN employees e2
  ON e1.department_id = e2.department_id
 AND e1.id < e2.id;

-- Employees who joined before their manager
SELECT e.name AS employee, m.name AS manager
FROM employees e
JOIN employees m ON e.manager_id = m.id
WHERE e.join_date < m.join_date;

-- The employee-manager pair with the largest salary gap
SELECT e.name AS employee, m.name AS manager, (m.salary - e.salary) AS salary_gap
FROM employees e
JOIN employees m ON e.manager_id = m.id
ORDER BY salary_gap DESC
LIMIT 1;

-- Products frequently bought together (market-basket analysis)
SELECT oi1.product_id AS product_a, oi2.product_id AS product_b, COUNT(*) AS times_together
FROM order_items oi1
JOIN order_items oi2
  ON oi1.order_id = oi2.order_id AND oi1.product_id < oi2.product_id
GROUP BY oi1.product_id, oi2.product_id
ORDER BY times_together DESC;

-- Overlapping room bookings (a range self-join)
SELECT b1.booking_id AS booking1, b2.booking_id AS booking2
FROM bookings b1
JOIN bookings b2
  ON b1.room_id = b2.room_id
 AND b1.booking_id < b2.booking_id
 AND b1.start_time < b2.end_time
 AND b2.start_time < b1.end_time;
```

The `a.id < b.id` trick appears everywhere in self joins. It does two jobs at once: it stops a row pairing with itself, and it returns each pair only once instead of twice (A–B *and* B–A).

---

## 32. Cross Join

**Cross Join returns the Cartesian product** of two tables — it combines every row from the first table with every row from the second. It requires no join condition.

- Combines all rows from both tables
- Rows in result = (Rows in Table 1) × (Rows in Table 2)
- Can produce enormous result sets

```sql
SELECT column_name
FROM table1
CROSS JOIN table2;
```

```sql
SELECT e.name, d.department_name
FROM employees e
CROSS JOIN departments d;
```
100 employees × 10 departments = 1,000 rows. Useful for generating test data, calendars, or every combination of two dimensions — dangerous by accident.

### Cross join vs inner join
A cross join returns the combination of **all** rows from two or more tables. An inner join returns **only the matching rows** based on a join condition.

> **The most common join bug:** forgetting the `ON` clause turns your join into a CROSS JOIN. If a query suddenly returns millions of rows, check for a missing `ON`.

---

### Join comparison summary

| Join Type | What it returns |
|-----------|-----------------|
| INNER JOIN | Rows with matches in both tables only |
| LEFT JOIN | All rows from left table + matching from right |
| RIGHT JOIN | All rows from right table + matching from left |
| FULL OUTER JOIN | All rows from both tables (matched or not) |
| SELF JOIN | Table joined with itself |
| CROSS JOIN | Cartesian product (every row of A with every row of B) |

### Common join mistakes and tips
- **Always specify the JOIN condition using `ON`.**
- **Missing `ON` leads to a CROSS JOIN** — a huge result.
- **Be careful with duplicate rows** (one-to-many joins multiply rows — "fan-out").
- **Use table aliases** to keep queries readable.
- **Difference between WHERE and ON in joins:**
  - `ON` filters rows **before** the join.
  - `WHERE` filters rows **after** the join.

### Real-world use cases
- Customers + Orders → get order details for customers
- Students + Departments → list students with their departments
- Employees + Salaries → see salary details with employee info
- Products + Categories → show products with category names

---

## 33. UNION, UNION ALL, INTERSECT, EXCEPT

These are **set operators**. They stack result sets **vertically** (more rows), whereas joins combine them **horizontally** (more columns).

For any set operator, the two SELECTs must have the **same number of columns** with **compatible data types**, in the same order.

| Operator | Description | Example |
|----------|-------------|---------|
| `UNION` | Combines results and **removes duplicates** | `SELECT id FROM A UNION SELECT id FROM B;` |
| `UNION ALL` | Combines results and **keeps duplicates** | `SELECT id FROM A UNION ALL SELECT id FROM B;` |
| `INTERSECT` | Returns only rows **common to both** queries | `SELECT id FROM A INTERSECT SELECT id FROM B;` |
| `EXCEPT` / `MINUS` | Returns rows in the **first query but not the second** | `SELECT id FROM A EXCEPT SELECT id FROM B;` (Oracle uses `MINUS`) |

**Visual example of UNION**

```
SELECT A        SELECT B          Result
   1               3                1
   2      UNION    4      ──►       2
   3               5                3
                                    4
                                    5
```
The duplicate `3` appears only once.

### UNION vs UNION ALL

| Criteria | UNION | UNION ALL |
|----------|-------|-----------|
| Duplicates | Removes duplicate rows | Includes all duplicate rows |
| Performance | Slower (due to duplicate removal / sorting) | Faster (no de-duplication) |
| Sorting | May sort the result set as a side effect of de-duplication | Does not sort |
| Usage | When duplicate data is not required | When duplicate data is meaningful or you know there are none |

```sql
SELECT city FROM customers
UNION
SELECT city FROM vendors;
-- → a unique list of cities

SELECT city FROM customers
UNION ALL
SELECT city FROM vendors;
-- → all cities, including duplicates
```

> **Performance habit:** if you *know* the two sets cannot overlap, always write `UNION ALL`. `UNION` pays for a sort/hash to remove duplicates that do not exist.

### UNION vs JOIN

| UNION | JOIN |
|-------|------|
| Combines result sets **vertically** (rows) from two or more tables | Combines result sets **horizontally** (columns) based on common columns |
| Removes duplicates by default (or keeps them with UNION ALL) | Does not remove duplicates |
| Tables must have the same number of columns and compatible data types | Tables can have different numbers of columns |
| Used when tables have **similar** data | Used when tables have **related** data through a common column |

### Practical uses

```sql
-- Fetch common records from two tables without a JOIN
SELECT column_name FROM table1
WHERE column_name IN (SELECT column_name FROM table2);
-- or
SELECT column_name FROM table1
INTERSECT
SELECT column_name FROM table2;

-- Unpivot: turn columns back into rows
SELECT product_id, 'Jan' AS month, jan_sales AS amount FROM sales_wide
UNION ALL
SELECT product_id, 'Feb', feb_sales FROM sales_wide
UNION ALL
SELECT product_id, 'Mar', mar_sales FROM sales_wide;

-- Label rows by source
SELECT name, 'Employee' AS type FROM Employee
UNION ALL
SELECT name, 'Manager'  AS type FROM Manager;

-- Reconcile two ledgers: report unmatched transactions on both sides
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

**Common mistakes with set operators**
- Mismatched column count or types in UNION/INTERSECT.
- Using `UNION` when duplicates are actually required.
- Placing `ORDER BY` inside a branch — it belongs at the **end**, applying to the whole result.

---

## 34. LATERAL joins and anti-joins

### LATERAL join
A `LATERAL` join lets a subquery on the right reference columns from the table on the left. It is the clean way to express "for each row in A, get its top N rows from B" — something a plain join cannot do.

```sql
-- Each customer's 3 most recent orders
SELECT c.customer_id, c.name, recent.*
FROM customers c
CROSS JOIN LATERAL (
  SELECT order_id, order_date, amount
  FROM orders o
  WHERE o.customer_id = c.customer_id
  ORDER BY order_date DESC
  LIMIT 3
) recent;

-- Each employee's most recent performance review
SELECT e.name, r.review_date, r.rating
FROM employees e
CROSS JOIN LATERAL (
  SELECT review_date, rating
  FROM performance_reviews pr
  WHERE pr.employee_id = e.id
  ORDER BY review_date DESC
  LIMIT 1
) r;

-- Best-selling product in each store (TOP-1 semantics)
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

-- Closest warehouse to each customer
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

SQL Server's equivalent is `CROSS APPLY` / `OUTER APPLY`. The **CROSS APPLY operator** invokes a table-valued function for each row of a table expression and returns the combined result set.

### Anti-joins with NOT EXISTS
```sql
-- Employees assigned to a project but missing from timesheets
SELECT pa.employee_id, pa.project_id
FROM project_assignments pa
WHERE NOT EXISTS (
  SELECT 1 FROM timesheets t
  WHERE t.employee_id = pa.employee_id AND t.project_id = pa.project_id
);

-- Products sold in store A but not store B (multi-column key)
SELECT p.product_id
FROM store_inventory p
WHERE p.store_id = 'A'
  AND NOT EXISTS (
    SELECT 1 FROM store_inventory q
    WHERE q.store_id = 'B' AND q.product_id = p.product_id
  );
```

### Multi-column joins
```sql
SELECT s.*
FROM shipments s
JOIN manifests m
  ON s.order_id     = m.order_id
 AND s.warehouse_id = m.warehouse_id
 AND s.ship_date    = m.ship_date;
```

### Relational division — "find rows matching ALL of something"
```sql
-- Customers who bought EVERY product in category 1
SELECT o.customer_id
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
WHERE p.category_id = 1
GROUP BY o.customer_id
HAVING COUNT(DISTINCT p.product_id) = (
  SELECT COUNT(*) FROM products WHERE category_id = 1
);

-- Products stocked in EVERY warehouse
SELECT product_id
FROM inventory
GROUP BY product_id
HAVING COUNT(DISTINCT warehouse_id) = (SELECT COUNT(*) FROM warehouses);

-- Customers with an order in EVERY month of the current year
SELECT customer_id
FROM orders
WHERE EXTRACT(YEAR FROM order_date) = EXTRACT(YEAR FROM CURRENT_DATE)
GROUP BY customer_id
HAVING COUNT(DISTINCT EXTRACT(MONTH FROM order_date)) = 12;
```
The pattern is always the same: **count the distinct matches per group, and compare it to the total count of things that exist.**

---

# PART 6 — QUERY BUILDING BLOCKS

## 35. Subqueries

**A subquery is a query nested inside another query.** It fetches data that the main query then uses as a condition, to filter or manipulate the result.

- Also called an **Inner Query** or **Nested Query**
- The inner query normally executes **first**, and its result is passed to the **outer query**
- Can be used with `SELECT`, `INSERT`, `UPDATE` or `DELETE`
- Can appear in `WHERE`, `HAVING`, `FROM` and `SELECT` clauses

**Syntax**
```sql
SELECT column_name
FROM table_name
WHERE column_name operator (SELECT column_name FROM table_name WHERE condition);
```

**Nesting diagram**
```
     Outer Query                          Inner (Sub) Query
  ┌────────────────┐   uses result of   ┌──────────────┐
  │ SELECT ...     │  ───────────────►  │ SELECT ...   │
  │ FROM ...       │  ◄───────────────  │ FROM ...     │
  │ WHERE (subq);  │   returns result   │ WHERE ...;   │
  └────────────────┘                    └──────────────┘
```

### The three types of subquery

| Type | Description | Example |
|------|-------------|---------|
| **Single-Row (Scalar)** | Returns exactly one row / one value | `SELECT name FROM Employee WHERE id = (SELECT MAX(id) FROM Employee);` |
| **Multi-Row** | Returns multiple rows (use with `IN`, `ANY`, `ALL`) | `SELECT name FROM Employee WHERE dept_id IN (SELECT id FROM Department);` |
| **Correlated** | Refers to columns from the outer query; executes for each row | `SELECT name FROM Employee e1 WHERE salary > (SELECT AVG(salary) FROM Employee e2 WHERE e2.dept_id = e1.dept_id);` |

**1. Single Row Subquery** — returns only one value.
```sql
SELECT * FROM Employees
WHERE Salary = (SELECT MAX(Salary) FROM Employees);
```
Selects the employee with the highest salary.

**2. Multiple Row Subquery** — returns multiple rows of data.
```sql
SELECT * FROM Employees
WHERE DepartmentID IN (SELECT DepartmentID FROM Departments WHERE Location = 'Bangalore');
```
Selects employees working in the Bangalore location.

**3. Correlated Subquery** — uses each row of the outer query to execute the subquery.
```sql
SELECT * FROM Employees e1
WHERE Salary > (SELECT AVG(Salary) FROM Employees e2 WHERE e2.DepartmentID = e1.DepartmentID);
```
Selects employees whose salary is higher than the average salary **of their own department**.

### Nested Query
A **nested query** is a query written inside another query to retrieve data based on the result of the inner query. It helps break down complex queries into smaller, more manageable parts.

```sql
-- Find employees who work in the 'Sales' department
SELECT * FROM Employees
WHERE department_id = (SELECT department_id FROM Departments WHERE name = 'Sales');
```
- The inner query finds the `department_id` for 'Sales'
- The outer query selects employees based on that `department_id`

### Subqueries in the FROM clause (derived tables)
```sql
SELECT department_id, AVG(total_hours) AS avg_hours_per_employee
FROM (
  SELECT e.department_id, t.employee_id, SUM(t.hours) AS total_hours
  FROM timesheets t
  JOIN employees e ON t.employee_id = e.id
  GROUP BY e.department_id, t.employee_id
) emp_project_hours
GROUP BY department_id;
```
A derived table must be given an alias.

---

## 36. Correlated Subqueries

**A correlated subquery depends on values from the outer query to execute.** It runs repeatedly, once for each row of the outer query, which makes it slower than a regular subquery.

- The inner query uses columns from the outer query
- Executes **row by row** for each result of the outer query
- **Cannot be executed independently** without the outer query
- Used for row-by-row comparisons

**Syntax**
```sql
SELECT column_name
FROM table1 t1
WHERE column_name operator (
    SELECT column_name FROM table2 t2 WHERE t2.column = t1.column
);
```

**Example — employees earning more than their department average**
```sql
SELECT * FROM Employees e1
WHERE Salary > (
    SELECT AVG(Salary) FROM Employees e2
    WHERE e2.DepartmentID = e1.DepartmentID
);
```
- The inner query calculates the average salary of each department
- The outer query checks whether the employee's salary exceeds their own department's average

**Products priced above the average price within their own category**
```sql
SELECT p1.*
FROM products p1
WHERE p1.price > (
  SELECT AVG(p2.price)
  FROM products p2
  WHERE p2.category_id = p1.category_id
);
```

### Correlated update
A **correlated update** is an UPDATE statement that refers to a column from the same table in a subquery. It updates values based on the result of the subquery for each row.

```sql
UPDATE orders o
SET status_id = s.status_id
FROM order_statuses s
WHERE o.status = s.status_name;
```

> Correlated subqueries are elegant but can be slow on large tables because they run once per outer row. In Part 10 you will see how to rewrite them as joins or window functions.

---

## 37. EXISTS vs IN

`EXISTS` checks whether a subquery returns **any rows**. It returns:
- **TRUE** if the subquery returns at least one row
- **FALSE** if the subquery returns no rows

```sql
SELECT column_name
FROM table_name
WHERE EXISTS (SELECT 1 FROM table2 WHERE condition);
```

| EXISTS | IN |
|--------|-----|
| Checks if a subquery returns any rows | Compares a value with a list of values returned by a subquery |
| Only works with subqueries | Works with static value lists **or** subqueries |
| Faster for large datasets | Slower with large datasets |
| **Stops checking after finding the first match** (short-circuits) | Builds and scans the whole list of values |
| Often better with large result sets | Good for smaller lists |

```sql
-- EXISTS
SELECT name FROM Employee e
WHERE EXISTS (SELECT 1 FROM Department d WHERE d.id = e.dept_id);

-- IN
SELECT name FROM Employee
WHERE dept_id IN (SELECT id FROM Department);
```

> **Rule of thumb: use EXISTS for an existence check, IN for a value comparison.**

### EXISTS vs NOT EXISTS
`EXISTS` returns true if a subquery returns any rows; `NOT EXISTS` returns true if a subquery returns no rows.

```sql
-- Employees who do not appear in project_assignments
SELECT *
FROM employees e
WHERE NOT EXISTS (
  SELECT 1 FROM project_assignments pa WHERE pa.employee_id = e.id
);

-- Departments where EVERY employee earns above 50000
-- ("no employee in this department earns 50000 or less")
SELECT DISTINCT department_id
FROM employees e1
WHERE NOT EXISTS (
  SELECT 1 FROM employees e2
  WHERE e2.department_id = e1.department_id AND e2.salary <= 50000
);
```
That second query is worth studying — **"all X satisfy Y" is expressed as "there does not exist an X that violates Y"**. It is one of the most useful logical tricks in SQL.

> **Important NULL trap:** `NOT IN` behaves unexpectedly when the subquery returns any NULL — the whole condition becomes unknown and you get **zero rows back**. `NOT EXISTS` does not have this problem. Prefer `NOT EXISTS`. (See §62.)

---

## 38. ANY and ALL

Both compare a value against the result of a subquery.

**ALL** — returns true if the comparison is true for **all** elements returned by the subquery.
```sql
SELECT * FROM Employee WHERE salary > ALL (SELECT salary FROM Employee WHERE dept = 'HR');
-- salary greater than EVERY HR salary → greater than the maximum
```

**ANY** (also written `SOME`) — returns true if the comparison is true for **at least one** element.
```sql
SELECT * FROM Employee WHERE salary > ANY (SELECT salary FROM Employee WHERE dept = 'HR');
-- salary greater than AT LEAST ONE HR salary → greater than the minimum
```

Mental shortcuts:
- `> ALL (...)` ≡ `> (SELECT MAX(...))`
- `> ANY (...)` ≡ `> (SELECT MIN(...))`
- `= ANY (...)` ≡ `IN (...)`

---

## 39. CTEs (Common Table Expressions) — full deep dive

### The intuition

Imagine you are organizing a birthday party.
- **Step 1:** You first make a guest list of everyone you want to invite.
- **Step 2:** Then you use that list to plan seating arrangements or food orders.

The guest list isn't a permanent document — it's just a temporary tool to help you plan efficiently.

**In SQL, a CTE is like that temporary guest list.** It helps you prepare data that you can use later in the same query.

### Formal definition

**A CTE (Common Table Expression) is a temporary, named result set — a shortcut — that you create and use within the same query.** It helps you organize and simplify SQL code, especially for complex queries.

### Syntax

```sql
WITH CTE_Name AS (
    -- Your query goes here
    SELECT column1, column2, ...
    FROM table_name
    WHERE condition
)
-- Main query referencing the CTE
SELECT *
FROM CTE_Name
WHERE another_condition;
```

- **WITH clause** — declares the start of the CTE.
- **CTE_Name** — a user-defined name for the CTE, used to reference it in subsequent queries.
- **Inner Query** — the query inside parentheses defines the temporary result set.
- **Main Query** — the outer query uses the CTE as if it were a table.

### Eight key points about CTEs

1. **Temporary Scope** — a CTE exists only during the execution of the query in which it is defined.
2. **Defined with WITH Clause** — starts with the keyword `WITH`, followed by a name and a query in parentheses.
3. **Reusable Within Query** — you can reference the CTE multiple times in the same query.
4. **Supports Recursion** — recursive CTEs traverse hierarchical data (org charts, file directories).
5. **Cannot Be Indexed** — CTEs are not stored on disk or indexed; they execute on the fly.
6. **Simplifies Joins and Aggregations** — makes handling joins, aggregations and derived data much cleaner.
7. **No Materialization** — unlike views or temporary tables, CTEs do not persist or store intermediate results; they are virtual and exist only during query execution.
8. **Can Use Multiple CTEs** — you can define and chain multiple CTEs in a single query.

Benefits: reusable and readable · allows recursion · avoids repeating subqueries.

### Worked example — a better alternative to subqueries

Input table `Employees`:

| EmployeeID | FirstName | LastName | DepartmentID | Salary |
|------------|-----------|----------|--------------|--------|
| 1 | Alice | Johnson | 101 | 70000 |
| 2 | Bob | Smith | 101 | 80000 |
| 3 | Charlie | Brown | 102 | 90000 |
| 4 | Diana | Lee | 102 | 75000 |
| 5 | Edward | Wilson | 103 | 60000 |
| 6 | Fiona | Carter | 103 | 65000 |

Goal: analyze employees who have a salary above their department's average salary.

```sql
WITH DepartmentAverage AS (
    SELECT DepartmentID, AVG(Salary) AS AvgSalary
    FROM Employees
    GROUP BY DepartmentID
)
SELECT e.EmployeeID, e.FirstName, e.LastName,
       e.DepartmentID, e.Salary, d.AvgSalary
FROM Employees e
INNER JOIN DepartmentAverage d
    ON e.DepartmentID = d.DepartmentID
WHERE e.Salary > d.AvgSalary;
```

**Breakdown**

1. The `DepartmentAverage` CTE computes the average salary for each department:

| DepartmentID | AvgSalary |
|--------------|-----------|
| 101 | 75000 |
| 102 | 82500 |
| 103 | 62500 |

2. The main query joins `Employees` with the CTE and filters employees earning more than their department's average.

Result:

| EmployeeID | FirstName | LastName | DepartmentID | Salary | AvgSalary |
|------------|-----------|----------|--------------|--------|-----------|
| 2 | Bob | Smith | 101 | 80000 | 75000 |
| 3 | Charlie | Brown | 102 | 90000 | 82500 |

- Bob (Dept 101) earns 80,000 — above the 75,000 average for his department.
- Charlie (Dept 102) earns 90,000 — above the 82,500 average for his department.

---

### TYPES OF CTEs

- **Recursive CTE** — for hierarchical or iterative data.
- **Non-Recursive CTE** — simplifies complex queries.
- **Inline CTE** — acts as an inline view for modular query design.
- **Multiple CTEs** — multiple result sets in a single query.
- **Materialized CTE** — performance optimization (PostgreSQL 12+, Snowflake, SQL Server 2022+).

---

### 02. Non-Recursive CTE

A **Non-Recursive CTE** is a query that does not reference itself. It is simply a temporary result set used to simplify complex queries, enhance readability, and avoid writing subqueries repeatedly.

How it works:
1. It is defined with a `WITH` clause.
2. The CTE contains a single query that is executed once.
3. The result is stored temporarily and can be referred to later in the main query.

```sql
WITH CTE_Name AS (
    SELECT <columns>
    FROM <table_name>
    WHERE <conditions>
)
SELECT <columns>
FROM CTE_Name;
```

**Example** — table `Sales`:

| SaleID | SaleAmount | SaleDate |
|--------|------------|----------|
| 1 | 100 | 2024-01-01 |
| 2 | 200 | 2024-02-01 |
| 3 | 150 | 2024-03-01 |
| 4 | 250 | 2024-01-15 |
| 5 | 300 | 2024-03-10 |
| 6 | 200 | 2023-03-10 |
| 7 | 100 | 2023-02-10 |
| 8 | 350 | 2023-01-10 |

```sql
WITH TotalSales AS (
    SELECT SUM(SaleAmount) AS TotalAmount
    FROM Sales
    WHERE YEAR(SaleDate) = 2024
)
SELECT *
FROM TotalSales
WHERE TotalAmount > 500;
```

- The CTE `TotalSales` calculates total sales for 2024.
- The main query filters to totals greater than 500.

Output:

| TotalAmount |
|-------------|
| 1000 |

---

### 03. Inline CTE

**Inline CTEs** define a temporary result set directly within a SQL query for immediate use. They are "inline" because they are defined and used within the scope of a single query, giving concise, readable SQL without creating a permanent table or repeating subquery logic.

Key characteristics:
- **Temporary Scope** — exist only within the scope of the query they are part of.
- **Defined and Used in a Single Query** — the `WITH` clause is defined once and used immediately.
- **Improved Readability** — eliminates nested subqueries.
- **No Stored Results** — computed on the fly during execution.

**Example** — table `Sales`:

| SaleID | CustomerID | SaleAmount | SaleDate |
|--------|------------|------------|----------|
| 1 | 101 | 500 | 2023-12-01 |
| 2 | 102 | 300 | 2023-12-05 |
| 3 | 103 | 700 | 2023-12-07 |
| 4 | 101 | 200 | 2023-12-10 |
| 5 | 102 | 400 | 2023-12-12 |

Calculate total sales per customer, then keep customers whose total is 600 or more:

```sql
WITH CustomerSales AS (
    SELECT CustomerID, SUM(SaleAmount) AS TotalSales
    FROM Sales
    GROUP BY CustomerID
)
SELECT CustomerID, TotalSales
FROM CustomerSales
WHERE TotalSales >= 600;
```

Result:

| CustomerID | TotalSales |
|------------|------------|
| 101 | 700 |
| 103 | 700 |

**Inline CTE vs Non-Recursive CTE**

| Aspect | Inline CTE | Non-Recursive CTE |
|--------|-----------|-------------------|
| Definition | A single-use query for simplification | Used for multi-step data processing |
| Complexity | Generally simple and straightforward | Can involve multiple layers of processing |
| Use Case | Replace subqueries, simplify SQL | Structure multi-step calculations |
| Recursion | Not recursive | Not recursive, but involves layered logic |
| Output | Produces a simplified query result | Can generate intermediate and final results |

---

### 04. Multiple CTEs

**Multiple CTEs** are when you define and use more than one CTE in a single query. They are useful for breaking complex queries into smaller, manageable pieces, and for reusing intermediate results.

Key features:
- **Sequential Definitions** — CTEs are defined one after another, separated by **commas** (`WITH` appears only once).
- **Dependent or Independent** — later CTEs can reference earlier ones, or operate independently.
- **Enhanced Readability** — makes complex queries modular.
- **Single Query Scope** — all CTEs exist within the context of one SQL query.

```sql
WITH CTE1 AS (
    SELECT <columns>
    FROM <table_name>
    WHERE <conditions>
),
CTE2 AS (
    SELECT <columns>
    FROM CTE1
    WHERE <conditions>
),
CTE3 AS (
    SELECT <columns>
    FROM <table_name>
    WHERE <conditions>
)
SELECT <columns>
FROM CTE2
JOIN CTE3 ON <condition>;
```

**Example** — table `Orders`:

| OrderID | CustomerID | OrderDate | OrderAmount |
|---------|------------|-----------|-------------|
| 1 | 101 | 2023-01-01 | 500 |
| 2 | 102 | 2023-01-02 | 300 |
| 3 | 103 | 2023-01-03 | 700 |
| 4 | 101 | 2023-01-04 | 200 |
| 5 | 102 | 2023-01-05 | 400 |

Calculate (1) total order amount per customer, then (2) customers with totals above 600:

```sql
WITH CTE1 AS (
    SELECT CustomerID, SUM(OrderAmount) AS TotalOrderAmount
    FROM Orders
    GROUP BY CustomerID
),
CTE2 AS (
    SELECT CustomerID, TotalOrderAmount
    FROM CTE1
    WHERE TotalOrderAmount > 600
)
SELECT CustomerID, TotalOrderAmount
FROM CTE2;
```

Result:

| CustomerID | TotalOrderAmount |
|------------|------------------|
| 101 | 700 |
| 103 | 700 |

---

### 05. Materialized CTE

**Materialized CTEs** are a concept in some database systems (Snowflake, PostgreSQL 12+) that improve query performance. When a CTE is materialized, its results are computed **once** and stored temporarily (like a temp table) for reuse in later parts of the query. This avoids recomputing the CTE when it is referenced multiple times.

Key characteristics:
- **Reusability** — the result is cached, so it is not recalculated every time it's used.
- **Performance Boost** — significant in complex queries where the same CTE is referenced multiple times.
- **Explicit Materialization** — some databases let you request it; others decide automatically.

**Syntax in PostgreSQL** — `MATERIALIZED` forces materialization; `NOT MATERIALIZED` forces inlining (recalculated each time).
```sql
WITH [MATERIALIZED | NOT MATERIALIZED] CTE_Name AS (
    SELECT <columns>
    FROM <table>
    WHERE <conditions>
)
SELECT * FROM CTE_Name;
```

**Example** — table `Sales`:

| SaleID | ProductID | Quantity | Price |
|--------|-----------|----------|-------|
| 1 | 101 | 10 | 20 |
| 2 | 102 | 15 | 30 |
| 3 | 101 | 20 | 20 |
| 4 | 103 | 10 | 50 |

```sql
WITH MATERIALIZED RevenueCTE AS (
    SELECT ProductID, SUM(Quantity * Price) AS TotalRevenue
    FROM Sales
    GROUP BY ProductID
)
SELECT *
FROM RevenueCTE
WHERE TotalRevenue > 500;
```

Output:

| ProductID | TotalRevenue |
|-----------|--------------|
| 101 | 600 |
| 103 | 500 |

**Simple CTE vs Materialized CTE**

| Aspect | Simple CTE | Materialized CTE |
|--------|-----------|------------------|
| Evaluation | Recomputed every time it is referenced | Computed once and stored temporarily |
| Performance | May be slower for repeated usage | Faster when reused multiple times |
| Storage | Not stored; purely inline execution | Stored temporarily in memory or disk |
| Syntax | Standard `WITH` clause | `WITH MATERIALIZED` or engine-specific equivalent |
| Support | Supported by most SQL engines | Limited support (PostgreSQL, Snowflake) |

Practical use — avoid recomputing an expensive aggregation referenced twice:
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

---

## 40. Recursive CTEs

**A Recursive CTE is a query that refers to itself** to perform repetitive operations until a specific condition is met. It is used for hierarchical data or iterative tasks:
- Tree traversals
- Generating sequential data
- Processing hierarchical relationships

### How a Recursive CTE works

A recursive CTE consists of two parts:

- **Base case** — the initial query that forms the starting point of the recursion. This query is executed **once**.
- **Recursive case** — the query that references the CTE itself, repeatedly calling the CTE to fetch results until a termination condition is met.

**The termination condition ensures the recursion stops. If it is not defined, it can lead to an infinite loop.**

```sql
WITH RECURSIVE CTEName AS (
    -- Base case: first query
    SELECT <columns>
    FROM <table_name>
    WHERE <conditions>

    UNION ALL

    -- Recursive case: query that references the CTE itself
    SELECT <columns>
    FROM <table_name>
    INNER JOIN CTEName ON <conditions>
)
SELECT * FROM CTEName;
```

(In MySQL and PostgreSQL you write `WITH RECURSIVE`; in SQL Server just `WITH`.)

### Worked example — Employee Hierarchy (Manager–Subordinate)

Table `Employees`:

| EmployeeID | EmployeeName | ManagerID |
|------------|--------------|-----------|
| 1 | John | NULL |
| 2 | Alice | 1 |
| 3 | Bob | 1 |
| 4 | Charlie | 2 |
| 5 | David | 3 |
| 6 | Eve | 3 |

We want to list employees in hierarchical order, starting from the CEO (who has no manager) and traversing down to all subordinates.

1. **Base condition:** start with the CEO (`ManagerID IS NULL`).
2. **Recursive step:** find employees who report to the employees in the previous level.
3. **Termination condition:** automatically stops when no employees are left to process.

```sql
WITH RECURSIVE EmployeeHierarchy AS (
    -- Base case: select top-level managers (those with no manager)
    SELECT EmployeeID, EmployeeName, ManagerID, 0 AS Level
    FROM Employees
    WHERE ManagerID IS NULL

    UNION ALL

    -- Recursive case: select employees under managers
    SELECT e.EmployeeID, e.EmployeeName, e.ManagerID, eh.Level + 1 AS Level
    FROM Employees e
    INNER JOIN EmployeeHierarchy eh ON e.ManagerID = eh.EmployeeID
)
SELECT * FROM EmployeeHierarchy
ORDER BY Level, EmployeeID;
```

Result:

| EmployeeID | EmployeeName | ManagerID | Level |
|------------|--------------|-----------|-------|
| 1 | John | NULL | 0 |
| 2 | Alice | 1 | 1 |
| 3 | Bob | 1 | 1 |
| 4 | Charlie | 2 | 2 |
| 5 | David | 3 | 2 |
| 6 | Eve | 3 | 2 |

**Explanation**

1. **Base Case** — starts with the CEO (`ManagerID IS NULL`), including their ID, name, ManagerID, and sets `Level = 0`.
2. **Recursive Step** — for each employee at the current level, finds their subordinates by matching `EmployeeID` with `ManagerID` in the Employees table, and increments the level by 1.
3. **Termination** — stops automatically when no more employees are found for the next level.

```
Level 0: John (CEO)
    Level 1: Alice, Bob
        Level 2: Charlie, David, Eve
```

### The full recursive toolkit

```sql
-- Generate a series of dates between two dates
WITH RECURSIVE date_series AS (
  SELECT DATE '2024-01-01' AS d
  UNION ALL
  SELECT d + 1 FROM date_series WHERE d + 1 <= DATE '2024-01-31'
)
SELECT d FROM date_series;

-- Generate the numbers 1..100 without a numbers table
WITH RECURSIVE seq AS (
  SELECT 1 AS n
  UNION ALL
  SELECT n + 1 FROM seq WHERE n < 100
)
SELECT n FROM seq;

-- Fibonacci-style forecast sequence
WITH RECURSIVE fib AS (
  SELECT 1 AS a, 1 AS b, 1 AS step
  UNION ALL
  SELECT b, a + b, step + 1 FROM fib WHERE step < 20
)
SELECT step, a AS fib_value FROM fib;

-- Build a materialized path string for each node in an org chart
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

-- All subordinates (direct and indirect) of manager 101
WITH RECURSIVE subordinates AS (
  SELECT id, name, manager_id FROM employees WHERE manager_id = 101
  UNION ALL
  SELECT e.id, e.name, e.manager_id
  FROM employees e
  JOIN subordinates s ON e.manager_id = s.id
)
SELECT * FROM subordinates;

-- Total direct + indirect reports for each manager
WITH RECURSIVE reports AS (
  SELECT id, manager_id FROM employees WHERE manager_id IS NOT NULL
  UNION ALL
  SELECT e.id, r.manager_id
  FROM employees e
  JOIN reports r ON e.manager_id = r.id
)
SELECT manager_id, COUNT(*) AS total_reports FROM reports GROUP BY manager_id;

-- Maximum depth of the org hierarchy
WITH RECURSIVE depth AS (
  SELECT id, manager_id, 1 AS lvl FROM employees WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.manager_id, d.lvl + 1
  FROM employees e JOIN depth d ON e.manager_id = d.id
)
SELECT MAX(lvl) AS max_depth FROM depth;

-- How many employees sit at each level
WITH RECURSIVE levels AS (
  SELECT id, manager_id, 0 AS lvl FROM employees WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.manager_id, l.lvl + 1
  FROM employees e JOIN levels l ON e.manager_id = l.id
)
SELECT lvl, COUNT(*) AS employees_at_level FROM levels GROUP BY lvl ORDER BY lvl;

-- Nested categories tree
WITH RECURSIVE cat_tree AS (
  SELECT category_id, category_name, parent_category_id, 1 AS depth
  FROM categories WHERE parent_category_id IS NULL
  UNION ALL
  SELECT c.category_id, c.category_name, c.parent_category_id, ct.depth + 1
  FROM categories c JOIN cat_tree ct ON c.parent_category_id = ct.category_id
)
SELECT * FROM cat_tree ORDER BY depth, category_name;

-- Walk UPWARD: all ancestor categories of a leaf category
WITH RECURSIVE ancestors AS (
  SELECT category_id, parent_category_id FROM categories WHERE category_id = 42
  UNION ALL
  SELECT c.category_id, c.parent_category_id
  FROM categories c JOIN ancestors a ON c.category_id = a.parent_category_id
)
SELECT * FROM ancestors;

-- Bill of materials: all sub-components of a product
WITH RECURSIVE bom AS (
  SELECT parent_product_id, component_id, quantity, 1 AS level
  FROM product_components WHERE parent_product_id = 500
  UNION ALL
  SELECT pc.parent_product_id, pc.component_id, pc.quantity, b.level + 1
  FROM product_components pc JOIN bom b ON pc.parent_product_id = b.component_id
)
SELECT * FROM bom ORDER BY level;

-- Roll up a budget through a department tree
WITH RECURSIVE dept_tree AS (
  SELECT department_id, parent_department_id, budget
  FROM departments WHERE department_id = 10
  UNION ALL
  SELECT d.department_id, d.parent_department_id, d.budget
  FROM departments d JOIN dept_tree t ON d.parent_department_id = t.department_id
)
SELECT SUM(budget) AS total_budget FROM dept_tree;

-- Friend-of-friend social graph, up to 2 hops
WITH RECURSIVE network AS (
  SELECT user_id, friend_id, 1 AS hops FROM friendships WHERE user_id = 1
  UNION ALL
  SELECT n.user_id, f.friend_id, n.hops + 1
  FROM friendships f JOIN network n ON f.user_id = n.friend_id
  WHERE n.hops < 2
)
SELECT DISTINCT friend_id FROM network;

-- Flatten threaded comments into conversation order
WITH RECURSIVE thread AS (
  SELECT comment_id, parent_comment_id, comment_text, 1 AS depth,
         LPAD(comment_id::TEXT, 5, '0') AS sort_path
  FROM comments WHERE parent_comment_id IS NULL
  UNION ALL
  SELECT c.comment_id, c.parent_comment_id, c.comment_text, t.depth + 1,
         t.sort_path || '.' || LPAD(c.comment_id::TEXT, 5, '0')
  FROM comments c JOIN thread t ON c.parent_comment_id = t.comment_id
)
SELECT * FROM thread ORDER BY sort_path;

-- Cycle detection: guard against infinite loops using a visited array
WITH RECURSIVE chain AS (
  SELECT id, manager_id, ARRAY[id] AS visited, FALSE AS is_cycle
  FROM employees
  UNION ALL
  SELECT e.id, c.manager_id, c.visited || e.id, e.id = ANY(c.visited)
  FROM employees e JOIN chain c ON e.manager_id = c.id
  WHERE NOT c.is_cycle
)
SELECT DISTINCT id FROM chain WHERE is_cycle;
```

> **Safety rule:** every recursive CTE needs a stopping condition — a depth limit, a bound in the WHERE clause, or a visited-list guard. Bad hierarchy data (an employee who is their own manager, directly or indirectly) will otherwise loop forever.

---

## 41. Temporary Tables and Table Variables

### Temporary Table
A **temporary table** stores temporary data for the duration of a session or transaction.

- Automatically deleted when the session (or transaction) ends
- Used to store intermediate results
- Prefixed with `#` in SQL Server; `TEMPORARY` keyword in MySQL/PostgreSQL
- Can be explicitly dropped

```sql
-- MySQL / PostgreSQL
CREATE TEMPORARY TABLE temp_employees AS
SELECT * FROM Employees WHERE Salary > 50000;

-- SQL Server
CREATE TABLE #TempEmployees (
    EmpID INT,
    Name  VARCHAR(50)
);
```

The table holds filtered data temporarily and is automatically deleted after the session ends.

### Temporary Table vs CTE

| Temporary Table | CTE (Common Table Expression) |
|-----------------|-------------------------------|
| Stores data physically in temporary memory/disk | Stores data logically, without physical storage |
| Needs to be explicitly created and dropped | Automatically disappears after query execution |
| Can be used **multiple times** within a session | Can be used only within the **same query** |
| Supports **indexing** and DDL operations | Does **not** support indexing or DDL operations |
| Slower for small datasets | Faster for small datasets |

**Use a Temporary Table** when data needs to be reused multiple times across statements.
**Use a CTE** for short-term data manipulation and improved readability within one query.

### Temporary table vs table variable
A **temporary table** is created and exists only for the duration of a session or transaction. It can be explicitly dropped, or is automatically dropped when the session/transaction ends.

A **table variable** stores a table-like structure **in memory**. It has a limited scope within a batch, stored procedure or function, and is automatically deallocated when the scope ends.

---

# PART 7 — ANALYTICS

## 42. Window Functions

**A window function performs calculations across a set of table rows related to the current row — without collapsing the rows** the way `GROUP BY` does.

- Works with the `OVER()` clause
- Does **not** group rows like aggregate functions
- Commonly used for ranking, running totals and moving averages

**Syntax**
```sql
FUNCTION_NAME() OVER (
    PARTITION BY column     -- optional: split rows into groups
    ORDER BY column         -- optional: order within each group
    ROWS BETWEEN ... AND ...-- optional: the frame
)
```

- **PARTITION BY** — divides rows into groups; the function restarts for each group. (Like GROUP BY, but rows are kept.)
- **ORDER BY** — orders rows within each partition. Required for ranking and for running totals.
- **Frame** (`ROWS`/`RANGE BETWEEN`) — narrows which rows around the current one are included.

### GROUP BY vs WINDOW FUNCTIONS — the key distinction

| GROUP BY | WINDOW FUNCTIONS |
|----------|------------------|
| **Collapses** rows into groups | **Keeps** all rows |
| Returns **one row per group** | Returns one row per input row |
| Used for aggregation | Performs a calculation across related rows |
| Example: total salary per dept | Example: rank each employee, running totals, percentiles |

### Partition illustration

```
Employee Table          Partition By Dept              Apply the window
                     ┌──────────────────┐              function within
   ▢▢▢▢▢▢     →      │ Dept = IT  ▢▢▢▢  │      →       each partition
                     │ Dept = HR  ▢▢▢▢  │              separately
                     └──────────────────┘
```

Compare a value to its group without losing the row:
```sql
-- Each employee's salary vs their department's average
SELECT name, department_id, salary,
       salary - AVG(salary) OVER (PARTITION BY department_id) AS diff_from_avg
FROM employees;

-- Each employee's salary vs the whole company's average
SELECT name, salary,
       salary - AVG(salary) OVER () AS variance_from_company_avg
FROM employees;
```
An empty `OVER ()` means "the whole result set is one window".

---

## 43. ROW_NUMBER vs RANK vs DENSE_RANK

These three ranking functions assign numbers to rows based on an order. The difference is **how they handle ties** — and this is asked in almost every SQL interview.

| Function | Purpose | Duplicates get same value? | Skips numbers? | Example output |
|----------|---------|---------------------------|----------------|----------------|
| `ROW_NUMBER()` | Assigns a unique sequential number to each row | **No** — always unique | No | 1, 2, 3, 4 |
| `RANK()` | Assigns the same rank to ties, then **skips** | Yes | **Yes** | 1, 2, 2, 4 |
| `DENSE_RANK()` | Assigns the same rank to ties, **no gaps** | Yes | No | 1, 2, 2, 3 |

**Worked example — dept-wise salary ranking**

| ID | Name | Dept | Salary | ROW_NUMBER() | RANK() | DENSE_RANK() |
|----|------|------|--------|--------------|--------|--------------|
| 1 | Abhi | IT | 70000 | 1 | 1 | 1 |
| 2 | Ravi | IT | 70000 | 2 | 1 | 1 |
| 3 | Sita | IT | 60000 | 3 | 3 | 2 |
| 4 | Neha | HR | 55000 | 1 | 1 | 1 |
| 5 | John | HR | 45000 | 2 | 2 | 2 |
| 6 | Pooja | HR | 45000 | 3 | 2 | 2 |

- `ROW_NUMBER()` → always a unique sequence
- `RANK()` → gaps after ties
- `DENSE_RANK()` → no gaps

```sql
SELECT name, dept, salary,
       ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS rn,
       RANK()       OVER (PARTITION BY dept ORDER BY salary DESC) AS rnk,
       DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS dense_rnk
FROM Employee;
```

### RANK() vs DENSE_RANK() — the interview table

| RANK() | DENSE_RANK() |
|--------|--------------|
| Assigns a unique rank to each row, but **skips the next rank** when there are duplicates | Assigns a rank **without skipping** numbers for duplicates |
| Gaps are created in the ranking sequence | No gaps in the ranking sequence |
| Slower than DENSE_RANK() | Faster than RANK() because it doesn't skip |
| Use for competition rank | Use for class rank |

### Which one to use

- Need **exactly one row per group** (deduplication, "latest record per customer")? → **ROW_NUMBER()**
- Need "top 3 salaries" where ties should all be included? → **DENSE_RANK()** (or RANK, depending on whether you want gaps)
- Reporting a competition placement? → **RANK()**

### The Top-N-per-group pattern

This is the single most-used window function pattern. Rank inside a subquery, filter outside:

```sql
-- Top 3 highest paid employees in each department
SELECT *
FROM (
  SELECT e.*,
         ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rnk
  FROM employees e
) ranked
WHERE rnk <= 3;
```

You **cannot** filter on a window function in `WHERE` — remember the execution order (§24): `WHERE` runs before `SELECT`, where the window function lives. So you wrap it in a subquery or CTE. (Some databases — Snowflake, BigQuery, DuckDB — offer a `QUALIFY` clause that does this filtering for you.)

More Top-N variants:
```sql
-- Nth highest salary overall
SELECT salary
FROM (SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk FROM employees) r
WHERE rnk = 3
LIMIT 1;

-- Second highest salary PER DEPARTMENT
SELECT department_id, salary
FROM (
  SELECT department_id, salary,
         DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rnk
  FROM employees
) ranked
WHERE rnk = 2;

-- Top earner per job title
SELECT *
FROM (SELECT *, RANK() OVER (PARTITION BY job_title ORDER BY salary DESC) AS rnk
      FROM employees) ranked
WHERE rnk = 1;

-- 3 most recently registered customers in each country
SELECT *
FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY country ORDER BY signup_date DESC) AS rnk
      FROM customers) ranked
WHERE rnk <= 3;

-- Second most expensive product in each category
SELECT category_id, product_name, price
FROM (
  SELECT category_id, product_name, price,
         DENSE_RANK() OVER (PARTITION BY category_id ORDER BY price DESC) AS rnk
  FROM products
) ranked
WHERE rnk = 2;

-- Top 2 per department, ties broken by earliest join date, with dept average alongside
SELECT *
FROM (
  SELECT e.*, d.avg_salary,
         ROW_NUMBER() OVER (
           PARTITION BY e.department_id
           ORDER BY e.salary DESC, e.join_date ASC
         ) AS rnk
  FROM employees e
  JOIN (SELECT department_id, AVG(salary) AS avg_salary
        FROM employees GROUP BY department_id) d
    ON e.department_id = d.department_id
) ranked
WHERE rnk <= 2;
```

### Deduplication with ROW_NUMBER

```sql
-- Keep only the most recent record per email, delete the rest
DELETE FROM customers
WHERE customer_id NOT IN (
  SELECT customer_id FROM (
    SELECT customer_id,
           ROW_NUMBER() OVER (PARTITION BY email ORDER BY updated_at DESC) AS rn
    FROM customers
  ) t
  WHERE rn = 1
);

-- First purchase made by each customer
SELECT *
FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rn
      FROM orders) t
WHERE rn = 1;
```

---

## 44. Running totals, moving averages, LEAD/LAG

### The frame clause

```
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW    -- everything up to here (running total)
ROWS BETWEEN 2 PRECEDING AND CURRENT ROW            -- 3-row trailing window
ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING            -- 5-row centered window
ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING  -- the whole partition
ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING    -- everything before, excluding current
RANGE BETWEEN INTERVAL '29 days' PRECEDING AND CURRENT ROW  -- value-based, not row-based
```

When you write `ORDER BY` without a frame, the default is `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` — which is why a plain `SUM(...) OVER (ORDER BY d)` already gives a running total.

### Running totals

```sql
-- Running total of sales by date
SELECT sale_date, amount,
       SUM(amount) OVER (ORDER BY sale_date) AS running_total
FROM sales;

-- Running total per department (worked example)
SELECT name, dept, salary,
       SUM(salary) OVER (PARTITION BY dept ORDER BY salary DESC) AS running_total
FROM Employee;
```

| Name | Dept | Salary | Running Total |
|------|------|--------|---------------|
| Abhi | IT | 70000 | 70000 |
| Ravi | IT | 70000 | 140000 |
| Sita | IT | 60000 | 200000 |
| Neha | HR | 55000 | 55000 |
| John | HR | 45000 | 100000 |
| Pooja | HR | 45000 | 145000 |

Notice the total **resets** at each new department — that is what `PARTITION BY` does.

```sql
-- Cumulative sum of sales per product, in chronological order
SELECT order_date, product_id, sales_amount,
       SUM(sales_amount) OVER (PARTITION BY product_id ORDER BY order_date) AS cumulative_sales
FROM sales;

-- Running total that resets at the start of every month
SELECT expense_date, amount,
       SUM(amount) OVER (
         PARTITION BY DATE_TRUNC('month', expense_date)
         ORDER BY expense_date
       ) AS monthly_running_total
FROM expenses;

-- Running total of revenue per product that resets each year
SELECT product_id, sale_date, amount,
       SUM(amount) OVER (
         PARTITION BY product_id, EXTRACT(YEAR FROM sale_date)
         ORDER BY sale_date
       ) AS yearly_running_total
FROM product_sales;

-- Running count of orders per customer (an order sequence number)
SELECT customer_id, order_date,
       COUNT(*) OVER (PARTITION BY customer_id ORDER BY order_date) AS order_sequence
FROM orders;

-- Cumulative new customers per month
SELECT signup_month, new_customers,
       SUM(new_customers) OVER (ORDER BY signup_month) AS cumulative_customers
FROM (
  SELECT DATE_TRUNC('month', signup_date) AS signup_month, COUNT(*) AS new_customers
  FROM customers GROUP BY DATE_TRUNC('month', signup_date)
) t;

-- Running maximum / "highest so far"
SELECT trade_date, price, MAX(price) OVER (ORDER BY trade_date) AS running_max
FROM stock_prices;

SELECT employee_id, raise_date, salary,
       MAX(salary) OVER (PARTITION BY employee_id ORDER BY raise_date) AS highest_so_far
FROM salary_history;
```

### Moving averages

```sql
-- 3-order moving average per customer
SELECT customer_id, order_date, amount,
       AVG(amount) OVER (
         PARTITION BY customer_id
         ORDER BY order_date
         ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
       ) AS moving_avg
FROM orders;

-- 7-day rolling average of website visits
SELECT visit_date, visits,
       AVG(visits) OVER (ORDER BY visit_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)
       AS rolling_7day_avg
FROM daily_visits;

-- Centered 5-day moving average (2 back, 2 forward)
SELECT sale_date, amount,
       AVG(amount) OVER (ORDER BY sale_date ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING)
       AS centered_avg
FROM sales;

-- 30-day trailing sum using a RANGE (date-based) frame
SELECT sale_date, amount,
       SUM(amount) OVER (
         ORDER BY sale_date
         RANGE BETWEEN INTERVAL '29 days' PRECEDING AND CURRENT ROW
       ) AS trailing_30day_sum
FROM daily_revenue;

-- Weighted moving average (quantity as the weight)
SELECT sale_date,
       SUM(amount * quantity) OVER (ORDER BY sale_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)
       / NULLIF(SUM(quantity) OVER (ORDER BY sale_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 0)
       AS weighted_moving_avg
FROM sales;

-- Running average that EXCLUDES the current row
SELECT customer_id, order_date, amount,
       AVG(amount) OVER (
         PARTITION BY customer_id ORDER BY order_date
         ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
       ) AS avg_excluding_current
FROM orders;
```

### LEAD and LAG — comparing a row to its neighbours

| Function | Purpose |
|----------|---------|
| `LAG(col, n, default)` | Accesses data from the n-th **preceding** row (the previous row's value) |
| `LEAD(col, n, default)` | Accesses data from the n-th **following** row (the next row's value) |

```sql
SELECT name, salary,
       LAG(salary)  OVER (ORDER BY salary) AS prev_salary,
       LEAD(salary) OVER (ORDER BY salary) AS next_salary
FROM employees;
```

**Period-over-period comparison** is the whole reason LAG exists:

```sql
-- Difference between each order and the previous order for the same customer
SELECT customer_id, order_date, amount,
       amount - LAG(amount) OVER (PARTITION BY customer_id ORDER BY order_date) AS diff
FROM orders;

-- Year-over-year revenue growth
SELECT year, revenue,
       revenue - LAG(revenue) OVER (ORDER BY year) AS yoy_growth
FROM annual_revenue;

-- Percentage change in monthly sales
SELECT month, total_sales,
       ROUND(100.0 * (total_sales - LAG(total_sales) OVER (ORDER BY month))
             / LAG(total_sales) OVER (ORDER BY month), 2) AS pct_change
FROM monthly_sales;

-- Gap in days between consecutive orders
SELECT customer_id, order_date,
       order_date - LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS days_gap
FROM orders;

-- Average time between orders per customer
SELECT customer_id, AVG(gap_days) AS avg_gap
FROM (
  SELECT customer_id,
         order_date - LAG(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS gap_days
  FROM orders
) t
GROUP BY customer_id;

-- 2-period lag of stock prices
SELECT symbol, trade_date, price,
       LAG(price, 2) OVER (PARTITION BY symbol ORDER BY trade_date) AS price_2_days_ago
FROM stock_prices;

-- Week-over-week: compare to 7 rows back
SELECT sale_date, total,
       LAG(total, 7) OVER (ORDER BY sale_date) AS total_last_week
FROM daily_totals;

-- Products whose sales dropped two consecutive months
SELECT product_id, month
FROM (
  SELECT product_id, month, total_sales,
         LAG(total_sales, 1) OVER (PARTITION BY product_id ORDER BY month) AS prev1,
         LAG(total_sales, 2) OVER (PARTITION BY product_id ORDER BY month) AS prev2
  FROM monthly_product_sales
) t
WHERE total_sales < prev1 AND prev1 < prev2;

-- Gap to the next lower salary
SELECT name, salary,
       salary - LEAD(salary) OVER (ORDER BY salary DESC) AS gap_to_next_lower
FROM employees;
```

**Year-over-year growth using a CTE and a self-join** (an alternative to LAG when the periods aren't adjacent rows):
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

---

## 45. NTILE, PERCENT_RANK, CUME_DIST, FIRST_VALUE / LAST_VALUE / NTH_VALUE

### NTILE(n)
Divides the result set into `n` roughly equal buckets and assigns a bucket number to each row.

```sql
-- Split employees into 4 salary quartiles
SELECT name, salary, NTILE(4) OVER (ORDER BY salary) AS quartile
FROM employees;

-- Rank customers into deciles by lifetime spend
SELECT customer_id, total_spend,
       NTILE(10) OVER (ORDER BY total_spend) AS spend_decile
FROM (SELECT customer_id, SUM(amount) AS total_spend FROM orders GROUP BY customer_id) t;
```

### PERCENT_RANK and CUME_DIST
```sql
-- Percentile rank of each employee's salary (0 to 1)
SELECT name, salary, PERCENT_RANK() OVER (ORDER BY salary) AS percentile_rank
FROM employees;

-- Cumulative distribution
SELECT name, salary, CUME_DIST() OVER (ORDER BY salary) AS cum_dist
FROM employees;
```

### PERCENTILE_CONT — medians and other percentiles
```sql
-- Median order amount
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY amount) AS median_amount
FROM orders;

-- Total, average and median together
SELECT COUNT(*)               AS total_orders,
       SUM(amount)            AS total_revenue,
       ROUND(AVG(amount), 2)  AS avg_order_value,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY amount) AS median_order_value
FROM orders;

-- Median per department
SELECT department_id,
       PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) AS median_salary
FROM employees
GROUP BY department_id;
```

**Median without PERCENTILE_CONT** (portable, uses LIMIT/OFFSET arithmetic to grab the middle 1 or 2 rows):
```sql
SELECT AVG(salary) AS median_salary
FROM (
  SELECT salary FROM employees ORDER BY salary
  LIMIT 2 - (SELECT COUNT(*) FROM employees) % 2
  OFFSET (SELECT (COUNT(*) - 1) / 2 FROM employees)
) AS median_subquery;
```

**Mode** (most frequently occurring value):
```sql
SELECT salary FROM employees GROUP BY salary ORDER BY COUNT(*) DESC LIMIT 1;
```

### FIRST_VALUE, LAST_VALUE, NTH_VALUE
```sql
-- Difference from the customer's first order
SELECT customer_id, order_date, amount,
       amount - FIRST_VALUE(amount) OVER (PARTITION BY customer_id ORDER BY order_date)
       AS diff_from_first
FROM orders;

-- Salary growth since first recorded salary
SELECT employee_id, raise_date, salary,
       salary - FIRST_VALUE(salary) OVER (PARTITION BY employee_id ORDER BY raise_date)
       AS growth_since_start
FROM salary_history;

-- First and last order amount per customer
-- NOTE the explicit frame: LAST_VALUE needs it, or it only sees up to the current row
SELECT DISTINCT customer_id,
       FIRST_VALUE(amount) OVER (
         PARTITION BY customer_id ORDER BY order_date
         ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS first_amount,
       LAST_VALUE(amount) OVER (
         PARTITION BY customer_id ORDER BY order_date
         ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_amount
FROM orders;

-- 3rd highest salary per department using NTH_VALUE
SELECT department_id,
       NTH_VALUE(salary, 3) OVER (
         PARTITION BY department_id ORDER BY salary DESC
         ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
       ) AS third_highest
FROM employees;
```

> **`LAST_VALUE` gotcha:** without an explicit frame, the default window ends at the current row, so `LAST_VALUE` returns the current row's value — which looks broken. Always add `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`.

### Percentage-of-total with window functions

```sql
-- Each product's share of total sales
SELECT product_id, total_sales,
       ROUND(100.0 * total_sales / SUM(total_sales) OVER (), 2) AS pct_of_total
FROM (SELECT product_id, SUM(quantity * price) AS total_sales
      FROM order_items GROUP BY product_id) t;

-- Each department's share of company headcount
-- (note SUM(COUNT(*)) OVER () — an aggregate inside a window function)
SELECT department_id, COUNT(*) AS headcount,
       ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS pct_of_company
FROM employees
GROUP BY department_id;

-- Ratio of each employee's salary to their department's maximum
SELECT name, department_id, salary,
       ROUND(salary::NUMERIC / MAX(salary) OVER (PARTITION BY department_id), 2)
       AS pct_of_dept_max
FROM employees;

-- Z-score of each employee's salary
SELECT name, salary,
       (salary - AVG(salary) OVER ()) / NULLIF(STDDEV(salary) OVER (), 0) AS z_score
FROM employees;

-- Count of employees earning more (an inverse rank)
SELECT name, salary,
       COUNT(*) OVER (ORDER BY salary DESC
                      ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING) AS higher_earners
FROM employees;
```

### Window function summary table

| Function | Purpose | Duplicates | Skips numbers | Example usage |
|----------|---------|------------|---------------|---------------|
| ROW_NUMBER | Unique rank | No | No | Employee ranking, dedup |
| RANK | Rank with skips | Yes | Yes | Competition rank |
| DENSE_RANK | Rank without skips | Yes | No | Class rank, Nth highest |
| NTILE | Divide rows into buckets | No | No | Quartiles, deciles |
| SUM | Running total | No | No | Salary analysis |
| AVG | Running average | No | No | Moving averages |
| LEAD | Next row's value | No | No | Price trends |
| LAG | Previous row's value | No | No | Sales trends, growth |

---

## 46. Pivot and Unpivot

**A Pivot Table in SQL transforms row data into column data** to give a summary report of the dataset. It performs data aggregation and presents it in a more readable format.

- Converts rows into columns
- Used to generate summary reports
- Commonly used with aggregate functions like `SUM()`, `AVG()`, `COUNT()`

### Pivot using CASE (works everywhere)

```sql
-- Turn months into columns
SELECT region,
       SUM(CASE WHEN month = 'Jan' THEN sales_amount ELSE 0 END) AS Jan,
       SUM(CASE WHEN month = 'Feb' THEN sales_amount ELSE 0 END) AS Feb,
       SUM(CASE WHEN month = 'Mar' THEN sales_amount ELSE 0 END) AS Mar
FROM sales
GROUP BY region;

-- Transpose exam scores so each subject becomes a column
SELECT student_id,
       MAX(CASE WHEN subject = 'Math'    THEN score END) AS Math,
       MAX(CASE WHEN subject = 'Science' THEN score END) AS Science,
       MAX(CASE WHEN subject = 'English' THEN score END) AS English
FROM exam_scores
GROUP BY student_id;

-- Year-over-year comparison of quarterly revenue in one pivoted result
SELECT quarter,
       SUM(CASE WHEN year = 2024 THEN revenue END) AS revenue_2024,
       SUM(CASE WHEN year = 2025 THEN revenue END) AS revenue_2025
FROM quarterly_revenue
GROUP BY quarter
ORDER BY quarter;
```

Use `ELSE 0` with SUM when you want zeros for missing combinations; omit the ELSE (giving NULL) when "no data" is meaningfully different from "zero".

### PIVOT operator (SQL Server / Oracle)
```sql
SELECT region, [Jan], [Feb], [Mar]
FROM (
  SELECT region, month, sales_amount
  FROM sales
) AS src
PIVOT (
  SUM(sales_amount)
  FOR month IN ([Jan], [Feb], [Mar])
) AS p;
```

### Unpivot — columns back into rows
```sql
SELECT product_id, 'Jan' AS month, jan_sales AS amount FROM sales_wide
UNION ALL
SELECT product_id, 'Feb', feb_sales FROM sales_wide
UNION ALL
SELECT product_id, 'Mar', mar_sales FROM sales_wide;
```

### GROUPING SETS, ROLLUP and CUBE
Rather than writing several UNIONed GROUP BY queries, ask for multiple grouping levels at once.

```sql
-- Subtotals per region and a grand total
SELECT region, product_category, SUM(amount) AS total_sales
FROM sales
GROUP BY ROLLUP (region, product_category);

-- Cross-tabulation of headcount by department and job title (every combination)
SELECT department_id, job_title, COUNT(*) AS headcount
FROM employees
GROUP BY CUBE (department_id, job_title);

-- Exactly the grouping levels you name
SELECT region, product_category, SUM(amount) AS total_sales
FROM sales
GROUP BY GROUPING SETS ((region), (product_category), (region, product_category));
```

- **ROLLUP** — hierarchical subtotals (region → region+category → grand total).
- **CUBE** — every possible combination of the grouping columns.
- **GROUPING SETS** — exactly the combinations you list.

---

## 47. Gaps and Islands

"Gaps and islands" problems ask about **runs of consecutive values** — login streaks, uptime periods, missing IDs. There is one trick that solves almost all of them.

### The trick

For consecutive dates, `date - ROW_NUMBER()` is **constant within a run**. When the run breaks, the constant changes. So you group by that constant.

```sql
-- Login streak groups
SELECT customer_id, login_date,
       login_date - ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY login_date)::INT
       AS streak_group
FROM logins;
```

### Longest streak of consecutive active days per user
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

### Islands: periods a machine was continuously active
```sql
SELECT machine_id, MIN(active_date) AS island_start, MAX(active_date) AS island_end
FROM (
  SELECT machine_id, active_date,
         active_date - ROW_NUMBER() OVER (PARTITION BY machine_id ORDER BY active_date)::INT AS grp
  FROM machine_activity
) t
GROUP BY machine_id, grp;
```

### Gaps: missing dates in a sequence of daily sales
```sql
SELECT d.calendar_date
FROM calendar d
LEFT JOIN sales s ON d.calendar_date = s.sale_date
WHERE s.sale_date IS NULL
  AND d.calendar_date BETWEEN (SELECT MIN(sale_date) FROM sales)
                          AND (SELECT MAX(sale_date) FROM sales);
```
(You need a calendar/date-dimension table for this — or generate one with a recursive CTE, §40.)

### Gaps in an ID sequence
```sql
-- Three consecutive missing IDs
SELECT id + 1 AS missing_start
FROM sequence_table s1
WHERE NOT EXISTS (SELECT 1 FROM sequence_table s2 WHERE s2.id = s1.id + 1)
  AND NOT EXISTS (SELECT 1 FROM sequence_table s3 WHERE s3.id = s1.id + 2)
  AND NOT EXISTS (SELECT 1 FROM sequence_table s4 WHERE s4.id = s1.id + 3);
```

### Merging overlapping ranges (the advanced version)
```sql
-- Merge overlapping subscription periods per user into continuous periods
WITH ordered AS (
  SELECT user_id, start_date, end_date,
         MAX(end_date) OVER (
           PARTITION BY user_id ORDER BY start_date
           ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING
         ) AS prev_max_end
  FROM subscriptions
),
flagged AS (
  SELECT *,
         CASE WHEN start_date > prev_max_end OR prev_max_end IS NULL THEN 1 ELSE 0 END
         AS is_new_island
  FROM ordered
),
grouped AS (
  SELECT *, SUM(is_new_island) OVER (PARTITION BY user_id ORDER BY start_date) AS island_id
  FROM flagged
)
SELECT user_id, island_id,
       MIN(start_date) AS period_start,
       MAX(end_date)   AS period_end
FROM grouped
GROUP BY user_id, island_id;
```

The pattern here is worth internalising: **flag where a new group starts (1/0), then take a running SUM of that flag to produce a group id.** It generalises far beyond dates.

### Login gaps larger than 30 days
```sql
SELECT user_id, login_date,
       login_date - LAG(login_date) OVER (PARTITION BY user_id ORDER BY login_date) AS gap_days
FROM logins;
-- then filter gap_days > 30 in an outer query
```

---

# PART 8 — OBJECTS AND PROGRAMMABILITY

## 48. Views and Materialized Views

**A View is a virtual table based on the result of a SELECT query.**

- Does **not** store data physically
- Simplifies complex queries
- Provides data security (expose only the columns people should see)
- Can be used like a table in SELECT queries
- Automatically reflects changes in the base table

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

```sql
CREATE VIEW vw_EmployeeBasic AS
SELECT id, name, dept, salary
FROM Employee
WHERE salary > 30000;

-- Then query it like a table
SELECT * FROM vw_EmployeeBasic;
```

Security use — expose only non-sensitive columns:
```sql
CREATE VIEW employee_directory AS
SELECT id, name, department_id, job_title, email
FROM employees;
```

### View vs Table

| View | Table |
|------|-------|
| Virtual table | Physical table |
| Does **not** store data physically | Stores data physically |
| Based on SQL queries | Contains raw data |
| Provides data security by restricting access to certain columns | No data restriction unless applied |
| Automatically updates when base table data changes | Needs manual updates |

### View vs Materialized View
A **materialized view** is a **physical copy** of the view's result set, stored in the database and refreshed periodically. It improves query performance at the cost of data freshness.

```sql
CREATE MATERIALIZED VIEW monthly_sales_summary AS
SELECT DATE_TRUNC('month', sale_date) AS month, SUM(amount) AS total_sales
FROM sales
GROUP BY DATE_TRUNC('month', sale_date);

REFRESH MATERIALIZED VIEW monthly_sales_summary;
```

Regular view = always current, computed each time. Materialized view = fast, possibly stale.

---

## 49. Indexes

**An Index is a data structure that speeds up data retrieval on one or more columns** — at the cost of extra disk space and slower writes.

Think of it like the index at the back of a book: instead of reading every page (a full table scan), you jump straight to the right page.

```sql
CREATE INDEX index_name
ON table_name (column_name);

CREATE INDEX idx_customer_id ON transactions(customer_id);
```

This makes queries like `SELECT * FROM transactions WHERE customer_id = 101;` dramatically faster.

**Key points**
- Speeds up `SELECT` queries
- Automatically maintained by the database as data changes
- Can be created on one or more columns
- **Slows down `INSERT`, `UPDATE`, `DELETE`** — because indexes must be updated too
- Especially valuable on large tables
- Best on columns used in `WHERE`, `JOIN`, `ORDER BY` and `GROUP BY`

| Feature | With Index | Without Index |
|---------|-----------|---------------|
| Search performance | Fast (uses B-tree / binary search) | Slow (scans every row — full table scan) |
| Used in | WHERE, JOIN, ORDER BY, GROUP BY | Inefficient for large datasets |
| Types | B-tree (default), Bitmap, Hash, etc. | — |

### Types of index

1. **Primary Index** — automatically created on Primary Key columns.
2. **Unique Index** — ensures values in a column are unique.
3. **Clustered Index** — sorts and stores the data rows physically based on key values. **Only one per table.**
4. **Non-Clustered Index** — a separate structure storing pointers to data rows. **Multiple allowed.**

### Clustered vs Non-Clustered Index

| Clustered Index | Non-Clustered Index |
|-----------------|---------------------|
| Stores data **physically sorted** by the indexed column | Stores **pointers** to the data |
| **Only one** per table | **Multiple** allowed per table |
| Faster for data retrieval | Slower than clustered index |
| Automatically created on the Primary Key | Manually created on any column |
| Affects the physical order of the table | Does **not** affect physical order |

```sql
-- Clustered (SQL Server syntax)
CREATE CLUSTERED INDEX idx_emp_id ON Employees(EmployeeID);

-- Non-clustered
CREATE NONCLUSTERED INDEX idx_emp_name ON Employees(Name);
```

### Advanced index types

```sql
-- Composite index for a common two-column filter
CREATE INDEX idx_orders_customer_date ON orders (customer_id, order_date);

-- Partial index: only index the rows you actually query
CREATE INDEX idx_active_employees ON employees (department_id) WHERE is_active = TRUE;
CREATE INDEX idx_active_orders    ON orders (order_date)       WHERE status = 'active';

-- Covering index: INCLUDE extra columns so the query never touches the table
CREATE INDEX idx_orders_covering ON orders (customer_id, order_date) INCLUDE (amount);
```

**Composite index rule (leftmost prefix):** an index on `(a, b, c)` helps queries filtering on `a`, on `a, b`, and on `a, b, c` — but generally *not* a query filtering only on `b` or only on `c`. Column order matters.

### Index best practices
- Index columns that are **frequently searched, joined or filtered**.
- **Do not over-index** — every index slows down writes.
- Avoid indexing columns with **low cardinality** (e.g. gender, a boolean flag) — the index barely narrows anything down.
- Use **composite indexes** when you query multiple columns together.
- Too many indexes can slow down `INSERT`/`UPDATE`.

### Index Fragmentation

**Index fragmentation occurs when the logical order of index pages does not match the physical order of the data on disk**, which makes data retrieval slower.

Two types:
1. **Internal Fragmentation** — unused space *inside* index pages, caused by deletions or updates.
2. **External Fragmentation** — index pages stored in non-sequential order, causing slower access.

How to fix it:
- MySQL: `OPTIMIZE TABLE table_name;` to reorganize index pages.
- SQL Server: `ALTER INDEX ... REORGANIZE` or `REBUILD`.
- PostgreSQL: `REINDEX` / `VACUUM FULL`.

Index fragmentation slows down query performance and should be fixed regularly to maintain database efficiency.

---

## 50. Stored Procedures and Functions

### Stored Procedure
**A Stored Procedure is a group of predefined SQL statements stored in the database that can be executed multiple times.**

- Improves code reusability
- Increases performance (parsed and compiled once)
- Supports **input and output** parameters
- Provides security by hiding SQL code

```sql
CREATE PROCEDURE procedure_name (IN param1 datatype)
BEGIN
    -- SQL statements
END;

-- Execute it
CALL procedure_name(value);      -- MySQL
EXEC procedure_name value;       -- SQL Server
```

```sql
CREATE PROCEDURE GetEmployeesByDept (IN deptId INT)
BEGIN
    SELECT * FROM Employees WHERE DepartmentID = deptId;
END;
```

### Function vs Stored Procedure

| Function | Stored Procedure |
|----------|------------------|
| Returns a single value or a table — **always returns something** | May or may not return a value |
| **Can** be used inside a SELECT statement | **Cannot** be used inside a SELECT statement |
| Allows only **input** parameters | Allows **input and output** parameters |
| **Cannot** modify database state (no INSERT/UPDATE/DELETE) | **Can** modify database state |
| Cannot call stored procedures inside it | Can call functions inside it |
| Used for calculations and returning values | Used for business logic and complex operations |

The short version: **a function computes and returns; a procedure does work.**

```sql
CREATE FUNCTION GetAnnualSalary(monthly DECIMAL(10,2))
RETURNS DECIMAL(10,2)
BEGIN
    RETURN monthly * 12;
END;

SELECT name, GetAnnualSalary(salary) AS annual FROM Employees;
```

---

## 51. Triggers

**A Trigger is an automatic action executed when a specified event occurs in a table.**

- Automatically executes on `INSERT`, `UPDATE` or `DELETE`
- Used for data validation, auditing and logging
- **Cannot be called manually** — it fires on its own
- Improves data integrity

```sql
CREATE TRIGGER trigger_name
BEFORE | AFTER  INSERT | UPDATE | DELETE
ON table_name
FOR EACH ROW
BEGIN
    -- statements
END;
```

**Example — auto-update an `updated_at` timestamp (PostgreSQL)**
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

**Example — audit logging (MySQL)**
```sql
CREATE TRIGGER after_employee_insert
AFTER INSERT ON Employees
FOR EACH ROW
BEGIN
    INSERT INTO Employee_Audit (EmpID, Action, ActionDate)
    VALUES (NEW.EmployeeID, 'INSERT', NOW());
END;
```

Triggers are powerful but invisible — someone reading the application code has no idea they exist. Use them sparingly and document them.

---

## 52. Cursors

**A Cursor is a database object used to retrieve, manipulate and navigate row-by-row through a result set.**

- Used to process results **one row at a time**
- **Slower** than set-based operations
- Helps in complex data manipulation
- **Not recommended for large datasets**

```sql
DECLARE cursor_name CURSOR FOR SELECT column FROM table;
OPEN cursor_name;
FETCH NEXT FROM cursor_name INTO @variable;
-- loop...
CLOSE cursor_name;
DEALLOCATE cursor_name;
```

> SQL is a **set-based** language. Almost anything a cursor does can be expressed as a single set-based statement that runs orders of magnitude faster. Reach for a cursor only when you genuinely need row-by-row procedural logic.

---

## 53. Sequences and Auto Increment

**Auto Increment automatically generates a unique sequential number whenever a new row is inserted.** It is typically used to create unique identifiers such as primary keys.

- Automatically generates unique numbers
- Commonly used with Primary Key columns
- Starts from a defined value (default is 1)
- Automatically increments by 1 for each new row

```sql
-- MySQL
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    Name       VARCHAR(50),
    Salary     DECIMAL(10,2)
);

-- PostgreSQL
CREATE TABLE Employees (
    EmployeeID SERIAL PRIMARY KEY,
    Name       VARCHAR(50)
);

-- SQL Server
CREATE TABLE Employees (
    EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
    Name       VARCHAR(50)
);
```

```sql
INSERT INTO Employees (Name, Salary) VALUES ('Vinay', 50000);
INSERT INTO Employees (Name, Salary) VALUES ('Awadhesh', 40000);
```

| EmployeeID | Name | Salary |
|------------|------|--------|
| 1 | Vinay | 50000 |
| 2 | Awadhesh | 40000 |

The `EmployeeID` column increments without any user input.

### Sequences (an independent number generator)
```sql
CREATE SEQUENCE invoice_seq START 10000;

UPDATE invoices
SET invoice_number = nextval('invoice_seq')
WHERE invoice_number IS NULL;
```
A sequence is a standalone object — unlike AUTO_INCREMENT, it is not tied to one table, so several tables can draw from the same sequence.

### Generated (computed) columns
```sql
CREATE TABLE order_items (
  order_id   INT,
  product_id INT,
  quantity   INT,
  price      DECIMAL(10,2),
  line_total DECIMAL(10,2) GENERATED ALWAYS AS (quantity * price) STORED
);
```
The database computes `line_total` for you and keeps it correct — you cannot forget to update it.

---

## 54. Dynamic SQL

**Dynamic SQL is a method of constructing and executing SQL statements at runtime**, instead of writing static queries.

- Allows flexible query creation based on user input or conditions
- Used for complex queries with varying conditions
- Helps in parameterized queries and stored procedures
- **Increases security risks if not handled properly**

**Example (MySQL)**
```sql
SET @query = CONCAT('SELECT * FROM Employees WHERE DepartmentID = ', @deptId);
PREPARE stmt FROM @query;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

Safer, parameterized form:
```sql
SET @query = 'SELECT * FROM Employees WHERE DepartmentID = ?';
PREPARE stmt FROM @query;
EXECUTE stmt USING @deptId;
DEALLOCATE PREPARE stmt;
```

> **Dynamic SQL provides flexibility, but should always be used with parameterized queries to prevent SQL injection attacks.** Never concatenate raw user input into a query string.

---

## 55. JSON and XML in SQL

### JSON
**JSON (JavaScript Object Notation) in SQL is used to store, retrieve and manipulate data in a structured, text-based format** inside a relational database.

- Stores data in key-value pairs
- Lightweight and easy to read
- Commonly used for semi-structured data
- Supported in MySQL, SQL Server and PostgreSQL

```sql
-- Create a table with a JSON column
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Details   JSON
);

-- Insert JSON data
INSERT INTO Products (ProductID, Details)
VALUES (1, '{"name": "Laptop", "brand": "Dell", "price": 55000}');

-- Retrieve JSON data (MySQL)
SELECT ProductID,
       JSON_EXTRACT(Details, '$.name')  AS ProductName,
       JSON_EXTRACT(Details, '$.price') AS Price
FROM Products;

-- PostgreSQL
SELECT Details->>'name' AS ProductName FROM Products;
```

JSON lets you handle semi-structured data inside a relational database without needing a separate NoSQL database.

### XML
**XML (Extensible Markup Language) in SQL is used to store, retrieve and manipulate structured data in a text-based format.**

- Stores data hierarchically using tags
- Commonly used for data exchange between applications
- Supported in SQL Server, MySQL and Oracle
- Helps store semi-structured data

```sql
CREATE TABLE Orders (
    OrderID   INT PRIMARY KEY,
    OrderData XML          -- SQL Server; use TEXT in MySQL
);

INSERT INTO Orders (OrderID, OrderData)
VALUES (1, '<order><item>Laptop</item><qty>2</qty></order>');

-- SQL Server extraction
SELECT OrderData.value('(/order/item)[1]', 'VARCHAR(50)') AS Item
FROM Orders;
```

XML is used to store and transfer hierarchical data in relational databases, making it easier to exchange data between applications.

---

# PART 9 — TRANSACTIONS AND RELIABILITY

## 56. Transactions and the ACID Properties

**A Transaction is a group of SQL operations executed as a single logical unit of work.** Either all of them succeed, or none of them do. It ensures data consistency and integrity by either committing all changes or rolling them back if an error occurs.

The classic example is a bank transfer: debit one account, credit another. If the second step fails, the first must be undone — otherwise money vanishes.

### The ACID Properties

**ACID** defines the key principles that ensure database transactions are processed reliably without damaging data integrity.

| Property | Description |
|----------|-------------|
| **A — Atomicity** | A transaction is all or nothing. If one part fails, the entire transaction fails and the database remains unchanged. |
| **C — Consistency** | The database must be in a valid, consistent state before and after the transaction. Data remains correct and valid. |
| **I — Isolation** | Transactions execute independently, without interfering with each other. |
| **D — Durability** | Once a transaction is committed, the changes are permanent — even if the system crashes. |

### Transaction commands

| Command | Description |
|---------|-------------|
| `BEGIN TRANSACTION` / `START TRANSACTION` | Starts a new transaction |
| `COMMIT` | Saves the changes permanently |
| `ROLLBACK` | Undoes changes if an error occurs |
| `SAVEPOINT` | Sets a point to roll back to partially |

### The bank transfer example

```sql
BEGIN TRANSACTION;

UPDATE Accounts SET Balance = Balance - 1000 WHERE AccountID = 1;
UPDATE Accounts SET Balance = Balance + 1000 WHERE AccountID = 2;

COMMIT;
```

How each ACID property applies here:

1. **Atomicity** — if one of the two queries fails, both updates are rolled back.
2. **Consistency** — the total amount across both accounts remains the same.
3. **Isolation** — if another transaction tries to access the same account, it waits until this transaction completes.
4. **Durability** — after `COMMIT`, the changes are saved permanently, even in a power failure.

### Transaction flow

```
        START TRANSACTION
                │
                ▼
       INSERT / UPDATE / DELETE
                │
                ▼
         SAVEPOINT (optional)
             ┌──┴──┐
             ▼     ▼
         COMMIT   ROLLBACK
       (Permanent) (Undo changes)
            ✓         ✗
```

---

## 57. COMMIT, ROLLBACK, SAVEPOINT

**COMMIT and ROLLBACK are transaction statements.**

### COMMIT
Used to store changes permanently, performed by a transaction.
```sql
COMMIT;
```

### ROLLBACK
Used for reverting changes performed by a transaction.
```sql
ROLLBACK;
```

### COMMIT vs ROLLBACK

| COMMIT | ROLLBACK |
|--------|----------|
| Saves the changes made by the transaction **permanently** into the database | **Undoes** all changes made by the transaction |
| Once executed, changes cannot be undone | Restores the database to its previous state |
| Syntax: `COMMIT;` | Syntax: `ROLLBACK;` |
| Used when all operations are successful | Used when an error occurs during the transaction |
| Improves data durability | Helps maintain data consistency |

### SAVEPOINT

**A Savepoint temporarily saves a transaction at a specific point, allowing you to roll back only *part* of the transaction** without affecting the entire transaction.

- Allows setting multiple points in a transaction
- Helps in **partial rollback**
- Improves error handling
- Used together with `ROLLBACK`

```sql
SAVEPOINT savepoint_name;
ROLLBACK TO savepoint_name;
```

**Worked example**
```sql
BEGIN TRANSACTION;

UPDATE Employees SET Salary = 60000 WHERE EmpID = 101;
SAVEPOINT sp1;

UPDATE Employees SET Salary = 70000 WHERE EmpID = 102;
ROLLBACK TO sp1;      -- undoes only the second update

UPDATE Employees SET Salary = 55000 WHERE EmpID = 103;

COMMIT;
```

- The first update **will be saved**.
- The second update **will be rolled back**.
- The remaining changes will be committed.

**Best practices**
- COMMIT persists changes permanently.
- ROLLBACK undoes uncommitted changes.
- SAVEPOINT allows partial rollback.
- Always test in a safe environment before running transactions in production.

---

## 58. Deadlocks

**A Deadlock occurs when two or more transactions block each other by holding locks on resources that the other transactions need.** A circular dependency forms, none of the transactions can proceed, and the system may become unresponsive.

```
Transaction A holds lock on Table 1, wants Table 2
Transaction B holds lock on Table 2, wants Table 1
→ Neither can proceed. Deadlock.
```

### Seven ways to avoid deadlocks

1. **Access tables in the same order** — always access tables in a consistent sequence across all transactions. This alone prevents most deadlocks.
2. **Minimize lock time** — keep transactions short and fast to reduce lock-holding time.
3. **Use lower isolation levels** — use `READ COMMITTED` instead of `SERIALIZABLE` where possible.
4. **Avoid user interaction inside transactions** — never wait for user input while a transaction holds locks.
5. **Use NOLOCK / READ UNCOMMITTED** — allow non-blocking reads for read-only operations (accepting that you may read uncommitted data).
6. **Proper indexing** — good indexes minimize the number of rows that need to be locked.
7. **Break large transactions** — split large transactions into smaller batches.

Most database engines detect deadlocks automatically and kill one transaction (the "victim"), which then returns an error. Well-written applications catch that error and retry.

---

## 59. Isolation Levels

Isolation levels control how much one transaction can see of another's uncommitted work. Lower isolation = more concurrency but more anomalies.

| Level | Dirty read | Non-repeatable read | Phantom read |
|-------|-----------|---------------------|--------------|
| READ UNCOMMITTED | Possible | Possible | Possible |
| READ COMMITTED | Prevented | Possible | Possible |
| REPEATABLE READ | Prevented | Prevented | Possible |
| SERIALIZABLE | Prevented | Prevented | Prevented |

- **Dirty read** — you read data another transaction wrote but has not committed (and may roll back).
- **Non-repeatable read** — you read the same row twice in one transaction and get different values.
- **Phantom read** — you run the same query twice and a new row has appeared.

```sql
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

`READ COMMITTED` is the default in PostgreSQL, Oracle and SQL Server. `REPEATABLE READ` is the default in MySQL/InnoDB.

---

# PART 10 — PERFORMANCE

## 60. What Indexing Really Does

Covered in detail in §49. The performance summary:

**Indexing improves the speed of data retrieval by creating a lookup structure — like a book's index.**
- Reduces the time required for SELECT queries.
- Automatically updated when data is inserted, updated or deleted.
- Create them on columns frequently used in `WHERE`, `JOIN` and `ORDER BY` clauses.

**Conclusion: indexing improves query performance by quickly locating data, but may increase the time for INSERT, UPDATE and DELETE operations.** Every index is a trade: faster reads, slower writes, more disk.

Finding indexes that aren't earning their keep (PostgreSQL):
```sql
SELECT relname AS table_name, indexrelname AS index_name, idx_scan
FROM pg_stat_user_indexes
WHERE idx_scan = 0
ORDER BY relname;
```
An index never scanned is pure write overhead — drop it.

---

## 61. Query Execution Plans

**A Query Execution Plan is the detailed roadmap the database engine uses to execute your SQL query.**

- Shows how the database will retrieve the data
- Helps analyze performance and optimize queries
- Displays the order of execution for each operation (joins, scans, sorting)
- Provides information about indexes, table scans and filtering methods

```sql
-- MySQL / PostgreSQL
EXPLAIN SELECT * FROM Employees WHERE DepartmentID = 5;

-- PostgreSQL: actually run it and report real timings
EXPLAIN ANALYZE
SELECT c.name, SUM(o.amount)
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.name;

-- SQL Server
SET SHOWPLAN_ALL ON;
```

**Why use the execution plan**
- Identify performance bottlenecks.
- Check if the query is using **indexes** or doing **table scans**.
- Understand how joins and filters are applied.

**What to look for:** a *Seq Scan* / *Table Scan* on a large table where you expected an *Index Scan* usually means a missing index — or a query written in a way that prevents the index being used (see §62).

Confirm an index actually helped:
```sql
CREATE INDEX idx_customers_email ON customers (email);
EXPLAIN ANALYZE
SELECT * FROM customers WHERE email = 'alice@example.com';
```

Diagnosing a blocked query (PostgreSQL):
```sql
SELECT blocked.pid AS blocked_pid, blocking.pid AS blocking_pid, blocked.query AS blocked_query
FROM pg_stat_activity blocked
JOIN pg_locks bl ON blocked.pid = bl.pid AND NOT bl.granted
JOIN pg_locks kl ON bl.locktype = kl.locktype AND bl.relation = kl.relation AND kl.granted
JOIN pg_stat_activity blocking ON kl.pid = blocking.pid
WHERE blocked.pid <> blocking.pid;
```

Checking table bloat to decide whether a VACUUM/REINDEX is needed:
```sql
SELECT relname, n_dead_tup, n_live_tup,
       ROUND(100.0 * n_dead_tup / NULLIF(n_live_tup + n_dead_tup, 0), 2) AS dead_pct
FROM pg_stat_user_tables
ORDER BY dead_pct DESC;
```

Refresh statistics after a bulk load so the planner makes good choices:
```sql
COPY orders FROM '/data/orders_bulk.csv' WITH (FORMAT csv, HEADER true);
ANALYZE orders;
```

---

## 62. Query Optimization Rules

**Query Optimization is the process of improving the efficiency and performance of SQL queries** to retrieve data faster while using minimal system resources.

- Reduces query execution time
- Improves database performance
- Minimizes CPU, memory and I/O
- Partly performed automatically by the Query Optimizer in most RDBMS

### The ten rules

**1. Use indexes** — create indexes on columns used in `WHERE`, `JOIN` and `ORDER BY` clauses.

**2. Avoid `SELECT *`** — select only the columns you need.
```sql
-- Bad
SELECT * FROM orders;
-- Good
SELECT order_id, customer_id FROM orders;

-- Bad (over-fetching on a high-traffic endpoint)
SELECT * FROM products WHERE category_id = 3;
-- Good
SELECT product_id, product_name, price FROM products WHERE category_id = 3;
```

**3. Use joins efficiently** — prefer `INNER JOIN` over `OUTER JOIN` when you don't need the unmatched rows.

**4. Use `EXISTS` instead of `IN`** for subqueries on large datasets.
```sql
SELECT name FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id);
```

**5. Use `WHERE` instead of `HAVING`** where possible — filter rows early, before grouping.

**6. Avoid functions on indexed columns** — a function wrapped around a column makes the index unusable.
```sql
-- Slower (cannot use the index on order_date)
WHERE YEAR(order_date) = 2024
-- Better: an index-friendly range scan
WHERE order_date >= '2024-01-01' AND order_date < '2025-01-01'
```
This one rule accounts for an enormous share of real-world slow queries.

**7. Optimize subqueries** — use `JOIN` instead of a correlated subquery where possible.
```sql
-- Correlated subquery (can be slow row-by-row)
-- SELECT * FROM employees e WHERE EXISTS (SELECT 1 FROM project_assignments p WHERE p.employee_id = e.id);
-- Semi-join rewrite
SELECT DISTINCT e.*
FROM employees e
JOIN project_assignments p ON p.employee_id = e.id;
```

**8. Partition large tables** — split large tables into smaller partitions (§63).

**9. Use CTEs and temp tables** — store intermediate results instead of recomputing them.
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

**10. Analyze the execution plan** — use `EXPLAIN` / `EXPLAIN ANALYZE` / `SHOWPLAN` to see how the query is actually executed.

Plus: **use `LIMIT`/`TOP`** to fetch only the rows you need, use **appropriate data types** and avoid implicit conversions, and **normalize** the schema to reduce redundancy.

### More rewrite patterns worth memorising

```sql
-- NOT IN → NOT EXISTS (avoids the NULL trap AND is usually faster)
-- Risky: if the subquery returns any NULL, you get ZERO rows back
-- SELECT * FROM customers WHERE customer_id NOT IN (SELECT customer_id FROM orders);
SELECT c.*
FROM customers c
WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id);

-- Chained ORs → IN list
-- WHERE status = 'pending' OR status = 'processing' OR status = 'shipped'
WHERE status IN ('pending', 'processing', 'shipped')

-- Self-join / correlated scalar subquery → window function (one pass instead of quadratic)
-- SELECT a.*, (SELECT MAX(amount) FROM orders b WHERE b.customer_id = a.customer_id) FROM orders a;
SELECT customer_id, amount,
       MAX(amount) OVER (PARTITION BY customer_id) AS max_amount
FROM orders;

-- DISTINCT masking a join fan-out → pre-aggregate before joining
-- SELECT DISTINCT c.customer_id, c.name FROM customers c JOIN orders o ON c.customer_id = o.customer_id;
SELECT c.customer_id, c.name, o.order_count
FROM customers c
JOIN (SELECT customer_id, COUNT(*) AS order_count FROM orders GROUP BY customer_id) o
  ON c.customer_id = o.customer_id;

-- Range join → equality join on a pre-bucketed key (when granularity allows)
-- SELECT * FROM events e JOIN sessions s ON e.event_time BETWEEN s.start_time AND s.end_time;
SELECT *
FROM events e
JOIN sessions s ON DATE_TRUNC('hour', e.event_time) = DATE_TRUNC('hour', s.start_time);

-- Keyset pagination: LIMIT with an indexed ORDER BY, instead of a huge OFFSET
SELECT order_id, order_date, amount
FROM orders
WHERE order_date < '2025-06-01'
ORDER BY order_date DESC
LIMIT 20;

-- Batch a large DELETE into chunks to avoid long lock times
DELETE FROM logs
WHERE ctid IN (
  SELECT ctid FROM logs
  WHERE log_date < CURRENT_DATE - INTERVAL '1 year'
  LIMIT 10000
);
-- Repeat in a loop until zero rows are affected.
```

**Good Query = Fast Query.** Write it, test it with small data, read the plan, then scale.

---

## 63. Table Partitioning

**Table Partitioning divides a large table into smaller, more manageable pieces without changing the table's logical structure.** Queries still address one table; the engine only reads the partitions it needs.

- Improves query performance on large datasets
- Simplifies data management (drop a whole month of data instantly)
- Helps in faster data retrieval
- Each partition is stored separately

### Types of partitioning

1. **Range Partitioning** — divides data based on value ranges (most common: by date).
2. **List Partitioning** — divides data based on specific column values (e.g. by country).
3. **Hash Partitioning** — distributes data evenly using a hash function.
4. **Composite Partitioning** — a combination of range and hash.

**MySQL range partitioning**
```sql
CREATE TABLE Sales (
    SaleID   INT,
    SaleDate DATE,
    Amount   DECIMAL(10,2)
)
PARTITION BY RANGE (YEAR(SaleDate)) (
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025),
    PARTITION p2025 VALUES LESS THAN (2026)
);
```

**PostgreSQL declarative partitioning**
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

Table partitioning improves performance and data management by splitting large datasets into smaller, manageable sections.

---

## 64. Index Fragmentation

Covered in §49 — summarised here for the performance checklist:

Fragmentation happens when the logical order of index pages stops matching the physical order on disk. Fix it periodically:
- MySQL: `OPTIMIZE TABLE t;`
- SQL Server: `ALTER INDEX ... REBUILD;`
- PostgreSQL: `REINDEX TABLE t;` / `VACUUM`

---

## 65. OLTP vs OLAP

| Feature | OLTP (Online Transaction Processing) | OLAP (Online Analytical Processing) |
|---------|--------------------------------------|-------------------------------------|
| Purpose | Day-to-day transactional operations, real-time | Data analysis and reporting |
| Operations | `INSERT`, `UPDATE`, `DELETE` | `SELECT` with complex aggregate/group/slice/dice queries |
| Focus | Data consistency and speed | Data aggregation and analysis |
| Data stored | Detailed, current transactional data | Historical and summarized data |
| Data structure | Highly **normalized** (3NF) | **De-normalized** (star / snowflake schema) |
| Speed | Fast read/write of **single rows** | Fast for complex analytical queries |
| Volume per operation | Small amounts of data per transaction | Large amounts processed at once |
| Users | Clerks, application users, DBAs | Analysts, data scientists |
| Backup/Recovery | Essential and frequent | Less frequent |
| Examples | Banking systems, e-commerce order processing | Data warehouses, BI dashboards, sales trend analysis |

**In short: OLTP = operational, fast, real-time transactions. OLAP = analytical, slow-changing, historical data.**

### Data Warehouse
**A data warehouse is a large, centralized repository that stores and manages data from various sources.** It is designed for efficient reporting, analysis and business intelligence — it is the classic home of OLAP workloads.

---

# PART 11 — REFERENCE

## 66. Types of Errors in SQL

| Error type | What it means | Example |
|-----------|---------------|---------|
| **Syntax Errors** | The SQL statement does not follow the correct syntax and structure of the language | `SELCT * FROM users;` — missing a keyword or a comma |
| **Semantic Errors** | The statement is grammatically correct, but does not produce the desired result due to incorrect logic | Using `WHERE` where you meant `HAVING`; joining on the wrong column |
| **Constraint Violations** | The SQL violates one or more constraints on the database | Inserting a duplicate value into a UNIQUE column; NULL into a NOT NULL column; an FK value that doesn't exist in the parent |
| **Datatype Errors** | Data is inserted in a way that does not match the expected data type | Inserting a string into a numeric field |
| **Transaction Errors** | A transaction fails due to problems with locking | Deadlocks, lock timeouts |

Semantic errors are the dangerous ones: the query runs happily and returns the *wrong answer*. This is why you test with small, known data before scaling.

---

## 67. Cheat Sheet — everything at a glance

### Basics
`SELECT`, `FROM`, `WHERE`, `ORDER BY`, `DISTINCT`, `ALIAS`, `LIMIT`/`TOP`

### Conditions
`=`, `<`, `>`, `<=`, `>=`, `<>` · `BETWEEN`, `IN`, `LIKE` · `IS NULL`, `IS NOT NULL` · `AND`, `OR`, `NOT`

### Joins
`INNER JOIN` · `LEFT` / `RIGHT JOIN` · `FULL OUTER JOIN` · `SELF JOIN`, `CROSS JOIN`

### Aggregate
`COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()` · `GROUP BY` · `HAVING`

### Subqueries
`WHERE`/`HAVING` subqueries · `IN`, `EXISTS`, `ANY`, `ALL` · correlated · scalar

### Advanced
`CTE`, window functions · `CASE WHEN` · `PIVOT`/`UNPIVOT` · `INDEX`, `VIEW`

### Clause order (write it, then read it back)
```
SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT   (written)
FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT   (executed)
```

### CRUD commands
`C: INSERT` · `R: SELECT` · `U: UPDATE` · `D: DELETE`

### Join meanings, in four words each
- `I` — Inner (Match)
- `L` — Left (All Left)
- `R` — Right (All Right)
- `F` — Full (All)

### ACID
Atomicity, Consistency, Isolation, Durability

### NULL
`NULL ≠ 0`, `NULL ≠ ''`, `NULL ≠ FALSE`

### Important function groups

| Group | Functions |
|-------|-----------|
| **String** | `UPPER()`, `LOWER()`, `INITCAP()`, `CONCAT()`, `SUBSTRING()`, `LENGTH()`, `TRIM()`, `REPLACE()` |
| **Date/Time** | `NOW()`, `CURDATE()`, `CURTIME()`, `DATEADD()`, `DATEDIFF()`, `FORMAT()`, `EXTRACT()`, `DATE_TRUNC()` |
| **Numeric** | `ROUND()`, `CEIL()`, `FLOOR()`, `ABS()`, `POWER()`, `MOD()`, `CAST()`, `CONVERT()` |
| **Aggregate** | `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`, `GROUP_CONCAT()`, `STDDEV()`, `VARIANCE()` |

### Common scenario → technique

| Scenario | Technique |
|----------|-----------|
| Find the second highest salary | `ORDER BY` + `LIMIT`/`OFFSET`, or a subquery with `MAX` |
| Find duplicate rows in a table | `GROUP BY` + `HAVING COUNT(*) > 1` |
| Find running total of salary by dept | `SUM() OVER (PARTITION BY ... ORDER BY ...)` |
| Find Nth highest salary | `LIMIT`/`OFFSET` or `DENSE_RANK()` |
| Delete duplicate rows keeping one | `ROW_NUMBER() OVER (PARTITION BY ...)`, keep `rn = 1` |
| Top N salaries in each department | `RANK()` / `DENSE_RANK()` by partition |
| Rows in A with no match in B | `LEFT JOIN ... WHERE b.key IS NULL`, or `NOT EXISTS` |
| "Has ALL of X" | `GROUP BY ... HAVING COUNT(DISTINCT ...) = (SELECT COUNT(*) ...)` |
| Consecutive-day streaks | `date - ROW_NUMBER()` grouping trick |
| Rows into columns | `SUM(CASE WHEN ... THEN ... END)` |

### Query writing checklist
- [ ] Understand the requirements clearly
- [ ] Identify the tables and their relationships
- [ ] Write the FROM clause first
- [ ] Apply WHERE filters
- [ ] Use GROUP BY if needed
- [ ] Add HAVING for groups
- [ ] Write ORDER BY
- [ ] Test with sample data
- [ ] Optimize (indexes and joins)
- [ ] Review performance

### Performance tips
- Use an INDEX on frequently searched columns.
- Avoid `SELECT *` — fetch only the columns you need.
- Use proper WHERE filters early.
- Avoid functions on indexed columns.
- Use JOINs instead of subqueries where possible.
- Use LIMIT to restrict large result sets.
- Analyze queries with `EXPLAIN` / `ANALYZE`.
- Normalize the schema to reduce redundancy.

### Bonus one-liners
- Check NULL → `IS NULL` / `IS NOT NULL`
- Filter multiple → `IN (..)` / `NOT IN (..)`
- Existence check → `EXISTS (subquery)`
- Pattern match → `LIKE '%text%'`
- Remove duplicates → `DISTINCT` or `GROUP BY`

### Important reminders
- Always handle NULLs carefully.
- Constraints ensure data accuracy.
- Transactions keep data safe.
- Practice complex joins and aggregations.
- Solve problems with logic, not luck.

**Final mantra: Write → Test → Optimize → Repeat → Excel.**

---

## 68. Practice Schema Used Throughout

Most examples in these notes (and all 350 questions in the interview file) are written against this schema.

### employees

| Column | Type | Description |
|--------|------|-------------|
| `id` | INT (PK) | Unique employee ID |
| `name` | VARCHAR | Employee full name |
| `department_id` | INT (FK) | Links to `departments.department_id` |
| `manager_id` | INT (FK, self) | Links to another employee's `id` |
| `job_title` | VARCHAR | Designation, e.g. Manager, Analyst |
| `salary` | DECIMAL | Monthly/annual salary |
| `join_date` | DATE | Date of hire |
| `email` | VARCHAR | Employee email address |

Sample rows:

| ID | NAME | DEPT_ID | MANAGER_ID | JOB_TITLE | SALARY | JOIN_DATE |
|----|------|---------|------------|-----------|--------|-----------|
| 1 | John Smith | 10 | NULL | Director | 120000 | 2018-03-01 |
| 2 | Aman Verma | 10 | 1 | Manager | 85000 | 2019-06-15 |
| 3 | Priya Singh | 20 | 1 | Manager | 90000 | 2020-01-10 |
| 4 | Rahul Mehta | 20 | 3 | Analyst | 55000 | 2021-09-20 |
| 5 | Sara Khan | 10 | 2 | Analyst | 52000 | 2022-02-05 |

### departments

| Column | Type | Description |
|--------|------|-------------|
| `department_id` | INT (PK) | Unique department ID |
| `department_name` | VARCHAR | e.g. Engineering, Sales, HR |
| `location` | VARCHAR | City/office location |

| DEPARTMENT_ID | DEPARTMENT_NAME | LOCATION |
|---------------|-----------------|----------|
| 10 | Engineering | New York |
| 20 | Sales | Chicago |
| 30 | HR | Boston |

### customers

| Column | Type | Description |
|--------|------|-------------|
| `customer_id` | INT (PK) | Unique customer ID |
| `name` | VARCHAR | Customer full name |
| `email` | VARCHAR | Customer email |
| `phone` | VARCHAR | Contact number |
| `signup_date` | DATE | Date customer registered |
| `country` | VARCHAR | Customer's country |

### orders & order_items

| Table | Columns | Description |
|-------|---------|-------------|
| `orders` | `order_id` (PK), `customer_id` (FK), `order_date`, `amount` | One row per order placed |
| `order_items` | `order_id` (FK), `product_id` (FK), `quantity`, `price` | Line items within an order |

Sample customers & orders:

| CUSTOMER_ID | NAME | ORDER_ID | ORDER_DATE | AMOUNT |
|-------------|------|----------|------------|--------|
| 101 | Alice Brown | 5001 | 2024-01-12 | 250.00 |
| 101 | Alice Brown | 5004 | 2024-03-02 | 180.50 |
| 102 | Mike Lee | 5002 | 2024-01-20 | 89.99 |
| 103 | Wei Zhang | 5003 | 2024-02-15 | 540.00 |

### products & categories

| Table | Columns | Description |
|-------|---------|-------------|
| `products` | `product_id` (PK), `product_name`, `category_id` (FK), `price`, `vendor_id`, `stock_quantity` | Product catalog |
| `categories` | `category_id` (PK), `category_name` | Product category lookup |

| PRODUCT_ID | PRODUCT_NAME | CATEGORY_ID | PRICE | STOCK_QUANTITY |
|------------|--------------|-------------|-------|----------------|
| 201 | Wireless Mouse | 1 | 25.99 | 120 |
| 202 | Mechanical Keyboard | 1 | 79.99 | 0 |
| 203 | Office Chair | 2 | 199.00 | 40 |

Some advanced questions also reference smaller, self-explanatory tables — `logins`, `leave_records`, `salary_history`, `project_assignments`, `subscriptions`, `timesheets`, `ledger_a` / `ledger_b`, `enrollments`, `sales`, `transactions` — whose purpose is always clear from the column names used in that query.

---

## A suggested learning order

If you are starting from zero, work through the notes in this order and write every query yourself:

1. **Week 1 — Foundations.** Parts 1–2. Create a database, create tables, add constraints. Understand keys and normalization.
2. **Week 2 — Single-table queries.** Part 3. SELECT, WHERE, operators, ORDER BY, LIMIT, NULL handling. Learn the execution order (§24) by heart.
3. **Week 3 — Summarizing.** Part 4. Aggregates, GROUP BY, HAVING, CASE, built-in functions.
4. **Week 4 — Multi-table queries.** Part 5. All join types, then the LEFT JOIN + IS NULL anti-join pattern, then set operators.
5. **Week 5 — Building blocks.** Part 6. Subqueries, correlated subqueries, EXISTS, CTEs.
6. **Week 6 — Analytics.** Part 7. Window functions, ranking, running totals, LAG/LEAD. This is where interview difficulty concentrates.
7. **Week 7 — Objects & transactions.** Parts 8–9. Views, indexes, procedures, triggers, ACID.
8. **Week 8 — Performance & practice.** Part 10, then work through **SQL-Interview-Questions.md** end to end.

Practice daily, write queries often, and think in sets rather than in loops.

---

*Compiled from: sqlnotes.pdf, sqlnotes2.pdf, sqlnotes3.pdf (handwritten class notes), sqlnotes4.pdf, sql350questions.pdf, ctesql.pdf (the CTE deep-dive, also present as file_63F0BA0C-2BD5-4C71-B6A9-A6689195148C.pdf — the two are identical), and the 10-page "SQL Complete Notes" screenshot series.*

*Part 6 §39–40 (CTEs and Recursive CTEs) is drawn entirely from ctesql.pdf.*

---

# Appendix A — "SQL Complete Notes" handwritten one-pagers (7 pages)

*Transcribed 19 Sep 2026 from a 7-page handwritten summary series by Asif Ali Quraishi, shared publicly on LinkedIn. Kept verbatim as a compact revision sheet — it overlaps §1–40 above but is denser and carries its own interview questions and practice queries. Where it contradicts the main notes, the main notes win.*

## A.1 — SQL Basics (page 1)

**What is a Database?**
A Database is an organized collection of data so that it can be easily accessed, managed and updated. Like a digital filing cabinet where data is stored.

**What is DBMS?**
DBMS (Database Management System) is software that helps to create, store, manage and retrieve data from a database.

Examples: MySQL · PostgreSQL · Oracle · SQL Server · SQLite

**What is RDBMS?**
RDBMS (Relational Database Management System) is a type of DBMS that stores data in the form of tables (rows and columns) and the data in tables are related to each other.
Examples: MySQL, PostgreSQL, Oracle, SQL Server, etc.

**What is SQL?**
SQL (Structured Query Language) is a standard language used to communicate with databases. It is used to perform operations like creating, reading, updating and deleting data.

**SQL vs MySQL**

| SQL | MySQL |
|---|---|
| SQL is a language | MySQL is a database management system |
| It is used to communicate with databases | It is an open-source RDBMS |
| Example: SELECT, INSERT, UPDATE, DELETE | It uses SQL language to manage data |

> Remember: "SQL is the language, MySQL is the software that uses SQL."

**Example Table: Employee**

| ID | Name | Age | Dept | Salary |
|---|---|---|---|---|
| 1 | Abhi | 22 | IT | 50000 |
| 2 | Ravi | 23 | HR | 45000 |
| 3 | Sita | 21 | IT | 52000 |

**SQL Command Types**
1. DDL — Data Definition Language
2. DML — Data Manipulation Language
3. DCL — Data Control Language
4. TCL — Transaction Control Language
5. DQL — Data Query Language

**Database → Table → Row → Column**
Database → Table → Row (one record) → Column (one field)

## A.2 — DDL & DML Commands (page 2)

These are the basic SQL commands used to create, modify and manage data in a database.

**1. CREATE (DDL)** — Used to create Database and Table.
```sql
CREATE TABLE table_name (
  column1 datatype,
  column2 datatype,
  ...
);

CREATE TABLE Student (
  id INT,
  name VARCHAR(50),
  age INT,
  course VARCHAR(50)
);
```

**2. ALTER (DDL)** — Used to modify existing table structure.
```sql
ALTER TABLE table_name ADD column_name datatype;
ALTER TABLE table_name MODIFY column_name datatype;
ALTER TABLE table_name DROP COLUMN column_name;

ALTER TABLE Student ADD email VARCHAR(50);
ALTER TABLE Student MODIFY age INT;
ALTER TABLE Student DROP COLUMN email;
```

**3. DROP (DDL)** — Used to delete the table permanently.
```sql
DROP TABLE table_name;
DROP TABLE Student;
```
> Once table is dropped, data cannot be recovered.

**4. TRUNCATE (DDL)** — Used to remove all records from table but structure remains.
```sql
TRUNCATE TABLE table_name;
TRUNCATE TABLE Student;
```
> Faster than DELETE because it does not log individual rows.

**5. INSERT (DML)** — Used to insert new data into table.
```sql
INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2, ...);
INSERT INTO Student (id, name, age, course) VALUES (1, 'Abhi', 22, 'CSE');
```

**6. UPDATE (DML)** — Used to update existing data in table.
```sql
UPDATE table_name SET column_name = value WHERE condition;
UPDATE Student SET age = 23 WHERE id = 1;
```

**7. DELETE (DML)** — Used to delete specific records from table.
```sql
DELETE FROM table_name WHERE condition;
DELETE FROM Student WHERE id = 1;
```
> Without WHERE it will delete all records.

**8. SELECT (DQL)** — Used to retrieve data from table.
```sql
SELECT column1, column2, ... FROM table_name WHERE condition;
SELECT * FROM Student;
SELECT name, age FROM Student WHERE age > 20;
```

**DELETE vs TRUNCATE vs DROP**

| Feature | DELETE | TRUNCATE | DROP |
|---|---|---|---|
| Removes Data | Yes | Yes | Yes (Table) |
| Table Structure | Remains | Remains | Removed |
| Rollback | Yes | No | No |
| Speed | Slow | Fast | Fast |
| Where clause | Yes | No | No |

**Key Points**
- DDL → Structure related commands
- DML → Data related commands
- Always end command with `;`
- SQL keywords are usually in UPPERCASE

**Tip to Remember**
CREATE → Makes · ALTER → Changes · DROP → Deletes · TRUNCATE → Empties · CRUD → Insert, Update, Delete, Read (Select)

**Interview Questions**
1. What is the difference between DROP, TRUNCATE and DELETE?
2. What is the difference between DDL, DML, DCL, TCL and DQL?
3. How will you add a new column in existing table?
4. Can we rollback after TRUNCATE command? Why or why not?

## A.3 — Filtering Data (page 3)

Filtering helps us to retrieve specific data from the table based on certain conditions.

| # | Topic | Description | Syntax | Example |
|---|---|---|---|---|
| 1 | WHERE | Used to filter records based on a condition. (It is used before GROUP BY) | `SELECT column1, column2 FROM table_name WHERE condition;` | Find employees from IT dept. `SELECT * FROM Employee WHERE Dept = 'IT';` |
| 2 | ORDER BY | Used to sort the result set in ascending (ASC) or descending (DESC) order. | `SELECT column1, column2 FROM table_name ORDER BY column1 ASC\|DESC;` | Show employees by salary (high to low). `SELECT * FROM Employee ORDER BY Salary DESC;` |
| 3 | DISTINCT | Used to return only unique (different) values. | `SELECT DISTINCT column_name FROM table_name;` | Get unique departments. `SELECT DISTINCT Dept FROM Employee;` |
| 4 | LIMIT | Used to limit the number of rows returned. | `SELECT column1, column2 FROM table_name LIMIT number;` | Show first 5 employees. `SELECT * FROM Employee LIMIT 5;` |
| 5 | BETWEEN | Used to filter values within a range. | `SELECT column1, column2 FROM table_name WHERE column BETWEEN value1 AND value2;` | Employees with salary between 30000 and 60000. `SELECT * FROM Employee WHERE Salary BETWEEN 30000 AND 60000;` |
| 6 | IN | Used to filter records where the value matches any value in a list. | `SELECT column1, column2 FROM table_name WHERE column IN (value1, value2, ...);` | Employees from IT, HR, Sales. `SELECT * FROM Employee WHERE Dept IN ('IT','HR','Sales');` |
| 7 | LIKE | Used to search for a specified pattern in a column. | `SELECT column1 FROM table_name WHERE column LIKE pattern;` | Names starting with 'A'. `SELECT * FROM Employee WHERE Name LIKE 'A%';` |
| 8 | IS NULL | Used to filter records with NULL values. | `SELECT column1 FROM table_name WHERE column IS NULL;` | Employees with no manager assigned. `SELECT * FROM Employee WHERE ManagerID IS NULL;` |
| 9 | ALIASES (AS) | Used to give a temporary name to a column or table. | `SELECT column_name AS alias_name FROM table_name AS alias_name;` | Show name and salary with alias. `SELECT Name AS Emp_Name, Salary AS Emp_Salary FROM Employee;` |

**LIKE wildcards:** `%` → any number of characters · `_` → single character

**Tip to Remember**
- WHERE filters rows **before** grouping.
- ORDER BY sorts the **final** result.

**Practice Queries**
1. Get all employees from the 'HR' department.
2. Get all employees earning more than 50000.
3. Get the names of employees in ascending order.
4. Get the top 3 highest paid employees.
5. Get employees with salary between 30000 and 60000.
6. Get employees from 'IT' and 'Sales' departments.
7. Get employees whose name starts with 'S'.
8. Get employees who have no manager assigned.
9. Show unique departments.
10. Show name and age of all employees using alias.

## A.4 — SQL Functions (page 4)

Functions are predefined formulas in SQL that perform specific operations and return a value.

**A. Aggregate Functions** (work on multiple rows and return a single value)

| Function | Description | Syntax | Example | Result |
|---|---|---|---|---|
| `COUNT()` | Counts number of rows | `SELECT COUNT(column) FROM table;` | `SELECT COUNT(*) FROM Employee;` | Total number of employees |
| `SUM()` | Returns sum of numeric values | `SELECT SUM(column) FROM table;` | `SELECT SUM(Salary) FROM Employee;` | Total Salary |
| `AVG()` | Returns average of numeric values | `SELECT AVG(column) FROM table;` | `SELECT AVG(Salary) FROM Employee;` | Average Salary |
| `MAX()` | Returns maximum value | `SELECT MAX(column) FROM table;` | `SELECT MAX(Salary) FROM Employee;` | Highest Salary |
| `MIN()` | Returns minimum value | `SELECT MIN(column) FROM table;` | `SELECT MIN(Salary) FROM Employee;` | Lowest Salary |

**B. String Functions**

| Function | Description | Syntax | Example | Result |
|---|---|---|---|---|
| `UPPER()` | Converts string to upper case | `SELECT UPPER(column) FROM table;` | `SELECT UPPER(Name) FROM Employee;` | ABHISHEK |
| `LOWER()` | Converts string to lower case | `SELECT LOWER(column) FROM table;` | `SELECT LOWER(Name) FROM Employee;` | abhishek |
| `LENGTH()` | Returns length of string | `SELECT LENGTH(column) FROM table;` | `SELECT LENGTH(Name) FROM Employee;` | 8 |
| `CONCAT()` | Joins two or more strings | `SELECT CONCAT(col1, col2) FROM table;` | `SELECT CONCAT(FirstName, ' ', LastName) FROM Employee;` | Abhishek Kumar |
| `SUBSTRING()` | Extracts part of string | `SELECT SUBSTRING(column, start, length) FROM table;` | `SELECT SUBSTRING(Name, 1, 5) FROM Employee;` | Abhis |

**C. Numeric Functions**

| Function | Description | Syntax | Example | Result |
|---|---|---|---|---|
| `ROUND()` | Rounds a number to given digits | `SELECT ROUND(column, n) FROM table;` | `SELECT ROUND(123.456, 1);` | 123.46 |
| `CEIL()` | Rounds up to nearest integer | `SELECT CEIL(column) FROM table;` | `SELECT CEIL(45.2);` | 46 |
| `FLOOR()` | Rounds down to nearest integer | `SELECT FLOOR(column) FROM table;` | `SELECT FLOOR(45.8);` | 45 |

**D. Date Functions**

| Function | Description | Syntax | Example | Result |
|---|---|---|---|---|
| `NOW()` | Returns current date & time | `SELECT NOW();` | `SELECT NOW();` | 2025-05-28 14:30:15 |
| `CURDATE()` | Returns current date | `SELECT CURDATE();` | `SELECT CURDATE();` | 2025-05-28 |
| `DATEDIFF()` | Returns difference between two dates (in days) | `SELECT DATEDIFF(date1, date2);` | `SELECT DATEDIFF('2025-05-28','2025-05-01');` | 27 |

**Key Points**
- Aggregate functions work on a set of rows and return a single value.
- String functions work with text (character) data.
- Numeric functions work with numbers.
- Date functions work with date and time values.
- These functions can be used in SELECT, WHERE, HAVING, ORDER BY etc.

**Quick Example**
```sql
SELECT UPPER(Name) AS Name,
       COUNT(*) AS Total_Employees,
       AVG(Salary) AS Avg_Salary
FROM Employee
WHERE Department = 'IT';
```

| Name | Total_Employees | Avg_Salary |
|---|---|---|
| ABHISHEK | 5 | 55000.00 |

**Interview Questions**
1. What is the difference between `COUNT(*)` and `COUNT(column)`?
2. What will be the result of `AVG()` on an empty table?
3. How does `DATEDIFF()` work?
4. What is the use of `CONCAT()` function?
5. Difference between `CEIL()` and `FLOOR()` with example.

## A.5 — GROUP BY & Joins (page 5)

**A. GROUP BY**
GROUP BY is used with aggregate functions to group rows that have the same values into summary rows.

```sql
SELECT column, Aggregate_Function(column)
FROM table_name
GROUP BY column;
```

Example:
```sql
SELECT Dept, COUNT(*) FROM Employee GROUP BY Dept;
```

| Dept | COUNT(*) |
|---|---|
| IT | 3 |
| HR | 2 |
| Sales | 2 |

**B. HAVING**
HAVING is used to filter groups created by GROUP BY.

```sql
SELECT column, Aggregate_Function(column)
FROM table_name
GROUP BY column
HAVING condition;
```

Example:
```sql
SELECT Dept, COUNT(*) FROM Employee GROUP BY Dept HAVING COUNT(*) > 2;
```

| Dept | COUNT(*) |
|---|---|
| IT | 3 |

**Key Points**
- GROUP BY groups rows.
- Aggregate functions work with GROUP BY.
- WHERE filters rows **before** grouping.
- HAVING filters groups **after** grouping.
- WHERE → Row level filter · HAVING → Group level filter

**C. JOINS** (used to combine rows from two or more tables based on a related column)

| Type | Description | Syntax | Example |
|---|---|---|---|
| **1. INNER JOIN** | Returns only the matching rows from both tables. | `SELECT * FROM A INNER JOIN B ON A.id = B.id;` | `SELECT * FROM Employee e INNER JOIN Department d ON e.dept_id = d.id;` |
| **2. LEFT JOIN** (LEFT OUTER JOIN) | Returns all rows from left table (A) and matching rows from right table (B). If no match, NULLs. | `SELECT * FROM A LEFT JOIN B ON A.id = B.id;` | `SELECT * FROM Employee e LEFT JOIN Department d ON e.dept_id = d.id;` |
| **3. RIGHT JOIN** (RIGHT OUTER JOIN) | Returns all rows from right table (B) and matching rows from left table (A). If no match, NULLs. | `SELECT * FROM A RIGHT JOIN B ON A.id = B.id;` | `SELECT * FROM Employee e RIGHT JOIN Department d ON e.dept_id = d.id;` |
| **4. FULL OUTER JOIN** | Returns all rows when there is a match in either left (A) or right (B) table. If no match, NULLs. | `SELECT * FROM A FULL OUTER JOIN B ON A.id = B.id;` | (Not supported in MySQL. Use LEFT JOIN + RIGHT JOIN with UNION.) |
| **5. SELF JOIN** | A table joined with itself. | `SELECT a.col1, b.col2 FROM TableA a JOIN TableA b ON a.id = b.manager_id;` | `SELECT e1.name, e2.name FROM Employee e1 JOIN Employee e2 ON e1.manager_id = e2.id;` |
| **6. CROSS JOIN** (CARTESIAN JOIN) | Returns the Cartesian product of both tables. Every row from A is combined with every row from B. | `SELECT * FROM A CROSS JOIN B;` | `SELECT * FROM Employee CROSS JOIN Department;` |

**Practice Query**
Find the department name and number of employees in each department where the number of employees is more than 2.
```sql
SELECT d.dept_name, COUNT(e.id) AS total_employees
FROM Department d
INNER JOIN Employee e ON d.id = e.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.id) > 2;
```

| dept_name | total_employees |
|---|---|
| IT | 3 |
| Sales | 4 |

**Interview Questions**
1. What is the difference between WHERE and HAVING?
2. Why can't we use aggregate functions in WHERE clause?
3. Write a query to find departments having more than 2 employees.
4. What is the difference between INNER JOIN and LEFT JOIN?
5. When would you use CROSS JOIN?

## A.6 — Constraints & Normalization (page 6)

**A. CONSTRAINTS**
Constraints are rules applied on table columns to ensure data accuracy and reliability.

| Constraint | Description | Syntax | Example |
|---|---|---|---|
| **PRIMARY KEY** | Uniquely identifies each row in a table. | `column_name DATA_TYPE PRIMARY KEY` | `id INT PRIMARY KEY` |
| **FOREIGN KEY** | Creates a link between two tables. | `column_name DATA_TYPE, FOREIGN KEY (ref_column) REFERENCES table_name` | `emp_id INT, FOREIGN KEY (dept_id) REFERENCES Department(id)` |
| **UNIQUE** | Ensures all values in a column are different. | `column_name DATA_TYPE UNIQUE` | `email VARCHAR(50) UNIQUE` |
| **NOT NULL** | Ensures a column cannot have NULL value. | `column_name DATA_TYPE NOT NULL` | `name VARCHAR(50) NOT NULL` |
| **CHECK** | Ensures values in a column satisfy a specific condition. | `CHECK (condition)` | `age INT CHECK (age >= 18)` |
| **DEFAULT** | Sets a default value for a column. | `column_name DATA_TYPE DEFAULT value` | `status VARCHAR(20) DEFAULT 'Active'` |

**Example Table with Constraints**
```sql
CREATE TABLE Student (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(50) UNIQUE,
  age INT CHECK (age >= 18),
  dept_id INT,
  status VARCHAR(50) DEFAULT 'Active',
  FOREIGN KEY (dept_id) REFERENCES Department(id)
);
```

Department (id PK, dept_name) ←FK— Student (id PK, name, email, age, dept_id FK, status)

**B. NORMALIZATION**
Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity.

| Normal Form | Description | Example (Before) | Example (After) |
|---|---|---|---|
| **1NF** (First Normal Form) | All values are atomic (indivisible). No repeating groups or arrays. | Not in 1NF: StudentID 1, Abhi, Subjects = "Maths, CS, DBMS" | In 1NF: three rows — (1, Abhi, Maths), (1, Abhi, CS), (1, Abhi, DBMS) |
| **2NF** (Second Normal Form) | Must be in 1NF. No partial dependency. Every non-key attribute must depend on the whole primary key. | Not in 2NF: OrderID, ProductID, ProductName, Qty, CustomerName in one table | In 2NF: Orders (OrderID, CustomerName) + OrderDetails (OrderID, ProductID, Qty) |
| **3NF** (Third Normal Form) | Must be in 2NF. No transitive dependency. Non-key attributes should not depend on another non-key attribute. | Not in 3NF: EmpID, EmpName, DeptID, DeptName in one table | In 3NF: Employee (EmpID, EmpName, DeptID) + Department (DeptID, DeptName) |
| **BCNF** (Boyce-Codd Normal Form) | Stronger than 3NF. For every functional dependency, the determinant must be a candidate key. | (Concept level) When 3NF is not enough, apply BCNF to handle complex cases. | (Concept level) Every determinant is a candidate key. |

**Key Points**
- 1NF → Remove repeating groups.
- 2NF → Remove partial dependency.
- 3NF → Remove transitive dependency.
- Normalization improves data integrity and reduces redundancy.

**Benefits of Normalization**
- Reduces data redundancy
- Improves data integrity
- Saves storage space
- Makes data easier to maintain

**Memory Tip**
1NF → Atomic Values · 2NF → Full Dependency · 3NF → No Transitive Dependency · BCNF → Stronger Version of 3NF

**Interview Questions**
1. What are constraints? Why are they used?
2. Difference between UNIQUE and PRIMARY KEY?
3. What is the difference between DELETE, DROP and TRUNCATE?
4. Explain 1NF, 2NF and 3NF with examples.
5. What is BCNF? When do we need it?

## A.7 — Subqueries & Set Operators (page 7)

**A. SUBQUERIES**
A subquery is a query inside another query. It is also called Inner Query or Nested Query.

| Type | Description | Syntax | Example |
|---|---|---|---|
| **1. SIMPLE SUBQUERY** | A subquery that returns a single value, used in WHERE clause. | `SELECT column FROM table WHERE column OP (SELECT column FROM table);` | `SELECT name FROM Employee WHERE salary > (SELECT AVG(salary) FROM Employee);` |
| **2. MULTI-ROW SUBQUERY** | Subquery returns multiple rows. Used with IN, NOT IN, ANY, ALL. | `SELECT column FROM table WHERE column IN (SELECT column FROM table);` | `SELECT name FROM Employee WHERE dept_id IN (SELECT dept_id FROM Department);` |
| **3. CORRELATED SUBQUERY** | Subquery depends on the outer query. It runs once for each row of outer query. | `SELECT column FROM table t1 WHERE column OP (SELECT column FROM table t2 WHERE t1.col = t2.col);` | `SELECT name FROM Employee e WHERE salary > (SELECT AVG(salary) FROM Employee WHERE dept_id = e.dept_id);` |
| **4. EXISTS SUBQUERY** | Checks if subquery returns any rows. Returns TRUE or FALSE. | `SELECT column FROM table WHERE EXISTS (SELECT 1 FROM table2 WHERE condition);` | `SELECT name FROM Employee e WHERE EXISTS (SELECT 1 FROM Department d WHERE d.dept_id = e.dept_id);` |
| **5. NOT EXISTS SUBQUERY** | Checks if subquery returns no rows. | `SELECT column FROM table WHERE NOT EXISTS (SELECT column FROM table2 WHERE condition);` | `SELECT name FROM Employee e WHERE NOT EXISTS (SELECT 1 FROM Department d WHERE d.dept_id = e.dept_id);` |

**B. SET OPERATORS**
Set operators are used to combine the result-set of two or more SELECT statements.

| Operator | Description | Syntax |
|---|---|---|
| **1. UNION** | Returns unique rows from both queries (removes duplicates). | `SELECT column FROM table1 UNION SELECT column FROM table2;` |
| **2. UNION ALL** | Returns all rows from both queries including duplicates. | `SELECT column FROM table1 UNION ALL SELECT column FROM table2;` |
| **3. INTERSECT** | Returns only the common rows from both queries. | `SELECT column FROM table1 INTERSECT SELECT column FROM table2;` |
| **4. EXCEPT (MINUS)** | Returns rows from the first query that are not in the second query. | `SELECT column FROM table1 EXCEPT SELECT column FROM table2;` |
| **5. EXCEPT ALL** | Returns all rows from first query that are not in second query, including duplicates. | `SELECT column FROM table1 EXCEPT ALL SELECT column FROM table2;` |

**Example for Set Operators**

Table A: (1, Apple) (2, Banana) (3, Mango) (4, Orange)
Table B: (3, Mango) (4, Orange) (5, Grapes)

| Operator | Result |
|---|---|
| UNION | Apple, Banana, Mango, Orange, Grapes |
| UNION ALL | Apple, Banana, Mango, Orange, Mango, Orange, Grapes |
| INTERSECT | Mango, Orange |
| EXCEPT (A − B) | Apple, Banana |
| EXCEPT ALL (A − B) | Apple, Banana |

**Key Points**
- Subqueries are used in SELECT, WHERE, HAVING clauses.
- Use IN when subquery returns multiple rows.
- EXISTS is generally faster than IN in some cases.
- Set operators require the same number of columns with compatible data types.

**Memory Tip**
Subqueries = Query inside Query · IN → Many values · EXISTS → Presence of any value · UNION → Combine results · INTERSECT → Common results

**Quick Practice**
Write queries using subqueries and set operators on the tables: `Employee(emp_id, name, dept_id, salary)`, `Department(dept_id, dept_name)`.
1. Employees earning more than average salary.
2. Departments having more than 3 employees.
3. Names of employees not in any department table.

---

# Appendix B — Data Engineering SQL

*Added 19 Sep 2026. Covers what §1–68 leaves out for pipeline work: upserts, deduplication, SCD Type 2, incremental loads, date spines, array/struct handling, data-quality assertions, and window-function performance at scale. Dialect differences are called out because standard SQL and Spark SQL diverge exactly where pipelines live.*

## B.0 — Schema used in this appendix

```sql
-- Bronze: raw append-only landing, duplicates expected, everything nullable
CREATE TABLE bronze_orders (
  order_id      BIGINT,
  customer_id   BIGINT,
  status        VARCHAR(20),
  amount        DECIMAL(12,2),
  currency      VARCHAR(3),
  updated_at    TIMESTAMP,
  _ingested_at  TIMESTAMP,
  _source_file  VARCHAR(500)
);

-- Silver: cleaned, deduplicated, one row per order_id
CREATE TABLE silver_orders (
  order_id      BIGINT PRIMARY KEY,
  customer_id   BIGINT NOT NULL,
  status        VARCHAR(20) NOT NULL,
  amount        DECIMAL(12,2),
  currency      VARCHAR(3),
  updated_at    TIMESTAMP NOT NULL,
  _loaded_at    TIMESTAMP
);

-- Silver dimension with history (SCD Type 2)
CREATE TABLE dim_customer (
  customer_sk   BIGINT,        -- surrogate key, unique per version
  customer_id   BIGINT,        -- natural/business key
  name          VARCHAR(100),
  tier          VARCHAR(20),
  country       VARCHAR(2),
  valid_from    TIMESTAMP,
  valid_to      TIMESTAMP,     -- NULL or 9999-12-31 for the current row
  is_current    BOOLEAN
);
```

The Bronze/Silver split is the reason most of this appendix exists: Bronze is appended to blindly, so every Silver load has to deduplicate, and every Silver table has to be idempotent — running the same load twice must not change the result.

## B.1 — Upsert: MERGE, ON CONFLICT, ON DUPLICATE KEY

The single most common write in a pipeline. Insert the row if the key is new, update it if the key exists.

**ANSI `MERGE`** (Oracle, SQL Server, Snowflake, Databricks/Delta, Postgres 15+):

```sql
MERGE INTO silver_orders AS t
USING staged_orders AS s
  ON t.order_id = s.order_id
WHEN MATCHED AND s.updated_at > t.updated_at THEN
  UPDATE SET status     = s.status,
             amount     = s.amount,
             currency   = s.currency,
             updated_at = s.updated_at,
             _loaded_at = CURRENT_TIMESTAMP
WHEN NOT MATCHED THEN
  INSERT (order_id, customer_id, status, amount, currency, updated_at, _loaded_at)
  VALUES (s.order_id, s.customer_id, s.status, s.amount, s.currency,
          s.updated_at, CURRENT_TIMESTAMP);
```

The `AND s.updated_at > t.updated_at` guard is not optional. Without it a late-arriving old record overwrites a newer one — the classic silent data-corruption bug in CDC pipelines.

**Postgres — `ON CONFLICT`** (the upsert, and what SWE interviews ask about):

```sql
INSERT INTO silver_orders (order_id, customer_id, status, amount, updated_at)
VALUES (101, 7, 'shipped', 250.00, '2026-09-19 10:00:00')
ON CONFLICT (order_id) DO UPDATE
  SET status     = EXCLUDED.status,
      amount     = EXCLUDED.amount,
      updated_at = EXCLUDED.updated_at
  WHERE EXCLUDED.updated_at > silver_orders.updated_at;
```

`EXCLUDED` is the pseudo-table holding the row that failed to insert. `ON CONFLICT DO NOTHING` is the idempotent-insert form — safe to re-run, no error on duplicates.

**MySQL:**
```sql
INSERT INTO silver_orders (order_id, status, amount)
VALUES (101, 'shipped', 250.00)
ON DUPLICATE KEY UPDATE
  status = VALUES(status),
  amount = VALUES(amount);
```

**Delta Lake / Databricks** — same as ANSI MERGE, plus deletes:
```sql
MERGE INTO silver_orders t
USING staged_orders s ON t.order_id = s.order_id
WHEN MATCHED AND s.op = 'D' THEN DELETE
WHEN MATCHED AND s.op = 'U' THEN UPDATE SET *
WHEN NOT MATCHED AND s.op != 'D' THEN INSERT *;
```
`UPDATE SET *` and `INSERT *` map columns by name — convenient, but they break silently when the source schema drifts. Spell the columns out in production.

**The trap that fails at runtime:** if the source contains two rows with the same key, `MERGE` errors with *"cannot perform merge as multiple source rows matched"*. Deduplicate the source first — which is B.2.

## B.2 — Deduplication: the most-used query in data engineering

Bronze is append-only, so the same order arrives many times. Keep the latest version per key.

```sql
-- The pattern, in standard SQL
SELECT order_id, customer_id, status, amount, updated_at
FROM (
  SELECT *,
         ROW_NUMBER() OVER (
           PARTITION BY order_id
           ORDER BY updated_at DESC, _ingested_at DESC
         ) AS rn
  FROM bronze_orders
) x
WHERE rn = 1;
```

Memorise this shape. `PARTITION BY` the business key, `ORDER BY` the recency column descending, keep `rn = 1`.

**Why `ROW_NUMBER` and not `RANK`:** `RANK` gives ties the same number, so two rows updated at the same instant both come back as `1` and the duplicate survives. `ROW_NUMBER` always produces exactly one winner. Add a deterministic tiebreaker (`_ingested_at`, `_source_file`) so re-running the job picks the same row — otherwise the pipeline isn't reproducible.

**`QUALIFY`** — filters on a window function without the wrapping subquery. Snowflake, Databricks, DuckDB, BigQuery, Teradata:

```sql
SELECT order_id, customer_id, status, amount, updated_at
FROM bronze_orders
QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) = 1;
```

Same plan, half the code. Not available in Postgres or MySQL.

**`DISTINCT ON`** — Postgres's shorthand for latest-per-group:
```sql
SELECT DISTINCT ON (order_id) order_id, customer_id, status, amount, updated_at
FROM bronze_orders
ORDER BY order_id, updated_at DESC;
```
The `ORDER BY` must start with the `DISTINCT ON` columns. Often faster than the window version because it can stop at the first row per group.

**Exact-duplicate removal** (whole row identical, no recency column):
```sql
SELECT DISTINCT * FROM bronze_orders;
-- or, keeping one of each key regardless of which:
SELECT * FROM bronze_orders GROUP BY order_id;  -- Spark/MySQL only; not ANSI
```

**Finding duplicates before deciding what to do about them:**
```sql
SELECT order_id, COUNT(*) AS n
FROM bronze_orders
GROUP BY order_id
HAVING COUNT(*) > 1
ORDER BY n DESC;
```

## B.3 — Slowly Changing Dimensions, Type 2

A customer's tier changes from Silver to Gold. Type 1 overwrites and loses history. **Type 2 closes the old row and inserts a new one**, so a fact joined on the order date sees the tier that applied *at that time*.

```sql
-- Step 1: close rows whose tracked attributes changed
MERGE INTO dim_customer t
USING staged_customers s
  ON t.customer_id = s.customer_id
 AND t.is_current = TRUE
WHEN MATCHED AND (
       t.tier    IS DISTINCT FROM s.tier
    OR t.country IS DISTINCT FROM s.country
    OR t.name    IS DISTINCT FROM s.name
  ) THEN UPDATE SET
       valid_to   = s.effective_at,
       is_current = FALSE;

-- Step 2: insert the new current version
INSERT INTO dim_customer
  (customer_sk, customer_id, name, tier, country, valid_from, valid_to, is_current)
SELECT
  hash(s.customer_id, s.effective_at),  -- or a sequence / identity column
  s.customer_id, s.name, s.tier, s.country,
  s.effective_at, TIMESTAMP '9999-12-31 00:00:00', TRUE
FROM staged_customers s
LEFT JOIN dim_customer d
       ON d.customer_id = s.customer_id AND d.is_current = TRUE
WHERE d.customer_id IS NULL              -- brand new customer
   OR d.tier    IS DISTINCT FROM s.tier  -- or an attribute changed
   OR d.country IS DISTINCT FROM s.country
   OR d.name    IS DISTINCT FROM s.name;
```

**`IS DISTINCT FROM` is the whole trick.** Plain `<>` returns NULL when either side is NULL, so a change from `NULL` to `'Gold'` is *not* detected and the history silently breaks. `IS DISTINCT FROM` treats NULL as a comparable value: `NULL IS DISTINCT FROM 'Gold'` is TRUE, `NULL IS DISTINCT FROM NULL` is FALSE. MySQL spells it `<=>` (null-safe equal, so negate it); Spark supports `<=>` and `IS DISTINCT FROM`.

**Querying a Type 2 dimension** — join on the key *and* the validity window:
```sql
SELECT o.order_id, o.amount, d.tier AS tier_at_order_time
FROM silver_orders o
JOIN dim_customer d
  ON d.customer_id = o.customer_id
 AND o.updated_at >= d.valid_from
 AND o.updated_at <  d.valid_to;
```

Use `9999-12-31` rather than `NULL` for the open end. It makes the `<` comparison work without a `COALESCE`, and it lets the optimiser use a range predicate.

**Type 1 vs 2 vs 3, for the interview:** Type 1 overwrites, no history. Type 2 adds a row per version, full history, the dimension grows. Type 3 adds a *column* (`previous_tier`), one step of history only.

## B.4 — Incremental loads and watermarks

Never rescan the whole source. Load only what changed since the last successful run.

```sql
-- Read the high-water mark from the control table
SELECT COALESCE(MAX(watermark), TIMESTAMP '1900-01-01')
FROM etl_control
WHERE table_name = 'silver_orders';

-- Pull only new/changed source rows
SELECT * FROM bronze_orders
WHERE updated_at > :last_watermark
  AND updated_at <= :run_started_at;   -- upper bound, see below

-- After a successful load, advance it
UPDATE etl_control
SET watermark = :run_started_at, updated_at = CURRENT_TIMESTAMP
WHERE table_name = 'silver_orders';
```

Three rules that prevent real incidents:

1. **Bound both ends.** Without the upper bound, rows written *during* the run get consumed but the watermark advances past them only if they happened to land before the read — so some are processed twice and, worse, the boundary is non-deterministic.
2. **Use `>` on the lower bound and `<=` on the upper**, consistently, or rows exactly on the boundary are processed twice or never.
3. **Advance the watermark only after the write commits.** If the load fails mid-way, the next run must re-read the same window. This is why the whole load should be one transaction, or the target write idempotent (which is what B.1's MERGE gives you).

**Late-arriving data** breaks watermarks by definition — a row with `updated_at` older than the watermark never gets picked up. The usual mitigation is a lookback window:
```sql
WHERE updated_at > :last_watermark - INTERVAL '3' DAY
```
and an idempotent MERGE, so reprocessing the overlap is harmless.

**Partition-based incremental** (typical over Parquet/Delta on S3):
```sql
SELECT * FROM bronze_orders
WHERE event_date >= DATE '2026-09-01'
  AND event_date <  DATE '2026-09-20';
```
Filter on the *partition column* with a literal range. A function on the column (`WHERE YEAR(event_date) = 2026`) kills partition pruning — the engine reads every file.

## B.5 — Date spines and gap filling

A `GROUP BY` over event data returns no row for days with zero events. Reports need the zero.

**Postgres / DuckDB:**
```sql
SELECT d::date AS day
FROM generate_series(DATE '2026-09-01', DATE '2026-09-30', INTERVAL '1 day') AS d;
```

**Spark SQL / Databricks:**
```sql
SELECT explode(sequence(DATE '2026-09-01', DATE '2026-09-30', INTERVAL 1 DAY)) AS day;
```

**Snowflake / BigQuery:**
```sql
-- Snowflake
SELECT DATEADD(day, SEQ4(), DATE '2026-09-01') AS day
FROM TABLE(GENERATOR(ROWCOUNT => 30));
-- BigQuery
SELECT day FROM UNNEST(GENERATE_DATE_ARRAY('2026-09-01','2026-09-30')) AS day;
```

**ANSI fallback — a recursive CTE** (works everywhere that supports §40):
```sql
WITH RECURSIVE spine (day) AS (
  SELECT DATE '2026-09-01'
  UNION ALL
  SELECT day + INTERVAL '1' DAY FROM spine WHERE day < DATE '2026-09-30'
)
SELECT day FROM spine;
```

**Putting it to work — daily revenue with zeros:**
```sql
WITH spine AS (
  SELECT d::date AS day
  FROM generate_series(DATE '2026-09-01', DATE '2026-09-30', INTERVAL '1 day') AS d
)
SELECT s.day,
       COALESCE(SUM(o.amount), 0) AS revenue,
       COUNT(o.order_id)          AS order_count
FROM spine s
LEFT JOIN silver_orders o
       ON DATE_TRUNC('day', o.updated_at) = s.day
GROUP BY s.day
ORDER BY s.day;
```

The spine must be on the **left** of the LEFT JOIN. Reversing it drops the empty days again — the mistake that makes this pattern look like it doesn't work.

**Forward-fill a sparse series** (carry the last known value into gaps):
```sql
SELECT day,
       COALESCE(price,
                LAST_VALUE(price IGNORE NULLS) OVER (
                  ORDER BY day ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
       ) AS price_filled
FROM spine LEFT JOIN prices USING (day);
```
`IGNORE NULLS` is the key clause — supported in Spark, Snowflake, Oracle, BigQuery, DuckDB; not in Postgres, where you fake it with a grouped running `MAX` over a partition built from a running `COUNT(price)`.

## B.6 — NULL ordering, and why it bites

```sql
SELECT order_id, amount FROM silver_orders ORDER BY amount DESC;
```

Where do the NULL amounts go? **It depends on the engine**, and the default differs:

| Engine | Default for `ORDER BY col ASC` | `DESC` |
|---|---|---|
| Postgres, Oracle | NULLs **last** | NULLs **first** |
| MySQL, SQLite, SQL Server | NULLs **first** | NULLs **last** |
| Spark SQL, Databricks | NULLs **first** | NULLs **last** |
| Snowflake | NULLs **last** | NULLs **first** |

So "top 10 by amount" can silently return ten NULL rows on some engines and none on others. Be explicit:

```sql
SELECT order_id, amount
FROM silver_orders
ORDER BY amount DESC NULLS LAST
LIMIT 10;
```

`NULLS FIRST` / `NULLS LAST` work in Postgres, Oracle, Spark, Snowflake, DuckDB, SQLite 3.30+. MySQL and SQL Server don't support the clause — emulate it:
```sql
ORDER BY (amount IS NULL), amount DESC;   -- MySQL: FALSE(0) sorts before TRUE(1)
ORDER BY CASE WHEN amount IS NULL THEN 1 ELSE 0 END, amount DESC;  -- portable
```

This matters most inside `ROW_NUMBER() OVER (... ORDER BY updated_at DESC)` in B.2: a NULL `updated_at` can win the deduplication and become your Silver row.

## B.7 — Aggregating into strings and arrays

```sql
-- Postgres, Snowflake, SQL Server 2017+, DuckDB
SELECT customer_id, STRING_AGG(status, ',' ORDER BY updated_at) AS status_path
FROM silver_orders GROUP BY customer_id;

-- MySQL
SELECT customer_id, GROUP_CONCAT(status ORDER BY updated_at SEPARATOR ',')
FROM silver_orders GROUP BY customer_id;

-- Spark SQL / Databricks
SELECT customer_id, concat_ws(',', collect_list(status)) AS status_path
FROM silver_orders GROUP BY customer_id;
```

`GROUP_CONCAT` silently truncates at `group_concat_max_len` (default 1024 bytes in MySQL) — a genuinely nasty source of quiet data loss.

**Arrays:**
```sql
-- Postgres / DuckDB
SELECT customer_id, ARRAY_AGG(DISTINCT status) AS statuses FROM silver_orders GROUP BY customer_id;
-- Spark
SELECT customer_id, collect_set(status) AS statuses FROM silver_orders GROUP BY customer_id;
```
`collect_set` deduplicates, `collect_list` keeps order and duplicates. Neither guarantees ordering without an explicit sort — `sort_array(collect_list(x))`.

**Exploding nested data** — the Bronze→Silver flattening step:
```sql
-- Spark SQL: one row per array element
SELECT order_id, item.sku, item.qty
FROM bronze_orders
LATERAL VIEW explode(line_items) AS item;

-- ANSI / Postgres equivalent
SELECT order_id, item->>'sku' AS sku
FROM bronze_orders, LATERAL jsonb_array_elements(line_items) AS item;
```
`explode` drops rows whose array is empty or NULL; `explode_outer` keeps them with a NULL — the difference silently changes your row count. See §34 for LATERAL.

**Higher-order functions** (Spark SQL, Databricks, Snowflake) — operate on arrays without exploding:
```sql
SELECT order_id,
       transform(line_items, x -> x.qty * x.price)          AS line_totals,
       filter(line_items,   x -> x.qty > 1)                 AS multi_qty,
       aggregate(line_items, 0D, (acc, x) -> acc + x.price) AS order_total
FROM bronze_orders;
```
Far cheaper than explode-then-regroup, because it never expands the row count.

## B.8 — Regular expressions

```sql
-- Match
SELECT * FROM bronze_orders WHERE currency ~ '^[A-Z]{3}$';          -- Postgres
SELECT * FROM bronze_orders WHERE currency REGEXP '^[A-Z]{3}$';      -- MySQL, Spark
SELECT * FROM bronze_orders WHERE RLIKE(currency, '^[A-Z]{3}$');     -- Spark, Snowflake

-- Extract
SELECT REGEXP_SUBSTR(_source_file, '[0-9]{4}-[0-9]{2}-[0-9]{2}') AS file_date FROM bronze_orders;
SELECT regexp_extract(_source_file, '(\\d{4}-\\d{2}-\\d{2})', 1)   AS file_date FROM bronze_orders;  -- Spark

-- Replace
SELECT REGEXP_REPLACE(phone, '[^0-9]', '', 'g') AS digits_only FROM customers;  -- Postgres 'g' = global
```

Two practical notes. Backslashes usually need doubling in string literals (`\\d`), and Spark uses Java regex semantics while Postgres uses POSIX — character classes like `\d` and `\w` work in both, but lookbehind support and lazy quantifiers differ.

Regex is the right tool for validation in a quality check; it's the wrong tool for parsing structured formats — use the JSON functions (§55) or a proper parser upstream.

## B.9 — GROUPING SETS, ROLLUP, CUBE

One pass, multiple aggregation levels. The alternative is several queries stitched with `UNION ALL`, which rescans the table each time.

```sql
-- Subtotals by country, by country+tier, and a grand total
SELECT country, tier, SUM(amount) AS revenue
FROM silver_orders o JOIN dim_customer d USING (customer_id)
GROUP BY ROLLUP (country, tier);
```

`ROLLUP (a, b)` gives `(a,b)`, `(a)`, `()` — a hierarchy. `CUBE (a, b)` gives every combination: `(a,b)`, `(a)`, `(b)`, `()`. `GROUPING SETS` lets you name exactly the ones you want:

```sql
GROUP BY GROUPING SETS ((country, tier), (country), ());
```

Subtotal rows carry NULL in the rolled-up columns, which is ambiguous when the data itself contains NULLs. `GROUPING()` disambiguates — it returns 1 for a subtotal placeholder, 0 for a real value:

```sql
SELECT CASE WHEN GROUPING(country) = 1 THEN 'ALL COUNTRIES' ELSE country END AS country,
       CASE WHEN GROUPING(tier) = 1    THEN 'ALL TIERS'     ELSE tier    END AS tier,
       SUM(amount) AS revenue
FROM silver_orders o JOIN dim_customer d USING (customer_id)
GROUP BY ROLLUP (country, tier);
```

Supported in Postgres, Spark, Snowflake, Oracle, SQL Server, DuckDB. MySQL has `WITH ROLLUP` only.

## B.10 — Data-quality assertions as SQL

Every check returns rows only when something is wrong, so "zero rows" means "pass". This is the shape behind DLT expectations, dbt tests and Great Expectations.

```sql
-- 1. Primary key is actually unique
SELECT order_id, COUNT(*) AS n FROM silver_orders GROUP BY order_id HAVING COUNT(*) > 1;

-- 2. No NULLs in required columns
SELECT COUNT(*) AS null_customer_ids FROM silver_orders WHERE customer_id IS NULL HAVING COUNT(*) > 0;

-- 3. Referential integrity (the anti-join from §34)
SELECT o.order_id, o.customer_id
FROM silver_orders o
LEFT JOIN dim_customer d ON d.customer_id = o.customer_id AND d.is_current = TRUE
WHERE d.customer_id IS NULL;

-- 4. Row count did not collapse vs the previous run
SELECT :today_count AS today, :yesterday_count AS yesterday
WHERE :today_count < :yesterday_count * 0.9;

-- 5. Domain / range checks
SELECT * FROM silver_orders
WHERE amount < 0
   OR status NOT IN ('pending','shipped','delivered','cancelled')
   OR updated_at > CURRENT_TIMESTAMP;

-- 6. SCD2 integrity: exactly one current row per key, and no overlapping windows
SELECT customer_id, COUNT(*) AS current_rows
FROM dim_customer WHERE is_current = TRUE
GROUP BY customer_id HAVING COUNT(*) > 1;

SELECT a.customer_id, a.valid_from, a.valid_to, b.valid_from, b.valid_to
FROM dim_customer a JOIN dim_customer b
  ON a.customer_id = b.customer_id
 AND a.customer_sk <> b.customer_sk
 AND a.valid_from < b.valid_to
 AND b.valid_from < a.valid_to;   -- any row returned = overlapping history
```

**A profiling query** worth keeping — null rates and cardinality for a whole table in one pass:
```sql
SELECT COUNT(*)                                                   AS rows,
       COUNT(customer_id)                                         AS non_null_customer,
       1.0 - COUNT(amount) * 1.0 / COUNT(*)                       AS amount_null_rate,
       COUNT(DISTINCT customer_id)                                AS distinct_customers,
       MIN(updated_at)                                            AS min_ts,
       MAX(updated_at)                                            AS max_ts,
       APPROX_COUNT_DISTINCT(order_id)                            AS approx_orders
FROM silver_orders;
```
`APPROX_COUNT_DISTINCT` (HyperLogLog) is dramatically cheaper than `COUNT(DISTINCT ...)` on large tables and is accurate to ~2% — fine for monitoring, not for billing.

## B.11 — Window functions on large partitions

Where pipeline queries actually fall over. A window function is fundamentally a **sort plus a scan**, and the cost is driven by partition size, not table size.

**What the engine does.** For `OVER (PARTITION BY k ORDER BY t)` it must group rows by `k` and order them by `t`. It does this by sorting (or hash-partitioning then sorting) the entire input on `(k, t)`, then walking each partition in one pass. So:

- **No `PARTITION BY` means one partition containing every row.** In Spark that is a single-task shuffle to one executor — the whole dataset on one machine. `ROW_NUMBER() OVER (ORDER BY ts)` over a billion rows is the classic OOM.
- **Skewed keys are the same problem, localised.** If 80% of rows share one `customer_id`, one task does 80% of the work while the rest idle. The job's runtime is that one task.
- **Partition count that is too high is also bad** — millions of tiny partitions means huge sort overhead and tiny per-task work.

**Diagnose skew before optimising:**
```sql
SELECT customer_id, COUNT(*) AS n
FROM silver_orders
GROUP BY customer_id
ORDER BY n DESC
LIMIT 20;
```
If the top key holds orders of magnitude more rows than the median, that's your skew.

**Seven things that actually help:**

**1. Filter before the window, not after.** The window runs over everything that reaches it.
```sql
-- Bad: sorts all history, then discards
SELECT * FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) rn
               FROM bronze_orders) x
WHERE rn = 1 AND updated_at >= DATE '2026-09-01';

-- Good: the predicate cuts the input first
SELECT * FROM (SELECT *, ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY updated_at DESC) rn
               FROM bronze_orders
               WHERE updated_at >= DATE '2026-09-01') x
WHERE rn = 1;
```
Optimisers push some predicates through a window, but **not** ones on the window's own output, and not reliably through `PARTITION BY` boundaries. Place the filter yourself.

**2. Project only the columns you need before the window.** The sort spills to disk at a size driven by row *width*. Dropping a wide JSON blob before the window can be the difference between in-memory and spilling.

**3. Reuse one window definition.** Multiple functions sharing an identical `OVER` clause are computed in a single sort; differing clauses each add a sort.
```sql
SELECT order_id,
       ROW_NUMBER() OVER w AS rn,
       LAG(amount)  OVER w AS prev_amount,
       SUM(amount)  OVER w AS running_total
FROM silver_orders
WINDOW w AS (PARTITION BY customer_id ORDER BY updated_at);
```
The named `WINDOW` clause (Postgres, Spark 3.x, DuckDB, Snowflake) makes the sharing explicit and the intent obvious.

**4. State the frame.** The default is `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`, and `RANGE` is slower than `ROWS` because it must look ahead for peer rows with equal `ORDER BY` values. Unless you need peer semantics:
```sql
SUM(amount) OVER (PARTITION BY customer_id ORDER BY updated_at
                  ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
```
`ROWS` is also the correct choice for a true running total — with `RANGE`, rows sharing a timestamp all get the same total, which is usually not what anyone wants.

**5. Prefer an aggregate to a window when you only need the aggregate.** `MAX(x) OVER (PARTITION BY k)` sorts; `GROUP BY k` can hash-aggregate, which is cheaper and parallelises cleanly. Use the window only when you need the per-row result alongside the detail.

**6. For deduplication specifically, consider the alternatives.** `DISTINCT ON` (Postgres) can short-circuit per group. An aggregate on a struct avoids the sort in Spark:
```sql
SELECT customer_id, max(struct(updated_at, order_id, amount)).* 
FROM bronze_orders GROUP BY customer_id;
```
`max` on a struct compares field by field, left to right — so this returns the whole row with the largest `updated_at`, using a hash aggregate instead of a sort.

**7. Handle skew explicitly when nothing else works.** Salt the key, aggregate, then combine:
```sql
WITH salted AS (
  SELECT *, CONCAT(customer_id, '-', CAST(FLOOR(RAND() * 16) AS INT)) AS salted_key
  FROM silver_orders
)
SELECT customer_id, SUM(partial) AS total
FROM (SELECT customer_id, SUM(amount) AS partial FROM salted GROUP BY salted_key, customer_id) x
GROUP BY customer_id;
```
On Databricks, check whether Adaptive Query Execution (`spark.sql.adaptive.skewJoin.enabled`) already handles it before hand-salting.

**Reading the plan.** In `EXPLAIN` output look for the `Window` / `WindowExec` operator and the `Sort` or `Exchange` directly beneath it. `Exchange hashpartitioning(customer_id, 200)` tells you the shuffle width; `Exchange SinglePartition` under a window is the red flag that means no `PARTITION BY`. In Postgres, `WindowAgg` over `Sort` with a large `Sort Method: external merge Disk: …` means it spilled — more `work_mem`, or fewer rows.

**Indexes help windows in row stores.** A btree on `(customer_id, updated_at DESC)` can supply rows already ordered, letting Postgres skip the sort entirely. This does not apply to Spark/Delta, where file layout is the equivalent lever: `ZORDER BY (customer_id)` co-locates a key's rows in fewer files, so a window over it reads less.

## B.12 — Bulk loading

```sql
-- Postgres: the fastest way in, by a wide margin
COPY silver_orders FROM '/data/orders.csv' WITH (FORMAT csv, HEADER true, NULL '');
COPY silver_orders TO   '/data/out.csv'    WITH (FORMAT csv, HEADER true);

-- DuckDB: reads Parquet/CSV/JSON directly, local or S3
CREATE TABLE silver_orders AS SELECT * FROM read_parquet('s3://bucket/orders/*.parquet');
COPY (SELECT * FROM silver_orders) TO 'out.parquet' (FORMAT parquet, COMPRESSION zstd);

-- Spark SQL / Databricks
CREATE TABLE silver_orders USING DELTA AS SELECT * FROM parquet.`s3://bucket/orders/`;
COPY INTO silver_orders FROM 's3://bucket/orders/' FILEFORMAT = PARQUET;

-- Snowflake
COPY INTO silver_orders FROM @my_stage/orders/ FILE_FORMAT = (TYPE = PARQUET);
```

`COPY INTO` in Databricks and Snowflake is **idempotent by file**: it tracks which files it has already ingested and skips them on re-run. That property is what makes it safe in a retrying scheduler, and it's the reason to prefer it over a plain `INSERT ... SELECT` over a path.

## B.13 — Delta Lake / Databricks specifics

Not ANSI SQL, but it's the dialect your pipelines run in.

```sql
-- Time travel
SELECT * FROM silver_orders VERSION AS OF 42;
SELECT * FROM silver_orders TIMESTAMP AS OF '2026-09-18T00:00:00';

-- What changed, and who changed it
DESCRIBE HISTORY silver_orders;

-- Restore after a bad load
RESTORE TABLE silver_orders TO VERSION AS OF 41;

-- File layout: compaction and co-location
OPTIMIZE silver_orders WHERE event_date >= '2026-09-01' ZORDER BY (customer_id);
VACUUM silver_orders RETAIN 168 HOURS;   -- deletes files older than the retention window

-- Change Data Feed — row-level changes between versions
SELECT * FROM table_changes('silver_orders', 41, 42);

-- Streaming table (DLT)
CREATE OR REFRESH STREAMING TABLE silver_orders
AS SELECT * FROM STREAM(LIVE.bronze_orders)
WHERE order_id IS NOT NULL;

-- DLT expectations — the quality checks of B.10, declared
CONSTRAINT valid_amount EXPECT (amount >= 0) ON VIOLATION DROP ROW
CONSTRAINT has_customer EXPECT (customer_id IS NOT NULL) ON VIOLATION FAIL UPDATE
```

`VACUUM` below the retention threshold breaks time travel and can break concurrent readers — the default 7 days exists for a reason.

## B.14 — Dialect quick reference

| Task | Postgres | MySQL | Spark / Databricks | Snowflake | DuckDB |
|---|---|---|---|---|---|
| Upsert | `ON CONFLICT` | `ON DUPLICATE KEY` | `MERGE INTO` | `MERGE INTO` | `ON CONFLICT` |
| Filter on window | subquery | subquery | `QUALIFY` | `QUALIFY` | `QUALIFY` |
| Latest per group | `DISTINCT ON` | window | `QUALIFY` / `max(struct)` | `QUALIFY` | `DISTINCT ON` |
| String agg | `STRING_AGG` | `GROUP_CONCAT` | `concat_ws`+`collect_list` | `LISTAGG` | `STRING_AGG` |
| Array agg | `ARRAY_AGG` | — (JSON) | `collect_list`/`collect_set` | `ARRAY_AGG` | `LIST` |
| Date series | `generate_series` | recursive CTE | `sequence`+`explode` | `GENERATOR` | `generate_series` |
| Null-safe compare | `IS DISTINCT FROM` | `<=>` | `<=>` | `IS DISTINCT FROM` | `IS DISTINCT FROM` |
| Null ordering | NULLs last (ASC) | NULLs first | NULLs first | NULLs last | NULLs last |
| Regex match | `~` | `REGEXP` | `RLIKE` | `RLIKE` | `REGEXP_MATCHES` |
| Approx distinct | — (`hll` ext) | — | `approx_count_distinct` | `APPROX_COUNT_DISTINCT` | `approx_count_distinct` |
| Median | `PERCENTILE_CONT` | — | `percentile_approx` | `MEDIAN` | `median` |

## B.15 — Interview questions this appendix answers

1. Write a query that keeps only the latest row per key from an append-only table. Why `ROW_NUMBER` and not `RANK`?
2. Your MERGE fails with "multiple source rows matched". What happened and how do you fix it?
3. Implement SCD Type 2. Why does `<>` break the change detection and what replaces it?
4. Design an incremental load. What are the two boundary conditions, and when do you advance the watermark?
5. How do you produce a daily report with zero-rows for days that had no events?
6. A window-function job OOMs on one executor. Give three possible causes and a fix for each.
7. What is the difference between `ROWS` and `RANGE` in a window frame? Which is the correct running total?
8. `ORDER BY amount DESC LIMIT 10` returns ten NULL rows. Explain and fix.
9. Write five data-quality assertions for a Silver table. What does "passing" look like?
10. How would you detect and handle key skew in a `GROUP BY` over a billion rows?
11. What makes `COPY INTO` safe to retry, and why is `INSERT ... SELECT` over a path not?
12. When is `COUNT(DISTINCT x)` the wrong choice, and what do you use instead?
