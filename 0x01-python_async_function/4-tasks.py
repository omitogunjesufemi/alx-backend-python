#!/usr/bin/env python3
"""
An asynchronous coroutine tha takes in an integer arguments
(n, max_delay) identical to wait_n except task_wait_random is called
"""
import random
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    An asynchronous coroutine tha takes in an integer arguments
    (n, max_delay) identical to wait_n except task_wait_random is called
    """
    results = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        results.append(await task)

    return (sorted(results))
