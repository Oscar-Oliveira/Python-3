"""
sum
"""

values = [10, 10, 5, 25, 25, 25.0]
print(values)
print(sum(values))

values = list(range(10))
print(values)
print(sum(values))

values = ["10.5", "11", 12.6]
print(values)
print(sum([float(x) for x in values]))
