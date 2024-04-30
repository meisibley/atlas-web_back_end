#!/usr/bin/env python3
"""Annotate function’s parameters & return values w/ appropriate types"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return a list of tuples, tuple(value, value length)"""
    return [(i, len(i)) for i in lst]
