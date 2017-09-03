"""
Class - Location
"""

class Location():

    def __init__(self, name, value=0):
        self.name = name
        self.value = value

    def __str__(self):
        return str(self.name).title()

    def __gt__(self, other):
        return self.name > other.name
    