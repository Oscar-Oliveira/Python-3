"""
Generator expressions
"""

items = (x*3 for x in range(1, 100) if x % 2 == 0)
for i in items:
    print(i, end=" ")

# Needs to generato new one because previous already finished. 
# Python's iterator protocol only provides the next() method.
# and no method to reset an iterator.

print("\n")
items = (x*3 for x in range(1, 100) if x % 2 == 0)
items = list(items) # force list generation consume large quantity of memory
print(items)

print()
sumValues = sum(x*3 for x in range(1, 100) if x % 2 == 0) 
print(sumValues)
