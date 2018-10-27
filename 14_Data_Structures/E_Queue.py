"""
Queue
"""

from A_Location import Location
from B_Node import Node

class QueueADT():

    def remove(self):
        raise NotImplementedError("Must implement this")

    def insert(self):
        raise NotImplementedError("Must implement this")

    def is_empty(self):
        raise NotImplementedError("Must implement this")

class Queue1(QueueADT):

    def __init__(self):
        self.Items = []

    def insert(self, obj):
        self.Items.append(obj)

    def remove(self):
        return_value = self.Items[0]
        del self.Items[0]
        return return_value

    def is_empty(self):
        return self.Items == []

class Queue2(QueueADT):

    def __init__(self):
        self.length = 0
        self.head = None

    def insert(self, obj):
        node = Node(obj)
        if self.is_empty():
            self.head = node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = node
        self.length += 1

    def remove(self):
        return_value = self.head
        self.head = self.head.next
        self.length -= 1
        return return_value

    def is_empty(self):
        return self.length == 0

class Queue3(QueueADT):

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def insert(self, T):
        node = Node(T)
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove(self):
        return_value = self.head
        self.head = self.head.next
        self.length -= 1
        if self.is_empty():
            self.tail = None
        return return_value

    def is_empty(self):
        return self.length == 0

def testQ(queue):
    queue.insert(Location("porto"))
    queue.insert(Location("Aveiro"))
    queue.insert(Location("lisboa"))
    while not queue.is_empty():
        print(queue.remove(), end=" ")

def main():

    testQ(Queue1())
    print()

    testQ(Queue2())
    print()

    testQ(Queue3())
    print()

if __name__ == "__main__":
    main()
