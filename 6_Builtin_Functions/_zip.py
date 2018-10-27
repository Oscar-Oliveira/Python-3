"""
zip
"""

students = ["Student1", "Student2", "Student3", "Student4", "Student5"] 
grades1 = [12, 14, 15, 15] 
grades2 = [13, 14, 14, 14, 10] 

for item in zip(students, grades1, grades2):
    print(item)

for name, first, second in zip(students, grades1, grades2):
    print("{}: {}".format(name, (first+second) / 2))
