"""
module for a function `measure_time`
takes two integers, n and max_delay as arguments
measures the total execution time for `wait_n(n, max_delay)`
returns (total_time / n): float
uses the time module to measure an approximate elapsed time
import wait_n from 1-concurrent_coroutines
"""

from asyncio import run
from time import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    args: n: int
        max_delay: int
    return: average_time: float
    """
    start: float = time()
    list_delay: List[float] = run(wait_n(n, max_delay))
    end: float = time()
    duration: float = (end - start)
    average_time: float = (duration / n)

    return (average_time)
