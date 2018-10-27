"""
Tuple
"""

import E_tuple_01 as t

def get_report(values):
    report = [] # empty list
    report.append(("sum", t.my_sum(values)))
    report.append(("len", t.my_len(values)))
    report.append(("Avg", t.my_sum(values) / t.my_len(values)))
    return report

first_year_grades = (15, 18, 12, 10)
second_year_grades = (13, 13, 12, 11)

grades = first_year_grades, second_year_grades

del first_year_grades
del second_year_grades

studentReport = get_report(grades)
print(studentReport)

for item in studentReport:
    # Unpack same as desc, value = item[0], item[1]
    desc, value = item
    print(desc, ":", value)

# Unpacking
x, y = (5, 6)
print(x, y)
x, y = 5, 6
print(x, y)

x, y = y, x # Swap
print(x, y)

# * represents: rest of
values = list(range(10))
print(values)
(one, two, *three) = values
print("one:", one)
print("two:", two)
print("three:", three)

(one, *two, three) = values
print("one:", one)
print("two:", two)
print("three:", three)

(*one, two, three) = values
print("one:", one)
print("two:", two)
print("three:", three)

def print_data(a, b, c):
    print("a:", a)
    print("b:", b)
    print("c:", c)

a = (1, 2, 3)
print_data(*a)
print("{} {} {}".format(*a))
