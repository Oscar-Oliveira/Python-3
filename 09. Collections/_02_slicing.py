"""
Slicing
"""

students = ["student1", "student2", "student3", "student4", "student5"]

for i in range(5):
    print("Student at {}: {}".format(i, students[i]))

print()
for i in range(-1, -(len(students) + 1), -1):
    print("Student at {}: {}".format(i, students[i]))

print()
print("Last element:", students[-1])

print()
print("First student first character:", students[0][0]) 

print()
print(students[ 0 : 2 ])  
print(students[ 1 : len(students) - 1 ]) 
print(students[ 1 : -2 ]) 
print(students[ 3 : ]) # 3 to the end
print(students[ : 3 ]) # start to 3
print(students[ : -2 ]) # start to -2
print(students[ : ]) 

print()
print(students[ : 4 : 2]) # increment of 2
print(students[ : -1 : 2])
print(students[::2])
print(students[::-1])
print(students[::-2])

print()
backupList = students # refers to the same object
print(students)
print(backupList)
students[0] = "XXX"
print(students)
print(backupList)

print()
backupList = students[:] # slicing creates a copy
print(students)
print(backupList)
students[0] = "YYY"
print(students)
print(backupList)
