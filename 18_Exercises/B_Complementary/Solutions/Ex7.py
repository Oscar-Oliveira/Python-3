"""
Exercise 7
"""

numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

for i in numbers:
    print(i)
    
print()
for i in numbers:
    print(i * i, i ** 2)

print()
temp = 0
for i in numbers:
    temp += i
print("  + ".join(str(x) for x in numbers), " = ", temp)
print(sum(numbers))

print()
temp = 1
for i in numbers:
    temp *= i
print(" * ".join(str(x) for x in numbers), " = ", temp)