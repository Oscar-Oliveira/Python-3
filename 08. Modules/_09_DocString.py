"""
DocString
This is a dummy DocString for this module
- Execute (on script folder):
    $ python
    >>> import _10_docString
    >>> help (_10_docString)
    >>> _10_docString.my_function(1, 2)
"""

def my_function(value1, value2):
    """
    This is a reST style docstring.
    More style at:
    https://stackoverflow.com/questions/3898572/
    :param value1: this is a first param
    :param value2: this is a second param
    :returns: this is a description of what is returned
    :raises keyError: raises an exception
    """
    return value1 + value2

if __name__ == "__main__":
    print(my_function(1, 2))
    print(my_function.__doc__)
