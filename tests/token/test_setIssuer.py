import pytest
from brownie import reverts

from tests.fixtures.token import token
from tests.fixtures.accounts import admin, issuer, non_holders

def test_setIssuer_from_non_owner(token, non_holders):
    with reverts("dev: missing role"):
        token.setIssuer(non_holders[0], {'from': non_holders[0]})

def test_setIssuer_from_issuer(token, issuer, non_holders):
    with reverts("dev: missing role"):
        token.setIssuer(non_holders[0], {'from': issuer})

def test_setIssuer_from_owner(token, admin, non_holders):
    token.setIssuer(non_holders[0], {'from': admin})
