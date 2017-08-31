"""
subprocess
See: https://docs.python.org/3/library/subprocess.html
"""

import subprocess

program = "notepad.exe"
programargs = ["ping", "www.google.com"]

subprocess.call(program)

code = subprocess.call(programargs) # arguments
print(code)
if code == 0: print("Success!")

process = subprocess.Popen(program) # new process, dows not wait.

code = subprocess.Popen(program).wait()

subprocess.Popen([program, __file__])

process = subprocess.Popen(programargs, stdout=subprocess.PIPE)
data = process.communicate()
for line in data:
    print(line, "\n")
