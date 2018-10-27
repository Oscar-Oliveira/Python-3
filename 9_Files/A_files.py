"""
Files
- open(FILE, ACCESS_MODE)
- ACCESS_MODE:
    - w, r, a: write, read, append
    - w+, r+, a+: write/read, read/write, append/read
    - wb, rb, ab: write, read append binary
    - wb+, rb+, ab+: write/read, read/write, append/read binary
"""

import os

file = open(os.path.realpath(__file__), "r")
content = file.read() 
print(content)
file.close()
