import unittest
from calculator import calculate_total


class TestCalculator(unittest.TestCase):

    def test_normal_calculation(self):
        self.assertEqual(calculate_total(500, 2), 1000)

    def test_zero_quantity(self):
        self.assertEqual(calculate_total(500, 0), 0)


if __name__ == "__main__":
    unittest.main()