"""
sys.exc_info
"""

import sys

try:
    b = "1"
    a = 1 / b
except TypeError as err:
    print("Error:", sys.exc_info())
except:
    print("ERROR:", sys.exc_info()[0])
else:
    print("Everithings Ok.")
