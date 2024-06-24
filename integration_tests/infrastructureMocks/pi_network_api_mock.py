import json
from unittest.mock import MagicMock

class PiNetworkAPIMock:
    def __init__(self):
        self.get_node_list_called = False
        self.register_node_called = False
        self.validate_transaction_called = False
        self.get_transaction_status_called = False

    def get_node_list(self):
        self.get_node_list_called = True
        return [
            {'node_id': 'node-1', 'node_type': 'full'},
            {'node_id': 'node-2', 'node_type': 'light'},
            #...
        ]

    def register_node(self, node_data):
        self.register_node_called = True
        self.register_node_data = node_data
        return {'node_id': 'node-11', 'node_type': 'full'}

    def validate_transaction(self, tx_data):
        self.validate_transaction_called = True
        self.validate_transaction_data = tx_data
        return {'tx_id': 'tx-1', 'amount': 10, 'tatus': 'pending'}

    def get_transaction_status(self, tx_id):
        self.get_transaction_status_called = True
        return {'tx_id': tx_id, 'tatus': 'confirmed'}

    def __getattr__(self, name):
        return MagicMock()
