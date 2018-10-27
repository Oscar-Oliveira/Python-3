"""
Class - Point3D
"""

import math
from B_Point import Point

class Point3D(Point):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.__z = z

    def distance_from_origin(self):
        p = super().get_point()
        return Point3D.DistanceFrom(0, 0, 0, p[0], p[1], self.__z)

    @staticmethod
    def DistanceFrom(x, y, z, x1, y1, z1):
        return math.sqrt(math.pow(x - x1, 2) + \
                         math.pow(y - y1, 2) + \
                         math.pow(z - z1, 2))

    def GetPoint(self):
        p = super().get_point()
        return (p[0], p[1], self.__z)

def main():

    print(Point3D.__bases__) # attribute base classes

    point = Point3D(1, 2, 3)

    print(isinstance(point, Point))

    print(issubclass(Point3D, Point))
    print(issubclass(Point, Point3D))

    print(point.distance_from_origin())

    print(point.get_point())
    print(point.get_corner())

if __name__ == "__main__":
    main()
    print("Done!")
