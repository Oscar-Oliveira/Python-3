"""
Exercise 6
"""

students = []
while True:
    name = input("Student name [empty to quit]: ")
    if not name:
        break
    students.append(name)

students.sort()
for student in students:
    print(student)
