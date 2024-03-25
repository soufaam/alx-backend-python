#!/usr/bin/env python3
"""ADD float module
"""
from typing import List, Tuple, Any, Sequence


def element_length(lst: Iterable[typing.Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
