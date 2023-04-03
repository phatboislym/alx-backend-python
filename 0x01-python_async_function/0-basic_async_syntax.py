#!/usr/bin/env python3

"""
module for the asynchronous coroutine wait_random
takes an integer argument, max_delay, with a default value of 10
waits for a random delay between 0 and max_delay (included and float value)
returns random delay
uses the random module
"""

from asyncio import sleep
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    args: max_delay: int
    return: random_delay: float
    """
    random_delay = uniform(0.0, max_delay)
    await sleep(random_delay)
    return (random_delay)
