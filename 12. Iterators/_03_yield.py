"""
yield
"""

def generator1():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

def generator2():
    for i in range(1, 6):
        yield i

g = generator1()
print(next(g), end=" ")
print(next(g), end=" ")
print(next(g), end=" ")

print()
g = generator1()
for _ in range(5):
    print(next(g), end=" ")

print()
for value in generator1():
    print(value, end=" ")

print()
for value in generator2():
    print(value, end=" ")
