"""
Exercise 4
"""

def exercise(now, alarm):
    return (now + (alarm % 24)) % 12

now = 3
alarm = 62
time = exercise(now, alarm)
print(time)

# second version
now = int(input("Now time: "))
alarm = int(input("Waiting time: "))
time = exercise(now, alarm)
print(time)
