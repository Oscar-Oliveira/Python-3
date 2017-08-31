'''
xml - etree.ElementTree
'''

try:
    # faster C implementation
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import os
import datetime
from pathlib import Path

def create(filename):
    root = ET.Element("students")
    tree = ET.ElementTree(root)
    with open(filename, "wb") as file:
        tree.write(file)

def append(filename, name, email):
    student = ET.Element("student")
    ET.SubElement(student, "name").text = name
    ET.SubElement(student, "email").text = email

    root = ET.ElementTree(file=filename).getroot()
    root.append(student)
    with open(filename, "wb") as file:
        ET.ElementTree(root).write(file)

def display(filename):
    print()
    tree = ET.ElementTree(file=filename)
    for student in tree.findall("student"):
        for node in student.getiterator():
            if node.text:
                print("{}: {}".format(node.tag, node.text))
        updated = student.attrib.get("updated")
        if updated:
            print(">>> Last updated at", updated)

def update(filename, name, newEmail):
    tree = ET.ElementTree(file=filename)
    root = tree.getroot()
    for elem in tree.iterfind('student[name="{}"]'.format(name)):
        elem.find("email").text = newEmail
        elem.set("updated", datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S"))
    with open(filename, "wb") as file:
        ET.ElementTree(root).write(file)

def delete(filename, name, all = False):
    removed = 0
    tree = ET.ElementTree(file=filename)
    root = tree.getroot()
    if all:
        for e in root.findall('student[name="{}"]'.format(name)):
            root.remove(e)
            removed += 1
    else:
        e = root.find('student[name="{}"]'.format(name))
        if e:
            root.remove(e)
            removed = 1
    with open(filename, "wb") as file:
        ET.ElementTree(root).write(file)
    return removed

if __name__ == "__main__":
    filePath = str(Path(os.path.dirname(__file__)).parent.parent.joinpath("Temp", "students2.xml"))
    create(filePath)
    append(filePath, "student1", "student1@email.com")
    append(filePath, "student2", "student2_1@email.com")
    append(filePath, "student3", "student3@email.com")
    append(filePath, "student4", "student4@email.com")
    append(filePath, "student2", "student2_2@email.com")
    append(filePath, "student2", "student2_3@email.com")
    append(filePath, "student2", "student2_4@email.com")
    append(filePath, "student2", "student2_5@email.com")
    display(filePath)

    update(filePath, "student1", "XXX@email.com")
    display(filePath)

    print("Removed:", delete(filePath, "student3"))
    display(filePath)

    print("Removed:", delete(filePath, "student2"))
    display(filePath)

    print("Removed:", delete(filePath, "student2", True))
    display(filePath)

    print("Removed:", delete(filePath, "studentXXX", True))
    display(filePath)

    print("Done!")
