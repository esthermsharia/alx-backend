#!usr/bin/env python3
"""
Defines the caching module
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Defines two methods that add and access an item
       from a dictinary.
    """

    def put(self, key, item):
        """Adds an item to the dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """accesses a dictinary item using a key and
           returns it if it exists
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
