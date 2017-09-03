"""
fractions
- Provide support for rational number arithmetic (https://en.wikipedia.org/wiki/Rational_number)
"""

import math
from fractions import Fraction

value = Fraction(32, -10)
print(value, value.numerator, value.denominator)

value = Fraction(100)
print(value, value.numerator, value.denominator)

# from strings
value = Fraction('10/5')
print(value, value.numerator, value.denominator)
value = Fraction('-10/5')
print(value, value.numerator, value.denominator)

print()
for numerator, denominator in [(1, 2), (2, 4), (3, 6)]:
    value = Fraction(numerator, denominator)
    print("{}/{} = {}".format(numerator, denominator, value))

print()
for item in [0.5, 1.5, 2.0]:
    value = Fraction(item)
    print("{} = {}".format(item, value))

# arithmetic
print()
value1, value2 = Fraction(1, 2), Fraction(2, 4)
print("{} + {} = {}".format(value1, value2, value1 + value2))
print("{} - {} = {}".format(value1, value2, value1 - value2))
print("{} * {} = {}".format(value1, value2, value1 + value2))
print("{} / {} = {}".format(value1, value2, value1 / value2))

# Limit denominator
print()
print("pi:", math.pi)
print("pi:", Fraction(math.pi))
for i in range(1, 100):
    value = Fraction(math.pi).limit_denominator(i)
    print("{} = {} - {}".format(i, value, float(value)))
