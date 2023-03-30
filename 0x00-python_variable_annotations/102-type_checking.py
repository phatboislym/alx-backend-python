#!/usr/bin/env python3
"""
module for type annotated function zoom_array
takes list: Tuple[Any]
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return (zoomed_in)


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
