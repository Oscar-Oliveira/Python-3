"""
Generators
- lazyness, does not create previously the series of data,
  it provides the elements when necessary
"""

import random

def pop(count, iterable):
    """pop n elements from iterable"""
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

def distinct(iterable):
    yielded = set()
    for item in iterable:
        if item not in yielded:
            yielded.add(item)
            yield item

def incremenetal_random_number():
    yielded = 1
    while True: # due to lazyness can model infinite series of data
        yielded += random.randint(0, yielded)
        yield yielded

def main():

    items = list("AAAAABBBBCCCDDE" * 3)
    print(items)

    print()
    for item in pop(4, items):
        print(item, end=" ")

    print()
    for item in distinct(items):
        print(item, end=" ")

    print()
    for item in pop(4, distinct(items)):
        print(item, end=" ")

    print()
    a = incremenetal_random_number()
    for i in range(3):
        print(next(a), end=" ") # could do this infinitely

if __name__ == "__main__":
    main()
