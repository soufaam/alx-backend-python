#!/usr/bin/env python3
"""ADD float module
"""
from typing import List, Tuple, Any, Sequence, Iterable, Union


def safe_first_element(lst: Iterable[Any]) -> Union[Any, type(None)]:
    """    The types of the elements of the input are not know"""
    if lst:
        return lst[0]
    else:
        return None
