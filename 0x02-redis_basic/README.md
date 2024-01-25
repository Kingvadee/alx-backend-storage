## AUTHOR:         [DAVID OJEIFO](https://github.com/Kingvadee).
## COHORT:         13.
## Repo:           [alx-backend-storage](https://github.com/Kingvadee/alx-backend-storage)
## Dir:		   0x02-redis_basic
# Tasks :page_with_curl:

# ![Image.jpg](https://private-user-images.githubusercontent.com/125440789/299472020-7d96d81b-ed5a-473b-95b0-6f8022833875.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDYxMzQxMjgsIm5iZiI6MTcwNjEzMzgyOCwicGF0aCI6Ii8xMjU0NDA3ODkvMjk5NDcyMDIwLTdkOTZkODFiLWVkNWEtNDczYi05NWIwLTZmODAyMjgzMzg3NS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMTI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDEyNFQyMjAzNDhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04ZDY2MmQ2OTE0Y2NjNTk5NzNlMDkzNDEzYWExOWUwOTQ3NTlhMzA4YmUwNGJiY2M0OTI3YWU1NDhhZWY2NmE5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.1MUrajNRevxuGGxb-1SKzP_DZR_0H3PkI5VZa0cy9i4)

## Redis

### Installation
- Install Redis on Ubuntu 18.04:
  ```
  $ sudo apt-get -y install redis-server
  $ pip3 install redis
  $ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
  ```

### Use Redis in a container
- Redis server is stopped by default - when you are starting a container, you should start it with:
  ```
  service redis-server start
  ```

## Tasks
### 0. Writing strings to Redis (Mandatory)
- Create a Cache class.
- In the `__init__` method, store an instance of the Redis client as a private variable named `_redis` (using `redis.Redis()`) and flush the instance using `flushdb`.
- Create a `store` method that takes a `data` argument and returns a string. The method should generate a random key (e.g., using uuid), store the input data in Redis using the random key, and return the key.
- Type-annotate `store` correctly. Remember that `data` can be a str, bytes, int, or float.

### 1. Reading from Redis and recovering the original type (Mandatory)
- Create a `get` method that takes a key string argument and an optional Callable argument named `fn`. This callable will be used to convert the data back to the desired format.
- Remember to conserve the original Redis.get behavior if the key does not exist.
- Also, implement 2 new methods: `get_str` and `get_int` that will automatically parameterize `Cache.get` with the correct conversion function.

### 2. Incrementing values (Mandatory)
- Define a `count_calls` decorator that takes a single method Callable argument and returns a Callable.
- As a key, use the qualified name of the method using the `__qualname__` dunder method.
- Create and return a function that increments the count for that key every time the method is called and returns the value returned by the original method.

### 3. Storing lists (Mandatory)
- Define a `call_history` decorator to store the history of inputs and outputs for a particular function.
- Every time the original function will be called, add its input parameters to one list in Redis and store its output into another list.
- In `call_history`, use the decorated function’s qualified name and append ":inputs" and ":outputs" to create input and output list keys, respectively.

### 4. Retrieving lists (Mandatory)
- Implement a `replay` function to display the history of calls of a particular function.
- Use keys generated in previous tasks to generate the following output.

### 5. Implementing an expiring web cache and tracker (Advanced)
- Implement a `get_page` function (prototype: `def get_page(url: str) -> str:`).
- The core of the function is very simple. It uses the requests module to obtain the HTML content of a particular URL and returns it.

## Copyright © 2024 ALX, All rights reserved.
