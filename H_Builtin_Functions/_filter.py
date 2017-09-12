"""
filter
"""

def is_even(number): 
    return number % 2 == 0

values = list(filter(lambda x: x >= 2, [1, 2, 3, 4]))
print("".join(str(x) for x in values))

values = list(range(10))
print("".join(str(x) for x in values))

values = filter(lambda x: x % 3 == 0, list(range(10)))
print("".join(str(x) for x in values))
