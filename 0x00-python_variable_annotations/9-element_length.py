#!/usr/bin/env python3
"""
A type-annotated function that takes a list and returns
a list of tuples
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A type-annotated function that takes a list and returns
    a list of tuples
    """
    return [(i, len(i)) for i in lst]
