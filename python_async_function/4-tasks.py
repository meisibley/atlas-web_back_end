#!/usr/bin/env python3
'''Take the code from wait_n and alter it into a new function task_wait_n'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Take code from wait_random and into function task_wait_n'''
    delayList: List[float] = []
    for i in range(n):
        delayList.append(wait_random(max_delay))

    doneList: List[float] = []
    for j in asyncio.as_completed(delayList):
        '''waiting for as_completed return'''
        doneItem = await j
        doneList.append(doneItem)

    return (sorted(doneList))
