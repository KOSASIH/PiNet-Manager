import pytest

@pytest.fixture
def pi_network_api():
    return PiNetworkAPI()

@pytest.fixture
def pi_network_node_registration():
    return PiNetworkNodeRegistration()

@pytest.fixture
def pi_network_transaction_validation():
    return PiNetworkTransactionValidation()

@pytest.fixture
def pi_network_blockchain_synchronization():
    return PiNetworkBlockchainSynchronization()

@pytest.fixture
def pi_network_data_exchange():
    return PiNetworkDataExchange()
