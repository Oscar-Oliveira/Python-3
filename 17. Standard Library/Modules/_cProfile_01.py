"""
cProfile
"""

import time

def Rabbit():
    print("Rabbit...")

def Turtle():
    time.sleep(3)
    print("Turtle...")

def Dog():
    time.sleep(1)
    print("Dog...")

def main():
    Rabbit()
    Turtle()
    Dog()

if __name__ == "__main__":
    main()
    