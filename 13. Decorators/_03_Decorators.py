"""
Decorators
"""

import logging
import sys
import random

logging.basicConfig(stream=sys.stdout, \
    format="%(asctime)s : %(levelname)s : %(message)s", \
    level=logging.DEBUG)
log = logging.getLogger("retry")

def log_me(func):

    def wrapper(arg):
        log.info("{}: {}".format(func.__name__, arg))
        func(arg)

    return wrapper

@log_me
def dummy1(arg):
    print("+++++", arg)
    
@log_me
def dummy2(arg):
    print("-----", arg)

@log_me
def dummy3(arg):
    print("*****", arg)

def main():
    functions = [dummy1, dummy2, dummy3]
    args = ["Server 1", "Server 2", "Server 3"]

    for i in range(20):
        functions[random.randint(0, len(functions)-1)]\
            (random.randint(0, len(args)-1))

if __name__ == "__main__":
    main()
