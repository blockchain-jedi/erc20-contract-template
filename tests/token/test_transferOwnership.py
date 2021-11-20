import pytest
from brownie import reverts

from tests.fixtures.token import token
from tests.fixtures.accounts import admin, issuer, non_holders

def test_transferOwnership_from_non_owner(token, non_holders):
    with reverts("dev: missing role"):
        token.transferOwnership(non_holders[0], {'from': non_holders[0]})

def test_transferOwnership_from_owner(token, admin, non_holders):
    token.transferOwnership(non_holders[0], {'from': admin})

def test_confirmOwnership_from_non_pending_owner(token, admin, non_holders):
    with reverts("dev: missing role"):
        token.confirmOwnership({'from': admin})

def test_confirmOwnership_from_pending_owner(token, admin, non_holders):
    token.confirmOwnership({'from': non_holders[0]})

