import random

class Weapons():

    Armory = ["Sword", "Cheese", "pistols", "Fish"]

    @staticmethod
    def Get():
        return Weapons.Armory[random.randint(0, len(Weapons.Armory)-1)]

class Character():

    def __init__(self, name, description=None):
        self.__name = name
        self.__description = description
        self.__conversation = None

    @property
    def Description(self):
        return self.__description

    @Description.setter
    def set_description(self, value):
        self.__description = value

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def set_name(self, value):
        self.__name = value

    @property
    def Talk(self):
        return "{}: {}".format(self.__name, self.__conversation)

    @Talk.setter
    def Talk(self, value):
        self.__conversation = value

    def __str__(self):
        return "I´m the {}".format(self.__name)

class Hero(Character):

    def __init__(self, name, description=None):
        super().__init__(name, description)
        self.__weapon = Weapons.Get()

    @property
    def Weapon(self):
        return self.__weapon

    @property
    def Back(self):
        return "I have a {}, i will be back with another weapon!!!!".format(self.__weapon)

    def fight(self, enemy):
        if enemy and self.Weapon == enemy.Weakness:
            return True
        return False

    def change_weapon(self):
        self.__weapon = Weapons.Get()

    def __str__(self):
        return "I´m the {} and my weapon is {}!!!".format(self.Name, self.__weapon)

class Enemy(Character):

    def __init__(self, name, description=None):
        super().__init__(name, description)
        self.__weakness = Weapons.Get()

    @property
    def Weakness(self):
        return self.__weakness

    def __str__(self):
        return "I´m the {} and my only weakness is {}!!!".format(self.Name, self.__weakness)
