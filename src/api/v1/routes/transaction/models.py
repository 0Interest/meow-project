from uuid import UUID
from pydantic import BaseModel
from datetime import date


class TransferRequest(BaseModel):
    sender_account_id: UUID
    receiver_account_id: UUID
    amount: float


class TransactionResponse(BaseModel):
    transaction_date: date
    transaction_id: UUID
    sender_account_id: UUID
    receiver_account_id: UUID
    amount: float

    class Config:
        from_attributes = True
