"""
Exercise 13
"""

def remove_symbols1(string):
    symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    newString = ""
    for c in string:
        if c not in symbols:
            newString += c
    return newString

def remove_symbols2(string):
    return "".join(x for x in string if x not in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")

def reverse1(string):
    newString = ""
    for i in range(-1, -(len(string) + 1), -1):
        newString += string[i]
    return newString

def reverse2(string):
    return string[::-1]

def is_palindrome(string):
    s = string.upper()
    return s == reverse2(s)

print(remove_symbols1("""Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea."""))

print(remove_symbols2("""Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea."""))

print(reverse1("Python"))
print(reverse2("Python"))

print(is_palindrome("Python"))

print(is_palindrome("Level"))
