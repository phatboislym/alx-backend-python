#!/usr/bin/env python3

"""
module for an async routine `task_wait_n`
takes two integer arguments (n, max_delay)
spawns `task_wait_random` n times with the specified max_delay
return the list of all the asyncio.Task objects
import task_wait_random from 3-tasks.py
"""

from asyncio import sleep
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    args: n: int, max_delay: int
    return: list_delay: List[Any]
    """
    list_tasks = []
    for i in range(n):
        list_tasks.append(await task_wait_random(max_delay))
        await sleep(0.1)
    list_tasks = sorted(list_tasks)
    return (list_tasks)
