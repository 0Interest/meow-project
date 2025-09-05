from fastapi import FastAPI

from src.api import employee_router, customer_router, account_router
from src.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(employee_router, tags=["employee"])
app.include_router(customer_router, tags=["customer"])
app.include_router(account_router, tags=["account"])
