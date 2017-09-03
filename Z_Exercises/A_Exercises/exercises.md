# Python 3 - Exercises

## Exercise 1
Write a program that will display the following text on the screen.

> Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach. 

source: [https://docs.python.org/3/tutorial/index.html](https://docs.python.org/3/tutorial/index.html)

## Exercise 2
Write a program that allows a person to personalize is employee tag atb FOO BAR.

```
************************************************************
FOO BAR                                                  
************************************************************
Name:
Departement:
************************************************************
```
1. Ask the user to enter the information.
2. Display the tag to the user.
2. Make sure you correct anything typed in with incorrect case. (Ex: john doe should be John Doe).

## Exercise 3
Write a C program that convert a temperature from Fahrenheit to Centigrade. The conversion is done with the following formula:

```
C = (5/9) * (F - 32)
```
1. Ask the user to enter the Fahrenheit temperature.
2. Display the answer to the user.
3. Confirm the calculation using the following formula:

```
F = ((9.0 / 5.0) * C) + 32.0;
```
## Exercise 4
Calculate the discount on a putchase following the rules:
* purchases over 50 euros have a discount of 10%
* purchases over 25 euros have a discount of 10%
* purchases bellow 25 euros have no discount

Example:
```
Purchase value: 110.1
Discount (10.0%): 11.01
Purchase w/ discount: 110.0
``` 
1. Ask the user to enter the purchase value.
2. Display the answer to the user (as in the example).

## Exercise 5
Calculate the shipping costs following the rules:
* if the purchase is made from Portugal Continental no shipping costs are charged.
* if the purchase is made from Portugal:
    * Continental no shipping costs are charged.
    * Azores or Madeira: 5 euros
* if the purchase is made from an european country and the purchase value is higher than 50 euros:
    * 15 euros
* others:
    * 25 euros

Example:
```
Purchase value? 150
Where are you from? portugal
Are you from Azores or Madeira? [Y/N] y
Purchase value: 150.0
Shipping: 5
Purchase w/ shipping: 155.0
```
1. Ask user for the required information.
2. Display the answer to the user (as in the example).

## Exercise 6
Ask the user to enter the names of all the student in the classroom.
Then return the list in alphabetical order.

Example:
```
Student name [empty to quit]: student1
Student name [empty to quit]: student3
Student name [empty to quit]: student2
Student name [empty to quit]:

Students:
student1
student2
student3
```

## Exercise 7
Create the CSV file with the information presented below :

```
Year,Make,Model,Description,Price
1997,Ford,E350,"ac, abs, moon",3000.00
1999,Chevy,"Venture ""Extended Edition""","",4900.00
1999,Chevy,"Venture ""Extended Edition, Very Large""",,5000.00
1996,Jeep,Grand Cherokee,"MUST SELL! air, moon roof, loaded",4799.00
```

source: [https://en.wikipedia.org/wiki/Comma-separated_values](https://en.wikipedia.org/wiki/Comma-separated_values)

## Exercise 8
Using the ```cvs``` module read the previous csv data file an display the values.

## Exercise 9
Create a function to append a text in a file with two parameters (text and filename)
1. Ask user to specify the file name and text.
2. Use your function to append in the file a new line the text.

## Exercise 10
Create a function to read the text of a file (given as a parameter).
1. Ask user to specify the file.
2. Use your function to display the file content.
3. Add error handling if the file is not found.

## Exercise 11
1. Ask the teacher to enter the ending for the session. 
2. Display the time left considering the system clock.

Example:
```
Insert ending time [%H:%M]: 17:00
Current:  14:17:00
Time left:  2:43:00 
```