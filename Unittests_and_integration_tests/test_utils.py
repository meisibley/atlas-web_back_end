#!/usr/bin/env python3
""" In this task you will write the first unit test for
utils.access_nested_map.
Create a TestAccessNestedMap class that inherits from
unittest.TestCase.
"""
from unittest import TestCase, mock
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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


class TestMemoize(TestCase):
    """ test utils.memoize """
    def test_memoize(self):
        """ Use unittest.mock.patch to mock a_method. Test that when calling
        a_property twice, the correct result is returned but a_method is only
        called once using assert_called_once."""
        class TestClass:
            """ memoization """
            def a_method(self):
                """ a mock method """
                return 42

            @memoize
            def a_property(self):
                """ a mock property get a_method value """
                return self.a_method()
        with mock.patch.object(TestClass, 'a_method') as mock_a_method:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            mock_a_method.assert_called_once()
