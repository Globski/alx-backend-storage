#!/usr/bin/env python3
"""
Web caching module using Redis.
"""
import requests
from redis import Redis

def get_page(url: str) -> str:
    """
    Get the HTML content of a URL with caching.
    
    Args:
        url (str): The URL to fetch.

    Returns:
        str: The HTML content of the page.
    """
    redis_client = Redis()
    
    if redis_client.exists(url):
        return redis_client.get(url).decode('utf-8')
    
    response = requests.get(url)
    redis_client.setex(url, 10, response.text)
    
    return response.text
