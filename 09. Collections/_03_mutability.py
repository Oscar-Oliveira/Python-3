"""
Mutability
- Python is strongly object-oriented in the sense that everything
    is an object including numbers, strings and functions
- Immutable objects: int, float, decimal, complex, bool, string,
    tuple, range, frozenset, bytes
- Mutable objects: list, dict, set, bytearray,user-defined classes
"""

def memory_address(obj):
    return hex(id(obj))

def print_memory(obj):
    print(memory_address(obj), ":", obj)

print(id(memory_address))

# integers are immutable
print()
integer_ = 5
print_memory(integer_)
integer_ += 1
print_memory(integer_)

print()
integer2_ = integer_
print(integer_ is integer2_) # identity equality

# tuples are immutable
print()
tuple_ = (1, 2, 3)
print_memory(tuple_)
tuple_ += (4, 5, 6)
print_memory(tuple_)

# list are mutable
print()
list_ = []
print_memory(list_)
list_ += [11, 22]
print_memory(list_)
list_.append(33)
print_memory(list_)
list_.remove(11)
print_memory(list_)

print()
list1 = [1, 2, 3] 
list2 = [1, 2, 3] 
print(list1 == list2)
print(list1 is list2)

print()
print(type(list_[0]))
print_memory(list_[0])
print_memory(list_)
list_[0] = 123
print_memory(list_[0])
print_memory(list_)
