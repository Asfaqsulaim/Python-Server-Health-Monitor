import unittest
from alerts import check_usage

class TestAlerts(unittest.TestCase):
    def test_check_usage_high(self):
        result = check_usage("CPU", 95, 80)
        self.assertIn("Warning:", result)
        self.assertIn("Optimize CPU usage", result)

    def test_check_usage_ram(self):
        result = check_usage("RAM", 90, 75)
        self.assertIn("Warning:", result) 
        self.assertIn("Close unnecessary applications", result)  

    def test_check_usage_disk(self):
        result = check_usage("Disk", 95, 90)
        self.assertIn("Warning:", result)
        self.assertIn("Free up Disk Space", result)
    

    def test_check_usage_normal(self):
        result = check_usage("CPU", 50, 80)
        self.assertIn("Normal:", result)
        self.assertIn("No action needed", result)  

    def test_usage_at_limit(self):
        result = check_usage("CPU", 80, 80)
        self.assertIn("Normal:", result)
        self.assertIn("No action needed", result)      
if __name__ == "__main__":
    unittest.main()