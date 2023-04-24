#!/usr/bin/env python3

"""
module for a test suite for the access_nested_map function
contains a `TestAccessNestedMap` class that inherits from unittest.TestCase
"""

from parameterized import parameterized
from typing import Mapping, Sequence, Union
from unittest import TestCase
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """
    test class for the access_nested_map function
    methods:    TestAccessNestedMap.test_access_nested_map
                TestAccessNestedMap.test_access_nested_map_exception
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected_result: Union[int, str, dict, list]) -> None:
        """
        args:   self
                nested_map: Mapping
                path: Sequence
                expected_result: Union[Any]
        return: None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path) -> None:
        """
        args:   self
                nested_map: Mapping
                path: Sequence
        return: None
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
