#!/usr/bin/env python3
"""
module for type annotated function safely_get_value
takes a dictionary, a key of unknown type and default set to None
returns the value for the key if it exists in the dict, else the default param
"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default=Union[T, None]) -> Union[Any, T]:
    """
    args: dct: dict
        key: T
        default: None|T
    return: value: T if key exists in dict, else None| default: T
    """
    if key in dct:
        return (dct[key])
    else:
        return (default)
