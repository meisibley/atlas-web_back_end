#!/usr/bin/env python3
""" declare the TestGithubOrgClient class and implement test_org method """
from unittest import mock
from client import GithubOrgClient
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(GithubOrgClient):
    """ child class to test GithubOrgClient class methods """
    @patch("client.get_json", return_value={"payload": True})
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    def test_org(self, org, mock_get_json):
        """ test GithubOrgClient.org and returns the correct value """
        test_client = GithubOrgClient(org)
        test_return = test_client.org
        self.assertEqual(test_return, mock_get_json.return_value)
