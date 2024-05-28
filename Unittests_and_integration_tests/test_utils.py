#!/usr/bin/env python3
""" In this task you will write the first unit test for
utils.access_nested_map.
Create a TestAccessNestedMap class that inherits from
unittest.TestCase.
"""
from unittest import TestCase, mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(TestCase):
    """ Implement the TestAccessNestedMap.test_access_nested_map method to
    test that the method returns what it is supposed to.
    Decorate the method with @parameterized.expand to test the function for
    following inputs:
    nested_map={"a": 1}, path=("a",)
    nested_map={"a": {"b": 2}}, path=("a",)
    nested_map={"a": {"b": 2}}, path=("a", "b")
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, map, path, result):
        """ For each of these inputs, test with assertEqual that the function
        returns the expected result.
        """
        self.assertEqual(access_nested_map(map, path), result)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, map, path):
        """ Use the assertRaises context manager to test that a KeyError is
        raised for the following inputs:
        nested_map={}, path=("a",)
        nested_map={"a": 1}, path=("a", "b")
        """
        self.assertRaises(KeyError, access_nested_map, map, path)


class TestGetJson(TestCase):
    """ inherits class unittest.TestCase """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @mock.patch('test_utils.get_json')
    def test_get_json(self, test_url, test_payload, mock_get_json):
        """ implement this method to test that utils.get_json returns
        the expected result.
        """
        mock_get_json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
