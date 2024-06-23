import unittest
from unittest.mock import patch, MagicMock
from pinet_manager.cli import PiNetManagerCLI

class TestPiNetManagerCLI(unittest.TestCase):
    @patch('pinet_manager.cli.argparse')
    def test_parse_args(self, mock_argparse):
        mock_parser = MagicMock()
        mock_argparse.ArgumentParser.return_value = mock_parser
        mock_parser.parse_args.return_value = {'config': 'tests/fixtures/config.json'}

        cli = PiNetManagerCLI()
        args = cli.parse_args()

        self.assertEqual(args.config, 'tests/fixtures/config.json')

    @patch('pinet_manager.cli.PiNetManagerAPI')
    def test_run(self, mock_api):
        mock_api_instance = MagicMock()
        mock_api.return_value = mock_api_instance
        mock_api_instance.get_device_list.return_value = [{'id': 1, 'name': 'Device 1'}]

        cli = PiNetManagerCLI()
        cli.run(['--config', 'tests/fixtures/config.json'])

        mock_api_instance.get_device_list.assert_called_once()

if __name__ == '__main__':
    unittest.main()
