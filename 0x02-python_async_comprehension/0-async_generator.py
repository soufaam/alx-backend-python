#!/usr/bin/env python3
"""This the third module 0x01-python_async_function project"""
import asyncio
import random


async def async_generator():
    """coroutine
    """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
