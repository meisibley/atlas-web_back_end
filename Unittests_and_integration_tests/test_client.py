#!/usr/bin/env python3
""" declare the TestGithubOrgClient class and implement test_org method """
import unittest
from unittest import mock
from client import GithubOrgClient
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ child class of unittest.TestCase class methods """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org_name, mock_get_json):
        """ test GithubOrgClient.org and returns the correct value """
        test_client = GithubOrgClient(org_name)
        test_return = test_client.org
        self.assertEqual(test_return, mock_get_json.return_value)
        mock_get_json.assert_called_once
