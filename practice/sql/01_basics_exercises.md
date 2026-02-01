# SQL Basics Exercises

**Database**: `company.db`
**Tables**: employees, departments, salaries, projects, employee_projects

Run `python setup_database.py` first to create the database.

---

## Level 1: SELECT & WHERE

### Exercise 1.1
Get all employees in the Engineering department (dept_id = 1).

```sql
-- Write your query in 01_my_solutions.sql
-- Hint: SELECT ... FROM ... WHERE ...
```

### Exercise 1.2
Find all employees hired after 2022-01-01.

### Exercise 1.3
List all employees whose last name starts with 'L'.
```sql
-- Hint: Use LIKE with wildcard %
```

### Exercise 1.4
Get employees who are in Engineering OR Sales departments.
```sql
-- Hint: Use IN or multiple OR conditions
```

---

## Level 2: ORDER BY & LIMIT

### Exercise 2.1
List all departments ordered by budget (highest first).

### Exercise 2.2
Get the 5 most recently hired employees.

### Exercise 2.3
Find the 3 employees with the longest tenure (earliest hire_date).

---

## Level 3: Aggregations (COUNT, SUM, AVG)

### Exercise 3.1
Count how many employees are in each department.
```sql
-- Expected output: dept_id, employee_count
```

### Exercise 3.2
What is the average salary? (Use current salaries where to_date IS NULL)

### Exercise 3.3
Find the total budget across all departments.

### Exercise 3.4
What is the highest and lowest current salary?

---

## Level 4: GROUP BY & HAVING

### Exercise 4.1
For each department, show the number of employees and average salary.
```sql
-- Join employees with salaries, group by department
```

### Exercise 4.2
Find departments that have more than 8 employees.
```sql
-- Hint: Use HAVING after GROUP BY
```

### Exercise 4.3
List projects with their total hours worked (sum of all employee hours).

---

## How to Practice

1. Open `01_my_solutions.sql`
2. Write your query for each exercise
3. Ask Claude Code: "Run exercise 1.1 from my SQL solutions"
4. I'll execute it and show you the results or errors
5. We iterate until you understand it

---

## Schema Reference

```sql
employees: emp_id, first_name, last_name, email, hire_date, dept_id, manager_id
departments: dept_id, dept_name, location, budget
salaries: salary_id, emp_id, amount, from_date, to_date
projects: project_id, project_name, start_date, end_date, budget, status
employee_projects: emp_id, project_id, role, hours_worked
```
