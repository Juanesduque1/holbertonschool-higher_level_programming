"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_at_the_end(self):
        """Test case for when max integer is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_the_beginning(self):
        """Test case for when max integer is at the beginning"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_at_the_beginning(self):
        """Test case for when max integer is in the middle"""
        self.assertEqual(max_integer([3, 4, 2, 1]), 4)

    def test_max_at_the_beginning(self):
        """Test case for when one negative number is on the list"""
        self.assertEqual(max_integer([-1, 2, 3, 4]), 4)

    def test_max_at_the_beginning(self):
        """Test case for a list with only negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_max_at_the_beginning(self):
        """Test case for a list with only one element"""
        self.assertEqual(max_integer([4]), 4)

    def test_max_at_the_beginning(self):
        """Test case for an empty list"""
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
