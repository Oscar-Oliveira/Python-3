"""
Properties - Getter and Setter
Class - PointExt2
"""

from _02_Point import Point

class PointExt2(Point):

    def __init__(self, x, y):
        super().__init__(x + 2, y + 2)
        self.__color = None

    def get_color(self):
        return self.__color

    def set_color(self, value):
        self.__color = value

    Color = property(get_color, set_color)

def main():
    
    point = PointExt2(2, 2)
    print(point.Color)
    point.Color = "red"
    print(point.Color)

if __name__ == "__main__":
    main()
    print("Done!")
