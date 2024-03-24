#!/usr/bin/env python3
# """ function sum_list which takes a list input_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sumlist function"""
    sum: float = 0
    for number in input_list:
        sum += number
    return sum
