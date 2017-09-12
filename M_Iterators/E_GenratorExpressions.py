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
# You can grab all the elements of an iterator by calling list() on it. 
# Forced list generation can consume large quantity of memory depending on the collection size.
items = list(items)
print(items)

print()
sumValues = sum(x*3 for x in range(1, 100) if x % 2 == 0) 
print(sumValues)
