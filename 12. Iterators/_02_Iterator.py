"""
Iterator
"""

class RangeAZ:

    def __init__(self, max):
        if isinstance(max, int) and 0 < max <= 26:
            self.current = 65
            self.max = self.current + max
        else: raise ValueError("max parameter must be in [1..26].")

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.max:
            raise StopIteration
        value = chr(self.current)
        self.current += 1
        return value

def get_next_value(data):
    try:
        return next(data)
    except StopIteration:
        return None

iterator = iter(RangeAZ(26))

while True:
    a = get_next_value(iterator)
    if a:
        print(a, end=" ")
        continue
    break
