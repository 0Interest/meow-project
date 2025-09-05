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


class TransactionResponse(BaseModel):
    transaction_id: UUID
    sender_account_id: UUID
    receiver_account_id: UUID
    amount: float

    class Config:
        from_attributes = True
