#!/usr/bin/env python3
""" Module contaning simple redis cache
"""

import requests
import redis



cache = redis.Redis()


def url_access_count(method):
    """ Decorator for get_page
    """
    @wraps(method)
    def for_each_call(url):
        """ Wrapper function
        """
        key = "cached:" + url
        cached_value = cache.get(key)
        if cached_value:
            return cached_value.decode("utf-8")

        # Update cache with new content
        key_count = "count:" + url
        html_content = method(url)

        cache.incr(key_count)
        cache.set(key, html_content, ex=10)
        cache.expire(key, 10)
        return html_content
    return for_each_call


@url_access_count
def get_page(url: str) -> str:
    """ Get the content of a page
    """
    results = requests.get(url)
    return results.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
