#!/usr/bin/env python3
"""
module for type-annotated function to_kv
takes a string k and an int OR float v as arguments
returns a tuple. The first element of the tuple is the string k
The second element is the square of the int/float v annotated as a float
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    args: k: str
        v: int|float
    return: tup: Tuple[str, float]
    """
    tup = (k, (v * v))
    return (tup)
