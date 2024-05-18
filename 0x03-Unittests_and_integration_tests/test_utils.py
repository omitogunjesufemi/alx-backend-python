#!/usr/bin/env python3
"""
Module to test method: access nested map
"""
import unittest
import utils
from parameterized import parameterized
from unittest.mock import patch
from utils import memoize


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
        """ Testing the access_nested_map method """
        result = utils.access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Testing KeyError is raised for the inputs """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class for get_json method"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mk_get):
        """Test that get_json returns the expected result: a json"""
        mk_get.return_value.json.return_value = test_payload
        response = utils.get_json(test_url)
        mk_get.assert_called_once_with(test_url)
        self.assertEqual(test_payload, response)


class TestClass:
    """Test Class"""
    def a_method(self):
        """a_method"""
        return 42

    @memoize
    def a_property(self):
        """Memoized method"""
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """Memoization"""
    @patch("test_utils.TestClass.a_method")
    def test_memoize(self, mock_method):
        """Test memoization"""
        tst = TestClass()
        tst.a_property()
        tst.a_property()
        mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
