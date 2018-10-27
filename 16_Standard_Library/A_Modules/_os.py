"""
os
"""

import os
from pathlib import Path
import pprint as pp

def touch(filename):
    with open(filename, 'w') as file:
        file.write("")

print("__file__: ", __file__) 
print("basename: ", os.path.basename(__file__))
print("dirname: ", os.path.dirname(__file__))
print("realpath: ", os.path.realpath(__file__))
print("relpath: ", os.path.relpath(__file__))
print("split: ", os.path.split(__file__))

os.system("notepad test") # Run command in the system shell

tempfolder = str(Path(os.path.dirname(__file__)).parent.parent.joinpath("_Temp", "FOLDER"))
tempfolder2 = str(Path(os.path.dirname(__file__)).parent.parent.joinpath("_Temp", "FOLDER2"))

print(tempfolder, "\\n", tempfolder2)

if not os.path.exists(tempfolder):
    os.mkdir(tempfolder)

if not os.path.exists(tempfolder2):
    os.mkdir(tempfolder2)
    os.rmdir(tempfolder2)

print("isdir: ", os.path.isdir(__file__))
print("isfile: ", os.path.isfile(__file__))
print("join: ", os.path.join(tempfolder, "_Temp"))

print()
file1 = os.path.join(tempfolder, "tempFile.tmp")
file2 = os.path.join(tempfolder, "back.txt")
touch(file1)
os.rename(file1, file2)
os.startfile(file2)
os.remove(file2)

tempfolder = str(Path(tempfolder).joinpath("1", "2", "3"))
os.makedirs(tempfolder)

print()
print(os.getcwd()) # Get current folder
os.chdir("c:\\")
print(os.getcwd()) # Get current folder

print()
print(os.name)
print(os.sep)

print()
print(os.environ["PROGRAMFILES"])
print(os.getenv("PROGRAMFILES"))
for item in os.environ.items():
    print(item)

for root, dirs, files in os.walk(str(Path(os.path.dirname(__file__)).parent)):
    print(root, dirs, files)
    print()


