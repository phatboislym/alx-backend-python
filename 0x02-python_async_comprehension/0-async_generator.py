#!/usr/bin/env python3

"""
module for a coroutine async_generator
takes no arguments
the coroutine loops 10 times, each time asynchronously wait 1 second
then yields a random number between 0 and 10
uses the random module
"""

from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    args: None
    return: Generator[float, None, None]
    """
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
