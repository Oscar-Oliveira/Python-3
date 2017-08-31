"""
Module example
"""

__version__ = 1.0 # builin attribute
__sprint__ = 7 # user attributes
some_value = 10

def my_sum(value1, value2):
    return value1 + value2

def daddy():
    return "Running from: " + __name__

if __name__ == "__main__":
    print(daddy())
    print(my_sum(some_value, some_value))
