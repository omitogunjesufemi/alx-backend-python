#!/usr/bin/env python3
"""
A type-annotated function that takes a Tuple and Integer as arguments
and returns a Tuple
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    A type-annotated function that takes a Tuple and Integer as arguments
    and returns a Tuple
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))
