"""
Attributes
"""

from B_Point import Point

def main():

    point1 = Point(1, 2)
    point2 = Point(2, 2)

    print(hasattr(point1, "color"))
    setattr(point1, "color", "red")
    print(hasattr(point1, "color"))

    print()
    color = getattr(point1, "color", "blue")
    print(color)
    color = getattr(point2, "color", "blue")
    print(color)

    delattr(point1, "color")
    print(hasattr(point1, "color"))

if __name__ == "__main__":
    main()
    print("Done!")
