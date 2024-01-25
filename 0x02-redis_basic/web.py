#!/usr/bin/env python3
'''Reading from Redis and recovering original type'''


import redis


class Cache:
    '''Cache class'''
    def __init__(self):
        '''Constructor'''
        self._redis = redis.Redis()
        self._redis.flushdb()
        print(self._redis.ping())

    def store(self, data):
        '''Store data in Redis'''
        for key in data:
            self._redis.set(key, data[key])
        return None
