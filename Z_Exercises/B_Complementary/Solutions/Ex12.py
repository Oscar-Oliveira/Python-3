"""
Exercise 12
"""

def number_digits(value):
    if value < 0:
        raise ValueError
    count = 1 if value == 0 else 0
    while value:
        count += 1
        value //= 10
    return count

print(number_digits(0))
print(number_digits(1))
print(number_digits(11))
print(number_digits(-1011))

print(len(str(0)))
