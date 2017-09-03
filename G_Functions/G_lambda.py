"""
lambda expressions
"""

f = lambda x: x ** (2 if x > 5 else 3)
for i in range(10):    
    print(f(i))

points = [{ 'x' : 2 , 'y' : 3 }, { 'x' : 4 , 'y' : 1 }] 
points.sort(key= lambda x: x['y']) 
print(points)

pairs = [(1, "one"), (2, "two"), (3, "three"), (4, "four")]
pairs.sort(key=lambda x: x[1])
print(pairs)
pairs.sort(key=lambda x: x[0])
print(pairs)
