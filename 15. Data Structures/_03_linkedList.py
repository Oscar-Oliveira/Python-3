"""
Class - LinkedList
"""

from _01_Location import Location
from _02_Node import Node

class LinkedList():

    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, obj):
        self.head = Node(obj, self.head)
        self.length += 1

    def print(self):
        node = self.head
        while node:
            print(node, end=" ")
            node = node.next
        print()

    def _print_reversed(self, node):
        if node:
            self._print_reversed(node.next)
            print(node, end=" ")

    def print_reversed(self):
        self._print_reversed(self.head)

def main():

    linked_list = LinkedList()
    linked_list.add(Location("porto"))
    linked_list.add(Location("Aveiro"))
    linked_list.add(Location("lisboa"))

    linked_list.print()
    print()
    linked_list.print_reversed()

if __name__ == "__main__":
    main()
