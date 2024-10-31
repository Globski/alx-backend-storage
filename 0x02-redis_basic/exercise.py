#!/usr/bin/env python3
"""
Module for Redis caching.
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

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

def count_calls(method: Callable) -> Callable:
    """
    Decorator to count the number of times a method is called.
    
    Args:
        method (Callable): The method to decorate.

    Returns:
        Callable: The decorated method with call counting.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        return super().store(data)
Cache.store = count_calls(Cache.store)

def call_history(method: Callable) -> Callable:
    """
    Decorator to record input/output history for a method.

    Args:
        method (Callable): The method to decorate.

    Returns:
        Callable: The decorated method with history tracking.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(f"{method.__qualname__}:inputs", str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(f"{method.__qualname__}:outputs", output)
        return output
    return wrapper

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        return super().store(data)
Cache.store = call_history(Cache.store)

class Cache:

    def replay(self, fn: Callable) -> None:
        """
        Display the history of calls for a method.

        Args:
            fn (Callable): The method to replay.
        """
        inputs = self._redis.lrange(f"{fn.__qualname__}:inputs", 0, -1)
        outputs = self._redis.lrange(f"{fn.__qualname__}:outputs", 0, -1) 
        count = len(inputs)

        print(f"{fn.__qualname__} was called {count} times:")
        for inp, outp in zip(inputs, outputs):
            print(f"{fn.__qualname__}(*{inp.decode('utf-8')}) -> {outp.decode('utf-8')}")
