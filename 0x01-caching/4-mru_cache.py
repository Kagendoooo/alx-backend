#!/usr/bin/env python3
"""
MRU caching
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """Caching system using MRU algorithm"""
    def __init__(self):
        """Class initialization"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add item to cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            most_key, _ = self.cache_data.popitem(True)
            print("DISCARD:", most_key)

    def get(self, key):
        """Retrieve an item"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
