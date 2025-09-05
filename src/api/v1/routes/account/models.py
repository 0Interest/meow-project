from uuid import UUID
from pydantic import BaseModel


class AccountCreate(BaseModel):
    customer_id: UUID
    account_balance: float


class AccountResponse(BaseModel):
    customer_id: UUID
    account_balance: float

    class Config:
        from_attributes = True
