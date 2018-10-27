"""
Exercise 10
"""

grades = [20, 10, 10, 5, 10]

def avg(grades):
    return sum(grades) / len(grades)

def pos(grades):
    grades = [x for x in grades if x >= 9.5]
    return sum(grades)

def mean(grades):
    temp = sum(grades) - min(grades) - max(grades)
    return temp / (len(grades) - 2)

print(avg(grades))

print(pos(grades))

print(mean(grades))
