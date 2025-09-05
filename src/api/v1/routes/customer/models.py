from uuid import UUID
from pydantic import BaseModel


class CustomerCreate(BaseModel):
    customer_first_name: str
    customer_last_name: str


class CustomerResponse(BaseModel):
    customer_id: UUID
    customer_first_name: str
    customer_last_name: str

    class Config:
        from_attributes = True
