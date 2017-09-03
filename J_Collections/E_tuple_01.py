"""
Tuple
"""

def my_sum(values):
    sum_ = 0
    for item in values:
        if isinstance(item, int) or isinstance(item, float):
            sum_ += item
        else:
            sum_ += my_sum(item)
    return sum_

def my_len(values):
    sum_ = 0
    for item in values:
        if isinstance(item, int) or isinstance(item, float):
            sum_ += 1
        else:
            sum_ += my_len(item)
    return sum_

def sum_and_len(values):
    sum_ = 0
    len_ = 0
    for item in values:
        if isinstance(item, int) or isinstance(item, float):
            len_ += 1
            sum_ += item
        else:
            sum_ += my_sum(item)
            len_ += my_len(item)
    return (sum_, len_)

if __name__ == "__main__":

    temp = tuple("Constructor")
    print(temp)
    temp = tuple(["Anoter", "Constructor", 2])
    print(temp)

    first_year_grades = (15, 18, 12, 10)
    second_year_grades = (13, 13, 12, 11)

    empty_tuple = ()
    singleton_tuple = (2, ) # (2) is integer 2

    grades = (15, 20, first_year_grades, second_year_grades)
    # could be done without parentheses, but bad practice
    # grades = 15, 20, firstYearGrades, secondYearGrades

    print()
    print(",".join(str(x) for x in first_year_grades))

    del first_year_grades
    del second_year_grades

    temp = (10, ) * 3 # (10, 10, 10)
    grades += temp # concatenation

    print()
    print(grades)
    print(len(grades))

    print()
    print(19 in grades)

    print()
    print("Sum:", my_sum(grades))
    print("Grades:", my_len(grades))
    print("AVG:", my_sum(grades)/ my_len(grades))

    print()
    print("First year grades: ", grades[2])
    print("Second year grades: ", grades[3])

    print()
    print("First year First grade: ", grades[2][0])
    print("First year Second grade: ", grades[2][1])
    print("First year Third grades: ", grades[2][2])

    a, b = sum_and_len(grades)
    print(a, b)

    _, b = sum_and_len(grades)
    print(b)
 