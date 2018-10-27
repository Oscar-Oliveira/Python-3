"""
dir
"""

import math

__version__ = 1.0 # attribute

def test():
    pass

print(dir()) # list thr names that the current module defines

print()
print(dir(math)) # list names from math module

print()
var = "teste"
print(dir(var))

print()
var = 5
print(dir(var))
