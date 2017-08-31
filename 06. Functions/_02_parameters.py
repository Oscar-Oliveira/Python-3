"""
Parameters
"""

def write_names(value1, value2):
    print("{} : {}".format(value1, value2))

def print_max(value1, value2):
    if value1 >= value2:
        print(value1)
    else:
        print(value2)

def say(value, qty):
    print(value * qty)

write_names("Student1", "123")
write_names("Student2", "456")
write_names("Student3", "789")

print()
value1 = 10
value2 = 12
print("Max ({}, {}): ".format(value1, value2))
print_max(value1, value2)

print()
say("Python", value1)
