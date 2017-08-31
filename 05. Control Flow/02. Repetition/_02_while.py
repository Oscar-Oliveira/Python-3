"""
while else
"""

NUMBER = 17
hit = False

while not hit:
    value = int(input("input a value: "))
    if value == NUMBER:
        hit = True
    elif value > NUMBER:
        print("your number is greater")
    else:
        print("your number is lower")
else:
    print("Winner!!!")
    