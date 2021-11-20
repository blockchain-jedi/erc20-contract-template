#
# Usage:
#
#       % brownie console
#       >>> from scripts import token
#       >>> green = token.main()
#       >>> token.issue(green)
#       >>> token.transfer(green, accounts[1], accounts[2], 1)
#

from brownie import Token, accounts

admin = accounts[0]
issuer = accounts[1]
holders = accounts[2:9]

max_supply = pow(10, 18+9) # 1,000,000,000

def main():
    return Token.deploy("Green", "GREEN", 18, admin, issuer, max_supply, {'from': admin})

def issue(token):
    amount = 1000
    for account in holders:
        token.mint(account.address, amount, {'from': issuer})
        amount = amount * 2

def transfer(token, sender, recipient, value):
    token.transfer(recipient.address, value, {'from': sender})
