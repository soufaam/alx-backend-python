#!/usr/bin/env python3
""" function sum_list which takes a list input_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sumlist function"""
    sum: float = 0
    for number in mxd_lst:
        sum += number
    return sum
