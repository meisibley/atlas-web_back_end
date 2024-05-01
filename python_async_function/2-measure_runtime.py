#!/usr/bin/env phthon3
'''Create a measure_time function with integers n and max_delay
as arguments that measures the total execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should return a float.
Use the time module to measure an approximate elapsed time.'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''measure the execution time for wait_n and reture total_time/n'''
    startTime = time.time()
    asyncio.run(wait_n(n, max_delay))
    endTime = time.time()
    total_time = endTime - startTime
    return (total_time / n)
