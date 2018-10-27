"""
Flow
"""

import sys

def first(option):
    second(option)

def second(option):
    third(option)
    if option == 3:
        raise ZeroDivisionError("UPS")

def third(option):
    fourth(option)
    if option == 2:
        raise TypeError("TypeError")

def fourth(option):
    try:
        fifth(option)
    except AttributeError:
        print("AttributeError Caught in fourth")

def fifth(option):
    if option == 1:
        raise AttributeError

try:
    first(1) # try with 1, 2, 3
    print("Done!")
except TypeError as err:
    print(err, "Caught in main try...except block")
except:
    print(sys.exc_info()[0].__name__, "Caught on default except")

print("Finished...")
