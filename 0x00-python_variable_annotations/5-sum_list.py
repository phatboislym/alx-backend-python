#!/usr/bin/env python3
"""
module for a type-annotated function sum_list
takes a list input_list of floats as argument
returns their sum as a float
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    args: input_list: list[float]
    return: sum_of_elements: float
    """
    sum_of_elements: float = sum(input_list)
    return (sum_of_elements)
