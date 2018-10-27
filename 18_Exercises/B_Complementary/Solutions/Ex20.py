"""
Exercise 20
"""

class Geometric2D():

    def get_area(self):
        """Return area"""
        raise NotImplementedError("Must implement this")

    def get_perimeter(self):
        """Return perimeter"""
        raise NotImplementedError("Must implement this")

class Rectangle(Geometric2D):

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __str__(self):
        return "{}x{}".format(self.width, self.height)

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

class Square(Rectangle):

    def __init__(self, size):
        super().__init__(size, size)

if __name__ == "__main__":
    r = Rectangle(15, 10)
    print(r, r.get_area(), r.get_perimeter())

    s = Square(10)
    print(s, s.get_area(), s.get_perimeter())
