"""
sys
"""

import sys
from pprint import pprint

def my_sum(numbers):
    sum = 0
    for i in numbers:
        sum += int(i)
    return sum

print("Command line arguments:")
for i in sys.argv:
    print(i)

sys.argv.pop(0)
print("SUM: ", my_sum(sys.argv))    

print(sys.getdefaultencoding())

print(sys.version_info)
print(sys.executable)

print(sys.platform)

print()
pprint(sys.path)

print()
pprint(vars(sys))

print("Done!")

sys.exit(0)

print("You do not see me!")
