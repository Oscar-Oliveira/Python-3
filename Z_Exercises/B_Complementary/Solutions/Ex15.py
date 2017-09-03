"""
Exercise 15
"""

def add_vector1(v1, v2):
    result = []
    for i in range(len(v1)):
        result.append(v1[i] + v2[i])
    return result

def add_vector2(v1, v2):
    result = []
    for one, two in zip(v1, v2):
        result.append(one + two)
    return result

def scalar_multiple1(f, v):
    result = []
    for item in v:
        result.append(f * item)
    return result
    [x * f for x in v]

def scalar_multiple2(f, v):
    return [x * f for x in v]

print(add_vector1([1, 2, 3], [1, 2, 3]))
print(add_vector2([1, 2, 3], [1, 2, 3]))

print(scalar_multiple1(2, [1, 2, 3]))
print(scalar_multiple2(2, [1, 2, 3]))
