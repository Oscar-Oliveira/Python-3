"""
Exercise 14
"""

def swap1(x, y):
    (x, y) = (y, x)

def swap2():
    global list1
    global list2
    (list1, list2) = (list2, list1)


list1 = ["one", "two", "three"]
list2 = [1, 2, 3]

print(list1, list2)

swap1(list1, list2)
print(list1, list2)

swap2()
print(list1, list2)
