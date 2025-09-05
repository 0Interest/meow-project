from uuid import UUID
from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    employee_first_name: str
    employee_last_name: str


class EmployeeResponse(BaseModel):
    employee_id: UUID
    employee_first_name: str
    employee_last_name: str

    class Config:
        from_attributes = True
