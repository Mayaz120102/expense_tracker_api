from fastapi import status

from database import SessionLocal
from main import app
from models import Transaction
from router.auth import get_current_user
from test.test_main import client


def override_get_current_user():
    return {"id": 1, "username": "testuser"}


def test_transactions():

    db = SessionLocal()

    db.query(Transaction).filter(Transaction.id == 99).delete()

    transaction = Transaction(
        id=99,
        title="testing",
        amount=155555.555,
        type="testing",
        category="testing",
        date="2080-08-09",
        owner_id=1,
    )

    db.add(transaction)
    db.commit()


app.dependency_overrides[get_current_user] = override_get_current_user


def test_get_all_transaction():
    response = client.get("/transactions")
    assert response.status_code == status.HTTP_200_OK


def test_get_specific_transaction():
    response = client.get("/transactions/99")
    assert response.status_code == status.HTTP_200_OK


def test_create_transaction():
    request_data = {
        "title": "string",
        "amount": 1,
        "type": "income",
        "category": "string",
    }
    response = client.post("/transactions", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED


def test_update_transaction():
    request_data = {"title": "updated"}
    response = client.put("/transactions/99", json=request_data)
    assert response.status_code == status.HTTP_200_OK


def test_delete_transaction():
    response = client.delete("/transactions/99")
    assert response.status_code == status.HTTP_200_OK
