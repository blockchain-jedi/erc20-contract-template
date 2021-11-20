import pytest
from brownie import reverts

from tests.fixtures.token import token, issuance, issuancedata
from tests.fixtures.accounts import admin, issuer, holders, zero_address

def test_transfer_to_zero_address(token, holders):
    with reverts("dev: requires non-zero address"):
        token.transfer(zero_address, 1, {'from': holders[0]})

@pytest.mark.parametrize('holder,balance', issuancedata)
def test_transfer_exceeds_balance(token, holders, holder, balance):
    with reverts("dev: exceeds balance"):
        token.transfer('0xFfFfF6637EfCf49e8ABd998F9f54AE402D4DD332', balance+1, {'from': holders[holder]})

transferdata = [
    # sender    recipient   amount  sender_balance,  recipient_balance
    (0,         1,          1,      0,               1),
    (1,         0,          1,      0,               1),
    (0,         2,          1,      0,               6),
    (2,         4,          4,      2,               8),
    (4,         5,          4,      4,              10),
    (5,         0,          10,     0,              10),
]

@pytest.mark.parametrize('sender,recipient,amount,sender_balance,recipient_balance', transferdata)
def test_transfer(token, holders, sender, recipient, amount, sender_balance, recipient_balance):
    sender = holders[sender]
    recipient = holders[recipient]
    token.transfer(recipient, amount, {'from': sender})

    assert token.balanceOf(sender) == sender_balance
    assert token.balanceOf(recipient) == recipient_balance
