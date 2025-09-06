# Banking System API

A simple **FastAPI-based Banking System** that demonstrates core banking operations:  
- Manage **Employees**  
- Manage **Customers**  
- Manage **Accounts**  
- Perform **Transfers**  

The project uses **FastAPI**, **SQLAlchemy/SQLModel**, **PostgreSQL**, and **Pydantic Settings** for configuration.  

---

## Features

- **Employee Endpoints**
  - Add a new employee
  - Get employee by ID
  - Remove employee

- **Customer Endpoints**
  - Add a new customer
  - Get customer by ID
  - Remove customer

- **Account Endpoints**
  - Add a new account
  - Get account by ID
  - Get accounts by customer ID
  - Transfer funds between accounts (with balance checks)

- **Transfer Endpoints**
  - Record a transfer transaction
  - Get transaction by ID
  - Get transactions by sender account ID

# Installation and Usage
- Clone the repository
- Run a local PostgreSQL server
- Change `.env` to have the right variables (Database name, username, password, host and port)
- Run `pip install -r requirements.txt`
- Run `fastapi dev main.py`