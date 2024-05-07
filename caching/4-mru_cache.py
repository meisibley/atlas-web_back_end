#!/usr/bin/env python3
""" Create a class MRUCache that inherits from BaseCaching and is
a caching system:
def put(self, key, item):
def get(self, key):
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ You must use self.cache_data - dictionary from the parent
    class BaseCaching
    """
    def __init__(self):
        """ You can overload def __init__(self): but don’t forget to call
        the parent init: super().__init__()
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data the item value
        for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS:
        you must discard the most recently used item (MRU algorithm)
        you must print DISCARD: with the key discarded and following
        by a new line
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        self.cache_data.move_to_end(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = list(self.cache_data.keys())[BaseCaching.MAX_ITEMS - 1]
            del self.cache_data[discard]
            print('DISCARD: {}'.format(discard))

    def get(self, key):
        """ Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
