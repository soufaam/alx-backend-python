#!/usr/bin/env python3
"""This the second module 0x01-python_async_function project"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ async routine called wait_n
    Args:
        n (int): _description_
        max_delay (int): _description_

    Returns:
    list: list of all the delays
    """
    delays_list = [wait_random(max_delay) for _ in range(n)]
    delays_list = await asyncio.gather(*delays_list)
    return (delays_list)
