#!/usr/bin/env python3
"""
Class BasicCache that inherits from BaseCaching
Caching system doesn’t have limit
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Defines a caching system with no limits"""
    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache by key
        """
        return self.cache_data.get(key)
