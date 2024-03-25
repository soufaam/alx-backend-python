#!/usr/bin/env python3
"""ADD float module
"""
from typing import List, Typle, Any, Sequence


def element_length(lst: Sequence) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
