"""
Multiple inheritance
Class - NewDog
"""

from G_Chipped import Chipped
from E_Dogs_and_Cats import Dog

def my_printer(self):
    print(self.get_name())
    print(self.chip)

    print(Dog.get_name(self))
    print(Chipped.get_name(self))

class NewDog(Dog, Chipped):

    printer = my_printer

    def __init__(self, name, chipNumber):
        Dog.__init__(self, None, name)
        Chipped.__init__(self, chipNumber)
        self.tricks = []

    def print(self):
        self.printer()

if __name__ == "__main__":
    A1 = NewDog("Rufus", "XPTO0001")
    A1.print()
