"""
Conditional expressions (ternary)
"""

grade = 9.5
value = "Approved" if grade >= 9.5 else "Not Approved"
print(value)

is_valid = False
value = 1 if is_valid else 0
print(value)

def One():
    print("First function")

def Two():
    print("Second function")

value = One if value else Two
value()
