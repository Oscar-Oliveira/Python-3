"""
decimal
- See: https://docs.python.org/3.6/library/decimal.html
"""

from decimal import Decimal, getcontext

a = 0.1
b = 0.2
print(a, b, a + b)
areEqual = (a + b) == 0.3
print(areEqual)

a = Decimal('0.1')
b = Decimal('0.2')
print(a, b, a + b)
areEqual = (a + b) == Decimal('0.3')
print(areEqual)

print()
value = Decimal('3.14')
print(value)
value = Decimal(3.14)
print(value)

print()
# arithmetic, differences between arithmetic on Decimal and on integers and floats.
a = -7
b = 4
print("{} / {} - {}".format(a, b, a / b))
print("{} // {} - {}".format(a, b, a // b))
print("{} % {} - {}".format(a, b, a % b))

a = Decimal(str(a))
b = Decimal(str(b))
print("{} / {} - {}".format(a, b, a / b))
print("{} // {} - {}".format(a, b, a // b))
print("{} % {} - {}".format(a, b, a % b))

# Precision
print()
a = Decimal('1.1')
b = Decimal('1.36')
print(getcontext().prec, "-", a / b)
getcontext().prec = 3
print(getcontext().prec, "-", a / b)
getcontext().prec = 10
print(getcontext().prec, "-", a / b)
getcontext().prec = 42
print(getcontext().prec, "-", a / b)
