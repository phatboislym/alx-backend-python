#!/usr/bin/env python3

"""
module for a coroutine, measure_runtime
takes no arguments
that executes async_comprehension four times in parallel using asyncio.gather
returns the total runtime
import async_comprehension from 1-async_comprehension
"""

from asyncio import create_task, gather, Task
from time import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    args: None
    return: total_runtime: float
    """
    start = time()
    gen: List[Task] = []
    for _ in range(4):
        gen.append(create_task(async_comprehension()))
    await gather(*gen)
    end = time()
    total_runtime: float = (end - start)
    return (total_runtime)
