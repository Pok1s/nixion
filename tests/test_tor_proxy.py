# test_tor_proxy.py
import unittest
from tor_proxy.tor_proxy import setup_tor_proxy

class TestTorProxy(unittest.TestCase):
    def test_setup_tor_proxy(self):
        setup_tor_proxy()
        # We should add checks to confirm that Tor is being used, e.g., through requests

if __name__ == '__main__':
    unittest.main()
