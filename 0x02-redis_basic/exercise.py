#!/usr/bin/env python3
"""
Module for Redis caching.
"""
import redis
import uuid
from typing import Union

class Cache:
    """
    Cache class to manage Redis operations.
    """

    def __init__(self):
        """
        Initialize the Cache instance.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis and return the generated key.
        
        Args:
            data (Union[str, bytes, int, float]): The data to store.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        
        self._redis.set(key, data)
        
        return key
