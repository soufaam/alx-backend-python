#!/usr/bin/env python3
"""first unit test for utils.access_nested_map"""
from unittest import TestCase
from utils import access_nested_map
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(TestCase):
    """ UnitTest Class for  utils.access_nested_map"""
    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",),  {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
            ]
                )
    def test_access_nested_map(
            self, nested_map: Mapping, path: Sequence, expected_result: Any):
        """method to test that the method returns what it is supposed"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)
