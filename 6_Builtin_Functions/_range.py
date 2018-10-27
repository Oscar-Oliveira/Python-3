"""
range
"""

def print_range(values):
    print(", ".join([str(i) for i in values]))

# range (stop)
print(list(range(4)))
print_range(range(4))
print_range(range(10))

# range (start, finish, [step])
print_range(range(3, 20))
print_range(range(0, 20, 2))
print_range(range(1, 20, 2))
print_range(range(20, 0, -1))
print_range(range(-20, 0, 2))
print_range(range(0, -20, -2))
