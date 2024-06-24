import pytest
from pi_network_api import PiNetworkAPI
from infrastructureMocks.pi_network_api_mock import PiNetworkAPIMock

@pytest.fixture
def pi_network_api_mock():
    return PiNetworkAPIMock()

def test_pi_network_api_get_node_list(pi_network_api_mock):
    api = PiNetworkAPI()
    nodes = api.get_node_list()
    assert len(nodes) == 10
    assert nodes[0]['node_id'] == 'node-1'

def test_pi_network_api_register_node(pi_network_api_mock):
    api = PiNetworkAPI()
    node_data = {'node_id': 'node-11', 'node_type': 'full'}
    api.register_node(node_data)
    assert pi_network_api_mock.register_node_called
    assert pi_network_api_mock.register_node_data == node_data

def test_pi_network_api_validate_transaction(pi_network_api_mock):
    api = PiNetworkAPI()
    tx_data = {'tx_id': 'tx-1', 'amount': 10}
    api.validate_transaction(tx_data)
    assert pi_network_api_mock.validate_transaction_called
    assert pi_network_api_mock.validate_transaction_data == tx_data
