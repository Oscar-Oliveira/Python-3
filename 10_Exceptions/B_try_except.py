"""
try except
"""

try:
    a = 1 / 0
except ZeroDivisionError:
    print("Something went wrong with a zero value")
except (TypeError, ValueError):
    print("Something went wrong with values")
except:
    print("Something went wrong")
else: print("Everithings Ok.")
