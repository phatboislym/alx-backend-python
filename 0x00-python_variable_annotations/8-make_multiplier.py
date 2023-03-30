#!/usr/bin/env python3
"""
module for type-annotated higher-order function make_multiplier
takes a float multiplier as argument
returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    args: multiplier: float
    return: inner: (multiplier: float)
    """
    def inner(n: float) -> float:
        """
        args: n: float
        return: x: float
        """
        x: float = (n * multiplier)
        return (x)
    return inner
