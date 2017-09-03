"""
Animal Class 
"""

from _01_Owner import Owner

class Animal:
    """Animal Class"""

    Counter = 0

    # initializer
    def __init__(self, ownby, name="A. Doe", age=0):
        self._name = name
        self._walked = 0
        self._owner = ownby
        self._age = age
        Animal.Counter += 1

    def _my_iteration(self, text):
        print(self._name, ":", text)

    # Instance Methods
    def speak(self):
        self._my_iteration("GRRRRR!!")

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def has_owner(self):
        return self._owner

    def get_owner_name(self):
        if self.has_owner():
            return self._owner.get_name()
        raise UnboundLocalError

    def _my_default_tag(self, name, owner, age):
        print("*" * 25)
        print("Name:", name)
        print("Owner:", owner)
        print("Age", age)
        print("*" * 25)

    def get_tag(self, maker=None):
        if not maker:
            maker = self._my_default_tag
        return maker(self._name, self.get_owner_name(), self._age)

    def walk(self, steps):
        self._walked += steps
        print(self._name, "walked", steps, "steps")

    def escaped(self):
        Animal.Counter -= 1

    @classmethod
    def Which(cls):
        return cls.__name__

    @staticmethod
    def Count():
        return Animal.Counter

    def __del__(self):
        print("I was destroyed")

    def __str__(self):
        return "My name is {} and i walked {} steps".format(self._name, self._walked)

    def __eq__(self, other):
        if self._name != other.get_name() or \
            self._age != other.get_age() or \
            self.get_owner_name() != other.get_owner_name():
            return False
        return True
