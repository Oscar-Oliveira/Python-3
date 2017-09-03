"""
Logical operators and nested if
"""

grade1 = 15
grade2 = 6
avg_grade = (grade1 + grade2) / 2.0

if avg_grade >= 9.5 and grade1 >= 9.5 and grade2 >= 9.5:
    print("Student is aproved")
    if avg_grade >= 17:
        print("Give him a little start!!")
elif avg_grade >= 7.5 and grade1 >= 7.5 and grade2 >= 7.5:
    print("Exam")
elif avg_grade >= 5.5 and (grade1 >= 15 or grade2 >= 15):
    print("Assigment")
else:
    print("Student is not aproved")

print()
student_name = "Student 1"
is_student = False
if student_name == "Student 1" \
    or student_name == "Student 2" \
    or student_name == "Student 3":
    is_student = True
print(is_student)

print()
is_student = student_name in ["Student 1", "Student 2", "Student 3"]
print(is_student)
