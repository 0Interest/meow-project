from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.api.v1.routes.customer.models import CustomerCreate, CustomerResponse
from src.database import get_db
from src.database.schemas import Customer

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.post("/", response_model=CustomerResponse)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    new_customer = Customer(
        customer_first_name=customer.customer_first_name,
        customer_last_name=customer.customer_last_name,
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer


@router.get("/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: UUID, db: Session = Depends(get_db)):
    emp = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Customer not found")
    return emp


@router.delete("/{customer_id}", response_model=CustomerResponse)
def delete_customer(customer_id: UUID, db: Session = Depends(get_db)):
    emp = db.query(Customer).filter(Customer.customer_id == customer_id).first()
    if not emp:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(emp)
    db.commit()
    return emp
