"""
Aritmetic
"""

a = 2 + 2
print("a = 2 + 2 = {}".format(a))
a = a - 2
print("a - 2 = {}".format(a))
a = a * 2
print("a = a * 2 = {}".format(a))
a = a / 2
print("a = a / 2 {}".format(a))

print()
a = a ** 2 # Power
print("a = a ** 2 = {}".format(a))

print()
# // Divide and round DOWN to the nearest whole number
b = a // 3 
print("b = a // 3 {}".format(b))
b = -a // 3
print("b = -a // 3 = {}".format(b))

print()
b = (a * 3) // 2.5 # Modulo
print("b = (a * 3) // 2.5 = {}".format(b))
c = (a * 3) % 2.5 # Modulo
print("c = (a * 3) % 2.5 = {}".format(b))
c = (b * 2.5) + c 
print("c = (b * 2.5) + c = {}".format(c))

print()
a += 2 # variable = variable operator value, a = a + 2
print("a += 2 (a={})".format(a))
a -= 2 #  a = a - 2
print("a += 2 (a={})".format(a))
a *= 2
print("a *= 2 (a={})".format(a))
a /= 2
print("a /= 2 (a={})".format(a))
a **= 2
print("a **= 2 (a={})".format(a))
a //= 2
print("a //= 2 (a={})".format(a))
a %= 2
print("a %= 2 (a={})".format(a))
