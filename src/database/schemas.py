import uuid
from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, DATE
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(UUID, primary_key=True, unique=True, index=True, default=uuid.uuid4)
    employee_first_name = Column(String, nullable=False)
    employee_last_name = Column(String, nullable=False)


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(UUID, primary_key=True, unique=True, index=True, default=uuid.uuid4)
    customer_first_name = Column(String, nullable=False)
    customer_last_name = Column(String, nullable=False)

    accounts = relationship("Account", back_populates="customer", cascade="all, delete-orphan")


class Account(Base):
    __tablename__ = 'accounts'

    account_id = Column(UUID, primary_key=True, unique=True, index=True, default=uuid.uuid4)
    customer_id = Column(UUID, ForeignKey('customers.customer_id'), nullable=False)
    account_balance = Column(Float, nullable=False)
    customer = relationship("Customer", back_populates="accounts")


class Transaction(Base):
    __tablename__ = "transactions"

    transaction_id = Column(UUID, primary_key=True, index=True)
    transaction_date = Column(DATE, index=True, nullable=False)
    sender_account_id = Column(UUID, index=True, nullable=False)
    receiver_account_id = Column(UUID, index=True, nullable=False)
    amount = Column(Float, index=True, nullable=False)
