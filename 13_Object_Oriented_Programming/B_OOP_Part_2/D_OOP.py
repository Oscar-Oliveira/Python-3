"""
OOP - Examples
"""

import A_Owner as O
import B_Animal as A

dog1 = A.Animal(None)
dog2 = A.Animal(O.Owner("Jack"), "Rufus", 15)

print(dog1) # call  __str__ from animal
print("Pack: ", A.Animal.Count())

dog1.walk(10)
dog2.walk(25)

dog1.walk(25)
dog1.speak()
dog1.walk(125)

dog1.escaped()
del dog1  # call  __del__ from animal

print("Pack: ", A.Animal.Count())

print()
print(A.Animal.__doc__)
print(A.Animal.walk.__doc__)

print()
dog3 = A.Animal(O.Owner("Jack"), "Rufus", 15)
print(id(dog2))
print(id(dog3))
print(dog2 == dog3) # uses __eq__ from animal
print(dog2 is dog3)
