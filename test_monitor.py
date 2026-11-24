import unittest
from monitor import get_server_metrics

class TestMonitor(unittest.TestCase):
    def test_get_server_metrics(self):
        metrics = get_server_metrics()
        self.assertIsInstance(metrics, dict)
        self.assertIn("CPU", metrics)
        self.assertIn("RAM", metrics)
        self.assertIn("Disk", metrics)
        for metric, usage in metrics.items():
            with self.subTest(metric=metric):
                self.assertIsInstance(usage, (int,float))
                self.assertGreaterEqual(usage, 0)
                self.assertLessEqual(usage, 100)

if __name__ == '__main__':
    unittest.main()                