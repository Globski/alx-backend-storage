#!/usr/bin/env python3
"""
Web caching module using Redis.
"""
import redis
import requests
import time
from functools import wraps

class WebCache:
    """Class to implement a web cache with Redis."""

    def __init__(self):
        """Initialize the Redis client."""
        self._redis = redis.Redis()
    
    def count_requests(self, fn):
        """Decorator to count how many times a URL has been requested."""
        
        @wraps(fn)
        def wrapper(url):
            """Wrap the function to count requests."""
            self._redis.incr(f"count:{url}")
            return fn(url)
        return wrapper

    @count_requests
    def get_page(self, url: str) -> str:
        """
        Fetch the HTML content of a URL and cache it for 10 seconds.
        Args:
            url (str): The URL to fetch.

        Returns:
            str: The HTML content of the page.
        """
        cached_page = self._redis.get(url)
        if cached_page:
            return cached_page.decode('utf-8')
        
        response = requests.get(url)
        content = response.text
        
        self._redis.setex(url, 10, content)
        return content
