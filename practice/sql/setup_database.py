"""
Run this once to create practice databases with realistic data.
Usage: python setup_database.py
"""
import sqlite3
import random
from datetime import datetime, timedelta

def create_company_db():
    """Create a company database for SQL practice"""
    conn = sqlite3.connect('company.db')
    c = conn.cursor()

    # DDL - Create tables
    c.executescript('''
        DROP TABLE IF EXISTS employees;
        DROP TABLE IF EXISTS departments;
        DROP TABLE IF EXISTS salaries;
        DROP TABLE IF EXISTS projects;
        DROP TABLE IF EXISTS employee_projects;

        CREATE TABLE departments (
            dept_id INTEGER PRIMARY KEY,
            dept_name TEXT NOT NULL,
            location TEXT,
            budget REAL
        );

        CREATE TABLE employees (
            emp_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE,
            hire_date DATE,
            dept_id INTEGER,
            manager_id INTEGER,
            FOREIGN KEY (dept_id) REFERENCES departments(dept_id),
            FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
        );

        CREATE TABLE salaries (
            salary_id INTEGER PRIMARY KEY,
            emp_id INTEGER,
            amount REAL,
            from_date DATE,
            to_date DATE,
            FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
        );

        CREATE TABLE projects (
            project_id INTEGER PRIMARY KEY,
            project_name TEXT NOT NULL,
            start_date DATE,
            end_date DATE,
            budget REAL,
            status TEXT
        );

        CREATE TABLE employee_projects (
            emp_id INTEGER,
            project_id INTEGER,
            role TEXT,
            hours_worked INTEGER,
            PRIMARY KEY (emp_id, project_id),
            FOREIGN KEY (emp_id) REFERENCES employees(emp_id),
            FOREIGN KEY (project_id) REFERENCES projects(project_id)
        );
    ''')

    # DML - Insert data
    departments = [
        (1, 'Engineering', 'Singapore', 500000),
        (2, 'Sales', 'Singapore', 300000),
        (3, 'Marketing', 'Malaysia', 200000),
        (4, 'HR', 'Singapore', 150000),
        (5, 'Finance', 'Singapore', 250000),
    ]
    c.executemany('INSERT INTO departments VALUES (?,?,?,?)', departments)

    first_names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace',
                   'Henry', 'Ivy', 'Jack', 'Karen', 'Leo', 'Mia', 'Nathan', 'Olivia']
    last_names = ['Wong', 'Tan', 'Lee', 'Lim', 'Chen', 'Ng', 'Kumar', 'Singh',
                  'Ahmad', 'Ali', 'Patel', 'Smith', 'Johnson', 'Williams', 'Brown']

    employees = []
    for i in range(1, 51):
        fname = random.choice(first_names)
        lname = random.choice(last_names)
        dept = random.randint(1, 5)
        hire_date = datetime(2018, 1, 1) + timedelta(days=random.randint(0, 2000))
        manager = random.randint(1, min(i-1, 10)) if i > 1 else None
        employees.append((
            i, fname, lname,
            f"{fname.lower()}.{lname.lower()}{i}@company.com",  # Add i for uniqueness
            hire_date.strftime('%Y-%m-%d'),
            dept, manager
        ))
    c.executemany('INSERT INTO employees VALUES (?,?,?,?,?,?,?)', employees)

    # Salaries with history
    salaries = []
    salary_id = 1
    for emp_id in range(1, 51):
        base = random.randint(3000, 12000)
        # Current salary
        salaries.append((salary_id, emp_id, base, '2024-01-01', None))
        salary_id += 1
        # Previous salary
        if random.random() > 0.3:
            salaries.append((salary_id, emp_id, base * 0.9, '2023-01-01', '2023-12-31'))
            salary_id += 1
    c.executemany('INSERT INTO salaries VALUES (?,?,?,?,?)', salaries)

    # Projects
    projects = [
        (1, 'Website Redesign', '2024-01-15', '2024-06-30', 75000, 'completed'),
        (2, 'Mobile App', '2024-03-01', '2024-12-31', 150000, 'in_progress'),
        (3, 'Data Pipeline', '2024-06-01', '2025-03-31', 100000, 'in_progress'),
        (4, 'CRM Integration', '2023-09-01', '2024-02-28', 50000, 'completed'),
        (5, 'AI Chatbot', '2024-09-01', '2025-06-30', 200000, 'planning'),
    ]
    c.executemany('INSERT INTO projects VALUES (?,?,?,?,?,?)', projects)

    # Employee-Project assignments
    roles = ['Lead', 'Developer', 'Analyst', 'Tester', 'Support']
    emp_projects = []
    for project_id in range(1, 6):
        num_members = random.randint(3, 8)
        members = random.sample(range(1, 51), num_members)
        for emp_id in members:
            emp_projects.append((
                emp_id, project_id,
                random.choice(roles),
                random.randint(20, 200)
            ))
    c.executemany('INSERT INTO employee_projects VALUES (?,?,?,?)', emp_projects)

    conn.commit()
    conn.close()
    print("Created company.db with 50 employees, 5 departments, 5 projects")


def create_ecommerce_db():
    """Create an e-commerce database for more complex queries"""
    conn = sqlite3.connect('ecommerce.db')
    c = conn.cursor()

    c.executescript('''
        DROP TABLE IF EXISTS orders;
        DROP TABLE IF EXISTS order_items;
        DROP TABLE IF EXISTS products;
        DROP TABLE IF EXISTS customers;
        DROP TABLE IF EXISTS categories;

        CREATE TABLE categories (
            category_id INTEGER PRIMARY KEY,
            category_name TEXT NOT NULL,
            parent_category_id INTEGER
        );

        CREATE TABLE products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            category_id INTEGER,
            price REAL,
            stock_quantity INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(category_id)
        );

        CREATE TABLE customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            city TEXT,
            signup_date DATE,
            is_premium INTEGER DEFAULT 0
        );

        CREATE TABLE orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER,
            order_date DATE,
            total_amount REAL,
            status TEXT,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        );

        CREATE TABLE order_items (
            order_id INTEGER,
            product_id INTEGER,
            quantity INTEGER,
            unit_price REAL,
            PRIMARY KEY (order_id, product_id),
            FOREIGN KEY (order_id) REFERENCES orders(order_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        );
    ''')

    # Categories
    categories = [
        (1, 'Electronics', None),
        (2, 'Clothing', None),
        (3, 'Books', None),
        (4, 'Phones', 1),
        (5, 'Laptops', 1),
        (6, 'Men', 2),
        (7, 'Women', 2),
    ]
    c.executemany('INSERT INTO categories VALUES (?,?,?)', categories)

    # Products
    products = [
        (1, 'iPhone 15', 4, 1299, 50),
        (2, 'Samsung Galaxy S24', 4, 999, 75),
        (3, 'MacBook Pro', 5, 2499, 30),
        (4, 'Dell XPS 15', 5, 1799, 40),
        (5, 'T-Shirt Basic', 6, 29, 200),
        (6, 'Jeans Slim Fit', 6, 89, 150),
        (7, 'Dress Floral', 7, 129, 80),
        (8, 'Python Crash Course', 3, 45, 100),
        (9, 'Data Science Handbook', 3, 55, 75),
        (10, 'AirPods Pro', 1, 249, 120),
    ]
    c.executemany('INSERT INTO products VALUES (?,?,?,?,?)', products)

    # Customers
    cities = ['Singapore', 'Kuala Lumpur', 'Bangkok', 'Jakarta', 'Manila']
    customers = []
    for i in range(1, 101):
        signup = datetime(2022, 1, 1) + timedelta(days=random.randint(0, 730))
        customers.append((
            i, f'Customer {i}', f'customer{i}@email.com',
            random.choice(cities), signup.strftime('%Y-%m-%d'),
            1 if random.random() > 0.8 else 0
        ))
    c.executemany('INSERT INTO customers VALUES (?,?,?,?,?,?)', customers)

    # Orders
    orders = []
    order_items = []
    statuses = ['completed', 'completed', 'completed', 'shipped', 'processing', 'cancelled']

    for order_id in range(1, 301):
        customer_id = random.randint(1, 100)
        order_date = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 365))
        status = random.choice(statuses)

        # Generate items for this order
        num_items = random.randint(1, 4)
        selected_products = random.sample(range(1, 11), num_items)
        total = 0

        for prod_id in selected_products:
            qty = random.randint(1, 3)
            # Get price from products list
            price = next(p[3] for p in products if p[0] == prod_id)
            total += price * qty
            order_items.append((order_id, prod_id, qty, price))

        orders.append((order_id, customer_id, order_date.strftime('%Y-%m-%d'), total, status))

    c.executemany('INSERT INTO orders VALUES (?,?,?,?,?)', orders)
    c.executemany('INSERT INTO order_items VALUES (?,?,?,?)', order_items)

    conn.commit()
    conn.close()
    print("Created ecommerce.db with 100 customers, 300 orders, 10 products")


if __name__ == '__main__':
    create_company_db()
    create_ecommerce_db()
    print("\nDatabases ready! Start practicing in the exercise files.")
