"""
Exercise 11
"""

import datetime
import time

now = datetime.datetime.now()

end = input("Insert ending time [%H:%M]: ")
end = datetime.datetime.strptime(end, "%H:%M")

now = datetime.datetime.strptime(str(now.hour) + ":"+ str(now.minute), "%H:%M")

print("Current: ", now.strftime("%H:%M:%S"))
print("End: ", end.strftime("%H:%M:%S"))

timeLeft = end - now

print("Time left: ", timeLeft)

secondsLeft = timeLeft.seconds
print("Seconds left: ", secondsLeft)

timeLeft = time.strftime("%H:%M:%S", time.gmtime(secondsLeft))
print("Time left: ", timeLeft)
