# Alx Backend Storage - Redis Basic

## Description

This project demonstrates how to use Redis for caching and data retrieval in Python. It includes several tasks that cover storing and retrieving data: Learn how to store data in Redis and retrieve it when needed. Reading from Redis Understand how to read existing data from the Redis database. Incrementing values. Discover how to increment numeric values stored in Redis. Implementing decorators. Explore how to create decorators that track function calls and maintain a history of interactions.

## Project Structure

| Task                                    | Description                                                                                                                                                                        | Source Code                    |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| 0. Writing Strings to Redis             | Create a `Cache` class, store an instance of the Redis client, flush the instance, and implement a `store` method to store data with a random key.                               | [exercise.py](exercise.py)     |
| 1. Reading from Redis                   | Implement a `get` method to retrieve data and convert it using an optional callable. Include `get_str` and `get_int` methods for automatic conversions.                          | [exercise.py](exercise.py)     |
| 2. Incrementing Values                  | Create a `count_calls` decorator to count how many times `Cache` methods are called and decorate `Cache.store` with it.                                                          | [exercise.py](exercise.py)     |
| 3. Storing Lists                        | Define a `call_history` decorator to store input/output history for a function using Redis lists.                                                                                | [exercise.py](exercise.py)     |
| 4. Retrieving Lists                     | Implement a `replay` function to display the history of function calls, showing inputs and outputs.                                                                              | [exercise.py](exercise.py)     |
| 5. Implementing an Expiring Web Cache   | Create a `get_page` function to fetch HTML content from a URL, track access counts, and cache the result with a 10-second expiration.                                             | [web.py](web.py)               |

## Environment
- Ubuntu 18.04 LTS
- Python 3.7
- Redis
- pycodestyle style (version 2.5)


## Requirements

- All of your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All of your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- Your code should use the pycodestyle style (version 2.5)
- All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions and methods should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Learning Objectives

- Understand how to use Redis for basic operations.
- Learn to implement caching mechanisms.
- Gain experience with decorators in Python.
- Familiarize with managing data types and conversions in Redis.

## Prototype Table

| Function Name    | Prototype                                 |
|-------------------|------------------------------------------|
| `store`           | `def store(self, data: Union[str, bytes, int, float]) -> str:` |
| `get`             | `def get(self, key: str, fn: Optional[Callable] = None) -> Any:` |
| `get_str`        | `def get_str(self, key: str) -> str:` |
| `get_int`        | `def get_int(self, key: str) -> int:` |
| `count_calls`    | `def count_calls(method: Callable) -> Callable:` |
| `call_history`    | `def call_history(method: Callable) -> Callable:` |
| `replay`         | `def replay(fn: Callable) -> None:` |
| `get_page`       | `def get_page(url: str) -> str:` |


## How to Use

1. Clone the repository.
2. Ensure Redis is installed and running.
3. Execute the `main.py` script to see examples of the Cache class in action:

```bash
python3 main.py
```

## Installation

To install Redis on Ubuntu, run the following commands:

```bash
sudo apt-get -y install redis-server
pip3 install redis
```

Make sure to configure Redis to bind to localhost:

```bash
sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
```

Before running your Python scripts, ensure the Redis server is started:

```bash
sudo service redis-server start
```

- Make sure to run each functionality with various input values to verify that the Redis operations work as expected.

## Additional Notes
- Basic Operations: Understand how to perform fundamental tasks with Redis.
- Caching Mechanisms: Learn how to implement caching for improved performance.
- Python Decorators: Gain experience in using decorators to enhance functionality.
- Data Management: Familiarize yourself with handling data types and conversions in Redis.

## Tasks

### 0. Writing Strings to Redis
- Create a Cache class. In the `__init__` method, store an instance of the Redis client as a private variable named `_redis` (using `redis.Redis()`) and flush the instance using `flushdb`.
- Create a `store` method that takes a `data` argument and returns a string. The method should generate a random key (e.g., using `uuid`), store the input data in Redis using the random key, and return the key.
- Type-annotate `store` correctly. Remember that `data` can be a `str`, `bytes`, `int`, or `float`.

- **Class**: `Cache`
- **Methods**:
  - `__init__`: Initializes Redis client and flushes the database.
  - `store(data)`: Stores data in Redis with a random UUID key and returns the key.

**Example**:
```python
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

bob@dylan:~$ python3 main.py 
3a3e8231-b2f6-450d-8b0e-0f38f16e8ca2
b'hello'
bob@dylan:~$ 
```

### 1. Reading from Redis and Recovering Original Type
- In this exercise, we will create a `get` method that takes a `key` string argument and an optional `Callable` argument named `fn`. This callable will be used to convert the data back to the desired format.
- Remember to conserve the original `Redis.get` behavior if the key does not exist.
- Also, implement 2 new methods: `get_str` and `get_int` that will automatically parametrize `Cache.get` with the correct conversion function.
- **Methods**:
  - `get(key, fn=None)`: Retrieves the value for a key and converts it using an optional callable `fn`.
  - `get_str(key)`: Returns the value as a string.
  - `get_int(key)`: Returns the value as an integer.

**Example**:
```python
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
```

### 2. Incrementing Values
- Familiarize yourself with the `INCR` command and its Python equivalent.
- In this task, we will implement a system to count how many times methods of the `Cache` class are called.
- Above `Cache`, define a `count_calls` decorator that takes a single method `Callable` argument and returns a `Callable`.
- Create and return a function that increments the count for that key every time the method is called and returns the value returned by the original method.
- Remember that the first argument of the wrapped function will be `self`, which lets you access the Redis instance.
- Decorate `Cache.store` with `count_calls`.

- **Decorator**: `count_calls`
- **Methods**:
  - `store(data)`: Decorated with `count_calls` to track how many times it has been called.

**Example**:
```python
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))

bob@dylan:~$ ./main.py
b'1'
b'3'
bob@dylan:~$ 
```

### 3. Storing Lists
- Familiarize yourself with Redis commands `RPUSH`, `LPUSH`, `LRANGE`, etc.
- In this task, we will define a `call_history` decorator to store the history of inputs and outputs for a particular function.
- Every time the original function is called, we will add its input parameters to one list in Redis and store its output into another list.
- Use `rpush` to append the input arguments, normalizing with `str(args)`.

- **Decorator**: `call_history`
- **Methods**:
  - `store(data)`: Decorated to store input and output history in Redis lists.

**Example**:
```python
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("secont")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))

bob@dylan:~$ ./main.py
04f8dcaa-d354-4221-87f3-4923393a25ad
a160a8a8-06dc-4934-8e95-df0cb839644b
15a8fd87-1f55-4059-86aa-9d1a0d4f2aea
inputs: [b"('first',)", b"('secont',)", b"('third',)"]
outputs: [b'04f8dcaa-d354-4221-87f3-4923393a25ad', b'a160a8a8-06dc-4934-8e95-df0cb839644b', b'15a8fd87-1f55-4059-86aa-9d1a0d4f2aea']
bob@dylan:~$ 
```

### 4. Retrieving Lists
- In this task, we will implement a `replay` function to display the history of calls of a particular function.
- Use keys generated in previous tasks to generate the following output:

- **Function**: `replay(method)`
- **Functionality**: Displays the call history of a function, showing input and output values.

  ```
  >>> cache = Cache()
  >>> cache.store("foo")
  >>> cache.store("bar")
  >>> cache.store(42)
  >>> replay(cache.store)
  Cache.store was called 3 times:
  Cache.store(*('foo',)) -> 13bf32a9-a249-4664-95fc-b1062db2038f
  Cache.store(*('bar',)) -> dcddd00c-4219-4dd7-8877-66afbe8e7df8
  Cache.store(*(42,)) -> 5e752f2b-ecd8-4925-a3ce-e2efdee08d20
  ```

**Tip:** use `lrange` and `zip` to loop over inputs and outputs.

### 5. Implementing an Expiring Web Cache and Tracker (Advanced)
- In this task, we will implement a `get_page` function (prototype: `def get_page(url: str) -> str:`). The core of the function is very simple. It uses the `requests` module to obtain the HTML content of a particular URL and returns it.
- Inside `get_page`, track how many times a particular URL was accessed in the key `count:{url}` and cache the result with an expiration time of 10 seconds.
- Bonus: Implement this use case with decorators.
- **Function**: `get_page(url: str) -> str`
- **Functionality**: Fetches the HTML content of a URL, tracks access counts, and caches results with a 10-second expiration.
