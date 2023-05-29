#!/usr/bin/env python3
""" Module contaning simple redis cache
"""

import requests
import redis
cache = redis.Redis()


def get_page(url: str) -> str:
    """ Obtain content of html page and return it
    """
    cache.set("cached:" + url, 0)
    cache.incr("count:" + url)
    cache.setex("cached:" + url, 10, cache.get("cached:" + url))
    data = requests.get(url)
    return data.text
