#!/usr/bin/env python3
"""
LIFO caching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Caching system using LIFO algorithm"""
    def __init__(self):
        """Class initialization"""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Add item to cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key in self.cache_data:
                del self.cache_data[self.last_key]
                print("DISCARD:", self.last_key)
        self.last_key = key

    def get(self, key):
        """Retrieve an item"""
        return self.cache_data.get(key, None)
