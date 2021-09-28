import turtle
from turtle import *

colors = ['red', 'yellow', 'blue', 'orange', 'green', 'red']
shelly = turtle.Turtle()
turtle.bgcolor('black')
for n in range(50):
    for i in range(6):
        shelly.color(colors[i])
        shelly.forward(100)
        shelly.left(60)
    shelly.right(10)

shelly.penup()
shelly.color("white")
for i in range(20):
    shelly.forward(220)
    shelly.pendown()
    shelly.circle(30)
    shelly.penup()
    shelly.backward(220)
    shelly.right(10)

shelly.hideturtle()
"""
pencil = turtle.Turtle()
pencil.speed(200)
COLOR=["purple","black","green","blue"]
for i in range(180):
    #pencil.pencolor(COLOR)
    pencil.forward(100)
    pencil.right(30)
    pencil.left(50)
    pencil.forward(20)
    pencil.left(60)
    pencil.right(10)
    pencil.forward(50)
    pencil.right(30)
    pencil.penup()
    pencil.setposition(0,0)
    pencil.pendown()
    pencil.right(2)

turtle.done()
"""
