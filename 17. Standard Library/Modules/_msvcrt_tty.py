"""
msvcrt and tty
- GetKey() - Detect keypress
 """

try: 
    import msvcrt # Windows
    def GetKey():
        return msvcrt.getch()
except ImportError: 
    import sys
    import tty # Unix
    import termios
    def GetKey():
        fd = sys.stdin.fileno()
        original_att = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_att)
        return ch

if __name__ == "__main__":
    print("Press a key to continue...")
    GetKey()
    print("Done.")
