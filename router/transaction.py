from typing import Annotated, Literal, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Transaction, Users
from router.auth import db_dependency, get_current_user, get_db

router = APIRouter()


class CreateTransaction(BaseModel):
    title: str
    amount: float = Field(gt=0)
    type: Literal["income", "expense"]
    category: str

class TransactionUpdate(BaseModel):
    title: Optional[str]= Field(default=None)
    amount: Optional[float] = Field(default=None, gt=0)
    type: Optional[Literal["income","expense"]]= None
    category:Optional[str]= Field(default=None) 


user_dependency = Annotated[dict, Depends(get_current_user)]


@router.post("/transactions", status_code=201)
def create_transaction(
    user: user_dependency, db: db_dependency, new_transaction: CreateTransaction
):

    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    transaction_model = Transaction(
        **new_transaction.model_dump(), owner_id=user.get("id")
    )
    db.add(transaction_model)
    db.commit()
    db.refresh(transaction_model)

    return transaction_model


@router.get("/transactions")
def get_all_transaction(user: user_dependency, db: db_dependency):

    if user is None:
        raise HTTPException(status_code=401, detail="Authentication failed")

    return db.query(Transaction).filter(Transaction.owner_id == user.get("id")).all()


@router.get("/transactions/{transaction_id}")
def get_specific_transaction(
    user: user_dependency, db: db_dependency, transaction_id: int
):

    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    specific_transaction = (
        db.query(Transaction)
        .filter(Transaction.owner_id == user.get("id"))
        .filter(Transaction.id == transaction_id)
        .first()
    )

    if specific_transaction is not None:
        return specific_transaction
    else:
        raise HTTPException(status_code=404, detail="Transaction not found")

@router.put("/transactions/{transaction_id}")
def update_transaction(user: user_dependency, db: db_dependency, transaction_id:int, update_transaction: TransactionUpdate):

    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")

    transaction =(
        db.query(Transaction).filter(Transaction.owner_id == user.get("id")).filter(Transaction.id == transaction_id).first()
    )

    if transaction is None:
        raise HTTPException(status_code=404,detail="Transaction not found")

    update_data = update_transaction.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(transaction, key, value)

    db.commit()
    db.refresh(transaction)
    return transaction

