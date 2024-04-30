#!/usr/bin/env python3
'''func sum_mixed_list takes a ints and floats mxd_lst, returns float sum'''


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''func sum_mixed_list take ints and floats mxd_lst return float sum'''
    return sum(mxd_lst)
