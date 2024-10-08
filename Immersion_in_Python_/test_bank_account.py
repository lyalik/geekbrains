import pytest
from bank_account import BankAccount, InsufficientFundsError

def test_initial_balance_default():
    account = BankAccount()
    assert account.get_balance() == 0

def test_initial_balance_custom():
    account = BankAccount(100)
    assert account.get_balance() == 100

def test_deposit():
    account = BankAccount()
    account.deposit(100)
    assert account.get_balance() == 100

def test_withdraw():
    account = BankAccount(100)
    account.withdraw(50)
    assert account.get_balance() == 50

def test_withdraw_insufficient_funds():
    account = BankAccount(50)
    with pytest.raises(InsufficientFundsError):
        account.withdraw(100)

def test_deposit_negative_amount():
    account = BankAccount()
    with pytest.raises(ValueError):
        account.deposit(-50)

def test_withdraw_negative_amount():
    account = BankAccount()
    with pytest.raises(ValueError):
        account.withdraw(-50)

def test_initial_balance_negative():
    with pytest.raises(ValueError):
        BankAccount(-100)