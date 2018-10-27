"""
dis
See: https://docs.python.org/3/library/dis.html
"""

import dis

def swap1():
    a = 5
    b = 4
    a, b = b, a

def swap2():
    a = 5
    b = 4
    c = a
    a = b
    b = c

print("swap1():")
dis.dis(swap1)

print("swap2():")
dis.dis(swap2)
