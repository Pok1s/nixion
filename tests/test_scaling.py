# test_scaling.py
import unittest
from scaling.scaling import AutoScaler
import time

class TestAutoScaler(unittest.TestCase):
    def setUp(self):
        self.scaler = AutoScaler()

    def test_scale_up(self):
        initial_resources = self.scaler.current_resources
        self.scaler.scale_up()
        self.assertGreater(self.scaler.current_resources, initial_resources)

    def test_scale_down(self):
        self.scaler.scale_up()  # Make sure we have at least 2 resources to scale down
        initial_resources = self.scaler.current_resources
        self.scaler.scale_down()
        self.assertLess(self.scaler.current_resources, initial_resources)

if __name__ == '__main__':
    unittest.main()
