"""
Owner
"""

class Owner():

    def __init__(self, name=None):
        self._name = name

    def get_name(self):
        return self._name

    def __str__(self):
        return "My name is " + self._name

if __name__ == "__main__":
    person = Owner("Jack")
    print(person)
    