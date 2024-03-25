#!/usr/bin/env python3
"""ADD float module
"""
from typing import List, Tuple, Any, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function element_lenght"""
    return [(i, len(i)) for i in lst]
