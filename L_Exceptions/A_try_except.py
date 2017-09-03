"""
try except
"""

try:
    a = 1 / 2
except:
    print("Something went wrong")

try:
    a = 1 / 0
except:
    print("Something went wrong")
else: # Executes if no exceptions are raised
    print("Everithings Ok.")
