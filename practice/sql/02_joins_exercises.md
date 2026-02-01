# SQL JOINs Exercises

**Database**: `company.db` and `ecommerce.db`

---

## Level 5: INNER JOIN

### Exercise 5.1
List all employees with their department names.
```sql
-- Output: first_name, last_name, dept_name
```

### Exercise 5.2
Show each employee's current salary with their name.
```sql
-- Join employees with salaries where to_date IS NULL
```

### Exercise 5.3
List all order items with product names and prices.
```sql
-- Database: ecommerce.db
-- Join order_items with products
```

---

## Level 6: LEFT JOIN

### Exercise 6.1
List ALL departments, even those with no employees.
```sql
-- Some departments might have 0 employees - show them too
```

### Exercise 6.2
Find customers who have never placed an order.
```sql
-- Database: ecommerce.db
-- LEFT JOIN customers with orders, filter where order_id IS NULL
```

### Exercise 6.3
Show all products and their total quantity sold (including unsold products).

---

## Level 7: Multiple JOINs

### Exercise 7.1
For each employee, show: name, department, and current salary.
```sql
-- Join 3 tables: employees, departments, salaries
```

### Exercise 7.2
List all orders with customer name, order date, and total items.
```sql
-- Database: ecommerce.db
```

### Exercise 7.3
Show employees and the projects they work on with their roles.
```sql
-- Join employees, employee_projects, projects
```

---

## Level 8: Self JOIN

### Exercise 8.1
List each employee with their manager's name.
```sql
-- Self-join employees table
-- Output: employee_name, manager_name
```

### Exercise 8.2
Find categories and their parent category names.
```sql
-- Database: ecommerce.db
-- Self-join categories table
```

---

## Schema Reference

**company.db:**
```sql
employees: emp_id, first_name, last_name, email, hire_date, dept_id, manager_id
departments: dept_id, dept_name, location, budget
salaries: salary_id, emp_id, amount, from_date, to_date
projects: project_id, project_name, start_date, end_date, budget, status
employee_projects: emp_id, project_id, role, hours_worked
```

**ecommerce.db:**
```sql
customers: customer_id, name, email, city, signup_date, is_premium
orders: order_id, customer_id, order_date, total_amount, status
order_items: order_id, product_id, quantity, unit_price
products: product_id, product_name, category_id, price, stock_quantity
categories: category_id, category_name, parent_category_id
```
