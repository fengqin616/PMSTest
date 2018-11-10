# test_wallet.py

import pytest
from .wallet import Wallet, InsufficientAmount

@pytest.fixture
def my_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

list1 = [
    (30, 10, 20),
    (20, 2, 18),
]
@pytest.mark.parametrize("earned,spent,expected",list1)
def test_transactions(my_wallet, earned, spent, expected):
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)

    assert my_wallet.balance == expected

