'''
threading
Note: run on terminal
'''

import random
import time
from threading import Thread

class MyThreadClass(Thread):

    def __init__(self, name):
        Thread.__init__(self)
        self._name = name
        self._duration = random.randint(2, 20)

    def run(self):
        time.sleep(self._duration)
        msg = "Done: {} in {}".format(self._name, self._duration)
        print(msg)

def main():
    for i in range(1, 6):
        name = "Thread n:{}".format(i)
        my_thread = MyThreadClass(name)
        my_thread.start()

if __name__ == "__main__":
    main()
    