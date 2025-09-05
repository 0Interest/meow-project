from fastapi import FastAPI

from src.api import employee_router, customer_router, account_router
from src.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(employee_router, tags=["Employees"])
app.include_router(customer_router, tags=["Customers"])
app.include_router(account_router, tags=["Accounts"])
