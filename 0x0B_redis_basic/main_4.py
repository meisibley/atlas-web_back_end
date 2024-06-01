#!/usr/bin/env python3
""" Main file """
from exercise import replay

Cache = __import__('exercise').Cache

cache = Cache()

s1 = cache.store("foo")
print(s1)
s2 = cache.store("bar")
print(s2)
s3 = cache.store(42)
print(s3)

replay(cache.store)