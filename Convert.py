#!/usr/bin/python
"""
Convert file structure
 :arg --md : to create md file to print (pandoc Out.md -o output.pdf)
 :arg -- pitchme : to create gitpitch file
"""

import os
from pathlib import Path
import sys

class Content(object):
    """Content Container"""
    def __init__(self):
        self._content = []

    def Add(self, text):
        self._content.append("{}\n".format(text))

    def Get(self):
        return "".join(self._content)

excludeFolders = [".git", ".vscode", "Assets", "Temp", "__pycache__", "Package1", "Package2", "Exercises"]
excludeFiles = ["__init__.py" ]
codeExtensions = [".py"]

def SetHeader(filePath, content, level, n):
    """ Extract header from code files """
    with open(filePath) as filetemp:
        line = filetemp.readline()
        if line.strip() == "#!/usr/bin/python":
            filetemp.readline()
        head = filetemp.readline()
        if head:
            content.Add("{} {}".format("#" * (level + n), head))

def GetTopicName(path):
    return path.split('.')[-1].strip()

def CreateFile(filename, content, toprint = False):
    folder = os.path.dirname(os.path.realpath(__file__))
    backupFile = os.path.join(folder, "Temp", "_" + filename)
    newFile = os.path.join(folder, filename)
    if os.path.isfile(backupFile): os.remove(backupFile)
    if os.path.isfile(newFile): os.rename(newFile, backupFile)
    md = content.Get()
    with open(newFile, "w") as file:
        file.write(md)
    if toprint:
        print(md)

def MD(toPrint):
    content = Content()
    #content.Add("---")
    #content.Add("geometry: margin=2cm")
    #content.Add("---")
    #content.Add("\n")
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in excludeFolders]
        level = root.count("\\")
        if level != 0:
            topicName = GetTopicName(root)
            if topicName != "Cover":
                content.Add("{} {}".format("#" * (level + 1), topicName))
            files[:] = [f for f in files if f not in excludeFiles]
            for name in files:
                filePath = os.path.join(root, name)
                if name.endswith(".md"):
                    with open(filePath) as file:
                        content.Add(file.read())
                if Path(name).suffix in codeExtensions:
                    SetHeader(filePath, content, level, 2)
                    content.Add("```")
                    with open(filePath) as file:
                        content.Add(file.read())
                    content.Add("```")
    CreateFile("Output.md", content, toPrint)

def Pitch(toPrint):
    content = Content()
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in excludeFolders]
        level = root.count("\\")
        if level != 0:
            topicName = GetTopicName(root)
            if topicName != "Cover":
                content.Add("---\n{}  {}".format("#" * (level + 1), topicName))
            files[:] = [f for f in files if f not in excludeFiles]
            for name in files:
                filePath = os.path.join(root, name)
                if name.endswith(".md"):
                    content.Add("+++?include={}".format(filePath.replace(" ", "%20").replace("\\", "/")))
                if Path(name).suffix in codeExtensions:
                    content.Add("+++?code={}&lang=python".format(filePath.replace(" ", "%20").replace("\\", "/")))
                    with open(filePath, "r") as file:
                        start = currentLine = 0
                        for line in file:
                            currentLine += 1
                            if start == 0 and line not in ['\n', '\r\n']:
                                start = currentLine
                            if line in ['\n', '\r\n'] and currentLine != 1:
                                content.Add("@[{}-{}]".format(start, currentLine - 1))
                                start = currentLine + 1
                        if start != 0 and currentLine != 0:
                            content.Add("@[{}-{}]".format(start, currentLine))

    CreateFile("PITCHME.md", content, toPrint)

if __name__ == "__main__":
    commands = sys.argv[1:]
    if not commands: commands.append("--pitchme") # create default
    if "--md" in commands: MD(True)
    if "--pitchme" in commands: Pitch(True)
    print("Done")
