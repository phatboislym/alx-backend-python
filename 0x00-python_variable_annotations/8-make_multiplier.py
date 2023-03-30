#!/usr/bin/env python3
from typing import Callable
"""
module for type-annotated higher-order function make_multiplier
takes a float multiplier as argument
returns a function that multiplies a float by multiplier
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    args: multiplier: float
    return: inner: (multiplier: float) -> x: float
    """
    def inner(multiplier: float) -> float:
        x: float = (multiplier * multiplier)
        return (x)
    return inner
