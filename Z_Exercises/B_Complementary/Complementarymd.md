# Python 3 - Complementary exercises

## Exercise 1
Store each word of the following sentece in a separate variable, then print it on one line.
> Special cases aren't special enough to break the rules. 

## Exercise 2
Add parenthesis to the expression ```a = 9 * 2 - 3 + 4 / 2``` to change its value from 17 to:
* 13.5
* -22.5

## Exercise 3
Evaluate the following expressions:
* 7 % 23
* 11 % 10
* 14 % 12
* 12 % 14
* 2 % 2
* 0 % 11
* 11 % 0

## Exercise 4
It is now 3pm and You have set an alarm to ring in 62 hours. At what time the alarm will ring?
* Second version: Ask the user for the time current hour and the number of hour to wait.

## Exercise 5
Write a program that prints 100 times the following sentence.
> Now is better than never.

## Exercise 6
Create a list of months, then write them using a for loop.

## Exercise 7
Create a list with 10 or more integer elements.
* print each of them on a new line.
* print the square of each of them.
* print the sum of all elements.
* Print the product of all elements.

## Exercise 8
Use the turtle module and the for loop to draw the following regular (all sides have the same size) polygons:
* equilateral triangle (3 sides)
* square (4 sides)
* hexagon (6 sides)
* octagon (8 sides)

## Exercise 9
Write a function which given the day number (assuming the days of the week are numbered from 0 (Sunday) to 6 (Saturday)), it returns the day name.

## Exercise 10
Given an exam mark list, write functions such that return:
* Average
* Sum of positive grades
* Average not considering the highest and lowest grade

## Exercise 11
Write a function called ```Compare(arg1, arg2)``` with two arguments ```arg1``` and ```arg2``` that returns:
* -1, if arg1 < arg2
* 0, if arg1 == arg2 
* 1, if arg1 > arg2

## Exercise 12
Write a function that returns the number of decimal digits in a positive integer given as a parameter.

## Exercise 13
Write the following functions:
* returns a string removing the symbols ```!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~``` from a given string parameter.
* returns a string reversed.
* returns a boolean value recognizing if the given string is a palindrome.

## Exercise 14
What is the result of the following code? The lists are really swapped?

```
def Swap(x, y):
    (x, y) = (y, x)

list1 = ["one", "two", "three"]
list2 = [1, 2, 3]

print(list1, list2)
Swap(list1, list2)
print(list1, list2)
```

## Exercise 15
Write one function to add vectors and another to returns the scalar multiple of a vector by a value.

Examples:
```
AddVector([1, 2, 3], [1, 2, 3]) = [2, 4, 6]
ScalarMultiple(2, [1, 2, 3]) = [2, 4, 6]
```
## Exercise 16
Create a function to generate a list containing ```n``` random integer values between a lower and an upper bound.

## Exercise 17
Write a function that receives a path to a file and writes out a new file with the lines in reversed order.

## Exercise 18
Write a funtion that reads a positive integer from the user. Raise execeptions for each case that not meet this requirement.

## Exercise 19
Write a program that returns a table of the letters (Case should be ignored) which occur in the string together with the number of times each letter occurs.

## Exercise 20 
Considering:
```
class Geometric2D():

    def get_area(self):
        """Return area"""
        raise NotImplementedError("Must implement this")

    def get_perimeter(self):
        """Return perimeter"""
        raise NotImplementedError("Must implement this")

class Rectangle(Geometric2D):

    def __init__(self, w, h):
        self.width = w
        self.height = h
    
    def __str__(self):
        return "{}x{}".format(self.width, self.height)

if __name__ == "__main__":
    r = Rectangle(15, 10)
    print(r, r.get_area(), r.get_perimeter())
    
```
* Complete the following code.
* Create a subclasse of Rectangle called Square, initializing the square with only one size. Example:
```
s = Square(10)
print(s, s.get_area(), s.get_perimeter())
```
