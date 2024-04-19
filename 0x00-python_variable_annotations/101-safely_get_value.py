#!/usr/bin/env python3
"""
Adding type annotations to a function using TypeVar
"""
from typing import TypeVar, Optional, Any, Mapping, Union


T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Adding type annotations to a function using TypeVar
    """
    if key in dct:
        return dct[key]
    else:
        return default
