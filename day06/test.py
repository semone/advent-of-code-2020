import unittest
from day6 import custom_scan


class TestDay5(unittest.TestCase):
    def test_scan_boarding_pass(self):
        self.assertEqual(custom_scan("abc"), 3)
        self.assertEqual(custom_scan("abc"), 3)
        self.assertEqual(custom_scan("abac"), 3)
        self.assertEqual(custom_scan("aaaa"), 1)
        self.assertEqual(custom_scan("b"), 1)


if __name__ == "__main__":
    unittest.main()