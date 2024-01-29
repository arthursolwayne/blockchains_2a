import eth_account
from web3 import Web3
from eth_account.messages import encode_defunct


def sign(m):
    w3 = Web3()
    account = eth_account.Account.create()
    eth_address, private_key = create_ethereum_account()
    message_encoded = encode_defunct(text=m)
    signed_message = w3.eth.account.sign_message(message_encoded, private_key)
    assert isinstance(signed_message, eth_account.datastructures.SignedMessage)
    return eth_address, signed_message

def create_ethereum_account():
    w3 = Web3()
    acc = w3.eth.account.create()
    private_key = w3.to_hex(acc.key)
    account_address = acc.address
    return private_key, account_address
