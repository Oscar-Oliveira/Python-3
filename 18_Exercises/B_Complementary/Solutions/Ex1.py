"""
Exercise 1
"""

sentence1 = "Special"
sentence2 = "cases"
sentence3 = "aren't"
sentence4 = "special"
sentence5 = "enough"
sentence6 = "to"
sentence7 = "break"
sentence8 = "the"
sentence9 = "rules."

print(sentence1, sentence2, sentence3, sentence4, \
    sentence5, sentence6, sentence7, sentence8, sentence9)

print()
var = [value for key, value in sorted(globals().items()) if "sentence" in key]
print(" ".join(var))
