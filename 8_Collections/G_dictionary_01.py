"""
Dictionary
- key:value pair.
- keys are uniques and must be immutables.
"""

#Add
students = {}
students["john"] = "student1@email.com"
students.setdefault("john", "1@1.com") # "setdefault()" inserts into a dictionary only if the given key isn't present
students.setdefault("jack", "student2@email.com") 
students.update({"jane":"jastudent3ne@email.com"})
print(students)

print("Number of students:", len(students))

print()
if "john" in students:
    print("John exit!!")
if "cliff" in students:
    print("cliff exit!!")

print()
# alias
backup_student = students
students["john"] = "john@python.org"
print(students)
print(backup_student)

print()
# copy() perform a shallow copy
backup_student = students.copy()
backup_student["john"] = "otherJohn@python.org"
print(students)
print(backup_student)

print()
for name, email in students.items():
    print("Name: {} | email: {}".format(name, email))

print()
for name, email in sorted(students.items()):
    print("Name: {} | email: {}".format(name, email))

print()
print(students.get("john")) # john@python.org
print(students.get("ford")) # None
print(students.get("john", -1)) # john@python.org
print(students.get("ford", -1)) # -1



