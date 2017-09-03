"""
Exercise 9
"""

import sys

def write_to_file(filename, text):
    with open(filename, "a") as file:
        file.write(text + "\n")

filename = input("File: ")
text = input("Text: ")

write_to_file(filename, text)
