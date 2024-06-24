import json
from unittest.mock import MagicMock

class PiNetworkNodeMock:
    def __init__(self):
        self.register_node_called = False
        self.get_node_info_called = False

    def register_node(self, node_data):
        self.register_node_called = True
        self.register_node_data = node_data
        return {'node_id': 'node-12', 'node_type': 'full'}

    def get_node_info(self, node_id):
        self.get_node_info_called = True
        return {'node_id': node_id, 'node_type': 'full', 'tatus': 'online'}

    def __getattr__(self, name):
        return MagicMock()
