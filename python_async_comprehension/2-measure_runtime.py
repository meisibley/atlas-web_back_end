#!/usr/bin/env python3
'''Import async_comprehension from the previous file and write
a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it..'''


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure_runtime coroutine execute async_comprehension four times
    in parallel using asyncio.gather and return the runtime'''
    startTime = time.time()
    runtime = [async_comprehension() for i in range(4)]
    await asyncio.gather(*runtime)
    endTime = time.time()

    return endTime - startTime

'''Notice that the total runtime is roughly 10 seconds, why?
function measure_runtime called async_comprehension 4 times,
so, async_comprehention called async_generator 4 times,
each async_generator running time: sleeping 1s and running roughly 0.5s,
each calling spent roughly 0.5 second,
so, 1+1+1+1+0.5+0.5+0.5+0.5 + 4*0.5 + 4*0.5 = 10 seconds'''
