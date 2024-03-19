#!/usr/bin/env python3
"""This the third module 0x01-python_async_function project"""
import asyncio
import time
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """_summary_

    Args:
        max_delay (int): _description_
    """
    return asyncio.create_task(wait_random(max_delay))
