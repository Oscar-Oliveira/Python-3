"""
map
"""

def multiply(value, times=1):
    return value * times

a = list(map(multiply, [1, 2, 3]))
print(a)

print()
a = list(map(multiply, [1, 2, 3], [1, 2, 3]))
print(a)
