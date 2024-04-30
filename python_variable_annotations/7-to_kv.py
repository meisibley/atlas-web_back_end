#!/usr/bin/env python3
'''func to_kv take string k & int/float v as arguments and return tuple'''


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''func to_kv take string k & int/float v as arguments and return tuple'''
    toKvList = [k, float(v * v)]
    to_kv = tuple(toKvList)
    return to_kv
