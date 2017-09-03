"""
Class - Node
"""

class Node:

    def __init__(self, obj=None, next=None):
        self.__obj = obj
        self.next = next

    def __str__(self):
        return str(self.__obj)
