# test_ai_optimizer.py
import unittest
import numpy as np
from ai_optimizer.ai_optimizer import AINetworkOptimizer

class TestAINetworkOptimizer(unittest.TestCase):
    def setUp(self):
        self.optimizer = AINetworkOptimizer()
        self.data = np.array([[1, 2], [2, 3], [1, 1], [10, 10]])
        self.optimizer.train(self.data)

    def test_detect_anomalies(self):
        anomalies = self.optimizer.detect_anomalies(self.data)
        self.assertIn(True, anomalies)  # Expect at least one anomaly

if __name__ == '__main__':
    unittest.main()
