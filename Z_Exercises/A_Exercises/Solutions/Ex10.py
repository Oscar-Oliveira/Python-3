"""
Exercise 10
"""

import sys

def print_file(filename):
    with open(filename, "r") as file:
        print(file.read())

try:
    filename = input("File: ")
    print_file(filename)
except FileNotFoundError:
    print("The file does not exist!!")
except:
    print("ERROR:", sys.exc_info()[0])
