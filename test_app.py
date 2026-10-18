import unittest
from app import calculate_total, check_access, find_average


class TestBugBash(unittest.TestCase):

    def test_calculate_total(self):
        # Should add tax, not subtract
        self.assertEqual(calculate_total(100, 18), 118)

    def test_check_access(self):
        # 18-year-olds should be granted access (edge case)
        self.assertEqual(check_access(18), "Access Granted")
        self.assertEqual(check_access(17), "Access Denied")

    def test_find_average(self):
        # Should handle normal list and empty list properly
        self.assertEqual(find_average([10, 20, 30]), 20)
        self.assertEqual(find_average([]), 0)


if __name__ == "__main__":
    unittest.main()
