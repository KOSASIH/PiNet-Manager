import pytest
from pi_network_blockchain_synchronization import PiNetworkBlockchainSynchronization
from infrastructureMocks.pi_network_blockchain_mock import PiNetworkBlockchainMock

@pytest.fixture
def pi_network_blockchain_mock():
    return PiNetworkBlockchainMock()

def test_pi_network_blockchain_synchronization_synchronize_blockchain(pi_network_blockchain_mock):
    synchronization = PiNetworkBlockchainSynchronization()
    synchronization.synchronize_blockchain()
    assert pi_network_blockchain_mock.synchronize_blockchain_called

def test_pi_network_blockchain_synchronization_get_blockchain_height(pi_network_blockchain_mock):
    synchronization = PiNetworkBlockchainSynchronization()
    height = synchronization.get_blockchain_height()
    assert height == 100
