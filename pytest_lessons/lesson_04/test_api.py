from fastapi.testclient import TestClient
from api import app , accounts
import pytest

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_accounts():
    accounts[1] = {"name": "Ashish", "balance": 100.0}
    accounts[2] = {"name": "Ravi", "balance": 50.0}

def test_get_account_success():
    response = client.get("/accounts/1")

    assert response.status_code == 200
    assert response.json() == {"name" : "Ashish" , "balance" : 100.0}


def test_get_account_not_found():
    response = client.get("/accounts/100")

    assert response.status_code == 404
    assert response.json() == {"detail" : "Account not found"}


def test_deposit_success():
    response = client.post("/accounts/1/deposit", json={"amount": 50})

    assert response.status_code == 200
    assert response.json() == {"name" : "Ashish" , "balance" : 150.0}



def test_bad_deposit():
    response = client.post("/accounts/1/deposit", json={"amount": -50})

    assert response.status_code == 400
    assert response.json() == {"detail" : "Amount must be positive"}


def test_withdraw_success():
    response = client.post("/accounts/1/withdraw", json={"amount": 50})
    assert response.status_code == 200
    assert response.json() == {"name" : "Ashish" , "balance" : 50.0}