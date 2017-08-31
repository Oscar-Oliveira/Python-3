"""
Multiple inheritance
Class - NewDog
"""

from _07_Chipped import Chipped
from _05_Dogs_and_Cats import Dog

class NewDog(Dog, Chipped):

    def __init__(self, name, chipNumber):
        Dog.__init__(self, None, name)
        Chipped.__init__(self, chipNumber)

    def Print(self):
        print(self.get_name())
        print(self.chip)

        print(Dog.get_name(self))
        print(Chipped.get_name(self))

if __name__ == "__main__":
    A1 = NewDog("Rufus", "XPTO0001")
    A1.Print()
