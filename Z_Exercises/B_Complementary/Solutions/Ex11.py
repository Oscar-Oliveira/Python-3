"""
Exercise 11
"""

def compare1(arg1, arg2):
    if arg1 < arg2:
        return -1
    if arg1 > arg2:
        return 1
    return 0

def compare2(arg1, arg2):
    return 0 if arg1 == arg2 else (-1 if arg1 < arg2 else 1)

def compare3(arg1, arg2):
    return (arg1 > arg2) - (arg1 < arg2)

print(compare1(10, 11))
print(compare1(10, -11))
print(compare1(10, 10))

print(compare2(10, 11))
print(compare2(10, -11))
print(compare2(10, 10))

print(compare3(10, 11))
print(compare3(10, -11))
print(compare3(10, 10))
