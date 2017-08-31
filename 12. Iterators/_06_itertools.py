"""
itertools
See: https://docs.python.org/3.6/library/itertools.html
"""

from itertools import islice, count, chain

v = islice((x for x in count() if x % 3 == 0), 100) 
for i in v: 
    print(i, end=" ")

print("\n")
# force list generation
x = list(islice((x for x in count() if x % 3 == 0), 100))
print(x)

print()
students = ["Student1", "Student2", "Student3", "Student4", "Student5"] 
grades1 = [12, 14, 15, 15]
grades2 = [13, 14, 14, 14, 10]
v = chain(students, grades1, grades2)
for item in v:
    print(item, end=" ")

print("\n")
print(all(x>=10 for x in chain(grades1, grades2)))
