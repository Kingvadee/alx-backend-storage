#!/usr/bin/env python3
""" implement the get_page function """
import requests
import redis
from functools import wraps
from typing import Callable
cache = redis.Redis()


def counter(method: Callable) -> Callable:
    """ set an expiration on a key """

    @wraps(method)
    def wrapper(*args, **kwargs) -> Callable:
        """ function wrapper """
        count_key = f"count:{args}"
        result_key = f"{args}"

        cache.incr(count_key)
        result = cache.get(result_key)
        if result:
            return result.decode('utf8')
        result = method(*args)
        cache.set(count_key, 0)
        cache.setex(result_key, 10, str(result))
        return result
    return wrapper


@counter
def get_page(url: str) -> str:
    """ get a url respobse """

    return requests.get(url).text
