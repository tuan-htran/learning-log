from bank_account_rebuild import BankAccount
import pytest

def test_initial_balance():
    account = BankAccount("Tuan", 500)
    assert account.balance == 500

def test_deposit():
    account = BankAccount("Tuan", 500)
    account.deposit(200)
    assert account.balance == 700

def test_withdraw():
    account = BankAccount("Tuan", 500)
    account.withdraw(400)
    assert account.balance == 100

def test_withdraw_insufficient_fund():
    account = BankAccount("Tuan", 500)
    with pytest.raises(ValueError):
        account.withdraw(1000) # more than the balance

def test_deposit_negative_amount():
    account = BankAccount("Tuan", 500)
    with pytest.raises(ValueError):
        account.deposit(-200)