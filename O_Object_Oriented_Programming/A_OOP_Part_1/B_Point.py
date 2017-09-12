"""
Class - Point
"""

from A_GeometricForm import GeometricForm

class Point(GeometricForm):
    """Class to define a point in space"""

    Counter = 0

    def __init__(self, x, y, name=None):
        self.__x = x # private
        self.__y = y # private
        self.name = name
        Point.Counter += 1

    def distance_from_origin(self):
        """Calculate distance from origin"""
        return ((self.__x ** 2) + (self.__y ** 2)) ** 0.5

    def get_point(self):
        return (self.__x, self.__y)

    # overides method from abstract class
    def get_corner(self):
        return self.get_point()

    def __str__(self):
        return "{}: {}x{}".format(self.name if self.name \
                        else "Not named", self.__x, self.__y)

    def __repr__(self):
        return "<{}, {}>".format(self.__class__.__name__, \
            self.__class__.__doc__)

    # rich comparison operators
    def __eq__(self, other):
        return self.distance_from_origin() == other.distance_from_origin()

    def __ne__(self, other):
        return self.distance_from_origin() != other.distance_from_origin()

    def __lt__(self, other):
        return self.distance_from_origin() < other.distance_from_origin()

    def __le__(self, other):
        return self.distance_from_origin() <= other.distance_from_origin()

    def __gt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def __ge__(self, other):
        return self.distance_from_origin() >= other.distance_from_origin()

    # Operator overload
    # See: https://docs.python.org/2/library/operator.html
    def __add__(self, other):
        p = other.get_point()
        return (self.__x + p[0], self.__y + p[1])

    def __mul__(self, other):
        p = other.get_point()
        return (self.__x * p[0], self.__y * p[1])

    @classmethod
    def From_Point(cls, point):
        return cls(point[0], point[1], "From class method")

def main():
    # Attributes
    print(Point.__doc__)
    print(Point.distance_from_origin.__doc__)
    print(Point.__name__)
    print(Point.__dict__) # Dictionary containing the class's namespace
    print(Point.__module__) # module name in which the class is defined

    point1 = Point(2, 2)
    point1.name = "My first point"
    point2 = Point(1, 2)

    # call method from abstract class
    print()
    print(point1.get_corner()) # if not implemented raise error

    print()
    print(point1) # call to __str__
    print(repr(point1)) # call to __repr__

    print()
    print(point1.distance_from_origin())
    print(point1.get_point())

    # call to rich comparison operators
    print()
    print(point1 == point2)
    print(point1 != point2)
    print(point1 < point2)
    print(point1 <= point2)
    print(point1 > point2)
    print(point1 >= point2)

    # call to rich comparison operators
    print()
    point3 = Point.From_Point(point1 + point2)
    print(point3)

    print()
    print(Point.Counter)

if __name__ == "__main__":
    main()
    print("Done!")
