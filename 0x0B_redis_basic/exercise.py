#!/usr/bin/env python3
""" Exercise Redis basic """
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ count_calls decorator that takes a single method Callable argument
    and returns a Callable.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ wrapper func keeps count value not lose. self is call itself """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ decorator to store the history of inputs and outputs for a particular
    function """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Execute the wrapped function to retrieve the output. Store the
        output using rpush in the "...:outputs" list, then return the output
        """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper

        
class Cache():
    """ class Cache """
    def __init__(self):
        """ store an instance of the Redis client as a private variable
        named _redis (using redis.Redis()) and flush the instance using
        flushdb.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
