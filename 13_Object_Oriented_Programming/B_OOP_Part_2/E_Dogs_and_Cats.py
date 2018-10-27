"""
Dogs and Cats
"""

from B_Animal import Animal

class Dog(Animal):

    def __init__(self, ownby, name="A. Doe", age=0):
        super().__init__(ownby, name, age)

    def speak(self):
        print(self._name, ": AU!!! AU!! AU!!")

    def sniff(self):
        print(self._name, " is sniffing!")

class Cat(Animal):

    def speak(self):
        print(self._name, ": MIAU!!! MIAU!! MIAU!!")
