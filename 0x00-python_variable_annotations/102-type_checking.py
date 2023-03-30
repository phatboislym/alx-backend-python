#!/usr/bin/env python3
"""
module for type annotated function zoom_array
takes lst of type List and factor of type int as params
returns object of type List
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    args: lst: Tuple
        factor: int
    return: zoomed_in: List
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return (zoomed_in)


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
