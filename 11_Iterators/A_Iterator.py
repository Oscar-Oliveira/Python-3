"""
Iterator
"""

def get_next_value(data):
    try:
        return next(data)
    except StopIteration:
        return None

students = ["student1", "student2", "student3", "student4"]

iterator = iter(students)

while True:
    a = get_next_value(iterator)
    if a:
        print(a)
        continue
    break
    