#!/usr/bin/env python3
""" In this task you will write the first unit test for
utils.access_nested_map.
Create a TestAccessNestedMap class that inherits from
unittest.TestCase.
"""
import unittest
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


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
