#!/usr/bin/env python3
""" Module contaning simple tasks for redis project
"""

from typing import Any, Union, Callable
from functools import wraps
import uuid
import redis


def count_calls(method: Callable) -> Callable:
    """ Decorator for class Cache
    """
    @wraps(method)
    def for_each_call(self, *args, **kwargs):
        """ Wrapped function for the decorator
        """
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return for_each_call

@count_calls
class Cache:
    def __init__(self) -> None:
        """ Initialize the Cache class
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in the redis db
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
