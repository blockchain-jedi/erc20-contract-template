import pytest
from brownie import reverts

from tests.fixtures.token import token
from tests.fixtures.accounts import admin, issuer, holders, zero_address

mintdata = [
    # holder    amount  balanceOf   totalSupply
    (0,         0,      0,          0),
    (1,         1,      1,          1),
    (1,         2,      3,          3),
    (2,         4,      4,          7),
    (2,         0,      4,          7),
    (2,         4,      8,          11),
]

@pytest.mark.parametrize('holder,amount,balance,supply', mintdata)
def test_mint(token, issuer, holders, holder, amount, balance, supply):
    recipient = holders[holder]
    token.mint(recipient, amount, {'from': issuer})

    assert token.balanceOf(recipient) == balance
    assert token.totalSupply() == supply

def test_mint_to_zero_address(token, issuer):
    with reverts("dev: requires non-zero address"):
        token.mint(zero_address, 1, {'from': issuer})

@pytest.mark.parametrize('holder', [0, 1, 2, 3, 4, 5])
def test_mint_non_issuer(token, holders, holder):
    with reverts("dev: missing role"):
        token.mint(zero_address, 1, {'from': holders[holder]})
