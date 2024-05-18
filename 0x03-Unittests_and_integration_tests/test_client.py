#!/usr/bin/env python3
"""
Module to test method: GithubOrgClient
"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch
from utils import memoize


class TestGithubOrgClient(unittest.TestCase):
    """
    Class to test method: GithubOrgClient
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json", return_value={"login": "mock_org"})
    def test_org(self, test_arg, mk):
        """Test org"""
        cl = GithubOrgClient(test_arg)
        result = cl.org
        mk.assert_called_once_with(f"https://api.github.com/orgs/{test_arg}")
        self.assertEqual(result, {"login": "mock_org"})


if __name__ == "__main__":
    unittest.main()
