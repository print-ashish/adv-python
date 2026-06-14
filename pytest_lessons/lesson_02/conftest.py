import pytest
from bank import BankAccount 

@pytest.fixture 
def account():
    return BankAccount("Ashish", 100)

@pytest.fixture
def broke_account():
    return BankAccount("Broke", 0)

@pytest.fixture
def account_with_deposit(account):
    account.deposit(30)
    return account