#!/usr/bin/env python3
"""
A type-annotated function that takes a float as argument and
returns a function that multiples a float by a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A type-annotated function that takes a float as argument and
    returns a function that multiples a float by a multiplier
    """
    def func(to_be_multiplied: float) -> float:
        """
        The function of the multiplier to be returned
        """
        return (to_be_multiplied * multiplier)

    return (func)
