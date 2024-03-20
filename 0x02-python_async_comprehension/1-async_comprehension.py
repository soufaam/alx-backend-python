#!/usr/bin/env python3
"""This the third module 0x01-python_async_function project"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """_summary_

    Returns:
        List[float]: _description_
    """
    result = [number async for number in async_generator()]
    return result
