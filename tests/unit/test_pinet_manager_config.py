import unittest
from pinet_manager.config import PiNetManagerConfig

class TestPiNetManagerConfig(unittest.TestCase):
    def test_load_config(self):
        config = PiNetManagerConfig()
        config.load_config('tests/fixtures/config.json')

        self.assertEqual(config.api_url, 'https://example.com/api')
        self.assertEqual(config.username, 'admin')
        self.assertEqual(config.password, 'password')

    def test_save_config(self):
        config = PiNetManagerConfig()
        config.api_url = 'https://example.com/api'
        config.username = 'admin'
        config.password = 'password'
        config.save_config('tests/fixtures/config.json')

        with open('tests/fixtures/config.json', 'r') as f:
            saved_config = json.load(f)

        self.assertEqual(saved_config['api_url'], 'https://example.com/api')
        self.assertEqual(saved_config['username'], 'admin')
        self.assertEqual(saved_config['password'], 'password')

if __name__ == '__main__':
    unittest.main()
