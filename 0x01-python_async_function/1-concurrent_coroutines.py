#!/usr/bin/env python3
"""
An async routine that takes in 2 int arguments: n and max_delay.
wait_random imported, will be spawned n times with the specified
max_delay
"""
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """
    An async routine that takes in 2 int arguments: n and max_delay.
    wait_random imported, will be spawned n times with the specified
    max_delay
    """
    i = random.uniform(0, max_delay)
    results = []
    for _ in range(n):
        results.append(await wait_random(max_delay))
    return (sorted(results))
