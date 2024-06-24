import json
from unittest.mock import MagicMock

class PiNetworkBlockchainMock:
    def __init__(self):
        self.synchronize_blockchain_called = False
        self.get_blockchain_height_called = False

    def synchronize_blockchain(self):
        self.synchronize_blockchain_called = True
        return {'blockchain_height': 100}

    def get_blockchain_height(self):
        self.get_blockchain_height_called = True
        return 100

    def __getattr__(self, name):
        return MagicMock()
