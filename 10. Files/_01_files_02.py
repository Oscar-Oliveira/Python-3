"""
Files
"""

import os

file = open(os.path.realpath(__file__), "r")
lines = file.readlines()
for line in lines:
    print(line, end="")
file.close()
