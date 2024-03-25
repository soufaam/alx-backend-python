#!/usr/bin/env python3
"""ADD float module
"""
from typing import List, Any, Union, Mapping, TypeVar


T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any, default: Union[T, type(None)] =
                     None) -> Union[Any, T]:
    
    """ docmention of this function"""
    if key in dct:
        return dct[key]
    else:
        return default
