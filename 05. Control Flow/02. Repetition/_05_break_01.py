"""
break
"""

NUMBER = 17

for attempt in range(5): # 5 attempts
    print("Attempt {}".format(attempt + 1))
    value = int(input("input a value: "))
    if value == NUMBER:
        print("WINNER!!!!")
        break
    elif value > NUMBER:
        print("your number is greater")
    else:
        print("your number is lower")
else: # only executes if for loop exits normally
    print("You didn´t make it")
