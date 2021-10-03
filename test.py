# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 22:27:44 2021

@author: Daniel Overton <redtigerdragon@gmail.com>
"""
from LRU import LeastRecentlyUsed

# Create an LRU Cache with a size of 3
cache = LeastRecentlyUsed(3)
 
 
cache.put("1","1")
print(cache.cache) # shows ('1', '1')
cache.put("2","2")
print(cache.cache) # shows ('1', '1'), ('2', '2')
cache.put("3","3")
print(cache.cache) # shows ('1', '1'), ('2', '2'), ('3', '3')
 
cache.get("1")
print(cache.cache) # shows ('2', '2'), ('3', '3'), ('1', '1')
cache.get("3")
print(cache.cache) # shows ('2', '2'), ('1', '1'), ('3', '3')
 
cache.put("4","4") # This will replace ('2', '2')
print(cache.cache) # shows ('1', '1'), ('3', '3'), ('4', '4')
cache.put("5","5") # This will replace ('1', '1')
print(cache.cache) # shows ('3', '3'), ('4', '4'), ('5', '5')
