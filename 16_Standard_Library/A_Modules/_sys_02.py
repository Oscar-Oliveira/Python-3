"""
sys
- On terminal: Use powershell command $LastExitCode to see error code
"""

import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Command line arguments are missing")
    try:
        result = int(sys.argv[1])
        print(str(result * 5))
        return 0
    except:
        return 1

if __name__ == "__main__":
    sys.exit(main())
