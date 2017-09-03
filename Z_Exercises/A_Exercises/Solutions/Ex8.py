"""
Exercise 8
"""

import csv

sep = ";"
with open("data.csv", "r") as file:
    data = csv.reader(file, delimiter=sep)
    for row in data:
        print(" | ".join(row))
