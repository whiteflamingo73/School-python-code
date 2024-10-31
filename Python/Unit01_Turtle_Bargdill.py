###############################################################################
#     Name : Aaron Bargdill              Date: 9/17/24                        #
#     Unit 1-1 Turtle Graphics                                                #
#                                                                             #
###############################################################################

import turtle

window = turtle.getscreen()
turtle.title("Unit 01 Turtle drawings - Star")
#different turtles needed for all the problems
myturtle = turtle.Turtle()

#problem 1: creating a 5 pointed star
myturtle.forward(200)
myturtle.right(144)
myturtle.forward(200)
myturtle.right(144)
myturtle.forward(200)
myturtle.right(144)
myturtle.forward(200)
myturtle.right(144)
myturtle.forward(200)

myturtle.clear()

#problem 2: creating a rectanguloid
turtle.title("Unit 01 Turtle Drawings - Rectanguloid")
myturtle.home
myturtle.right(144)
#first rectangle
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
#second rectangle
myturtle.goto(50,50)
myturtle.left(90)
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(200)
myturtle.left(90)
myturtle.forward(100)
#creating the sides
myturtle.penup()
myturtle.goto(50,100)
myturtle.pendown()
myturtle.goto(0,100)
myturtle.left(135)
myturtle.forward(71)
myturtle.penup()
myturtle.goto(200,100)
myturtle.pendown()
myturtle.forward(71)
myturtle.penup()
myturtle.goto(200,0)
myturtle.pendown()
myturtle.forward(71)

myturtle.clear()
#Problem 3: Creating a quardanent plane with 4 shapes
turtle.title("Unit01 Turtle Drawings - Four Shapes")
#setting up positioning
myturtle.penup()
myturtle.home()
myturtle.pendown()
#quardenent plane
myturtle.forward(400)
myturtle.backward(800)
myturtle.home()
myturtle.right(90)
myturtle.forward(400)
myturtle.backward(800)
#square
myturtle.color("green")
myturtle.penup()
myturtle.goto(200,200)
myturtle.pendown()
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(100)
myturtle.penup()
myturtle.goto(205,200)
myturtle.pendown()
myturtle.write("Square", font = ("Arial", 16, "normal"))
#circle
myturtle.color("magenta")
myturtle.penup()
myturtle.goto(200,-200)
myturtle.pendown()
myturtle.circle(50)
myturtle.penup()
myturtle.goto(150,-200)
myturtle.pendown()
myturtle.write("Circle", font = ("Arial", 16, "normal"))
#triangle
myturtle.color("red")
myturtle.penup()
myturtle.goto(-200,200)
myturtle.pendown()
myturtle.forward(100)
myturtle.left(120)
myturtle.forward(100)
myturtle.left(120)
myturtle.forward(100)
myturtle.penup()
myturtle.goto(-300,200)
myturtle.pendown()
myturtle.write("Triangle", font = ("Arial", 16, "normal"))
#pentagon
myturtle.color("blue")
myturtle.penup()
myturtle.goto(-200,-200)
myturtle.pendown()
myturtle.left(120)
myturtle.forward(100)
myturtle.left(72)
myturtle.forward(100)
myturtle.left(72)
myturtle.forward(100)
myturtle.left(72)
myturtle.forward(100)
myturtle.left(72)
myturtle.forward(100)
myturtle.penup()
myturtle.goto(-300,-200)
myturtle.pendown()
myturtle.write("Pentagon", font = ("Arial", 16, "normal"))
#hiding turtle
myturtle.hideturtle()
#keeping window open:
window.mainloop()
