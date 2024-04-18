#!/usr/bin/env python3
"""
A type-annotated function which takes a list of integers and
floats as arguments and returns their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    A type-annotated function which takes a list of integers and
    floats as arguments and returns their sum as a float
    """
    total: float = 0.0
    for element in mxd_lst:
        total += element
    return total
