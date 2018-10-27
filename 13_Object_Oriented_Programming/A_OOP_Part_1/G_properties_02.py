"""
Properties - Decorators
Class - PointExt3
"""

from B_Point import Point

class PointExt3(Point):

    _defaut_Color = None

    def __init__(self, x, y):
        super().__init__(x + 2, y + 2)
        self.__color = PointExt3._defaut_Color

    @property
    def Color(self):
        return self.__color

    @Color.setter
    def Color(self, value):
        self.__color = value

    @Color.deleter
    def Color(self):
        print("Deleting color...")
        del self.__color

def main():

    point = PointExt3(2, 2)
    print(point.Color)
    point.Color = "red"
    print(point.Color)
    del point.Color

if __name__ == "__main__":
    main()
    print("Done!")
