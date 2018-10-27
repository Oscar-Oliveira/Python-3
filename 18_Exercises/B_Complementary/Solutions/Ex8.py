"""
Exercise 8
"""

import turtle

window = turtle.Screen() 
window.bgcolor("white")
window.title("Exercise 8")

MyTurtle = turtle.Turtle()
MyTurtle.shape("blank")
MyTurtle.pensize(1)

sides = 8
rot = 360 // sides
size = 50

MyTurtle.color("black", "gray")
MyTurtle.begin_fill()
for i in range(sides):
    MyTurtle.left(rot)
    MyTurtle.forward(size)
MyTurtle.end_fill()

window.mainloop() # Wait for user input to close window
