import pytest
from pi_network_transaction_validation import PiNetworkTransactionValidation
from infrastructureMocks.pi_network_transaction_mock import PiNetworkTransactionMock

@pytest.fixture
def pi_network_transaction_mock():
    return PiNetworkTransactionMock()

def test_pi_network_transaction_validation_validate_transaction(pi_network_transaction_mock):
    validation = PiNetworkTransactionValidation()
    tx_data = {'tx_id': 'tx-2', 'amount': 20}
    validation.validate_transaction(tx_data)
    assert pi_network_transaction_mock.validate_transaction_called
    assert pi_network_transaction_mock.validate_transaction_data == tx_data

def test_pi_network_transaction_validation_get_transaction_status(pi_network_transaction_mock):
    validation = PiNetworkTransactionValidation()
    tx_id = 'tx-2'
    status = validation.get_transaction_status(tx_id)
    assert status == 'pending'
