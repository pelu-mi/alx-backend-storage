#!/usr/bin/env python3
""" Module contaning simple tasks for redis project
"""

import requests
import redis


cache = redis.Redis()


def get_page(url: str) -> str:
    """ Obtain content of html page and return it
    """
    cache.set("cached:" + key, 0)
    cache.incr("count:" + key)
    cache.setex("cached:" + key, 10, cache.get("cached:" + key))
    data = requests.get(url)
    return data.text
