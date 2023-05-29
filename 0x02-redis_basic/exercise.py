#!/usr/bin/env python3
""" Module contaning simple tasks for redis project
"""

from typing import Any, Union, Callable
from functools import wraps
import uuid
import redis


def count_calls(method: Callable) -> Callable:
    """ Decorator for Cache.store
        Count the number of calls for this method
    """
    @wraps(method)
    def for_each_call(self, *args, **kwargs):
        """ Wrapped function for the decorator
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return for_each_call


def call_history(method: Callable) -> Callable:
    """ Decorator for Cache.store
        Store input and output params for Cache.store in redis
    """
    @wraps(method)
    def for_each_call(self, *args, **kwargs):
        """ Wrapped function for the decorator
        """
        key_input = method.__qualname__ + ":inputs"
        key_output = method.__qualname__ + ":outputs"
        self._redis.rpush(key_input, str(args))
        output: Any = method(self, *args, **kwargs)
        self._redis.rpush(key_output, str(output))
        return output

    return for_each_call


def replay(method: Callable) -> Callable:
    """ Display history of calls of a function
    """
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name).decode("utf-8")
    print("{} was called {} times:".format(name, calls))
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, i.decode("utf-8"),
              o.decode("utf-8")))


class Cache:
    def __init__(self) -> None:
        """ Initialize the Cache class with an instance of redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in the redis cache 
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable[[Any], Any] = None) -> Any:
        """ Get item from db and call fn to convert it from byte to datatype
        """
        value: bytes = self._redis.get(key)
        if fn:
            return fn(value)
        else:
            return value

    def get_str(self, key: str) -> str:
        """ Call get function with string class
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ Call get function with int class
        """
        return self.get(key, int)
