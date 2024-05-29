#!/usr/bin/env python3
""" declare the TestGithubOrgClient class and implement test_org method """
import unittest
from unittest import mock
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """ method to unit-test GithubOrgClient._public_repos_url """
        with patch.object(GithubOrgClient,
                          "org",
                          new_callable=PropertyMock,
                          return_value={"repos_url": "atlas"}) as mock_org:
            test_json = {"repos_url": "atlas"}
            test_client = GithubOrgClient(test_json.get("repos_url"))
            test_return = test_client._public_repos_url
            self.assertEqual(test_return,
                             mock_org.return_value.get("repos_url"))

    @patch("client.get_json", return_value=[{"name": "atlas"}])
    def test_public_repos(self, mock_get_json):
        """ unit-test GithubOrgClient.public_repos method """
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_callable=PropertyMock,
                          return_value={"https://api.github.com/"}) as mock_v:
            test_client = GithubOrgClient("atlas")
            test_return = test_client.public_repos()
            self.assertEqual(test_return, ["atlas"])
            mock_get_json.assert_called_once
            mock_v.assert_called_once
