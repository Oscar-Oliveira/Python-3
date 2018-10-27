"""
Scope
"""

value = "Global Scope"

def write_v1():
    value = "Inner Scope"
    print(value)

def write_v2(value): # 1) by Value, 2) Overloading is not allowed
    print("Param. Value: " + value)
    Value = "Inner Scope"
    print(Value)

def write_v3():
    global value
    print("Value: " + value)
    value = "Inner Scope"
    print(value)

def outer():

    def inner():
        print("2")

    print("1")
    inner()

print(value)
write_v1()
print(value)

print()
write_v2(value)
print(value)

print()
write_v3()
print(value)

print()
outer()
