"""
as
"""

try:
    a = 1 / 0
except ZeroDivisionError as err:
    print("Error:", err)
except TypeError as err:
    print("Error:", err, "\nCould not convert data.")
else:
    print("Everithings Ok.")
