"""
Handler
"""

import sys

def handleError(err):
    if err[0] == TypeError:
        print("Type Error!")
    elif err[0] == ZeroDivisionError:
        print("Zero Division Error!")
    else:
        print("Ups!")

try:
    a = 1 / "0"
except:
    handleError(sys.exc_info())
else:
    print("Everithings Ok.")
