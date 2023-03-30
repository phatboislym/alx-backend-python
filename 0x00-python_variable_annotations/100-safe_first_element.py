#!/usr/bin/env python3
"""
module for type annotated function safe_first_element
takes a list input param of unknown element type
returns the first element in the list or None
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    args: lst: Sequence[Any]
    return: lst[0]: or None
    """
    if lst:
        return lst[0]
    else:
        return None
