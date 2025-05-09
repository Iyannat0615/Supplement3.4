import unittest
from prime_finder import is_prime, split_range

class TestPrimeFinder(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(29))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(100))

    def test_split_range_even(self):
        result = split_range(1, 100, 4)
        self.assertEqual(result, [(1, 25), (26, 50), (51, 75), (76, 100)])

    def test_split_range_uneven(self):
        result = split_range(1, 10, 3)
        self.assertEqual(result, [(1, 4), (5, 7), (8, 10)])

if __name__ == "__main__":
    unittest.main()
