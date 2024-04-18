#!/usr/bin/env python3
"""
A type-annotated function that takes a list and
returns the first element
"""
from typing import List, Any, Union, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    A type-annotated function that takes a list and returns
    the first element
    """
    if lst:
        return lst[0]
    else:
        return None
