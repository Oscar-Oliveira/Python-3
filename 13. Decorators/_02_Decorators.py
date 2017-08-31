"""
Decorators
"""

import time
import random

def execTime(func):

    def wrapper():
        t1 = time.time()
        func()
        print("ExecTime: {}".format(time.time() - t1))

    return wrapper

@execTime
def dummy_function1():
    sum_ = 0
    for value in range(500):
        sum_ += value
    print("\nSum: ", str(sum_))

@execTime
def dummy_function2():
    mult = 1
    for value in range(1, 500):
        mult *= value
    print("Mult: ", str(mult))

@execTime
def main():
    dummy_function1()
    dummy_function2()

if __name__ == "__main__":
    main()
