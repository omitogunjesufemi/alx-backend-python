#!/usr/bin/env python3
"""
A type-annotated function which takes a string and an int OR
float as arguments and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str,  float]:
    """
    A type-annotated function which takes a string and an int OR
    float as arguments and returns a tuple. The first element of
    the tuple is the string k. The second element is the square
    of the int/float v and should be annotated as a float.
    """
    v *= v
    return ((k, v))
