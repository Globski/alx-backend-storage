#!/usr/bin/env python3
"""
Web caching module using Redis.
"""
import redis
import requests
from functools import wraps
from typing import Callable

redis_store = redis.Redis()

def data_cacher(method: Callable) -> Callable:
    """Decorator to cache output of fetched data and count requests.
    
    Args:
        method (Callable): The function to cache.
    
    Returns:
        Callable: The wrapped function.
    """
    @wraps(method)
    def invoker(url: str) -> str:
        """Wrap the function to count requests and cache the result.

        Args:
            url (str): The URL to fetch.

        Returns:
            str: The HTML content of the page.
        """
        redis_store.incr(f'count:{url}')
        
        cached_result = redis_store.get(f'result:{url}')
        if cached_result:
            return cached_result.decode('utf-8')
        
        result = method(url)
        
        redis_store.setex(f'result:{url}', 10, result)
        
        return result

@data_cacher
def get_page(url: str) -> str:
    """Fetch and return the HTML content of a URL.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the page.
    """
    response = requests.get(url)
    return response.text
