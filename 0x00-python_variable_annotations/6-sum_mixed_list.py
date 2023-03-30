#!/usr/bin/env python3
"""
a module for type-annotated function sum_mixed_list
takes a list mxd_lst of integers and floats
returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    args: mxd_lst: List[int|float]
    return: sums: float
    """
    sums: float = sum(mxd_lst)
    return (sums)
