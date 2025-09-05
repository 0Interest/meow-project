import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.api.v1.routes.transaction.models import TransactionResponse
from src.database import get_db
from src.database.schemas import Transaction

router = APIRouter(prefix="/transactions", tags=["Transactions"])


@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction_by_transaction_id(transaction_id: uuid.UUID, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


@router.get("/by-sender/{sender_account_id}", response_model=list[TransactionResponse])
def get_transactions_by_sender_account_id(sender_account_id: uuid.UUID, db: Session = Depends(get_db)):
    transactions = db.query(Transaction).filter(Transaction.sender_account_id == sender_account_id).all()
    if not transactions:
        raise HTTPException(status_code=404, detail="No transactions found for this sender account")
    return transactions
