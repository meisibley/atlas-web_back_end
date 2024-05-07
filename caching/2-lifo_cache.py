#!/usr/bin/env python3
""" Create a class LIFOCache that inherits from BaseCaching and is a
caching system:
def put(self, key, item):
def get(self, key):
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ must use self.cache_data - dictionary from parent class BaseCaching
    """
    def __init__(self):
        """can overload def __init__(self): but don’t forget to call the
        parent init: super().__init__()
        """
        super().__init__()

    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data the item value for
        the key key.
        If key or item is None, this method should not do anything.
        If number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS:
        you must discard the last item put in cache (LIFO algorithm)
        you must print DISCARD: with the key discarded and following by
        a new line
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

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
        return self.cache_data[key]
