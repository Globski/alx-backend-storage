#!/usr/bin/env python3
"""
web.py

This module implements a simple web caching mechanism using Redis.
It fetches HTML content from a given URL and caches the result for 10 seconds.
It also tracks how many times a particular URL was accessed.
"""

import redis
import requests
from functools import wraps

cache = redis.Redis()

def cache_page(expiration=10):
    """
    A decorator to cache the results of a function call with a specified expiration time.

    Args:
        expiration (int): Time in seconds for the cache to expire.

    Returns:
        function: The decorated function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(url):
            cached_result = cache.get(url)
            if cached_result:
                return cached_result.decode('utf-8')
            
            result = func(url)
            cache.setex(url, expiration, result)
            return result
        return wrapper
    return decorator

@cache_page(expiration=10)
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a given URL, caching the result.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the URL.
    """
    count_key = f"count:{url}"
    
    cache.incr(count_key)
    response = requests.get(url)
    return response.text
