"""
any(iterable) | all(iterable)
- Iterables: str, list, dict, range, tuple, set, bytes
"""

value = all([True, True, True])
print(value)
value = all([True, False, False])
print(value)

value = any([True, False, False])
print(value)
value = any([False, False, False])
print(value)

print()
value = any([0, 0])
print(value)
value = any("")
print(value)
value = any("X")
print(value)

def is_div_by_3(val):
    return val % 3 == 0

print(is_div_by_3(9))
print(is_div_by_3(19))

print()
value = any(is_div_by_3(x) for x in range(1000, 1051))
print(value)

value = all(name == name.title() for name \
                in ["Student1", "Student2", "student3"])
print(value)
