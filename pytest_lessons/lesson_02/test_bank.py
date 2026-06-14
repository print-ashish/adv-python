import pytest
from bank import BankAccount , InsufficientBalanceError 


# def test_deposit_balance():
#     account = BankAccount("John", 100)
#     new_balance = account.deposit(50)
#     assert new_balance == 150
#     assert account.balance == 150


# def test_withdraw_decreases_balance(account):
#     new_balance = account.withdraw(50)
#     assert new_balance == 50
#     assert account.balance == 50


# def test_withdraw_raises_when_not_enough_balance():
#     account = BankAccount("Ashish", balance=50)
#     with pytest.raises(InsufficientBalanceError):
#         account.withdraw(100)

# def test_deposit_raises_for_zero_or_negative():
#     account = BankAccount("Ashish", balance=30)
#     with pytest.raises(ValueError):
#         account.deposit(0)
#     assert account.balance == 30


# def test_new_account_starts_with_zero_balance():
#     account = BankAccount("Ashish")
#     assert account.balance == 0


# def test_deposit_using_fixture(account):
#     new_balance = account.deposit(50)
#     assert new_balance == 150

# def test_withdraw_using_fixture_with_account(account):
#     new_balance = account.withdraw(100)
#     assert new_balance == 0

# def test_deposit_using_fixture_with_broke_account(broke_account):
#     with pytest.raises(ValueError):
#         broke_account.deposit(0)
#     assert broke_account.balance == 0

# def test_new_account_starts_with_zero_balance_using_fixture(broke_account):
#     assert broke_account.balance == 0

# def test_withdraw_using_fixture(broke_account):
#     with pytest.raises(InsufficientBalanceError):
#         broke_account.withdraw(100)


# def test_account_with_deposit_fixture(account_with_deposit):
#     assert account_with_deposit.balance == 130



@pytest.mark.parametrize("amount , expected ",[
    (10,110),
    (20,120),
    (30,130),
    (40,140),
    (50,150),
    (60,160),
    (70,170),
    (80,180),
    (90,190),
    (100,200),
])
def test_deposit_multiple_amounts(account,amount,expected):
    new_balance = account.deposit(amount)
    assert new_balance == expected


@pytest.mark.parametrize("invalid_amount",[-3,0,-4])
def test_deposit_raises_for_invalid_amount(account,invalid_amount):
    with pytest.raises(ValueError):
        account.deposit(invalid_amount)

@pytest.mark.parametrize("withdraw_amount , expected ",[
    (50,50),
    (100,0),
])
def test_withdraw_multiple_amounts(account,withdraw_amount,expected):
    new_balance = account.withdraw(withdraw_amount)
    assert new_balance == expected


@pytest.mark.parametrize("withdraw_amount",[200, 300, 2003])
def test_withraw_failure(account,withdraw_amount):
    with pytest.raises(InsufficientBalanceError):
        account.withdraw(withdraw_amount)