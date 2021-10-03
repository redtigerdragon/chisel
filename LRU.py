# -*- coding: utf-8 -*-
"""
This is an implementation of a LeastRecentlyUsed cache.
@author: Daniel Overton <redtigerdragon@gmail.com>
"""


from collections import OrderedDict

class LeastRecentlyUsed:
    """
    This class implements a Least-Recently Used Cache.
    
    We use an OrderedDict for our cache, as, according to python documentation,
    "An OrderedDict would also be useful for implementing variants of 
    functools.lru_cache()". The cache is strutured such that in the beginning
    of the list is the least recently used and in the end the most recently 
    used. As per the instructions, "Both reading and writing a value of a key 
    are considered use of that key"; thus when a value is read, it is placed 
    at the end, and any write is automatically placed at the end of the cache.
    """
    
    def __init__(self, size: int):
        """
        This method creates a new LRU.
    
            :param name: szie
            :type name: int
        """
        self.size = size
        self.cache = OrderedDict()
        
    def put(self, key, value):
        """
        First, we check if the key is already in the cache. If it isn't, 
        and if the cahce has exceeded our length, then we pop the first item 
        in the list (which will be the least recently used). Finally, no 
        matter what, we add the key, value pair and move them to the end of 
        the list to show they have been used.
    
        :returns: none
        """
        if not key in self.cache.keys():            
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False)
        self.cache[key] = value
        self.cache.move_to_end(key)
            
    
    def get(self, key):
        """
        Return the value of the key, raising an error of we do not find the 
        key. If the key is returned, we move it to the end of the cache to 
        show it was used.

        :returns: int -- the value
        """
        if key not in self.cache:
            raise KeyError("Invalid Key.")
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
     
    def delete(self, key):
        """
        First, we check if the key exists. If it does not, we do nothing 
        (no op). If it does exist, we pop the key, value pair from the cache.
    
        :returns: none
        """
        if key not in self.cache:
            return
        else:
            self.cache.pop(key)
            
    def reset(self):
        """
        Clear all key, value pairs from the cache.
    
        :returns: none
        """
        self.cache.clear()