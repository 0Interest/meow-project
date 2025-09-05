from fastapi import FastAPI

from src.api import employee_router
from src.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(employee_router, tags=["employee"])
