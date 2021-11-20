import pytest
from brownie import Token

from tests.fixtures.accounts import admin, issuer, holders

@pytest.fixture(scope="module", autouse=True)
def token(admin, issuer):
    max_supply = pow(10, 18+9) # 1,000,000,000
    yield admin.deploy(Token, "Green", "GREEN", 18, admin, issuer, max_supply)

issuancedata = [
    # holder    balance
    (0,         1),
    (2,         5),
    (4,         4),
    (5,         6),
]

@pytest.fixture(scope="module", autouse=True)
def issuance(token, admin, issuer, holders):
    for holder,balance in issuancedata:
        token.mint(holders[holder], balance, {'from': issuer})

approvaldata = [
    # holder    spender     amount
    (0,         1,          1),
    (2,         1,          2),
    (2,         3,          2),
    (2,         2,          1),
    (4,         0,          3),
    (5,         6,          9),
]

@pytest.fixture(scope="module", autouse=True)
def approval(token, holders):
    for holder,spender,amount in approvaldata:
        token.approve(holders[spender], amount, {'from': holders[holder]})
