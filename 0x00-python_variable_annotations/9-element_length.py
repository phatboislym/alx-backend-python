#!/usr/bin/env python3
"""
module for type-annotated function element_length
takes an iterable (List, Sequence, Tuple) as argument
returns a list of tuples containing a sequence and an int
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    args: lst: Iterable[Sequence]
    return: List[Tuple[Sequence, int]]
    """
    return [(i, len(i)) for i in lst]
