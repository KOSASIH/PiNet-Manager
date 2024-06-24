import json
from unittest.mock import MagicMock

class PiNetworkTransactionMock:
    def __init__(self):
        self.validate_transaction_called = False
        self.get_transaction_status_called = False

    def validate_transaction(self, tx_data):
        self.validate_transaction_called = True
        self.validate_transaction_data = tx_data
        return {'tx_id': 'tx-2', 'amount': 20, 'tatus': 'pending'}

    def get_transaction_status(self, tx_id):
        self.get_transaction_status_called = True
        return {'tx_id': tx_id, 'tatus': 'confirmed'}

    def __getattr__(self, name):
        return MagicMock()
