"""
Decorators
Class - PointExt1
See: http://pythoncentral.io/difference-between-staticmethod-and-classmethod-in-python/
"""

from B_Point import Point

class PointExt1(Point):

    def __init__(self):
        super().__init__(0, 0)
        self.__temp = 0

    # instance method
    def instance_method(self, x):
        self.__temp = x
        print("InstanceMethod: {}".format(self.__temp))

    @classmethod
    def class_method(cls, x):
        """
        class of the object instance is implicitly passed as argument.
        """
        print("ClassMethod: {} {}".format(cls.__name__, x))

    @staticmethod
    def static_method(x):
        """
        self (instance) and cls (class) are not
        implicitly passed as arguments.
        """
        print("StaticMethod: {} {}".format(x, Point.Counter))

def main():
    
    tempInstance = PointExt1()
    tempInstance2 = PointExt1()
    tempInstance.instance_method(10)
    tempInstance2.instance_method(15)

    print()
    tempInstance.class_method(10)
    PointExt1.class_method(10)

    print()
    tempInstance.static_method(10)
    PointExt1.static_method(10)

if __name__ == "__main__":
    main()
    print("Done!")
