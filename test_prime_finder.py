"""
test_prime_finder.py

Author: [Iyanna Thweatt]
Date: [5/8/2025}

Description:
------------
Unit tests for the `prime_finder` module.
These tests verify the correctness of:
- Prime number checking (is_prime)
- Range splitting logic (split_range)

Run tests:
----------
    python -m unittest test_prime_finder.py
"""

import unittest
from prime_finder import is_prime, split_range


class TestPrimeFunctions(unittest.TestCase):
    """
    Unit tests for prime checking and range splitting.
    """

    def test_is_prime_basic(self):
        """
        Test the is_prime() function with known values.
        """
        self.assertFalse(is_prime(0), "0 is not prime")
        self.assertFalse(is_prime(1), "1 is not prime")
        self.assertTrue(is_prime(2), "2 is prime")
        self.assertTrue(is_prime(3), "3 is prime")
        self.assertFalse(is_prime(4), "4 is not prime")
        self.assertTrue(is_prime(5), "5 is prime")
        self.assertFalse(is_prime(9), "9 is not prime")
        self.assertTrue(is_prime(13), "13 is prime")

    def test_split_range_even(self):
        """
        Test split_range() on a range divisible evenly by the number of chunks.
        """
        result = split_range(1, 9, 2)
        expected = [(1, 5), (5, 9)]
        self.assertEqual(result, expected)

    def test_split_range_uneven(self):
        """
        Test split_range() when the range is not evenly divisible.
        """
        result = split_range(1, 10, 3)
        expected = [(1, 4), (4, 7), (7, 10)]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
