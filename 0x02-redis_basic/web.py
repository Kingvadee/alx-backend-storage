#!/usr/bin/env python3
"""this is module for redis"""
import requests
import redis
from functools import wraps

cache_store = redis.Redis()


def track_url_access(method):
    """track url access method for redis"""

    @wraps(method)
    def decorated_function(url):
        cached_key = f"cached:{url}"
        cached_data = cache_store.get(cached_key)

        if cached_data:
            return cached_data.decode("utf-8")

        count_key = f"count:{url}"
        html = method(url)

        cache_store.incr(count_key)
        cache_store.set(cached_key, html)
        cache_store.expire(cached_key, 10)

        return html

    return decorated_function


@track_url_access
def get_page(url: str) -> str:
    """get page method for redis"""
    response = requests.get(url)
    return response.text
