#!/usr/bin/env python3

"""
module for an async routine wait_n
takes two integer arguments (n, max_delay)
spawns wait_random n times with the specified max_delay
return the list of all the delays (float values) in ascending order
without using sort() because of concurrency
import wait_random from ./0-basic_async_syntax.py
"""

from asyncio import sleep
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    args: n: int, max_delay: int
    return: list_delay: List[float]
    """
    list_delay = []
    for i in range(n):
        list_delay.append(await wait_random(max_delay))
        await sleep(0.1)
    list_delay = sorted(list_delay)
    return (list_delay)
