"""
Exercise 2
"""

SYMBOL = "*"
TAGSIZE = 30
ENTERPRISE_NAME = "FOO BAR"

userName = input("Enter your name: ").title()
departement = input("Enter your departement: ").title()

tag = "\n{0}\n{1}\n{0}\nName:{2}\nDepartement:{3}\n{0}\n". \
    format(SYMBOL * TAGSIZE, ENTERPRISE_NAME, userName, departement)

print(tag)
