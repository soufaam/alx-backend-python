#!/usr/bin/env python3
"""This the third module 0x01-python_async_function project"""
import asyncio
import time
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ async routine called wait_n
    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
    list: list of all the delays
    """
    delays_list = [task_wait_random(max_delay) for _ in range(n)]
    delays_list = await asyncio.gather(*delays_list)
    return sorted(delays_list)
