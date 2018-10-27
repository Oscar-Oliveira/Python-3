"""
enumerate
"""

name = "Student1"
print(enumerate(name))
print(list(enumerate(name)))

items = ["Student1", "Student2", "Student3", "Student4"]

print()
for counter, value in enumerate(items):
    print(counter, value)

print()
for counter, value in enumerate(items, start=1):
    print(counter, value)

print()
enumeratedItem = list(enumerate(items, 1))
print(enumeratedItem)
print(enumeratedItem[1][1])
