#!/usr/bin/env python3
"""ADD float module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ an anotated function function"""
    def mult(nbr: float) -> float:
        """function that multiple a nbr by multiplier"""
        return multiplier * nbr
    return mult
