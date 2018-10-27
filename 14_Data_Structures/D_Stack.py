"""
Stack
"""

from A_Location import Location

class StackADT():

    def pop(self):
        raise NotImplementedError("Must implement this")

    def push(self):
        raise NotImplementedError("Must implement this")

    def is_empty(self):
        raise NotImplementedError("Must implement this")

class Stack(StackADT):

    def __init__(self):
        self.__items = []

    def pop(self):
        return self.__items.pop()

    def push(self, obj):
        self.__items.append(obj)

    def is_empty(self):
        return self.__items == []

def main():

    stack = Stack()
    stack.push(Location("porto"))
    stack.push(Location("Aveiro"))
    stack.push(Location("lisboa"))

    while not stack.is_empty():
        print(stack.pop(), end=" ")

if __name__ == "__main__":
    main()
