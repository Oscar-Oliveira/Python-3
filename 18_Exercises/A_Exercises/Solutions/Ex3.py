"""
Exercise 3
"""

F = float(input("Enter Fahrenheit temperature: "))

C = (5/9) * (F - 32)

print("{} degrees Fahrenheit are {} degrees Centigrades.".format(F, C))

F2 = ((9.0 / 5.0) * C) + 32.0

print("{} degrees Centigrades are {} degrees Fahrenheit.".format(C, F2))
