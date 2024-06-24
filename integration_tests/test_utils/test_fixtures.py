# Advanced test fixtures with cutting-edge features
import pytest
from typing import Any, Dict

@pytest.fixture
def api_client() -> Any:
    """Fixture to create an API client"""
    from pynet_manager.api import APIClient
    return APIClient()

@pytest.fixture
def mock_api_server() -> Any:
    """Fixture to create a mock API server"""
    from pynet_manager.mocks import MockAPIServer
    return MockAPIServer()

@pytest.fixture
def network_device() -> Dict[str, Any]:
    """Fixture to create a network device"""
    return {
        'name': 'Device 1',
        'ip_address': '192.168.1.1',
        'username': 'admin',
        'password': 'password'
    }

@pytest.fixture
def network_topology() -> Dict[str, Any]:
    """Fixture to create a network topology"""
    return {
        'devices': [
            {'name': 'Device 1', 'ip_address': '192.168.1.1'},
            {'name': 'Device 2', 'ip_address': '192.168.1.2'}
        ],
        'links': [
            {'device1': 'Device 1', 'device2': 'Device 2', 'interface': 'eth0'}
        ]
    }
