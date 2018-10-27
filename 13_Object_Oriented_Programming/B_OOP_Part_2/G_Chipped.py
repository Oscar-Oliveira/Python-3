"""
Class - Chipped
"""

class Chipped:

    def __init__(self, chipNumber):
        self.chip = chipNumber

    def chip(self):
        print(self.chip)

    def get_name(self):
        return "Chipped with " + str(self.chip)
