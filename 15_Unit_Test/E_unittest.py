"""
unittest
"""

import unittest
from pathlib import Path
import os

class TextAnalysisTests(unittest.TestCase):

    def setUp(self):
        self.a = 100
        self.b = 10

    def tearDown(self):
        del self.a, self.b

    def test_function_runs(self):
        self.assertEqual(multiply(self.a, self.b), 1000)

    def test_Division_runs(self):
        self.assertEqual(divide(self.a, self.b), 10)

    def test_TenLenghtString_runs(self):
        assert len(create_lenght10_string()) == 10

    def test_Division_ZeroException(self):
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

def multiply(value1, value2):
    return value1 * value2

def divide(value1, value2):
    return value1 / value2

def create_lenght10_string():
    return 'A' * 10

if __name__ == "__main__": 
    unittest.main()
