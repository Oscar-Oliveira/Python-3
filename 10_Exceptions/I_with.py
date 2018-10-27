"""
with
- with EXPR as VAR: BLOCK
- call VAR.__enter__ method at the begining
- call VAR.__exit__ method at the end
"""

import os
import inspect
from pathlib import Path

filePath = str(Path(os.path.dirname(__file__)).parent.joinpath("_Temp", "with.txt"))

# Guaranteed to close the file
with open(filePath, "w") as file:
    file.write("Hi there!")
    print(dir(file))

print()
a = [2, 4, 2]
print(dir(a))

class temp:

    def __enter__(self):
        print("__enter__")
        return self

    def Using(self):
        print("Using()")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")

print()
print(dir(temp))

print()
with temp() as t:
    t.Using()
