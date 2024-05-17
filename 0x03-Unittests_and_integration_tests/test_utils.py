#!/usr/bin/env python3
"""
Module to test method: access nested map
"""
import unittest
import utils
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Class to test method: access nested map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Testing the access_nested_map method"""
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
