"""
filter
"""

def is_even(number): 
    return number % 2 == 0

values = list(range(10))
print("".join(str(x) for x in values))

values = filter(is_even, values)
print("".join(str(x) for x in values))

values = filter(lambda x: x % 3 == 0, list(range(10)))
print("".join(str(x) for x in values))
