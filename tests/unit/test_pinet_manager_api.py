import unittest
from unittest.mock import patch, MagicMock
from pinet_manager.api import PiNetManagerAPI

class TestPiNetManagerAPI(unittest.TestCase):
    @patch('pinet_manager.api.requests')
    def test_get_device_list(self, mock_requests):
        mock_response = MagicMock()
        mock_response.json.return_value = [{'id': 1, 'name': 'Device 1'}, {'id': 2, 'name': 'Device 2'}]
        mock_requests.get.return_value = mock_response

        api = PiNetManagerAPI()
        devices = api.get_device_list()

        self.assertEqual(len(devices), 2)
        self.assertEqual(devices[0]['id'], 1)
        self.assertEqual(devices[1]['name'], 'Device 2')

    @patch('pinet_manager.api.requests')
    def test_get_device_details(self, mock_requests):
        mock_response = MagicMock()
        mock_response.json.return_value = {'id': 1, 'name': 'Device 1', 'ip_address': '192.168.1.100'}
        mock_requests.get.return_value = mock_response

        api = PiNetManagerAPI()
        device = api.get_device_details(1)

        self.assertEqual(device['id'], 1)
        self.assertEqual(device['name'], 'Device 1')
        self.assertEqual(device['ip_address'], '192.168.1.100')

if __name__ == '__main__':
    unittest.main()
