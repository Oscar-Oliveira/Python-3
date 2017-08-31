"""
Decorators
See: https://stackoverflow.com/questions/739654/how-to-make-a-chain-of-function-decorators/1594484#1594484
See: https://pythonconquerstheuniverse.wordpress.com/2012/04/29/python-decorators/
"""

def make_me_pretty(func):

    def wrapper(*args):
        print('-' * 20)
        print("{:^20}".format(func(*args)))
        print('-' * 20)

    return wrapper

@make_me_pretty
def add(x, y):
    return x + y

def main():
    add(3, 2)

if __name__ == "__main__":
    main()
