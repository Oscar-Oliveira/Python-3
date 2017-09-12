"""
Tree
"""

from A_Location import Location

class TreeADT():

    def insert(self):
        raise NotImplementedError("Must implement this")

    def traverseInorder(self):
        raise NotImplementedError("Must implement this")

    def traversePreorder(self):
        raise NotImplementedError("Must implement this")

    def traversePostorder(self):
        raise NotImplementedError("Must implement this")

class Tree(TreeADT):

    class Node():

        def __init__(self, obj):
            self.obj = obj
            self.left = None
            self.right = None

        def __str__(self):
            return str(self.obj)

    def __init__(self):
        self.root = None

    def insert(self, obj, node=None):
        if not self.root:
            self.root = Tree.Node(obj)
        else:
            if node is None:
                node = self.root
            if node.obj > obj:
                if node.left is None:
                    node.left = Tree.Node(obj)
                else:
                    self.insert(obj, node.left)
            else:
                if node.right is None:
                    node.right = Tree.Node(obj)
                else:
                    self.insert(obj, node.right)

    def traverseInorder(self):
        self._traverseInorder(self.root)

    def traversePreorder(self):
        self._traversePreorder(self.root)

    def traversePostorder(self):
        self._traversePostorder(self.root)

    def _traverseInorder(self, node):
        if node is not None:
            self._traverseInorder(node.left)
            print(node.obj)
            self._traverseInorder(node.right)

    def _traversePreorder(self, node):
        if node is not None:
            print(node.obj)
            self._traversePreorder(node.left)
            self._traversePreorder(node.right)

    def _traversePostorder(self, node):
        if node is not None:
            self._traversePreorder(node.left)
            self._traversePreorder(node.right)
            print(node.obj)

def main():
    tree = Tree()
    tree.insert(Location("porto"))
    tree.insert(Location("Felgueiras"))
    tree.insert(Location("Aveiro"))
    tree.insert(Location("Alijo"))
    tree.insert(Location("lisboa"))
    tree.insert(Location("beja"))
    tree.insert(Location("evora"))
    tree.insert(Location("braga"))

    tree.traverseInorder()

    print()
    tree.traversePreorder()

    print()
    tree.traversePostorder()

if __name__ == "__main__":
    main()
