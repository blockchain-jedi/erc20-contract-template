import pytest
from brownie import accounts

zero_address = "0x0000000000000000000000000000000000000000"

@pytest.fixture(scope="session", autouse=True)
def admin():
    yield accounts[0]

@pytest.fixture(scope="session", autouse=True)
def issuer():
    yield accounts[1]

@pytest.fixture(scope="session", autouse=True)
def holders():
    yield accounts[2:9]

@pytest.fixture(scope="session", autouse=True)
def non_holders():
    yield accounts[9:16]
