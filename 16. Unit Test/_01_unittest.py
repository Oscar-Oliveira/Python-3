"""
unittest
See: https://docs.python.org/3.6/library/unittest.html
See: https://jeffknupp.com/blog/2013/12/09/improve-your-python-understanding-unit-testing/
"""

import unittest 

class TextAnalysisTests(unittest.TestCase):

    # test cases begin with test_
    def test_function_runs(self):
        """The function run? aka 'Smoke test'"""
        multiply()

if __name__ == "__main__": 
    unittest.main()
