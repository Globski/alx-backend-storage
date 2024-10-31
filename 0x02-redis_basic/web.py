#!/usr/bin/env python3
import redis
import requests
import time
from functools import wraps

cache = redis.Redis(host='localhost', port=6379, db=0)

def cache_page(expiration=10):
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
    count_key = f"count:{url}"
    cache.incr(count_key)
    
    response = requests.get(url)
    return response.text
