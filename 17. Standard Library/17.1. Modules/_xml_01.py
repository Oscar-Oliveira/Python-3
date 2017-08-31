'''
xml - minidom
'''

import xml.dom.minidom
import urllib.request
import os
from pathlib import Path
from pprint import pprint as p

class StudentParser(object):

    def __init__(self, url):
        self.students = []
        self._enrolled = 0
        students = self.get_XML(url)
        self.get_students(students)

    def get_XML(self, url):
        try:
            f = urllib.request.urlopen(url)
        except urllib.error.URLError:
            f = url
        doc = xml.dom.minidom.parse(f)
        return doc.documentElement

    def get_text(self, node):
        return " ".join(t.nodeValue \
                        for t in node[0].childNodes \
                        if t.nodeType == t.TEXT_NODE)

    def get_grades(self, node):
        grades = []
        for n in node.getElementsByTagName("grade"):
            number = n.getAttribute("number")
            grade = n.firstChild.nodeValue
            grades.append((number, grade))
        return grades

    def get_students(self, xml):
        self._enrolled = xml.getAttribute("enrolled")
        for node in xml.getElementsByTagName("student"):
            number = node.getAttribute("number")
            name = self.get_text(node.getElementsByTagName("name"))
            grades = self.get_grades(node.getElementsByTagName("grades")[0])
            self.students.append({"name": name, "number": number, \
                "grades": grades})
  
if __name__ == "__main__":
    filePath = str(Path(os.path.dirname(__file__)).parent.parent.joinpath("Temp", "students.xml"))
    print(filePath)
    students = StudentParser(filePath)
    p(students.students)
