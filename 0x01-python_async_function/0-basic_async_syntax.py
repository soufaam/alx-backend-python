#!/usr/bin/env python3
"""This the first module 0x01-python_async_function project"""
import random
import asyncio


async def wait_random(max_delay: int=10)->float:
    """This a couroutine function
    """
    random_value = random.uniform(0, max_delay)
    await asyncio.sleep(random_value)
    return random_value
