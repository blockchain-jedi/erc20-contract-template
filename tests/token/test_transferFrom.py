import pytest
from brownie import reverts

from tests.fixtures.token import token, issuance, approval, issuancedata
from tests.fixtures.accounts import admin, issuer, holders, zero_address

def test_transferfrom_zero_address(token, holders):
    with reverts("dev: requires non-zero address"):
        token.transferFrom(holders[0], zero_address, 0, {'from': holders[0]})

transferfromdata = [
    # holder    recipient,  spender  amount  holder_balance,  recipient_balance,  updated_approval
    (0,         0,          0,       0,      1,               1,                  0),  # Send 0 to self, from unapproved self
    (0,         1,          0,       0,      1,               0,                  0),  # Send 0 to other, from unapproved self
    (0,         0,          1,       1,      1,               1,                  0),  # Send all to self, from approved
    (2,         2,          2,       1,      5,               5,                  0),  # Send 1 to same address, from self
    (2,         2,          3,       1,      5,               5,                  1),  # Send 1 to same address, from approved
    (4,         6,          0,       1,      3,               1,                  2),  # Send 1 to new holder, from approved
    (4,         6,          0,       2,      1,               3,                  0),  # Send all to new holder, from approved
]

@pytest.mark.parametrize('holder,recipient,spender,amount,holder_bal,recipient_bal,approved', transferfromdata)
def test_transferFrom(token, holders, holder, recipient, spender, amount, holder_bal, recipient_bal, approved):
    owner = holders[holder]
    recipient = holders[recipient]
    spender = holders[spender]
    token.transferFrom(owner, recipient, amount, {'from': spender})

    assert token.balanceOf(owner) == holder_bal
    assert token.balanceOf(recipient) == recipient_bal
    assert token.allowance(owner, spender) == approved

def test_transferFrom_exceeds_allowance(token, holders):
    with reverts("dev: exceeds allowance"):
        token.transferFrom(holders[5], holders[0], 10, {'from': holders[6]})

def test_transferFrom_exceeds_balance(token, holders):
    with reverts("dev: exceeds balance"):
        token.transferFrom(holders[5], holders[0], 7, {'from': holders[6]})
