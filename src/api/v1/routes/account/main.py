import uuid
from datetime import date
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.api.v1.routes.account.models import AccountResponse, AccountCreate, TransactionResponse, TransferRequest
from src.database import get_db
from src.database.schemas import Account, Transaction

router = APIRouter(prefix="/accounts")


@router.post("/", response_model=AccountResponse)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):
    new_account = Account(
        customer_id=account.customer_id,
        account_balance=account.account_balance,
    )
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account


@router.post("/transfer", response_model=TransactionResponse)
def transfer(transfer: TransferRequest, db: Session = Depends(get_db)):
    if transfer.amount <= 0:
        raise HTTPException(status_code=400, detail="Transfer amount must be greater than zero")

    sender_account = db.query(Account).filter(Account.account_id == transfer.sender_account_id).first()
    receiver_account = db.query(Account).filter(Account.account_id == transfer.receiver_account_id).first()

    if not sender_account:
        raise HTTPException(status_code=404, detail="Sender account not found")
    if not receiver_account:
        raise HTTPException(status_code=404, detail="Receiver account not found")

    if sender_account.account_balance < transfer.amount:
        raise HTTPException(status_code=400, detail="Insufficient funds in sender's account")

    # Update balances
    sender_account.account_balance -= transfer.amount
    receiver_account.account_balance += transfer.amount

    # Create transaction record
    new_transaction = Transaction(
        transaction_id=uuid.uuid4(),
        transaction_date=date.today(),
        sender_account_id=transfer.sender_account_id,
        receiver_account_id=transfer.receiver_account_id,
        amount=transfer.amount
    )

    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)

    return new_transaction


@router.get("/{account_id}", response_model=AccountResponse)
def get_account_by_account_id(account_id: UUID, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.account_id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account


@router.get("/{customer_id}", response_model=list[AccountResponse])
def get_accounts_by_customer_id(customer_id: UUID, db: Session = Depends(get_db)):
    accounts = db.query(Account).filter(Account.customer_id == customer_id)
    if not accounts:
        raise HTTPException(status_code=404, detail="Account not found")
    return accounts


@router.delete("/{account_id}", response_model=AccountResponse)
def delete_account(account_id: UUID, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.customer_id == account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    db.delete(account)
    db.commit()
    return account
