"""
unittest
"""

import unittest 
from pathlib import Path
import os

class TextAnalysisTests(unittest.TestCase):

    # Fixture, called before each test
    def setUp(self):
        self.a = 10
        self.b = 11
        print(">", end="")

    # Fixture, called after each test
    def tearDown(self):
        del self.a, self.b
        print("<", end="")

    def test_function_runs(self):
        print("?", end="")
        multiply(self.a, self.b)

def multiply(value1, value2):
    print("!", end="")
    return value1 * value2

if __name__ == "__main__":
    unittest.main()
