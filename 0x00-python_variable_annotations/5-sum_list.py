#!/usr/bin/env python3
"""
A type-annotated function which takes a list of floats as arguments
and returns their sum as a float
"""
from typing import List

def sum_list(input_list: List[float] ) -> float:
    """
    A type-annotated function which takes a list of floats as arguments
    and returns their sum as a float
    """
    total: float = 0.0
    for element in input_list:
        total += element
    return total
