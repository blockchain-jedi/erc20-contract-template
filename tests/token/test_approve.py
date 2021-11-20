import pytest
from brownie import reverts

from tests.fixtures.token import token
from tests.fixtures.accounts import admin, issuer, holders

approvedata = [
    # owner     spender  amount
    (0,         0,       0),
    (1,         1,       1),
    (1,         2,       3),
    (2,         4,       4),
    (2,         0,       4),
    (2,         4,       8),
]

@pytest.mark.parametrize('owner,spender,amount', approvedata)
def test_approve(token, holders, owner, spender, amount):
    holder = holders[owner]
    recipient = holders[spender]
    token.approve(recipient, amount, {'from': holder})
    assert token.allowance(holder, recipient) == amount
