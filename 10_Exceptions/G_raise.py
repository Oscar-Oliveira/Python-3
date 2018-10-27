"""
raise
"""

try:
    b = 5
    if b == 5:
        raise ValueError("Cannot divide by five :)")
    a = 1 / b
    print(a)
except ValueError as err:
    print("My exceptionError: {0}".format(err))
except ZeroDivisionError as err:
    print("Error: {0}".format(err))
except TypeError:
    print("Could not convert data to an integer.")
else:
    print("Everithings Ok.")
