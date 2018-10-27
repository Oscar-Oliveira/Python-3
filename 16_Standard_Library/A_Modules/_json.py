"""
json
"""

import json
import os
from pathlib import Path

filePath = str(Path(os.path.dirname(__file__)).parent.parent.joinpath("_Temp", "json.log"))

grades = {
    "student1": [10, 11, 12],
    "student2": [15, 14, 14],
    "student3": [10, 10, 12],
    "student4": [14, 14, 10]
}

json_ = json.dumps(grades)
print(json_)

grades = json.loads(json_)
print(grades)

with open(filePath, "w") as file:
    json.dump(grades, file)

with open(filePath, "r") as file:
    grades = json.load(file)
    print(grades)