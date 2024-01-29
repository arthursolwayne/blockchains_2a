import eth_account
from web3 import Web3
from eth_account.messages import encode_defunct


def sign(m):
    w3 = Web3()

    # Create an eth account
    account = eth_account.Account.create()
    eth_address = account.address
    private_key = account.privateKey

    # Encode the message
    message_encoded = encode_defunct(text=m)

    # Generate signature using the private key
    signed_message = w3.eth.account.sign_message(message_encoded, private_key)

    # Check that signed_message is an instance of SignedMessage
    assert isinstance(signed_message, eth_account.datastructures.SignedMessage)

    return eth_address, signed_message
