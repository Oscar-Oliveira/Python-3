"""
OOP - Examples
"""

from _02_Animal import Animal
from _05_Dogs_and_Cats import Dog, Cat

A1 = Dog("Rufus")
A2 = Dog("Bobby")
A3 = Cat("Kitty")
A4 = Cat("Diamond")
A5 = Animal("T-REX")

# call to class method
print("Class: ", A1.Which())
print("Class: ", A2.Which())
print("Class: ", A3.Which())
print("Class: ", A4.Which())
print("Class: ", A5.Which())

print()
print("Pets: ", Animal.Count())

print()
A1.walk(10)
A2.walk(25)
A3.walk(5)
A4.walk(15)

print()
pets = [A1, A2, A3, A4, A5]
for animal in pets:
    if isinstance(animal, Dog):
        animal.sniff()
    animal.speak()
