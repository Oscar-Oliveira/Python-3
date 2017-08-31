"""
Exercise 16
"""

import random

def generate_random_list1(qty, start, end):
    result = []
    for i in range(qty):
        result.append(random.randrange(start, end))
    return result

def generate_random_list2(qty, start, end):
    return [random.randrange(start, end) for x in range(qty)]

print(generate_random_list1(10, 10, 100))

print(generate_random_list2(10, 10, 100))
