#!/usr/bin/env python3

"""
module for a coroutine async_comprehension
takes no arguments
the coroutine collects 10 random numbers using an async comprehension
over async_generator, then return the 10 random numbers.
Import async_generator from the previous task and then write
"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    args: None
    return: generator: List[float]
    """
    generator: List[float] = []
    async for gen in async_generator():
        generator.append(gen)
    return (generator)
