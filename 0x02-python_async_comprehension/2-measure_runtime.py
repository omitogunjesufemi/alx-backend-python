#!/usr/bin/env python3
"""
A coroutine that will execute async_comprehension four times
in parallel using asyncio.gather

The measure_runtime should measure the total runtime and return it.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    A coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather

    The measure_runtime should measure the total runtime and return it.
    """
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time.perf_counter() - start
    return (end)
