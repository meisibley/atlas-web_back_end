#!/usr/bin/env python3
'''function sum_list takes float input_list as argument and returns sum'''


def sum_list(input_list: float) -> float:
    listSum = 0.0
    for listItem in input_list:
        listSum += listItem
    return listSum
