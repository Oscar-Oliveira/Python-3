"""
List
"""

import math

def my_avg(myList):
    sum = 0
    for grade in myList:
        sum += grade
    return sum / len(myList)

def list_one_by_one_v1(myList):
    for i in range(len(myList)):
        print(myList[i])

def list_one_by_one_v2(myList):
    for item in myList:
        print(item)

def append_value(myList, value):
    myList.append(value)

def change_my_list(myList):
    myList.append(10)
    myList = [1, 1, 1, 1]
    print(myList)

grades = [10, 8, 4, 17]

listCons = list("Student Grades")
print(listCons)

print("Grades:", grades)
print("Avg:", my_avg(grades))

print(10 in grades)

print()
grades.append(15)
print("Updated grades:", grades)
print("Updated avg:", my_avg(grades))

print()
append_value(grades, 12)
print("Updated grades:", grades)
change_my_list(grades)
print("Updated grades:", grades)

print()
list_one_by_one_v1(grades)
list_one_by_one_v2(grades)

print()
print("First grade:", grades[0])
del grades[0]
print("First grade:", grades[0])

print()
grades.append(12.5)
grades.sort()
print("Sorted grades:", grades)
grades.sort(reverse=True)
print("Sorted grades:", grades)
grades.reverse()
print("Sorted grades:", grades)

print()
print("Sorted grades:", sorted(grades, reverse=False))
print("Sorted grades:", grades)

grades += [18, 9, 7]
grades.extend([18, 9, 7])
print("extended:", grades)

grades2 = [18, 9, 7] * 3
print()
print(grades2)
del grades2[3:]
print(grades2)

print()
# List comprehension
pos_grades = [math.ceil(i) for i in grades if i > 9.5]
print(pos_grades)

print()
print(", ".join(str(x) for x in pos_grades))

print()
print("index of 17: ", pos_grades.index(17))

print()
pos_grades.append(17)
print(pos_grades)
pos_grades.remove(17) # remove first
print(pos_grades)

print(pos_grades.index(10)) # raises ValueError exception
pos_grades.remove(10) # raises ValueError exception
