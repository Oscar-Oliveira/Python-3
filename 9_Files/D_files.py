"""
Files
"""

import os
import time
from pathlib import Path

filePath = str(Path(os.path.dirname(__file__)).parent.joinpath("_Temp", "files.txt"))

fileOut = open(filePath, "w+")
fileOut.write("{}\n\n".format("_" * 40))
fileOut.write("Backup created: ")
fileOut.write(time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
fileOut.write("{}\n\n".format("_" * 40))

fileIn = open(os.path.realpath(__file__), "r")
for line in fileIn:
    print(line)
    fileOut.write(line) 
fileIn.close()
fileOut.close()
