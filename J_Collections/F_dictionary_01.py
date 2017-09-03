"""
Dictionary
- key:value pair.
- keys are uniques and must be immutables.
"""

student = {}
student["john"] = "student1@email.com"
student["jack"] = "student2@email.com"

print("Number of students:", len(student))

print()
if "john" in student:
    print("John exit!!")
if "cliff" in student:
    print("cliff exit!!")

print()
# alias
backup_student = student
student["john"] = "john@python.org"
print(student)
print(backup_student)

print()
# copy() perform a shallow copy
backup_student = student.copy()
backup_student["john"] = "otherJohn@python.org"
print(student)
print(backup_student)

print()
for name, email in student.items():
    print("Name: {} | email: {}".format(name, email))

print()
for name, email in sorted(student.items()):
    print("Name: {} | email: {}".format(name, email))
