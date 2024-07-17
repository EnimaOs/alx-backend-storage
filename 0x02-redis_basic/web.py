#!/usr/bin/env python3
"""tasks"""


from typing import Callable
from functools import wraps
import redis
import requests

redis_client = redis.Redis()


def url_count(method: Callable) -> Callable:
    """counts how many times an url is accessed"""

    @wraps(method)
    def wrapper(*args, **kwargs):
        url = args[0]
        redis_client.incr(f"count:{url}")
        cached = redis_client.get(url)
        if cached:
            return cached.decode("utf-8")
        result = method(*args, **kwargs)
        redis_client.setex(url, 10, result)
        return result

    return wrapper


@url_count
def get_page(url: str) -> str:
    """Makes a http request to a given endpoint"""
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    print(get_page("http://slowwly.robertomurray.co.uk"))
