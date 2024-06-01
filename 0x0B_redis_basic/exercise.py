#!/usr/bin/env python3
""" Exercise Redis basic """
import redis
import uuid
from typing import Union, Callable


class Cache():
    """ class Cache """
    def __init__(self):
        """ store an instance of the Redis client as a private variable
        named _redis (using redis.Redis()) and flush the instance using
        flushdb.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ takes a data argument and returns a string. The method should
        generate a random key (e.g. using uuid), store the input data in
        Redis using the random key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable[[bytes], str] = None) -> str:
        """ take a key string argument and an optional Callable argument
        named fn. This callable will be used to convert the data back to
        the desired format. conserve the original Redis.get behavior if the
        key does not exist. return data stored in Redis
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ automatically parametrize Cache.get with the correct conversion
        function
        """
        return self.get(key, str)

    def get_int(self, key: int) -> int:
        """ automatically parametrize Cache.get with the correct conversion
        function
        """
        return self.get(key, int)
