#!/usr/bin/env python3
'''function sum_list takes float input_list as argument and returns sum'''


from typing import List


def sum_list(input_list: List[float]) -> float:
    '''function sum_list takes input_list float list and returns sum'''
    listSum = 0.0
    for listItem in input_list:
        listSum += listItem
    return listSum
