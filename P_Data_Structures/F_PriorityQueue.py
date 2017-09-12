"""
Priority Queue
"""

from A_Location import Location
from E_Queue import Queue1

class PriorityQueue(Queue1):

    def remove(self):
        pos = 0
        for i in range(1, len(self.Items)):
            if self.Items[i].value > self.Items[pos].value:
                pos = i
        return_value = self.Items[pos]
        del self.Items[pos]
        return return_value

def testPQ(queue):
    queue.insert(Location("porto", 216405))
    queue.insert(Location("Aveiro", 78455))
    queue.insert(Location("lisboa", 506892))
    while not queue.is_empty():
        print(queue.remove(), end=" ")

def main():
    testPQ(PriorityQueue())
    print()

if __name__ == "__main__":
    main()
