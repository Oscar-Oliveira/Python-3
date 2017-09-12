"""
Dictionary
"""

grades = {
    "student1" : [10, 11, 12],
    "student2" : [15, 14, 14],
    "student3" : [10, 10, 12],
    "student4" : [14, 14, 10]
}

grades["student5"] = [10, 10, 10]
print(grades) # The order is defined by python.

del grades["student3"]
print(grades)

print()
print(grades.values())

print()
print("Number of students:", len(grades))

print()
if "student1" in grades:
    grades["student1"][0] = 13
    print(grades["student1"])
    grades["student1"].append(15)
    print(grades["student1"])

print()
# alias
backup_grades = grades # alias
backup_grades["student1"][0] = 1
print(backup_grades)
print(grades)

print()
# after copy() the LISTs (complex object) of grades 
# will refer to the same objects, so remain equals in both
backup_grades2 = grades.copy()
backup_grades2["student5"][0] = 3
print(backup_grades2)
print(grades)

print()
for name, student_grades in grades.items():
    print("Name: {} | Grades: {}".format(name, student_grades))

for name, student_grades in sorted(grades.items()):
    print("Name: {} | Grades: {}".format(name, student_grades))

print()
print(",".join(str(x) for x in grades.items()))
for name, student_grades in sorted(grades.items()):
    print(name + "," + ",".join(str(x) for x in student_grades))

print()
for value in grades.values(): 
    print(value)
for keys in grades.keys(): 
    print(keys)

print()
positive = {name: grade for name, grade 
            in grades.items()
            if 10 in grade}
for name, student_grades in positive.items():
    print("Name: {} | Grades: {}".format(name, student_grades))

print()
print(list(grades.keys()))
print(list(grades.values()))
