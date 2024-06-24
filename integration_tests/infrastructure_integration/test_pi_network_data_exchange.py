import pytest
from pi_network_data_exchange import PiNetworkDataExchange
from infrastructureMocks.pi_network_data_exchange_mock import PiNetworkDataExchangeMock

@pytest.fixture
def pi_network_data_exchange_mock():
    return PiNetworkDataExchangeMock()

def test_pi_network_data_exchange_exchange_data(pi_network_data_exchange_mock):
    exchange = PiNetworkDataExchange()
    data = {'key': 'value'}
    exchange.exchange_data(data)
    assert pi_network_data_exchange_mock.exchange_data_called
    assert pi_network_data_exchange_mock.exchange_data == data

def test_pi_network_data_exchange_get_data(pi_network_data_exchange_mock):
    exchange = PiNetworkDataExchange()
    key = 'key'
    value = exchange.get_data(key)
    assert value == 'value'
