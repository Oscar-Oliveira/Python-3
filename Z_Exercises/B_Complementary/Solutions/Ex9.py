"""
Exercise 9
"""

def day1(day):
    if day == 0: return "Sunday"
    elif day == 1: return "Monday"
    elif day == 2: return "Tuesday"
    elif day == 3: return "Wednesday"
    elif day == 4: return "Thursday"
    elif day == 5: return "Friday"
    else: return "Saturday"

def day2(day):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days[day]

print(day1(1))

print(day2(1))
