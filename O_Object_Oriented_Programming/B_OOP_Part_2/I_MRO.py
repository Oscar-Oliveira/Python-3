"""
Method Resolution Order (MRO)
- See: http://python-history.blogspot.pt/2010/06/method-resolution-order.html
"""

class A(object):

    def __init__(self, value1):
        super(A, self).__init__()
        print("A > Passed value: {0}".format(value1))

class B(object):

    def __init__(self, value1):
        super(B, self).__init__(value1)
        print("B > Passed value: {0}".format(value1))

class C(object):

    def __init__(self, value1, value2):
        super(C, self).__init__(value1)
        print("C > Passed value: {0}".format(value2))

class D(C,B,A):

    def __init__(self, val1, val2):
        super(D, self).__init__(value1=val1, value2=val2)

def main():
    example = D(10, 20)
    print(D.__mro__)

if __name__ == "__main__":
    main()
