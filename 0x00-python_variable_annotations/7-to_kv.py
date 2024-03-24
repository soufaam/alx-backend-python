#!/usr/bin/env python3
"""ADD float module
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ an anotated function function"""
    return (k, v**2)
