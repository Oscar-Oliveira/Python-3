"""
Exercise 19
"""

import re

def print_dict(d):
    print()
    for l, c in sorted(d.items()):
        print(l, c)

def letter_count1(phrase):
    result = {}
    for l in phrase:
        if 97 <= ord(l) <= 122:
            if l in result:
                result[l] += 1
            else:
                result[l] = 1
    return result

def letter_count2(phrase):
    result = {}
    phrase = re.sub("[^a-z]+", "", phrase.lower())
    for l in phrase:
        if l.strip():
            if l in result:
                result[l] += 1
            else:
                result[l] = 1
    return result

phrase = "If the implementation is easy to explain, it may be a good idea."

r = letter_count1(phrase)
print()
print_dict(r)

r = letter_count2(phrase)
print()
print_dict(r)
