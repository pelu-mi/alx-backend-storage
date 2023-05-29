#!/usr/bin/env python3
""" Module contaning simple tasks for redis project
"""

from typing import Any, Union
import uuid
import redis


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
