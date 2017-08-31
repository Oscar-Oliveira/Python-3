"""
Properties - Decorators
Class - PointExt3
"""

from _02_Point import Point

class PointExt3(Point):

    def __init__(self, x, y):
        super().__init__(x + 2, y + 2)
        self.__color = None

    @property
    def Color(self):
        return self.__color

    @Color.setter
    def Color(self, value):
        self.__color = value

def main():

    point = PointExt3(2, 2)
    print(point.Color)
    point.Color = "red"
    print(point.Color)

if __name__ == "__main__":
    main()
    print("Done!")
