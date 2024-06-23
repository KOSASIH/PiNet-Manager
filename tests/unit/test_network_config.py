import unittest
from pi_net_manager.core.network_config import NetworkConfig

class TestNetworkConfig(unittest.TestCase):
    def test_set_ip_address(self):
        network_config = NetworkConfig()
        network_config.set_ip_address("192.168.1.100")
        self.assertEqual(network_config.ip_address, "192.168.1.100")

    def test_get_ip_address(self):
        network_config = NetworkConfig()
        network_config.set_ip_address("192.168.1.100")
        self.assertEqual(network_config.get_ip_address(), "192.168.1.100")
