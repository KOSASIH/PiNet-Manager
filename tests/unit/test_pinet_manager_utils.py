import unittest
from pinet_manager.utils import validate_ip_address

class TestPiNetManagerUtils(unittest.TestCase):
    def test_validate_ip_address(self):
        self.assertTrue(validate_ip_address('192.168.1.100'))
        self.assertFalse(validate_ip_address('256.1.1.1'))
        self.assertFalse(validate_ip_address('abc.def.ghi.jkl'))

if __name__ == '__main__':
    unittest.main()
