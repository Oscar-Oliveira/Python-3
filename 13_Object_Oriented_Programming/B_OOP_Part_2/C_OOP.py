"""
OOP - Examples
"""

from A_Owner import Owner
from B_Animal import Animal

owner1 = Owner("Jack")
owner2 = Owner("John")

animal1 = Animal(None)
animal2 = Animal(owner2, "Rufus", 10)

print()
print(type(owner1))
print(type(animal1))

print()
print(isinstance(animal1, Owner))
print(isinstance(animal1, Animal))

animals = [animal1, animal2]

print()
for a in animals:
    a.speak()

print()
for a in animals:
    Animal.speak(a)

print()
for a in animals:
    a.get_name()

print()
# everything is "public"
for a in animals:
    print(a._name) # Bad pratice

print()
for a in animals:
    try:
        print("{:15}: {}".format(a.get_name(), a.get_owner_name()))
    except UnboundLocalError:
        print("{:15}: {}".format(a.get_name(), "No Owner"))

# Bad practice, call GetOwner() instaed
# Law of Demeter: Only talk to your immediate friends.
# See: https://en.wikipedia.org/wiki/Law_of_Demeter
print(animal2._owner.get_name())

print()
for a in animals:
    try:
        a.get_tag()
    except UnboundLocalError:
        print("{:15}: {}".format(a.get_name(), "No TAG"))

def new_tag_maker(name, owner, age):
    print("-" * 30)
    print("My name is {} and i am {} years old.".format(name, age))
    print("Please contact: {}".format(owner))
    print("-" * 30)

print()
for a in animals:
    try:
        a.get_tag(new_tag_maker)
    except UnboundLocalError:
        print("{:15}: {}".format(a.get_name(), "No TAG"))
              