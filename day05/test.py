import unittest
from day5 import scan_boarding_pass


class TestDay5(unittest.TestCase):
    def test_scan_boarding_pass(self):
        self.assertEqual(
            scan_boarding_pass("FBFBBFFRLR", (0, 127), (0, 7)), (44, 5, 357)
        )
        self.assertEqual(
            scan_boarding_pass("BFFFBBFRRR", (0, 127), (0, 7)), (70, 7, 567)
        )
        self.assertEqual(
            scan_boarding_pass("FFFBBBFRRR", (0, 127), (0, 7)), (14, 7, 119)
        )
        self.assertEqual(
            scan_boarding_pass("BBFFBBFRLL", (0, 127), (0, 7)), (102, 4, 820)
        )


if __name__ == "__main__":
    unittest.main()