#!/usr/bin/env python3
"""
A coroutine that takes no arguments. It would loop 10 times,
each time asynchronously wait 1 second, then yield a random
number between 0 and 10 using the random module
"""
import asyncio
from random import uniform


async def async_generator() -> float:
    """
    A coroutine that takes no arguments. It would loop 10 times,
    each time asynchronously wait 1 second, then yield a random
    number between 0 and 10 using the random module
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
