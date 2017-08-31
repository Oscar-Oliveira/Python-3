"""
operator
"""

import operator

def calculate(op, max_):
    print("\n")
    for x in range(1, max_+1):
        print()
        for y in range(1, max_+1):
            result = op(x, y)
            if isinstance(result, float):
                print("{:7.2f}".format(result), end="")
            else:
                print("{:5}".format(result), end="")

for o in (operator.add, operator.sub, operator.mul, operator.itruediv):
    calculate(o, 10)
