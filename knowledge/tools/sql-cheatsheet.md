# SQL Cheatsheet

Quick reference for SQL concepts - from basics to advanced.

---

## Basics

### SELECT
```sql
-- All columns
SELECT * FROM employees;

-- Specific columns
SELECT name, salary FROM employees;

-- With alias
SELECT name AS employee_name, salary AS annual_salary FROM employees;

-- Distinct values
SELECT DISTINCT department FROM employees;
```

### WHERE (Filtering)
```sql
-- Comparison operators
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM employees WHERE department = 'Engineering';
SELECT * FROM employees WHERE hire_date >= '2023-01-01';

-- Multiple conditions
SELECT * FROM employees WHERE salary > 50000 AND department = 'Engineering';
SELECT * FROM employees WHERE department = 'Engineering' OR department = 'Sales';
SELECT * FROM employees WHERE NOT department = 'HR';

-- IN and BETWEEN
SELECT * FROM employees WHERE department IN ('Engineering', 'Sales', 'Marketing');
SELECT * FROM employees WHERE salary BETWEEN 50000 AND 100000;

-- LIKE (pattern matching)
SELECT * FROM employees WHERE name LIKE 'J%';      -- Starts with J
SELECT * FROM employees WHERE name LIKE '%son';    -- Ends with son
SELECT * FROM employees WHERE name LIKE '%oh%';    -- Contains oh
SELECT * FROM employees WHERE name LIKE 'J___';    -- J followed by 3 chars

-- NULL handling
SELECT * FROM employees WHERE manager_id IS NULL;
SELECT * FROM employees WHERE manager_id IS NOT NULL;
```

### ORDER BY
```sql
-- Single column
SELECT * FROM employees ORDER BY salary;           -- Ascending (default)
SELECT * FROM employees ORDER BY salary DESC;      -- Descending

-- Multiple columns
SELECT * FROM employees ORDER BY department, salary DESC;
```

### LIMIT
```sql
-- First N rows
SELECT * FROM employees ORDER BY salary DESC LIMIT 10;

-- Skip rows (offset)
SELECT * FROM employees ORDER BY salary DESC LIMIT 10 OFFSET 20;
```

---

## Aggregations

### Basic Aggregate Functions
```sql
SELECT COUNT(*) FROM employees;                    -- Count all rows
SELECT COUNT(DISTINCT department) FROM employees;  -- Count unique values
SELECT SUM(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MIN(salary), MAX(salary) FROM employees;
```

### GROUP BY
```sql
-- Aggregate by group
SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;

SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
ORDER BY avg_salary DESC;
```

### HAVING (Filter Groups)
```sql
-- WHERE filters rows, HAVING filters groups
SELECT department, COUNT(*) AS count
FROM employees
GROUP BY department
HAVING COUNT(*) > 5;

SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;
```

---

## JOINs

### INNER JOIN (Matching rows only)
```sql
SELECT e.name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;
```

### LEFT JOIN (All left + matching right)
```sql
-- All employees, even without department
SELECT e.name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;
```

### RIGHT JOIN (All right + matching left)
```sql
-- All departments, even without employees
SELECT e.name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.id;
```

### FULL OUTER JOIN (All from both)
```sql
SELECT e.name, d.department_name
FROM employees e
FULL OUTER JOIN departments d ON e.department_id = d.id;
```

### Self JOIN
```sql
-- Employee with their manager's name
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;
```

### Multiple JOINs
```sql
SELECT e.name, d.department_name, s.amount AS salary
FROM employees e
JOIN departments d ON e.department_id = d.id
JOIN salaries s ON e.id = s.employee_id
WHERE s.end_date IS NULL;  -- Current salary
```

---

## Subqueries

### In WHERE clause
```sql
-- Employees earning more than average
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Employees in departments with > 10 people
SELECT name
FROM employees
WHERE department_id IN (
    SELECT department_id
    FROM employees
    GROUP BY department_id
    HAVING COUNT(*) > 10
);
```

### Correlated Subquery
```sql
-- Employees earning more than department average
SELECT name, salary, department_id
FROM employees e1
WHERE salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e2.department_id = e1.department_id
);
```

### In FROM clause (Derived Table)
```sql
SELECT dept_avg.department_id, dept_avg.avg_salary
FROM (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
) AS dept_avg
WHERE dept_avg.avg_salary > 70000;
```

---

## CTEs (Common Table Expressions)

### Basic CTE
```sql
WITH high_earners AS (
    SELECT * FROM employees WHERE salary > 100000
)
SELECT department, COUNT(*) AS count
FROM high_earners
GROUP BY department;
```

### Multiple CTEs
```sql
WITH
dept_stats AS (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
),
above_avg AS (
    SELECT e.*
    FROM employees e
    JOIN dept_stats d ON e.department_id = d.department_id
    WHERE e.salary > d.avg_salary
)
SELECT * FROM above_avg;
```

### Recursive CTE (Hierarchies)
```sql
-- Employee hierarchy (org chart)
WITH RECURSIVE org_chart AS (
    -- Base case: top-level (no manager)
    SELECT id, name, manager_id, 1 AS level
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive case
    SELECT e.id, e.name, e.manager_id, oc.level + 1
    FROM employees e
    JOIN org_chart oc ON e.manager_id = oc.id
)
SELECT * FROM org_chart ORDER BY level, name;
```

---

## Window Functions

### ROW_NUMBER, RANK, DENSE_RANK
```sql
-- Rank employees by salary within department
SELECT
    name,
    department,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS row_num,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dense_rank
FROM employees;
```

### LAG, LEAD (Previous/Next row)
```sql
-- Compare to previous month's value
SELECT
    month,
    revenue,
    LAG(revenue, 1) OVER (ORDER BY month) AS prev_month,
    revenue - LAG(revenue, 1) OVER (ORDER BY month) AS change
FROM monthly_sales;
```

### Running Totals
```sql
SELECT
    date,
    amount,
    SUM(amount) OVER (ORDER BY date) AS running_total
FROM transactions;

-- Running total per category
SELECT
    date,
    category,
    amount,
    SUM(amount) OVER (PARTITION BY category ORDER BY date) AS category_running_total
FROM transactions;
```

### Moving Averages
```sql
-- 3-month moving average
SELECT
    month,
    revenue,
    AVG(revenue) OVER (
        ORDER BY month
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_avg_3mo
FROM monthly_sales;
```

---

## Common Interview Patterns

### Second Highest Salary
```sql
-- Method 1: Subquery
SELECT MAX(salary) FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Method 2: DENSE_RANK
SELECT salary FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rank
    FROM employees
) ranked
WHERE rank = 2;
```

### Find Duplicates
```sql
SELECT email, COUNT(*)
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

### Top N Per Group
```sql
-- Top 3 earners per department
WITH ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS rn
    FROM employees
)
SELECT * FROM ranked WHERE rn <= 3;
```

### Year-Over-Year Growth
```sql
WITH yearly AS (
    SELECT
        EXTRACT(YEAR FROM date) AS year,
        SUM(revenue) AS total
    FROM sales
    GROUP BY EXTRACT(YEAR FROM date)
)
SELECT
    year,
    total,
    LAG(total) OVER (ORDER BY year) AS prev_year,
    ROUND((total - LAG(total) OVER (ORDER BY year)) * 100.0 /
          LAG(total) OVER (ORDER BY year), 2) AS growth_pct
FROM yearly;
```

---

## Quick Reference

| Operation | Syntax |
|-----------|--------|
| Filter rows | `WHERE` |
| Filter groups | `HAVING` |
| Sort | `ORDER BY col [ASC/DESC]` |
| Limit | `LIMIT n` or `LIMIT n OFFSET m` |
| Count | `COUNT(*)` or `COUNT(col)` |
| Group | `GROUP BY col` |
| Join | `[INNER/LEFT/RIGHT] JOIN table ON condition` |
| Rank | `ROW_NUMBER() OVER (ORDER BY col)` |
| Previous row | `LAG(col, 1) OVER (ORDER BY col)` |
| Running total | `SUM(col) OVER (ORDER BY col)` |

---

*Last updated: February 2026*
