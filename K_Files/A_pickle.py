"""
pickle
- Allows the serialization of complex objects
"""

import pickle
import os
from pathlib import Path

grades = {
    "student1": [10, 11, 12],
    "student2": [15, 14, 14],
    "student3": [10, 10, 12],
    "student4": [14, 14, 10]
}

filePath = str(Path(os.path.dirname(__file__)).parent.joinpath("_Temp", "pickle.dat"))

file = open(filePath, "wb") 
pickle.dump(grades, file) 
file.close() 

file = open(filePath, "rb")
grades2 = pickle.load(file)
print(grades2)
print(len(grades2))
print(grades2["student1"][1])
