"""
Class - Rectangle
"""

import copy
from A_GeometricForm import GeometricForm
from B_Point import Point

class Rectangle(GeometricForm):

    def __init__(self, c, w, h):
        self.__corner = c
        self.__width = w
        self.__height = h

    def get_width(self):
        return self.__width
    def set_width(self, value):
        self.__width = value

    def get_height(self):
        return self.__width
    def set_height(self, value):
        self.__width = value

    Width = property(get_width, set_width)
    Height = property(get_height, set_height)

    def get_corner(self):
        return self.__corner.get_point()

    def __str__(self):
        return "Corner:{} Width:{} Height:{}".\
            format(self.__corner.get_point(), self.__width, self.__height)

    def my_ids(self):
        print("self:", id(self))
        print("Corner:", id(self.__corner))
        print("Width:", id(self.__width))
        print("Height:", id(self.__height))

def main():

    rectangle = Rectangle(Point(1, 1), 1000, 1500)
    print(rectangle)
    print(rectangle.get_corner())

    print()
    rectangle.my_ids()

    print()
    rectangle2 = rectangle
    rectangle2.my_ids()

    print()
    rectangle3 = copy.copy(rectangle)
    rectangle3.my_ids()
    del rectangle3

    print()
    rectangle4 = copy.deepcopy(rectangle)
    rectangle4.Width = 20000
    rectangle4.my_ids()
    print()
    rectangle.my_ids()

if __name__ == "__main__":
    main()
  