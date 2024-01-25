#!/usr/bin/env python3
"""web caching module"""
import requests
import redis
from functools import wraps
from typing import Callable


rd = redis.Redis()


def count_access(method: Callable) -> Callable:
    """count access decorator"""
    @wraps(method)
    def wrapper(url):
        """wrapper function for decorator"""
        rd.incr(f"count:{url}")
        cached_html = rd.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode("utf-8")
        html = method(url)
        rd.setex(f"cached:{url}", 10, html)
        return html
    return wrapper


@count_access
def get_page(url: str) -> str:
    """function that returns the HTML content of a URL"""
    return requests.get(url).text
