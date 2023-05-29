#!/usr/bin/env python3
""" Module contaning simple tasks for redis project
"""

import requests
import redis


def get_page(url: str) -> str:
    """ Obtain content of html page and return it
    """
    key = "count:" + url
    cache = redis.Redis()
    cache.incr(key)
    data = requests.get(url)
    return data.text
