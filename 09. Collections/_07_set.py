"""
Sets
- A set is an unordered collection with no duplicate elements.
- Allow operations based on set theory.
"""

set1 = {'a', 'b', 'c', 'a', 'd', 'e', 'f'}
print(set1)
set2 = set("aaaabcd")
print(set2)

print()
print(set1 & set2)
print(set1.intersection(set2))

print()
print(set1 | set2)
print(set1.union(set2))

print()
print(set1 - set2)
print(set1.difference(set2))

print(set1.symmetric_difference( set("xzabc") )) # not in both

print()
print(set1.issuperset(set2))
print(set2.issubset(set1))
print(set2.isdisjoint(set("xz")))

print(set2.issuperset({'a', 'b'}))
print(set2.issuperset({'a', 'b'}))

print()
for item in set1 - set2:
    set2.add(item)
print(set2)

print()
set2.remove('a')
print(set2)

print()
print(",".join(str(x) for x in set2))

print()
print('b' in set2)

print()
# Set comprehension
words = ("stu", "stud", "student", "dent")
w = {x for x in words if len(x) == 4}
print(w)

print()
set2.clear()
print(set2)
