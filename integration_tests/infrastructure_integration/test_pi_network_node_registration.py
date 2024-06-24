import pytest
from pi_network_node_registration import PiNetworkNodeRegistration
from infrastructureMocks.pi_network_node_mock import PiNetworkNodeMock

@pytest.fixture
def pi_network_node_mock():
    return PiNetworkNodeMock()

def test_pi_network_node_registration_register_node(pi_network_node_mock):
    registration = PiNetworkNodeRegistration()
    node_data = {'node_id': 'node-12', 'node_type': 'full'}
    registration.register_node(node_data)
    assert pi_network_node_mock.register_node_called
    assert pi_network_node_mock.register_node_data == node_data

def test_pi_network_node_registration_get_node_info(pi_network_node_mock):
    registration = PiNetworkNodeRegistration()
    node_id = 'node-12'
    node_info = registration.get_node_info(node_id)
    assert node_info['node_id'] == node_id
    assert node_info['node_type'] == 'full'
