#!/usr/bin/env python3

"""
module for a function task_wait_random
takes an integer max_delay
returns a asyncio.Task
import wait_random from 0-basic_async_syntax
"""

from asyncio import create_task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """
    args: max_delay: int
    return: task: asyncio.Task
    """
    task = create_task(wait_random(max_delay))
    return (task)
