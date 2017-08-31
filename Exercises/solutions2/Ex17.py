"""
Exercise 17
"""

import os
from pathlib import Path

def reverse(filepathIn, filepathOut):
    with open(filepathIn, "r") as FileIn:
        with open(filepathOut, "w+") as fileOut:
            for item in FileIn.readlines()[::-1]:
                fileOut.write(item)

filePathIn = str(os.path.realpath(__file__))
filePathOut = str(Path(os.path.dirname(__file__)).parent.parent.joinpath("Temp", "Ex17Out.txt"))

reverse(filePathIn, filePathOut)
