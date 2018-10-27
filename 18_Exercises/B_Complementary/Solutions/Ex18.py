"""
Exercise 18
"""

def pos_int():
    value = input("Enter a positive integer: ")
    try:
        value = int(value)
        if value < 0:
            raise ValueError
    except ValueError:
        print(">>>Error: Value must be a positive integer")
        return pos_int()
    return value

def main():
    pos_int()

if __name__ == "__main__":
    main()
    print("Done!")
    