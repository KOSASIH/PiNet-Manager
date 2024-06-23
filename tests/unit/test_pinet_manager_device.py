import unittest
from pinet_manager.device import PiNetManagerDevice

class TestPiNetManagerDevice(unittest.TestCase):
    def test_init(self):
        device = PiNetManagerDevice({'id': 1, 'name': 'Device 1', 'ip_address': '192.168.1.100'})

        self.assertEqual(device.id, 1)
        self.assertEqual(device.name, 'Device 1')
        self.assertEqual(device.ip_address, '192.168.1.100')

    def test_repr(self):
        device = PiNetManagerDevice({'id': 1, 'name': 'Device 1', 'ip_address': '192.168.1.100'})

        self.assertEqual(repr(device), '<PiNetManagerDevice: Device 1 (192.168.1.100)>')

if __name__ == '__main__':
    unittest.main()
