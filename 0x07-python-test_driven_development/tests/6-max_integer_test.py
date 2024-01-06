#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])"""

    def test_list_inorder(self):
        """Test the list in order."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_notordered_list(self):
        """Test the list when not in order."""
        notordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(notordered), 4)

    def test_max_at_start(self):
        """Test a list with a max value at start."""
        max_at_start = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_start), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_elem_list(self):
        """Test a list with one element."""
        one_elem = [4]
        self.assertEqual(max_integer(one_elem), 4)

    def test_float_num(self):
        """Test a list with float numbers."""
        float_num = [2.53, 8.33, -7.123, 20.4, 5.0]
        self.assertEqual(max_integer(float_num), 20.4)

    def test_int_float(self):
        """Test a list with both ints and floats."""
        int_float = [2.53, 20.5, -7, 20, 8]
        self.assertEqual(max_integer(int_float), 20.5)

    def test_string(self):
        """Tests a string."""
        string = "Brand"
        self.assertEqual(max_integer(string), 'r')

    def test_string_list(self):
        """Test a list with strings."""
        string_list = ["Brand", "is", "awesome"]
        self.assertEqual(max_integer(string_list), "is")

    def test_empty_str(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
