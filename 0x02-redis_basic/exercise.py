#!/usr/bin/env python3
"""
Module for Redis caching.
"""
import redis
import uuid
from typing import Union, Callable, Optional

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

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieve data from Redis and convert using fn if provided.

        Args:
            key (str): The key for the stored data.
            fn: Optional callable to convert the retrieved data.

        Returns:
            The data in its original format, or None if the key doesn't exist.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Get a string value from Redis."""
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Get an integer value from Redis."""
        return self.get(key, int)