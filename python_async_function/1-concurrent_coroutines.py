#!/usr/bin/env python3
"""Import wait_random from the previous python file that you’ve written
and write an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random n times with
the specified max_delay.
wait_n should return the list of all the delays (float values). The list
of the delays should be in ascending order without using sort() because of
concurrency."""


from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''return the list of all the delays in ascending order'''
    delayList: List[float] = []
    for i in range(n):
        delayList.append(await wait_random(max_delay))

    '''sort the delayList'''
    sortedList: List[float] = []
    for i in delayList:
        min = delayList[0]
        for j in delayList:
            if min > j:
                min = j
        sortedList.append(min)
        delayList.remove(min)

    return sortedList
